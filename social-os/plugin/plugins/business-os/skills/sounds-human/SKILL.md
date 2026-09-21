---
name: sounds-human
description: >
  Audits whether a draft reads as though a person wrote it, and rewrites the shape
  when it doesn't. Runs the structural pass that word-level editing cannot reach —
  a lesson stated too often, an arc that resolves too neatly, emotion performed
  through the body instead of named, vague allusion where a real thing should be
  named, and a skeleton identical to the last three posts — then checks the result
  still sounds like the owner rather than merely clean. Use when she says "this
  sounds like AI", "this doesn't sound like me", "make this sound human", "humanize
  this", "it reads robotic", "too polished", when a draft is for something longer
  than a caption, or before anything goes out that a reader will judge on trust.
---

# Sounds human

A parent choosing who watches their kid decides in about a second and a half whether
a person wrote the post. Everything else in this system checks whether the copy is
*true*. This checks whether it is *believable*, which for a childcare brand is the
same as whether it works.

Read `${CLAUDE_PLUGIN_ROOT}/shared/sounds-human.md` first — the two layers, the
evidence, and **the trap**, which matters more than any individual fix here.

> **The trap, restated because it is the thing most likely to go wrong:** applying
> this checklist uniformly builds a new fingerprint. Rarity is the human signal.
> **One or two deliberate moves per piece, varied across pieces, and you can say why
> this one got this shape.** Never the whole menu.

---

## Before you start

**The surface layer is already handled.** `draft-post` runs the mechanical tells as
checks — em dashes, hype vocabulary, the antithesis cadence, sycophancy — and fixes
them before anything reaches here. If those have not run, run them first: this pass
reads the skeleton, and vocabulary noise makes the skeleton harder to see.

**Know what you are auditing.** A 120-word caption and a 900-word email are different
jobs. Audits 1–4 apply everywhere. The two long-form audits at the end apply only
when there is room.

---

## 1 · Extract the skeleton, and audit that — not the prose

The one step people skip, and skipping it is why structural tells survive editing.
Structural problems are invisible at sentence level; they only appear in outline.

Write the piece out as its bones:

```
Opens:        how — scene, claim, question, number, outcome?
Beats:        in order, one line each
The point:    where it is stated, and how many times
Emotion:      each moment, and whether it is named or performed
Named things: what is specific, what is vague
Ends:         on what — resolution, moment, number, open question?
```

Six lines. Then audit those, one at a time — checking one dimension per pass found
95% of issues in the source study's own pipeline against 68% for a single combined
look.

---

## 2 · The four audits

### 1 · Is the lesson stated, and how often?
AI narrators explain the theme **77%** of the time; humans **52%**.

Look for: the takeaway sentence, "what this means for you", a closing line that
re-derives the point, every example dutifully interpreted.

**Fix:** state it once where it lands hardest, or not at all. About a third of posts
should end on the moment or the number and let the comments interpret it.

### 2 · Is emotion named, or performed through the body?
**The largest gap in the study, and the one this brand is most exposed to.** AI
performs emotion physically **81%** of the time against **38%** for humans. Humans
name it: explicit emotion labels **29%** against **8%**.

Look for: *chest tightened · breath caught · heart sank · a knot in her stomach ·
swallowed hard · hands shaking · something shifted.*

**Fix:** *"honestly, that first day scared her"*, not *"her chest tightened."*

This contradicts "show, don't tell" — the advice every caregiver-testimonial caption
is written under, which is exactly why it is the highest-yield audit here. Keep one
earned embodied moment per piece at most.

### 3 · Are things named, or alluded to?
Humans name real things **47%** against **24%**; AI alludes **72%** against **50%**.

Look for: *a parenting book · experts say · studies show · a well-known approach ·
recently · a local family.*

**Fix:** name it, or cut it. The title, the date, the neighbourhood, the age, the
price, the number of years. **Anything specific enough to name is specific enough to
check** — so run every new specific past `What we offer` before it ships.

### 4 · Does this have the same skeleton as the last three?
Read the last three to five packets in `4 Published/` — opener type, arc, emotion
mode, closer, CTA shape.

**We can do this audit better than almost anyone**, because the corpus is on disk
with its packets. Most people running a check like this have nothing to compare
against.

**Fix:** if the skeleton repeats, change it deliberately — and note in the packet
which move was used, so the *variation* does not itself settle into a rotation.

### Long-form only — skip at caption length

**5 · Tidiness.** Single track, everything resolved. Humans digress and leave threads
open. One tangent that only obliquely relates, or one question raised and left
standing.

**6 · Reader acknowledgment.** Not "you" — social copy already says "you" constantly
and that gap does not transfer. The transferable move is acknowledging the writing
itself: *"skip this if you've already booked."* A spice, and at caption length it
reads as a gimmick.

---

## 3 · Choose one or two moves. Not more.

Pick from the menu, genre-appropriate, **different from the last piece**:

- **Outcome first.** Open at the end state, then rewind.
- **Cold open.** Start inside the moment; context comes later.
- **Delayed reveal.** Withhold the number the piece is built on until two-thirds in.
- **Callback that recontextualises.** An earlier detail means something new by the end.
- **Unstated point.** End on the moment. Say nothing about what it means.
- **The named thing.** Swap every vague allusion for something checkable.
- **Plain emotion.** Replace body-performance with the stated feeling.
- **End hot.** Stop at the spike instead of the quiet wrap-up.
- **Genuine ambivalence.** Both feelings intact, no resolution forced. Long-form only.
- **The oblique tangent.** One paragraph that echoes without serving. Long-form only.

**Say which ones you picked and why**, in one line. A move you cannot justify is a
move you applied because it was on a list, which is the trap.

---

## 4 · Claude's own fingerprint

Everything here is drafted by Claude, whose fingerprint the study found the most
distinctive of the five models tested. Check for these by name:

- **The epilogue.** A wrap-up line after the piece has already landed. **Cut it and
  end earlier.** The most common fix on our own drafts, by a distance.
- **Flat intensity.** Every sentence at the same energy. Vary the stakes.
- **Reverent quiet endings.** Sometimes end on the spike.

---

## 5 · Then check it still sounds like her

**This is the step that makes the pass safe**, and it runs last for a reason.

Re-read the rewrite against `Told to us/Brand voice` and the room's `Examples/`:

- Are her words still in it — the way she names her own service, her CTAs, her
  signature phrases?
- Do the tone sliders still hold?
- Does it read like the examples she approved, or like a well-edited stranger?

> **Copy that passes every check and says nothing has not been de-slopped. It has
> been sanded.**

A caption with an em dash in it is a five-second fix. A voiceless caption is a
rewrite. **If the de-slopping cost her voice, put the voice back and accept the
tell** — then say which one and why, so she can overrule you.

---

## 6 · Report it briefly

Two or three lines. What the skeleton looked like, what you changed, what you left.

> The draft stated the point twice and ended on a wrap-up line. Cut the closing
> restatement and ended on the number instead. Left the em dash in "eight years —
> same two families" because that pause is hers; it's in three of your examples.

Then record it: one line in `Learned by us/History` naming the move used, so audit 4
has a trail next time.

---

## Rules

- **Never the whole menu.** One or two moves, chosen and justified.
- **Never the same move as last time** without saying why.
- **Never sand her voice off to pass a check.** The voice re-check outranks the audits.
- Never claim this makes anything undetectable. It does not, and that is not the job.
- Never apply the long-form audits to a caption.
- If the piece is fine, say so in one line and change nothing. A clean draft is a real
  result, and rewriting it to demonstrate effort is how a system loses trust.

## If there is no workspace yet

This reads `Brand voice` and `4 Published/`. Without them it is guessing at a voice,
which is the opposite of the job. Run `business-os:brand-onboarding` first.
