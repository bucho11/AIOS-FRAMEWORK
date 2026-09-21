# Migrations — the ordered list of workspace shape changes

Every change to the **shape** of an owner's workspace gets one file here and one row
below. `business-os:upgrade-workspace` reads this list, compares it to the
`workspace_version` in her `0 — Map`, and runs what's pending.

The list is **ordered and append-only**. A migration that has shipped is never
edited and never renumbered — some workspace out there has already recorded that it
ran, and changing what "3" means makes that record a lie.

| To version | Lane | What changes | File |
|---|---|---|---|
| 1 | — | the original shape: `0 — Setup`, `0 — What's Installed`, `Learned by us/Her preferences` | *(baseline — no file)* |
| 2 | **2 — migrate** | one index (`0 — Map`), and every rule moves into `Told to us/` | `001-one-index-one-rules-folder.md` |

**Current shape: version 2.** A workspace with no `workspace_version` in its map is
version 1.

---

## The two lanes

Declared per migration, because putting a change in the wrong lane is the only way
this system can do something she didn't want.

- **Lane 1 · reconcile** — purely additive. Creates what's missing. Runs silently,
  no permission. Nothing that already exists is touched.
- **Lane 2 · migrate** — renames, moves, merges, retires. **Plans first, shows her
  the exact diff, applies on one yes.**

A migration that does both is **two migrations**. Split it.

## Writing one

`NNN-short-description.md`, numbered in sequence, with these sections:

```
# NNN — <title>

**To version:** N
**Lane:** 1 (reconcile, silent) | 2 (migrate, plan then apply)
**Shipped in:** plugin vX.Y.Z

## Why

One paragraph. What was wrong with the old shape.

## Steps

Numbered. Each one states:
- what it does
- **how to tell if it already ran** (mandatory)
- what it does if it already ran (must be: nothing)

## What she sees

The exact plan lines for Lane 2, as she would read them.

## Rollback

What to do if this goes wrong. "Everything is in 9 — Archive" is a valid and
common answer — it is what makes never-delete worth the discipline.
```

**The "how to tell if it already ran" line is load-bearing.** A Cowork session can
end mid-migration for reasons that have nothing to do with us. A step that cannot
be checked cannot be resumed, and an unresumable migration is one interruption away
from a workspace nobody can repair.

## The rules that never bend

From `${CLAUDE_PLUGIN_ROOT}/shared/versioning.md`:

- **Never delete.** Supersede — rename with ` — superseded YYYY-MM-DD`, move to
  `9 — Archive/`, and point at the replacement.
- **Never reuse** a retired room number or document role. `0 — Map` keeps them under
  `## Retired`.
- **Never combine** adding the new shape with removing the old. Expand, migrate,
  contract — separate releases, in that order.
- **Every step idempotent.** Running the whole migration twice changes nothing the
  second time.
- **Readers tolerant before writers strict.** For at least one release after a
  rename, every skill reads both names.
