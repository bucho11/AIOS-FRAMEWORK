# Growth and upkeep — how the workspace adds rooms and stays healthy

Read this before creating any folder or document the existing layout does not
already name, and whenever the owner asks for something that is not social media.

The workspace is not a social media tool that happens to use folders. It is her
**AI workspace**, and social is the first room in it. Email marketing, reviews,
caregiver recruiting, invoicing — each of those is a room that can be added later
without touching anything that already works. This file is what makes that true
instead of aspirational.

---

## 1. The shape, and why it is this shape

```
<Business> — AI Workspace/
├── 0 — Start Here            how to use it, written for her
├── 0 — Map                   every ID, setting, rule document and room —
│                             read first, every session
│
├── 1 — Brain/                ── SHARED BY EVERY ROOM ──
│   ├── Told to us/           THE RULES — only these change behaviour
│   └── Learned by us/        THE EVIDENCE — proposes, never decides
│
├── 2 — Brand Assets/         ── SHARED BY EVERY ROOM ──
│
├── 3 — Social/               ── A ROOM ──
│   ├── 1 Ideas · 2 Drafts · 3 Approved · 4 Published
│   ├── Content Calendar
│   └── Results/
│
├── 4 — <next room>/          e.g. Email · Reviews · Recruiting · Invoicing
│
└── 9 — Archive/              ── SHARED ── everything retired, from any room
```

**Two shared things, N rooms.** The brain and the brand assets are shared because
her voice, her offers and her logo do not change when the channel changes. A room
holds one domain's working material and nothing else.

**Numbers force Drive's sort order.** `0` files are the index, `1` and `2` are
shared, rooms start at `3`, and `9 — Archive` sits last. A new room takes the next
free number.

**The cap is ten, and it is deliberate.** `0` through `9`, with `0`, `1`, `2` and
`9` already spoken for — so **six rooms, ever**. That is not a limitation we
forgot to remove; it is the constraint that keeps the folder scannable. A numbered
filing system works because you never face more than about ten choices at one level;
past that you are browsing, and browsing is how a folder stops being usable.

Six rooms is more than any single business has run at once. If a seventh is ever
genuinely needed, the answer is to retire a dead room, not to add `10 —`.

**A retired number is never reused.** Retire `4 — Email` and `4` stays retired
forever; the next room takes the next free number. Her notes, an old report and an
archived document all still say "room 4" — handing that number to Invoicing makes
every one of them quietly wrong, and nothing errors. Retired numbers live in
`0 — Map` under `## Retired`.

---

## 2. Where does a new thing go?

Ask these in order and stop at the first yes. This is the router — use it instead
of inventing a location.

| Question | It goes… |
|---|---|
| Is it something **she told us** about the business, her voice, her offers or her rules? | `1 — Brain/Told to us/` |
| Is it something **we learned** from real results or her corrections? | `1 — Brain/Learned by us/` |
| Is it a **logo, photo, font, template or release form**? | `2 — Brand Assets/` |
| Is it **working material for one channel** — a draft, a calendar, a report? | that channel's **room** |
| Is it **finished and no longer live**? | `9 — Archive/` |
| Is it **none of these**? | It probably needs a **new room** — see §3 |

**Before creating anything in `1 — Brain/`, check `0 — Map` for its role.** If a
document already answers that question, you are editing it, not creating a sibling.
Two documents holding one role is the failure state this whole system is built
against (`the-law.md`, Law 1) — and it is far easier to prevent here than to
untangle in six months.

**The test that settles arguments:** place it by *the question she will ask later*,
not by where it came from. A performance report is dated, but she will ask "how did
social do?" — so it lives in `3 — Social/Results/`, not in a logs folder.

---

## 3. Adding a room (a new domain)

> Room definitions live in `${CLAUDE_PLUGIN_ROOT}/rooms/` — one file each, plus a
> template. A room is mostly **data**: the laws, the map, correction, housekeeping
> and upgrades already apply to it. Read that folder before building anything.


When she wants something the workspace does not do yet — email marketing, review
responses, caregiver recruiting — **do not bolt it into `3 — Social/`.** Give it a room.

1. **Confirm it is really a new domain**, not a new kind of social post. A new domain
   has its own audience, its own destination, and its own idea of "done."
2. **Create `N — <Plain Name>/`** at the top level, taking the next free number.
   Plain English, no jargon: `4 — Email`, `5 — Reviews`.
3. **Give it the same inner grammar** where it fits: ideas → drafts → approved →
   sent/published, plus its own `Results/`. The approve-before-anything-goes-out
   gate is not social-specific; it applies in every room.
4. **Rebuild `0 — Map`** — one row in the rooms table (what it is for, which
   connector, when it was added), plus every new folder ID. Anything installed but
   not in the map is invisible to every future session.
5. **Add its learning file** — `1 — Brain/Learned by us/What works — <Room>`. Each
   room learns separately, because what works in email is not what works on Reels.
6. **Never move or rename an existing room** to make space. Rooms are permanent
   addresses; other documents and her own memory point at them.

**Adding a room needs no migration.** It is purely additive — nothing that already
exists is touched — which makes it a MINOR release and the cheap path by design
(`${CLAUDE_PLUGIN_ROOT}/shared/versioning.md`). Only *reshaping* what she already has
is expensive, and that goes through `business-os:upgrade-workspace`, which shows her
the diff first.

**The brain does not fork — this is the single most likely way this system ever
acquires a contradiction.** A new room reads the same `Brand voice` and the same
`What we offer`. If a room genuinely needs a different voice — a recruiting room
might — that is a *section inside* `Brand voice`, not a second document.

The moment there is an "Email brand voice" beside a "Brand voice", nobody can say
which one is in force, and every future correction lands in one of the two at
random. A room adds **working material**, never a second copy of a rule. Growth goes
through `business-os:update-the-brain`, which checks this before the room is made.

---

## 4. The rule of three

When **three or more documents of the same kind** pile up loose in a folder, give
them a subfolder named for what they are — not for a date. `Results` rather than
`October`. `Testimonials` rather than `2026`.

Left alone, a folder with forty loose documents is where a system stops being
usable — and she is the one who has to look at it.

Do this **deliberately, when the third one appears**, and mention it in one line.
Never reorganise her folder silently.

---

## 5. What keeps it healthy

Two different jobs, and they run at two different speeds. Confusing them is how a
system looks maintained while quietly rotting.

**The guard runs at change time — `business-os:update-the-brain`.** A contradiction is
born the *instant* a change lands, not on the first of the month. So every write to
a rule document, every room added, every correction she makes, goes through the
guard right then: find the source, check nothing else already holds that role, fix
it, fix what was built from it, re-stamp the map. This is the load-bearing layer.

**Housekeeping runs monthly — a backstop and a janitor.** It assumes the guard is
imperfect and audits what it might have missed, then does the maintenance that has
no natural trigger:

- **The invariants still hold** — no two documents with one role, the map matches
  what is actually in Drive, no orphaned documents, no rule document whose
  `modifiedTime` says a human edited it
- **Published content ages out** to `9 — Archive/` after ~90 days, keeping the room
  small enough to scan
- **Weekly learning documents compact** into a quarterly summary once a quarter has
  passed, so `Learned by us` stays readable instead of becoming 52 files
- **Stale brain documents get flagged** — if `What we offer` has not changed in six
  months while the business plainly has, that is worth a question
- **Broken connections surface** — accounts needing reconnection, failed posts
  nobody retried
- **Drift gets named, never silently fixed** — loose files, rooms that stopped being
  used, a registry that no longer matches reality

**Housekeeping reports and proposes. It does not reorganise her folder on its own.**
Her workspace is hers; a system that rearranges her things without asking is one
she stops trusting.
