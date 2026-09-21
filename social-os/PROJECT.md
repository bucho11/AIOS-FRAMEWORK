# PROJECT.md — social-os

> The router. Paths, status, and next actions. **This is the only authoritative
> source for these facts** — never use paths or status from memory or old notes.

**Updated:** 2026-09-21
**Phase:** **Phase 2 — reframed as a business OS, benchmarked, and given an upgrade path.**
The plugin is now `business-os` (DEC-035): a small business's whole AI workspace,
with social as room one and rooms 4-8 open for email, reviews, recruiting and
invoicing. Benchmarked against master data management, ISO 15489 records management,
bitemporal modeling, CMDB/drift, multi-tenant schema migration, Johnny Decimal and
release engineering — **four of six laws had decades-old names, and the study found
three real defects, now fixed** (`03-research/benchmark-study.md`). Added: semver +
CHANGELOG + PR-with-bump releases (DEC-037), two-lane workspace upgrades with a
visible diff (DEC-038), workspace versioning with an explicit FAILED state
(DEC-039), supersede-never-trash (DEC-040), and `tools/validate.py`, which gates
every release and caught a real bug on its first run (DEC-043).
**Still untested:** nothing has been executed against a real workspace (OQ-020,
OQ-023).

**Plus — the playbook and proof layers (v0.4.0).** Benchmarked a second time, against
*The AI Delegation Loop* (Actionable AI), which the operator brought. It confirmed two
of our laws by independent convergence and exposed the largest gap the project has
had: **we had one real check in the entire system, so the owner was the quality
control.** Added 34 checks across five jobs with three severity tiers (DEC-044/045),
`teach-it-a-job` to interview a process rather than invent it (DEC-046), a toolbox
that fills from rebuilt work and examples that carry their reason (DEC-047), and
four-layer diagnosis where **every escape earns a check** (DEC-048). No migration —
the release is purely additive.

**Then hardened against the source's own prompts (v0.5.0).** The operator supplied
the four prompt texts that OQ-024 was tracking. They produced thirteen changes
(DEC-049…054) — the three that matter most: checks now **fix what they can and
re-run** before she sees anything, **three failures on one pass stops the run** and
diagnoses the process instead of patching output, and **the second occurrence of a
mistake earns a preventive rule rather than a reminder.**

**Then the sounds-human layer (v0.6.0).** Every check asked *is this true?*; none
asked the question a reader asks first. For a childcare brand those are the same
question. Added seven surface checks and a structural `sounds-human` skill, adapted
from `humanizer-stack` (MIT) and grounded in Russell et al. 2026 — **verified against
the paper's own abstract** (DEC-055). The rule that outranks the rest: **one or two
moves per piece; a uniformly applied checklist is a new fingerprint** (DEC-056). Voice
is the input and the final guard, not a coat of paint (DEC-057). And the first
licensing decision this project has had to make: **the CC BY-SA lineage was
deliberately not vendored** (DEC-058), with `LICENSE` and `ATTRIBUTION.md` added —
the repo had neither.

**Previously — Phase 1 built and hardened.** Plugin scaffold, **8 skills**, reviewer agent, guardrails, Drive template, 13 evals — in `social-os/plugin/`, mirrored to the public repo `bucho11/social-os`. Zernio verified live end to end (OQ-009/013/016 closed). Latest pass added the **contradiction discipline** (DEC-027…034): one job one document, rules-vs-records, the `0 — Map` index, the `update-the-brain` guard, and the hand-edit precondition. **Untested:** nothing has been executed by Claude against a real workspace — see OQ-020.

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
| **Plugin** | `business-os` v0.6.0 · workspace shape version **2** · 11 skills · 1 room (social; 4-8 free) · 41 checks, 12 blocking · 37 evals · MIT + `ATTRIBUTION.md` |
| **Public plugin repo** | `github.com/bucho11/social-os` — branch `main`. Local clone at `/home/user/social-os`. Source of truth is `social-os/plugin/` in this repo; mirror on every change. **Repo name unchanged on purpose** — renaming it is outward-facing and the operator's call (DEC-035). |
| **Release path** | PR + semver bump in `plugin.json` + CHANGELOG entry. `python3 tools/validate.py` gates it. Direct pushes to `main` do not trigger marketplace sync. |
| **Correctness layer** | `0 — Map` (one index) + `shared/the-law.md` (six laws) + `skills/update-the-brain/` (the guard) + Cowork **Project instructions** pasted at setup (DEC-032). Housekeeping is the monthly backstop, not the guard (DEC-030). |
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
| 11 | **Run migration `001` end to end** against a hand-built version-1 workspace, including one deliberate mid-run interruption and the documented rollback — closes OQ-023. A rollback never performed is a hypothesis | 7 |
| 12 | Confirm whether personal plugins auto-update after a PR-with-bump — closes OQ-021. Until then the runbook says "click Update" | 7 |
| 13 | **Test one check in both directions** — a documented claim must PASS and a one-character change must FAIL. Closes OQ-025. The verbatim match against a Google Doc read back as text is the real risk: a blocking check that false-positives gets overridden habitually within two weeks, which is worse than no check | 7 |
| 14 | Trigger a blocking failure, override it, and read the packet back in a fresh session to confirm the override, reason and date survived — closes OQ-026 | 13 |
| 15 | ~~Get the four prompt texts and fold in anything sharper~~ **✅ done** — operator supplied them; 13 hardenings shipped as v0.5.0 (DEC-049…054). OQ-024 closed | ✅ |
| 16 | Decide whether to report the two measured upstream scanner defects back to `humanizer-stack` — one-line regex fixes, MIT repo, good practice given we built on it. Outward-facing, so operator's call (OQ-029) | operator |
| 17 | Test whether a bundled script executes in a real Cowork session (OQ-028). If it does, checks 11-14 become deterministic scripts and their false-negative rate goes to zero | 7 |
| 18 | Package as the clone kit | 8, 11, 13 |

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
