# Changelog

Every release, written as what changes for the business owner — not as commit
history. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Two numbers move here. The **plugin version** below is the code. The **workspace
version** is the shape of an owner's Drive folder, and it only moves when a release
says so. See `shared/versioning.md`.

## [Unreleased]

## [0.7.0] — 2026-09-21

**No workspace migration.** Behaviour only.

### Added
- **A deterministic caption scanner.** The mechanical tells — the negate-then-assert
  cadence, hype vocabulary, sycophancy, vague allusion, embodied emotion, em dash
  density — are now caught by a script rather than by remembering to look. A script
  does not drift, does not get tired on the fortieth caption, and does not quietly
  decide a borderline case is fine.

  It catches **all five** realistic variants of the "it's not just X, it's Y" tell,
  including the contracted forms (`isn't just`, `that's not just … that's`) that a
  pattern anchored on the literal string "not just" cannot see — the letters *n-o-t*
  do not occur in "isn't", and social copy runs on contractions. Measured against the
  scanner this one is informed by: two of five.

  Verified clean on human-written copy, so it flags tells rather than prose.

### Changed
- **A scanner is an accelerator, never a dependency.** Every scripted check is written
  twice: once as the script, once as the pattern list a reader can run by hand. If the
  script does not execute, those checks report `SKIP — read manually` and are
  surfaced. **Never a pass.**

  This closes a gap in our own reasoning: the previous release declined to ship a
  scanner because "one that silently never runs is worse than none" — a risk the
  never-report-an-unrun-check-as-a-pass rule had already eliminated.

## [0.6.0] — 2026-09-21

**No workspace migration.** Behaviour only.

### Added
- **It now checks whether a person appears to have written the post.** That is the
  question a reader asks first, in about a second and a half, before any question
  about whether the post is true. For a childcare brand it is not a style question:
  a parent choosing who watches their kid is making a trust decision, and copy that
  reads as machine-made leaks trust in the one market where trust is the product.
- **Seven new checks on every draft** (11–17): the "it's not just X, it's Y" cadence,
  hype vocabulary, em dash density, sycophantic openers and wrap-ups, emotion
  performed through the body, vague allusion where a name belongs, and a skeleton
  identical to the last three posts. None block — they are style, and blocking is for
  what ends an account. Under fix-then-re-run she never sees most of them.
- **`sounds-human`** — the structural pass, for when the shape is the problem rather
  than the words. Extracts the skeleton and audits *that*, because structural tells
  are invisible at sentence level. Four audits at caption length, two more for
  long-form.
- **Emotion is now named rather than performed.** "Honestly, that first day scared
  her" instead of "her chest tightened." This is the largest measured gap between
  human and AI writing, and it inverts "show, don't tell" — which is precisely the
  advice caregiver stories get written under, making it the highest-yield change here.
- **Shape convergence checked against her actual published posts.** The last three
  packets are on disk, so "does this look like everything else we've run" is a real
  comparison rather than a memory exercise.
- **`ATTRIBUTION.md` and `LICENSE`.** MIT for this repository's own work, with the
  upstream lineages named — including one that carries a share-alike obligation, which
  is why the general-purpose humanizer skill was deliberately *not* vendored and
  childcare-scoped checks were written instead. Read it before white-labelling.

### Changed
- **`Brand voice` now outranks the de-slop checks**, explicitly. If removing a tell
  costs her voice, the tell stays and the reason is said out loud. Copy that passes
  every check and says nothing has not been de-slopped — it has been sanded, and a
  voiceless caption is a rewrite where an em dash was a five-second fix.
- **The voice profile gained a section on handling feeling**, because it is the rule
  most likely to be broken by instinct.

## [0.5.0] — 2026-09-21

**No workspace migration.** Behaviour only.

Thirteen hardenings, from reading the four prompts behind the model v0.4.0 was built
against. v0.4.0 had the architecture; this has the mechanics that make it hold.

### Added
- **Checks now fix what they can and re-run before the owner sees anything.** Nine
  hashtags when the rule is three to five is not news for her — it is something to
  correct and re-check. Handing her a list of failures you could have fixed yourself
  turns a proof layer into a complaints department. Fixes are recorded in the report
  so she can see what the checks are actually catching.
- **More than two failures on the first pass stops the run.** That is not a bad
  output, it is a broken process — a brain document that is wrong so everything
  downstream fails together, or a step that ran out of order. Patching three failures
  individually produces work that passes on a process that will fail the same way
  tomorrow.
- **The second occurrence of a mistake earns a rule, not a reminder.** Once is a
  correction; twice is a missing mechanism. A note saying *"remember to keep hashtags
  between three and five"* is what an apology looks like written down — it reads as a
  fix and enforces nothing. The second time now produces a check, a decision rule, a
  template, or a document rewritten so the wrong reading is no longer available.
- **A correction ends with the before and the after.** The same work, re-run with the
  fix in place, shown both ways. That is the proof the fix worked, and it is what
  separates a correction from a claim of one.
- **The interview has two hard gates** — at least eight questions asked, *and* she
  has said you're done. Eight topics is not eight questions, and an interview that
  ends when the interviewer feels satisfied ends early every time.
- **It closes by asking two questions, separately:** *what did I get wrong*, and
  *what did you forget to tell me*. The second earns the interview — it catches the
  knowledge so obvious to her it never felt like a step, which is where a job's real
  difficulty usually lives.
- **An active test for rebuilt work**, not just passive noticing: run the job again
  from scratch and say which saved files you used and which parts you built from
  nothing. Noticing depends on attention, and attention is what fails on the fortieth
  run.
- **Nothing is ever reported as saved when the save failed.** If a write fails, it
  says so, prints what would have been written, and names where it belongs. A claimed
  save that did not happen is worse than an admitted failure, because nobody goes
  looking for it.

### Changed
- **Decisions in a playbook are written `if X then Y`**, not as prose. *"If the
  invoice is under $50, leave it"* can be followed and checked. *"She applies
  judgement about which are worth chasing"* becomes whatever seems reasonable that
  day.
- **Template filenames say what a file is and nothing else** — no dates, no version
  numbers. A version in a filename creates a second file doing the same job the
  moment it is updated, which is the one-job-one-document law broken by a naming
  habit. Replace the file; the archive keeps the old one.
- **Every template carries one filled-in example underneath it.** The bracketed slot
  says what changes; the example says what belongs there, which a slot name never
  quite does.
- **A template's entry says when NOT to use it**, not only when to. One applied in
  the wrong place is worse than none, because it looks considered.
- **Three things never enter the toolbox:** one-off outputs, anything holding a
  password or key, and a draft she has not approved. An unapproved draft saved as a
  template makes a guess into a standard, quietly.

## [0.4.0] — 2026-09-21

**No workspace migration.** The new folders are created on first use and the new
artifacts are written into new work only, so nothing already in a workspace moves.

### Added
- **It checks its own work before the owner does.** Every job now runs checks that
  can actually fail — is that price written in *What we offer*, is there a release on
  file for that photo, does the published link resolve, does every number in the
  weekly report trace to the data it came from. 34 checks across the five social
  jobs. The result is written into the work itself as an evidence report, so it can
  be read a year later when someone asks how something got out.

  Until now the owner was the quality control: every draft she opened, she was
  proofreading. That is the most expensive possible use of the one person this whole
  system exists to protect.

- **Three severity tiers instead of one policy.** *Blocking* stops the work and is a
  deliberately short list — for a childcare brand, a child's face with no release,
  and a claim she hasn't written down. *Needs-a-look* surfaces with the evidence and
  one word approves it anyway. *Informational* is recorded. An override is written
  down with her reason and the date, because an override is a decision.

- **A check that could not run says so.** It is never reported as a pass. That is
  the most common way a checking layer quietly becomes decoration.

- **`teach-it-a-job`** — learns a job by interviewing the owner about it instead of
  guessing how she works, then writes it into her own workspace. Eight topics: what
  starts it, what you need and where it lives, the steps in your order, the decisions
  and why, how you know it's done, what has gone wrong before, how it should sound,
  and what a bad one looks like. Writes the checks before the job ever runs.

  Writing someone's process for them fails in a way that is hard to see: what you
  wrote is plausible, so it survives review, and it is only wrong in the specifics
  that made it theirs.

- **Playbooks, with four layers per job** — process, toolbox, proof, and context.
  Every playbook declares whether it is *shipped* (we wrote it, improves for everyone
  on release) or *interviewed* (hers, in her Drive, **and no upgrade may ever
  rewrite it**).

- **A toolbox per room.** Anything rebuilt from scratch that existed before is the
  signal that it should be a template. Written into the room's `Templates/` with
  placeholders and indexed, so nothing gets rebuilt because nobody knew it existed.

- **Examples that carry their reason.** Each week's best post is saved to the room's
  `Examples/` with two or three lines on *why* it worked. An example with no reason
  is just an old post. Best ten per room, not the most recent ten — and they are
  records, so they inform drafting and never override *Brand voice*.

- **Diagnosis names the layer.** When something goes wrong: process (a step was
  missed), toolbox (something was rebuilt), proof (nothing caught it), or context
  (the brain document was wrong). The proof row is the one that compounds and the one
  most often skipped, because fixing the output feels like fixing the problem. It
  isn't — **every escape now earns a check.**

- **The corrections log gets read.** Monthly, grouped by layer: the same failure
  three times is not three corrections, it is one missing mechanism. One concrete
  proposal per repeated pattern.

- **A definition of done** on every job, concrete enough that a check could test it.
  A post is done when it is live and its packet says so — not when the vendor
  accepted it.

### Changed
- **The plugin/Drive line is stated precisely.** It was written as "no behaviour
  rules in her Drive", which was never true — `Rules for the AI` is a behaviour rule
  and always lived there. The real line: how the *system* behaves is the plugin's,
  how *her work* is done is hers. Her processes are her work.

## [0.3.0] — 2026-09-21

**Workspace version: 2.** Existing workspaces upgrade through migration `001`, which
shows the owner exactly what changes before changing anything.

### Added
- **Upgrades that don't surprise anyone.** `upgrade-workspace` brings a workspace to
  the current shape. Purely additive gaps are filled silently; anything that renames,
  moves, merges or retires is shown as an exact diff first and applied on one yes.
  Every step is safe to re-run, and a half-finished upgrade records itself as FAILED
  so it can be resumed rather than guessed at.
- **A migration history in the owner's own map**, so the system can always tell what
  shape her workspace is in and what has already run against it.
- **`Told to us/How she likes to work`** — a proper rules document for how she wants
  to be worked with: when to ask, when to decide, when she reviews, what annoys her.
- **`shared/versioning.md`** — the release rules and the expand/migrate/contract
  ceremony for changing a workspace's shape.
- **`tools/validate.py`** — a pre-release check for broken file references, paths
  that escape their skill directory, skill names and descriptions, version
  agreement, and migrations that are listed but not written.

### Changed
- **The plugin is now `business-os`, not `social-os`.** It was never only a social
  media tool: the laws, the map, onboarding, correction, housekeeping and upgrades
  are about running a business's workspace. Social media is the first room. Email,
  reviews, recruiting and invoicing are rooms you add later without touching what
  already works.
- **Two documents that disagree are now reconciled point by point, not by picking a
  winner.** Choosing one document whole throws away whatever the other one got
  right. Master data management calls this attribute-level survivorship, and it is
  the difference between a merge and a loss.
- **A replaced document is superseded, not trashed.** It is renamed with the date and
  moved to `9 — Archive`, so the history of what her brand voice used to be survives
  and a bad correction is recoverable. Records management has held this line for
  decades: a superseded version is marked superseded and retained, never overwritten.
- **A change and a correction are now told apart.** "We charge more now" leaves old
  posts historically correct. "That price was always wrong" makes them false. The
  system asks which, because the answer changes what happens to work already
  published.
- **`housekeeping`** also audits for broken references between documents — a
  documented failure mode of every configuration registry, and one the old audit
  missed.

### Removed
- **`Learned by us/Her preferences`.** Its own text claimed that "never say X"
  instructions "land here and hold from then on" — authority over how to write, from
  a second document sitting beside the one that already holds that job. Its contents
  move to the document that owns each piece. Existing copies are archived, never
  deleted.

## [0.2.0] — 2026-09-21

### Added
- **Corrections that actually stick.** A correction now changes the document that
  caused the behaviour, not just the next few messages. Pushback — "that's wrong",
  "why did you", and above all "I already told you" — stops the task, finds the
  source, fixes it, and fixes whatever was built from it.
- **`0 — Map`** — one index, read first every session. Every folder, every setting,
  and every rules document with the single job it holds. Replaces the two separate
  index documents, which could disagree with each other.
- **A hand-edit guard.** Replacing a document creates a new file and retires the old
  one, so an edit made directly in Drive would have vanished without a trace. The
  system now checks and asks instead.
- **Rooms.** The workspace grows a room at a time — social first, then whatever comes
  next — sharing one brand and one set of brand assets.
- **`housekeeping`** — a monthly safety net and tidy-up.

## [0.1.0] — 2026-09-20

### Added
- First release: onboarding interview, weekly planning, drafting in the owner's
  voice, Canva graphics, approve-then-publish through Zernio, and a weekly learning
  loop. Childcare-grade compliance guardrails and an independent compliance reviewer.
