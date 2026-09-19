# social-os — Branded Social Content OS for Franchise Businesses

**What this is.** A resellable, Claude-Cowork-native operating system that lets a
non-technical business owner get correctly-branded social content created,
approved, and published — with almost no manual work — from one Google Drive
folder and a chat window.

**First client:** Lifetime of Love Nannies (franchise location).
**Product goal:** clone it to the other ~20 Lifetime of Love markets, then to any
local service business.

---

## Start here

Read in this order. Each file says what it is for in its first line.

| # | File | Read it when |
|---|---|---|
| 1 | [`CLAUDE.md`](./CLAUDE.md) | **Always first.** How any session works this project. |
| 2 | [`PROJECT.md`](./PROJECT.md) | You need current status, paths, and what's next. |
| 3 | [`02-decisions/DECISIONS.md`](./02-decisions/DECISIONS.md) | You're about to change or question a decision. |
| 4 | [`02-decisions/OPEN-QUESTIONS.md`](./02-decisions/OPEN-QUESTIONS.md) | You're about to build on something unverified. |
| 5 | [`03-research/VERIFIED-FACTS.md`](./03-research/VERIFIED-FACTS.md) | You need ground truth, not memory. |
| 6 | [`04-architecture/STACK.md`](./04-architecture/STACK.md) | You're building or explaining the system. |
| 7 | [`05-product/`](./05-product/) | You're building the deliverable. |

## Folder map

```
social-os/
├── README.md                          ← you are here
├── CLAUDE.md                          ← operating contract for any session
├── PROJECT.md                         ← Current State table + next actions
│
├── 01-context/                        ← WHO and WHY (rarely changes)
│   ├── operator-intent.md             ← Bucho's own words + answers
│   ├── client-lifetime-of-love.md     ← the client, researched
│   └── business-model.md              ← resale, ownership, pricing
│
├── 02-decisions/                      ← WHAT we chose (changes deliberately)
│   ├── DECISIONS.md                   ← decision log + reversal triggers
│   └── OPEN-QUESTIONS.md              ← unknowns + the exact test for each
│
├── 03-research/                       ← EVIDENCE (append-only, provenance-tagged)
│   ├── VERIFIED-FACTS.md              ← the ground-truth table
│   ├── review-of-prior-findings.md    ← challenge of the uploaded research doc
│   ├── cowork-platform.md
│   ├── publishing-layer.md
│   ├── image-layer.md
│   └── nanny-industry.md
│
├── 04-architecture/                   ← HOW it's built
│   ├── STACK.md
│   └── RISKS.md
│
└── 05-product/                        ← the DELIVERABLE
    ├── client-folder-template.md
    └── skills-spec.md
```

## Licensing note

Every file here is **original work**, authored for this project. It borrows
*structural ideas* from the AIOS framework (declared/observed context split,
trust contract, decision log, index discipline) — structure is not copyrightable.
**No AIOS source files are copied into this tree**, so AIOS's GPL-2.0-or-later
does not attach to this work. See [`04-architecture/RISKS.md`](./04-architecture/RISKS.md) § Licensing.
