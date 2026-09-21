#!/usr/bin/env python3
"""caption_scan.py - deterministic scan for the mechanical AI-writing tells in a caption.

Covers the pattern-matchable slice of checks 11-14 and 16 in
references/checks.md. The judgement half (emotion mode, shape convergence,
polished-but-empty) is not catchable here and stays with the skill.

    python3 caption_scan.py caption.txt
    cat caption.txt | python3 caption_scan.py -
    python3 caption_scan.py --json caption.txt

Exit 0 always: these are needs-a-look, never blocking. The caller fixes and re-runs.

IF THIS SCRIPT DOES NOT RUN in your environment, do not treat that as a pass.
Report the checks as `SKIP - scanner unavailable, read manually` and read for the
same patterns yourself. See shared/proof.md.

Two deliberate differences from the upstream scanner this is informed by
(NulightJens/humanizer-stack, MIT - see ATTRIBUTION.md), both measured:

  1. ANTITHESIS MATCHES CONTRACTIONS. A pattern anchored on the literal string
     "not just" cannot match "isn't just" - the letters n-o-t do not occur in
     that word - so every contracted form passes clean. Social copy runs on
     contractions. Measured: upstream caught 2 of 5 realistic variants.
  2. THE CLOSER ALTERNATION IS WIDE. "That's not just a nanny, that's a partner"
     must fail. Upstream accepts only it's|but.
"""

import argparse, json, re, sys

# "not" or a contracted negative ("isn't", "aren't", "wasn't", "ain't", "don't")
NEG = r"(?:\bnot\b|\b(?:is|are|was|were|ai|do|does|did|wo|ca)n[''`]?t\b)"
# what can carry the assertion half
CLOSER = r"(?:it|that|this|they|we|you|he|she)\s*[''`]?(?:s|re)\b|\bit\s+is\b|\bbut\b"

RULES = [
    ("antithesis", "The negate-then-assert cadence",
     "Lead with the real claim and drop the negation. If what's left is thin, that's the actual problem.",
     [rf"{NEG}\s+(?:just|only|merely|simply)\b[^.!?;]{{1,60}}[,.]?\s*(?:{CLOSER})",
      r"\bnot\s+only\b[^.!?;]{1,60},?\s*but\b",
      r"\bnot\s+because\b[^.!?;]{1,60}[.,]\s*because\b"]),

    ("hype", "Marketing cliche that says nothing checkable",
     "Write what it literally does. 'Most families meet three candidates in the first week' is checkable.",
     [r"\btransform(?:ing|s)?\s+your\b", r"\bsupercharge\b", r"\bunleash\b",
      r"\beffortlessl?y?\b", r"\breimagined\b", r"\bgame[- ]?changer\b",
      r"\bunlock(?:ing)?\s+(?:your|the|its)?\s*(?:full\s+)?potential\b",
      r"\b(?:deep[- ]dive|dive\s+in|let[''`]?s\s+dive)\b", r"\bdelv\w+\b",
      r"\belevate\s+your\b", r"\bin\s+today[''`]?s\s+(?:fast[- ]paced|digital)\s+world\b",
      r"\bworld[- ]class\b", r"\bcutting[- ]edge\b", r"\brevolutionary\b",
      r"\bbest[- ]in[- ]class\b", r"\bseamless(?:ly)?\b", r"\bempower(?:ing|s)?\b",
      r"\btake\s+(?:your|it|things)?\s*[^.!?]{0,30}to\s+the\s+next\s+level\b"]),

    ("servile", "Sycophantic opener or signposted wrap-up",
     "Start on the real point and end on the real point.",
     [r"\bgreat\s+question\b", r"\bi\s+hope\s+this\s+helps\b",
      r"\bin\s+conclusion\b", r"\bin\s+summary\b",
      r"\bat\s+the\s+end\s+of\s+the\s+day\b", r"\bultimately,\s"]),

    ("vague", "Allusion where a name belongs",
     "Name it, date it, price it - or cut it. Then check the new specific against What we offer.",
     [r"\b(?:experts?|researchers?|scientists?|professionals?|specialists?)\s+(?:say|agree|believe|argue|warn|suggest|recommend)\b",
      r"\bstudies\s+(?:show|suggest|have\s+shown|indicate)\b",
      r"\bresearch\s+(?:shows|suggests|indicates)\b",
      r"\ba\s+(?:famous|popular|well[- ]known|renowned|leading|prominent|trusted)\s+\w+",
      r"\bsome\s+(?:people|parents|families|critics|folks)\s+(?:say|argue|believe|claim)\b",
      r"\bit[''`]?s\s+(?:often|widely|commonly)\s+(?:said|believed|known)\b",
      r"\bas\s+the\s+(?:old\s+)?saying\s+goes\b"]),

    ("embodied", "Emotion performed through the body instead of named",
     "Name the feeling: 'honestly, that first day scared her'. One earned embodied moment per post, at most.",
     [r"\b(?:my|his|her|their|your|the)\s+(?:chest|throat|jaw|stomach|gut|shoulders?|heart)\s+(?:tighten|clench|knot|drop|sink|sank|sag|seize|twist|churn|pound|hammer|race|lurch|skip)\w*",
      r"\b(?:breath|breathe)\w*\s+(?:caught|hitched|stalled)\b",
      r"\bcaught\s+(?:my|his|her|their)\s+breath\b",
      r"\ba\s+knot\s+(?:of\s+\w+\s+)?in\s+(?:my|his|her|their)\b",
      r"\bpit\s+of\s+(?:my|his|her|their)\s+stomach\b",
      r"\bswallow(?:ed|ing)?\s+hard\b",
      r"\b(?:hands?|voice)\s+(?:trembl|shak|shook|quiver)\w*",
      r"\bbreath\s+(?:she|he|they|I)\s+(?:didn[''`]?t|hadn[''`]?t)\s+(?:know|realize)\w*",
      r"\bsomething\s+(?:in\s+(?:my|his|her|their)\s+\w+\s+)?(?:shift|loosen|settle|unclench)\w*",
      r"\ba\s+weight\s+(?:lift|off)\w*"]),
]

EM_DASH_LIMIT = 1
EM_DASH_RE = re.compile(r"\w\s*[—–]\s*\w")


def scan(text):
    lines = text.splitlines() or [""]
    hits = {}
    for rid, label, fix, pats in RULES:
        found = []
        for i, line in enumerate(lines, 1):
            if "scan-ignore" in line:
                continue
            for p in pats:
                m = re.search(p, line, re.I)
                if m:
                    found.append({"line": i, "match": m.group(0).strip(), "text": line.strip()[:110]})
                    break
        if found:
            hits[rid] = {"label": label, "fix": fix, "hits": found}

    dashes = [{"line": i, "match": m.group(0), "text": l.strip()[:110]}
              for i, l in enumerate(lines, 1) if "scan-ignore" not in l
              for m in [EM_DASH_RE.search(l)] if m]
    words = len(text.split())
    if len(dashes) > EM_DASH_LIMIT:
        hits["em_dash"] = {
            "label": f"{len(dashes)} em dashes (limit {EM_DASH_LIMIT} in a caption)",
            "fix": "A comma, a full stop, or brackets. Not a colon. Keep one only if Brand voice says it is hers.",
            "hits": dashes}
    return {"words": words, "categories": hits,
            "total": sum(len(v["hits"]) for v in hits.values())}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    out = {}
    for f in a.files:
        text = sys.stdin.read() if f == "-" else open(f, encoding="utf-8").read()
        out[f] = scan(text)

    if a.json:
        print(json.dumps(out, indent=2))
        return

    for name, r in out.items():
        print(f"\n=== {name} ({r['words']} words) ===")
        if not r["categories"]:
            print("  no mechanical tells found."
                  "\n  Emotion mode, shape convergence and polished-but-empty are NOT"
                  "\n  checked here - they need a reader. See skills/sounds-human/.")
            continue
        for rid, c in r["categories"].items():
            print(f"\n  [{rid}] {c['label']}  ({len(c['hits'])})")
            print(f"    fix: {c['fix']}")
            for h in c["hits"][:6]:
                print(f"    L{h['line']}: \"{h['match']}\"  |  {h['text']}")
            if len(c["hits"]) > 6:
                print(f"    ... and {len(c['hits']) - 6} more")
        print(f"\n  {r['total']} hit(s). All needs-a-look: fix them, then re-run.")
        print("  Not checked here: emotion nuance, shape convergence, empty-but-clean.")


if __name__ == "__main__":
    main()
