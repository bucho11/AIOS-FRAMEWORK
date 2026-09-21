#!/usr/bin/env python3
"""Validate the Business OS plugin before release.

Catches the failure classes that have actually bitten this repo:
  - a file reference that resolves to nothing (silent: the skill just runs
    without its guardrails)
  - a relative path that escapes its own skill directory (the same, worse)
  - a skill description too long to be read, or a name that can't be matched
  - plugin.json and the marketplace entry disagreeing about the version
  - a migration listed but not written, or written but not listed

Run: python3 tools/validate.py     Exit 0 = safe to release.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
PLUGIN = os.path.join(ROOT, "plugins", "business-os")
errors, warnings = [], []


def err(m): errors.append(m)
def warn(m): warnings.append(m)


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm, out, key = m.group(1), {}, None
    for line in fm.splitlines():
        if re.match(r"^\w[\w-]*:", line):
            key, _, rest = line.partition(":")
            out[key.strip()] = rest.strip()
        elif key and line.strip():
            out[key] = (out.get(key, "") + " " + line.strip()).strip()
    return out


# ---------- 1. JSON is parseable ----------
jsons = {}
for rel in [".claude-plugin/marketplace.json",
            "plugins/business-os/.claude-plugin/plugin.json",
            "plugins/business-os/.mcp.json",
            "plugins/business-os/hooks/hooks.json",
            "plugins/business-os/evals/evals.json"]:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        err(f"missing file: {rel}")
        continue
    try:
        jsons[rel] = json.loads(read(p))
    except json.JSONDecodeError as e:
        err(f"{rel}: invalid JSON — {e}")

mkt = jsons.get(".claude-plugin/marketplace.json")
plg = jsons.get("plugins/business-os/.claude-plugin/plugin.json")

# ---------- 2. Versions agree, and are semver ----------
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
if plg:
    v = plg.get("version")
    if not v:
        err("plugin.json: no version — the marketplace sync is triggered by a version bump")
    elif not SEMVER.match(v):
        err(f"plugin.json: version {v!r} is not semver MAJOR.MINOR.PATCH")
    if mkt:
        entries = mkt.get("plugins", [])
        if len(entries) != 1:
            warn(f"marketplace lists {len(entries)} plugins; this check assumes one")
        for e in entries:
            if e.get("version") and e["version"] != v:
                err(f"version mismatch: plugin.json {v} vs marketplace entry {e['version']}")
            if e.get("name") != plg.get("name"):
                err(f"name mismatch: plugin.json {plg.get('name')!r} vs marketplace {e.get('name')!r}")
            src = (e.get("source") or "").rstrip("/")
            if src and not os.path.isdir(os.path.join(ROOT, src)):
                err(f"marketplace source {src!r} is not a directory")

# ---------- 3. Every ${CLAUDE_PLUGIN_ROOT} reference resolves ----------
md_files = []
for dirpath, dirnames, filenames in os.walk(PLUGIN):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    md_files += [os.path.join(dirpath, f) for f in filenames if f.endswith(".md")]

REF = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\s)`\"']+)")
for f in md_files:
    text = read(f)
    rel_f = os.path.relpath(f, ROOT)
    for target in set(REF.findall(text)):
        target = target.rstrip(".,;:")
        if not os.path.exists(os.path.join(PLUGIN, target)):
            err(f"{rel_f}: ${{CLAUDE_PLUGIN_ROOT}}/{target} does not exist")

# ---------- 4. No relative path escapes its own skill directory ----------
ESCAPE = re.compile(r"[(`]\.\./")
for f in md_files:
    if "/skills/" not in f:
        continue
    for i, line in enumerate(read(f).splitlines(), 1):
        if ESCAPE.search(line):
            err(f"{os.path.relpath(f, ROOT)}:{i}: relative path escapes the skill "
                f"directory — use ${{CLAUDE_PLUGIN_ROOT}}")

# ---------- 5. Skill frontmatter ----------
skills_dir = os.path.join(PLUGIN, "skills")
skill_names = set()
for name in sorted(os.listdir(skills_dir)):
    d = os.path.join(skills_dir, name)
    if not os.path.isdir(d):
        continue
    p = os.path.join(d, "SKILL.md")
    if not os.path.exists(p):
        err(f"skills/{name}/: no SKILL.md")
        continue
    fm = frontmatter(read(p))
    if fm is None:
        err(f"skills/{name}/SKILL.md: no YAML frontmatter")
        continue
    n, desc = fm.get("name", ""), fm.get("description", "").lstrip("> ").strip()
    skill_names.add(n)
    if n != name:
        err(f"skills/{name}/SKILL.md: name {n!r} does not match its directory")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", n or ""):
        err(f"skills/{name}/SKILL.md: name {n!r} must be lowercase letters, digits, hyphens (1-64)")
    if len(desc) > 1024:
        err(f"skills/{name}/SKILL.md: description is {len(desc)} chars, max 1024")
    if len(desc) < 80:
        warn(f"skills/{name}/SKILL.md: description is only {len(desc)} chars — "
             f"it is the only thing that decides whether the skill ever fires")

# ---------- 6. Cross-references to skills point at skills that exist ----------
INVOKE = re.compile(r"business-os:([a-z0-9-]+)")
for f in md_files:
    for target in set(INVOKE.findall(read(f))):
        if target not in skill_names:
            err(f"{os.path.relpath(f, ROOT)}: refers to business-os:{target}, which is not a skill")

# ---------- 7. Migrations: listed <-> written, numbered in sequence ----------
mig_dir = os.path.join(PLUGIN, "migrations")
if os.path.isdir(mig_dir):
    files = sorted(f for f in os.listdir(mig_dir)
                   if re.match(r"^\d{3}-.*\.md$", f))
    index = os.path.join(mig_dir, "_index.md")
    if not os.path.exists(index):
        err("migrations/: no _index.md")
    else:
        idx = read(index)
        for f in files:
            if f not in idx:
                err(f"migrations/{f} exists but is not listed in _index.md")
        for ref in set(re.findall(r"`(\d{3}-[a-z0-9-]+\.md)`", idx)):
            if ref not in files:
                err(f"migrations/_index.md lists {ref}, which does not exist")
    for i, f in enumerate(files, 1):
        if int(f[:3]) != i:
            err(f"migrations/: {f} breaks the sequence — expected {i:03d}-…")
        body = read(os.path.join(mig_dir, f))
        for needed in ("**To version:**", "**Lane:**", "## Steps", "## Rollback"):
            if needed not in body:
                err(f"migrations/{f}: missing required section {needed!r}")
        if "Already ran?" not in body:
            err(f"migrations/{f}: no step says how to tell if it already ran — "
                f"an unresumable migration is one interruption from an unrepairable workspace")

# ---------- 8. CHANGELOG has an entry for this version ----------
ch = os.path.join(PLUGIN, "CHANGELOG.md")
if not os.path.exists(ch):
    err("plugins/business-os/CHANGELOG.md is missing")
elif plg and plg.get("version") and f"[{plg['version']}]" not in read(ch):
    err(f"CHANGELOG.md has no entry for [{plg['version']}] — "
        f"a release nobody can read about is a release nobody trusts")

# ---------- report ----------
for w in warnings:
    print(f"  warn  {w}")
for e in errors:
    print(f"  FAIL  {e}")
print(f"\n{len(md_files)} markdown files - {len(skill_names)} skills - "
      f"{len(errors)} errors, {len(warnings)} warnings")
print("PASS — safe to release" if not errors else "FAILED — do not release")
sys.exit(1 if errors else 0)
