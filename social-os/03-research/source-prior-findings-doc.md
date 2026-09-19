> **ARCHIVED SOURCE — not authoritative.** The prior research document supplied by
> the operator on 2026-09-19, preserved verbatim for provenance. It contains at
> least one foundational factual error and one recommendation that conflicts with
> the operator's stated constraints. **Read `review-of-prior-findings.md` before
> acting on anything here.**

# Nanny Business AI Ops — Social Content Agent: Research Findings

**Prepared:** 2026-09-19
**For:** a Claude Code agent to reason through, not to execute blindly.
**Posture:** findings + recommendation. All five stacks stay open. Nothing here is a decision you must obey — it is evidence you should test.

---

## 0. How to read this document

Every factual claim carries a provenance tag. **Do not treat tags as interchangeable.**

| Tag | Meaning |
|---|---|
| `[PRIMARY]` | Fetched directly from the vendor's own live docs or pricing page on 2026-09-19. Highest trust. |
| `[SECONDARY]` | From Perplexity Sonar research citing third-party sources. Directionally right, specifics may be stale. **Verify before spending money or writing code against it.** |
| `[UNVERIFIED]` | Named explicitly as an open question. Do not build on it. Section 10 tells you how to close it. |

**Operating rule for the agent working from this doc:** if a design decision depends on a `[SECONDARY]` or `[UNVERIFIED]` fact, run the verification in §10 *before* writing the code that depends on it. Do not infer. Do not fill gaps from training data — several facts in this space changed inside the last 60 days (see §4.1, the Late→Zernio rename).

### Stated constraints this document was written against

1. **One nanny business now.** Multi-tenant later, "we can always change backend connectors later."
2. **Cheapest and fastest route first.** This is a hard constraint and it changes the recommendation — see §6.
3. **Composio AI is already the chosen API connection layer.**
4. **Claude Cowork is the intended operator surface** — human sets it up, then it runs on repeat.
5. Target platforms: **Instagram and Facebook**, specifically.

Because of (1) + (2), the single most important architectural decision in this document is not *which vendor* — it is **where you put the swap seam** (§7). Get that right and the vendor choice becomes reversible in an afternoon.

---

## 1. The decisive constraint

Everything else follows from this.

### 1.1 Instagram has no scheduling. Facebook does.

**Instagram Content Publishing API** `[SECONDARY — Meta docs cited]`

Publishing is two calls:

```
POST /{ig-user-id}/media          → returns a container ID
GET  /{container-id}?fields=status_code   → poll until FINISHED
POST /{ig-user-id}/media_publish  → creation_id = <container ID>
```

There is **no `scheduled_publish_time` parameter** on either call. Instagram's own in-app scheduler exists (reportedly 25 posts/day, up to 75 days out) but is **not exposed through the API**.

**Consequence: something must be awake and running at the exact publish minute to fire `media_publish`.** That "something" is the central design question of this whole build.

Supported IG media types: single image, single video, Reels, carousels (up to 10 children), Stories.

**Daily publish cap — sources conflict.** Meta's current Instagram-with-Instagram-Login docs reportedly say **50 API-published posts per rolling 24h** (carousels count as 1). Older docs and multiple production reports say **25**. `[SECONDARY]`
→ **Design for 25.** Composio exposes `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` so you can read the real remaining quota at runtime rather than guessing — use it.

**Facebook Pages API** `[SECONDARY — Meta docs cited]`

```
POST /{page-id}/feed
  published=false
  scheduled_publish_time=<unix timestamp>
  message="..."
```

Meta holds it and publishes it for you. Window: **10 minutes minimum, 75 days maximum** from the API call. Older guides say 30 days; the current reference reportedly says 75.

**This asymmetry is exploitable and most people miss it.** Facebook scheduling is free, reliable, and requires zero infrastructure on your side. Only Instagram needs a clock.

### 1.2 Permissions and review gates

`[SECONDARY]`

| Path | Scopes needed |
|---|---|
| Instagram API with Instagram Login (`graph.instagram.com`) | `instagram_business_basic`, `instagram_business_content_publish` |
| Instagram Graph API via Facebook Login (`graph.facebook.com`) | `instagram_basic`, `instagram_content_publish`, `pages_show_list` |
| Facebook Pages | `pages_manage_posts`, `pages_read_engagement`, `pages_show_list` |

Content-publish scopes are **Advanced Access** permissions. They require **App Review**, and in most business cases **Business Verification** too. This is a multi-week gate with real rejection risk.

**This gate is the main reason to use a third-party publisher for v1** — the established vendors own their own reviewed Meta apps, so you inherit their access instead of applying for your own.

Recent breaking changes to be aware of `[SECONDARY]`:
- **2025-01-27** — unprefixed Instagram Login scopes (`business_content_publish` etc.) deprecated in favour of `instagram_business_*`.
- **2025-04-21 → 2025-05-20** — legacy Instagram v1.0 endpoints retired.
- **Instagram Basic Display API** is effectively dead; do not use it.

### 1.3 Cowork cannot be the clock

`[PRIMARY — code.claude.com/docs/en/desktop-scheduled-tasks, fetched 2026-09-19]`

Anthropic publishes this comparison directly:

| | Cloud routine | Desktop task | `/loop` |
|---|---|---|---|
| Runs on | Anthropic-managed cloud | Your machine | Your machine |
| **Requires machine on** | **No** | **Yes** | Yes |
| Requires open session | No | No | Yes |
| Persistent across restarts | Yes | Yes | Restored on `--resume` |
| Access to local files | No (fresh clone) | Yes | Yes |
| Permission prompts | **No (runs autonomously)** | Configurable | Inherits |
| **Minimum interval** | **1 hour** | 1 minute | 1 minute |

Cowork scheduled tasks `[SECONDARY — support.claude.com article 13854387, last updated 2026-09-17]` offer frequency options of **hourly, daily, weekly, weekdays, or manual**, with fields for task name, prompt, approval mode, frequency, model, and folder.

**Read this carefully, because it is the trap:**
- Cowork / Desktop tasks give you **1-minute precision** but **die when the laptop sleeps**. Unacceptable for a client's publish schedule.
- Cloud routines **survive anything** but have a **1-hour floor**. You cannot hit 3:07 PM.

**Therefore: Cowork is the brain and the approval surface. It is not the publisher.** Any design that has Cowork firing `media_publish` at the target minute is broken on a closed laptop. This is the most common mistake in this architecture — do not make it.

---

## 2. What Composio actually provides

`[PRIMARY — docs.composio.dev, fetched 2026-09-19]`

This is better than expected and materially changes option 2 in §5.

### Instagram toolkit — version `20260915_00`, 38 tools

- **Authentication: "Composio-managed OAuth available", OAuth2.**
- **Business and Creator accounts only.** Not personal accounts.
- Documented FAQ on the page: *"Why can Instagram reply-to-comment fail with the managed OAuth app?"* — confirms a managed OAuth app exists and has known edge-case limits.

Publishing-relevant tools:

```
INSTAGRAM_POST_IG_USER_MEDIA              # create media container
INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH      # publish the container
INSTAGRAM_CREATE_CAROUSEL_CONTAINER       # carousel parent
INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT   # remaining quota — USE THIS
INSTAGRAM_GET_IG_USER_STORIES
INSTAGRAM_GET_IG_MEDIA_INSIGHTS
INSTAGRAM_GET_USER_INSIGHTS
INSTAGRAM_POST_IG_MEDIA_COMMENTS          # first-comment pattern
INSTAGRAM_POST_IG_COMMENT_REPLIES
```

Several `*_DEPRECATED` tools exist (`INSTAGRAM_CREATE_POST`, `INSTAGRAM_CREATE_MEDIA_CONTAINER`, `INSTAGRAM_GET_POST_INSIGHTS`). **Do not wire to anything marked Deprecated** — they map to the retired v1.0 endpoints from §1.2.

### Facebook toolkit — version `20260902_00`, 44 tools

- **Authentication: "Composio-managed OAuth available", OAuth2.**
- **Facebook Pages only.** Not personal accounts.
- FAQ on page: *"How do I set up custom OAuth credentials for Meta (Facebook)?"* — custom credentials are an option, not a requirement.

Publishing and scheduling tools:

```
FACEBOOK_CREATE_POST
FACEBOOK_CREATE_PHOTO_POST
FACEBOOK_CREATE_VIDEO_POST
FACEBOOK_CREATE_MULTI_PHOTO_POST
FACEBOOK_GET_SCHEDULED_POSTS       # <- scheduling is a first-class concept
FACEBOOK_PUBLISH_SCHEDULED_POST
FACEBOOK_RESCHEDULE_POST
FACEBOOK_GET_PAGE_INSIGHTS
FACEBOOK_GET_POST_INSIGHTS
FACEBOOK_UPLOAD_PHOTO / FACEBOOK_UPLOAD_PHOTOS_BATCH
```

### The one thing that decides everything — currently unknown

`[UNVERIFIED]` **Does Composio's managed Meta OAuth app carry the `instagram_business_content_publish` / `pages_manage_posts` Advanced Access scopes, or does it only cover read scopes?**

- If **yes** → you can publish to IG and FB through Composio with zero Meta App Review. Option 2 in §5 becomes dramatically the cheapest and fastest path, and this whole project gets simpler.
- If **no** → you bring your own Meta app and inherit the multi-week review gate, and a third-party publisher (§4) becomes clearly correct for v1.

`[UNVERIFIED]` **Does `FACEBOOK_CREATE_POST` accept `scheduled_publish_time`/`published=false`?** The presence of `GET_SCHEDULED_POSTS`, `PUBLISH_SCHEDULED_POST` and `RESCHEDULE_POST` strongly implies scheduled creation is supported, but the tool's parameter schema is JS-rendered and could not be read. **Implication is not verification.**

**§10 tells you exactly how to close both. Close them before choosing a stack.**

---

## 3. Content creation options

### 3.1 Copy

Claude (Opus 5 / Sonnet 5), via the Anthropic API or inside Cowork.

**Design note, learned from auditing a production system that does this well:** put the brand voice rules in a **skill file the agent loads at runtime**, not in the prompt. A real-world marketing skill enforced things like banned-word lists, "one CTA on its own line", per-platform link placement (IG = link in bio; FB = URL in copy; TikTok = URL in first comment), and search-term-first phrasing. Rules in a versioned file can be audited, diffed and improved. Rules in a prompt cannot.

### 3.2 Images

`[PRIMARY — ai.google.dev model list, fetched 2026-09-19]`

Current Google model IDs:

```
gemini-3-pro-image          # "Nano Banana Pro" — flagship
gemini-3.1-flash-image      # faster / cheaper
gemini-3.1-flash-lite-image
gemini-2.5-flash-image
imagen-4.0-generate
```

Google's docs place Nano Banana as a headline capability with strong text-in-image rendering and character consistency across generations — the two things that matter for branded social.

Alternatives `[SECONDARY]`:
- OpenAI `gpt-image-2.5-sunburst` / `gpt-image-2.5-flare` — token-billed, roughly $0.013 (medium) to $0.053 (high) per 1024×1024 image. Note `gpt-image-1` is reportedly deprecated 2026-10-23.
- Black Forest Labs **FLUX.2 [flex]** — BFL's own docs flag it as *best for typography*; from ~$0.05/image. `FLUX.2 [klein] 4B` from ~$0.014/image for volume.

### 3.3 Video

`[PRIMARY — ai.google.dev/gemini-api/docs/video, fetched 2026-09-19]`

Google's documentation now says, verbatim, to **use Gemini Omni Flash as your default model for video generation** — citing superior video coherence, multi-input reasoning, **character consistency**, factual accuracy, and multi-turn conversational editing. It positions **Veo 3.1** as the specialist choice, for scene extension, last-frame control, or legacy pipeline integration.

```
gemini-omni-1.1-flash
veo-3.1-generate-preview
veo-3.1-lite-generate-preview
```

⚠️ **Time-sensitive** `[SECONDARY]`: multiple independent sources report **OpenAI's Sora 2 video API shuts down 2026-09-24** — five days from this document's date. Model IDs `sora-2` / `sora-2-pro`. This could not be confirmed on OpenAI's own docs. **Do not build on Sora without checking first.**

### 3.4 What you should *not* generate

See §9. For a childcare client this is not a style preference, it is an account-survival rule.

---

## 4. Publisher options — who owns the clock

### 4.1 ⚠️ Correction: "Late" / getlate.dev is now Zernio

`[PRIMARY — getlate.dev/pricing redirects to Zernio, fetched 2026-09-19]`

Research from secondary sources reported Late at "$19/mo for 10 profiles." **That is wrong as of today.** The domain now serves **Zernio**, with a completely different, usage-based model:

| Connected accounts | Price |
|---|---|
| **1–2** | **Free** |
| 3–10 | $6/mo each |
| 11–100 | $3/mo each |
| 101+ | $1/mo each |

Stated as included on **every** account, no plan gating:
- Scheduling + publishing, **unlimited posts**, threads, first comment, queue, calendar
- Analytics (impressions, reach, engagement, follower tracking)
- Messaging (read/send DMs), comments + reviews
- **Webhooks — real-time events for post status, messages, comments**
- Ads (boost posts, create campaigns), Blogs API (WordPress/Shopify)

**For one nanny business — one Instagram + one Facebook Page = 2 accounts = $0/month, with webhooks and unlimited posts.**

That is almost certainly your cheapest and fastest v1, and it directly matches your stated constraint. **But treat it with appropriate suspicion:** a rebrand this recent means the secondary research about this vendor is untrustworthy across the board, and three things are unconfirmed — whether the free tier includes API access, whether Instagram Reels/Stories/carousels are covered, and how mature the platform is post-rename. §10 has the tests.

### 4.2 The others

| Vendor | Pricing | Provenance | Notes |
|---|---|---|---|
| **Zernio** (ex-Late) | 1–2 accts **free**; 3–10 $6/acct | `[PRIMARY]` | Webhooks, unlimited posts. Cheapest by a mile at your scale. Rebrand risk. |
| **bundle.social** | Free: 3 accts, **20 posts/mo**. Pro **$100/mo**: unlimited accounts, 10k posts. Business $400/mo: 100k posts. Priced **per organization**, not per account. | `[PRIMARY]` | Free tier's 20 posts/month is too low for a real cadence (§8.1 implies 30–50/mo). Pro is the multi-tenant sweet spot later. |
| **Ayrshare** | Per **social profile**. Premium ~$149/mo (1 profile / 13 accounts); Business ~$599/mo (30 profiles) | `[SECONDARY]` — tier table is JS-rendered, could not read directly | `[PRIMARY]` from their site: 30M+ daily API calls, **99.99% uptime**, 14+ networks, multi-tenant architecture, MCP server, explicit "For AI Companies" positioning. Confirmed `scheduleDate` param returning `status: "scheduled"`, plus webhooks, bulk post, retry, analytics, comments. **The mature choice. Overkill and overpriced for one client.** |
| **Blotato** | ~$29/mo Starter (1,250 credits, 20 accounts) | `[SECONDARY]` | Markets itself explicitly at AI agents / Claude. Meta format coverage unconfirmed. |
| **Buffer API** | ~$6/channel/mo; 100 req/15min, 250/day | `[SECONDARY]` | Built around *your* Buffer account, not multi-tenant. Tight rate caps. Poor fit for agents. |
| **Postiz** | Cloud from ~$29/mo; also open-source self-hostable | `[SECONDARY]` | Self-hosting means you own Meta app review again. |
| **Metricool** | API only on Advanced tier (~$53/mo+) | `[SECONDARY]` | Analytics-first. Publishing via API unclear. Not an agent platform. |
| **Your own Meta app** | $0 vendor cost | — | You do App Review + Business Verification + build the scheduler. Weeks of gate, then free forever. |

---

## 5. The five stacks

All five share the same front half: **Cowork (or a Claude Code cloud routine) drafts → human approves → something publishes.** They differ only in *who owns the clock* and *who owns the Meta app*.

### Stack 1 — Cowork brain + Zernio clock
Cowork scheduled task drafts → approval queue → on approval, call Zernio with a schedule time → Zernio fires it. Zernio owns the Meta app; you inherit their access.
- **Cost: $0/mo** at 2 accounts. Model costs only.
- **Meta App Review: none.**
- **Precision: exact** (their scheduler, not yours).
- **Risk:** newly rebranded vendor; three unknowns in §10.

### Stack 2 — Cowork brain + Composio direct + cloud routine clock
Composio's Meta toolkits post directly. **Facebook uses Meta's own native scheduler** (free, 75-day window, zero infra). **Instagram** drafts sit in a queue and a **Claude Code cloud routine runs hourly** and publishes whatever is due.
- **Cost:** Composio + model costs. No publishing vendor.
- **Meta App Review: none *if* Composio's managed OAuth carries publish scope — otherwise weeks.** This is the `[UNVERIFIED]` from §2.
- **Precision:** exact on FB, **±1 hour on IG** (cloud routine floor). Schedule IG on the hour and this is a non-issue.
- **Risk:** you own reliability, retries, and failure alerting. No webhooks unless you build them.

### Stack 3 — Cowork brain + bundle.social
Same as Stack 1, different vendor. Per-organization pricing with unlimited connected accounts.
- **Cost:** free tier is 20 posts/mo (likely too low); **$100/mo** for real use.
- **Why it's here:** when you go multi-tenant, per-organization pricing beats per-profile badly. This is your likely *destination*, not your start.

### Stack 4 — Hybrid: FB native + IG via vendor
Facebook goes through Meta's free native scheduler. Only Instagram touches a paid publisher.
- **Cost:** roughly half a vendor bill.
- **Trade:** two code paths, two failure modes, two sets of logs.
- **Honest note:** given Zernio is free at 2 accounts, this optimisation saves nothing today. It becomes interesting at 50+ accounts.

### Stack 5 — Own Meta app + real scheduler (Cloud Scheduler / Temporal / Supabase cron)
You hold the tokens, run the queue, fire at the exact second.
- **Cost:** engineering time + App Review + Business Verification.
- **Worth it when:** many tenants, or you need surfaces vendors expose inconsistently (Stories especially).
- **Not your v1.** Explicitly ruled out by your "cheapest and fastest" constraint.

---

## 6. Recommendation, given your stated constraints

**Start with Stack 1 (Zernio) — but run the §10 verifications first, because if Composio's managed OAuth carries the publish scope, Stack 2 is better.**

Reasoning:

1. **"Cheapest" is unambiguous.** Zernio is $0/mo at two accounts, with webhooks and unlimited posts. Nothing else is free at a real posting cadence. bundle.social's free tier caps at 20 posts/month, which §8.1's cadence blows through in week two.
2. **"Fastest" means avoiding Meta App Review.** That gate is weeks with genuine rejection risk. Both Stack 1 and Stack 2-if-managed-OAuth-works skip it entirely. Stack 5 fails this test outright.
3. **"We can change backend connectors later" is only true if you build the seam.** See §7. This is the part people skip and then regret.
4. **Cowork stays as the brain**, per your intent — drafting, reasoning, brand voice, the approval surface. It just never holds the clock (§1.3).

**Prefer Stack 2 over Stack 1 if** verification V1 in §10 comes back positive. Reason: you are already committed to Composio as your connection layer, so Stack 2 removes an entire vendor from the dependency graph for the same $0. The only cost is ±1 hour IG precision and owning your own retry logic.

**Migration path as you grow:** Zernio ($0, 1 client) → Zernio at $6/account (2–10 clients) → bundle.social Pro $100/mo flat (10+ clients, unlimited accounts) → own Meta app (when vendor fees exceed an engineer-week per quarter, or you need Stories at scale).

---

## 7. The swap seam — the one thing to get right on day one

You said the backend connectors can change later. **That is only true if nothing above the publisher knows which publisher you use.**

Define one narrow interface. Everything upstream — Cowork, the drafting agent, the approval queue — talks only to this. Every vendor gets an adapter behind it.

```
Publisher interface (conceptual — 5 methods, no more)

  schedule(post, publish_at, platforms[]) -> external_id
  cancel(external_id)                     -> bool
  status(external_id)                     -> queued | scheduled | published | failed
  quota(platform)                         -> remaining posts in window
  publish_now(post, platforms[])          -> external_id      # Stories, urgent
```

Rules that keep it swappable:

- **Store your own `post_id` as the primary key.** The vendor's ID is a foreign key on your record, never your identity. Vendors churn; your history should not.
- **Never let vendor-shaped payloads leak upstream.** The drafting agent emits a neutral post object — caption, media URLs, platform list, publish time, first-comment text. The adapter translates.
- **Implement `quota()` even where the vendor hides it.** For direct Composio, that's `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT`. For vendors, it may be a stub returning `unknown`. Having the method means the IG 25/50-per-day ceiling never surprises you in production.
- **Keep Facebook's native scheduling reachable through the same interface.** FB scheduling is free and excellent; the adapter should be able to use it even when Instagram goes through a vendor. That is Stack 4 available as a config flag rather than a rewrite.
- **Log every call's request and response verbatim.** When you swap vendors you will need to prove behaviour parity, and when Meta changes something you will need to see what actually broke.

Build this before the second post is ever scheduled. It is perhaps 200 lines and it is the difference between "change connectors later" being true and being a sentence you said once.

---

## 8. Full nanny AI ops system map

Social is one node. Here is the operational reality it sits inside.

`[SECONDARY — synthesised from agency public pages, APNA guidance, and household payroll providers. Fee figures are real quoted numbers from named agencies, but they are that agency's price, not an industry standard.]`

### 8.0 The end-to-end workflow

```
  ┌─────────────┐
  │ 1. LEAD     │  family finds you (social, Google, referral)
  │    INTAKE   │  → intake form OR discovery call
  └──────┬──────┘     often gated by a non-refundable fee:
         │            $250–$1,000 registration / launch / engagement
         v
  ┌─────────────┐
  │ 2. CONSULT  │  30–60 min call. Schedule, duties, comp range,
  │             │  special requirements. Educate on employer duties.
  └──────┬──────┘  ← BIGGEST MANUAL TIME SINK #1
         │
         v
  ┌─────────────┐
  │ 3. SOURCE   │  internal roster first, then job boards
  │             │  (Care.com, Sittercity, Indeed, FB groups)
  └──────┬──────┘
         │
         v
  ┌─────────────┐
  │ 4. SCREEN   │  FCRA-governed background checks, sex offender
  │             │  registry, MVR if driving, CPR/First Aid,
  └──────┬──────┘  2–3 verified references
         │
         v
  ┌─────────────┐
  │ 5. MATCH    │  shortlist 3–8 candidates, hand-written fit notes
  │             │  ← BIGGEST MANUAL TIME SINK #2
  └──────┬──────┘  typical: profiles to family in 1–5 days
         │
         v
  ┌─────────────┐
  │ 6. INTERVIEW│  phone/video → in-person. 3-way scheduling.
  │             │  ← BIGGEST MANUAL TIME SINK #3
  └──────┬──────┘
         │
         v
  ┌─────────────┐
  │ 7. TRIAL    │  ALWAYS PAID. 2 days – 2 weeks typical.
  │             │  Some agencies run a guided 30-day trial.
  └──────┬──────┘
         │
         v
  ┌─────────────┐
  │ 8. PLACE    │  fee: 15–30% of first-year gross comp,
  │             │  OR flat $2,500–$4,500. Contract + guarantee.
  └──────┬──────┘
         │
         v
  ┌─────────────┐
  │ 9. SUPPORT  │  30–90 day replacement guarantee.
  │             │  Check-ins at 30/60/90. ← TIME SINK #4
  └──────┬──────┘
         │
         v
  ┌─────────────┐
  │ 10. PAYROLL │  handed off to a specialist provider —
  │             │  agencies do NOT run this themselves
  └─────────────┘
```

### 8.1 Where the social agent plugs in

It feeds **node 1 only** — lead intake. That is its entire job. Do not let it sprawl.

What actually drives local service leads `[SECONDARY]`:
- **Reels / short vertical video** — highest reach and discovery. "Day in the life," safety tips, vetting-process explainers, parent Q&A.
- **Carousels** — highest saves and profile visits. "How to choose a nanny," "5 red flags when hiring childcare." Best for trust-building, which is the whole ballgame in childcare.
- **Static** — lowest organic reach. Announcements and "meet the team" only.
- Suggested cadence: **3–5 Reels/week + 2–4 carousels/week on IG; 3–7 posts/week on FB**, plus near-daily Stories. Call it **30–50 posts/month** for sizing your publisher tier. (This is why bundle.social's 20-post free tier fails.)
- Local signals that matter: complete business info with the correct category ("Child Care Service"), geo-tags, neighbourhood hashtags, Facebook reviews, and **"Send Message" as the primary CTA** — DMs and calls are the conversion event for local services, not link clicks.

**The measurable handoff:** the social agent's success metric is qualified intake-form submissions and DMs, not impressions. Wire node 1's intake source field back to the post that produced it, or you are optimising blind.

### 8.2 Other automatable nodes, ranked by ROI

| Node | Automation potential | Why |
|---|---|---|
| **2. Consult prep** | **High** | Agent pre-reads the intake form and drafts a needs-assessment brief + a realistic local pay range before the call. Saves the recruiter 20 min every time and improves the call. |
| **5. Matching shortlist** | **High** | Agent drafts the fit notes for a human-picked shortlist. **Never let it pick the candidates** — that is a judgement call with a child's safety attached. Draft the prose, not the decision. |
| **6. Interview coordination** | **High, low risk** | Pure scheduling logistics across three parties. Boring, mechanical, entirely automatable. |
| **9. Support check-ins** | **High** | 30/60/90-day check-ins are calendar-driven and templated. Easy win, directly protects the replacement guarantee. |
| **3. Sourcing** | **Medium** | Drafting outreach, yes. Evaluating candidates, no. |
| **8. Contracts** | **Medium** | Generate from a lawyer-approved template with variables filled. Never generate contract *language*. |
| **4. Screening** | **LOW — do not automate the decision** | FCRA governs this. Adverse-action rules mean a wrong automated decline creates legal exposure. Agent may *track* check status; it must not *evaluate* results. |
| **10. Payroll** | **Do not build** | Already solved. HomePay reportedly $59–$75/mo; GTM and Poppins Payroll comparable. Household employer tax is a compliance minefield — FICA withholding threshold reportedly $3,000 in 2026, employer burden ~10% of gross, Schedule H filing, state-by-state workers' comp. **Integrate with a provider. Never reimplement.** |

### 8.3 Classification landmine worth knowing

Nannies are **W-2 household employees, not 1099 contractors**, in essentially all standard placements — the family controls hours, duties and environment. If any agent you build ever drafts copy or documents implying 1099 treatment, that is a real liability for the client. Worth a hard rule.

---

## 9. Child imagery — the constraint that can end the account

This is findings, not preference. For a childcare client it outranks every growth tactic in this document.

`[SECONDARY — FTC COPPA FAQ, Meta transparency and newsroom material, 2026 reporting]`

**The legal position:**
- The FTC treats **photos, videos, and audio recordings containing a child's image or voice as personal information** under COPPA.
- Commercial use of a child's likeness needs a **written guardian release** naming the platforms, the duration, and explicitly covering **paid advertising** — not just organic posts.
- Where parental responsibility is shared, the safe practice is **both parents' consent**. Custody disputes over posted images are a live category of litigation.
- State right-of-publicity and "sharenting" / child-influencer laws add a second layer that varies by state.

**The platform position:**
- Meta runs zero tolerance on child exploitation content and states this applies to **AI-generated material identically to real material**.
- In 2026 Meta was reported to have served ads containing AI-generated CSAM, and responded by tightening enforcement hard. Automated ad review is now aggressive in this category.
- A false positive does not get a warning. It kills the ad account — your client's, not yours.

**What this means for the build:**

1. **Never generate AI images of children.** Not photorealistic, not stylized, not "obviously cartoon." The downside is catastrophic and asymmetric, and the upside is zero.
2. **No identifiable child faces without a release on file.** The agent should check a release registry and refuse to draft if there is no match — the same shape as a SKU-registry pre-check in an e-commerce content agent. Refuse, name the reason, offer the alternative framing.
3. **Default visual language:** staff, parents, homes, hands, toys, backs of heads, blurred faces, empty play spaces.
4. **Disclose AI illustrations** where they might be read as depicting real clients. FTC guidance on deceptive AI content in advertising applies.

**This is not a handicap — it is the winning strategy anyway.** Childcare converts on trust signals: real staff on camera, transparent vetting process, credentials shown, parent video testimonials, community presence. Children's faces convert nothing and risk everything.

---

## 10. Verification checklist — run these before writing code

Four unknowns gate the architecture. Each has a specific test. **Do not proceed past the one that blocks your chosen stack.**

### V1 — Does Composio's managed Meta OAuth carry publish scope? `BLOCKS STACK 2`

This is the highest-value test in the list. A positive result removes an entire vendor from your stack.

1. Create a Composio auth config for the `instagram` toolkit using **Composio-managed OAuth** (not custom credentials). Complete the OAuth flow against a real Instagram **Business or Creator** account. Personal accounts will not work — the toolkit docs say so explicitly.
2. Call the cheapest read that requires business scope:

```
INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT
```

   A `200` with a quota payload means business scope is present. A permissions error means the managed app is read-limited.

3. The real test — attempt a full publish to a throwaway Business account:

```
INSTAGRAM_POST_IG_USER_MEDIA
  image_url = <a publicly reachable HTTPS image URL>
  caption   = "test"
→ capture the returned container id

INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH
  creation_id = <container id>
```

   **Note:** Instagram requires a *publicly accessible URL*. Direct file upload is not supported. Your media pipeline must publish to a CDN or bucket first — factor that in regardless of which stack you pick.

4. Repeat for Facebook against a test Page:

```
FACEBOOK_CREATE_POST   (message = "test", to your test Page)
```

**Record:** did managed OAuth alone get you a published post on each platform, yes or no? Everything downstream depends on this answer.

### V2 — Does Composio's Facebook tool support native scheduling? `BLOCKS STACKS 2 AND 4`

1. Open the Composio playground or SDK introspection for `FACEBOOK_CREATE_POST` and read its **actual parameter schema**. You are looking for `scheduled_publish_time`, `published`, or an equivalently named field. The docs page renders this via JS and could not be read programmatically — check it in the playground UI or via the SDK's tool-schema call.
2. If present, schedule a real post ~15 minutes out (remember the **10-minute minimum**), then confirm it appears in:

```
FACEBOOK_GET_SCHEDULED_POSTS
```

3. Then confirm `FACEBOOK_RESCHEDULE_POST` moves it and that it actually publishes at the target time.

**If `CREATE_POST` has no scheduling parameter,** check whether `FACEBOOK_PUBLISH_SCHEDULED_POST` implies a different creation route, and fall back to calling Meta's Graph API directly for the scheduled-create step while keeping Composio for everything else.

### V3 — Is Zernio real, and does it cover Instagram properly? `BLOCKS STACK 1`

The rebrand from getlate.dev invalidates all secondary research on this vendor. Verify from scratch.

1. Sign up on the free tier. Connect **one Instagram Business account and one Facebook Page** — confirm that counts as 2 accounts and stays free.
2. Confirm **API access is included on the free tier** (not gated behind a paid step). Their pricing page says every feature is included on every account; confirm that is true of API keys.
3. Schedule one of each and verify each actually publishes:
   - IG single image
   - **IG Reel** (the format you will use most)
   - **IG carousel**
   - IG Story — if unsupported, you need a fallback path
   - FB Page post
4. Register a **webhook** and confirm you receive a real `published` event. Webhooks are listed as included; this is what saves you from building a polling loop.
5. Test failure behaviour: schedule with a deliberately broken media URL and confirm you get a usable error, not silence.

### V4 — Confirm the Meta facts that came from secondary sources `INFORMS ALL STACKS`

Read these primary pages directly and record what they actually say today:

| Question | Where |
|---|---|
| IG daily publish cap — 25, 50, or other? | `developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/content-publishing/` |
| FB `scheduled_publish_time` window — is it 30 or 75 days? | `developers.facebook.com/docs/graph-api/reference/page/feed/` |
| Which scopes are Advanced Access, and is Business Verification required? | Meta App Dashboard → App Review → Permissions and Features |
| Sora 2 API shutdown on 2026-09-24 — real? | OpenAI's own API docs and changelog |

Also worth pinning: current Gemini per-image and per-second pricing from `ai.google.dev/gemini-api/docs/pricing`. That page is JS-rendered and resisted scraping; read it in a browser.

### V5 — Cowork operational reality `INFORMS ALL STACKS`

1. Create a Cowork scheduled task and confirm the available frequency options (reported: hourly, daily, weekly, weekdays, manual).
2. **Close the laptop over a scheduled run time and confirm the task does not fire.** Prove the §1.3 constraint to yourself rather than taking this document's word for it — it is the single assumption most likely to wreck the design if it is wrong in either direction.
3. Create a Claude Code **cloud** routine and confirm it runs with the machine off, and confirm the 1-hour minimum interval.
4. Confirm how a Cowork task reaches your publisher — via a custom MCP server, a connector, or a shell/HTTP call. Cowork has no generic "make an HTTP request" primitive; external calls go through MCP tools or connectors. **If you need an MCP server to call your publisher, that is a build task nobody has scoped yet.**

---

## 11. Open questions for the human

1. **Does the nanny business already have an Instagram Business account and a Facebook Page, properly linked?** Instagram must be Business or Creator — Composio and every vendor reject personal accounts. If it is personal today, converting it is step zero.
2. **Who approves?** One person, or owner-plus-marketer? Determines whether the approval queue needs roles at all in v1 (it probably does not).
3. **Where does approval happen?** Cowork itself, a Slack message, a simple web page, or a spreadsheet? Cheapest is whatever they already open daily.
4. **Is there an existing photo/video release process for client families?** If not, that must exist before a single child appears in any post. It is a business process, not a software feature, and it gates §9.
5. **What is the real posting cadence the client will sustain?** §8.1 suggests 30–50/month. If the honest answer is 8/month, several vendor tiers collapse into "free" and this gets even cheaper.
6. **Who owns the Meta assets** — you or the client? Determines whether you can afford to risk their ad account, and who holds the tokens on offboarding.

---

## 12. Sources

**Fetched directly, 2026-09-19 `[PRIMARY]`**
- `docs.composio.dev/toolkits/instagram` — toolkit version `20260915_00`, 38 tools, managed OAuth
- `docs.composio.dev/toolkits/facebook` — toolkit version `20260902_00`, 44 tools, managed OAuth
- `docs.composio.dev/kb/toolkit/facebook`, `.../instagram` — setup and OAuth guidance
- `code.claude.com/docs/en/desktop-scheduled-tasks` — the cloud / desktop / loop comparison table
- `ai.google.dev/gemini-api/docs/models` — current model IDs
- `ai.google.dev/gemini-api/docs/video` — "use Gemini Omni Flash as your default model for video generation"
- `ai.google.dev/gemini-api/docs/image-generation` — Nano Banana
- `getlate.dev/pricing` → now Zernio — the pricing table in §4.1
- `bundle.social/pricing` — Free / Pro $100 / Business $400, per organization
- `ayrshare.com/pricing` and `ayrshare.com/docs/apis/post/post` — `scheduleDate`, `status: "scheduled"`, 99.99% uptime, MCP server

**Perplexity Sonar research, 2026-09-19 `[SECONDARY]`** — Meta IG/FB publishing API requirements and 2025–26 deprecations; third-party posting API comparison; AI image and video API landscape; Claude Cowork scheduled tasks; nanny agency operations, fees, screening and household payroll; childcare social media practice and child-imagery law. Underlying citations included FTC COPPA FAQ, Meta developer docs and newsroom, APNA client-contract guidance, GTM / HomePay / Poppins Payroll, and named agency fee pages.

---

*Facts in this document were true on 2026-09-19 and several are moving fast. Anything tagged `[SECONDARY]` or `[UNVERIFIED]` should be re-checked before it becomes load-bearing.*
