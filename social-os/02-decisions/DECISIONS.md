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

### DEC-035 — This is a business OS. Social is the first room, not the product.
**Date:** 2026-09-21 · **Status:** ✅ locked · **reframes DEC-025**
**Decision:** The plugin is renamed `social-os` → **`business-os`**. It is a small
business's whole AI workspace, operated from chat, with social media as room one and
email, reviews, recruiting and invoicing as rooms added later. Room definitions live
in `rooms/` as **data** — a definition file, folders, and one or two skills — because
the laws, the map, onboarding, correction, housekeeping and upgrades already apply to
every room.
**Why:** the operator's read was right, and the artifacts already proved it —
`the-law.md`, `the-map.md`, `drive-conventions.md`, `growth-and-upkeep.md`,
`project-instructions.md` and `update-the-brain` **do not mention social media**.
Only 5 of 9 skills are social-specific. The substrate was already general and merely
packaged as though it were a social tool. Zero clients are installed, which makes
this the cheapest it will ever be.
**The GitHub repo keeps its name** (`bucho11/social-os`). Renaming it is
outward-facing and reversible later via GitHub's automatic redirects; the marketplace
works regardless of what the plugin inside is called. Operator's call, not ours.
**Reverses if:** never.

### DEC-036 — One plugin, many rooms. Not a core plugin plus room plugins.
**Date:** 2026-09-21 · **Status:** ✅ locked · **forced by a verified constraint**
**Decision:** Everything ships as a single plugin. Rooms are folders and skills
inside it, not separate installable plugins.
**Why:** `[PRIMARY]` — *"Claude Code doesn't let a plugin reference files outside its
own directory. It rejects a component path that resolves outside the plugin root."*
A separate `social` plugin could not read the core's laws. There is a documented
symlink exception, but it is **Claude Code** documentation and unverified on Cowork,
and this repo has already shipped one silent path-resolution bug (DEC-024) where
every skill ran without its guardrails and nothing errored. Betting the architecture
on an unverified substitution mechanism repeats that exact mistake.
**It is also the better answer on its own merits.** Splitting the laws from the rooms
would put one job in two places — our own Law 1, violated at the code level. And one
plugin means one version, one changelog, one Update click.
**Cost, stated:** only skill *descriptions* are always in context (~700 chars each,
9 skills ≈ 6 KB). Each future room adds ~600 chars. Revisit at roughly twenty skills.
**Reverses if:** Cowork's symlink dereferencing is verified AND the description
budget becomes the binding constraint. Both, not either.

### DEC-037 — Clients float to latest; every release is a PR with a version bump
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** Clients are not pinned. Every release goes through a pull request that
bumps `version` in `plugin.json` (kept equal in the marketplace entry) and adds a
`CHANGELOG.md` entry in Keep a Changelog format. Additive by default (MINOR).
Breaking changes are MAJOR and require the expand/migrate/contract ceremony. The
operator's own workspace is the canary — every release runs there first.
**Why:** the operator's bar was *"future plugins can happen within a week and I want
my clients to be aware of them... no ruckus, super simple, 10/10 value for the user,
always."* A pinned client must be told to do something before receiving work already
done for them — friction both ways, and a shipped fix helping nobody.
**Floating is only safe because of everything else**: additive by default, breaking
changes get the ceremony, migrations show a diff before touching anything, and
nothing is ever deleted. **Make "latest" safe, then let everyone have it**, rather
than making everyone opt in to safety.
**The PR-with-bump is not ceremony — it is the mechanism.** `[PRIMARY]`: sync fires
*"when a pull request that includes a plugin version bump is merged"* and *"direct
pushes to the default branch don't trigger a sync."* We had been pushing straight to
`main` at a frozen `0.1.0` — the configuration least likely to reach anyone.
**Reverses if:** a release ever reaches a client in a broken state. Then clients pin
and the operator promotes deliberately.

### DEC-038 — Two lanes for change: reconcile silently, migrate with a visible diff
**Date:** 2026-09-21 · **Status:** ✅ locked · **the answer to "how do we not cause chaos"**
**Decision:** Workspace change splits by kind, not by size.
**Lane 1 — reconcile.** Purely additive: a missing folder, a rule document she has
never had, a stale ID. Runs **silently, continuously, no permission**. This is not
changing her stuff; it is the system finishing building itself. (Kubernetes' control
loop: observe actual state, move toward desired state, forever.)
**Lane 2 — migrate.** Anything that renames, moves, merges or retires. **Plans
first, shows her the exact diff, applies on one yes.** (Terraform's `plan`/`apply`,
and its own stated reason: a visible diff exists *"because infrastructure changes are
risky and often destructive; operators need to know exactly what will be created,
changed, or destroyed before committing."*)
**Why this rather than the three options put to the operator:** auto-migrate breaks
the never-rearrange-without-a-yes stance we had just committed to; ask-every-time
turns creating a missing folder into a permission dialog, and noise is how people
stop reading what you say; never-touch guarantees divergence. The kind of change is
the right discriminator, and it is the one the industry uses.
**Putting a change in the wrong lane is the only real risk here**, which is why each
migration declares its lane and a migration that does both is split in two.
**Reverses if:** never.

### DEC-039 — Never a breaking change in one step; a workspace carries its own version
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** Two version numbers, never conflated: the **plugin version** (semver,
in git) and the **workspace version** (an integer, in her `0 — Map`). Shape changes
ship as **expand → migrate → contract**, three separate releases minimum. Every
migration step is idempotent and states how to tell whether it already ran. The map
carries an upgrade history, and a half-applied upgrade is recorded **`FAILED`**.
**Why:** we have no fleet orchestration — a workspace is reachable only when a
session runs against it — so a client who doesn't open Cowork for six weeks **is** a
client on an old shape. Research is unambiguous: additive changes are the only ones
safe while older instances are still running, and *"a single migration that adds and
removes in one shot is unsafe."* The governing rule we adopted verbatim: **"make
readers tolerant before making writers strict."**
**We took Flyway's failure behaviour, not Rails'.** Flyway writes an explicit failed
entry; Rails and Django leave the migration reading as *pending* while *"partial side
effects can remain."* A half-applied change that looks like it never started is
exactly the chaotic state the operator asked us to prevent — worse than an old shape,
because nothing about the folder looks wrong.
**Reverses if:** never.

### DEC-040 — Nothing is destroyed: supersede, never trash
**Date:** 2026-09-21 · **Status:** ✅ locked · **Law 6 · fixes DEC-020**
**Decision:** Replacing a rule document creates the new version and **supersedes**
the old one — renamed `<title> — superseded YYYY-MM-DD`, moved to `9 — Archive/`.
`trash_file` is reserved for something created by mistake seconds ago that nothing
has referenced. Retired document roles and room numbers are recorded in `0 — Map`
under `## Retired` and **never reused**.
**Why:** `[PRIMARY]`, Google's own docs — *"Files you move to the Trash are deleted
forever after 30 days."* Every correction was starting a 30-day timer on the record
of what her brand voice used to be, with nothing warning anyone on day 31. For a
system whose whole premise is *"correct me freely, thousands of times,"* **the cost
of being wrong must be zero**, and it wasn't.
Records management has held this line for decades: a superseded version is marked
superseded and retained; a correction preserves the original and adds to it rather
than overwriting the evidence. Same number of calls as trashing.
**Never reusing a name** is Protobuf's rule about field numbers, for the same reason:
her notes, an old report and an archived document all still point at "room 4," and
reassigning it makes every one of them quietly wrong with nothing to notice.
**Reverses if:** never.

### DEC-041 — Resolve duplicates point by point, never by picking a winner
**Date:** 2026-09-21 · **Status:** ✅ locked · **corrects DEC-027's resolution step**
**Decision:** When two documents hold one job, reconcile **attribute by attribute**:
keep what only one of them says, and ask only about the places they genuinely
disagree — usually one or two. One reconciled document survives; the other is
superseded.
**Why:** master data management is explicit that *"good practice is to treat
survivorship at the attribute level, not as a whole-record winner-takes-all
decision."* Our original rule — *"she decides which survives, the other is trashed"*
— was exactly the named anti-pattern. Two documents exist **because both got
written**; each holds something the other doesn't. Picking one whole silently
discards work she did, and she discovers it a month later as *"I already told you"*
— the most serious signal in the system, produced by the system's own repair step.
**Reverses if:** never.

### DEC-042 — A change and a correction have different blast radii
**Date:** 2026-09-21 · **Status:** ✅ locked · **Law 4 · corrects the blast-radius table**
**Decision:** When a **fact** changes, ask one line: *"did that change, or was it
always wrong?"* A **new fact** leaves already-published work historically correct —
leave it alone. A **correction of a past belief** makes that work false — surface it
immediately and let her decide whether to take it down.
**Why:** bitemporal modeling exists for precisely this, separating *when a fact was
true* from *when we came to believe it*: *"update as new fact"* versus *"correction
of past belief."* We collapsed them — both rewrote the document and logged one line —
and the blast-radius table said published claims *"now false"* should be flagged,
which is right for one case and wrong for the other.
**The cost of each error is real and opposite:** treating a price rise as a
correction scrubs honest history off her feed, losing the engagement and links on
those posts; treating a correction as a rise leaves a false pricing or credential
claim standing. Three words from her settles it.
**Reverses if:** never.

### DEC-043 — Validate the plugin before every release
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** `tools/validate.py` runs before every release and gates it. It checks
that every `${CLAUDE_PLUGIN_ROOT}` reference resolves, no relative path escapes its
skill directory, skill names match their directories, descriptions are within 1024
characters, `plugin.json` and the marketplace entry agree on name and version,
every migration is both listed and written and states how to tell if it already ran,
and the CHANGELOG has an entry for the version being shipped.
**Why:** this repo has already shipped two bugs of exactly this class — 22 file
references that escaped their skill directory (DEC-024) and a reference containing a
space that cannot be parsed unambiguously. **Both were silent at runtime**: the skill
runs, just without its guardrails, and nothing errors. A discipline that depends on
files being read is a discipline that needs a machine to confirm the files are
reachable.
**It earned itself on its first run**, catching the space-in-path reference and a
missing changelog entry.
**Reverses if:** never. Extend it whenever a new silent-failure class appears.

### DEC-044 — A proof layer: checks that can fail, before the work reaches her
**Date:** 2026-09-21 · **Status:** ✅ locked · **the largest gap this project has had**
**Decision:** Every job runs checks producing **external evidence** — a claim found
verbatim in a named document, a file that exists, a URL that resolves, a count — and
the result is written into the work itself as an evidence report, never only into the
conversation. 34 checks across the five social jobs. **"If a check cannot fail, it is
not a check."** A check that could not run reports `SKIP` and is surfaced; it is
**never** reported as a pass.
**Why:** we had exactly **one** real check in the whole system (`validate_media`).
Everything else was judgment — `compliance-reviewer` reads a draft and opines, which
is worth having and is not proof. The consequence was that **the owner was the
quality control**: every draft she opened, she was proofreading for a missing release
and a price that changed. That is the most expensive possible use of the one person
this system exists to protect, and it degrades — proofreading the tenth draft is not
proofreading the first.
**The report lists every check including the passes**, because a report showing only
problems cannot be told apart from one where the checks never ran. And it carries
**evidence, not verdicts** — `"$30/hour" found in What we offer, line 12`, not
`pricing ok` — so it is auditable by someone who does not trust the checker.
**Reverses if:** never. Extend it; the generator for new checks is escapes, not
imagination.

### DEC-045 — Three severity tiers, declared per check — not one gate/annotate policy
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** **blocking** (work cannot move to Approved; she may override in words,
and the override is recorded with her reason and the date) · **needs-a-look**
(surfaced with the evidence; one word approves anyway) · **informational** (recorded,
not surfaced). Blocking is a deliberately short list — for this brand, a child's face
with no release on file and a claim not written in `What we offer`, checked in the
caption, the first comment, **and text baked into a graphic**.
**Why:** one global policy is the wrong shape; CI systems have had error/warning/info
for thirty years. A missing photo release and a caption three words over are not the
same event, and treating them alike either blocks her over nothing or lets through
the thing that ends an account. **Every check promoted to blocking buys safety with
her Friday evening**, so promotion needs a reason each time.
**The override is recorded because an override is a decision**, and decisions are
recorded (Law 2). It is also the signal that a brain document is out of date — she
approving a price the document does not know is exactly when `What we offer` should
be updated.
**Reverses if:** never.

### DEC-046 — Playbooks are shipped or interviewed, and an upgrade may never rewrite an interviewed one
**Date:** 2026-09-21 · **Status:** ✅ locked · **refines DEC-032's tier line**
**Decision:** Every job declares its origin. **Shipped** — we wrote the process, it
lives in the plugin, a release improves it for every client at once. **Interviewed** —
extracted from her by `business-os:teach-it-a-job`, lives in her Drive, listed in
`0 — Map`, and **no upgrade may rewrite it**; an upgrade may only propose, with a
diff, like any other Lane 2 change.
**Why:** writing someone's process for them fails in a way that is hard to catch —
what you wrote is plausible, so it survives review, and it is only wrong in the
specifics that made it theirs. Social stays shipped because we genuinely know the
domain and a client who had to teach us that got a worse deal. Her invoicing sequence
is not ours to invent.
**The correction this forces:** DEC-032 said *"no behaviour rules go in her Drive."*
That was never true — `Rules for the AI` is a behaviour rule and has always lived
there. The real line: **how the *system* behaves is the plugin's; how *her work* is
done is hers.** Her processes are her work. Restated in `playbooks.md` and the
bootstrap.
**Reverses if:** never. The interaction with DEC-039 is load-bearing — a migration
that overwrites an interviewed playbook destroys something no release can restore.

### DEC-047 — The toolbox fills from rebuilt work; examples carry their reason
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** **Toolbox** — the signal is *anything rebuilt from scratch that existed
before*. When you notice it while working, write it into the room's `Templates/` with
placeholders, index it, use it from then on. **Examples** — `learn` saves each week's
top performer to the room's `Examples/` with two or three lines on **why** it worked.
Best ten per room, not the newest ten; the eleventh supersedes the weakest to Archive.
**Why:** we learned from post *performance* and never from the agent **redoing work
it had already done**. If the screening paragraph is rewritten monthly, that is a
template nobody noticed. The agent is the only party who can see it, because it is
the one rebuilding it — so the check is "did I just rebuild something?", watched
while working rather than on a schedule.
**Examples carry their reason or they are worthless** — the source's own tell is
*"the update the client replied to."* An example with no reason is an old post.
Quality-selected, not recent, and `learn` already identifies top performers weekly,
so the selector already existed.
**Examples are records (Law 2):** they inform drafting and never override
`Brand voice`. A disagreement between an example and the voice document is resolved
by the document, and is worth raising with her.
**Reverses if:** never.

### DEC-048 — Diagnosis names the layer, and every escape earns a check
**Date:** 2026-09-21 · **Status:** ✅ locked · **extends DEC-031**
**Decision:** Before finding the document, name the layer: **process** (a step was
missed) · **toolbox** (something was rebuilt that existed) · **proof** (it reached her
and nothing caught it) · **context** (the steps ran correctly and the brain document
was wrong). `History` entries record the layer, and `housekeeping` mines them monthly
— the same layer failing the same way three times is **one missing mechanism**, not
three corrections.
**Why:** the source's three-layer diagnosis is sharper than "which document", and
`proof` is a diagnosis we previously could not even express, because we had no
checks. **The proof row is the one that compounds and the one most often skipped**,
because fixing the output feels like fixing the problem — it is not, and the same
escape returns every month until a check exists. *An escape that produces a check
cannot happen twice; an escape that produces an apology happens forever.*
**The fourth layer is ours, and it is why this is a merge rather than an adoption.**
Their model assumes a job's knowledge lives in its playbook. Here one `Brand voice`
serves every room, which is an advantage and which creates a failure their taxonomy
cannot name: everything ran correctly and the output was still wrong, because the
shared document was wrong.
**Reverses if:** never.

### DEC-049 — Checks fix what they can and re-run before she sees anything
**Date:** 2026-09-21 · **Status:** ✅ locked · **hardens DEC-044**
**Decision:** The run is: run every check → **fix what fails** → **run them again** →
report one line per check with evidence, including the passes and the fixes → list
what could not be verified and why. Surface only what genuinely cannot be resolved —
a blocking failure, a judgement call, a fact the brain does not know. Fixes appear in
the report as `FIXED` with the before and after value.
**Why:** v0.4.0 ran the checks and handed her the failures, which is the lazy half.
Nine hashtags when the rule is three to five is not news for her; it is something to
correct and re-check. **A proof layer that only reports is a complaints department**,
and she will start skimming it, which is the same as not having it. The re-run is not
optional either: a fix nobody re-checked is a fix nobody verified, and unverified
work is the problem this layer exists to solve.
**Recording the fixes matters as much as making them.** A layer whose work is
invisible is the first thing removed when someone asks what it is for.
**Reverses if:** never.

### DEC-050 — More than two failures on the first pass stops the run
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** Three or more checks failing on the first pass is **not a bad output,
it is a broken process.** Stop, and name the part of the process that caused it — a
brain document that is wrong so every downstream check fails together, a step that
ran out of order, a stale template, a missing input. Do not patch them individually.
**Why:** patching three failures one at a time produces work that passes on a process
that will produce three failures again tomorrow. It is the same instinct as
`housekeeping`'s monthly review — *a failure repeating is one missing mechanism, not
many corrections* — applied **inside a single run, where it is cheapest and the
evidence is still in front of you.**
**The threshold is deliberately low.** Two is noise; three is a pattern, and waiting
for more costs a wasted run and teaches everyone that the checks are just friction.
**Reverses if:** never.

### DEC-051 — The second occurrence earns a rule, not a reminder
**Date:** 2026-09-21 · **Status:** ✅ locked · **sharpens DEC-048's cadence**
**Decision:** Once is a correction. **Twice is a missing mechanism**, and the fix
must be something that *prevents* it: a check that fails when it happens, a decision
rule written `if X then Y`, a template that makes the wrong version harder to produce
than the right one, or a document rewritten so the wrong reading is no longer
available — **never a caveat added beneath the wrong reading.**
**Why:** a note saying *"remember to keep hashtags between three and five"* is what
an apology looks like once it has been written down. It reads as a fix, it enforces
nothing, and the same thing happens a third time. We already had the monthly
three-strikes review in `housekeeping`; this moves the trigger to **two, in the
moment**, and `housekeeping`'s third strike becomes a backstop that also reports a
correction handled shallowly.
**Reverses if:** never.

### DEC-052 — The interview has two hard gates and closes with two questions
**Date:** 2026-09-21 · **Status:** ✅ locked · **hardens DEC-046**
**Decision:** No playbook is written until **at least eight questions have been
asked AND she has said you're done.** It then prints the whole playbook and asks two
questions, **separately, waiting between them**: *what did I get wrong?* and *what
did you forget to tell me?* Decisions are written `if X then Y`, not as prose.
**Why:** eight *topics* is not eight *questions* — three compound questions touch all
eight and return a summary of her process rather than her process. And an interview
that ends when the interviewer feels satisfied ends early every time, because the
thing you don't know about is the thing you don't know to ask about.
**The second closing question is the one that earns the interview.** The first
catches errors you made; the second catches knowledge so obvious to her it never
registered as a step — which is where a job's real difficulty usually lives, and
which no question asked during the interview could have surfaced, because neither
party knew it was missing. Rolled into *"anything to add?"* they get one answer, and
it is about the first.
**Reverses if:** never.

### DEC-053 — Toolbox hygiene: names, examples, exclusions, and an active rebuild test
**Date:** 2026-09-21 · **Status:** ✅ locked · **hardens DEC-047**
**Decision:** A template filename **says what the file is and nothing else** — no
dates, no version numbers. Placeholders are bracketed, with **one filled-in example
underneath**. The playbook step points at it by name and says **when not to use it**.
Never saved: one-off outputs, anything holding a password or key, and a draft she has
not approved. And rebuild detection gets an **active** test beside the passive one:
run the job again from scratch and say which saved files were used and which parts
were built from nothing.
**Why:** a date or version in a filename creates a second file doing the same job the
moment it is updated — **Law 1, broken by a naming habit.** Replace the file; the
archive keeps the old one (Law 6). A slot name alone never quite says what belongs in
it, so the example carries what the name cannot. A template applied in the wrong
place is worse than none because it looks considered. An unapproved draft saved as a
template makes a guess into a standard, quietly, and every future output inherits it.
**The active test matters most:** passive noticing depends on attention, and attention
is exactly what fails on the fortieth run.
**Reverses if:** never.

### DEC-054 — Never report work that did not happen
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** If a write fails, say so, print what would have been written, and name
exactly where it belongs. Never report a save that did not happen, and never report a
check that errored as one that passed.
**Why:** the two are the same failure — **silence read as success** — and it is the
quietest way any of this rots. A claimed save that did not happen is worse than an
admitted failure, because an admitted one gets retried and a claimed one is never
looked for again. This was already the rule for checks (DEC-044); it now covers
writes, which is where it is more likely to bite, because a Drive write failing
mid-session is an ordinary event.
**Reverses if:** never.

### DEC-055 — "Did a person write this" is a check, not a style preference
**Date:** 2026-09-21 · **Status:** ✅ locked · **extends DEC-044**
**Decision:** Seven checks (11–17) run on every draft for the signs of machine
writing, plus a `sounds-human` skill for when the *shape* is the problem rather than
the words. None block — style is not what blocking is for.
**Why:** all 34 existing checks asked *is this true?* None asked the question a reader
actually asks first, in about a second and a half. **For a childcare brand those are
the same question:** a parent choosing who watches their kid is making a trust
decision, and copy that reads as machine-generated leaks trust in the one market where
trust is the entire product. A caregiver deciding where to apply reads it identically.
**Two layers, because one does not reach the other.** Surface (words, punctuation,
cadence) is cheap, mechanical, and **decaying as a signal** as vendors tune it away.
Structure (where the lesson sits, how emotion is rendered, what gets named, whether
the skeleton repeats) is where the durable fingerprint lives.
**Verified, not taken on trust:** Russell et al. 2026 (arXiv:2604.03136) classified
61,608 stories on discourse features alone, with every style feature withheld, at
**93.2% macro-F1** — checked against the paper's own abstract, along with the 68.4%
six-way attribution figure and the corpus size. Professional span-level surface
rewriting of AI text moved detection **1.6 points**. A caption can pass every
word-level check and still read as machine-written, and that is the normal case.
**Reverses if:** never, though the surface half will need re-derivation as models
change. The structural half is the durable investment.

### DEC-056 — One or two moves per piece. A uniformly applied checklist is a new fingerprint.
**Date:** 2026-09-21 · **Status:** ✅ locked · **outranks DEC-055's audits**
**Decision:** Never apply the full intervention menu. One or two deliberate structural
moves per piece, varied across pieces, each one justifiable in a line.
**Why:** the research's deepest finding is **convergence** — five models occupy one
tight region of structural space while human writing is dispersed; 24.7% of human
stories fall in the corpus's rarest 10% against 7.1% of AI stories. **Rarity is the
human signal.** Which means a de-slopping checklist applied uniformly does not remove
a fingerprint, it replaces one with ours — and four posts that all open mid-scene and
end unresolved read exactly as machine-made to anyone reading them in sequence.
**This is the rule most likely to be broken while following every other one**, because
each individual fix looks correct. It is stated in three places on purpose.
**Reverses if:** never.

### DEC-057 — Voice is the input and the final guard, not a coat of paint
**Date:** 2026-09-21 · **Status:** ✅ locked
**Decision:** The order is **draft in her voice → surface pass → structural pass →
re-check against her voice.** `Brand voice` and the room's `Examples/` explicitly
**outrank** every de-slop check: if removing a tell costs her voice, the tell stays
and the reason is stated so she can overrule.
**Why:** the published pipeline for this work puts a voice layer *last, as something
additive*. That assumes a generic draft being cleaned and then voiced. Ours is voiced
from the start — `draft-post` writes *from* `Brand voice` — so running de-slop passes
over it risks the opposite failure, and it has a name: **copy that passes every check
and says nothing has not been de-slopped, it has been sanded.**
**The asymmetry is what settles it.** An em dash left in is a five-second fix. A
voiceless caption is a rewrite, and worse, it is the failure nobody notices because
everything passed.
**Reverses if:** never.

### DEC-058 — Do not vendor the CC BY-SA lineage; write our own and credit it
**Date:** 2026-09-21 · **Status:** ✅ locked · **commercial, not academic**
**Decision:** The general-purpose `humanizer` skill from the upstream stack is **not
vendored.** Our surface checks are written for this system, in our own check format,
scoped to short childcare social copy. `ATTRIBUTION.md` credits every lineage, and
`LICENSE` (MIT) is added — the repo previously had none, which is a real gap for
something being resold.
**Why:** that skill's pattern catalogue traces to Wikipedia's *Signs of AI writing*,
**CC BY-SA 4.0 — a share-alike license**, and the upstream repository says plainly
that redistribution should carry the obligation and that relicensing needs a legal
read. This plugin is built to be deployed to paying clients across ~20 franchises.
**Inheriting a share-alike obligation on a core file is a question better avoided than
answered.**
The individual observations — that models overuse em dashes, that "not just X, it's Y"
is a tell — are facts about how language models write, and facts are not
copyrightable; a particular selection and arrangement of them can be, which is exactly
why we made our own selection for a different purpose. Wikipedia is credited anyway,
because someone did the work of noticing.
**Stated as our reading, not as legal advice**, with a recommendation to get a real one
if it matters commercially.
**Reverses if:** a legal read says otherwise, in which case vendoring saves us nothing
we care about anyway.

### DEC-059 — Read for the shape, not the string; and scope the em dash check to captions
**Date:** 2026-09-21 · **Status:** ✅ locked · **both findings measured, not assumed**
**Decision:** Check 11 reads for the antithesis **shape** and names the contracted
forms explicitly. Check 13 (em dashes) applies to captions only, never to internal
documents.
**Why, measured:** we ran the upstream scanner against five realistic variants of the
antithesis tell and **it caught two.** The pattern anchors on the literal string
`not just`, which cannot match `isn't just` — the letters *n-o-t* do not occur in that
word — so the contracted forms, which are the common ones in social copy, pass clean.
Its closer alternation accepts only `it's` or `but`, so *"That's not just a nanny,
that's a partner"* also passes. **A regex over a contraction-heavy genre is the wrong
tool**, and a model reading for the shape is the right one.
**And:** scanning our own client-facing seed documents returned **13 em dash hits,
every one a folder name** (`1 — Brain`, `3 — Social`). Our workspace's entire naming
convention is built on the character the check flags. The upstream README warns that
applying it to internal docs will fire constantly; we confirmed it empirically rather
than trusting either direction.
**Both are recorded in `ATTRIBUTION.md`** so the upstream author can have them if he
wants them.
**Reverses if:** never.


### DEC-060 — Ship the scanner; a script is an accelerator, never a dependency
**Date:** 2026-09-21 · **Status:** ✅ locked · **corrects DEC-055's reasoning**
**Decision:** `skills/draft-post/scripts/caption_scan.py` ships. Every scripted check
is **written twice** — once as the script, once as the pattern list in the skill's
`checks.md` — and if the script does not run, those checks report
`SKIP — read manually` and are surfaced. Never a pass. `tools/validate.py` now
compiles every bundled script and runs it on a trivial input, because a script that
errors on import is a check that silently never runs.
**Why this reverses last release's call:** we declined to ship a scanner on the
grounds that *"one that silently never runs is worse than none — it reads as
coverage."* **That risk was already eliminated by our own proof contract** (DEC-044):
a check that could not run reports SKIP and is surfaced. So the failure mode we were
protecting against could not occur, and the honest consequence is that the scanner
should have shipped. Worst case it degrades to the model reading the same list, and
announces that it did.
**Why it matters beyond this one file:** a script does not drift, does not get tired
on the fortieth caption, and does not quietly decide a borderline case is fine. Model
judgement is the thing this whole proof layer exists to stop relying on, so making
any slice of it deterministic is a real gain — and the two-places rule means the gain
costs nothing when the script is unavailable.
**Measured:** catches **5 of 5** realistic variants of the antithesis tell where the
upstream scanner catches 2, and returns clean on human-written copy.
**Reverses if:** never. Extend the pattern — where a check *can* be deterministic, it
should be.

### DEC-061 — Read what she already has before asking her to describe it
**Date:** 2026-09-21 · **Status:** ✅ locked · **corrects a claim in four documents**
**Decision:** Onboarding calls `list-brand-kits` and `search-brand-templates` **before**
interviewing her about how her brand looks, and `make-graphic` instantiates her own
Brand Templates in preference to generating new designs. `Colors and fonts` **mirrors**
her Brand Kit and adds what a Brand Kit cannot hold — when each colour is used, what
the logo must never sit on, her photo style — rather than substituting for it.
**The correction:** four documents said her Brand Kit was an Enterprise feature and
therefore out of reach. It is not. `[PRIMARY]`, already in `VERIFIED-FACTS.md`:
Pro+ gives `resize-design`, `search-brand-templates`, `list-brand-kits` and
`create-design-from-brand-template`; **Enterprise-only is `autofill-design` and
`get-brand-template-dataset`.** Autofill is a different feature and we never needed
it — the edit loop replaces text on any plan.
**This is the second time the same over-generalisation has surfaced.** DEC-018
corrected "Canva is out", which came from reading *autofill is Enterprise* as *Canva
is Enterprise*. The decision was fixed; the prose in four other files was not, and it
survived six releases. The file that had done the actual verification —
`canva-cheatsheet.md` — was right the whole time. **A correction that updates the
decision log and not the prose has not landed** (Law 5 — blast radius), and this is
that failure, found by the operator asking a question rather than by any check.
**Why it matters beyond accuracy:** a client with an existing Brand Kit and four
templates has already done the work this interview was about to ask her to redo. Using
what she built is better data, zero effort for her, and the fastest trust available on
a setup call. Most of the look-and-feel interview exists only because a client has
nothing.
**Reverses if:** never.
