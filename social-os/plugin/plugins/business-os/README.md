# Business OS

A small business's whole AI workspace, in one Google Drive folder, run from chat.

**Interview once. Approve weekly. Add a room when you need one.**

Social media is the first room. Email marketing, review replies, recruiting and
invoicing are rooms you add later — without touching anything that already works,
because your brand, your offers and your logos are shared across all of them.

| Skill | What it does |
|---|---|
| `brand-onboarding` | Researches the business, interviews the owner, builds the workspace, connects accounts, drafts three posts |
| `update-the-brain` | The only safe way to change anything. Fires on every correction |
| `upgrade-workspace` | Brings a workspace to the current shape — shows the diff before changing anything |
| `housekeeping` | Monthly safety net: audits the invariants, archives, compacts |
| `plan-week` | *(social)* Plans the week across topics and both audiences from real performance |
| `draft-post` | *(social)* Writes one post in the owner's voice, stages it for approval |
| `make-graphic` | *(social)* Designs on-brand graphics in Canva Pro, resized per platform |
| `publish` | *(social)* The only skill that knows the publisher. Approve → schedule → live |
| `learn` | *(social)* Weekly: results → what works → the brain gets smarter |

Plus an independent **compliance reviewer** that reads every draft before it can be
approved, and shared **guardrails** written for childcare brands.

Connectors: Google Drive · Zernio · Canva (Pro, optional).

---

## The part that matters after month one

Anything can write a good caption. What decides whether this is still trusted in
year three is what happens the twentieth time the owner says *"no, that's wrong."*

The common failure is quiet: the assistant apologises, adjusts for the rest of the
conversation, and maybe writes a note somewhere. The document that caused the
behaviour is untouched. Tomorrow the old version is back — and now two records
disagree, with nothing to say which one wins.

So a correction here is a **write to a specific document**, and nothing less counts.
Six laws, in `shared/the-law.md`:

1. **One job, one document.** A correction replaces; it never adds a second one
   beside it. Two documents that disagree are reconciled **point by point** — never
   by picking a winner, which throws away whatever the other one got right.
2. **Rules govern, records don't.** `Told to us/` decides behaviour. `Learned by us/`
   is evidence: it can choose between things the rules allow and it can *propose* a
   rule change, but it can never make one.
3. **Precedence is ordered, not accumulated** — and a correction that lives only in
   the conversation is not a correction.
4. **A change and a correction are different things.** *"We charge more now"* leaves
   old posts honest. *"That price was always wrong"* makes them false. One question
   decides what happens to everything already published.
5. **Every change has a blast radius**, handled in the same turn — the drafts written
   in the old voice get redone, or named to her. Never left stale silently.
6. **Nothing is destroyed.** A replaced document is renamed with the date and moved
   to `9 — Archive`, never trashed — Google empties the trash after 30 days, and the
   record of what her brand voice used to be is exactly what you want on the day a
   correction turns out to have been wrong.

Enforced by `update-the-brain`, audited monthly by `housekeeping`.

## Why it stays fast as it grows

One document — **`0 — Map`** — holds every folder ID, every setting, and every rules
document with the single job it does. Every session reads it first and goes straight
to what it needs. No searching, and no walking the tree as the workspace grows from
one room to six.

It is pointers, never prose, and records are excluded — so it stays about thirty
lines forever. It is also the reason *"does a document for this job already exist?"*
is a one-read check rather than a folder sweep, which is what turns law 1 from an
intention into a check.

## Why upgrading it doesn't cause chaos

The shape of a workspace will change over the years, and there is no way to upgrade
every client at once — a workspace is only reachable when a session runs against it.
So two lanes, and putting a change in the wrong one is the only real risk:

- **Filling in what's missing** happens silently. A folder that should exist and
  doesn't isn't *her* stuff being changed; it's the system finishing building itself.
- **Anything that renames, moves, merges or retires** shows her the exact diff first
  and happens on one yes. That standard is borrowed from infrastructure tooling,
  where a visible plan before action exists because changes are risky and people need
  to know what will be created, changed or destroyed before committing.

Plus: never a breaking change in one step — expand, migrate, contract as separate
releases. Every step safe to re-run. A half-finished upgrade records itself as
`FAILED` so it can be resumed rather than guessed at. And nothing is ever deleted.

`shared/versioning.md` · `skills/upgrade-workspace/` · `migrations/`

## Setup

At client setup, paste the block in `shared/project-instructions.md` into the Cowork
project's **Project instructions**. Those are the rules that have to fire before any
skill is chosen, so they cannot live in a skill. `brand-onboarding` prints the block
at the end of setup.

## For contributors

`python3 tools/validate.py` before every release. It catches the failures that are
silent at runtime: a file reference that resolves to nothing, a relative path that
escapes its skill directory, a description too long to be read, a version that
disagrees with the marketplace entry, a migration listed but never written.

Releases go through a pull request with a version bump — that is the documented
trigger for marketplace sync, and a push straight to `main` reaches nobody.
See `shared/versioning.md`.
