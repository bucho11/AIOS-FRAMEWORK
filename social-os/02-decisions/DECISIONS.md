# Decision log

> Append-only. Never delete a decision — supersede it with a new entry.
> Every decision carries a **reversal trigger**: the specific fact that, if it
> changed, should make us revisit. A decision without one gets silently
> re-litigated in three weeks.

---

### DEC-001 — Single agent + skills, not multi-agent
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** One Cowork agent with many skills. No agent-to-agent orchestration.
**Why:** The operator proposed it and he is right. Multi-agent adds coordination
failure modes, debugging difficulty and cost for zero benefit at this scope. The
work is sequential (research → draft → image → approve → publish), not parallel.
**Reverses if:** a single client needs genuinely concurrent independent workstreams —
realistically not before ~50 locations on one account.

### DEC-002 — Google Drive via connector. Not a local folder. Not Notion.
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** The filesystem is a Google Drive folder reached through the Drive
connector.
**Why:** Forced, not preferred. Anthropic `[PRIMARY]`: Cowork scheduled tasks
*"can't be tied to a folder on your computer"* — they see connectors and files in
the Claude account. A local folder goes dark for **every automated run**, which is
the half of the system the client is paying for. Drive over Notion because Drive
holds real image and video files and Notion is a database wearing a filesystem's
clothes.
**Reverses if:** Anthropic gives cloud scheduled tasks access to synced local folders.

### DEC-003 — Approve-then-publish is a hard gate
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** Nothing publishes without explicit human approval, in Cowork.
**Why:** Operator's explicit answer, and correct independently: this is a
childcare brand where one bad post is existential, not a metric dip.
**Reverses if:** the operator explicitly graduates a specific content type after a
sustained track record. Graduate by *category* (e.g. "open roles"), never wholesale.

### DEC-004 — No own Meta app, no App Review
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** Inherit a vendor's reviewed Meta app.
**Why:** App Review plus Business Verification is a multi-week gate with real
rejection risk, **per franchise**. It would make the product un-clonable, which
is the entire commercial thesis. Both Composio and Ayrshare remove it.
**Reverses if:** vendor fees exceed roughly an engineer-week per quarter, or a
surface is needed that no vendor exposes consistently (Stories is the usual one).

### DEC-005 — Ayrshare is the publisher. Composio is the connector layer + fallback.
**Date:** 2026-09-19 · **Status:** ⏳ **recommended, pending operator sign-off**
**Decision:** Ayrshare owns publishing and scheduling for IG + FB. Composio stays
for Drive and future workflows, and is the ready fallback behind the seam.
**Why:**
- "Proven" was stated twice as the bar. Ayrshare is the category veteran;
  Zernio is one year old and eight people.
- It removes the most fragile component entirely — **nobody on our side owns the
  Instagram clock.** No retry logic, no quota surprise, no silent failure.
- It ships an **MCP server**, so Cowork talks to it with no code.
- Economics invert with scale: $149 for one client, ~$30/client at ten,
  ~$20/client at thirty. With ~20 markets in play, the portfolio price governs.
**Rejected — Zernio:** $0 and genuinely promising, but founded 2025, team of 8,
bootstrapped. Fails the stated "proven" bar for a childcare brand's lead engine.
**Rejected — Composio-direct as primary:** credible and free, but we would own the
IG clock, retries and alerting. Correct later; wrong for launch.
**Reverses if:** Ayrshare's price stops justifying itself at scale, or a live test
shows the Composio publish path is solid **and** the operator re-weights toward cost.

### DEC-006 — Bannerbear is the image layer. Canva is a human tool, not an API.
**Date:** 2026-09-19 · **Status:** ⏳ **recommended, pending operator sign-off**
**Decision:** Branded graphics via Bannerbear template-fill. Canva stays for
human design work.
**Why:**
- Canva Connect autofill is **Enterprise-only** (`[PRIMARY]`, Canva's own docs).
  Pro is our floor, so it is unavailable.
- Bannerbear **hosts the output at a public HTTPS URL**, which is exactly what
  Instagram requires and what a **Google Drive share link cannot provide**. One
  vendor closes two gaps.
- It ships an **MCP server**. No code.
- Most established in a mature category — the "proven" bar.
- AI image generation rejected for the *layout*: brand lock, typography and logo
  placement are what diffusion models do not guarantee, and no AI children is a
  hard rule anyway.
**Reverses if:** the client turns out to have Canva Enterprise, or Bannerbear's
hosted-URL behaviour fails `OQ-003`.

### DEC-007 — Client owns her data; operator owns the machine
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** Client owns Meta accounts and the Drive folder (operator as Editor).
Operator owns Composio, Ayrshare, Bannerbear and the skills/templates.
**Why:** She can walk away with everything that is hers and still hold nothing
that competes. That is what makes it safe to sell her — and referral to the brand
owner is the whole play. Holding a client's accounts or data is how that dies.
**Reverses if:** a brand-level deal makes corporate, not the franchisee, the
account owner.

### DEC-008 — Original files only. No AIOS source copied.
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** Borrow AIOS *structure*; write original text.
**Why:** AIOS is GPL-2.0-or-later. Copying its files into a product sold to
franchises attaches GPL obligations. Structure is not copyrightable; the text is.
Costs nearly nothing and keeps commercial rights clean.
**Reverses if:** the operator accepts GPL terms for the distributed product.

### DEC-009 — Build on Anthropic's plugins, don't rebuild them
**Date:** 2026-09-19 · **Status:** ✅ locked
**Decision:** Install Anthropic's `small-business` plugin (and `marketing` where
useful) as the generic capability layer. Our own build shrinks to: the deep
onboarding that fills the brain, the publish skill (swap seam), the learning
loop, and the childcare domain guardrails.
**Why:** `[PRIMARY]` Anthropic ships 43 skills in `small-business` including
`smb-onboard`, `social-content-engine`, `brand-style` and a shared
`voice-profile.md`. Rebuilding those is wasted work that decays as they improve.
Three verified gaps remain ours: **no IG/FB publishing** in either plugin,
**Canva autofill is Enterprise-only so their Pro path is semi-manual**, and
**their memory is one opaque `## Business context` block** with no
declared/observed split, no versioning, no portability and no learning loop.
**Reverses if:** Anthropic ships IG/FB publishing and a structured, portable,
client-owned context layer. Watch `anthropics/knowledge-work-plugins` — this is
the single most important thing to monitor for this business.

### DEC-010 — **REVERSES DEC-005.** Zernio is the publisher, at $0.
**Date:** 2026-09-20 · **Status:** ⏳ pending one verification (`OQ-009`)
**Decision:** Zernio free tier (2 accounts = 1 IG + 1 FB) publishes and schedules.
Ayrshare becomes the documented upgrade path, not the launch choice.
**Why this reverses DEC-005:** that decision rested on the operator's stated
"proven beats cheap." On 2026-09-20 he explicitly re-weighted to **most
affordable, one client, free if possible.** With the tiebreaker flipped the
earlier reasoning no longer holds, and Ayrshare's real floor is **$149/mo with no
free tier** — verified on their own pricing page, not the $0 the budget now asks
for. Zernio is **$0** for exactly the two accounts needed, with full API, an MCP
server, webhooks and unlimited posts, and **no feature tiers** between free and paid.
**The risk, stated plainly:** Zernio is a 2025-founded, 8-person, bootstrapped
company. That is a real maturity gap. It is acceptable here because (a) nothing
publishes without human approval, (b) Google Drive holds all content so a vendor
failure loses no work, (c) the swap seam makes changing publishers a one-file
edit, and (d) at $0 the downside is time, not money.
**Reverses if:** client count passes ~10, or Zernio fails `OQ-009`, or a
reliability incident occurs. Then Ayrshare Launch ($299 / 10 profiles ≈
$30/client) becomes the rational choice.

### DEC-011 — **REVERSES DEC-006.** Cloudinary replaces Bannerbear, at $0.
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** Cloudinary free tier for generated graphics + public URLs. Canva
stays as the free manual design tool. Bannerbear is cut.
**Why:** Bannerbear is **$49/mo** with only a 30-credit trial. Cloudinary is
**free forever**, 25 credits/mo (1 credit = 1,000 transformations), does text
overlay via URL parameters, and returns a public HTTPS CDN URL — which is exactly
what Instagram requires. `[PRIMARY]` Claude cannot generate images natively, so
some external layer is required; this is the free one.
**Also:** if `OQ-009` confirms Zernio hosts uploaded media, Cloudinary is needed
only for *generating* graphics, not for hosting — and becomes fully optional for v1.
**Reverses if:** Cloudinary's URL-based text overlay proves too limited for her
carousel layouts. Then APITemplate.io free (50/mo, visual editor) is next.

### DEC-012 — Ship the loop before the graphics
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** v1 ships with real media (her Reels and photos) + Claude-written
copy. Generated graphics are added after one real post has published end to end.
**Why:** the sector research says Reels and real photos are the highest-converting
content and **neither needs image generation** — only hosting. A beautiful image
pipeline over untested publishing plumbing is the classic failure mode here.
**Reverses if:** she has no usable photo/video library at all, making graphics the
only possible content.

### DEC-013 — Nothing for this venture lives in HIDEit's Google Workspace or Claude account
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** Build nothing for this venture inside the `@hideitmounts.com`
Workspace. No Drive folders, no files. The repo is the factory; client Drive
folders are created in the **client's own** Google account, with a **personal
operator Google account** (outside any employer domain) holding Editor access.
**Why — visibility `[PRIMARY]`, Google's own docs:** in Google Workspace,
"private" means *not shared with coworkers*, **not** hidden from admins. A super
admin can reach any My Drive file through **Vault export** ("Drive files owned and
shared with a specific user"), **org-wide data export**, or **ownership transfer**
— which Google explicitly says can include *"files that aren't shared with
anyone."* The Drive audit log records every file created. Google documents **no**
mode in which a Workspace user can create files their admin cannot reach; the only
remedy is to be outside the managed domain.
*Fair nuance:* an admin cannot casually browse a My Drive from the Admin console —
it takes a deliberate export or transfer. Not on a dashboard; fully reachable if
anyone looks.
**Why — ownership, the larger risk:** this venture is intended for resale to ~20
franchises. Work product created inside an employer's systems is commonly
claimable by that employer under standard IP terms. Visibility is the small
problem; **ownership is the big one.**
**Consequence:** the "master template in the operator's Drive" step from
`delivery-model.md` Phase 1 is **removed**. It was a convenience, never a
requirement. The template lives in the repo and is materialized directly into the
client's Drive at setup. **Phase 1 needs no Drive at all.**
**Also flagged, not yet decided:** the Claude account and GitHub org in use are
likewise employer-associated. Migrating the venture to its own Claude account and
its own GitHub is far cheaper now than after a client and 20 franchises are
attached. Tracked as `OQ-011`.
**Reverses if:** the operator obtains explicit written consent from HIDEit that
this venture and its artifacts are personally owned — in which case the visibility
point still stands and only the ownership risk clears.

### DEC-014 — Distribution is our own plugin, synced from our own GitHub marketplace
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** Build one plugin in one GitHub repo that carries a
`.claude-plugin/marketplace.json`. Clients add the marketplace once and install.
Fork nothing.
**Verified `[PRIMARY]`** (Anthropic, "Use plugins in Claude"): *"Add from a
repository: Sync a marketplace from a GitHub repository or git URL."* Path is
**Customize → Plugins → Personal plugins → "+" → Add marketplace → Add from a
repository**. Plugins work in *"chat on the web, the Chat tab in Claude Desktop,
and Claude Cowork."* Available on **all paid plans**, so Pro qualifies.
> A secondary source claimed GitHub marketplaces are Claude-Code-only. **That is
> wrong** — it was reading Claude Code docs. Anthropic's claude.ai plugins article
> documents the repository sync for Cowork explicitly.
**Format confirmed** from `anthropics/knowledge-work-plugins/.claude-plugin/marketplace.json`:
a `name`, an `owner`, and a `plugins[]` array where each entry has `name`,
`displayName`, `description`, `category` and a `source` (a local path like
`"./productivity"`, or a `git-subdir` object).
**Fork nothing:** real public skill libraries exist (`claude-market/marketplace`,
`alirezarezvani/claude-skills`, `claude-office-skills/skills`, `lyndonkl/claude`,
`VoltAgent/awesome-agent-skills`, `anthropics/skills`), but they are **generic**.
None encode childcare compliance, nanny-agency operations, or Zernio. Read them
for structure; the manifest is ~20 lines. The value is the domain content, not the
scaffolding.
**Reverses if:** Anthropic removes repository-sync from claude.ai/Cowork.

### DEC-015 — The repo is NOT the brain. It cannot be.
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** The plugin repo ships **instructions**. The client's Google Drive
holds **memory**. They are not interchangeable and neither replaces the other.
**Why:**
1. **A plugin is one-way.** Claude reads it on install and on update. It never
   writes back. The brain must be written to continuously — what worked, her
   corrections, published posts, the calendar.
2. **There is no GitHub connector** in Claude's connector directory (checked
   directly, 2026-09-20). Cowork cannot read or write a repo as a filesystem.
3. **The plugin is identical for all 20 franchises; the brain is unique to each.**
   Putting the brain in the repo would mean a fork per client that Claude could
   not update.
**The model:** *the repo is the machine · Drive is the memory · Zernio is the hands.*
**Reverses if:** a first-party GitHub connector with write access ships for Cowork.

### DEC-016 — Drop Cloudinary from v1. Correcting an overstatement.
**Date:** 2026-09-20 · **Status:** ✅ locked · **supersedes DEC-011**
**Decision:** No image-generation vendor in v1. Content is her **Reels and real
photos** (Zernio hosts them) plus **Canva** (free, manual) for the occasional
designed graphic.
**Why — the correction:** Cloudinary genuinely does text-on-image by URL
(`l_text:Arial_80:Hello,fl_layer_apply`). But verified honestly, it is suited to
*"watermarks, badges, labels, promo callouts, and simple quote cards"* and
explicitly **not** to *"fully designed branded social media graphics with careful
typography, spacing, line breaks, and visual hierarchy."* DEC-011 oversold it as a
Bannerbear replacement. It is not one.
**Also:** the sector research says her highest-converting content is **Reels and
real photos**, which need **no generation at all** — only hosting, which Zernio
does. Adding a vendor for the minority case complicates the client sale for little
gain.
**Reverses if:** she has no usable photo or video library, making graphics the only
possible content. Then APITemplate.io free (50/mo, real visual editor) beats
Cloudinary.

### DEC-017 — Ship only our plugin in v1. Skip Anthropic's `small-business`.
**Date:** 2026-09-20 · **Status:** ✅ locked · **narrows DEC-009**
**Decision:** v1 installs **one** plugin — ours. Anthropic's `small-business`
plugin is not part of the client setup.
**Why:** it carries **43 skills and ~34 connectors** covering payroll, tax prep,
inventory, Shopify, bookkeeping. For a nanny franchise doing Instagram and
Facebook that is mostly noise, and every irrelevant skill is a phantom capability
the client can trigger by accident. DEC-009's reasoning (don't rebuild what
Anthropic maintains) still holds for *us* — we read their skills for patterns —
but shipping it **to her** costs clarity, which is the thing being sold.
**Reverses if:** the client asks for broader business automation. It is a one-click
install at any time; nothing is lost by deferring it.

### DEC-018 — Canva ships inside the plugin. Canva **Pro** is enough.
**Date:** 2026-09-20 · **Status:** ✅ locked · **supersedes the Canva half of DEC-016**
**Decision:** The **native Canva MCP connector** ships as part of our plugin,
alongside Zernio. Canva **Pro** is the required plan.

**The correction I owe the record:** DEC-006 and DEC-016 said "Canva is out."
That generalised one endpoint to the whole product and was **wrong**. What is
Enterprise-gated is **brand-template autofill**, not Canva. Canva's own MCP
documentation gates by capability, not by product:

| Capability | Free | **Pro** | Enterprise |
|---|---|---|---|
| Create designs | ✅ | ✅ | ✅ |
| Edit designs | ✅ | ✅ | ✅ |
| Search designs | ✅ | ✅ | ✅ |
| Export | ✅ standard | ✅ **lossless PNG, transparent bg, premium elements** | ✅ |
| Asset upload | ✅ | ✅ | ✅ |
| Comments | ✅ | ✅ | ✅ |
| **Resize design** | ❌ | ✅ **Pro and above** | ✅ |
| Autofill templates | ❌ | ❌ | ✅ |
| Brand kits / brand templates | ❌ | ❌ | ✅ |

`[SECONDARY]` from Canva's official MCP docs: the server *"works with a Canva
account on any plan"*; resize requires Pro+; autofill, brand kits and brand
templates require Enterprise.

**Why Pro is genuinely sufficient:**
- **`resize-design` is the sleeper feature.** One design → IG feed, IG Story, FB.
  That is the single most repetitive task in social, and it is a Pro feature.
- **Pro exports are production-grade** — lossless PNG and transparent backgrounds.
- **The brain replaces the Brand Kit.** Brand Kit is Enterprise, but we do not
  need it: `Brand voice.md` and `Colors and fonts.md` in her Drive hold the exact
  hex values, fonts and layout rules, and Claude applies them when creating the
  design. **Our context layer substitutes for the feature we cannot buy** — which
  is the product thesis working exactly as intended.

**What we still cannot do:** fill variables into a locked brand template in one
call. Claude creates and edits each design instead. Slightly more model work per
graphic, same output, no Enterprise contract.

**Reverses if:** a client is on Canva Free (no resize — the main loss), or turns
out to have Enterprise (then autofill is worth wiring).

### DEC-019 — Canva makes it, Zernio hosts and ships it
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** Canva is the **design** surface. Zernio remains the **hosting and
publishing** surface. Canva exports → the file is uploaded through Zernio's
presign flow → the returned `publicUrl` goes into the post.
**Why not pass a Canva export URL straight to Instagram:** Canva Connect export
URLs are job-scoped and expire; Instagram requires a durable, directly-fetchable
public HTTPS URL. Re-hosting through Zernio (`POST /v1/media/presign` → 5 GB,
permanent `publicUrl`) removes that whole class of failure.
**Verify at build time (`OQ-013`):** the exact shape the Canva MCP returns on
export, and that the handoff to Zernio's upload needs no manual download step.
