# The map — one document that replaces every search

`0 — Map` sits at the top of the owner's workspace. **Every skill reads it first and
almost never needs to read anything else to find its way.** It is the reason this
system does not get slower as her workspace grows.

It replaces the two index documents earlier versions used (`0 — Setup` and
`0 — What's Installed`). Two index documents can disagree about which folder the
drafts are in. One cannot.

---

## What it is for

**Three jobs, and the third is the one people miss.**

1. **Navigation.** Every folder ID and every rule document, in one read. No
   searching, no guessing, no walking the tree.
2. **Settings.** The values skills need — timezone, account IDs, what she's capable
   of each week.
3. **The contradiction index.** It lists every rule document *and the role it
   holds*. That is what makes Law 1 checkable in one call instead of a Drive sweep.
   A check that is expensive is a check that stops running.

## What it is NOT for

**Content.** The map holds pointers, never prose. One line per thing, about fifteen
words. If the map starts explaining her brand voice, it has become a second brand
voice document and it is now the problem it was built to prevent.

**Records.** Post packets, weekly reports and history entries are never in the map.
There can be hundreds of them and they are found by folder. This is what keeps the
map roughly **thirty lines forever** instead of growing with her workspace.

---

## Its shape

Plain `key: value` lines and simple tables, so it survives conversion to a Google
Doc and reads back cleanly.

```
# Map

workspace_version: 2
Last rebuilt: 2026-09-21

## Settings

business_name: Lifetime of Love Nannies — Reno
timezone: America/Los_Angeles
approval_word: approve
posting_capacity_per_week: 4
reels_she_can_film_per_week: 2
canva_available: yes            ← no ⇒ photo/video/text posts only, no graphics
recruiting_in_scope: yes
zernio_profile_id: <24-hex>
zernio_instagram_account_id: <24-hex>    (blank until connected)
zernio_facebook_account_id: <24-hex>     (blank until connected)

## Folders

| Folder | Drive ID |
|---|---|
| root                      | <id> |
| 1 — Brain/Told to us      | <id> |
| 1 — Brain/Learned by us   | <id> |
| 2 — Brand Assets          | <id> |
| 2 — Brand Assets/Photo releases | <id> |
| 3 — Social/1 Ideas        | <id> |
| 3 — Social/2 Drafts       | <id> |
| 3 — Social/3 Approved     | <id> |
| 3 — Social/4 Published    | <id> |
| 3 — Social/Results        | <id> |
| 9 — Archive               | <id> |

## Rule documents

One role per row. Two rows may never share a role.

| Document | Role — the one question it answers | Drive ID | claude_wrote |
|---|---|---|---|
| About the business    | what this business is and where          | <id> | 2026-09-21T18:04Z |
| Brand voice           | how she sounds                           | <id> | 2026-09-21T18:04Z |
| Who we talk to        | who we are speaking to                   | <id> | 2026-09-21T18:04Z |
| What we offer         | what she sells and for how much          | <id> | 2026-09-21T18:04Z |
| Colors and fonts      | what it looks like                       | <id> | 2026-09-21T18:04Z |
| Rules for the AI      | what the AI may do without asking        | <id> | 2026-09-21T18:04Z |
| How she likes to work | how she wants to be worked with          | <id> | 2026-09-21T18:04Z |

## Rooms

| Room | What it's for | Connector | Added | Last used |
|---|---|---|---|---|
| 3 — Social | Instagram and Facebook, idea to published | Zernio, Canva | 2026-09-21 | 2026-09-21 |

## Connections

| Service | What it does | Status |
|---|---|---|
| Google Drive | holds this workspace | connected |
| Zernio | publishes and schedules, hosts photos | connected |
| Canva | branded graphics | connected |

## Upgrade history

| To version | When | Result |
|---|---|---|
| 2 | 2026-09-21T18:04Z | done |

## Retired

Never reused. Old notes and old links still point at these names.

| Name | Retired | Replaced by |
|---|---|---|
| 0 — Setup | 2026-09-21 | 0 — Map |
| 0 — What's Installed | 2026-09-21 | 0 — Map |
| Her preferences | 2026-09-21 | Brand voice · Rules for the AI · How she likes to work |
```

**`workspace_version`** is the shape of her folder, and it is not the plugin's
version — see `${CLAUDE_PLUGIN_ROOT}/shared/versioning.md`. A map with no
`workspace_version` is version 1.

**The upgrade history is not decoration.** A row reading `FAILED` is how a
half-applied change becomes visible instead of silently pending, and it is the one
thing standing between an interrupted session and a workspace nobody can repair.
`business-os:upgrade-workspace` writes it, reads it, and refuses to do anything else
while one is open.

**`## Retired`** exists because every name in this system is referenced from outside
it — her own memory, an old report, an archived document. Reusing a retired room
number or document role makes all of those quietly point at the wrong thing, with
nothing to notice.

---

## Reading it

1. `search_files` for the folder `<Business> — AI Workspace`.
2. Read `0 — Map` inside it.
3. That is the whole orientation. Go straight to what you need.

**If `0 — Map` is missing or unreadable, stop.** Do not fall back to searching the
folder — a silent fallback is how nobody notices the map died. Say so and rebuild it
with `business-os:update-the-brain`, or run `business-os:brand-onboarding` if there is no
workspace at all.

## Looking up a document

**Read by ID first; heal on a miss.** Drive IDs in this system churn, because
replacing a document's content means creating a new file (see
`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`). So:

1. Try the ID from the map.
2. If it fails, or the title does not match, `search_files` by **title + parent
   folder** — the true identity of a rule document.
3. **Re-stamp the map row with the ID you found**, in the same turn. A map that
   heals itself silently and never records the heal will drift again tomorrow.

## Writing it

**Re-stamp on every rule-document write.** Whenever a rule document is created or
replaced, update its row — the new `Drive ID` and `claude_wrote` set to now, in UTC.

That stamp is load-bearing twice over: it is how a lookup stays fast, and it is the
cross-check on a hand-edit. The hand-edit test itself compares the file against
**itself** — `modifiedTime` later than `createdTime` means a human touched it after
Claude wrote it — because `createdTime` is immutable and stays right even if this
stamp has drifted. A `createdTime` that does not match the stamp means the row is
stale: heal it before deciding anything. Full rule: `drive-conventions.md`.

**Rebuild the whole map** — walk the folders, confirm every ID, rewrite it — only
in three cases:

- at the end of `brand-onboarding`
- when a room is added
- when the map is wrong, missing, or contradicts what is actually in Drive

Replace it the same way as any other document: create, then trash the old
(`drive-conventions.md`). The map's *own* ID is not stored anywhere — it is found by
title in the root folder, which never changes.

## Invariants — what `housekeeping` checks

The map is not self-validating. Every configuration registry that nobody audits goes
stale the same way, and the documented failure modes are always the same five:
missing entries, wrong attributes, broken relationships, duplicates, and rows that
outlived the thing they described. So these are checked on a cadence, not assumed:

1. **Every role appears at most once.** Two rows with the same job is the failure
   state (`the-law.md`, Law 1).
2. **Every Drive ID resolves**, and the document it resolves to has the title the row
   claims. A miss is healed by title + parent, then re-stamped.
3. **Every folder in the table exists**, and nothing in `Told to us/` is missing from
   the table.
4. **Every room's connector is in the connections table**, and still connected. A
   room pointing at a service that isn't there is a broken relationship — the
   failure mode that hides longest, because the room looks fine until she uses it.
5. **No retired name is in live use.**
6. **No upgrade history row reads `FAILED`.**

A violation of 1 or 6 stops other work. The rest are reported and proposed.

## The format lives here and nowhere else

Every skill that writes a row reads **this file** for the shape first. The format
written down in two places is two formats. If a row needs a new column, it changes
here, and here only.
