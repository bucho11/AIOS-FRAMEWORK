# Benchmark study — what we were measuring against, and what we should have been

**Date:** 2026-09-21 · **Provenance:** `[SECONDARY]` throughout unless marked
otherwise — Perplexity `sonar`, six queries, cross-read against the primary vendor
docs already in `VERIFIED-FACTS.md`.

---

## Why this exists

The operator asked a question worth taking seriously:

> *"What benchmark are we playing towards? Your own system memory? Or battle-tested
> and proven system architectures that exist on the market? Because the only thing
> that we have right now is the AIOS structure. I believe we need more."*

The honest answer was **yes** — the architecture had exactly two inputs: the AIOS
framework and my own reasoning inside this project. Both are one source, and one of
them is mine. Everything below is the second opinion that was missing.

The finding, stated up front: **we had been rediscovering solved problems.** Four of
our six laws have decades-old names in disciplines built for exactly this. Where we
matched them, it is worth knowing we are on firm ground. Where we didn't, the gaps
were real, and three of them were defects.

---

## 1 · Where the architecture was already right

### One job, one document = the golden record, and authority control

Master data management calls the authoritative view of an entity a **golden
record**, built by matching duplicates and then governing which values survive. The
distinction it draws is one we independently reached: *the golden record is what the
enterprise currently trusts; the system of record is where a value is maintained.*

Library science got there first and got there harder. **Authority control** maintains
one *authorized heading* per entity in an *authority file*, with every variant form
carrying a **see reference** pointing at the authorized form rather than sitting
beside it as a competing entry. That is Law 1, plus the map, plus retired names —
a solution refined over more than a century of catalogues that could not afford two
answers to one question.

**Verdict: on firm ground.** `0 — Map` is an authority file; the role column is the
authorized heading; `## Retired` is the see-reference list.

### Rules vs records = the document/record distinction, and SCD Type 4

ISO 15489 draws precisely our line. A **document** is a mutable informational
object. A **record** is *"information created, received, and maintained as evidence
of business activity"* — fixed, and judged on **authenticity, reliability,
integrity, usability**. A record is *declared* into a managed context, after which
*"it must not be changed in a way that compromises its completeness or provenance."*

That is Law 2, arrived at from first principles and matching a standard we hadn't
read. The vocabulary is better than ours: her post packets and weekly reports are
**declared records**; her `Told to us/` documents are **active documents**.

Data warehousing has the structural name too: **slowly changing dimension Type 4** —
the current values in one small fast table, the history in a separate table. Rule
documents plus `History` is Type 4 exactly.

**Verdict: on firm ground, and now with better words for it.**

### The map = a CMDB, and its failure modes are documented

A **CMDB** stores configuration items and their relationships. **Configuration
drift** is the gap between what it records and what is actually there;
**reconciliation** closes it. The load-bearing line: *"the CMDB should not be treated
as self-validating; it needs ongoing discovery, change control, and verification."*

The documented failure modes are a ready-made audit list: **missing entries, wrong
attributes, broken relationships, duplicate records, and records that outlived the
thing they described.** Our housekeeping audit had four of five.

**Verdict: right shape, one gap** — see §2.4.

### Numbered folders = a bounded taxonomy, and ours was accidentally correct

**Johnny Decimal** caps each level at ten so *"you never face more than 10 choices at
the next decision point,"* explicitly *"a usability constraint, not a
storage-capacity constraint."* Our `0/1/2/3…9` scheme obeys this by accident. We had
never stated the cap, which means the first person to want a seventh room would have
invented `10 —` and quietly broken the property that makes the folder scannable.

**PARA** orders by **actionability** rather than topic — `Projects → Areas →
Resources → Archives`, most actionable first. Our `1 Ideas → 2 Drafts → 3 Approved →
4 Published` is the same principle applied to one room.

**Verdict: right by instinct, now stated on purpose.** Cap written down: six rooms.

---

## 2 · The gaps — three of them were defects

### 2.1 Whole-record survivorship was the wrong resolution *(fixed)*

MDM is explicit: *"Good practice is to treat survivorship at the **attribute level**,
not as a whole-record winner-takes-all decision."* High-risk disagreements escalate
to a human steward; the rest resolve field by field.

**What we had:** *"she decides which survives; the other is trashed."* Whole-record
winner-takes-all — the thing named as wrong practice.

**Why it matters concretely:** two documents about how she sounds exist *because both
got written*. Each holds something the other doesn't. Picking one whole silently
discards work she did, and she finds out a month later when the thing she wrote has
stopped happening — which arrives as *"I already told you,"* the most serious signal
in the system.

**Fixed:** reconcile point by point. Keep what only one says; ask only about the
places they genuinely disagree, which is usually one or two. One document survives,
the other is superseded.

### 2.2 Trashing the old version destroyed her history *(fixed)*

Records management: a superseded version is *"marked superseded and retained... rather
than deleting or overwriting,"* and a correction *"preserves the original record and
adds a controlled annotation, new version, or audit trail rather than overwriting the
evidence."*

**What we had:** replace = `create_file` new + `trash_file` old. And
`[PRIMARY]`, from Google's own documentation: *"Files you move to the Trash are
deleted forever after 30 days."*

So every correction started a thirty-day timer on the record of what her brand voice
used to be, and nothing warns anybody on day thirty-one. `History` got one line —
an audit trail, but not the artifact.

**Why it matters concretely:** a bad correction becomes unrecoverable a month later.
For a system whose entire premise is *"correct me freely, thousands of times,"* the
cost of being wrong must be zero. It wasn't.

**Fixed:** Law 6. Supersede — rename with the date, move to `9 — Archive/`. One
`update_file` call, same cost as trashing, and in eighteen months she can still read
what her voice document said the day she signed up.

### 2.3 A change and a correction were treated identically *(fixed)*

Bitemporal modeling separates **valid time** (when a fact was true in the world) from
**transaction time** (when we came to believe it), and draws the distinction we were
collapsing:

> *Update as new fact*: "X was true until date A, then Y became true from date A."
> *Correction of past belief*: "We believed X, but later learned Y had actually been
> the case all along."

**What we had:** both rewrote the document and logged one line. And the blast-radius
table said, for `What we offer`, *"claims in published posts that are now false (flag
those)"* — which is right for one case and wrong for the other.

**Why it matters concretely, in her feed:**

| She says | Old posts saying $25 | What we must do |
|---|---|---|
| *"we charge $30 now"* | were **true when posted** | leave them — a March post quoting the March price is history, not an error |
| *"we've never charged $25"* | were **always false** | tell her today; a false pricing or credential claim is a live problem |

Treating a price rise as a correction scrubs honest history off her feed, losing the
engagement and links on those posts. Treating a correction as a rise leaves a false
claim standing. **One question — *"did that change, or was it always wrong?"* — and
the answer decides.**

**Fixed:** Law 4, plus a step in `update-the-brain` and a section in
`blast-radius.md`.

### 2.4 Broken relationships were not audited *(fixed)*

CMDB failure modes we covered: missing entries, duplicates, orphans, wrong
attributes. The one we missed: **broken relationships.**

**Concretely:** a room whose connector is listed but disconnected. Nothing looks
wrong — the folder is there, the map row is there, the skills load. It fails on the
day she tries to use it, which is the worst possible day to discover it.

**Fixed:** invariant 4 in `the-map.md`, checked by `housekeeping`.

### 2.5 No migration story at all *(fixed — this was the largest gap)*

There was none. A structural change in v0.2 simply would not reach a client built on
v0.1. At one client that is invisible; at twenty franchises it is a fleet migration
with no plan and no way to tell which workspace is in which shape.

The research is unambiguous about the pattern, and about why it isn't optional:

- **Expand / migrate / contract** (parallel change). Expand is *"purely additive;
  additive changes are the only ones that are safe while old binaries are still
  running."* Contract waits until nothing depends on the old shape. *"A single
  migration that adds and removes in one shot is unsafe."*
- **Idempotency**, because *"a tenant migration can fail halfway"* and tooling
  retries.
- **A migration history table** as the canonical record of what ran. The tools differ
  instructively: **Flyway writes an explicit failed entry**, so a half-applied change
  is visible; **Rails and Django do not mark it**, so *"partial side effects can
  remain in the database even though [it] still considers the migration pending."*
- **Lazy vs eager.** We have no fleet orchestration — a workspace is reachable only
  when a session runs against it — so **lazy/on-read is the only option we have**,
  and the research names its cost honestly: *"can leave cold tenants on old schema
  indefinitely"* and *"reads may have to handle both old and new shapes."*
- The rule that makes it survivable: **"Make readers tolerant before making writers
  strict."**

**Fixed:** `shared/versioning.md`, `skills/upgrade-workspace/`, `migrations/`, and
`workspace_version` + an upgrade history in every map. **We adopted Flyway's
explicit-FAILED behaviour rather than Rails'**, because a partial change that reads
as "not started" is precisely the chaotic state the operator asked us to prevent.

### 2.6 No pre-release validation *(fixed)*

Nothing checked the plugin before it shipped. This repo has already produced two
bugs of exactly the class a validator catches — 22 file references that escaped
their skill directory, and a reference containing a space that could not be parsed
unambiguously. **Both were silent at runtime:** the skill runs, just without its
guardrails.

**Fixed:** `tools/validate.py`. It caught a real defect on its first run.

### 2.7 No release discipline *(fixed)*

`plugin.json` sat at `0.1.0` across four substantive releases, marketplace entries
carried no version, and every push went straight to `main`. Against the `[PRIMARY]`
documented behaviour — *"automatic sync runs when a pull request that includes a
plugin version bump is merged to the repository's default branch"* and *"direct
pushes to the default branch don't trigger a sync"* — that is the configuration
least likely to reach anybody.

**Fixed:** semver, `CHANGELOG.md` in Keep a Changelog format, PR-with-bump as the
release path, and the validator enforcing that the changelog has an entry for the
version being shipped.

---

## 3 · Where we deliberately differ from the benchmark

Not every gap is a defect. Three places we are knowingly different:

**Progressive delivery is one workspace, not a percentage.** Canary releases and
staged rollout percentages assume a fleet and metrics. We have one client. The
honest local equivalent is *the operator runs every release in his own workspace
first*, and upgrades clients in waves once there are more than a handful.

**No automated contract test against a live workspace.** JSON Schema, Pact and
schema-registry compatibility modes all assume a validator that runs. There is no CI
that can reach a client's Google Drive. So the map's contract is stated as
**invariants a skill checks on a cadence**, not as a schema a machine enforces. We
validate the plugin mechanically and the workspace behaviourally, and we say so
rather than implying more rigour than exists.

**No `plan`/`apply` dry-run mode as a separate command.** Terraform separates them
into two invocations. We fold the plan into the conversation — the diff is shown,
she answers, it applies in the same turn. Splitting them would mean she has to come
back, and a pending upgrade nobody returns to is worse than one applied on a yes.

---

## 4 · What is still missing, honestly

- **None of it has been executed.** The whole correction and upgrade discipline has
  been structurally validated and logically reviewed, never run. `OQ-020` is the
  open question and it is the most important one in the project.
- **Reference tolerance is asserted, not tested.** "Readers tolerant before writers
  strict" is written down. Whether skills actually read both shapes has not been
  exercised, because there is no old workspace to read.
- **`${CLAUDE_PLUGIN_ROOT}` substitution in Cowork is still `OQ-017`.** A large
  amount now lives in `shared/`. The mitigation stands — the hard rules are inlined
  in each skill body, so a substitution failure costs depth rather than safety — but
  it is a mitigation, not a resolution.
- **No rollback rehearsal.** Every migration documents a rollback. None has been
  performed. A rollback that has never been run is a hypothesis.

---

## Sources

Perplexity `sonar`, 2026-09-21, six queries covering: master data management and
authority control · ISO 15489 records management · bitemporal modeling and slowly
changing dimensions · multi-tenant schema migration, expand/contract, and migration
tooling · CMDB, configuration drift and desired-state reconciliation · Johnny Decimal
and PARA · JSON Schema, Pact and schema-registry compatibility · semantic versioning,
Keep a Changelog and progressive delivery. All `[SECONDARY]`.

Primary sources verified separately and recorded in `VERIFIED-FACTS.md`: Google
Drive trash retention, Drive connector timestamp fields, and Anthropic's plugin
marketplace sync behaviour.
