---
name: learn
description: >
  The weekly learning loop that makes next week better than this week: pull real
  Instagram and Facebook performance from the publisher, find what worked and why,
  detect failed posts and accounts that need reconnecting, check the best posting
  times, write a plain-English report to 3 — Social/Results, and update Learned by us /
  What works (current) so plan-week and draft-post read it next time. Use whenever
  the owner says "how did we do", "what's working", "weekly report", "any
  problems", or a weekly scheduled task runs. Read-only against the publisher
  except for retrying failed posts with permission.
---

# Learn

Without this skill the social room is a posting tool. With it, the brain compounds: the
owner's own results rewrite the strategy every week, in her own Drive, where she
can read it. That is the product.

Read `${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md` and
`${CLAUDE_PLUGIN_ROOT}/shared/the-law.md`. Read `0 — Map` for ids and timezone.
Vendor tool names are in `${CLAUDE_PLUGIN_ROOT}/skills/publish/references/zernio-cheatsheet.md` — this skill
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
   recommendation for next week. Plain English; she reads this. Observations and
   evidence only — if something here reads like an instruction, it belongs in
   `Told to us/` and needs her yes first (see below).

7. **Update the rolling synthesis** — replace `What works (current)` with a short,
   current view: "post more of X, less of Y, at these times, because…" with the
   evidence dated. This is what `plan-week` reads. Keep it under a page.

8. **Report to `3 — Social/Results/`** — same content, in her words, as
   `Weekly report — YYYY-Www`. Lead with anything that needs her (reconnect, film
   a Reel), then the win of the week, then the ask for next week.

9. **Move published packets.** Any `3 Approved/` packet the vendor shows as
   `published` → add `published_urls`, move to `4 Published/`.

10. **Save this week's best as an example.** The top performer, copied into the
    room's `Examples/` as `YYYY-MM-DD — <what made it good>`, with two or three lines
    on **why** it worked: the hook shape, the audience, the format, the slot.

    An example with no reason on it is just an old post. The reason is the whole
    value — it is what `draft-post` reads to write the next one, and it is far
    stronger training than any description of her voice, because it is her voice
    proven against her own audience.

    Keep the **ten best per room**, not the ten most recent. When an eleventh
    arrives, retire the weakest to `9 — Archive/` (superseded, never trashed) and say
    which one in the report.

    Examples are **records** (`the-law.md`, Law 2). They show what worked; they never
    override `Brand voice`. If an example and the voice document disagree, the voice
    document wins and the disagreement is worth raising with her.

11. **Run the checks.** `${CLAUDE_PLUGIN_ROOT}/skills/learn/references/checks.md`.
    The first one is the one that matters: **every number in the report traces to the
    analytics response it came from.** A report she cannot trace is a report she
    cannot correct, and she will act on it anyway.

## When the results say a rule is wrong

This is the moment the whole contradiction discipline is built for, and it happens
here more than anywhere else.

Results will sometimes suggest a change to something she declared — the voice is too
formal, the audience is wrong, an offer isn't landing. **Do not write that into
`Learned by us/`.** A rule living in the evidence folder is a second source of
truth that quietly competes with `Told to us/` forever, and nobody can see which one
is winning (`the-law.md`, Law 2).

Instead: **propose it.** One line in the report, in her words, with the evidence and
the date. If she says yes, `business-os:update-the-brain` rewrites the `Told to us/`
document that owns that job — one document, replaced, blast radius handled.

> Your three best posts this month all dropped the exclamation points. **Brand
> voice** still says to use them. Want me to change it?

`What works (current)` stays what it is: a guide to choosing *between things the
rules already allow* — which topic, which format, which time slot. It never decides
what is allowed.

## Done means

A dated weekly document in `Learned by us/`, a rolling `What works (current)` under
a page, a report in the room's `Results/` that leads with anything needing her, every
published packet moved and recorded, this week's best saved as an example with its
reason, and an evidence report showing every number traced.

## Rules

- Never rewrite `Told to us/` from here. Propose; she decides; `update-the-brain`
  writes it.
- Never write an instruction into `Learned by us/`. Observations only, with dates.
- Never present one post's result as a rule. Tendencies, with evidence and dates.
- Never delete a weekly doc. History is how a bad inference gets caught later.

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

If the map exists but a value this skill needs is blank, ask for that one value,
then re-stamp the map (`${CLAUDE_PLUGIN_ROOT}/shared/the-map.md`) so nobody asks
again.
