---
name: upgrade-workspace
description: >
  Brings an owner's workspace up to the current shape when the system has changed
  since it was built, and repairs one that is out of shape. Runs two ways: quietly
  filling in anything missing (a folder, a document, a map row) without asking,
  and — for anything that renames, moves, merges or retires — showing her exactly
  what will change before it changes, then doing it on one yes. Use at the start of
  any session where the workspace version is behind, when a document or folder the
  map promises is not there, when the map disagrees with what is actually in Drive,
  when a previous upgrade is recorded as FAILED, or when the owner says "is my setup
  current", "something's missing", "this looks broken", or "update my workspace".
  Never deletes, always resumable, safe to run twice.
---

# Upgrade workspace

The system will change over the years. Her folder was built by whatever version
existed the day she signed up, and it is only reachable when a session happens to
run — there is no way to upgrade everyone at once, and a client who doesn't open
Cowork for six weeks **is** a client running an old shape.

So this skill assumes divergence is normal, and makes closing it boring.

Read `${CLAUDE_PLUGIN_ROOT}/shared/versioning.md` (the two version numbers and the
change rules), `${CLAUDE_PLUGIN_ROOT}/shared/the-map.md`, and
`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`. The ordered list of shape
changes is `${CLAUDE_PLUGIN_ROOT}/migrations/_index.md`.

---

## Two lanes, and putting a change in the wrong one is the whole risk

**Lane 1 · Reconcile — silent, no permission, whenever you notice.**

Purely additive. Something the current shape says should exist, and doesn't:

- a folder the map lists that isn't in Drive
- a rule document that was added in a later version and she has never had
- a map row missing for a document that does exist
- a stale Drive ID, healed by finding the document by title and parent

**This is not changing her stuff. It is the system finishing building itself.** She
never asked for an empty `Photo releases` folder to be missing. Create it, mention
it in half a line if it's worth mentioning, move on. Asking permission to fix your
own gaps is noise, and noise is what makes people stop reading what you say.

This lane runs continuously — any skill that notices a gap fixes it. That is the
Kubernetes model: observe actual state, move it toward desired state, forever.

**Lane 2 · Migrate — plan, show the diff, then apply on one yes.**

Anything that **renames, moves, merges, retires, or restructures** something she
already has. This touches work she has looked at, referred to, and built a mental
model of.

Here the standard is Terraform's, and the reason is stated plainly in its own
design: a visible diff before action exists *because changes are risky and often
destructive, and operators need to know exactly what will be created, changed, or
destroyed before committing.* Her workspace deserves at least what a server gets.

**Never run Lane 2 silently. Never run Lane 1 with a prompt.** A rearrangement she
didn't see coming is how trust dies; a permission dialog for creating a missing
folder is how attention dies.

---

## The pass

### 1 · Read where she is

From `0 — Map`: `workspace_version` (no value ⇒ treat as `1`) and the upgrade
history table.

**A `FAILED` row outranks everything.** A half-applied change is the actual source
of chaos — worse than an old shape, because nothing about the folder looks wrong.
Go to *Resuming a failed upgrade* below before anything else.

### 2 · Work out what is pending

Read `migrations/_index.md`. Every entry above her `workspace_version`, in order, is
pending. Each declares its **lane**.

Nothing pending and no gaps → **say nothing at all** and carry on with what she
actually asked for. A clean check is not an achievement worth reporting.

### 3 · Reconcile (Lane 1) — just do it

Run every pending Lane-1 step, plus any gap you noticed: create what's missing from
its seed text, add the missing map rows, heal the stale IDs. Guard every step —
create only if absent, so running twice changes nothing the second time.

Then re-stamp the map and record the version reached.

### 4 · Plan (Lane 2) — write the diff before you touch anything

For every pending Lane-2 step, build the list of exactly what would change, in her
words, grouped the way Terraform groups it — because the grouping is what makes a
diff skimmable:

```
Your workspace can update. Here's exactly what changes:

  CREATE   "How she likes to work"  in 1 — Brain / Told to us
  RENAME   "0 — Setup"  →  "0 — Map"
  MOVE     "Her preferences"  →  9 — Archive  (superseded, kept)
  MERGE    "Tone notes"  into  "Brand voice"  (I'll ask about the 2 places they disagree)

Nothing is deleted. Nothing you've written is lost. Want me to go ahead?
```

**Rules for the plan:**

- **Every line is a real change.** Never pad it with things that are already true.
- **Name the documents as she sees them**, never a path or an ID.
- **State the reassurance once**, because it is true and it is the only thing she
  actually needs to decide: nothing is deleted.
- **If a step needs her judgement** — two documents that disagree — say so in the
  plan and ask *after* she approves the plan, one question at a time. Do not make
  her answer content questions before she has agreed to the upgrade at all.
- **If the plan is one boring line**, still show it. A one-line diff takes her two
  seconds; a surprise takes her trust.

### 5 · Apply — in order, recording as you go

On her yes, run the steps **in migration order**, and after each one:

- **write the map** — the version reached, the new IDs, the history row
- never batch the recording to the end; a session that dies mid-way must leave a
  truthful record behind, which is the entire reason the history exists

If a step fails: **stop**. Do not continue to the next one. Write the history row
as `FAILED` with what was done and what wasn't, in plain words. Tell her which parts
landed and that nothing was lost. A stopped upgrade with an honest record is
recoverable in one minute; a half-applied one that claims success is not.

### 6 · Confirm, briefly

> Done — your workspace is up to date. The two documents that said the same thing
> are now one, and the old one is in Archive if you ever want it.

Then go back to whatever she originally asked for.

---

## Resuming a failed upgrade

The history says `FAILED`. Do not re-run the whole thing blind and do not assume
nothing happened.

1. **Look at what is actually there.** Every migration step is written to be
   checkable — the document exists or it doesn't, the folder is there or isn't.
2. **Skip what already landed.** This is why steps are guarded; a completed step
   run again is a no-op, not a duplicate.
3. **Run the rest**, recording after each.
4. **Clear the FAILED row** by appending a new row for the same version with the
   real result. Never edit the old row away — a failure that happened is a record,
   and records are not rewritten (`the-law.md`, Law 2).

If you genuinely cannot tell what state a step left behind, **stop and say so**,
naming the one thing you're unsure about. A wrong guess here costs her a document.

---

## Writing a migration

One file in `migrations/`, named `NNN-short-description.md`, listed in
`_index.md`. It declares, in this order: the **version it moves to**, its **lane**,
**why** it exists, the **exact steps**, and **how to tell if each step already ran.**

That last one is not optional. A step you cannot check is a step that cannot be
resumed, and an unresumable migration is one failure away from a workspace nobody
can repair.

**Hard rules, from `shared/versioning.md`:**

- **Never delete.** Supersede: rename with ` — superseded YYYY-MM-DD`, move to
  `9 — Archive/`, and leave a line in the replacement saying where it came from.
- **Never reuse** a retired room number or document role. `0 — Map` keeps a
  `## Retired` list; old notes and old links still point at those names.
- **Never combine** adding a new shape with removing the old one. Those are separate
  releases — expand, then migrate, then contract.
- **Every step idempotent**, so running twice is harmless.

## Rules

- Lane 1 never asks. Lane 2 never assumes.
- Never delete. Never trash. Archive, superseded, with a pointer.
- Never continue past a failed step.
- Never report success for a step that did not complete.
- Never touch a document whose `modifiedTime` is later than its `createdTime`
  without asking — she edited it by hand (`drive-conventions.md`).
- If nothing is pending, say nothing.

## If there is no workspace yet

Nothing to upgrade. Run `business-os:brand-onboarding`.
