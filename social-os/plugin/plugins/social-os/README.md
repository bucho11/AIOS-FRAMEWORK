# Social OS

Branded Instagram + Facebook content that runs itself — from one Google Drive
folder and a chat.

**Interview once. Approve weekly. Everything else is handled.**

| Skill | What it does |
|---|---|
| `brand-onboarding` | Researches the business, interviews the owner, builds the Drive brain, connects accounts, drafts three posts |
| `plan-week` | Plans the week across topics and both audiences from real performance |
| `draft-post` | Writes one post in the owner's voice, stages it for approval |
| `make-graphic` | Designs on-brand graphics in Canva Pro, resized per platform |
| `publish` | The only skill that knows the publisher. Approve → schedule → live |
| `learn` | Weekly: results → what works → the brain gets smarter |
| `update-the-brain` | The only safe way to change anything. Fires on every correction |
| `housekeeping` | Monthly safety net: audits the invariants, archives, compacts |

Plus an independent **compliance reviewer** that reads every draft before it can be
approved, and shared **guardrails** written for childcare brands.

Connectors: Google Drive · Canva (Pro) · Zernio.

---

## The part that matters after month one

Anything can write a good caption. What decides whether this is still trusted in
year three is what happens the twentieth time the owner says *"no, that's wrong."*

The common failure is quiet: the assistant apologises, adjusts for the rest of the
conversation, and maybe writes a note somewhere. The document that caused the
behaviour is untouched. Tomorrow the old version is back — and now there are two
records that disagree, with nothing to say which one wins. By month six nobody can
explain why it does what it does.

So this plugin treats a correction as a **write to a specific document**, and
nothing less counts:

- **One job, one document.** There is one document for how she sounds. Forever. A
  correction replaces it; it never adds a second one beside it.
- **Rules govern, records don't.** `Told to us/` decides behaviour.
  `Learned by us/` is evidence — it can pick between things the rules already allow,
  and it can *propose* a rule change, but it can never make one.
- **A correction that lives only in the conversation is not a correction.**
- **Every change has a blast radius**, handled in the same turn — the drafts already
  written in the old voice get redone, or named to her. Never left stale silently.
- **She changes the system by talking, not by editing.** Before replacing anything,
  the file's `modifiedTime` is checked against its own `createdTime` — a hand-edit
  stops the write and becomes a question instead of silent data loss.
- **Pushback stops the task.** "Why did you…", "that's wrong", and above all "I
  already told you" — that last one means an earlier fix never landed, and it gets
  the full pass.

Written down in `shared/the-law.md`, enforced by `update-the-brain`, audited
monthly by `housekeeping`.

## Why it stays fast as it grows

One document — **`0 — Map`** — holds every folder ID, every setting, and every rules
document with the single job it does. Every session reads it first and goes straight
to what it needs. No searching, and no walking the folder tree as the workspace
grows into email, reviews, recruiting and invoicing.

It is pointers, never prose, and records are not in it — so it stays about thirty
lines forever. It is also what makes "does a document for this job already exist?"
answerable in one read, which is what turns the one-job-one-document rule from a
good intention into a check. Spec: `shared/the-map.md`.

## Setup

At client setup, paste the block in `shared/project-instructions.md` into the Cowork
project's **Project instructions**. It is seven short rules — read the map
first, one job one document, a correction must land in a document, pushback stops
the task, the precedence order, nothing publishes without a yes. Those are the rules
that have to fire before any skill is chosen, so they cannot live in a skill.
`brand-onboarding` prints the block at the end of setup.
