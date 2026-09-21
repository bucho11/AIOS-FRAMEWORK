# Zernio cheat-sheet — verified against docs.zernio.com and the live MCP, 2026-09-20

Server: `https://mcp.zernio.com/mcp`. OAuth 2.1 + PKCE with dynamic client
registration (the owner signs in; no key to paste) or `Authorization: Bearer sk_…`.
`tools/list` returns ~50 tools; the rest are behind `search_tools` → `call_tool`.

## Live verification — 2026-09-21, real account, `[PRIMARY]`

Auth, accounts, health, quota, media round-trip and a full dry-run post all pass.
`tools/list` returned **52** tools. Confirmed by running it:

- **`validate_post`** is the pre-flight: same checks as creation, publishes nothing,
  returns `{"valid": true, "message": "No validation issues found."}`. **Use it every
  time.** A real cross-posted IG+FB body with media, `firstComment`, `scheduledFor`
  and `timezone` validated clean.
- **A presigned `publicUrl` 404s until the file is PUT.** Validate after upload, never
  before. `PUT` to `uploadUrl` with the same `Content-Type` → HTTP 200.
- **Zernio fetches external URLs server-side** — a `raw.githubusercontent.com` URL
  validated `valid: true` with correct type and size. So a live Canva export URL can
  be passed directly as `mediaItems[].url`.
- **Redirecting URLs fail** — `picsum.photos/1080` → *"URL returned HTTP 404"*.
  Consistent with the docs' warning about Drive/Dropbox links.
- **Live Instagram quota: `quotaTotal: 100`**, `quotaDurationSeconds: 86400`. Settles
  the 25-vs-50-vs-100 question; still read it at run time.
- `validate_media` returns per-platform `withinLimit` — it reports **Facebook 10 MB**
  while the Facebook platform page says 4 MB "rejected in practice". **Trust 4 MB.**
- `validate_post_length` takes **`text`**, not `content`.
- **Comment automations are NOT in the core 52** — use `search_tools` → `call_tool`.

## Core tools

`accounts_list` · `accounts_get` · `profiles_list/get/create/update/delete` ·
`posts_list/get/create/update/delete` · `posts_publish_now` · `posts_cross_post` ·
`posts_retry` · `posts_list_failed` · `posts_retry_all_failed` ·
`media_generate_upload_link` · `media_check_upload_status` · `docs_search` ·
`search_tools` · `call_tool`

### `posts_create` (assistant-shaped)
`content` · `platform` (instagram | facebook | …) · `account_id` · `profile_id` ·
`is_draft` · `publish_now` · `schedule_minutes` (default 60) · `media_urls`
(comma-separated public URLs) · `title`

| `is_draft` | `publish_now` | Result |
|---|---|---|
| true | any | draft, not scheduled |
| false | true | published now |
| false | false | scheduled `schedule_minutes` from now |

Write tools **refuse an ambiguous account** and list candidates — call
`accounts_list`, retry with `account_id`.

### REST shape (via `call_tool` / generated tools) — for exact times and extras
`POST /v1/posts`: `content`, `mediaItems[{url,type}]`, `platforms[{platform,
accountId, platformSpecificData}]`, `scheduledFor` (ISO; no offset ⇒ read in
`timezone`), `timezone` (IANA), `publishNow`, `isDraft`, `metadata` (free-form —
put our packet ID here; it comes back on every webhook/read), header
`x-request-id` (UUID per logical post; retries return the original). Identical
content to the same account within **24 h → 409**. `scheduledFor` in the past
publishes immediately.
`PUT/PATCH /v1/posts/{id}` (update): to promote a draft send **`isDraft: false`
together with `scheduledFor`** (or `publishNow`). `scheduledFor` alone → 200 but
still a draft.
`queuedFromProfile` schedules into the profile's queue slots instead of a fixed time.

### Instagram `platformSpecificData`
`contentType: "story"` · `shareToFeed` (Reels) · `firstComment` (links + hashtags —
captions have no live links) · `locationId` (numeric Facebook Page id with location
data) · `collaborators[]` · `userTags[]` · `instagramThumbnail` / `thumbOffset` ·
`commentsEnabled` · `isAiGenerated` · `isPaidPartnership` · `muteAudio`

### Media
- `mediaItems[].url` must be public HTTPS returning the file. **Google Drive,
  Dropbox, OneDrive, iCloud links fail** (HTML, not the file).
- `POST /v1/media/presign` → `uploadUrl` (1 h) + `publicUrl` (`media.zernio.com/…`),
  ≤ 5 GB. MCP path: `media_generate_upload_link` → owner drops file in browser
  (30-min link) → `media_check_upload_status(token)` → `media_urls`.
- Uploads sit in **temp storage 7 days**; copied to permanent when the post publishes.
- Zernio **compresses** images/videos above a platform limit (Facebook's 4 MB is
  handled). `customMedia` on a platform entry overrides `mediaItems` for that one.
- `POST /v1/tools/validate/media {url}` → content type, size, per-platform checks.

### Limits (verified on Zernio's platform pages)
| | Instagram | Facebook |
|---|---|---|
| Caption | 2,200 chars | 63,206 (truncates ~480) |
| Images / post | 1 feed · 10 carousel · JPEG/PNG · 8 MB | 10 · JPEG/PNG/GIF · 4 MB |
| Video | MP4/MOV · 300 MB feed & Reels · 100 MB Story | MP4/MOV · 4 GB |
| Reel | **90 s** | **60 s** |
| Story | 60 s | 120 s |
| Account | Business/Creator; Instagram Login needs no Page | Page; Admin/Editor; tokens expire often |
| Publish cap | `GET /v1/accounts/{id}/instagram/publishing-limit` → `quotaUsage`/`quotaTotal` (docs say 100/24 h; **trust the live value**) | — |

### Connect, health, analytics, automations
- `GET /v1/connect/{platform}?profileId=…` → `authUrl` for the owner to click.
- `GET /v1/accounts/health` → `summary.needsReconnect`, per-account `canPost`,
  `status: healthy|warning|error`.
- `GET /v1/analytics` (postId | platform, profileId, fromDate, toDate, sortBy
  engagement) · `GET /v1/analytics/best-time` → `slots[{day_of_week 0=Mon, hour UTC,
  avg_engagement, post_count}]` · content-decay · posting-frequency ·
  instagram-account-insights · facebook-page-insights. Included on usage-based plans.
- `POST /v1/comment-automations` → `profileId`, `accountId`, `name`, `keywords[]`,
  `matchMode: exact|contains|word`, `typoTolerance`, `excludeKeywords[]`,
  `dmMessage` (≤ 640 with buttons, ~1000 without), `buttons[]` (1–3),
  `commentReply`, `alsoMatchInDms`, `trigger: comment|story_reply`,
  `platformPostId` or `postId` (binds to a not-yet-published Zernio post), delays,
  `linkTracking`, `clickTag`.
- Webhooks exist (`post.published`, `post.failed`, `post.partial`,
  `account.disconnected`, `comment.received`, …) but need a receiving server; v1
  polls `posts_get` / `posts_list` instead.

### Errors
`type`: invalid_request_error · authentication_error · permission_error · not_found ·
rate_limit_error · platform_error (carries `platformError` verbatim from Meta,
incl. `error_subcode`, `error_user_msg`) · api_error. `ACCOUNT_DISCONNECTED` ⇒
reconnect, then refresh ids from `accounts_list`. **207** on multi-platform
publish means some platforms failed — branch on the status code.

### Billing (why this is $0 for one client)
First 2 connected accounts free; profiles free and unlimited; every account gets
every feature. 3–10 accounts $6 · 11–100 $3 · 101+ $1, graduated.
