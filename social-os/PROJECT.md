# PROJECT.md — social-os

> The router. Paths, status, and next actions. **This is the only authoritative
> source for these facts** — never use paths or status from memory or old notes.

**Updated:** 2026-09-21
**Phase:** **Phase 1 built and hardened.** Plugin scaffold, **8 skills**, reviewer agent, guardrails, Drive template, 13 evals — in `social-os/plugin/`, mirrored to the public repo `bucho11/social-os`. Zernio verified live end to end (OQ-009/013/016 closed). Latest pass added the **contradiction discipline** (DEC-027…034): one job one document, rules-vs-records, the `0 — Map` index, the `update-the-brain` guard, and the hand-edit precondition. **Untested:** nothing has been executed by Claude against a real workspace — see OQ-020.

---

## Current State

| Field | Value |
|---|---|
| **Type** | Hybrid — product template + client instance |
| **Repo** | `/home/user/AIOS-FRAMEWORK/social-os` |
| **Branch** | `claude/agentic-social-media-system-kfnf7n` |
| **Client (first)** | Lifetime of Love Nannies — one franchise location, market TBC |
| **Client Drive folder** | ❌ not created. Will live in **client's** Google account; operator access via a **personal** account, never HIDEit's (DEC-013). |
| **Operator surface** | Claude Cowork (Pro plan) |
| **Brain / filesystem** | Google Drive via native connector — **not** a local folder (DEC-002) |
| **Publishing layer** | **Zernio** — free at 2 accounts (DEC-010). Also hosts media + native draft gate. |
| **Image layer** | **Canva Pro** via native MCP (DEC-018) — Brand Templates + `replace_text` + `resize-design`. Zernio hosts. |
| **Connector layer** | Native Google Drive + Zernio custom MCP. Composio = fallback only. |
| **Public plugin repo** | `github.com/bucho11/social-os` — branch `main`. Local clone at `/home/user/social-os`. Source of truth is `social-os/plugin/` in this repo; mirror on every change. |
| **Correctness layer** | `0 — Map` (one index) + `shared/the-law.md` (five laws) + `skills/update-the-brain/` (the guard) + Cowork **Project instructions** pasted at setup (DEC-032). Housekeeping is the monthly backstop, not the guard (DEC-030). |
| **Status** | Phase 1 built in repo (no Drive writes, DEC-013). Next: operator is client zero. |

## Platforms in scope

| Platform | Phase 1 | Notes |
|---|---|---|
| Instagram (Business) | ✅ | Must be Business/Creator, linked to the FB Page |
| Facebook Page | ✅ | Native scheduling available — free, reliable |
| TikTok / LinkedIn / GBP | later | Operator said "open"; not phase 1 |

---

## Next actions

| # | Action | Blocked by |
|---|---|---|
| 1 | Operator answers Round 2 questions | — |
| 2 | Confirm IG account is **Business/Creator** and linked to the FB Page | client access |
| 3 | Close `OQ-009` — free Zernio signup, verify MCP tools + one real IG post | **the gate** |
| 4 | ~~Build the client Drive folder~~ → **done as `drive-template/` inside the plugin**; created per client by `brand-onboarding` | ✅ |
| 5 | ~~Build the onboarding skill~~ **✅ built** — `skills/brand-onboarding/` | ✅ |
| 6 | ~~Mint the plugin repo~~ **✅ done** — public at `github.com/bucho11/social-os` (OQ-011/012 closed) | ✅ |
| 7 | **Operator is client zero:** free Zernio + own test IG/FB + Canva Pro → run evals 1,3,4,6 → close OQ-014 | 6 |
| 8 | **Run evals 8, 9, 11, 13 against a real workspace** — the contradiction discipline has never been executed. Eval 9 ("I already told you") and eval 13 (hand-edit) are the two that matter most; OQ-020 is the open question they close | 7 |
| 9 | At first setup: paste the Project-instructions block **before** the interview (runbook step 3), then confirm it reads back verbatim — closes OQ-018 | client call |
| 10 | Rotate the Zernio API key before the first client onboards | operator |
| 11 | Package as the clone kit | 8 |

---

## What is NOT being built

Recorded so it doesn't get silently re-added:

- Multi-agent orchestration. One agent + skills. (DEC-001)
- A custom-built scheduler or queue service. Vendor owns the clock. (DEC-005)
- Our own Meta app / App Review. (DEC-004)
- Anything touching nanny **screening decisions** — FCRA liability. (RISKS.md)
- Payroll. Already solved by specialist providers; a compliance minefield.
- A PreToolUse hook enforcing the laws. Tempting, but `OQ-014` (does the plugin's
  hook fire in Cowork at all) is still open, and a load-bearing guard must not sit
  on an unverified mechanism. If OQ-014 closes positive, a hook becomes cheap
  hardening on top of the instructions — never a replacement for them. (DEC-030)
- A separate correctness *sub-agent*. The pass has to **write** — fix the source,
  propagate, re-stamp the map — and writes belong in the main thread where she can
  see and approve them. Sub-agents stay read-only review (`compliance-reviewer`).
