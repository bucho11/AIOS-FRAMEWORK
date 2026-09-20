# PROJECT.md — social-os

> The router. Paths, status, and next actions. **This is the only authoritative
> source for these facts** — never use paths or status from memory or old notes.

**Updated:** 2026-09-20
**Phase:** Stack locked at $0. Ready to build Phase 1 in the repo. One gate open (`OQ-009`).

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
| **Image layer** | Hosting solved by Zernio. **Cloudinary** free tier for generated graphics, optional (DEC-011). |
| **Connector layer** | Native Google Drive + Zernio custom MCP. Composio = fallback only. |
| **Status** | Stack locked. Building Phase 1 (repo only — no Drive, DEC-013). |

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
| 4 | Build the client Drive folder from `05-product/client-folder-template.md` | DEC-002 ✅ done |
| 5 | Build the **onboarding skill** — the highest-leverage piece | Round 2 answers |
| 6 | Package the four skills as a **plugin repo** (the clone mechanism) | 5 |
| 7 | Wire connectors into her Cowork, run one end-to-end test post | 3–6 |
| 8 | Package as the clone kit | 7 |

---

## What is NOT being built

Recorded so it doesn't get silently re-added:

- Multi-agent orchestration. One agent + skills. (DEC-001)
- A custom-built scheduler or queue service. Vendor owns the clock. (DEC-005)
- Our own Meta app / App Review. (DEC-004)
- Anything touching nanny **screening decisions** — FCRA liability. (RISKS.md)
- Payroll. Already solved by specialist providers; a compliance minefield.
