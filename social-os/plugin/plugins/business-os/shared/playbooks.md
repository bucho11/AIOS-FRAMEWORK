# Playbooks — four layers per job

Read this before adding a job, changing how one works, or diagnosing why one went
wrong.

A **room** is a domain: social, email, invoicing. A **playbook** is one job inside
it: draft a post, send the weekly update, chase an unpaid invoice. A room holds
several playbooks, and each one has four layers.

Three of them are borrowed from a model worth borrowing from — process, toolbox,
proof. The fourth is ours, and the merge is the point: **their model assumes the
job's knowledge lives in the playbook. In this system it mostly lives in the brain**,
shared across every room, which is why a fourth layer exists and why a failure can
land there.

---

## The four layers

| Layer | What it holds | Where it lives |
|---|---|---|
| **1 · Process** | the steps, in execution order — triggers, inputs, decisions, done, edge cases | `skills/<job>/SKILL.md` (shipped) or a `Playbook` document in her room (interviewed) |
| **2 · Toolbox** | reusable artifacts — templates with placeholders, reference data, scripts, style guides | her room's `Templates/` |
| **3 · Proof** | checks that can fail, producing external evidence, before the work reaches her | `skills/<job>/references/checks.md` — evidence written into the work |
| **4 · Context** | who she is, how she sounds, what she sells, what the AI may do | `1 — Brain/Told to us/` — **shared by every playbook** |

Plus the two things that make it compound, which are records, not layers:

- **Examples** — `Examples/` in her room: work she approved, each one carrying
  **why** it was good. An example with no reason is just an old post.
- **Corrections** — `Learned by us/History`: dated, newest first, mined monthly.

---

## Layer 4 is why this isn't a straight copy

In a standalone playbook, "how we sound" is written into the job. Here, one
`Brand voice` document serves social, email, reviews and recruiting at once, and
the brain does not fork (`growth-and-upkeep.md`).

That is a real advantage — correct the voice once and every room changes — and it
creates a failure mode the three-layer model has no name for: **the process was
right, the toolbox was right, the checks passed, and the output was still wrong,
because the brand document it read was wrong.**

So diagnosis has four answers, not three. See below.

---

## Shipped or interviewed — every playbook declares which

The most important rule in this file, because it decides what an upgrade may
touch.

**`shipped`** — we wrote the process, it lives in the plugin, it is the same for
every client, and a release can improve it for everyone at once. Social is shipped:
we know how Instagram works, and a client who had to teach us that got a worse deal
than one who didn't.

A shipped playbook is **a domain default, not a claim to know her business.** It
starts as a draft and becomes hers through correction. The first month of
corrections against a shipped playbook is the most valuable month it will ever have
— harvest it (`update-the-brain`), don't let it sit in chat.

**`interviewed`** — *she* holds the process, it was extracted by asking her, it
lives in her Drive, and **no upgrade may ever overwrite it.** Her invoicing
sequence, her caregiver screening call, the way she handles a late cancellation.

> **Writing her process yourself instead of asking is the classic failure**, and it
> fails in a way that is hard to see: what you wrote is plausible, so it survives
> review, and it is only wrong in the specifics that make it hers. Use
> `business-os:teach-it-a-job`.

**The upgrade rule, stated once so it cannot be misread:**

> An upgrade may rewrite a **shipped** playbook. An upgrade may **never** rewrite an
> **interviewed** one — it may only *propose*, with a diff, like any other Lane 2
> change. Her process is hers in the same way her brand voice is hers.

This is also where the tier line sits, and it corrects a rule that was stated too
bluntly before. The real boundary is not *"no behaviour rules in her Drive"* — her
`Rules for the AI` has always been a behaviour rule in her Drive. It is:

| | Lives in the plugin | Lives in her Drive |
|---|---|---|
| **How the system behaves** — the laws, correction, the map format, upgrades | ✅ always | ❌ never |
| **How her work is done** — her voice, offers, permissions, **processes** | ❌ never | ✅ always |

---

## What goes in a toolbox, and how you know

The toolbox is the layer nobody builds deliberately, because its contents only
become obvious in hindsight. The signal is precise:

> **Anything rebuilt from scratch that existed before belongs in the toolbox.**

If a caption's screening paragraph gets rewritten every month, that is a template.
If the same five hashtags are re-derived every week, that is reference data. If the
same intro is retyped, that is a snippet.

**Two ways to catch it, and the second one is the real test.**

*Passively*, while working: you are the one rebuilding it, so you are the only one
who can notice. When you do, say so in one line and save it.

*Actively*, after a job runs: **run the whole job again from scratch and say which
saved files you used and which parts you built from nothing.** Everything in the
second list is a toolbox candidate. This is a test rather than a hope — noticing
depends on attention, and attention is exactly what fails on the fortieth run.

Do the active test when a job is new, and again whenever it starts feeling slow.

### Writing one

**A filename says what it is, and nothing else.** `screening-paragraph.md`, not
`screening-paragraph-v3.md` or `screening-2026-10-05.md`. A date or a version number
in a filename creates a second file that does the same job the moment it is updated —
which is Law 1, broken by a naming habit. **Replace the file; the archive keeps the
old one** (Law 6).

**Placeholders in square brackets, with one filled-in example underneath.** The
brackets mark what changes per use; the example shows what belongs there, which the
slot name alone never quite does.

```
We screen every caregiver with [screening_steps], and every placement is
backed by [guarantee_terms].

---
Example, as used 2026-10-05:
We screen every caregiver with a national background check, driving record,
CPR verification and three reference calls, and every placement is backed
by a 30-day replacement guarantee.
```

*(These brackets are not the `{{double braces}}` used in onboarding seed documents.
Those are filled once, at setup, by `brand-onboarding`. These are filled every time
the template is used. Different lifetimes, different marks — deliberately.)*

**The playbook step points at the file by name, and says when NOT to use it.** A
template applied in the wrong place is worse than no template, because it looks
considered. *"Use for any post explaining vetting. Do not use for a caregiver-facing
post — they are the ones being screened, and it reads as a warning."*

### What never goes in the toolbox

- **One-off outputs.** Something written for one occasion is not reusable; saving it
  guarantees it gets reused somewhere it does not fit.
- **Anything holding a password, key or token.** Never, and not only here —
  `drive-conventions.md` forbids it workspace-wide.
- **A draft she has not approved.** An unapproved draft saved as a template makes a
  guess into a standard, quietly, and every future post inherits it.

`Templates/INDEX.md` — one line each, so nothing is rebuilt because nobody knew it
existed:

```
| File | What it's for | Added |
|---|---|---|
| screening-paragraph.md | the standard how-we-vet explanation | 2026-09-28 |
| local-hashtags.md      | the 12 that work in this market      | 2026-10-05 |
```

Shared brand things — logos, photos, fonts, release forms — stay in
`2 — Brand Assets/`. A toolbox is one job's working material, not the brand.

---

## Diagnosis — which layer failed

When something goes wrong, name the layer before fixing anything. The fix is
different in each, and fixing in the wrong one means it happens again.

| The failure | Layer | The fix |
|---|---|---|
| a step was missed, or the order was wrong | **process** | add or correct the step in the playbook |
| it rebuilt something that already existed | **toolbox** | write the file, index it, use it |
| it reached her and nothing caught it | **proof** | **write the check.** Every escape earns one |
| the steps ran correctly and the output was still wrong | **context** | fix the brain document — `update-the-brain` |

**The proof row is the one that compounds**, and it is the one most often skipped
because fixing the output feels like fixing the problem. It isn't: the same escape
returns next month. An escape that produces a new check cannot happen twice. An
escape that produces an apology happens forever.

Then: smallest durable fix, one dated line in `History`, rerun from the start, and
show the before and after.

---

## Adding a playbook

1. **Is it a job or a step?** A job has its own trigger, its own inputs and its own
   idea of done. "Write the caption" is a step of drafting a post. "Chase unpaid
   invoices" is a job.
2. **Shipped or interviewed?** A domain we genuinely know → shipped. Anything
   specific to how *she* works → interviewed, via `business-os:teach-it-a-job`.
3. **Write the process** — steps in execution order, with a definition of done.
4. **Write the checks first, not last.** Five to ten, each able to fail, before the
   job runs for real. Checks written after a month of running are written around the
   bugs you got used to.
5. **Leave the toolbox empty.** It fills from real work. A template written before
   the job has run is a guess.
6. **Register it** — a row in the room's definition under `rooms/`.
