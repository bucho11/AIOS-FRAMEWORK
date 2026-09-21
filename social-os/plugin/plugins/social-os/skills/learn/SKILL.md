---
name: learn
description: >
  The weekly learning loop that makes next week better than this week: pull real
  Instagram and Facebook performance from the publisher, find what worked and why,
  detect failed posts and accounts that need reconnecting, check the best posting
  times, write a plain-English report to 4 — Results, and update Learned by us /
  What works (current) so plan-week and draft-post read it next time. Use whenever
  the owner says "how did we do", "what's working", "weekly report", "any
  problems", or a weekly scheduled task runs. Read-only against the publisher
  except for retrying failed posts with permission.
---

# Learn

Without this skill Social OS is a posting tool. With it, the brain compounds: the
owner's own results rewrite the strategy every week, in her own Drive, where she
can read it. That is the product.

Read `../../shared/drive-conventions.md`. Read `0 — Setup` for ids and timezone.
Vendor tool names are in `../publish/references/zernio-cheatsheet.md` — this skill
reads through them; it never schedules.

## Steps

1. **Health first.** Accounts health → any `needsReconnect` or `canPost: false`?
   Facebook tokens expire often. Tell her plainly and give the reconnect link via
   the connect endpoint. Nothing else matters if posts can't go out.

2. **Failures.** `posts_list status=failed` for her profile. For each: the reason in
   plain English, and the fix (reconnect / re-export media / retry). Offer
   `posts_retry` — do it only when she says so, or when `Rules for the AI` allows.

3. **Performance.** Analytics for the last 7 days, and the last 30 for context,
   sorted by engagement. For each published packet in `4 Published/`, pair the
   numbers with its topic, audience, format, hook, and CTA from the packet.

4. **Find the pattern, not the number.** Top three and bottom three, and *why* in
   terms the plan can use: which topic, format, hook shape, CTA, time. One post
   is noise; look for repeats across weeks (read last week's `What works — …`).
   Saves, shares, and DMs matter more than likes; watch time matters for Reels.

5. **Best times.** Best-time-to-post for the profile → convert UTC slots to her
   timezone. Only trust slots with a few posts behind them.

6. **Write the weekly doc** — `Learned by us/What works — YYYY-Www` (new doc, never
   replaced): health, failures, top/bottom with reasons, best times, one
   recommendation for next week. Plain English; she reads this.

7. **Update the rolling synthesis** — replace `What works (current)` with a short,
   current view: "post more of X, less of Y, at these times, because…" with the
   evidence dated. This is what `plan-week` reads. Keep it under a page.

8. **Report to `4 — Results/`** — same content, in her words, as
   `Weekly report — YYYY-Www`. Lead with anything that needs her (reconnect, film
   a Reel), then the win of the week, then the ask for next week.

9. **Move published packets.** Any `3 Approved/` packet the vendor shows as
   `published` → add `published_urls`, move to `4 Published/`.

## Rules

- Never rewrite `Told to us/`. If results contradict something she declared,
  say so in the report and let her decide.
- Never present one post's result as a rule. Tendencies, with evidence and dates.
- Never delete a weekly doc. History is how a bad inference gets caught later.

## If there is no brain yet

Search Drive for a folder named `<Business> — Social OS` and read its `0 — Setup`
doc. **If either is missing, stop and run `social-os:brand-onboarding` instead** —
this skill has nothing to read and would invent a brand. Say so in one plain line:
*"I don't have your brand set up yet — let's do that first, it takes about forty
minutes and you'll have three posts at the end."*

If Setup exists but a value this skill needs is blank, ask for that one value,
then replace the Setup doc (`../../shared/drive-conventions.md`) so nobody asks again.
