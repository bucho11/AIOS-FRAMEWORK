# Brain layout — the owner's Drive folder

One folder per business. Plain-English names on purpose: the owner has to
understand it at a glance forever, without training. Numbers force Drive's sort
order.

```
<Business> — AI Workspace/
├── 0 — Start Here                  (Doc) how to talk to it, written for her
├── 0 — Map                         (Doc) every ID, every setting, every rule
│                                         document and its role — read first,
│                                         every session. Written for the AI.
│
├── 1 — Brain/                      ── SHARED BY EVERY ROOM ──
│   ├── Told to us/                 THE RULES. Only these change behaviour.
│   │   ├── About the business
│   │   ├── Brand voice
│   │   ├── Who we talk to          families AND caregivers — two audiences
│   │   ├── What we offer
│   │   ├── Colors and fonts        replaces Canva Brand Kit on Pro
│   │   ├── Rules for the AI        what it may do alone, what needs a yes
│   │   └── How she likes to work   how she wants to be worked with
│   └── Learned by us/              THE EVIDENCE. Never changes behaviour.
│       ├── What works — Social (current)     rolling, replaced weekly
│       ├── What works — YYYY-Www             one per week, never replaced
│       ├── What works — YYYY Q#              quarterly compaction (housekeeping)
│       └── History                           dated log of every change
│
├── 2 — Brand Assets/               ── SHARED BY EVERY ROOM ──
│   ├── Logos/   Photos/   Templates/
│   └── Photo releases/             gates any content with a real child
│
├── 3 — Social/                     ── THE FIRST ROOM ──
│   ├── 1 Ideas/ 2 Drafts/ 3 Approved/ 4 Published/
│   ├── Content Calendar            (Doc) the truth surface for the week
│   ├── Templates/                  the toolbox — appears when first needed
│   ├── Examples/                   approved work that worked, with why (best 10)
│   └── Results/                    weekly performance reports
│
├── 4 — <next room>/                Email · Reviews · Recruiting · Invoicing …
│                                   (rooms 4–8; see `${CLAUDE_PLUGIN_ROOT}/rooms/`)
│
└── 9 — Archive/                    ── SHARED ── retired from any room
```

**Two shared things, N rooms.** The brain and the brand assets are shared because
her voice and her logo do not change when the channel does. Each room holds one
domain and nothing else. Adding a room never touches a room that already works —
the rules are in `growth-and-upkeep.md`, and every skill that creates a folder or a
document reads it first.


## The `0 — Map` doc

**Created by `brand-onboarding`, read first by every other skill, every session.**
It holds every folder ID, every setting, and every rule document with the one role
it holds — so a skill goes straight to what it needs instead of searching, and so
"is there already a document that does this job?" is answerable in one read.

It also carries `workspace_version` — the **shape** her folder is in, which is not
the plugin's version and does not move with it
(`${CLAUDE_PLUGIN_ROOT}/shared/versioning.md`) — plus the upgrade history and the
list of retired names.

Its exact format, how to read it, how to heal a stale ID, what must always be true
about it, and when to rebuild it all live in **`the-map.md`** — one file, so the
format cannot drift.

It replaces the `0 — Setup` and `0 — What's Installed` documents earlier versions
used. Two index documents can disagree about where the drafts are. One cannot.

If a value the map needs is missing, the skill that needs it asks the owner once,
then re-stamps the map (per `drive-conventions.md`) so nobody asks again.


## Why this shape

- **`Told to us` / `Learned by us` is the contradiction firewall.** Hers and
  Claude's — and only hers *decides anything*. `Learned by us` holds evidence: it
  can choose between things the rules allow, never change what is allowed. When
  results suggest a rule should change, Claude **proposes it and she says yes**, and
  it goes into `Told to us` where it belongs. That is why there is no second file
  quietly steering the voice. See `the-law.md`.
- **One role, one document.** There is exactly one document for how she sounds. A
  correction replaces it; it never adds a note beside it. Every role is listed in
  `0 — Map`, which is what makes the rule checkable instead of aspirational.
- **`1 Ideas → 4 Published`** is an approval gate you can *see*. A file physically
  moving is an obvious act.
- **`Photo releases/`** turns a legal rule into a file Claude can check.
- **`Colors and fonts`** exists because Canva's Brand Kit is Enterprise-only; the
  hex values living here is what lets Canva Pro produce on-brand output.
- **`Templates/` and `Examples/` are per room, and they appear when first needed.**
  A template is anything that got rebuilt from scratch after existing before; an
  example is work she approved, carrying the reason it worked. Both are a job's
  working material, which is why they live in the room rather than in the shared
  brand assets. Empty folders at setup would be clutter — the folder-birth rule says
  a folder appears the day it holds something
  (`${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md`).
- **`How she likes to work`** is a rule document, not a notes file. Earlier versions
  kept corrections in `Learned by us/Her preferences` — a document about how to
  write, sitting beside `Brand voice`, another document about how to write. Two
  sources, one role: exactly the failure this system is built to prevent. Retired.
  Voice corrections now go into `Brand voice`; permissions into `Rules for the AI`;
  how she wants to be worked with, here.
