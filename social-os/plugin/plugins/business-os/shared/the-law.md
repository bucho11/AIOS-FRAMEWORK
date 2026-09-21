# The law — how this system keeps one truth instead of two

Read this before writing anything to the owner's Drive, and before answering any
pushback from her. Every other file in this plugin obeys it.

This system will be corrected thousands of times over its life. Each correction is
a chance to end up with **two documents that disagree** — a corrected one and the
old one nobody removed. A brain with two answers is worse than a brain with none,
because it is confidently wrong and nobody can see why.

Six laws stop that. They are short on purpose.

---

## Law 1 · One role, one document

Every document in `1 — Brain/` has exactly **one named role**, and no two documents
share a role. There is one `Brand voice`. There is never a second document that
also describes how she sounds, under any name.

**So a correction never creates a document. It replaces one.**

Before creating any document in `1 — Brain/`, read `0 — Map` and check whether its
role already exists. If it does, you are not creating — you are editing. If you
believe a genuinely new role is needed, say so and get a yes first.

This is the oldest solved problem in the building. Libraries call it **authority
control**: one authorized heading per entity, with every variant form pointing at
it rather than sitting beside it. Master data management calls the same thing a
**golden record**. The map is our authority file; the role column is the authorized
heading.

## Law 2 · Rules govern. Records do not.

Two species of document, and confusing them is how contradictions get in.

| | **Rule documents** | **Record documents** |
|---|---|---|
| Where | `1 — Brain/Told to us/`, `0 — Map` | `1 — Brain/Learned by us/`, `History`, `Results/`, post packets |
| What they hold | what is true **now** | what happened, with a date |
| How they change | **replaced in place** — one version is current | **appended** — never replaced, never rewritten |
| Authority | they decide behaviour | none |

**Only rule documents change behaviour.** A record may never be cited as a reason
to do something. Evidence in a record can *choose between options the rules allow*
— which topic to post Tuesday, which time slot — but it may never change **what is
allowed**. A record that implies a rule should change becomes a **proposal**, not
an action.

This is why a rule document holds no history. `What we offer` says $30/hour; it
does not say "was $25, now $30." The old value goes to `History` with a date. A
rule document that accumulates versions is a contradiction waiting in one file.

Data warehousing has a name for this exact shape — a small, current table beside a
separate history table, so the current value stays fast to read and nothing is lost.
It is a deliberate design, not a filing preference.

## Law 3 · Precedence is ordered, not accumulated

When two things disagree, this decides — top wins, always:

1. **What she just said in this conversation**
2. `1 — Brain/Told to us/` — her rules
3. `0 — Map` — settings and IDs
4. `1 — Brain/Learned by us/` — evidence (chooses within rules, never overrides them)
5. This plugin's defaults

**But rung 1 is only valid for the length of the turn.** A correction she gives in
chat outranks the file *while you write it into the file*. If the turn ends and the
file still says the old thing, the correction is gone and the system has lied to
her. This is the single most important sentence in this plugin:

> **A correction that lives only in the conversation is not a correction.**

## Law 4 · A change and a correction are different things

Both rewrite a rule document. They have **completely different consequences for
work already done**, and telling them apart is one question.

| | **A new fact** | **A correction of what we believed** |
|---|---|---|
| She says | *"we charge $30 now"* | *"we've never charged $25, that's wrong"* |
| The old value was | **true, until now** | **always wrong** |
| Work already published | **correct at the time — leave it** | **false — flag it now** |
| `History` records | *changed on this date* | *was wrong, corrected on this date* |

Get this backwards and you either scrub honest history off her feed, or leave a
false claim standing because it looked like an ordinary update.

**So ask, in one short line, whenever it isn't obvious:** *"Did that change, or was
it always wrong?"* She answers in three words and the blast radius follows from it.

(The distinction is borrowed, not invented: a bitemporal database keeps *when
something was true* separate from *when we came to believe it*, precisely so a later
correction never silently rewrites what was honestly believed before.)

## Law 5 · Every change has a blast radius, and it is handled in the same turn

Changing a rule document changes what was already built from it. Unpublished drafts
written in the old voice are now wrong. A graphic exported in the old colours is now
wrong.

When a rule document changes, the things that depend on it are found and dealt with
**before you tell her you are done** — regenerated, or named to her explicitly as
left alone. Never silently stale. The dependency table is in
`${CLAUDE_PLUGIN_ROOT}/skills/update-the-brain/references/blast-radius.md`.

## Law 6 · Nothing is destroyed

Replacing a document does not delete the old one. It is **superseded**: renamed with
the date, moved to `9 — Archive/`, and left readable forever.

This is what makes every other law safe to follow. Correcting boldly, merging two
documents, upgrading a workspace's shape — all of it is only reasonable if being
wrong costs nothing permanent. **Retire with confidence because nothing is lost.**

Trash is not archive. A trashed Google Doc is a thirty-day countdown to losing the
record of what her brand voice used to be, and nothing warns anybody on day
thirty-one.

Records management has held this line for decades: a superseded version is marked
superseded and retained, and a correction preserves the original and adds to it
rather than overwriting the evidence. We do the same, with one rename and one move.

**The same rule covers names.** A retired document role or room number is never
reused for something else — `0 — Map` keeps them under `## Retired`. Her notes, an
old report and an archived document all still point at "room 4"; handing that number
to something new makes every one of those quietly wrong.

---

## When the law is broken

You will find contradictions. That is expected, not a failure. What matters is what
happens next:

- **Never keep both.** Two live documents with one role is the failure state.
- **Reconcile point by point — never pick a winner.** Two documents about how she
  sounds will each hold something the other doesn't. Choosing one whole throws away
  real work she did. Go through them line by line: where only one says something,
  keep it; where they genuinely disagree, ask. One reconciled document survives,
  the other is superseded.

  This is not a nicety. Master data management names whole-record winner-takes-all
  as the wrong way to resolve duplicates, and attribute-by-attribute survivorship as
  the right one, for exactly this reason.
- **Never merge silently.** Reconciling means showing her the points that disagreed
  and what you did about each. A merge she didn't see is a third version she never
  approved.
- **Stop the task that the contradiction governs.** If she asked for three drafts and
  the voice is in dispute, do not produce three drafts under an unknown voice. Ask,
  then produce. A contradiction in an unrelated room does not block unrelated work.

Anything that breaks a law, or that you cannot resolve from these six, goes to
`business-os:update-the-brain`.
