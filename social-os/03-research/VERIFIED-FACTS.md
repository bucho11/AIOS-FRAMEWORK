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
| IG publish cap: Meta's current docs reportedly say **50 per rolling 24h** (carousels = 1); older docs and field reports say 25. **Design for 25.** | `[SECONDARY]` |
| Composio exposes `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` — read real remaining quota at runtime rather than guessing | `[PRIMARY]` |
| **`image_url` must be a public HTTPS URL returning the file directly.** Direct file upload is not supported. | `[SECONDARY]` |
| **Google Drive share links do not work** as `image_url` — they involve login, redirects and an HTML wrapper. All three are documented failure causes. | `[SECONDARY]` |
| IG feed/carousel images: JPEG or PNG, **max 8 MB**, aspect **4:5 to 1.91:1**, width 320–1440 px | `[SECONDARY]` |
| IG Reels: MP4/MOV, max 1 GB, **9:16**, min ~540×960 | `[SECONDARY]` |
| IG Business or Creator accounts only — personal accounts rejected | `[PRIMARY]` (Composio toolkit docs) |

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
