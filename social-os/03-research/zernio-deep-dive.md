# Zernio — deep dive

> `[PRIMARY]` throughout unless tagged. Read from `docs.zernio.com` (900 doc
> pages, machine-readable index at `/llms.txt`), live endpoint probes, and the
> official plugin repo. 2026-09-20.
>
> **Verdict: materially stronger than assumed.** Not a publisher — a full social
> operations platform. Three findings below change the build.

---

## Scale of the thing

**900 documented API pages.** Categories by size: platforms (114) · whatsapp (75) ·
connect (57) · business-agent (55) · ad-campaigns (50) · ad-accounts (46) ·
analytics (26) · google-business (25) · messages (16) · accounts (16) ·
webhooks (15) · comments (15) · workflows (14) · posts (10) · lead-gen (7) ·
comment-automations (6) · queue (6) · profiles (5) · multi-tenant (3) · media (1).

Ships Node + Python SDKs, a CLI, webhooks, idempotency keys, and a detailed error
taxonomy that passes upstream platform errors through verbatim (Meta's
`error_subcode`, `error_user_msg`; Google's `quotaScope`). This is not a thin wrapper.

---

## 1. The MCP server

- Hosted: **`https://mcp.zernio.com/mcp`**, Streamable HTTP
- **20 hand-written core tools** + one generated tool per API endpoint (**300+**)
- `search_tools` / `call_tool` load the long tail on demand — **solves tool bloat**
- **OAuth 2.1 + PKCE + dynamic client registration (RFC 7591)** — a client can
  register itself with no pre-approval, so the server URL alone is enough
- OAuth scopes advertised: `posts:read` `posts:write` `accounts:read`
  `accounts:write` `analytics:read` `ads:write` `messaging:write` `automations:write`
- API-key auth also supported (`Authorization: Bearer sk_…`) for headless agents

### Core tools
`accounts_list` · `accounts_get` · `profiles_list/get/create/update/delete` ·
`posts_list/get/create/update/delete` · `posts_publish_now` · `posts_cross_post` ·
`posts_retry` · `posts_list_failed` · `posts_retry_all_failed` ·
`media_generate_upload_link` · `media_check_upload_status` · `docs_search`

### `posts_create` — the approval gate is built in
| `is_draft` | `publish_now` | Result |
|---|---|---|
| `true` | any | **Saved as a draft, not scheduled** |
| `false` | `true` | Published immediately |
| `false` | `false` | Scheduled `schedule_minutes` from now (default 60) |

Params: `content` · `platform` · `account_id` · **`profile_id`** ("one client in an
agency setup") · `is_draft` · `publish_now` · `schedule_minutes` · `media_urls` · `title`

> **`is_draft: true` IS the approve-then-publish gate.** We do not have to build
> one. Claude drafts → she approves in Cowork → we flip it to scheduled.

### Official Claude plugin
`github.com/zernio-dev/zernio-claude-plugin` — **MIT**, v2.0.0, bundles the MCP
server. Documented for Claude Code: `/plugin marketplace add zernio-dev/zernio-claude-plugin`
→ `/mcp` → browser sign-in. Verbatim: **"There's no API key to copy."**

⚠️ **Doc/behaviour mismatch found:** docs state `tools/list` "needs no credential";
the live server returns **401** with a `www-authenticate` header. Minor, but it is
the reason the tool list still can't be enumerated without an account.

---

## 2. Media — Zernio hosts. Cloudinary is no longer needed for hosting.

`POST /v1/media/presign`
- Request: `filename`, `contentType`, optional `size`
- Returns: **`uploadUrl`** (presigned, expires 3600s) + **`publicUrl`** (public,
  accessible after upload) + `key`
- **Up to 5 GB**

PUT the file to `uploadUrl`, then pass `publicUrl` into the post.

> **This closes the single hardest constraint in the whole project.** Instagram
> requires a public HTTPS URL and rejects Google Drive links. Zernio supplies one.
> **Cloudinary drops to optional, and is only needed to *generate* graphics.**

---

## 3. Instagram — the real numbers

| Property | Value |
|---|---|
| Caption | 2,200 chars (first 125 before the fold) |
| Carousel | up to 10 images |
| Image | JPEG/PNG, **8 MB, auto-compressed** |
| Video | MP4/MOV — 300 MB feed & Reels, 100 MB Stories |
| Reel length | **90 seconds** max |
| Post types | Feed · Carousel · Story · **Reel** |
| Scheduling | ✅ |
| DMs · Comments | ✅ ✅ |
| **Comment-to-DM automations** | ✅ |
| **Story-reply automations** | ✅ |
| Analytics | ✅ |
| **Publishing cap** | **100 posts / rolling 24h**, all types combined |

**Corrects two earlier entries in `VERIFIED-FACTS.md`:**
- The cap is **100**, not the 25–50 previously recorded. Read the live quota with
  `GET /instagram/get-instagram-publishing-limit` and compare to `quotaTotal`
  rather than hardcoding anything.
- **Instagram Login (`loginMethod=instagram_login`, the default) needs no Facebook
  Page at all** — the user authorizes their Instagram professional account
  directly. Facebook Login is only required for ads scopes, catalog audio and paid
  partnership labels. Business or Creator account is still mandatory.

---

## 4. 🔥 Comment-to-DM automation — the lead-gen machine

The sector research said the highest-converting CTA for local services is a DM
keyword ("DM **NANNY** for availability") because **DMs and calls are the
conversion event, not link clicks.** Zernio does this natively.

`POST /v1/comment-automations`
- **Triggers:** `comment` (keyword on any post/reel) or `story_reply` (keyword
  reply to an Instagram story)
- **Targeting:** per-post, or **account-wide** ("any post") — unlimited stacked
  account-wide automations, each with its own keyword set, all running independently
- **`alsoMatchInDms: true`** — one automation covers both the comment door and the
  DM door, deduplicated separately
- **Audience filters** (Instagram): followers / non-followers / above a follower
  count, with a `followGate` one-tap confirmation for unknown relationships
- **Link click tracking** on by default, optional `clickTag` for segmentation
- **Stats returned:** delivered, read, link clicks

> **This is a sellable product feature on its own.** Her posts stop being content
> and become an automated intake funnel, with attribution.

---

## 5. Multi-tenant — profiles are free

- **One profile per customer.** `POST /v1/profiles`
- **"Profiles are free; each connected account is metered."** Profiles are unlimited.
- A profile holds at most one account per platform
- Requests carry `profileId`; webhooks carry `accountId`

### Real pricing (graduated, billed per band)
| Connected accounts | Per account / month |
|---|---|
| **1–2** | **Free, no credit card** |
| 3–10 | $6 |
| 11–100 | $3 |
| 101–2,000 | $1 |
| 2,001+ | $1, no cap |

Accounts count across the whole team. Ad accounts count as accounts (a Page, its
Instagram and the Meta ad account = 3). Free allowance is a **$12/month credit**
against the connected-accounts line only.

**Every account, free or paid, includes: full API access, unlimited posts, all 16
platforms, analytics, inbox and ads.** No feature tiers.

### What this means commercially
| Scenario | Accounts | Cost/mo | Per client |
|---|---|---|---|
| **Client #1** (1 IG + 1 FB) | 2 | **$0** | $0 |
| 5 franchises | 10 | $48 | $9.60 |
| **20 franchises** (IG + FB each) | 40 | **$138** | **~$7** |

Compare Ayrshare: **$599/mo** for 30 profiles. Zernio does 20 franchises for $138.

Metered extras to watch: outbound messages free to **10,000/month** then
$1 per 10,000 (**meter starts 2026-10-01**); managed ads free to 500;
X/Twitter is pass-through per call — irrelevant here.

---

## 6. Capability we did not know we were getting

Beyond publishing: unified **inbox** (DMs + comments across platforms) ·
**analytics** (26 endpoints — feeds the learning loop) · **lead-gen forms**
(7 endpoints) · **workflows** (14) · **queue slots** (6 — recurring time slots) ·
**reviews** · **Google Business Profile** · **ads** across Meta/Google/TikTok ·
`validate_post` / `validate_media` dry-runs · **bulk upload** · webhooks.

Google Business Profile matters: research named the correct business category and
reviews as real local-SEO signals for a service business.

---

## What still can't be verified without an account

1. The MCP tool list (`tools/list` returns 401 despite the docs)
2. Whether **Cowork's** custom-connector OAuth completes against them — the plugin
   flow is documented for **Claude Code**, not Cowork. DCR support says it should.
3. A real end-to-end Instagram publish on the free tier

→ `OQ-009` still stands, but it is now a **confirmation**, not an investigation.
