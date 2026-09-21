# AIOS lineage — what we took, and where each piece lives

> Answers: *"how does AIOS play into this — is it just the Drive folder?"*
> **No. AIOS contributes two things, and they live in two different places.**

---

## The mistake worth avoiding

It is tempting to say *"the AIOS structure = the Drive folder we sell."*
That is half right and it is the dangerous half.

**A folder is dead on its own.** Anyone can make folders named `Brand voice` and
`What works`. What makes AIOS compound is not its structure — it is the
**rituals** that keep the structure honest month after month: the discipline that
routes a new fact to the right file, updates the observed layer at the end of a
session, and stops the whole thing quietly drifting into stale noise.

So AIOS splits across our product:

| AIOS contributes | Lives in | Who owns it |
|---|---|---|
| **The structure** — where knowledge goes | **Her Google Drive folder** | Client |
| **The rituals** — what keeps it alive | **Our skills, in the plugin** | Operator |

**Structure without rituals is a filing cabinet. Rituals without structure have
nowhere to write. You need both, and they ship separately.**

---

## The mapping, piece by piece

| AIOS | → | Our product | Where |
|---|---|---|---|
| `context/declared/` (about_me, personal_voice, about_business) | → | `1 Brain/Told to us/` — About the business · Brand voice · Who we talk to · What we offer | **Drive** |
| `context/observed/` (patterns, preferences, growth) | → | `1 Brain/Learned by us/` — What works · Her preferences · History | **Drive** |
| **`INTENT.md`** — the trust contract, autonomy per domain | → | `Rules for the AI.md` — what it may do alone, what needs a yes | **Drive** |
| **`CLAUDE.md`** — behavioral contract loaded every session | → | **The skills themselves.** She never reads a contract; the behavior is baked into what runs. | **Plugin** |
| Session-end ritual — update observed context, never skip | → | The **`learn`** skill + the weekly scheduled task | **Plugin** |
| `/today`, `/close-day` — daily/weekly rhythm | → | Two **Cowork scheduled tasks** — weekly plan, weekly report | **Plugin** |
| Commands (`/aios:*`) | → | **Skills** she triggers in plain language | **Plugin** |
| **File Placement Router** — route by the question you'll ask later | → | The router in **`growth-and-upkeep.md`**, plus the numbered flow `1 Ideas → 2 Drafts → 3 Approved → 4 Published` inside each room | **Plugin + Drive** |
| **Folder-birth rule (rule of 3)** | → | Same rule, same threshold, in `growth-and-upkeep.md` | **Plugin** |
| **Bespoke rooms are legitimate** | → | **Rooms.** A new domain takes the next number and never disturbs an existing one | **Plugin + Drive** |
| **`/aios:housekeeping`** — 28 audit buckets | → | The **`housekeeping`** skill — archive, compact, flag staleness, check the registry, name drift. Reports; never rearranges. | **Plugin** |
| **`/aios:compact`** — monthly digest + archive | → | Quarterly compaction of weekly learning notes, inside `housekeeping` | **Plugin** |
| **INTENT.md recalibration** — trust grows with evidence | → | `housekeeping` offers, once and by category, when she has approved everything for months | **Plugin** |
| Snapshot-before-edit, `updated:` stamps | → | Simplified away. Git history is ours; **hers is the live file.** | — |
| Anti-values (never a to-do list, sycophancy kills trust) | → | The **`guardrails`** skill, plus honest-voice rules in `brand-onboarding` | **Plugin** |

---

## What we deliberately dropped

AIOS is built for a **technical operator** with a terminal, git, Obsidian and
slash commands. Our user is a **nanny franchise owner who will never open a
terminal.**

So we kept the ideas and threw away the machinery:

- ❌ Git, commits, snapshots, `aios-commit`
- ❌ Obsidian, wiki-links, graph view
- ❌ Slash commands, spawn, MCP profiles, agent bundles
- ❌ `_index.md` per folder — too much upkeep for a non-technical owner. **One registry instead:** `0 — What's Installed`, maintained by Claude, read by her.
- ❌ Current State tables, roadmap keys, truth-surface resolution order
- ❌ Framework vocabulary entirely — she never sees the words "declared",
  "observed", "context layer" or "ritual"

**That is a translation, not a copy** — which is also what keeps us clear of
AIOS's GPL (DEC-008). We took patterns, which are not copyrightable. We wrote
every file ourselves.

---

## The one idea that matters most

From AIOS's own framing: *the quality of context the operator gives an AI entirely
determines what it can do for them.*

Everything else here — Zernio, Canva, the plugin, the folder — is plumbing that
many people could assemble. **The compounding context layer is the product.**
`What works.md` getting smarter every week is the only part a competitor cannot
copy by reading our repo, because it is built from her data over her months.

---

## So: where does everything live?

```
AIOS-FRAMEWORK repo  (this one)
  └─ the teacher. Never shipped. Read for patterns only.
  └─ social-os/ = our private thinking: research, decisions, specs

PLUGIN repo  (to be minted)
  └─ what ships. The RITUALS.
     skills/ · marketplace.json · the Drive folder template

HER GOOGLE DRIVE
  └─ her instance. The STRUCTURE, filled with her knowledge.
     Created from the template at setup. She owns it.

ZERNIO + CANVA
  └─ the hands. Not AIOS at all — just the tools the rituals drive.
```

**AIOS is the teacher, not the product.** It never ships to a client, is never
copied, and is never mentioned to her. It taught us the shape.
