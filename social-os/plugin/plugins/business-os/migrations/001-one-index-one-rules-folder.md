# 001 — One index, one rules folder

**To version:** 2
**Lane:** 2 (migrate — plans first, applies on one yes)
**Shipped in:** plugin v0.3.0

## Why

Version 1 had two problems that are the same problem.

**Two index documents.** `0 — Setup` held IDs and settings; `0 — What's Installed`
held the room and connector registry. Two documents can disagree about which folder
the drafts are in. One cannot. They merge into `0 — Map`, which also gains the one
thing neither had: a row per rule document naming **the single job it holds**, so
"is there already a document for this?" is answerable in one read.

**A second source of behaviour.** `Learned by us/Her preferences` shipped with seed
text reading *"If you tell Claude 'never say X' or 'always do Y', it lands here and
holds from then on."* That is a claim of authority, from a document sitting beside
`Brand voice`, which is the other document about how to write. Two documents, one
job — the exact failure the system exists to prevent, seeded on day one.

Its content splits to where each piece belongs: voice corrections into
`Brand voice`, permissions into `Rules for the AI`, and how she wants to be worked
with into a new rule document, `Told to us/How she likes to work`.

## Steps

Run in order. Record the map after each.

**1 · Create `Told to us/How she likes to work`.**
Seed from the `How she likes to work.md` file in
`${CLAUDE_PLUGIN_ROOT}/skills/brand-onboarding/assets/`.
*Already ran?* A document with that title exists in `Told to us/`.
*If so:* nothing.

**2 · Move anything behaviour-shaped out of `Her preferences`.**
Read it. For each line, route it to the rule document that owns that job — voice to
`Brand voice`, permissions to `Rules for the AI`, working style to
`How she likes to work`. **Show her each line and where it's going before writing**;
these are her words and she may disagree about where they belong. If the document
is empty or only holds the seed table, skip silently.
*Already ran?* `Her preferences` is not in `Learned by us/` — step 3 moved it.
*If so:* nothing.

**3 · Supersede `Her preferences`.**
Rename to `Her preferences — superseded YYYY-MM-DD`, move to `9 — Archive/`.
**Never trash it** — it is where her corrections lived, and it stays readable.
*Already ran?* Not in `Learned by us/`.
*If so:* nothing.

**4 · Build `0 — Map`.**
Read `0 — Setup` and `0 — What's Installed`. Write `0 — Map` in the root, in the
exact shape in `${CLAUDE_PLUGIN_ROOT}/shared/the-map.md` — settings, folder IDs, one
row per rule document with its single job and a `claude_wrote` stamp, rooms,
connections. Set `workspace_version: 2`.
*Already ran?* `0 — Map` exists in the root and carries `workspace_version`.
*If so:* nothing.

**5 · Supersede the two old index documents.**
`0 — Setup` and `0 — What's Installed` → rename with ` — superseded YYYY-MM-DD`,
move to `9 — Archive/`.
*Already ran?* Neither is in the root.
*If so:* nothing.

**6 · Record the retirements.**
In `0 — Map` under `## Retired`, list the three roles so nothing ever reuses them:
`0 — Setup`, `0 — What's Installed`, `Her preferences`.
*Already ran?* All three appear under `## Retired`.
*If so:* nothing.

## What she sees

```
Your workspace can update — it's a tidy-up, and nothing gets deleted.

  CREATE   "How she likes to work"  in 1 — Brain / Told to us
  MOVE     the notes in "Her preferences"  →  the document each one belongs to
           (I'll show you each one first)
  CREATE   "0 — Map"  — one index instead of two
  ARCHIVE  "0 — Setup", "0 — What's Installed", "Her preferences"
           (renamed "superseded", kept in 9 — Archive)

Why: you had two documents that could disagree about how you sound, and two
indexes that could disagree about where things live. After this there's one
of each. Go ahead?
```

## Rollback

Everything superseded is in `9 — Archive/` under its original name plus a date. To
undo: move the three documents back to their original folders, drop the date suffix,
trash `0 — Map`, and set nothing — a workspace with no `workspace_version` reads as
version 1 and the system handles it.

Nothing in this migration deletes, so rollback is always possible.
