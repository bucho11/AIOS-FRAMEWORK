# STACK — the architecture as of 2026-09-20

> Supersedes the 2026-09-19 version (Ayrshare + Bannerbear). See DEC-010, DEC-013,
> DEC-018 (**Canva Pro is in — DEC-016's "Canva is out" was too broad**).
>
> **Total added cost: $0.** Every component verified on the vendor's own docs.

---

## The system

```
                    CLAUDE COWORK  (Pro, $20/mo — hers, already required)
                    brain · chat · the approval surface
                                  │
        ┌──────────────┬───────┴───────┬──────────────┐
        │              │               │              │
  GOOGLE DRIVE     CANVA MCP       ZERNIO MCP     SCHEDULED
   connector        (native)        (custom)        TASKS
   (native)                                       (built in)
        │              │               │              │
   THE BRAIN      create · edit    host media     cloud-run,
   brand voice    RESIZE (Pro)     publish        machine off,
   colors/fonts   export PNG       schedule       hourly floor
   content        upload assets    inbox · DMs
   what works                      comment→DM
   ← OUR PRODUCT  Canva Pro        analytics
                  ~$15/mo (hers)   $0 at 2 accounts
                       │                │
                       └──── design ────┘
                          then publish
                                │
                       Instagram + Facebook
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
| **Graphics / design** | **Canva** native MCP connector — **Pro** | ~$15/mo (hers) | ✅ verified |
| **Multi-size output** | **Canva `resize-design`** — one design → IG feed / Story / FB | Pro feature | ✅ verified |
| **Distribution** | **Our plugin** synced from a GitHub marketplace | $0 | ✅ verified |

### Rejected, and why
- **Ayrshare** — no free tier; floor is **$149/mo** for one profile. Documented upgrade path past ~10 clients.
- **Bannerbear** — $49/mo, trial only. Canva Pro covers design.
- **Cloudinary** — dropped (DEC-016). Its URL text overlay suits watermarks and simple labels, not designed graphics. Canva does the job properly.
- **Composio** — free and has verified Meta publish scopes, but **no Instagram scheduling tool**, so we would own the clock. Kept as the fallback publisher.
- **Metricool** — API gated to paid plans; MCP publish capability unverified.
- **Canva Connect brand-template autofill** — Enterprise-only. **Only autofill is out, not Canva.** Claude creates and edits each design instead (DEC-018).
- **Canva Enterprise** — quote-based, **150+ seat minimum**; the reseller program still requires buying licences. No shortcut exists.
- **Local folder as the filesystem** — Cowork scheduled tasks "can't be tied to a folder on your computer."

---

## Canva Pro — what it actually gives us

| Capability | Free | **Pro** | Enterprise |
|---|---|---|---|
| Create · edit · search · export · upload assets · comments | ✅ | ✅ | ✅ |
| Export quality | standard | **lossless PNG, transparent bg, premium elements** | ✅ |
| **Resize design** | ❌ | ✅ | ✅ |
| Autofill templates · brand kits · brand templates | ❌ | ❌ | ✅ |

**`resize-design` is the sleeper feature** — one design becomes IG feed, IG Story
and FB automatically. That is the most repetitive task in social, and it is Pro.

**The brain replaces the Brand Kit.** Brand Kit is Enterprise, but we do not need
it: `Colors and fonts.md` and `Brand voice.md` in her Drive hold the exact hex
values, fonts and layout rules, and Claude applies them when creating each design.
*The context layer substitutes for the feature we cannot buy* — the product thesis
working as intended.

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

Five skills. Everything else is bought or free.

| Skill | Job |
|---|---|
| **`brand-onboarding`** | The centrepiece. Researches her site + IG before saying hello, interviews her, fills the brain, ends with 3 real posts. |
| **`make-graphic`** | Canva: create using brand colors/fonts from the brain → resize per platform → export → hand to Zernio for hosting. |
| **`publish`** | The **only** skill that knows Zernio exists — the swap seam. Calls `is_draft` on draft, flips to scheduled on approval, checks quota, moves the file. |
| **`learn`** | Weekly: pulls Zernio analytics, rewrites `What works.md`. The compounding loop. |
| **`guardrails`** | Child imagery, W-2 classification, banned safety claims. **The moat.** |

Plus: the **Drive folder template** (the brain) and **two Cowork scheduled tasks**
(weekly plan, weekly report).

---

## The content loop

```
 PLAN (weekly task)
   reads brain + What works.md → proposes the week
        │
 DRAFT  Claude writes copy in her voice
        │
 DESIGN ── CANVA ── create design using her colors/fonts from the brain
        │           → resize for IG feed / IG Story / FB
        │           → export lossless PNG
        │
 HOST  ── ZERNIO ─ presign → upload → permanent publicUrl
        │
 STAGE   posts_create is_draft:true → 2 Drafts/
        │
   ► SHE APPROVES IN COWORK ◄
        │
 SHIP    flip to scheduled → 3 Approved/ → Zernio publishes → 4 Published/
        │
 LEARN (weekly task) pulls Zernio analytics → What works.md ──┐
                                                               └→ feeds PLAN
```

**Reels and real photos skip the DESIGN step entirely** — straight from her phone
to Drive to Zernio hosting. Canva is for carousels, quote cards and tips graphics.

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
