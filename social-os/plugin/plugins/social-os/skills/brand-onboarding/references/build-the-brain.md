# Build the brain — the exact creation sequence

Phase 8 of onboarding. Follow this order: a failure part-way leaves a usable
partial brain rather than a broken one. Read `${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`
first — especially that folders are files and `update_file` cannot change content.

## Step 1 — The folder tree, parents before children

A folder is `create_file` with `contentMimeType` omitted and
`mimeType: "application/vnd.google-apps.folder"`. **Each call returns the new
folder's ID; you need that ID as the `parentId` of everything inside it.** So build
top-down, holding each ID as you go.

```
create_file(title: "<Business> — AI Workspace",
            mimeType: "application/vnd.google-apps.folder")          → ROOT

with parentId = ROOT:
  "1 — Brain"          → BRAIN
  "2 — Brand Assets"   → ASSETS
  "3 — Social"        → CONTENT
  "3 — Social/Results"        → RESULTS
  "9 — Archive"        → ARCHIVE

with parentId = BRAIN:
  "Told to us"         → TOLD
  "Learned by us"      → LEARNED

with parentId = ASSETS:
  "Logos"  "Photos"  "Templates"  "Photo releases"   → RELEASES (keep this ID)

with parentId = CONTENT:
  "1 Ideas"  "2 Drafts" → DRAFTS
  "3 Approved" → APPROVED
  "4 Published" → PUBLISHED
```

Keep every ID. They all go in the Setup doc, which is what stops future sessions
from searching Drive on every run.

**If a folder with that name already exists** (re-run, or she made it herself),
reuse it rather than creating a second one: `search_files` with
`title = '…' and parentId = '<parent>' and mimeType = '…folder'` before creating.
Two folders with the same name is the worst outcome here — every later search
becomes ambiguous.

## Step 2 — The seed documents

Each file in `assets/` is the starting content for one Drive doc.
For each:

1. Read the bundled `.md` file.
2. Replace the placeholders with what the interview captured:
   `{{business_name}}` · `{{owner_first_name}}` · `{{approval_word}}` ·
   `{{timezone}}` · `{{date}}`
3. **Fill in what she actually told you.** The template is a skeleton with
   headings and prompts; replace each prompt line with her real answer. A heading
   left with its prompt underneath is a blank page in disguise — the one thing
   onboarding must never produce.
4. `create_file(title: "<doc name, no .md>", parentId: <TOLD or LEARNED or ROOT>,
   textContent: <the filled text>, contentMimeType: "text/markdown")`

| Bundled file | Drive title | Parent |
|---|---|---|
| `0 — Start Here.md` | `0 — Start Here` | ROOT |
| `Told to us/About the business.md` | `About the business` | TOLD |
| `Told to us/Brand voice.md` | `Brand voice` | TOLD |
| `Told to us/Who we talk to.md` | `Who we talk to` | TOLD |
| `Told to us/What we offer.md` | `What we offer` | TOLD |
| `Told to us/Colors and fonts.md` | `Colors and fonts` | TOLD |
| `Told to us/Rules for the AI.md` | `Rules for the AI` | TOLD |
| `Learned by us/What works.md` | `What works (current)` | LEARNED |
| `Learned by us/Her preferences.md` | `Her preferences` | LEARNED |
| `Learned by us/History.md` | `History` | LEARNED |

Also create an empty `Content Calendar` doc in CONTENT — `plan-week` fills it.

## Step 3 — Zernio

1. `profiles_list`. If a profile for this business exists, reuse its `_id`;
   otherwise `profiles_create` with the business name. **One profile per client** —
   a profile holds at most one account per platform, and profiles are free.
2. `search_tools` for the connect endpoint, then `call_tool`:
   `GET /v1/connect/instagram?profileId=<id>` → `authUrl`. Same for `facebook`.
3. Give her both links, one at a time, with what to expect:
   - **Instagram** must be **Business or Creator**. Personal accounts connect but can
     never publish. If she is on personal: Instagram app → Settings → Account type
     and tools → Switch to professional → **Creator**. Free, 30 seconds, reversible.
     Instagram Login needs no Facebook Page.
   - **Facebook** needs a **Page** she is Admin or Editor of. Personal profiles
     cannot post.
4. When she says done: `accounts_list` → record each `accountId` and platform.
5. **Verify before claiming success:** `accounts_get_all_accounts_health`. Every
   account must read `canPost: true`. If one doesn't, say exactly which and why —
   do not proceed as if it worked.

## Step 4 — The Setup doc

Write every value from `${CLAUDE_PLUGIN_ROOT}/shared/brain-layout.md` § `0 — Setup` as plain
`key: value` lines, `create_file` into ROOT. This is the index every other skill
reads first, so a missing ID here becomes a Drive search on every future run.

## Step 5 — Prove it

Run `social-os:draft-post` on the first three Content Calendar ideas. Show her the
captions. Close with the exact words that operate the system:

> "Plan my week" · "Show me the drafts" · "<approval word> <post name>"

## If something fails part-way

Say what exists and what doesn't, then offer to resume. The next run detects the
folder and the Setup doc and picks up from the first missing piece — never
re-interviews, never creates a duplicate folder.
