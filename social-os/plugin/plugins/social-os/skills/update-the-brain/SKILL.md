---
name: update-the-brain
description: >
  The only safe way to change what this system knows or how it behaves, and the
  required first response when the owner pushes back. Use when she corrects
  something ("that's wrong", "no, we don't do that", "I never said that"), asks why
  something happened ("why did you post that", "where did that come from"), repeats
  herself ("I already told you", "we talked about this"), disagrees or sounds
  frustrated, changes a fact ("we charge more now", "we've added overnight care",
  "change my brand voice"), asks to add a room, connector or new kind of work, or
  when you notice two things in her workspace that disagree. Finds the document that
  caused the behaviour, fixes that document, fixes everything built from it, and
  records it — instead of apologising and leaving the old version in place.
---

# Update the brain

**Everything this system does comes from a document.** So a correction that does not
change a document has not happened — it lasts until the end of the conversation and
then the old version takes over again. Worse, if a note gets added beside the old
version instead of replacing it, her brain now holds two answers and nobody can see
which one is winning.

That is the failure this skill exists to make impossible.

Read `${CLAUDE_PLUGIN_ROOT}/shared/the-law.md` — the five laws — and
`${CLAUDE_PLUGIN_ROOT}/shared/the-map.md` before doing anything here. The five laws
in one line each:

1. **One role, one document.** A correction replaces; it never adds.
2. **Rules govern; records don't.** `Told to us/` decides. `Learned by us/` proposes.
3. **Precedence is ordered** — and a correction is only real once it is in the file.
4. **Every change has a blast radius**, handled in the same turn.
5. **She changes things by talking.** A hand-edited file is a stop, not an overwrite.

---

## When this runs

**Always, on any write to a rule document.** Rule documents are the ones in
`1 — Brain/Told to us/` and `0 — Map`. Creating a room, adding a connector, or
installing a new kind of work counts. Assume a contradiction is possible on every
single one; the check below costs two calls.

**Always, on pushback.** Detection list and the protocol are in
`${CLAUDE_PLUGIN_ROOT}/skills/update-the-brain/references/pushback.md`. Read it
before responding to her.

**Always, when you notice it yourself.** If you read two things in her workspace
that disagree, stop there. Waiting for her to catch it means the contradiction has
already produced bad work.

**Never for records.** Drafts, weekly reports, history entries, post packets,
results. They cannot contradict anything, because they have no authority.

---

## The pass

### 1 · Find the source

Name the document that caused the behaviour. Not "I'll fix it" — *which document*.

Read `0 — Map` and match what she is talking about to a role in the rule-documents
table. Voice → `Brand voice`. Pricing or services → `What we offer`. Audience →
`Who we talk to`. What you may do alone → `Rules for the AI`. How she wants to be
worked with → `How she likes to work`. Look, colours, fonts → `Colors and fonts`.
The business itself → `About the business`.

If you genuinely cannot tell which document, **ask exactly one short question** —
see the pushback reference for how to ask it without making her do your work.

### 2 · Check for a competitor

Scan the rule-documents table in the map for a **second document holding the same
role**. This is the check that keeps Law 1 true, and it costs one read.

Found one → that is the bug, and it outranks whatever she asked about. Quote both,
ask which is right, keep one, trash the other, and say what happened.

### 3 · Check nobody edited it by hand

`get_file_metadata` on the document. **Is `modifiedTime` later than `createdTime`?**
Compare the file to itself — `createdTime` is the moment Claude created it (every
replacement mints a new file), so it is an immutable anchor that holds even if the
map's stamp drifted. Cross-check `createdTime` against `claude_wrote`; if those
disagree, the map row is stale — heal it first.

**`modifiedTime` later means a human edited it.** Stop. Do not replace it — replacing means
creating a new file and trashing the old one, and her edit would go with it. Read
what it says now, tell her in one line what changed, and ask whether to keep it. If
yes, fold her wording in and continue. Her edit becomes canon through the system
instead of beside it.

### 4 · Verify before you flip

If what she is saying contradicts what the document says, do not just believe the
newest voice in the room — that is how a misremembered detail becomes canon.

Read the document. Then either:

- **it agrees with her** → she is describing something the system got wrong
  elsewhere; keep looking for the real source, or
- **it disagrees with her** → say so plainly, in one line, quoting it: *"Right now
  What we offer says $25/hour — do you want that to be $30?"*

She is almost always right. Saying what the file currently holds costs one sentence
and stops a wrong correction becoming permanent.

### 5 · Fix the source

Replace the document — never add a note beside the old text, never keep a
"previously" section. `${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md` has the
two-call replace. Rules hold only what is true now.

### 6 · Handle the blast radius — in this turn

Everything built from that document is now out of date. Find it and deal with it
before you tell her you are done. Table and procedure:
`${CLAUDE_PLUGIN_ROOT}/skills/update-the-brain/references/blast-radius.md`.

**Stale is never acceptable, but leaving something alone can be** — as long as you
say so. "I redid the two drafts; the three posts already scheduled for this week
still use the old wording — want me to redo those too?"

### 7 · Re-stamp the map

New Drive ID, `claude_wrote` set to now. One line, per `the-map.md`. Skipping this
is how the next lookup fails and the next hand-edit goes unnoticed.

### 8 · Record it

One dated line in `1 — Brain/Learned by us/History`: what changed, from what to
what, and why. That is the trail — the rule document itself keeps no history.

### 9 · Go back to what she asked for

Resume the original task **from the corrected state**. Not from where you were.

---

## How to talk while doing this

**Never open with an apology.** "Sorry, I'll fix that" is the exact response that
produced the problem — it sounds like a fix and changes nothing. Open with the
cause: *"That came from Brand voice — it says to use exclamation points."*

**Be short when it goes cleanly.** Most corrections are two lines:

> Got it — I changed **Brand voice** to drop the exclamation points, and redid the
> two drafts that used it. The post going out Thursday still has the old wording;
> want me to redo it?

**Be silent when nothing is wrong.** If the check finds no competitor, no hand-edit
and no dependents, do not narrate it. She should feel a system that is easy to
correct, not one that audits itself out loud.

**Ask one question at a time, and make it answerable in a word.** Not "how would you
like me to handle the tension between these documents." Instead: *"Which is right —
$25 or $30?"*

---

## Adding something new — a room, a connector, a kind of work

Growth goes through the same door, and the same laws.
`${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md` has the room procedure. The two
things this skill adds:

- **A new room may not duplicate a role.** An email room does not get its own voice
  document — her voice is one document with a section for email if it needs one. The
  brain does not fork. This is Law 1 at the room level, and it is the single most
  likely way this system acquires a contradiction as it grows.
- **A new room, connector or skill gets exactly one row in the map**, and the map is
  rebuilt. Anything installed but not in the map is invisible to every future
  session.

## Rules

- Never keep two documents with one role. Ever.
- Never merge two versions on your own. One wins, she decides, the other is trashed.
- Never write a behaviour rule into `Learned by us/` — propose it, get a yes, put it
  in `Told to us/`.
- Never overwrite a document whose `modifiedTime` is newer than its stamp.
- Never say something is fixed before the document is written.
- Never do this to a post, a report or a history entry. Records are not corrected;
  they are the evidence.

## If there is no workspace yet

Search Drive for `<Business> — AI Workspace`. Missing → run
`social-os:brand-onboarding`. Folder there but no `0 — Map` → rebuild the map from
the folders as they actually are (per `the-map.md`), say that you did, and continue.
