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
