# Drive conventions — how every skill reads and writes the brain

Read this before touching any file in the owner's Drive. The Google Drive connector
has three properties that shape everything, and skills that ignore them silently
corrupt the brain.

## The three facts

1. **Files are Google Docs, not markdown.** `create_file` converts text content to a
   Google Doc by default. That is what we want: the owner opens and edits them
   natively, and `read_file_content` reads them back as text. Never set
   `disableConversionToGoogleType` for brain files.
2. **`update_file` changes only the title and the parent folder.** It cannot change
   content. There is no "edit this doc" tool.
3. **Folders are files** with `mimeType: application/vnd.google-apps.folder`.

## Operations

| Intent | How |
|---|---|
| **Find the brain** | `search_files` with `title = '<Business> — AI Workspace' and mimeType = 'application/vnd.google-apps.folder'`. Then read the `0 — Map` doc inside it — it holds every folder ID, every setting and every rule document, so you never search twice. Missing or unreadable → **stop and say so**; never fall back to searching. |
| **Read a doc** | `search_files` (title + `parentId`) → `read_file_content(fileId)`. Never guess an ID. |
| **Read a doc as raw text** | `download_file_content(fileId)` — exports Google Docs as plain text. |
| **Create a doc** | `create_file(title, parentId, textContent, contentMimeType: "text/markdown")`. Markdown headings survive conversion well enough to read back. |
| **Replace a doc's content** | **Rule documents: check the precondition below first.** Then `create_file` with the **same title and same parent**, then `trash_file` the old ID. Two calls. Do the create first so a failure never leaves the owner with nothing. Then re-stamp `0 — Map`. |
| **Append to history** | Do not replace — create a **new dated doc** (`What works — 2026-W39`). History is the point. |
| **Check for a hand-edit** | `get_file_metadata(fileId)` → is `modifiedTime` later than `createdTime`? See the precondition below. |
| **Move a doc between folders** | `update_file(fileId, parentId: <new folder ID>)`. This is how a post moves `2 Drafts → 3 Approved → 4 Published`. |
| **Rename** | `update_file(fileId, title)`. |
| **Retire** | `trash_file`. Never permanently delete; trash is recoverable. |

## The precondition — never overwrite a hand-edit

**Replacing a document destroys the original.** The old file is trashed; anything a
human typed into it while it was open goes with it, silently.

The owner is not supposed to edit the folder by hand — every change is meant to go
through the conversation (`the-law.md`, Law 5). But it is a promise, not a lock, and
promises get broken by accident. So **before replacing any rule document**, call
`get_file_metadata(fileId)` and compare two of its own fields:

| Reading | Means |
|---|---|
| `modifiedTime` ≈ `createdTime` | untouched since Claude wrote it — safe to replace |
| `modifiedTime` **later than** `createdTime` by more than a minute | **a human edited it — stop** |

**Compare the file against itself, not against the map.** Because replacing a
document always creates a *new* file, `createdTime` **is** the moment Claude wrote
it — which makes it an immutable anchor that stays correct even if the map's
`claude_wrote` stamp has drifted. Verified 2026-09-21: `get_file_metadata` returns
both fields as RFC3339 UTC, and `modifiedTime` is **not** reliably wall-clock — on
an uploaded file it came back *earlier* than `createdTime`, because the upload
preserved the source's mtime. A check anchored on the map stamp alone would have
inherited that.

Use `claude_wrote` as the cross-check, not the primary: if `createdTime` does not
match the stamp either, the map row is stale — heal it (`the-map.md`) before
deciding anything.

**When it is a hand-edit:** do not replace it. Read what it says now, tell her in
one line what looks different, and ask whether to keep it. If she says keep, fold
her wording into the version you write, so her edit becomes canon *through* the
system instead of sitting beside it.

This check costs one call and turns silent data loss into a question.

Records — drafts, reports, history, post packets — are exempt. They are appended,
never replaced, so there is nothing to destroy.

## Rules of the road

- **The owner owns `Told to us/`. Claude owns `Learned by us/`.** Claude may rewrite
  a `Told to us/` document **only on her explicit say-so, in the conversation** —
  that is how a correction gets recorded (`social-os:update-the-brain`). It never
  edits one on its own initiative; if something there looks wrong, say so and
  propose the change.
- **`Learned by us/` never governs.** It is evidence. When results suggest a rule
  should change, propose it and get a yes — then the change goes into `Told to us/`.
  Writing a behaviour rule into `Learned by us/` creates a second source of truth,
  which is the one thing this system must never do (`the-law.md`).
- **Replace-by-recreate changes the file ID.** So after replacing a document,
  **re-stamp its row in `0 — Map`** — new ID, `claude_wrote` set to now. When a
  stored ID fails, fall back to `search_files` by **title + parent folder** (a rule
  document's real identity) and re-stamp the map with what you found, in the same
  turn. A lookup that heals itself and never records the heal drifts again tomorrow.
- **One doc per post.** A post packet is a single Google Doc that moves through the
  folders. Its Drive file ID is the post's identity everywhere, including inside
  Zernio's `metadata`. Post packets are **not** listed in `0 — Map` — there can be
  hundreds, and they are found by folder.
- **Never store secrets in Drive.** No API keys, no tokens. Account and profile IDs
  are fine; they are not secrets.
