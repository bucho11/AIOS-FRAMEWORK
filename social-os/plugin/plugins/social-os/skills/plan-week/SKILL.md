---
name: plan-week
description: >
  Plan the coming week of Instagram and Facebook content for a business owner:
  read their brain (voice, offers, audiences, what has worked), pick a balanced mix
  across topics and both audiences, choose formats and posting times from real
  performance data, and write it into the Content Calendar so drafts can be made.
  Use whenever the owner says "plan my week", "what should we post", "content for
  next week", "I've gone quiet", "fill the calendar", or a weekly scheduled task
  runs. Also use when someone asks for a month of content — plan it week by week.
  Never publishes anything; it only plans.
---

# Plan the week

Owners don't stop posting for lack of ideas. They stop because posting falls off
the list when the week gets busy. This skill keeps the next week already decided,
so the only decision left is "yes".

Read `${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`, then the `0 — Setup` doc, then everything
in `1 — Brain/Told to us/` and `Learned by us/What works (current)`. Read
`references/pillars-and-cadence.md` for the mix and the sector defaults.

Read `${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md` before creating any folder or document the layout does not already name — especially if the owner asks for something that is not social media.


## Steps

1. **Load the brain.** Setup → capacity (`posting_capacity_per_week`,
   `reels_she_can_film_per_week`, `recruiting_in_scope`, timezone) → voice →
   offers → audiences → `What works (current)` → the last two weeks of the
   `Content Calendar` (so you never repeat an angle within 60 days).

2. **Check what's still open.** List packets in `2 Drafts/` and `3 Approved/`. Posts
   already waiting count against this week's capacity; don't bury her in drafts.

3. **Pick the mix.** Exactly `posting_capacity_per_week` posts, cross-posted to
   Instagram + Facebook unless `Rules for the AI` says otherwise. Balance:
   - Reels ≤ `reels_she_can_film_per_week` (she has to film them)
   - at least one educational carousel or graphic (saves and shares) — **only if
     `canva_available: yes` in Setup**; otherwise convert that slot to a photo post
     or a talking-to-camera Reel, which the research ranks higher for reach anyway
   - at least one caregiver-facing post per week **if recruiting is in scope**
   - rotate topics; no topic twice in a week unless she asked
   - one local-presence hook (market name in the first line) per week
   Read `What works (current)`: lean toward the formats and hooks it says perform;
   drop what it says flopped.

4. **Pick times.** Ask `publish` for best times (it wraps the vendor's best-time
   data); fall back to the sector defaults in the reference. Always on the hour or
   half hour, in her timezone. Spread across days.

5. **Write the plan** into `Content Calendar` (replace-by-recreate): one row per post
   — date/time, platforms, topic, audience, format, media source (`owner-upload`
   for her photos/Reels, `canva` for graphics), the hook idea in one line, and the
   CTA. Mark rows that need something from her (a Reel to film, a photo to upload)
   with **what and by when**.

6. **Tell her what she owes.** In one short message: which Reels to film (length
   ≤ 60 s so they work on both platforms, vertical), which photos to drop into
   `2 — Brand Assets/Photos`, and by when. Filming specs live in the reference.

7. **Hand off.** If this run was triggered by a scheduled task or she said "go
   ahead", run `social-os:draft-post` for each planned row and report what is now
   waiting in `2 Drafts/`. Otherwise stop after the plan and ask.

## Rules

- Never exceed her stated capacity. A calendar she can't keep is worse than none.
- Never plan a post that needs a child's face unless a matching release is listed
  in `Photo releases/` (see `${CLAUDE_PLUGIN_ROOT}/shared/guardrails.md`).
- Never repeat a hook or angle used in the last 60 days.
- The calendar is the truth surface for the week. Drafts cite it; they don't
  compete with it.

## If there is no brain yet

Search Drive for a folder named `<Business> — AI Workspace` and read its `0 — Setup`
doc. **If either is missing, stop and run `social-os:brand-onboarding` instead** —
this skill has nothing to read and would invent a brand. Say so in one plain line:
*"I don't have your brand set up yet — let's do that first, it takes about forty
minutes and you'll have three posts at the end."*

If Setup exists but a value this skill needs is blank, ask for that one value,
then replace the Setup doc (`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`) so nobody asks again.
