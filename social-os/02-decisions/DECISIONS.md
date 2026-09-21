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

### DEC-020 — Brain files are Google Docs; "update" is create-new + trash-old
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** Every document in the owner's Drive brain is a **Google Doc**. Claude
never edits in place; it replaces (create same title/parent → `trash_file` old) or
appends a new dated doc. `Learned by us/What works` is a rolling "current" doc plus
one immutable doc per week.
**Why `[PRIMARY]`:** the Google Drive connector's `update_file` changes **only title
and parent**; there is no content-edit tool. `read_file_content` supports Google
Docs/Sheets/Slides, PDF, Office and images — not `.md`. `create_file` converts text
to a Google Doc by default. So Docs are the only format both she and Claude can read
and that Claude can write. The append-only weekly pattern also happens to be AIOS's
own snapshot discipline — history for free.
**Reverses if:** the Drive connector gains content editing, or a first-party Docs
connector ships.

### DEC-021 — Canva exports happen at approval time, never at draft time
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** `make-graphic` records `canva_design_id` + edit URL in the packet and
does not export. `publish` exports at the moment of approval and hands the fresh URL
straight to Zernio.
**Why `[PRIMARY]`:** Canva: *"Signed export URLs expire. Use them immediately, and
don't store or share them."* A URL minted at draft time is dead by approval time.
Also Cowork's sandbox egress is **allow-listed through a mandatory proxy**, so a
re-hosting script (GET Canva → PUT Zernio storage) cannot be relied on. Exporting
inside the approval step removes the gap. Bonus: Canva's own handoff guidance is to
surface the edit URL so the owner can adjust before export — which is exactly the
approval gate.
**Still open (`OQ-013`):** whether Zernio fetches an external `mediaItems.url` at
post creation or at publish time. If at publish, a long-scheduled post could outlive
the signed URL. Mitigation in the skill: `validate_media` before submit and prefer
the Zernio upload path when the schedule is far out.

### DEC-022 — Guardrails are three layers; only the first two are load-bearing
**Date:** 2026-09-20 · **Status:** ✅ locked
**Decision:** (1) `shared/guardrails.md` read by every drafting/design/publish skill;
(2) an independent read-only **`compliance-reviewer` sub-agent** that fills
`## Compliance check` before a packet can be approved; (3) an optional
**PreToolUse prompt hook** on the vendor's publish/update tools as a last line.
**Why:** `[PRIMARY]` Anthropic: *"Hooks and sub-agents run only in Cowork, so they
appear grayed out in chat"* — both are available where this runs. The reviewer is
the AIOS "independent judge" principle: a second reader catches what the author
cannot. The hook is defence in depth but hook-*type* support in Cowork is not
enumerated (`OQ-014`), so nothing depends on it firing.
**Reverses if:** the hook proves reliable in Cowork — then it could become the
primary gate and the reviewer a quality pass.

### DEC-023 — Canva is an upgrade, not a dependency
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** `0 — Setup` carries `canva_available: yes | no`. With `no`, the system
runs fully on photos, short videos and text; `make-graphic` refuses loudly rather
than half-working, and `plan-week` converts graphic slots to photo or Reel slots.
**Why:** the operator is not buying Canva Pro, so the Canva path cannot be tested
before the first client. Rather than ship an untested component in the critical
path, it moves out of it. This costs almost nothing: sector research ranks **Reels
and real photos** as the highest-converting content for local childcare, and those
need no design at all — only hosting, which Zernio does. Graphics matter for
carousels and quote cards, which are the minority case.
**Consequence:** the end-to-end path that ships **fully verified** is
brain → plan → draft → owner media → Zernio upload → validate → schedule → publish
→ learn. Canva is additive and gets proven on the first client who has Pro.
**Reverses if:** the operator or a client provides a Canva Pro account to test with.

### DEC-024 — Bundled files live inside their skill; cross-plugin refs use `${CLAUDE_PLUGIN_ROOT}`
**Date:** 2026-09-21 · **Status:** ✅ locked · **fixes a real bug**
**Decision:** `drive-template/` moved to `skills/brand-onboarding/assets/`. Every
reference that escaped a skill's own directory now uses the documented
`${CLAUDE_PLUGIN_ROOT}/…` variable. The four hard safety rules are also **inlined**
into `draft-post`, `make-graphic` and `publish`.
**Why `[PRIMARY]`:** Anthropic's skills documentation states that relative paths in
`SKILL.md` **resolve within the skill's own directory**, and that
`${CLAUDE_PLUGIN_ROOT}` is the way to reach other plugin resources
(`${CLAUDE_SKILL_DIR}` for a skill's own). The convention is that bundled files —
`references/`, `scripts/`, `assets/` — live **inside** the skill, with `assets/`
specifically for "templates and files used in output."
**The bug:** 22 references across 8 files used `../../shared/…` and
`../../drive-template/…`, which escape the skill directory and would not have
resolved. Every skill would have run without its shared guardrails, Drive
conventions and post-packet spec — silently, with no error. Found only because the
operator asked how the folder template reaches Drive.
**Belt and braces:** `${CLAUDE_PLUGIN_ROOT}` substitution is documented for Claude
Code; whether Cowork substitutes it identically is unverified (`OQ-017`). So the
four rules that must never bend are now written **directly into** the three skills
that could otherwise publish something harmful. A failed file load now degrades
gracefully instead of silently dropping safety.
**Reverses if:** nothing. This is strictly more correct.

### DEC-025 — The folder is a workspace with rooms, not a social media tool
**Date:** 2026-09-21 · **Status:** ✅ locked · **supersedes the layout in DEC-002's spec**
**Decision:** The client folder is `<Business> — AI Workspace`. Two shared things
(`1 — Brain`, `2 — Brand Assets`) and **N rooms**, starting with `3 — Social`. A new
domain — email marketing, reviews, recruiting, invoicing — takes the next free
number and never disturbs a room that already works. `9 — Archive` is shared.
**Why:** the operator's stated goal from the first conversation was *"she wants all
of her tasks automated"*, and he confirmed she will want email marketing and other
plugins over time. The previous layout hard-coded social into the top level
(`3 — Content`, `4 — Results`), so a second domain had **nowhere to go** — it would
have been bolted into the social room or dumped loose at the root.
**What makes growth real rather than aspirational:** a new shared reference,
`growth-and-upkeep.md`, carries the **router** (where does a new thing go, asked in
order), the **rule of three** (three loose files of a kind earn a subfolder, named
for the species not the date), the **room-creation procedure**, and the rule that
**the brain does not fork** — a new room reads the same voice and offers, so it
knows who she is on day one. Every skill that creates a folder or document reads it
first. `0 — What's Installed` is the registry she and Claude both read.
**Reverses if:** nothing. A single-domain layout was the defect.

### DEC-026 — Housekeeping: the system maintains itself, and reports rather than rearranges
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** A seventh skill, `housekeeping`, runs monthly: ages published content
into the archive at ~90 days, compacts a finished quarter's weekly learning notes
into one summary (archiving the weeklies rather than deleting them), flags stale
brain documents, surfaces broken connections and un-retried failures, checks the
registry against reality, and names drift.
**Why:** this was the largest AIOS discipline missing. AIOS's own
`/aios:housekeeping` runs **28 audit buckets** precisely because a context system
that only ever grows becomes unusable in about a year. Ours had **none**. Left
alone, `Learned by us` reaches 52 weekly documents and `4 Published` reaches
hundreds of packets, with nothing archiving, compacting, or noticing drift — and
the owner is the one who has to look at it.
**The stance is load-bearing:** it **reports and proposes; it does not reorganise.**
The one exception is the mechanical 90-day archive sweep. A system that silently
moves her things is one she stops trusting, and trust is the product. Nothing is
ever deleted — archived.
**One inheritance worth naming:** it also watches whether *trust should grow* — if
she has approved everything for months, it offers, once and by category, to let a
low-risk category run on its own. That is AIOS's `INTENT.md` recalibration, in
plain English.
**Reverses if:** nothing.

### DEC-027 — One job, one document. A correction replaces; it never appends.
**Date:** 2026-09-21 · **Status:** ✅ locked · **the core invariant**
**Decision:** Every document in `1 — Brain/` holds exactly one named job, and no
two documents may hold the same job. A correction therefore **replaces** the
document that caused the behaviour. It never adds a note, a "preferences" file, or
a second document beside the old one. Every job is listed in `0 — Map`, which makes
the rule checkable in one read rather than a Drive sweep.
**Why:** the operator named the failure exactly: *"the agent just says oh I'm sorry
I'm just going to go fix it but doesn't actually fix it, it just layers another
context layer on top, so now there's two contradicting things — a corrected form
and the older form."* Two live documents answering one question is worse than
neither: the system is confidently wrong and nobody can see which one is winning.
**A check nobody can afford stops running**, which is why the rule is enforced
through the map rather than by reading the folder — two calls, not twenty.
**Reverses if:** never. Everything else here is an implementation of this.

### DEC-028 — Rules govern, records don't — and `Her preferences` is retired
**Date:** 2026-09-21 · **Status:** ✅ locked · **supersedes the `Her preferences`
document in DEC-002's layout**
**Decision:** Two species of document. **Rule documents** (`1 — Brain/Told to us/`,
`0 — Map`) hold what is true *now*, are replaced in place, and are the only things
that change behaviour. **Record documents** (`Learned by us/`, `History`, results,
post packets) are dated, appended, never replaced, and have **no authority**.
Evidence may choose between options the rules allow; it may never change what is
allowed. When results imply a rule should change, Claude **proposes** it, she says
yes, and it goes into `Told to us/`.
`Learned by us/Her preferences` is **deleted**. `Told to us/How she likes to work`
is added as a proper rule document for working-style preferences.
**Why (a defect found in our own build):** the shipped seed text for
`Her preferences` read *"If you tell Claude 'never say X' or 'always do Y', it
lands here and holds from then on."* That is a claim of authority over `Brand
voice` — a second document about how to write, sitting beside the first. We shipped
the exact failure this system exists to prevent, in the onboarding defaults, and it
would have been seeded on day one of every client. This is also why a rule document
holds no history: `What we offer` says $30/hour and never "was $25" — the old value
goes to `History`, so the governing layer can never accumulate two answers.
**Reverses if:** never. If a preference has no home, the answer is a new rule
document with a distinct job, not a notes file.

### DEC-029 — `0 — Setup` + `0 — What's Installed` merge into `0 — Map`
**Date:** 2026-09-21 · **Status:** ✅ locked · **supersedes the two index documents
in DEC-025**
**Decision:** One agent-facing index at the top of the workspace, read first every
session: settings, every folder ID, one row per rule document carrying **the single
job it holds**, plus the rooms and connections registries. `0 — Start Here` stays
separate — that one is written for her. Spec lives in `shared/the-map.md` and
nowhere else, so the format cannot drift. Pointers only, never prose; records are
excluded, which caps it at roughly thirty lines forever.
**Why:** three things at once. (1) The operator's constraint — *"a constantly
updating directory so the agent never searches many files; overbloating context is
something I will not accept."* One small read replaces N searches, and the cost
does not grow as the workspace grows into email, reviews and invoicing. (2) Two
index documents can disagree about where the drafts are; one cannot. (3) **It is
the contradiction index** — listing each document's job is what makes DEC-027
enforceable at change time instead of at audit time.
**Reverses if:** the map ever exceeds ~50 rows, which would mean records or prose
leaked in. Fix the leak, don't split the map.

### DEC-030 — The guard runs at change time; housekeeping is the backstop
**Date:** 2026-09-21 · **Status:** ✅ locked · **narrows DEC-026**
**Decision:** An eighth skill, `update-the-brain`, is the only sanctioned path to
change a rule document, add a room, or respond to pushback. It runs synchronously
on **every** rule-document write and **every** correction. `housekeeping` is
demoted from "the maintenance pass" to a monthly **safety net plus janitor**: it
audits the invariants the guard should have held (two-documents-one-job,
map-matches-Drive, no hand-edits, no rule hiding in `Learned by us`), then archives,
compacts, and flags staleness.
**Why:** this was the operator's direct question — *is housekeeping the right
approach?* It is not, as the guard. **A contradiction is born the instant a change
lands, not on the first of the month.** A monthly sweep leaves a wrong rule
governing for up to thirty days, which is long enough to produce thirty pieces of
wrong work — precisely the *"four to six months from now they don't like what's
happening"* scenario. The guard's check costs two calls (read the map, check
`modifiedTime`), which is cheaper than one Drive search, so "always" is affordable.
Defense in depth, honest about which layer is load-bearing.
**Reverses if:** never; the two jobs are genuinely different.

### DEC-031 — Pushback is a barrier, not a remark. Never apologise first.
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** Correction, confusion, disagreement, repetition, and silent rejection
(three passes with no reason given) all stop the task in flight. The first response
is never *"sorry, I'll fix it"* — it is **naming the document that caused it**, or
one short question answerable in a word. Then: fix the source, handle the blast
radius, re-stamp the map, log to `History`, resume **from the corrected state**.
**"I already told you" gets the full pass**, not a targeted one — a repeat means a
previous fix never landed in a document, which almost always means a second
document holding the same job exists.
**Why:** research into human-AI repair converges on *"acknowledge once, correct
once, verify if needed, then proceed from the corrected state,"* and names the
specific failure of *accepting the correction socially while leaving the internal
state unchanged.* That is what an apology is. Two guards against overcorrecting in
the other direction: **verify before you flip** (say what the document currently
holds — she is usually right, but silently rewriting canon to match a
misremembering is the same corruption wearing a nicer face), and **don't
re-litigate afterwards** — one confirmation, then it is simply how things are.
**Reverses if:** never.

### DEC-032 — Three instruction tiers with fixed roles; the bootstrap is pasted at setup
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** **Bootstrap** (Cowork Project instructions — seven rules that must
fire with zero tool calls; pasted once at setup, identical for every client but the
folder name) · **Law** (this plugin — how the system behaves, same everywhere,
versioned in git) · **Facts** (her Drive — who she is, her IDs, her rules). Nothing
client-specific in the plugin. No behaviour rules in her Drive. Precedence is stated
identically in all three and is **ordered, not accumulated**: what she just said >
`Told to us/` > `0 — Map` > `Learned by us/` > plugin defaults.
**Why:** Cowork does not read a CLAUDE.md-style file out of a connected Drive folder
— verified. Project instructions are the only text guaranteed to be in context
before any tool runs, which is exactly what the pushback rule and the read-the-map
rule need, because both govern the moment *before* a skill is chosen. The research
on multi-source instruction systems is unambiguous that tiers need **explicit
precedence rather than accumulation**, and that rebuilding from canonical state
beats merging historical instructions. Anthropic's docs do not say Claude can update
*project* instructions from inside a session, so the bootstrap is deliberately fixed
at setup and carries nothing that changes over time — no IDs, no capacities, no room
list. Those live in `0 — Map`.
**Reverses if:** Anthropic documents in-session editing of project instructions,
which would let the bootstrap carry live state. Even then, probably don't — a second
place for facts to live is a second place for them to be wrong.

### DEC-033 — She changes the system by talking; a hand-edit is a stop, not an overwrite
**Date:** 2026-09-21 · **Status:** ✅ locked · **fixes a data-loss bug in DEC-020**
**Decision:** The owner never edits her Drive folder by hand; every change is a
sentence in chat. Because that is a promise and not a lock, **before replacing any
rule document**, `get_file_metadata` → is `modifiedTime` later than the file's own
`createdTime`? Yes means a human edited it: **stop**, read it, tell her what
changed, ask whether to keep it, fold it in properly. `0 — Start Here` teaches this
with the reason, not as a rule — *if you change it there, I won't know, and we'll
end up with two versions.*
**Why:** the operator's requirement — *"we don't want the user to go into the drive
and actually make any changes."* It is also a **live bug fix**: DEC-020 established
replace-by-recreate (create new, trash old) because the Drive connector's
`update_file` cannot change content. If she had a document open in Google Docs, that
sequence would trash the file her edits live in — **silent data loss, no error**.
One `get_file_metadata` call turns it into a question. Enforcement is impossible (it
is her Drive), so the design is: make it unnecessary, make it detectable, make it
recoverable.
**Verified 2026-09-21, and the probe changed the design:** `get_file_metadata`
returns both `modifiedTime` and `createdTime` as RFC3339 UTC — but `modifiedTime` is
**not reliably wall-clock**. On a real uploaded file it came back *earlier* than
`createdTime`, because the upload preserved the source's mtime. So the check is
anchored on the file's **own** `createdTime` rather than the map's `claude_wrote`
stamp: every replacement mints a new file, so `createdTime` *is* Claude's write
moment, and it is immutable. The map stamp is the cross-check — if it disagrees with
`createdTime`, the row is stale and gets healed first. The original stamp-only
design would have inherited the mtime quirk and could have missed a hand-edit.
**Reverses if:** the Drive connector ever gains real content editing, which removes
the trash step and most of the risk. The check stays useful regardless.

### DEC-034 — Growth goes through the same door: the brain does not fork
**Date:** 2026-09-21 · **Status:** ✅ locked · **hardens DEC-025 §3**
**Decision:** Adding a room, connector, or domain runs through `update-the-brain`
and the same laws. A new room may **not** duplicate a job: no "Email brand voice"
beside `Brand voice` — a section inside the one document if a room genuinely needs
different treatment. A room adds *working material*, never a second copy of a rule.
Every new room, connector or skill gets exactly one row in `0 — Map`, and the map is
rebuilt.
**Why:** the operator's requirement that this be *"ever evolving for everything, not
just social media — QuickBooks, Klaviyo"* in a *"highly disciplined way."* None of
DEC-027 through DEC-033 mentions social media; they are laws about documents and
jobs, so they hold for every future domain unchanged. The one place growth
predictably breaks them is room creation, because a new domain *feels* like it needs
its own voice — and the moment there are two voice documents, every subsequent
correction lands in one of them at random. That is the single most likely way this
system ever acquires a contradiction, so it is checked before the room is made
rather than audited afterwards.
**Reverses if:** never.
