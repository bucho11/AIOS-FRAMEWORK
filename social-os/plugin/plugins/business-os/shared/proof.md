# Proof — checks that can actually fail

Read this before writing any check, and before any skill hands work to the owner.

**Without this layer, she is the quality control.** Every draft she opens, she is
proofreading: did it get the price right, is that claim real, is there a release for
that photo. That is the most expensive possible use of the one person whose time
this system exists to protect — and it degrades, because proofreading the tenth
draft is not proofreading the first.

The bar, and it is the whole file in one line:

> **If a check cannot fail, it is not a check.**

---

## What a check is

A check produces **external evidence** — something outside the model's own opinion.

| A check | Not a check |
|---|---|
| "$30/hour" appears verbatim in `What we offer` | "the pricing looks right" |
| the caption is 1,840 characters, limit 2,200 | "the caption is a good length" |
| `Photo releases/` holds a file naming this family | "this photo seems fine" |
| the published URL returns HTTP 200 | "it should be live" |
| every number in the report appears in the analytics response | "the numbers look consistent" |
| the words licensed · certified · guaranteed · 100% safe do not appear | "no overclaiming" |

The right-hand column is **judgment**. Judgment has a place — the
`compliance-reviewer` agent is judgment and it is worth having — but judgment is not
proof, and a system that only has judgment has no floor under it.

**The test before you write one:** *what specific input would make this fail?* No
answer means it is not a check. Delete it; do not soften it.

## Five or ten per job, not thirty

Enough to catch what actually goes wrong, few enough that every one is read. A
hundred checks nobody looks at is the same as none, with more work.

The generator for new checks is not imagination — it is **escapes**. Something
reaches her that shouldn't have, and the fix is a check, written that day
(`update-the-brain`, layer diagnosis). Checks that come from real escapes are the
only ones that stay worth running.

---

## Severity — three tiers, declared per check

One global policy for all checks is the wrong shape. A missing photo release and a
caption three words over are not the same event, and treating them the same either
blocks her over nothing or lets something through that ends an account.

| Tier | What happens | For |
|---|---|---|
| **blocking** | **Work cannot move to `3 — Approved/`.** She can override, but only by saying so explicitly, and the override is recorded. | The existential ones. For a childcare brand: a child's face with no release on file, and an unsubstantiated safety or credential claim. Nothing else. |
| **needs-a-look** | Surfaced with her, with the exact evidence, in one line. One word approves anyway. | Most things. A price not found in `What we offer`. A caption over the limit. A missing alt text. |
| **informational** | Written to the evidence report. Not surfaced. | Counts and context she'd only want when investigating. |

**Blocking is a short list and it stays short.** Every check promoted to blocking
buys safety with her Friday evening. Promote one only when the failure is something
she would want stopped even at the cost of missing a post.

## A check that could not run is not a check that passed

If the evidence was unavailable — the connector was down, the file could not be
read, the URL timed out — the result is **`could not check`**, and it is surfaced
like a `needs-a-look`. Never a pass.

This is the single most common way a proof layer quietly becomes decoration: the
check errors, the error is swallowed, the report says nothing, and everyone reads
silence as success.

---

## The evidence report

Checks that only spoke in the conversation did not happen — Law 3. **The report is
written into the work itself**, in the post packet or document it checked, so it
survives the session and can be read a year later when someone asks how something
got out.

Format, kept to what can be scanned:

```
## Checks — 2026-09-21T18:04Z · draft-post v0.4.0

PASS   claim check          "$30/hour" found in What we offer, line 12
PASS   banned words         none of licensed/certified/guaranteed/100% safe
PASS   caption length       1,840 of 2,200
PASS   alt text             present, 94 chars
LOOK   hashtag count        8, expected 3-5
BLOCK  photo release        no file in Photo releases/ names "the Ruiz family"
SKIP   media validates      could not check — publisher returned 503

1 blocking, 1 needs a look, 1 could not be checked.
```

**Rules for the report:**

- **Every check appears, including the passes.** A report that lists only problems
  cannot be told apart from a report where the checks never ran.
- **Evidence, not verdicts.** `"$30/hour" found in What we offer, line 12` — not
  `pricing ok`. The evidence is what makes it auditable by someone who doesn't trust
  the checker.
- **The version that ran it.** Checks change; a report from six months ago must say
  which set it used.
- **An override is recorded in the report**, in her words and dated, not just acted
  on. *"Approved anyway — I have the release on paper, filing it Monday."*

## What she sees

One line when everything passes. Silence is wrong — she needs to know the checks
ran — but a clean run does not deserve a paragraph.

> ✅ 7 checks passed. Ready when you are.

When something needs her, lead with it and give the evidence, never the verdict:

> ⛔ I can't stage this one: there's no photo release on file for the Ruiz family.
> Want me to swap in the no-faces version?
>
> One other thing: 8 hashtags, we've been using 3–5.

---

## Writing checks for a job

Checks live with the job they check — `skills/<job>/references/checks.md` — because
a check separated from its process drifts from it.

Each one states four things:

```
### Claim check
**Tier:** needs-a-look
**Evidence:** every factual claim in the caption appears verbatim in `What we offer`
**Fails when:** the caption states a service, price, credential, timeframe or
  guarantee that is not written in that document
**Report as:** the claim, and the line it was found on — or that it was not found
```

If you cannot write the **fails when** line concretely, you do not have a check yet.
