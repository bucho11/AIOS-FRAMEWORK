# Changelog

Every release, written as what changes for the business owner — not as commit
history. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Two numbers move here. The **plugin version** below is the code. The **workspace
version** is the shape of an owner's Drive folder, and it only moves when a release
says so. See `shared/versioning.md`.

## [Unreleased]

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
