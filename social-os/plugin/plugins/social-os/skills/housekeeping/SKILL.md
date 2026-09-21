---
name: housekeeping
description: >
  The monthly maintenance pass that keeps the owner's AI workspace healthy for
  years instead of months: archives published content that has aged out, compacts
  weekly learning notes into quarterly summaries, flags brain documents that have
  gone stale, surfaces accounts needing reconnection and posts nobody retried,
  checks the installed-rooms registry still matches reality, and reports loose
  files that need a home. Use when the owner says "tidy up", "housekeeping", "is
  everything okay", "spring clean", "my folder is getting messy", when a monthly
  scheduled task runs, or before adding a new room to the workspace. Reports and
  proposes; never reorganises her folder without a yes.
---

# Housekeeping

A workspace that only grows becomes unusable in about a year. This is what stops
that — and it is the difference between a tool she abandons and a system she still
uses in year three.

Read `${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md` for the layout rules and
`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md` for how to touch files. Read
`0 — Setup` for the folder IDs.

## The stance

**Report and propose. Do not rearrange.** Her workspace is hers. A system that
silently moves her things is one she stops trusting — and trust is the whole
product. Every change below is offered, and only the ones she says yes to happen.

The exception is genuinely mechanical: moving a post packet that has been published
for 90+ days into `9 — Archive/`. Say it is happening, do it, move on. Nothing is
lost — archive is a folder, not a shredder.

## The pass

**1 · Is anything broken?** Lead with this; nothing else matters if posts cannot go
out.
   - Account health — any `needsReconnect`, any `canPost: false`
   - Failed posts nobody retried
   - A room whose connector is no longer connected

**2 · Age out published content.** Post packets in any room's `4 Published/` older
than ~90 days move to `9 — Archive/`. They stay findable; the room stays scannable.

**3 · Compact the learning notes.** Once a quarter has fully passed, read its ~13
weekly `What works — YYYY-Www` documents and write one
`What works — YYYY Q#` that keeps what still holds and drops what was noise.
**Then archive the weeklies rather than deleting them** — a compaction that loses
the evidence cannot be audited later. Leave the current quarter's weeklies alone.

**4 · Check the brain for staleness.** For each document in `Told to us/`, when was
it last meaningfully changed? Flag — do not edit — anything that looks out of date:
   - `What we offer` unchanged for 6+ months while the business has plainly moved
   - `Brand voice` never corrected, when `Her preferences` shows repeated corrections
     in the same direction — that means the voice file is wrong and nobody fixed it
   - `Rules for the AI` unchanged since setup, when she has been approving everything
     for months — she may be ready to let something run on its own

   That last one matters: **trust should grow as the system earns it.** Offer once,
   by category, and let her decide.

**5 · Check the registry.** Does `0 — What's Installed` still match reality? A room
nobody has used in 90 days is worth asking about — pause it, or is something
blocking her? A connector listed but disconnected is a broken promise.

**6 · Look for drift.** Loose documents that do not fit the router, three-plus files
of a kind that want a subfolder (the rule of three), a room whose inner folders have
gone empty. Name them; propose homes.

## The report

Write to `9 — Archive/Housekeeping — YYYY-MM` and say it plainly in chat. Lead with
anything that needs her, then what was tidied, then what you are proposing:

```
Needs you
- Facebook needs reconnecting — here's the link
- 2 posts failed last month and were never retried

Done
- Archived 14 published posts from June–July
- Compacted Q2's weekly notes into one summary

Worth a look
- "What we offer" hasn't changed since March, but you've added overnight care
- You've approved every post for 11 weeks — want me to schedule the
  availability posts without asking, and keep asking on everything else?
```

## Rules

- Never delete. Archive.
- Never move a document out of `Told to us/` — that is hers.
- Never reorganise without a yes, except the 90-day archive sweep.
- Never compact the current quarter.
- If nothing needs attention, say so in one line. A clean month is a real result,
  not a reason to manufacture work.

## If there is no brain yet

Search Drive for a folder named `<Business> — AI Workspace` and read its
`0 — Setup`. If either is missing, stop and run `social-os:brand-onboarding`
instead — there is nothing here to maintain yet.
