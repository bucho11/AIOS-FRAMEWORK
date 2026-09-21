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
| **Find the brain** | `search_files` with `title = '<Business> — AI Workspace' and mimeType = 'application/vnd.google-apps.folder'`. Then read the `0 — Setup` doc inside it — it holds every folder ID so you never search twice. |
| **Read a doc** | `search_files` (title + `parentId`) → `read_file_content(fileId)`. Never guess an ID. |
| **Read a doc as raw text** | `download_file_content(fileId)` — exports Google Docs as plain text. |
| **Create a doc** | `create_file(title, parentId, textContent, contentMimeType: "text/markdown")`. Markdown headings survive conversion well enough to read back. |
| **Replace a doc's content** | `create_file` with the **same title and same parent**, then `trash_file` the old ID. Two calls. Do the create first so a failure never leaves the owner with nothing. |
| **Append to history** | Do not replace — create a **new dated doc** (`What works — 2026-W39`). History is the point. |
| **Move a doc between folders** | `update_file(fileId, parentId: <new folder ID>)`. This is how a post moves `2 Drafts → 3 Approved → 4 Published`. |
| **Rename** | `update_file(fileId, title)`. |
| **Retire** | `trash_file`. Never permanently delete; trash is recoverable. |

## Rules of the road

- **The owner owns `Told to us/`. Claude owns `Learned by us/`.** Claude reads
  `Told to us` and never rewrites it; if something there looks wrong, say so and let
  the owner change it. Claude writes `Learned by us` and the owner reads it.
- **Replace-by-recreate changes the file ID.** After replacing a doc, if its ID is
  recorded anywhere (the Setup doc, a post packet), update that record too. Prefer
  finding docs by **title + parent folder** rather than by stored ID, precisely
  because IDs churn.
- **One doc per post.** A post packet is a single Google Doc that moves through the
  folders. Its Drive file ID is the post's identity everywhere, including inside
  Zernio's `metadata`.
- **Never store secrets in Drive.** No API keys, no tokens. Account and profile IDs
  are fine; they are not secrets.
