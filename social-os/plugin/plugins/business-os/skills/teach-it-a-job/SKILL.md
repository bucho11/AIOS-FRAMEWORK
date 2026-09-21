---
name: teach-it-a-job
description: >
  Learns a job the owner already does, by interviewing her about it rather than
  guessing how she works, and writes it down as a playbook in her own workspace so
  it runs the same way every time. Use when she says "can you do X for me", "I want
  you to handle my invoicing", "let me show you how I do this", "here's my process",
  "do it the way I do it", when she describes a recurring task this system does not
  already have a job for, or when a shipped job keeps being corrected in the same
  direction because her real process is different from the default. Extracts the
  trigger, the inputs and where they live, the steps in order, the decisions and
  their reasoning, what done means, the edge cases, and what a bad version looks
  like — then writes the checks before the job ever runs.
---

# Teach it a job

The single most common way a system like this fails is that somebody wrote down a
process **for** the owner instead of getting it **from** her. What gets written is
plausible, which is exactly why it survives review — and it is wrong in precisely
the specifics that made it hers.

So this skill does not write. It **asks**, and then writes down what it heard.

Read `${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md` (the four layers, and shipped
versus interviewed), `${CLAUDE_PLUGIN_ROOT}/shared/proof.md` (what a check is), and
`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`. Read `0 — Map` for the room.

---

## Before you start

**Is it a job, or a step?** A job has its own trigger, its own inputs and its own
idea of done. *"Write the caption"* is a step inside drafting a post. *"Chase unpaid
invoices"* is a job. If it is a step, it belongs in an existing playbook — say so
and go fix that instead.

**Does a job already cover it?** Check `0 — Map` and the room definitions in
`${CLAUDE_PLUGIN_ROOT}/rooms/`. Two playbooks for one job is the same failure as two
documents for one job (`the-law.md`, Law 1). If one exists and is merely wrong, this
is a correction — `business-os:update-the-brain`.

**Does it need a new room?** A genuinely new domain — its own audience, its own
destination — gets a room first (`growth-and-upkeep.md`). A new job inside a domain
she already runs does not.

**Say how long it takes and why.** *"Fifteen minutes of questions, and after that I
do it your way every time instead of you correcting me every week."* People answer
better when they know the trade.

---

## The interview

**One question at a time.** A wall of eight questions gets eight short answers. One
at a time gets the aside after the answer, and the aside is usually the real rule.

**Ask about the last real time she did it**, not about the process in the abstract.
*"Walk me through the last invoice you chased"* gets you the truth. *"What's your
invoicing process?"* gets you an idealised version she does not actually follow.

Eight topics. Follow the conversation; do not read them out as a list.

**1 · What starts it, and how often.**
> What makes you sit down and do this? Is it a day of the week, or does something
> happen that sets it off?

**2 · What you need in front of you, and where it lives.**
> What do you need open to do it? Where exactly is that — which folder, which app,
> who sends it to you?

Push for the exact location. *"The spreadsheet"* becomes a question you have to ask
again every single run.

**3 · The steps, in the order you actually do them.**
> Take me through it from the top. What's the very first thing you do?

Then: *"and then what?"* until she runs out. **The order matters more than the
words** — write what she says, in her sequence, even where a different order would
be tidier.

**4 · The decisions, and why.**
> You said you sometimes do X instead — how do you know which?

This is the layer that makes it hers, and the one she is least likely to volunteer,
because to her it is obvious. Every *"it depends"* is a rule that has not been said
out loud yet. Chase all of them.

**5 · How you know it's done, and how you check.**
> When do you consider this finished? Is there anything you look at to be sure?

Her check is the first proof check. Write it down in her words.

**6 · What has gone wrong before.**
> Has this ever gone sideways? What happened?

Past failures are the highest-value thing in the whole interview: each one is an
edge case *and* a check, and it is already known to be real rather than imagined.

**7 · How it should sound or feel.**
> Does it need to sound a particular way? Who reads it?

If it is written output, this refers to `Brand voice` — **do not create a second
voice for this job.** A genuine difference is a section inside the existing
document (`the-law.md`, Law 1).

**8 · What a bad one looks like.**
> If I did this badly, what would you notice first?

**Ask this one even when you are out of time.** "What would you notice" is the
fastest route to a check that can fail, because she answers with something specific
and observable rather than a quality adjective.

### While she talks

- **Write her words**, not a tidied version. *"I don't chase the ones under fifty
  bucks, it's not worth the awkwardness"* is a better decision rule than *"apply a
  materiality threshold."*
- **Never fill a gap yourself.** If she skips a step, ask. A plausible invention is
  worse than an admitted hole, because nobody ever comes back to check it.
- **Say what you're hearing, once, near the end**, so she can correct it while it is
  cheap: *"So it's every Friday, you start from the aging report, anything under $50
  you leave, and you only phone after two emails. Right?"*

---

## What you write

### 1 · The playbook — her room, her Drive

`N — <Room>/Playbook — <Job name>`, created per `drive-conventions.md`. It is an
**interviewed** playbook, which means **no upgrade may ever rewrite it** — only
propose a change with a diff, like any other Lane 2 change (`playbooks.md`).

Seven sections, in this order:

```
Origin: interviewed · <date> · from <her name>

## Purpose          what this job is for, one line
## When to use      the exact words she'd say, and the schedule if it has one
## Inputs           what's needed and exactly where each thing lives
## Steps            numbered, in her order
## Decisions        each rule, with her reasoning
## Done             what finished means, and how it gets verified
## Edge cases       what has gone wrong, and what to do
```

**`When to use` gets the exact wording she would actually type.** A vague trigger is
why a job never fires. *"When she says 'chase the invoices' or 'who owes me money'"*
— not *"for accounts receivable follow-up."*

### 2 · The checks — before it ever runs

Five to ten, per `${CLAUDE_PLUGIN_ROOT}/shared/proof.md`. **Write them now**, not
after a month: checks written later are written around the mistakes everyone got
used to.

You already have most of them from the interview. Question 5 gave you her own
verification. Question 6 gave you the real failures. Question 8 gave you what she
would notice. Turn each into something that can fail, with a tier.

An interviewed playbook keeps its checks with it, in a `## Checks` section of the
same document, because both are hers.

**If you cannot write the *fails when* line concretely, it is not a check.** Drop
it rather than softening it into a judgement.

### 3 · The registration

Add the job to the room's row in `0 — Map` and rebuild the map. A playbook that is
not in the map is invisible to every future session.

### 4 · Nothing in the toolbox yet

Leave `Templates/` alone. It fills from real work — the signal is *anything rebuilt
from scratch that existed before* (`playbooks.md`). A template written before the job
has ever run is a guess wearing a filename.

---

## Then run it once, with her there

Do the job while she watches, from the playbook you just wrote. This is where it
gets real: she will say *"no, not like that"* three or four times in ten minutes,
and each one is a correction that costs nothing now and would have cost a month
later.

Fold every one into the playbook **as it happens** — into the document, not just
into the conversation (`the-law.md`, Law 3). Then show her the evidence report and
ask whether the checks are checking the right things.

Close with the two sentences she needs:

> This is saved as **Playbook — <job>** in your <room> folder. Say *"<her trigger
> words>"* any time and I'll run it exactly this way. If I get it wrong, tell me and
> I'll fix the playbook, not just that one run.

## Rules

- Never write a step she did not describe. An admitted gap beats a plausible
  invention.
- Never create a second document for something the brain already holds — no job-level
  brand voice, no job-level offer list.
- Never skip the checks because the interview ran long. A playbook with no checks
  makes her the quality control, which is what she was trying to stop doing.
- Never let an upgrade overwrite an interviewed playbook. Propose, with a diff.
- If she says *"just do what you think"*, that is not permission to invent — it means
  the job is not well-formed yet. Offer to run it once together and write it down
  afterwards from what actually happened.

## If there is no workspace yet

Run `business-os:brand-onboarding` first. A job needs a room to live in and a brain
to read.
