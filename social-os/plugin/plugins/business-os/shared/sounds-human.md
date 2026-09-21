# Sounds human — the layer that decides whether a parent trusts the post

Read this before writing or auditing anything the owner's audience will read.

Every other check in this system asks *is it true?* — is the price right, is there a
release, does the link resolve. This one asks the question a reader asks first, before
any of that, in about a second and a half:

> **Did a person write this, or did a machine?**

For most businesses that is a style problem. **For a childcare brand it is the
product.** A parent deciding who watches their kid is making a trust decision, and
copy that reads as machine-generated leaks trust in exactly the market where trust is
the only thing being sold. A caregiver deciding where to apply reads it the same way.

---

## Two layers, and the second one is the one that survives

**Surface** — words, punctuation, phrasing. Em dashes, hype vocabulary, the
"not just X, it's Y" cadence, sycophantic openers. Cheap to fix, mechanically
checkable, and **decaying as a signal on its own** because model vendors keep tuning
it away.

**Structure** — the shape of the piece. Where the lesson sits, whether everything
resolves, how emotion is rendered, whether things get named. Expensive to fix,
requires rewriting rather than word-swapping, and **it is where the durable
fingerprint lives.**

The evidence is specific, and it is why this file exists at all. The StoryScope study
(Russell et al. 2026, arXiv:2604.03136 — verified against the paper's own abstract)
classified **61,608 stories** from humans and five LLMs using **only discourse-level
features, with every style feature withheld**, and detected AI text at **93.2%
macro-F1**. Then the authors ran AI text through a professional span-level rewriting
system that strips cliché and purple prose — functionally an excellent surface
humanizer. **Detection dropped 1.6 points.**

So a caption can pass every word-level check and still read as machine-written, and
that is the normal case rather than the edge case.

---

## The trap — read this before applying anything below

The study's deepest finding is **convergence**: all five models occupy one tight
region of structural space, while human writing is dispersed and rare. 24.7% of human
stories fall in the corpus's rarest 10%, against 7.1% of AI stories.

**Rarity is the human signal.** Which means:

> **A checklist applied uniformly builds a new detectable cluster.**

If every post now opens mid-scene, names one plain feeling and ends unresolved, that
is a fingerprint too — ours instead of the model's, and just as machine-like to anyone
reading four of them in a row.

**So: one or two deliberate moves per post, varied across posts, and you should be
able to say why this post got this shape.** Never the whole menu. This rule outranks
every other instruction in this file, and violating it while following everything else
is the most likely way to make the output worse.

---

## Where this sits in the order

The published pipeline for this work puts a voice layer last, as something additive.
**We invert that, on purpose.**

```
draft in her voice  →  surface pass  →  structural pass  →  re-check against her voice
```

Her voice is not a coat of paint applied at the end. It is the input — `Brand voice`
and the room's `Examples/` are what `draft-post` writes *from*. So the de-slop passes
run against something that already has a point of view, and the final step is not
adding voice but **checking that the de-slopping did not sand it off.**

That failure has a name and it is the one to watch for:

> Copy that passes every scanner and still says nothing has not been de-slopped.
> It has been sanded.

A caption stripped of every tell and left generic is worse than one with an em dash
in it, because the em dash is a five-second fix and a voiceless caption is a rewrite.

---

## What each layer owns

| Layer | Owns | Does not own |
|---|---|---|
| **Surface** — checks in `draft-post/references/checks.md` | vocabulary, punctuation, the antithesis cadence, hype words, sycophancy | shape, where the lesson sits, what resolves |
| **Structural** — `business-os:sounds-human` | stated lessons, tidy arcs, embodied emotion, vague reference, shape convergence | word choice, punctuation, house style |
| **Voice** — `Told to us/Brand voice` + the room's `Examples/` | register, rhythm, her words, her CTAs, what she'd never say | anything the first two layers handle |

Keeping them separate matters: a skill that tries to do all three does the structural
work badly, because structure has to be audited on the extracted skeleton rather than
on the prose.

---

## The four audits that transfer to captions

The study looked at ~5,000-word fiction. **Applying it to a 150-word caption is an
inference, not a finding**, and saying otherwise would be overclaiming. Six audits
exist in the source work; the four below are the ones whose mechanism plainly
survives the jump to short-form, because they are about *what is said* rather than
*how long the arc is*.

### 1 · Is the lesson stated, and how often?
Narrators explain the theme **77% of the time in AI text, 52% in human**. In a
caption this is the takeaway sentence, the "what this means for you", the closing
line that re-derives the point the post already made.
**The move:** say it once, where it lands hardest, or don't say it at all and end on
the moment. Roughly a third of posts should leave the point unstated and let the
comments do the interpreting.

### 2 · How is emotion rendered? *(the biggest gap, and the one that bites this brand hardest)*
AI performs emotion through the body **81% of the time against 38% for humans** —
*her chest tightened, my breath caught, a knot in my stomach*. Humans just name it:
explicit emotion labels **29% against 8%**.

**This inverts "show, don't tell,"** which is the advice every caregiver-testimonial
caption is written under. A nanny agency reaches for embodied emotion by reflex — it
is exactly the register the subject matter invites — which makes this the single
highest-yield audit here.

**The move:** *"honestly, that first day scared her"* beats *"her chest tightened."*
Keep embodied detail for the one moment in a piece that earns it, not as the default.

### 3 · Are things named, or alluded to?
Humans name real things — **explicit named references 47% against 24%**; AI stays at
vague allusion, **72% against 50%**.
**The move:** *"a parenting book"* becomes the title. *"experts say"* gets a name or
gets cut. *"recently"* gets a date. The neighbourhood, the price, the age, the number
of years. This is the cheapest human marker available and it doubles as a fact check —
anything specific enough to name is specific enough to verify against `What we offer`.

### 4 · Does this post have the same skeleton as the last three?
The convergence finding, applied.
**We can run this audit better than almost anyone**, because the corpus is sitting in
`4 Published/`: the last N posts, with their packets, including hook shape, format,
audience and CTA. Most people running a check like this have nothing to compare
against. Compare, and if the skeleton repeats, change it deliberately — and record
which move was used, so the *variation* itself does not fall into a pattern.

**Two more audits exist in the source work** — structural tidiness (tangents,
unresolved threads) and reader engagement (fourth-wall acknowledgment). Both need room
to breathe and both read as gimmick at caption length. Use them in long-form only —
an email, a blog post, a room that writes at length.

---

## Model fingerprints, since we know what drafted it

Everything here is drafted by Claude, whose fingerprint the study found the most
distinctive of the five models. Three habits to check for by name:

- **The epilogue.** A wrap-up line after the post has already landed. **Cut it and end
  earlier** — this is the most common single fix on our own drafts.
- **Flat intensity.** Every sentence at the same energy. Vary it.
- **Reverent quiet endings.** Sometimes end on the spike instead.

---

## Honest limits

- **Nothing here makes text undetectable, and that is not the goal.** The goal is
  copy that reads as though a specific person with a point of view wrote it — because
  one did, and her voice is in `Brand voice`.
- **The fiction-to-caption transfer is an inference.** Stated, not hidden.
- **Roughly half of what matters is not mechanically checkable.** Uniform sentence
  rhythm, formulaic shape, and polished-but-empty filler are visible only to a reader.
- **Reader address does not transfer.** Humans address the reader far more than AI in
  fiction — but social copy already says "you" constantly, so that gap means nothing
  here. The part that does transfer is acknowledging the writing itself, and at
  caption length it reads as a gimmick. Left out deliberately.

## Where this came from

The two-layer framing, the trap, and the structural audits are adapted from
[humanizer-stack](https://github.com/NulightJens/humanizer-stack) by Jens Heitmann
(MIT), which packages them as Claude Code skills and grounds them in Russell et al.
Our surface tells trace, through that work, to
[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
by WikiProject AI Cleanup (CC BY-SA 4.0), and the copy-specific ranking to
[vibecoded-design-tells](https://github.com/jcarterjohnson/vibecoded-design-tells) by
jcarterjohnson (MIT). The underlying research is Russell, Rajendhran, Pham, Iyyer and
Wieting (2026), *StoryScope: Investigating idiosyncrasies in AI fiction*,
arXiv:2604.03136 — cited, not relicensed.

Written for this system rather than vendored. See `ATTRIBUTION.md`.
