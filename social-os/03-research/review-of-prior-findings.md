# Review of the prior research document

> The operator supplied `nanny-ops-social-agent-findings.md` (dated 2026-09-19,
> produced by a separate Claude Code session) and asked for it to be **challenged,
> not absorbed**. This is that review.
>
> **Verdict: roughly 80% excellent, with one foundational factual error, one
> recommendation that contradicts the operator's own stated constraint, and two
> significant gaps.** Its §7 (swap seam), §8 (nanny ops map) and §9 (child
> imagery) are genuinely first-rate and are adopted wholesale.

---

## Correction 1 — "Cowork cannot be the clock" is **wrong**

**Its claim (§1.3), tagged `[PRIMARY]`:**

> "Cowork / Desktop tasks give you 1-minute precision but **die when the laptop
> sleeps**. Unacceptable for a client's publish schedule."
>
> "**Therefore: Cowork is the brain and the approval surface. It is not the
> publisher.**"

**What actually happened:** it cited `code.claude.com/docs/en/desktop-scheduled-tasks`.
I fetched that page. Its title is **"Schedule recurring tasks in Claude Code
Desktop."** It is about **Claude Code**, not Cowork. Its table row
*"Requires machine on: Yes"* describes a **Claude Code Desktop** task.

**What Anthropic's Cowork documentation says** (support article 13854387,
fetched independently, `[PRIMARY]`):

> "Scheduled tasks run remotely, so they run on their cadence **even when your
> computer is asleep or the Claude Desktop app is closed**."

**Two different products were merged into one claim.** Cowork scheduled tasks
run in Anthropic's cloud with the machine off.

**What survives:** the *conclusion* that you cannot hit 3:07 PM is correct —
Cowork's frequencies are hourly/daily/weekly/weekdays/manual, so hourly is the
floor. But the *reason* was wrong, and the wrong reason drove a real design cost:
the document added an entire **Claude Code cloud routine** as a separate
component to act as the clock. **That component is unnecessary.** Cowork's own
scheduled task is already a cloud clock at hourly granularity.

**Also missed, and it matters:** Cowork scheduled tasks *"can't be tied to a
folder on your computer"* — they run against **connectors** and files in the
Claude account. This independently confirms the Drive-via-connector decision
(DEC-002) and rules out a local-folder design for anything automated.

**Lesson recorded:** a `[PRIMARY]` tag certifies *that a page was fetched*, not
*that the page was about the right product*. Provenance must include the subject,
not just the source.

---

## Correction 2 — recommending Zernio contradicts the operator's own constraint

**Its recommendation (§6):** "Start with Stack 1 (Zernio)."

**Its own words about Zernio (§4.1):** *"a rebrand this recent means the secondary
research about this vendor is untrustworthy across the board"*, plus three
unverified unknowns, plus `[UNVERIFIED]` on whether the free tier even includes
API access.

**What I verified independently:** Zernio was founded in **2025**, is based in
Girona, Spain, has a **team of 8**, is **bootstrapped**, reached ~$1M ARR by
July 2026, and carries a ~4.8 Trustpilot rating. It is real and it is not a scam.
It is also **about one year old**.

**The contradiction:** the document optimised for "cheapest and fastest," which
were the constraints it was given. The operator's constraints have since been
stated explicitly and differently:

> "i need it to be **proven already** something that works, **not invented by you**"
> "best of the best"

A one-year-old, eight-person, bootstrapped vendor holding the publish path for a
**childcare brand's** Meta accounts is not "proven." The asymmetry is what
settles it: saving $149/month against a non-zero chance of a vendor incident on
the account that generates the client's leads — and the account that is the demo
for a ~20-location brand deal. **Wrong trade.**

**Not a knock on Zernio.** It is a reasonable pick for a hobby project or a
price-sensitive v1. It is the wrong pick for *this* buyer's stated bar, and it
should be revisited at scale where the per-account economics genuinely bite.

---

## Correction 3 — `[SECONDARY]` facts presented with `[PRIMARY]` confidence downstream

The document tags diligently in §1–§4, then reasons in §5–§6 as though the tags
were gone. The IG 25-vs-50 cap, the FB 75-day window, and every Ayrshare price
are `[SECONDARY]`, but the stack comparison treats them as settled. The tagging
discipline is excellent; it just has to survive into the conclusions.

**Adopted as a rule:** `CLAUDE.md` rule 2 — a `[SECONDARY]` fact may not become
load-bearing without either verification or an explicit "assuming X" in the design.

---

## Gap 1 — the public-URL problem is noted, then dropped

§10 V1 step 3 correctly notes: *"Instagram requires a publicly accessible URL.
Direct file upload is not supported. Your media pipeline must publish to a CDN or
bucket first — factor that in regardless of which stack you pick."*

Then no stack factors it in. None of the five names who hosts the image.

**This is not a detail — it is a component.** Verified independently: a **Google
Drive share link does not work** as `image_url` (login, redirect, HTML wrapper —
all three are documented failure causes). So "the files live in Google Drive"
does not by itself produce a postable image.

**Resolution:** the image layer must host. Bannerbear returns a hosted public URL
(`https://images.bannerbear.com/...`) as standard API output, which closes this
gap and the branded-image gap with one vendor. See `image-layer.md`.

## Gap 2 — no answer for branded image creation

The document covers **copy** (§3.1) and **AI image/video generation** (§3.2–3.3)
well, but never addresses **on-brand templated graphics** — the actual need.
Canva is not evaluated at all.

AI image generation is the wrong tool here regardless of model quality:
brand-locked layout, exact logo placement and exact typography are precisely what
diffusion models do not guarantee, and §9's own constraint rules out generating
people-shaped content for a childcare brand. A **template-fill API** is the
proven pattern, and it is a mature category. See `image-layer.md`.

---

## Adopted wholesale — the document's best work

| Section | Why it stands |
|---|---|
| **§7 swap seam** | Correct and important. The five-method publisher interface, your own `post_id` as primary key, no vendor payloads upstream, implement `quota()` even where stubbed. Adopted verbatim into `STACK.md`. |
| **§9 child imagery** | The most valuable section in the document. Correct on COPPA, correct that Meta applies child-safety enforcement to AI-generated material identically, and correct that the constraint is *the winning strategy anyway*. Adopted into `RISKS.md` as a hard rule. |
| **§8 nanny ops map** | Excellent domain research and the right answer to "what's the second workflow." Adopted into `nanny-industry.md`. Its §8.2 ranking (never automate screening decisions, never reimplement payroll) is sound. |
| **§8.3 W-2 classification** | Correct and a genuine liability catch. Adopted as a content rule. |
| **§1.1 FB/IG asymmetry** | Correct and underused elsewhere. FB scheduling is free and native; only IG needs a clock. |
| **§10 verification checklist** | The right instinct, well structured. Carried into `OPEN-QUESTIONS.md` with the closed items removed. |

---

## Questions it left open that are now **closed**

| Its open question | Status now |
|---|---|
| **V1** — does Composio's managed Meta OAuth carry publish scope? | **Substantially closed.** Queried the Composio v3 API directly: the managed Instagram config requests `instagram_business_content_publish`; the Facebook config requests `pages_manage_posts` + `business_management`. `[PRIMARY]`. A live publish test remains for 100% certainty — `OQ-001`. |
| **V5** — does a Cowork task fire with the laptop closed? | **Closed — yes.** Anthropic's own Cowork documentation, quoted above. |
| Canva plan gating | **Closed — autofill is Enterprise-only.** Canva's own docs. Rules it out on Pro. |
