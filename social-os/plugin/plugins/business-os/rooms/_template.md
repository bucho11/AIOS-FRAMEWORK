# <Room name>

**Number:** `N`
**Connector:** <service, or none>
**Added:** <plugin version>

## What it's for

One paragraph, in the owner's language. What work happens here and what "done"
looks like.

## Folders

```
N — <Room name>/
├── 1 Ideas/
├── 2 Drafts/          nothing leaves from here
├── 3 Approved/        she said yes
├── 4 Sent/            went out, with the evidence
├── Templates/         the toolbox — created when the first one is needed
│   └── INDEX.md       one line per file, so nothing is rebuilt unknowingly
│                      names say what a file is — never a date or a version
├── Examples/          work she approved, each with WHY it was good (best 10)
└── Results/
```

`Templates/` and `Examples/` are **created on first use, not at setup** — the
folder-birth rule. An empty folder at onboarding is clutter; a folder that appears
the day it holds something is a system that grew.

Keep the `ideas → drafts → approved → sent` grammar wherever it fits. It is not
social-specific, and the approval gate applies in every room.

## Playbooks

One row per job in this room. Every job declares whether we wrote it or she did —
an **interviewed** playbook is hers and no upgrade may rewrite it
(`${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md`).

| Job | Skill | Origin | Checks |
|---|---|---|---|
| | | shipped \| interviewed | `skills/<job>/references/checks.md` |

## Skills

| Skill | What it does |
|---|---|

## What it reads from the brain

Which `Told to us/` documents govern this room. **It reads the shared ones** —
list them; do not create copies.

## What it learns

`1 — Brain/Learned by us/What works — <Room>` — one per room, because what works in
email is not what works on Reels.

## Definition of done

What "finished" means for this room's main job, concretely enough that a check could
test it.

## Proof

Five to ten checks per job, each able to fail, producing external evidence before the
work reaches her (`${CLAUDE_PLUGIN_ROOT}/shared/proof.md`). Name which are
**blocking** — keep that list short, and only for failures she would want stopped
even at the cost of missing a send.

## Guardrails

Anything domain-specific and non-negotiable. Regulatory limits, claims that may not
be made, things that must never be sent automatically.

## Setup

What the owner must connect or provide before this room works.
