# VERIFIED FACTS

> Ground truth. Append-only. Every row carries a tag and a date.
> **When this file and your memory disagree, this file wins.**
>
> `[PRIMARY]` = fetched from the vendor's own live docs/API. `[SECONDARY]` =
> research citing third parties — verify before spending money or writing code.

All entries verified **2026-09-19** unless noted.

---

## Claude Cowork

| Fact | Tag |
|---|---|
| Two execution modes: **cloud sessions** (Anthropic-managed sandbox, files stored in the member's Claude account) and **local sessions** (agent loop on device, code in an isolated VM) | `[PRIMARY]` |
| Local sessions: "Claude can only read and write files in folders you've connected" | `[PRIMARY]` |
| Supports **Skills**, **Plugins** (bundle skills + connectors + sub-agents), and **custom MCP** via remote MCP + desktop extensions | `[PRIMARY]` |
| Available on **Pro, Max, Team, Enterprise**. Paid plans only. Desktop, web, mobile, Chrome | `[PRIMARY]` |
| **Scheduled tasks run remotely** — verbatim: *"Scheduled tasks run remotely, so they run on their cadence even when your computer is asleep or the Claude Desktop app is closed."* | `[PRIMARY]` |
| Scheduled tasks **cannot be tied to a local folder** — verbatim: *"they work with your connectors and the files saved to your Claude account. They can't be tied to a folder on your computer."* | `[PRIMARY]` |
| Scheduled tasks have "the same capabilities as regular Cowork tasks, including connected tools, skills, and installed plugins" | `[PRIMARY]` |
| Scheduled-task frequencies: **hourly, daily, weekly, weekdays, manual**. No minute-level precision. | `[PRIMARY]` |
| Scheduled tasks available on **Pro, Max, Team, Enterprise** | `[PRIMARY]` |
| **Custom connectors via remote MCP** available on Free, Pro, Max, Team, Enterprise. Added at **Customize → Connectors** with the MCP server URL. Free capped at 1. | `[PRIMARY]` |

> ⚠️ **Do not confuse Cowork scheduled tasks with Claude Code Desktop scheduled
> tasks.** They are different products with opposite properties. See
> `review-of-prior-findings.md` § Correction 1.

## Composio

| Fact | Tag |
|---|---|
| API v3 live; **v1/v2 retired** (`"This endpoint is no longer available. Please upgrade to v3 APIs."`) | `[PRIMARY]` |
| Toolkits with **Composio-managed OAuth**: `instagram`, `facebook`, `canva`, `googledrive`, `notion` | `[PRIMARY]` |
| `shopify` — **no** managed auth; needs own credentials | `[PRIMARY]` |
| **Instagram managed-OAuth requested scopes:** `instagram_business_basic`, `instagram_business_content_publish`, `instagram_business_manage_messages`, `instagram_business_manage_comments`, `instagram_business_manage_insights` | `[PRIMARY]` |
| **Facebook managed-OAuth requested scopes:** `public_profile`, `email`, `pages_show_list`, `pages_read_engagement`, `pages_manage_posts`, `pages_manage_engagement`, `pages_read_user_content`, `pages_manage_metadata`, `pages_messaging`, `read_insights`, `business_management` | `[PRIMARY]` |
| Free tier: **100,000 tool calls/month**, hard-capped, no card. Then ~$0.0003/call | `[SECONDARY]` |

> **Significance:** the managed Meta OAuth configs **request the publish scopes**
> (`instagram_business_content_publish`, `pages_manage_posts`). This is strong
> evidence Composio holds an App-Reviewed Meta app — a managed app requesting a
> scope it was never granted would be non-functional as a product. It is **not
> absolute proof of a live publish**; see `OQ-001`.

## Meta publishing

| Fact | Tag |
|---|---|
| Instagram publishing: two-step — `POST /{ig-user-id}/media` → container, then `POST /{ig-user-id}/media_publish`. **No scheduling parameter exists.** | `[SECONDARY]` |
| Facebook Pages: `POST /{page-id}/feed` with `published=false` + `scheduled_publish_time`. **Native scheduling, free, Meta holds the post.** Window reported 10 min – 75 days. | `[SECONDARY]` |
| ~~IG publish cap 25–50~~ **SUPERSEDED 2026-09-20:** Zernio's docs state **100 posts per rolling 24h**, all content types combined. Read the live quota via `GET /instagram/get-instagram-publishing-limit` and compare to `quotaTotal` — never hardcode. | `[PRIMARY]` |
| Composio exposes `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` — read real remaining quota at runtime rather than guessing | `[PRIMARY]` |
| **`image_url` must be a public HTTPS URL returning the file directly.** Direct file upload is not supported. | `[SECONDARY]` |
| **Google Drive share links do not work** as `image_url` — they involve login, redirects and an HTML wrapper. All three are documented failure causes. | `[SECONDARY]` |
| IG feed/carousel images: JPEG or PNG, **max 8 MB**, aspect **4:5 to 1.91:1**, width 320–1440 px | `[SECONDARY]` |
| IG Reels: MP4/MOV, max 1 GB, **9:16**, min ~540×960 | `[SECONDARY]` |
| IG Business or Creator accounts only — personal accounts rejected | `[PRIMARY]` |
| **Instagram Login needs NO Facebook Page.** `loginMethod=instagram_login` (the default) authorizes the Instagram professional account directly. Facebook Login is only required for ads scopes, catalog audio and paid-partnership labels. | `[PRIMARY]` (Zernio docs) |
| **Zernio hosts media:** `POST /v1/media/presign` returns `uploadUrl` + **`publicUrl`**, up to **5 GB**. This satisfies Instagram's public-HTTPS-URL requirement and removes the need for a separate image host. | `[PRIMARY]` |

> ⚠️ **The public-URL requirement is architecturally load-bearing.** The image
> layer must host, or you need a bucket/CDN. This is the strongest single
> argument for Bannerbear — see `image-layer.md`.

## Image layer

| Fact | Tag |
|---|---|
| **Canva Connect autofill is Enterprise-only** — verbatim: *"your integration must act on behalf of a user who is a member of a Canva Enterprise organization"*, plus MFA required. **Pro and Teams cannot use brand-template autofill via API.** | `[PRIMARY]` |
| Composio's `canva` toolkit exposes autofill tools, but **Canva will reject the call** on non-Enterprise plans. Tool existence ≠ permission. | `[PRIMARY]` + inference |
| **Bannerbear** — free trial 30 credits; **Automate $49/mo** (1,000 API credits, REST API, **MCP**, 50+ integrations); Scale $149 (10,000 credits, Instant URLs, custom S3); Enterprise $299 | `[PRIMARY]` |
| Bannerbear API returns a **hosted public image URL** (`https://images.bannerbear.com/...`); appears standard across the API, not tier-gated | `[PRIMARY]` |
| Bannerbear ships an **MCP server** — verbatim: *"Bannerbear provides an MCP server, so AI agents and assistants—such as Claude, Cursor and other MCP-compatible clients—can use Bannerbear directly without writing against the REST API."* Hosted OAuth endpoint or `@bannerbear/mcp` locally. | `[PRIMARY]` |
| Bannerbear "Instant URLs" (render-on-demand from query string) are **Scale tier and up** — a *different* feature from standard hosted output | `[PRIMARY]` |
| **Placid** — tiers Basic/Pro/Business/VIP at 500/2,500/25,000/100,000 credits. REST API + URL API on **all** tiers. Free trial, no permanent free tier. **Dollar prices not exposed on the page.** | `[PRIMARY]` |
| Most established in this category: **Bannerbear**, then Placid and APITemplate.io | `[SECONDARY]` |

## Publishing vendors

| Fact | Tag |
|---|---|
| **Ayrshare MCP server is live at `https://api.ayrshare.com/mcp`** | `[SECONDARY]` |
| Ayrshare pricing by **social profile**: Premium **$149/mo** (1 profile), Launch **$299/mo** (10), Business **$599/mo** (30), Enterprise custom (300+) | `[SECONDARY]` |
| Ayrshare supports IG posts, **Stories, Reels, carousels**, and FB Pages | `[SECONDARY]` |
| Ayrshare **does not host media** — you still supply a public URL | `[SECONDARY]` |
| Customers do **not** complete Meta App Review to use Ayrshare | `[SECONDARY]` |
| **Zernio** (formerly Late / getlate.dev): founded **2025**, Girona Spain, **team of 8**, **bootstrapped**, ~$1M ARR by Jul 2026, Trustpilot ~4.8. Free at 1–2 connected accounts. | `[SECONDARY]` |
| Zernio rebrand: "same API, same team, same infrastructure", "zero breaking changes"; old domain redirects | `[SECONDARY]` |
| **bundle.social**: founded 2024. Free 3 accounts/20 posts per mo; Pro $100/mo unlimited accounts + 10k posts; Business $400/mo. Priced **per organization**. | `[SECONDARY]` |

## Nanny-sector social (strategy inputs)

| Fact | Tag |
|---|---|
| Best-converting formats: **Reels** for reach/discovery, **carousels** for saves and qualification, **Stories** for nurture, **static** weakest for discovery | `[SECONDARY]` |
| Cadence that works: FB **3–5/week**; IG **3–4/week + near-daily Stories**; practically 2–3 Reels + 1–2 carousels weekly | `[SECONDARY]` |
| Highest-converting CTAs are **DM keyword** ("DM 'NANNY'"), comment-keyword lead magnets, and book-a-consult. **DMs and calls are the conversion event for local services — not link clicks.** | `[SECONDARY]` |
| Local signals that matter: city/neighbourhood in bio + captions + on-screen text, location tags on every post, **small local hashtags** not large generic ones, correct category ("Child Care Service"), FB reviews | `[SECONDARY]` |
| Top childcare accounts avoid children's faces by default: backs of heads, hands, toys, wide/cropped shots, staff-only, graphics and quote cards, blurred testimonials | `[SECONDARY]` |
| COPPA: FTC treats photos/video/audio containing a child's image or voice as **personal information**. Commercial use needs a written guardian release naming platforms, duration, and **paid advertising** explicitly. | `[SECONDARY]` |
| Meta applies child-safety enforcement to **AI-generated material identically to real material**; enforcement tightened in 2026. A false positive can kill the ad account without warning. | `[SECONDARY]` |

## Build-phase verifications (2026-09-20)

| Fact | Tag |
|---|---|
| Plugin layout: `.claude-plugin/plugin.json` (only `name` required), `.mcp.json` with `{"type":"http","url":…}` for remote servers, `skills/<name>/SKILL.md`, `agents/*.md`, `hooks/hooks.json`; marketplace `.claude-plugin/marketplace.json` with `plugins[].source` as a relative path | `[PRIMARY]` |
| Anthropic's own plugins declare `canva` → `https://mcp.canva.com/mcp` and `google-drive` → `https://drivemcp.googleapis.com/mcp/v1`; Zernio's plugin declares `https://mcp.zernio.com/mcp` — all `type: http` | `[PRIMARY]` |
| SKILL.md frontmatter: `name` 1–64 chars lowercase/digits/hyphens; `description` ≤ 1024 chars; optional `license`, `compatibility`, `metadata`, `allowed-tools` | `[SECONDARY]` |
| **"Hooks and sub-agents run only in Cowork, so they appear grayed out in chat."** Hook types by surface not enumerated. | `[PRIMARY]` |
| PreToolUse matcher `mcp__<server>__<tool>`; block via exit 2 or `hookSpecificOutput.permissionDecision: "deny"`; `prompt`/`agent` hooks return the same JSON | `[PRIMARY]` |
| Google Drive connector: `update_file` edits **title and parent only**; `read_file_content` supports Docs/Sheets/Slides/PDF/Office/images; `download_file_content` exports Docs as text; `create_file` converts text to a Google Doc unless disabled; folders via `mimeType application/vnd.google-apps.folder`; `trash_file` exists; **no Google Docs connector in the directory** | `[PRIMARY]` |
| Cowork cloud sandbox: *"All traffic leaving the sandbox passes through a mandatory proxy… only allow-listed destinations are reachable."* | `[PRIMARY]` |
| Cowork scheduled tasks are created by the user (name, prompt, frequency); a plugin cannot create them | `[SECONDARY]` |
| **Canva MCP plan gating (corrects earlier table):** Pro+ = `resize-design`, `search-brand-templates`, `list-brand-kits`, `create-design-from-brand-template`; Enterprise-only = `autofill-design`, `get-brand-template-dataset`; everything else all plans | `[PRIMARY]` |
| Canva Pro users **can** create Brand Templates in the Canva UI | `[SECONDARY]` |
| Canva edit loop: `start-editing-transaction` → `perform-editing-operations` (`replace_text {type, element_id, text}`; `find_and_replace_text` on responsive pages) → `commit-editing-transaction`; element ids from `get-design-content` | `[PRIMARY]` |
| Canva `generate-design` → `job.result.generated_designs[{candidate_id,url,thumbnails}]`; `create-design-from-candidate` takes the job id + candidate | `[PRIMARY]` |
| Canva `export-design(design, format, …)` → `job.urls[]`; **"Signed export URLs expire. Use them immediately."** Pro = lossless PNG / transparent bg. Rate limit 20/min on generate/create/resize/export | `[PRIMARY]` |
| Canva handoff rule: always surface `https://www.canva.com/design/{id}/edit`; "don't end the workflow at export" | `[PRIMARY]` |
| Zernio: to promote a draft send **`isDraft:false` with `scheduledFor`**; `scheduledFor` alone returns 200 and leaves it a draft | `[PRIMARY]` |
| Zernio `mediaItems[].url` must be public HTTPS returning the file; **Google Drive, Dropbox, OneDrive, iCloud links fail**; uploads live 7 days in temp storage then are copied permanent on publish; Zernio compresses above platform limits | `[PRIMARY]` |
| Zernio MCP media path = browser upload (`media_generate_upload_link`, 30-min link → `media_check_upload_status`), because "an AI client cannot read files on your computer" | `[PRIMARY]` |
| Zernio `hashtags` and `mentions` fields are reference-only — hashtags must be in `content` (or `firstComment`) | `[PRIMARY]` |
| Zernio `metadata` is free-form and echoed on every read and webhook — our packet ID lives there | `[PRIMARY]` |
| Zernio idempotency: `x-request-id` UUID per logical post (retry returns original); identical content to same account within 24 h → **409** | `[PRIMARY]` |
| Zernio Instagram `platformSpecificData`: `contentType:"story"`, `shareToFeed`, `firstComment`, `locationId`, `collaborators`, `userTags`, `instagramThumbnail`, `commentsEnabled`, `isAiGenerated`, `isPaidPartnership`, `muteAudio` | `[PRIMARY]` |
| Zernio Facebook: image **4 MB**, Reel **60 s**, Story 120 s, Page required, "tokens expire frequently" | `[PRIMARY]` |
| Zernio `GET /v1/accounts/{id}/instagram/publishing-limit` → `quotaUsage`/`quotaTotal`; "Meta's prose documentation and the live API disagree… the live value is authoritative" | `[PRIMARY]` |
| Zernio `GET /v1/accounts/health` → `summary.needsReconnect`, per-account `canPost`, `status` | `[PRIMARY]` |
| Zernio analytics: `GET /v1/analytics` (sortBy engagement, 90-day default, 366 max), `GET /v1/analytics/best-time` → `slots[{day_of_week 0=Mon, hour UTC, avg_engagement}]`; included on usage-based plans | `[PRIMARY]` |
| Zernio comment-automation body: `profileId`, `accountId`, `name`, `keywords[]`, `matchMode exact|contains|word`, `typoTolerance`, `excludeKeywords`, `dmMessage`, `buttons[]`, `commentReply`, `alsoMatchInDms`, `trigger comment|story_reply`, `postId` (binds to unpublished post) | `[PRIMARY]` |
| Zernio webhook events include `post.published`, `post.failed`, `post.partial`, `account.disconnected`, `comment.received`; they carry `post.metadata` | `[PRIMARY]` |
| 2026 caption rules for local service: hook + keyword in first 125 chars; ≤ 5 relevant local hashtags; one CTA last; algorithm rewards watch time, saves, shares, DMs | `[SECONDARY]` |
| Voice card backbone: Nielsen Norman's four tone dimensions (formality, humor, respect, enthusiasm) + Mailchimp/Atlassian execution rules; extract from 10–20 posts; never-dos are the strongest signal | `[SECONDARY]` |
| FTC: testimonials must disclose material connections clearly; paraphrase may not change meaning; "licensed/certified" must be literally true; no absolute safety claims; COPPA treats a child's image/voice as personal information | `[SECONDARY]` |

## Live Zernio verification — 2026-09-21, operator's real account `[PRIMARY]`

Run with `social-os/tools/verify-zernio.sh` plus follow-up probes. Nothing published.

| Fact | Result |
|---|---|
| API key auth (`Bearer sk_…`) | ✅ works |
| Profile | one, `Default`, holds both accounts |
| Accounts | Facebook Page + Instagram, both `isActive: true`, same profile |
| **`accounts/health`** | `healthy 2, warning 0, error 0, needsReconnect 0`; **both `canPost: true`, `canFetchAnalytics: true`** |
| **Creator switch works** | an Instagram switched to **Creator** reports `canPost: true` — confirms OQ-016's fix |
| **Instagram live quota** | **`quotaTotal: 100`**, `quotaUsage: 0`, `quotaDurationSeconds: 86400`. Settles 25 vs 50 vs 100. |
| `POST /v1/media/presign` | returns `uploadUrl` (Cloudflare R2), `publicUrl` (`media.zernio.com/temp/…`), `expiresIn: 3600` |
| `PUT` bytes to `uploadUrl` | HTTP **200** |
| **Presigned URL 404s until the PUT happens** | validating before upload always fails — **validate after upload** |
| `validate_media` after upload | `valid: true` + `contentType`, `size`, per-platform `withinLimit` |
| **Zernio fetches external URLs server-side** | a `raw.githubusercontent.com` URL → `valid: true`. **A live Canva export URL can be passed directly as `mediaItems[].url`.** Closes OQ-013. |
| Redirecting URLs | `picsum.photos/1080` → `"URL returned HTTP 404"` — matches the Drive/Dropbox warning |
| **`validate_post` dry run** | a real cross-posted IG+FB body (media, `firstComment`, `scheduledFor`, `timezone`) → **`{"valid": true, "message": "No validation issues found."}`**. Free pre-flight; nothing published. |
| MCP `tools/list` authenticated | **52 tools**, incl. `validate_post`, `validate_media`, `validate_post_length`, queue, analytics, comments, mentions, `search_tools`, `call_tool` |
| Comment automations | **not** in the core 52 — reach via `search_tools` → `call_tool` |
| `validate_post_length` | takes **`text`**, not `content` |
| Facebook image limit | `validate_media` says 10 MB; the Facebook platform page says 4 MB "rejected in practice" — **trust 4 MB** |

> **Sandbox note, not a product fact:** this Claude environment's egress is
> allow-listed — `upload.wikimedia.org` and `export-download.canva.com` were blocked
> (HTTP 400/403), while `zernio.com`, Cloudflare R2 and `raw.githubusercontent.com`
> were reachable. Cowork's architecture doc describes the same allow-list model, so
> **do not design on Claude downloading a Canva file and re-uploading it.** Zernio's
> own server-side fetch is the supported path.
