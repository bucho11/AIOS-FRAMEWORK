# Checks — learn

The weekly report is the document she trusts to tell her what is working. A number
in it that traces to nothing is worse than no report, because she will act on it.

Contract: `${CLAUDE_PLUGIN_ROOT}/shared/proof.md`.

---

### 1 · Every number traces
**Tier:** needs-a-look
**Evidence:** each figure in the report, matched to the analytics response it came
from
**Fails when:** a number appears that is not in the source response, or is a
derived figure whose inputs are not shown
**Report as:** each number and its source field — or `not traceable`

The single most important check here. A report that cannot be traced is a report
that cannot be corrected.

### 2 · No adjective without a number
**Tier:** needs-a-look
**Evidence:** the report's sentences
**Fails when:** a performance claim — *strong, up, dropped, best, underperformed* —
appears with no figure beside it
**Report as:** the sentence

### 3 · Attribution is possible
**Tier:** needs-a-look
**Evidence:** each published packet in the window, and whether its Drive id came
back with the analytics
**Fails when:** a post in the window has performance data that cannot be paired to a
packet
**Report as:** the count paired, and the count orphaned

An orphaned post means `publish` dropped the packet id (its check 9). Say so — the
fix belongs in that skill, not here.

### 4 · The window is the window
**Tier:** informational
**Evidence:** the date range requested versus the range the data covers
**Fails when:** they differ
**Report as:** both ranges

### 5 · Health was actually checked
**Tier:** informational
**Evidence:** the account health response
**Fails when:** it was not called, or could not be reached
**Report as:** each account and its state

### 6 · One recommendation, and it is followable
**Tier:** needs-a-look
**Evidence:** the report's closing recommendation
**Fails when:** there is none, there is more than one, or it does not name a
specific thing to do differently next week
**Report as:** the recommendation

*"Post more Reels"* fails. *"Two Reels instead of one, Tuesday around 6pm — that
slot carried the top three posts this month"* passes.

### 7 · A proposal is a proposal
**Tier:** needs-a-look
**Evidence:** the report text, and what was written to `Learned by us/`
**Fails when:** the report changed a rule rather than proposing one — anything that
reads as an instruction written into `Learned by us/`, or a `Told to us/` document
edited from this skill
**Report as:** what was written and where

Law 2. Evidence proposes; it never decides. This check exists because that boundary
is crossed by helpfulness, not by malice, and nothing else would notice.
