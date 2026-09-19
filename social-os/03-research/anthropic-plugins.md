# Anthropic's own plugins — what already exists

> `[PRIMARY]` — read from the live claude.ai plugin catalog and from
> `github.com/anthropics/knowledge-work-plugins` source, 2026-09-19.
> **This changes the product strategy. Read before building any skill.**

---

## The two that matter

### `marketing` — by Anthropic
8 skills: `brand-review` · `campaign-plan` · `competitive-brief` ·
`content-creation` · `draft-content` · `email-sequence` · `performance-report` ·
`seo-audit`
13 MCP servers: ahrefs · amplitude · **canva** · figma · gmail · google calendar ·
hubspot · klaviyo · notion · similarweb · slack · supermetrics

### `small-business` — by Anthropic — **the big one**
**43 skills**, ~34 MCP servers. Directly relevant:
`social-content-engine` · `content-strategy` · `brand-style` · `canva-creator` ·
`smb-onboard` · `smb-router` · `lead-triage` · `speed-to-lead` ·
`review-reputation` · `marketing-monday` · `business-pulse` · `hiring-screener` ·
`job-post-builder` · `outreach-composer` · `crm-autopilot`

Connectors include **google-drive**, canva, shopify, hubspot, slack, gmail,
stripe, square, **tiktok**, zapier, notion.

Also relevant: `brand-voice` (Tribe AI) — brand discovery + enforcement, with
sub-agents.

**None of these are enabled on the operator's account yet** (`enabled: false`).

---

## What Anthropic already built that overlaps our plan

| Our planned piece | Anthropic's equivalent | Overlap |
|---|---|---|
| `brand-onboarding` skill | **`smb-onboard`** — 7-question interview, one at a time, stores to memory | **High** |
| Brand voice file | **`shared/voice-profile.md`** — one file every writing skill reads | **High** |
| `plan-week` | `social-content-engine` — holds a rolling calendar between sessions | **High** |
| `draft-post` | `social-content-engine` + `draft-content` | **High** |
| `make-image` | `canva-creator` / Canva autofill | Partial — **see gap 2** |
| `publish` | ❌ **nothing** | **None — see gap 1** |
| `weekly-report` | `performance-report`, `business-pulse`, `marketing-monday` | Medium |

`smb-onboard` step 5, verbatim: *"Write the block to the **Cowork session memory
directory** under the heading `## Business context`."*

`shared/voice-profile.md`, verbatim: *"Every skill that writes in the owner's
name reads the same file, so a correction the owner makes once holds
everywhere."* — **this is the AIOS declared-context pattern, already shipped.**

---

## The three verified gaps

### Gap 1 — **Neither plugin can publish to Instagram or Facebook**
Full connector lists checked. `small-business` has **tiktok** and nothing else
social. `marketing` has no social publishing connector at all.
`social-content-engine` *"stages posts for approval instead of publishing on its
own"* — and then there is no IG/FB path to publish through.
**➡️ The publishing layer (Ayrshare / Composio) is still required. DEC-005 stands.**

### Gap 2 — **Their Canva path is semi-manual on Pro**
Anthropic's own `social-content-engine/reference/canva-api.md` carries this table:

| Feature | Free | Pro | Teams | Enterprise |
|---|---|---|---|---|
| Brand templates (read) | — | — | — | ✓ |
| Autofill brand templates | — | — | — | ✓ |

And verbatim: *"Pro/Teams asset generation is **semi-manual**: Claude creates the
design shell and…"*

**This independently confirms DEC-006.** Anthropic hit the same Canva Enterprise
wall and accepted a semi-manual fallback. Every client here is on **Pro**.
**➡️ Bannerbear remains the answer — fully automatic on Pro, and it hosts the
public URL Instagram requires.**

### Gap 3 — **Their memory is thin, opaque, and not the client's**
What `smb-onboard` stores is **one `## Business context` block** plus a voice
profile, written to **Cowork session memory**. `[SECONDARY]`: Claude Projects
carry per-project memory.

What it is not:
- Not files the client owns or can port
- Not readable or editable by her outside Claude
- Not versioned, not auditable, no history of what changed and why
- No declared-vs-observed separation
- **No performance → strategy loop.** It is a snapshot, not a compounding corpus.

**➡️ This is the real product surface. Not "a folder" — a brain with depth,
ownership and a learning loop.**

---

## Strategy change: build ON it, not against it

**Do not rebuild what Anthropic ships free and maintains.** Rewriting
`smb-onboard` or a generic calendar skill is wasted work that gets worse over
time as they improve theirs.

**Revised shape:**

```
Anthropic small-business plugin   ← generic capability. free. Anthropic maintains it.
              +
Publishing layer (Ayrshare MCP)   ← gap 1. they have no IG/FB.
Image layer (Bannerbear MCP)      ← gap 2. their Pro path is semi-manual.
              +
THE BRAIN (Drive, AIOS-shaped)    ← gap 3. the actual product.
 + childcare/nanny domain rules   ← what a generic plugin will never have
```

Our skills shrink to what is genuinely ours: the **deep onboarding** that fills
the brain, the **publish** skill that holds the swap seam, the **learning loop**
that writes `What works.md`, and the **domain guardrails** (child imagery, W-2
classification, banned claims).

## Honest note on defensibility

A folder structure is not a moat — Anthropic could ship one. What is defensible:
**encoded domain expertise** (childcare compliance, two-sided marketplace,
nanny agency ops), **the managed service**, and **the relationship**. Price and
position on those, not on the folder.
