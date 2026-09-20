# Cost-floor analysis — the cheapest stack that actually works

> Requirement changed 2026-09-20: **most affordable, one client, free if possible.**
> That flips the "proven beats cheap" tiebreaker used in DEC-005/006. This file
> records the re-research. All prices verified from the vendor's own pricing page
> unless tagged otherwise.

---

## Already free — no decision needed

| Component | Answer | Cost | Tag |
|---|---|---|---|
| Interface | Claude Cowork **Pro** | $20/mo — she pays anyway | `[PRIMARY]` |
| Filesystem / brain | **Google Drive** native connector | $0 | `[PRIMARY]` |
| Generic skills | Anthropic **`small-business`** plugin, 43 skills | $0 | `[PRIMARY]` |
| Copywriting | Claude itself | included | — |
| Scheduler / clock | Cowork **scheduled tasks** (cloud, machine off) | $0 | `[PRIMARY]` |
| Design tool (manual) | **Canva** native connector | $0 to connect | `[PRIMARY]` |

That leaves exactly **three gaps**: publishing, image hosting, image generation.

---

## Publishing — the vendor comparison at one client

| Vendor | Cheapest real cost for 1 IG + 1 FB | MCP | Verdict |
|---|---|---|---|
| **Zernio** | **$0** — first 2 accounts free | ✅ `mcp.zernio.com/mcp` | **WINNER** |
| Ayrshare | **$149/mo** — Premium, 1 profile. **No free tier**, 28-day trial only | ✅ verified live | Too expensive at 1 client |
| Metricool | API is **Advanced/Custom plans only** (paid). MCP on any plan but publish capability **unverified** | ⚠️ live, needs auth | More costly, less verified |
| Composio | $0 (100k calls) — but **no Instagram scheduling tool**; we'd own the clock | ✅ | Fallback only |
| bundle.social | Free tier caps at **20 posts/mo** — below a real cadence | — | Too limited |
| Buffer | ~$6/channel = ~$12/mo | — | Not free, worse than Zernio |
| Postiz self-host | "Free" but needs **your own Meta app** → App Review | — | Dead on arrival |

### Zernio, verified

From **zernio.com/pricing** `[PRIMARY]`:
- **First 2 connected social accounts free. No credit card.**
- Free includes: unlimited posts, threads, first comment, queue, calendar,
  analytics, inbox (comments + DMs), **full API access**, **webhooks**
- **"No feature tiers exist"** — everything available on free and paid alike
- Paid only starts at account 3 ($6/mo each, 3–10)

From **docs.zernio.com** `[PRIMARY]`:
- 16+ platforms incl. Instagram, Facebook, TikTok, LinkedIn, YouTube, GBP
- Auth: `Authorization: Bearer sk_…`, env var `ZERNIO_API_KEY`
- `POST /v1/profiles` · `GET /v1/connect/{platform}` · `GET /v1/accounts` ·
  `POST /v1/posts` · `GET /v1/posts/{postId}`
- Posts take `scheduledFor` + timezone, or `publishNow: true`, or neither for a draft
- States: `scheduled` → `publishing` → `published`
- MCP endpoint probed: **HTTP 401** = live, auth required

`[SECONDARY]` — **Zernio accepts direct media upload and returns a public URL**
(plus a presigned-upload flow). Instagram: feed, carousel (≤10 mixed), Reels,
Stories. **If this holds, Zernio solves image HOSTING too** and one whole
component disappears. Closes with `OQ-009`.

**1 Instagram + 1 Facebook = exactly 2 accounts = $0/month.**

---

## Image generation — Claude cannot do it

`[PRIMARY]` Anthropic: Claude does **not** generate photos or illustrations.
"Custom visuals" in chat and Cowork are **diagrams and charts**, rendered inline
and **ephemeral**. So the image layer is genuinely external.

| Option | Cost | Verdict |
|---|---|---|
| **Cloudinary** | **Free forever**, 25 credits/mo (1 credit = 1,000 transformations *or* 1 GB storage *or* 1 GB bandwidth). No card. Text overlay via URL params. Public HTTPS CDN URL. | **WINNER for automation** |
| Canva (free/Pro) | $0 | Manual design. Keep — she likely has it. |
| APITemplate.io | Free 50 images/mo, 3 templates, REST API. **CDN storage listed for paid only** | Viable, but hosting unclear on free |
| Cloudflare Images | Free 5,000 transformations/mo; overlay needs Workers | Less turnkey for text |
| Bannerbear | **$49/mo**; 30-credit trial only | Cut for cost |
| Python Pillow in the Cowork sandbox | $0 | Possible — Cowork does execute code `[PRIMARY]` — but we'd own rendering and hosting. Not v1. |

**Important framing:** her highest-converting content is **Reels she films** and
**real photos of staff/homes/hands** — neither needs generation, only hosting.
Generation only matters for carousels and quote cards. So the image layer is an
**enhancement, not a gate.**

---

## The verified total

| | Monthly |
|---|---|
| Claude Cowork Pro (hers, already required) | $20 |
| **Everything we add** | **$0** |

Upgrade path when it's earned: Zernio paid accounts at $6 each (3–10), then
Ayrshare Launch at $299/10 profiles (~$30/client) when reliability is worth more
than cost — realistically past ~10 clients.
