---
name: draft-post
description: >
  Write one Instagram + Facebook post in the owner's voice from a Content Calendar
  row or a one-line idea: hook in the first 125 characters, one clear call to
  action, local hashtags, first-comment text, alt text, and — when the row calls for
  a graphic — hand off to make-graphic. Runs the guardrails before saving and stages
  the result as a post packet in 2 Drafts for approval. Use whenever the owner says
  "draft this", "write a post about…", "make the posts for this week", "turn this
  into a caption", or plan-week hands over rows. Never publishes.
---

# Draft a post

Write it so she reads it once and says "yes, that's me." Voice first, then
structure, then compliance, then stage it. Nothing here publishes.

Read `../../shared/drive-conventions.md`, `../../shared/post-packet.md`,
`../../shared/guardrails.md`, and `references/caption-rules.md`. Then read the
brain: `Brand voice`, `What we offer`, `Who we talk to`, `Her preferences`,
`What works (current)`.

## Steps

1. **Know the row.** From the Content Calendar (or the owner's one-liner): topic,
   audience, format, platforms, publish time, media source, hook idea, CTA.

2. **Write in her voice.** Apply `Brand voice` literally — sliders, sentence length,
   POV, emoji policy, never-use list, CTA verbs. Then check `Her preferences` for
   any correction she has ever made and honour it. When in doubt, pick the plainer,
   warmer line.

3. **Structure per `caption-rules.md`.** Hook + market/service keyword inside the
   first 125 characters. One idea per line. Value, then proof, then **one** CTA as
   the last line. 3–5 small local hashtags — in the caption or in the first comment,
   never both. No links in an Instagram caption; links go in `first_comment`.
   Write alt text describing the image plainly.

4. **Facts only from the brain.** Every claim about screening, credentials,
   pricing, guarantees must appear in `What we offer`. If the idea needs a fact that
   isn't there, write around it or ask — never invent.

5. **Media.**
   - `owner-upload` → note exactly what she should upload (which photo/Reel) in the
     packet; `publish` will hand her the upload link at approval time.
   - `canva` → **check `canva_available` in Setup first.** `yes` → run
     `social-os:make-graphic` with the caption's headline and the brand's colours; it
     returns a `canva_design_id` and edit URL for the packet. `no` → switch the post
     to `owner-upload` and say which photo or short video would carry it. The system
     is complete without Canva; graphics are an upgrade, not a dependency.
   - Any real child → check `Photo releases/` first. No match → refuse that image,
     offer the no-face framing, keep going.

6. **Self-check against `guardrails.md`.** Claims, classification, testimonial
   disclosure, child imagery. Fix before staging.

7. **Stage.** Create the packet doc in `2 Drafts/` per `post-packet.md`, status
   `draft`, with the calendar row's time as `publish_at`. Ask the
   `compliance-reviewer` agent to read it and fill `## Compliance check`.

8. **Show her**, briefly: the caption as it will post, the graphic thumbnail or edit
   link if any, what she needs to upload if anything, and the exact phrase to
   approve it.

## Rules

- One CTA. Two CTAs is zero CTAs.
- No hashtags-only comment blocks of 20; 3–5 local ones.
- Instagram captions cap at 2,200 characters; aim far lower. Facebook shows
  ~480 before "See more" — the hook must land before that.
- Never write "licensed", "certified", "guaranteed", or "100% safe" unless
  `What we offer` documents the exact credential.
- Never imply nannies are contractors.

## If there is no brain yet

Search Drive for a folder named `<Business> — Social OS` and read its `0 — Setup`
doc. **If either is missing, stop and run `social-os:brand-onboarding` instead** —
this skill has nothing to read and would invent a brand. Say so in one plain line:
*"I don't have your brand set up yet — let's do that first, it takes about forty
minutes and you'll have three posts at the end."*

If Setup exists but a value this skill needs is blank, ask for that one value,
then replace the Setup doc (`../../shared/drive-conventions.md`) so nobody asks again.
