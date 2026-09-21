# Client setup runbook

Everything the operator does to take a new client from nothing to a live system.
**~45 minutes**, most of it her talking during the interview.

Do it **live with her on a call** the first time. After that it is repeatable, and
the interview is the only part that needs her.

---

## Before the call — operator, 10 minutes, once per client

| # | Do | Why |
|---|---|---|
| 1 | Confirm her **Instagram is Business or Creator** | Personal accounts connect and then fail every publish. Instagram app → Settings → Account type and tools → Switch to professional → **Creator**. Free, 30 seconds, reversible. |
| 2 | Confirm she has a **Facebook Page** she admins | Personal profiles cannot post via API. |
| 3 | Confirm she has **Claude Pro** (or Max) | Cowork and plugins are paid-plan only. |
| 4 | Confirm she has **Canva Pro** | Free loses `resize-design`, which is the whole multi-size win. |
| 5 | Decide **who owns the Drive folder** | Her Google account, operator as Editor (DEC-007). Never an employer domain (DEC-013). |
| 6 | Create her **Zernio profile** if pre-staging | Or let `brand-onboarding` do it. Profiles are free and unlimited. |

**Accounts 1 and 2 across your whole Zernio team are free.** Client #1 costs $0;
you only start paying at account 3.

---

## On the call — with her, ~35 minutes

### 1 · Install the plugin (2 min)
**Customize → Plugins → Personal plugins → "+" → Add marketplace → Add from a
repository** → paste the marketplace repo URL → install **Social OS**.

### 2 · Connect three things (5 min)
**Customize → Connectors**, or when prompted:
1. **Google Drive** — her account
2. **Canva** — her Canva **Pro** login
3. **Zernio** — browser sign-in, no key to paste

### 3 · Run the interview (~30 min)
She says: **"set me up"**

`brand-onboarding` then: researches her site and Instagram, interviews her in eight
phases, builds the Drive folder and every brain document, creates her Zernio profile,
hands her the Instagram and Facebook connect links, verifies `canPost: true` on both,
and drafts three real posts.

**Do not let it claim success without the health check passing.** If an account reads
`canPost: false`, fix it on the call — that is almost always the Instagram account
type.

### 4 · Set two scheduled tasks (2 min — she must do this)
Plugins cannot create scheduled tasks; the owner does, once, in Cowork.

| Name | When | Prompt |
|---|---|---|
| **Weekly content plan** | Weekly, Sunday evening | `Run social-os:plan-week for next week, then social-os:draft-post for every planned row, stage them as drafts, and tell me what's waiting for approval and what I need to film or upload.` |
| **Weekly results** | Weekly, Monday morning | `Run social-os:learn for last week. Lead with anything that needs me.` |

### 5 · Approve one post together (5 min)
Pick the best of the three drafts. She says **"approve \<post name\>"**. Watch it
schedule. **That moment is the sale** — she sees the loop close.

---

## Hand her three sentences

> - **"Plan my week"** — it plans and drafts.
> - **"Show me the drafts"** — it shows what's waiting.
> - **"Approve \<post name\>"** — the only way anything goes live.

Everything else is in `0 — Start Here` in her folder.

---

## Week one — operator

- **Day 2:** check `accounts/health`. Facebook tokens expire often.
- **Day 7:** run `social-os:learn` yourself before her scheduled task does, so the
  first report she sees is one you have read.
- **Day 14:** ask what she has corrected. Those corrections should be in
  `Her preferences` — if they aren't, the loop isn't closing and that is the thing
  to fix.

---

## Clone to the next franchise — ~45 min, no new build

1. New **Zernio profile** (free) + connect their two accounts *(accounts 3+ cost $6/mo each)*
2. They install the **same plugin**
3. They connect Drive + Canva + Zernio
4. **"set me up"**
5. Two scheduled tasks
6. First approval together

The plugin, the guardrails and the skills are identical. Only the brain differs —
which is exactly the design.

---

## What to charge

Real marginal cost at 20 franchises is roughly **$7/client/month** (Zernio,
graduated). Her own subscriptions — Claude Pro ~$20, Canva Pro ~$15 — she pays
directly and would likely pay anyway.

Price the **managed service**, not the software. The plugin is the delivery
mechanism; there is no paid plugin marketplace and nobody sells plugins
(`01-context/monetization.md`).
