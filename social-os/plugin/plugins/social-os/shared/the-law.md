# The law — how this system keeps one truth instead of two

Read this before writing anything to the owner's Drive, and before answering any
pushback from her. Every other file in this plugin obeys it.

This system will be corrected thousands of times over its life. Each correction is
a chance to end up with **two documents that disagree** — a corrected one and the
old one nobody removed. A brain with two answers is worse than a brain with none,
because it is confidently wrong and nobody can see why.

Five laws stop that. They are short on purpose.

---

## Law 1 · One role, one document

Every document in `1 — Brain/` has exactly **one named role**, and no two documents
share a role. There is one `Brand voice`. There is never a second document that
also describes how she sounds, under any name.

**So a correction never creates a document. It replaces one.**

Before creating any document in `1 — Brain/`, read `0 — Map` and check whether its
role already exists. If it does, you are not creating — you are editing. If you
believe a genuinely new role is needed, say so and get a yes first.

## Law 2 · Rules govern. Records do not.

Two species of document, and confusing them is how contradictions get in.

| | **Rule documents** | **Record documents** |
|---|---|---|
| Where | `1 — Brain/Told to us/`, `0 — Map` | `1 — Brain/Learned by us/`, `History`, `Results/`, post packets |
| What they hold | what is true **now** | what happened, with a date |
| How they change | **replaced in place** — one version exists | **appended** — never replaced, never deleted |
| Authority | they decide behaviour | none |

**Only rule documents change behaviour.** A record may never be cited as a reason
to do something. Evidence in a record can *choose between options the rules allow*
— which topic to post Tuesday, which time slot — but it may never change **what is
allowed**. A record that implies a rule should change becomes a **proposal**, not
an action.

This is why a rule document holds no history. `What we offer` says $30/hour; it
does not say "was $25, now $30." The old value goes to `History` with a date. A
rule document that accumulates versions is a contradiction waiting in one file.

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

## Law 4 · Every change has a blast radius, and it is handled in the same turn

Changing a rule document changes what was already built from it. Unpublished drafts
written in the old voice are now wrong. A graphic exported in the old colours is now
wrong.

When a rule document changes, the things that depend on it are found and dealt with
**before you tell her you are done** — regenerated, or named to her explicitly as
left alone. Never silently stale. The dependency table is in
`${CLAUDE_PLUGIN_ROOT}/skills/update-the-brain/references/blast-radius.md`.

## Law 5 · She changes the system by talking, not by editing

She does not edit the Drive folder by hand. Every change she wants is a sentence in
chat, and this system makes it happen. That is not a restriction on her — it is the
only way the map, the blast radius and the history stay true.

Because it is a promise rather than a lock, it can be broken by accident. So before
replacing any rule document, check its own two timestamps: **`modifiedTime` later
than `createdTime` means a human edited it** after Claude wrote it. Do not
overwrite. Read what
changed, tell her, and fold it in properly — her edit becomes canon *through* the
system instead of beside it. Details in
`${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md`.

---

## When the law is broken

You will find contradictions. That is expected, not a failure. What matters is what
happens next:

- **Never keep both.** Two live documents with one role is the failure state.
- **Never merge silently.** A merge invents a third version she never approved.
- **Never pick for her** when the two say genuinely different things. Quote both in
  her words, ask one question, then fix it.
- **Stop the task that the contradiction governs.** If she asked for three drafts and
  the voice is in dispute, do not produce three drafts under an unknown voice. Ask,
  then produce. A contradiction in an unrelated room does not block unrelated work.

Anything that breaks a law, or that you cannot resolve from these five, goes to
`social-os:update-the-brain`.
