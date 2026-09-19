# Publishing layer — who owns the clock

---

## The asymmetry everything hinges on

| | Instagram | Facebook Pages |
|---|---|---|
| Native API scheduling | ❌ **None.** Two-step create-then-publish, both immediate | ✅ `published=false` + `scheduled_publish_time`, 10 min – 75 days |
| Consequence | **Something must be awake at publish time** | **Meta holds it. Zero infrastructure.** |

So the only real question is: **what fires Instagram at the right moment?**

Three answers, and the prior research document's own answer was based on a
product confusion (see `review-of-prior-findings.md` § Correction 1).

## Option A — Cowork's own scheduled task is the clock

**This works, and it was wrongly ruled out.** Anthropic, `[PRIMARY]`:

> "Scheduled tasks run remotely, so they run on their cadence **even when your
> computer is asleep or the Claude Desktop app is closed**."

- Runs in Anthropic's cloud. Machine off is fine.
- Has connectors, skills and plugins available.
- **Cannot be tied to a local folder** — it uses connectors + files in the Claude
  account. Independently confirms the Drive-connector decision.
- **Floor is hourly.** You cannot hit 3:07 PM; you can hit 3:00 PM.

**Verdict: viable.** Schedule on the hour and the limitation vanishes. Costs $0
and adds no vendor. Its weakness is that *you* own retries, failure alerting and
quota handling — there are no webhooks.

## Option B — Composio publishes directly

- `[PRIMARY]` Managed Instagram OAuth requests **`instagram_business_content_publish`**.
- `[PRIMARY]` Managed Facebook OAuth requests **`pages_manage_posts`** + `business_management`.
- Free to 100,000 tool calls/month.
- FB scheduling is native and free; IG needs Option A as its clock.

**This substantially closes the prior document's single biggest unknown.** A
managed OAuth app that requests publish scope it was never granted would be a
broken product. Not absolute proof of a live publish — `OQ-001` — but strong.

**Verdict: cheapest by far, and credible.** Its cost is that you own reliability.

## Option C — a proven publishing vendor

| Vendor | Price | Maturity | MCP |
|---|---|---|---|
| **Ayrshare** | $149 (1 profile) / $299 (10) / $599 (30) | Market veteran; multi-tenant; explicit AI-agent positioning | **Yes** — `https://api.ayrshare.com/mcp` |
| Zernio (ex-Late) | Free at 1–2 accounts | **Founded 2025**, team of 8, bootstrapped, ~$1M ARR | — |
| bundle.social | Free (20 posts/mo) / $100 / $400, **per organization** | Founded 2024 | — |

Ayrshare supports IG posts, **Stories, Reels and carousels**, plus FB Pages.
Customers do **not** do Meta App Review. It does **not** host media — you still
need the public URL, which Bannerbear supplies.

`[SECONDARY]` throughout — **verify prices on ayrshare.com before quoting.**

## Recommendation

**Ayrshare for launch, Composio kept warm behind the seam.**

Reasoning, in the operator's own terms:

1. **"Proven" was stated twice as the bar.** Ayrshare is the market veteran of
   this category. Zernio is one year old and eight people — fine vendor, wrong
   answer to "best of the best" for a childcare brand's lead engine.
2. **It removes the most fragile component entirely.** With Ayrshare, *nobody on
   our side owns the IG clock* — no hourly task, no retry logic, no quota
   surprise, no silent failure. That is the single biggest reliability win
   available, and reliability is the operator's stated requirement
   ("no mess ups").
3. **It has an MCP server.** Cowork connects natively. No code to write, nothing
   to maintain, nothing to break on a vendor's schema change.
4. **The economics invert fast.** $149 for client #1 hurts; $299 for ten clients
   is $30 each, and $599 for thirty is $20 each. With ~20 Lifetime of Love
   markets in play, the portfolio price is what matters — not client #1's.

**Composio still earns its place** as the general connector layer (Drive, and
whatever workflow #2 turns out to be), and as the ready fallback if Ayrshare's
price stops being worth it. That is exactly what the swap seam is for.

**Do not run both publish paths at once.** Two code paths, two failure modes, two
sets of logs, and a real risk of double-posting.
