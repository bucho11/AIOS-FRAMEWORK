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

Read `${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`, `${CLAUDE_PLUGIN_ROOT}/shared/post-packet.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/guardrails.md`, and `references/caption-rules.md`. Then read the
brain: `Brand voice`, `What we offer`, `Who we talk to`, `How she likes to work`,
`What works (current)`.

Read `${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md` before creating any folder or document the layout does not already name — especially if the owner asks for something that is not social media.


> **The four rules that never bend**, restated here so they hold even if the shared
> file above fails to load: never post an identifiable child's face without a signed
> release on file; never generate an AI image of a child; never write "licensed",
> "certified", "guaranteed" or "100% safe" unless that exact credential is documented
> in `What we offer`; never imply nannies are 1099 contractors. When in doubt, refuse
> the specific thing, say why in one plain sentence, and offer the compliant version.


## Steps

1. **Know the row.** From the Content Calendar (or the owner's one-liner): topic,
   audience, format, platforms, publish time, media source, hook idea, CTA.

2. **Write in her voice.** Apply `Brand voice` literally — sliders, sentence length,
   POV, emoji policy, never-use list, CTA verbs. Then check `How she likes to work` for
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
     `business-os:make-graphic` with the caption's headline and the brand's colours; it
     returns a `canva_design_id` and edit URL for the packet. `no` → switch the post
     to `owner-upload` and say which photo or short video would carry it. The system
     is complete without Canva; graphics are an upgrade, not a dependency.
   - Any real child → check `Photo releases/` first. No match → refuse that image,
     offer the no-face framing, keep going.

6. **Run the checks.** `${CLAUDE_PLUGIN_ROOT}/skills/draft-post/references/checks.md`
   — seventeen of them, two blocking. **Run
   `${CLAUDE_PLUGIN_ROOT}/skills/draft-post/scripts/caption_scan.py` first** for the
   mechanical slice; if it does not run, report those as `SKIP — read manually` and
   read for the patterns yourself. Never a pass. Checks 11–17 ask the question a reader asks
   first: *did a person write this?* For a childcare brand that is not a style
   question, because trust is the product
   (`${CLAUDE_PLUGIN_ROOT}/shared/sounds-human.md`). **Every one runs, including the ones you expect to
   pass**, and the result goes into the packet as an evidence report
   (`${CLAUDE_PLUGIN_ROOT}/shared/proof.md`), not into the conversation. A check that
   could not run reports `SKIP` with the reason and is surfaced — never a pass.

   **Fix what you can fix, then run them again** before showing her anything. Nine
   hashtags when the rule is three to five is not news for her — it is something to
   correct and re-check. Surface only what you genuinely cannot resolve, and record
   the fixes in the report so she can see what the checks are catching.

   **More than two failures on the first pass means stop.** That is not a bad draft,
   it is a broken run — a brain document that is wrong so everything downstream fails
   together, or a step that ran out of order. Say which, rather than patching three
   things individually and producing a draft that passes on a process that will fail
   the same way tomorrow.

   **A blocking failure means the packet is not staged.** Say what failed, with the
   evidence, and offer the nearest version that would pass. She can override in
   words, and the override is written into the report with her reason and the date.

   This is what stops her being the quality control. Without it she is proofreading
   every draft for a missing release and a price that changed — which is the most
   expensive possible use of the one person this system exists to protect.

7. **Judgement pass against `guardrails.md`.** Claims, classification, testimonial
   disclosure, child imagery. Fix before staging.

8. **Stage.** Create the packet doc in `2 Drafts/` per `post-packet.md`, status
   `draft`, with the calendar row's time as `publish_at`. Ask the
   `compliance-reviewer` agent to read it and fill `## Compliance check`.

9. **If the shape is the problem, not the words** — check 17 flags a skeleton
   matching the last three posts, or the draft states its point twice and closes on a
   wrap-up line — hand it to `business-os:sounds-human` before staging. That pass
   rewrites structure and then checks the result still sounds like *her*, which is a
   different job from fixing a word.

   **One or two structural moves, not the whole menu.** A checklist applied uniformly
   builds a new fingerprint; rarity is the human signal.

10. **Show her**, briefly: the caption as it will post, the graphic thumbnail or edit
   link if any, what she needs to upload if anything, and the exact phrase to
   approve it.

## Done means

The packet is in `2 Drafts/` with a caption, media decision, alt text, audience and
first comment; its evidence report shows every check run with no unresolved blocking
failure; and she has seen the caption exactly as it will post, with one line on
anything that needs her.

Not done: a caption in the chat. Not done: checks that were "looked at".

## Was anything rebuilt?

If you wrote something from scratch that has been written before — the screening
paragraph, the local hashtag set, a standard opener — that is the toolbox signal
(`${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md`). Say so in one line, write it into the
room's `Templates/` with bracketed placeholders and one filled-in example, index it,
and use it from then on.

You are the only one who can notice this passively, because you are the one
rebuilding it. **When a job is new, or starts feeling slow, run the active test
instead:** do the whole job again from scratch and say which saved files you used and
which parts you built from nothing. Everything in the second list is a candidate.
Noticing depends on attention; the re-run does not.

## Rules

- One CTA. Two CTAs is zero CTAs.
- No hashtags-only comment blocks of 20; 3–5 local ones.
- Instagram captions cap at 2,200 characters; aim far lower. Facebook shows
  ~480 before "See more" — the hook must land before that.
- Never write "licensed", "certified", "guaranteed", or "100% safe" unless
  `What we offer` documents the exact credential.
- Never imply nannies are contractors.

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
