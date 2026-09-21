---
name: make-graphic
description: >
  Create an on-brand social graphic in Canva for a post — carousel slides, tips
  cards, quote cards, availability announcements — using the owner's colors, fonts
  and voice from their Drive brain, sized for Instagram and resized for Facebook,
  and hand back a Canva design id plus an edit link for the post packet. Use
  whenever a post's media source is "canva", the owner says "make a graphic",
  "design this", "turn this into a carousel", "I need an image for this post", or
  draft-post asks for one. Works on Canva Pro; does not require Enterprise. Does
  not export the final file — publish does that at approval time.
---

# Make a graphic

Canva makes the design; the brain makes it on-brand. Canva's Brand Kit is an
Enterprise feature, so the exact colours and fonts live in
`1 — Brain/Told to us/Colors and fonts`, and you apply them yourself. That doc is
the substitute for the feature we cannot buy — read it every time.

Read `references/canva-cheatsheet.md` for tool names, the editing transaction, and
plan gating. Read `${CLAUDE_PLUGIN_ROOT}/shared/guardrails.md` before choosing any imagery.

> **The four rules that never bend**, restated here so they hold even if the shared
> file above fails to load: never post an identifiable child's face without a signed
> release on file; never generate an AI image of a child; never write "licensed",
> "certified", "guaranteed" or "100% safe" unless that exact credential is documented
> in `What we offer`; never imply nannies are 1099 contractors. When in doubt, refuse
> the specific thing, say why in one plain sentence, and offer the compliant version.


## First: is Canva even available?

Read `canva_available` in `0 — Map`. **`no` ⇒ stop and say so plainly** — there is
no partial version of this skill worth running. Tell the caller to use a photo or a
short video instead, which is what the sector research says converts best anyway,
and offer to note the graphic idea in `1 Ideas/` for whenever Canva is added.

`canva_available` is also `no` in practice when the Canva connector is not
connected, or when the account is Canva **Free** and the post needs more than one
size — `resize-design` is Pro-and-above. Say which of those it is; "it didn't work"
is not a useful answer to a non-technical owner.

## Two paths — prefer the first

**A · From one of her Brand Templates (Pro+).** If the owner has built Brand
Templates in Canva for this format (onboarding asks; `search-brand-templates`
confirms), instantiate one and swap the text. Consistent, fast, and it looks like
*her*, because it is.

**B · Generate.** No template for this format → `generate-design` with a prompt
that carries the exact hex colours, font names, the headline text, the format
preset, and the visual-language rules from guardrails. Review candidates'
thumbnails, pick the closest, `create-design-from-candidate`.

## Steps

1. **Load brand.** `Colors and fonts` (hex values, font names, logo asset name),
   `Brand voice` (for on-image copy), the headline/body lines from `draft-post`.
2. **Choose path A or B** as above.
3. **Set the text.** `get-design-content` → element ids → `start-editing-transaction`
   → `perform-editing-operations` with `replace_text` per element (use
   `find_and_replace_text` if the page is responsive) → `commit-editing-transaction`.
   Keep on-image copy short: a hook and at most two supporting lines per slide.
4. **Set the imagery.** Prefer her real photos: `upload-asset-from-url` needs a
   public URL, so use a logo/photo already in Canva or one the owner uploaded there.
   Never generate people-shaped imagery for a childcare brand; never any child.
   Graphics, icons, colour blocks, hands-and-toys photography are the default.
5. **Resize.** `resize-design` (Pro+) for the other platform sizes the post targets:
   Instagram square/portrait for feed, 9:16 for Story, landscape for Facebook where
   it helps. One design becomes every size — this is the most repetitive task in
   social and Canva does it in one call.
6. **Do not export.** Export links are signed and expire; `publish` exports at
   approval time. Record in the packet: `canva_design_id`, `canva_edit_url`
   (`https://www.canva.com/design/<id>/edit`), and which resized variants exist.
7. **Show her** the thumbnail and the edit link. Canva's own guidance: the edit link
   *is* the handoff — she can nudge anything in Canva before approving, and
   `publish` exports whatever is there at that moment.

## Checks

`${CLAUDE_PLUGIN_ROOT}/skills/make-graphic/references/checks.md` — six, three
blocking. Run them after export and write the evidence into the packet
(`${CLAUDE_PLUGIN_ROOT}/shared/proof.md`).

Two are easy to think are unnecessary and are not: **text baked into an image is not
seen by the caption checks**, and **an unreplaced `{{placeholder}}` on a published
graphic** is the most embarrassing failure available and is entirely mechanical to
catch.

**Fix what you can, re-run, then report.** Handing her a list of failures you could
have fixed yourself is the lazy half of this. Surface only what you genuinely cannot
resolve. **More than two failures on the first pass is a broken run, not a bad
output** — stop and say which part of the process caused it rather than patching
three things individually (`${CLAUDE_PLUGIN_ROOT}/shared/proof.md`).

## Done means

An exported image whose URL resolves, sized for its destination, using only colours
from `Colors and fonts`, with every placeholder substituted, and an evidence report
in the packet with no unresolved blocking failure.

## Rules

- Hex values and fonts come from `Colors and fonts`. Never approximate a brand
  colour from memory.
- Set Instagram's `isAiGenerated` note in the packet if any AI imagery is on the
  design.
- Rate limits: generate/create/resize/export are 20 requests per minute. Batch a
  week's graphics with that in mind; don't hammer.
- If Canva returns `license_required` on export, a premium element is blocking —
  swap it, don't buy it silently.

## If she pushes back while you are doing this

Stop. Do not apologise and carry on, and do not just adjust for the rest of the
conversation — that fix disappears tonight. Corrections, confusion ("why did you…"),
disagreement, and especially "I already told you" all mean a **document** is wrong.
Hand it to `business-os:update-the-brain`, which finds that document, fixes it, and
fixes whatever was built from it. Then come back here and continue from the
corrected state.

## If there is no brain yet

Search Drive for a folder named `<Business> — AI Workspace` and read its `0 — Map`
doc. **If either is missing, stop and run `business-os:brand-onboarding` instead** —
this skill has nothing to read and would invent a brand. Say so in one plain line:
*"I don't have your brand set up yet — let's do that first, it takes about forty
minutes and you'll have three posts at the end."*

If Setup exists but a value this skill needs is blank, ask for that one value,
then replace the Setup doc (`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`) so nobody asks again.
