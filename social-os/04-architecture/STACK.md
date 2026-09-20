# STACK — the architecture as of 2026-09-20

> Supersedes the 2026-09-19 version (Ayrshare + Bannerbear), which was written
> before the affordability constraint. See DEC-010, DEC-011, DEC-013.
>
> **Total added cost: $0.** Every component verified on the vendor's own docs.

---

## The system

```
                    CLAUDE COWORK  (Pro, $20/mo — hers, already required)
                    brain · chat · the approval surface
                                  │
        ┌─────────────────┬───────┴────────┬─────────────────┐
        │                 │                │                 │
  GOOGLE DRIVE        ZERNIO          small-business     SCHEDULED
   connector        custom MCP           plugin            TASKS
   (native)                              (Anthropic)      (built in)
        │                 │                │                 │
   THE BRAIN        publish · schedule   43 generic       cloud-run,
   brand · content  media hosting        skills, free     machine off,
   calendar         inbox · DMs                           hourly floor
   what works       comment→DM
   ← OUR PRODUCT    analytics
                    $0 at 2 accounts
                         │
                  Instagram + Facebook
                      (client's)

  OPTIONAL, both $0:  Cloudinary (generate graphics) · Canva (manual design)
```

**Everything is a connector or a skill. There is no service to deploy, host,
monitor or patch.** That is forced, not chosen: Cowork has no generic
"make an HTTP request" primitive, so every external call goes through an MCP
tool or connector.

---

## Components

| Layer | Choice | Cost | Status |
|---|---|---|---|
| **Interface** | Claude Cowork **Pro** | $20/mo (hers) | ✅ verified |
| **Brain / filesystem** | **Google Drive** native connector | $0 | ✅ verified |
| **Generic skills** | Anthropic **`small-business`** plugin (43 skills) | $0 | ✅ verified |
| **Publishing + scheduling** | **Zernio** custom MCP | **$0** (2 accounts) | ⏳ `OQ-009` |
| **Media hosting** | **Zernio** `POST /v1/media/presign` → `publicUrl`, 5 GB | $0 | ✅ verified |
| **Approval gate** | **Zernio** `posts_create` with `is_draft: true` | $0 | ✅ verified |
| **Lead capture** | **Zernio** comment-to-DM automations | $0 | ✅ verified |
| **Analytics** | **Zernio** (26 endpoints) | $0 | ✅ verified |
| **Clock** | Cowork **scheduled tasks** (cloud, machine off, hourly floor) | $0 | ✅ verified |
| **Copywriting** | Claude | included | ✅ |
| **Graphics** *(optional, phase 2)* | **Cloudinary** free tier | $0 | ✅ verified |
| **Manual design** *(optional)* | **Canva** native connector | $0 | ✅ verified |
| **Distribution** | **Our plugin** synced from a GitHub marketplace | $0 | ✅ verified |

### Rejected, and why
- **Ayrshare** — no free tier; floor is **$149/mo** for one profile. Documented upgrade path past ~10 clients.
- **Bannerbear** — $49/mo, trial only. Cloudinary does it free.
- **Composio** — free and has verified Meta publish scopes, but **no Instagram scheduling tool**, so we would own the clock. Kept as the fallback publisher.
- **Metricool** — API gated to paid plans; MCP publish capability unverified.
- **Canva Connect autofill** — **Enterprise-only**, confirmed by Canva *and* by Anthropic's own reference table. Every client is on Pro.
- **Local folder as the filesystem** — Cowork scheduled tasks "can't be tied to a folder on your computer."

---

## Zernio — what it actually gives us

| Capability | Detail |
|---|---|
| MCP | `https://mcp.zernio.com/mcp` · OAuth 2.1 + PKCE + dynamic client registration · 20 core tools + 300+ generated · `search_tools`/`call_tool` for the long tail |
| Publishing | Feed · Carousel (10) · **Reels** (90s) · Stories, IG + FB + 14 more platforms |
| Scheduling | `scheduledFor` or `schedule_minutes`; states `scheduled → publishing → published` |
| **Approval** | `is_draft: true` — native, nothing to build |
| **Media hosting** | presign → `uploadUrl` + **`publicUrl`**, up to **5 GB** |
| **Lead capture** | comment-to-DM + story-reply automations, keyword triggers, audience filters, click tracking, delivered/read/click stats |
| Inbox | DMs + comments, unified |
| Analytics | 26 endpoints — feeds the learning loop |
| Reliability | `validate_post` · `validate_media` dry-runs · `posts_retry` · webhooks · idempotency keys |
| Multi-tenant | **Profiles free and unlimited**; only accounts meter |
| IG limits | **100 posts / rolling 24h**; 8 MB images (auto-compressed); 300 MB video |
| IG auth | **Instagram Login needs no Facebook Page** |

---

## Cost at scale

Zernio is graduated: 1–2 accounts free · 3–10 $6 · 11–100 $3 · 101+ $1.

| | Accounts | Zernio/mo | Per client |
|---|---|---|---|
| **Client #1** (1 IG + 1 FB) | 2 | **$0** | $0 |
| 5 franchises | 10 | $48 | ~$10 |
| **20 franchises** | 40 | **$138** | **~$7** |

Ayrshare for comparison: **$599/mo** at 30 profiles.

Metered extras to watch: outbound messages free to 10,000/mo then $1 per 10,000
(**meter starts 2026-10-01**); managed ads free to 500.

---

## What we build

Four skills. Everything else is bought or free.

| Skill | Job |
|---|---|
| **`brand-onboarding`** | The centrepiece. Researches her site + IG before saying hello, interviews her, fills the brain, ends with 3 real posts. |
| **`publish`** | The **only** skill that knows Zernio exists — the swap seam. Calls `is_draft` on draft, flips to scheduled on approval, checks quota, moves the file. |
| **`learn`** | Weekly: pulls Zernio analytics, rewrites `What works.md`. The compounding loop. |
| **`guardrails`** | Child imagery, W-2 classification, banned safety claims. **The moat.** |

Plus: the **Drive folder template** (the brain) and **two Cowork scheduled tasks**
(weekly plan, weekly report).

---

## The content loop

```
 PLAN (weekly task) → DRAFT (copy + media) → media presign → publicUrl
   → posts_create is_draft:true → 2 Drafts/
   → ► SHE APPROVES IN COWORK ◄
   → flip to scheduled → 3 Approved/ → Zernio publishes → 4 Published/
   → LEARN (weekly task) pulls analytics → What works.md ──┐
                                                            └→ feeds PLAN
```

---

## The swap seam

Only `publish` knows the vendor. Everything upstream emits a neutral post object
(caption, media URLs, platforms, publish time, first comment) and calls five
operations: `schedule` · `cancel` · `status` · `quota` · `publish_now`.
Our own `post_id` is the primary key; Zernio's id is a foreign key on our record.
**Changing publishers edits one file.**

---

## Where it all lives (DEC-013)

| What | Home |
|---|---|
| Template, research, decisions | **This repo** — the factory |
| Skills + connector config | **A plugin repo** on GitHub — the shipping box |
| The brain | **Client's** Google Drive — the product |
| Social accounts | Client's **Zernio profile** |

**Nothing lives in HIDEit's Workspace or Drive.** Operator access to client folders
comes from a **personal** Google account outside any employer domain.
