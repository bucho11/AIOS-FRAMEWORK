---
name: housekeeping
description: >
  The monthly maintenance pass and safety net that keeps the owner's AI workspace
  healthy for years instead of months. Audits the invariants the change-time guard
  is supposed to hold — no two documents doing the same job, the map matching what
  is really in Drive, nothing edited by hand behind our back — then archives
  published content that has aged out, compacts weekly learning notes into
  quarterly summaries, flags brain documents that have gone stale, surfaces
  accounts needing reconnection and posts nobody retried, and reports loose files
  that need a home. Use when the owner says "tidy up", "housekeeping", "is
  everything okay", "spring clean", "my folder is getting messy", or when a monthly
  scheduled task runs. Reports and proposes; never reorganises her folder without a
  yes.
---

# Housekeeping

A workspace that only grows becomes unusable in about a year. This is what stops
that — and it is the difference between a tool she abandons and a system she still
uses in year three.

Read `${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md` for the layout rules,
`${CLAUDE_PLUGIN_ROOT}/shared/the-law.md` for the invariants, and
`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md` for how to touch files. Read
`0 — Map` for the folder IDs.

## What this is, and what it is not

**This is the backstop, not the guard.** Contradictions are prevented at change
time by `business-os:update-the-brain` — because a contradiction is born the instant a
change lands, not on the first of the month, and thirty days is long enough for a
wrong rule to produce thirty pieces of wrong work.

Housekeeping assumes that guard is imperfect. It audits what the guard should have
caught, and does the maintenance that has no natural moment to happen at. If this
skill ever finds a Step-1 violation, the interesting question is not the violation —
it is *how it got past the guard*. Say so.

## The stance

**Report and propose. Do not rearrange.** Her workspace is hers. A system that
silently moves her things is one she stops trusting — and trust is the whole
product. Every change below is offered, and only the ones she says yes to happen.

The exception is genuinely mechanical: moving a post packet that has been published
for 90+ days into `9 — Archive/`. Say it is happening, do it, move on. Nothing is
lost — archive is a folder, not a shredder.

## The pass

**1 · Do the invariants still hold?** This runs first because everything else
assumes it. The full list is in `${CLAUDE_PLUGIN_ROOT}/shared/the-map.md` §
Invariants; these are the ones that need judgement:

   - **Two documents, one role.** List `1 — Brain/Told to us/`. Does anything hold a
     job another document already holds — a second voice document, a "notes" or
     "preferences" file that steers behaviour, a room-specific copy of a shared
     rule? **This is the most serious thing this skill can find.** Do not resolve it
     yourself: hand it to `business-os:update-the-brain`, which quotes both and asks
     her which is right.
   - **The map matches Drive.** Every folder and rule document in `0 — Map` still
     exists at that ID; nothing sits in `Told to us/` that the map doesn't list.
     Repair by rebuilding the map (`the-map.md`), and say you did.
   - **Nothing was edited by hand.** For each rule document, `get_file_metadata` →
     is `modifiedTime` later than its own `createdTime`? If so, someone typed into it
     directly. (`createdTime` is when Claude created it — every replacement mints a
     new file — so this holds even where the map's stamp has drifted.) Do not overwrite. Read it, tell her what changed, ask whether to keep
     it. If she wants it kept, `update-the-brain` folds it in properly.
   - **A rule is not hiding in `Learned by us/`.** Anything in there that reads like
     an instruction rather than an observation is a rule in the wrong place. Propose
     moving it into the `Told to us/` document that owns that job.
   - **No broken relationships.** Every room's connector is listed in the map's
     connections table and still connected; every document the map names still
     exists under the title claimed; no retired name is back in live use. **This is
     the failure that hides longest** — a room pointing at a disconnected service
     looks completely fine until the day she tries to use it.
   - **No upgrade left half-done.** An `FAILED` row in the upgrade history stops
     everything: hand it to `business-os:upgrade-workspace` before doing anything
     else in this pass. A half-applied shape change is worse than an old one,
     because nothing about the folder looks wrong.
   - **Is the workspace behind?** If `workspace_version` is below the current shape,
     say so in one line and offer `business-os:upgrade-workspace`. Do not migrate
     from here — that skill shows her the diff first, and this one doesn't.

**2 · Is anything broken?** Nothing else matters if posts cannot go out.
   - Account health — any `needsReconnect`, any `canPost: false`
   - Failed posts nobody retried
   - A room whose connector is no longer connected

**3 · Age out published content.** Post packets in any room's `4 Published/` older
than ~90 days move to `9 — Archive/`. They stay findable; the room stays scannable.

**4 · Compact the learning notes.** Once a quarter has fully passed, read its ~13
weekly `What works — YYYY-Www` documents and write one
`What works — YYYY Q#` that keeps what still holds and drops what was noise.
**Then archive the weeklies rather than deleting them** — a compaction that loses
the evidence cannot be audited later. Leave the current quarter's weeklies alone.

**5 · Check the brain for staleness.** For each document in `Told to us/`, when was
it last meaningfully changed? Flag — do not edit — anything that looks out of date:
   - `What we offer` unchanged for 6+ months while the business has plainly moved
   - `Brand voice` unchanged, while `History` shows repeated corrections pulling the
     same direction — that means a correction has been landing shallowly and the
     voice document is still wrong
   - `Rules for the AI` unchanged since setup, when she has been approving everything
     for months — she may be ready to let something run on its own

   That last one matters: **trust should grow as the system earns it.** Offer once,
   by category, and let her decide.

**6 · Check the registry.** Does the rooms table in `0 — Map` still match reality? A
room nobody has used in 90 days is worth asking about — pause it, or is something
blocking her? A connector listed but disconnected is a broken promise.

**7 · Mine the corrections log.** Read `Learned by us/History` for the month. Each
entry names a layer (`update-the-brain` step 8). Group them and look for repetition,
because **the same failure three times is not three corrections — it is one missing
mechanism**, and it will keep costing her attention until something changes:

   - **the same layer failing the same way 3+ times** → name it. Three `proof`
     entries about claims nobody caught is a missing check, not three bad drafts.
     **And ask why it got here:** `update-the-brain` is supposed to catch this on the
     *second* occurrence and write a preventive rule. A third occurrence in the log
     means that did not happen, so the finding is two things — the missing mechanism,
     and a correction that was handled shallowly.
   - **`toolbox` entries repeating** → something is being rebuilt weekly. That is a
     template that should exist. Propose it.
   - **`context` entries pulling one direction** → a brain document is wrong and the
     corrections have been landing shallowly. That outranks the rest of this pass.
   - **a job with no corrections in three months** → it works. Say so; that is the
     candidate to let run with less review, and trust should grow as it is earned.

   **The point is to stop paying for the same mistake.** A correction log that is
   written and never read is a diary. Propose one concrete mechanism per repeated
   pattern — a check, a template, a step — and let her pick.

**8 · Check the toolbox and the examples.** Per room:

   - `Templates/INDEX.md` lists every file that is there, and every file listed is
     there. An unindexed template is a template that gets rebuilt because nobody knew
     it existed — which is the exact waste the toolbox exists to stop.
   - `Examples/` holds at most ten, each one carrying **why** it was good. An example
     with no reason is an old post; propose retiring it or ask her what made it work.
   - A room with real output and an empty `Templates/` after two months is worth a
     question. Either nothing repeats, or nobody is noticing that it does.

**9 · Look for drift.** Loose documents that do not fit the router, three-plus files
of a kind that want a subfolder (the rule of three), a room whose inner folders have
gone empty. Name them; propose homes.

## The report

Write to `9 — Archive/Housekeeping — YYYY-MM` and say it plainly in chat. Lead with
anything that needs her, then what was tidied, then what you are proposing:

```
Needs you
- There are two documents describing how you sound — "Brand voice" and a
  "Tone notes" doc from July. They disagree about emoji. Which is right?
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

- Never delete. Supersede — renamed with the date, moved to `9 — Archive/`, still
  readable. Trash is a 30-day countdown, not a safety net.
- Never rewrite a `Told to us/` document here. Flag it; `update-the-brain` fixes it
  with her in the room.
- Never resolve a two-documents-one-role finding on your own. She decides which
  survives; the other is trashed, not merged.
- Never reorganise without a yes, except the 90-day archive sweep.
- Never compact the current quarter.
- If nothing needs attention, say so in one line. A clean month is a real result,
  not a reason to manufacture work.

## If there is no brain yet

Search Drive for a folder named `<Business> — AI Workspace` and read its
`0 — Map`. If either is missing, stop and run `business-os:brand-onboarding`
instead — there is nothing here to maintain yet.
