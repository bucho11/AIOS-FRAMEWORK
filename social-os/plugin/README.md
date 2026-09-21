# Business OS — marketplace

This folder is a complete Claude plugin marketplace. Its contents are the root of
the public repo **`github.com/bucho11/social-os`** — mirror this folder there on
every change.

*(The repo keeps the name it was created with. Renaming it is outward-facing and
GitHub redirects make it safe to do later, so it stays the operator's call. The
marketplace works regardless of what the plugin inside is named.)*

```
plugin/                              ← the repo root
├── .claude-plugin/marketplace.json  ← the catalog clients sync
├── tools/validate.py                ← gates every release
└── plugins/business-os/             ← the plugin
    ├── .claude-plugin/plugin.json   ← name, version (semver)
    ├── .mcp.json                    ← zernio · canva · google-drive
    ├── CHANGELOG.md                 ← Keep a Changelog; one entry per release
    ├── shared/                      ← the laws, the map, conventions, versioning
    ├── skills/                      ← 9 skills, each SKILL.md + references/
    ├── rooms/                       ← room definitions as data + a template
    ├── migrations/                  ← ordered workspace shape changes
    ├── agents/compliance-reviewer.md
    ├── hooks/hooks.json             ← optional PreToolUse safety net (OQ-014)
    └── evals/evals.json             ← 18 prompts
```

## Shipping a release

**Never push straight to `main`.** It is documented that *"direct pushes to the
default branch don't trigger a sync"* and that auto-sync fires *"when a pull request
that includes a plugin version bump is merged."* A push without a bump reaches
nobody.

```bash
git checkout -b release/vX.Y.Z
# make the change
# bump "version" in plugins/business-os/.claude-plugin/plugin.json
#   and the matching marketplace entry — keep them equal
# add the CHANGELOG.md entry: Added / Changed / Deprecated / Removed / Fixed / Security
python3 tools/validate.py          # must print PASS
git commit -am "feat: <what changes for the owner>"
git push -u origin release/vX.Y.Z
# open the PR, merge it
```

Then run it in your own workspace before a client sees it. That is the whole canary
process at this scale, and it costs nothing.

To move a client onto a release the same day: *"open Plugins, find Business OS,
click Update."* One sentence.

## What the validator catches

The failures that are **silent at runtime** — the skill runs, just without its
guardrails, and nothing errors:

- a `${CLAUDE_PLUGIN_ROOT}` reference that resolves to nothing
- a relative path that escapes its own skill directory
- a skill name that doesn't match its directory, or a description over 1024 chars
- `plugin.json` and the marketplace entry disagreeing on name or version
- a migration listed but not written, out of sequence, missing a required section,
  or with no step stating how to tell whether it already ran
- a version with no CHANGELOG entry

This repo has already shipped two bugs of exactly that class. Run it every time.

## Licensing, before you resell this

`LICENSE` is MIT for this repository's own work. **`ATTRIBUTION.md` is the one to read
before white-labelling**, because a few parts adapt other people's work and one
upstream lineage carries a **share-alike** obligation.

The short version: we deliberately did **not** vendor the general-purpose humanizer
skill whose pattern catalogue traces to Wikipedia's CC BY-SA 4.0 material, and wrote
our own childcare-scoped checks instead. Full reasoning, credits and the two upstream
scanner defects we found while testing are in `ATTRIBUTION.md`.

## Changing the shape of a workspace

Read `plugins/business-os/shared/versioning.md` first. The short version:

- **Two version numbers.** The plugin's is semver in git. The workspace's is an
  integer in her `0 — Map`. They do not move together.
- **Never a breaking change in one step** — expand, migrate, contract, as separate
  releases.
- **Additive changes need no migration.** A new room is a MINOR release and touches
  nothing that already exists. That is the cheap path by design.
- **Anything that renames, moves, merges or retires** gets a migration in
  `migrations/`, and `upgrade-workspace` shows the owner the exact diff before it
  touches anything.
- **Nothing is ever deleted.** Superseded, dated, moved to `9 — Archive/`.
