# Versioning — two numbers, and the discipline that keeps them honest

Read this before shipping a release, and before changing anything about the shape
of a workspace.

There are **two** version numbers in this system, they mean different things, and
confusing them is the classic way a fleet of clients quietly diverges.

| | **Plugin version** | **Workspace version** |
|---|---|---|
| Lives in | `plugin.json` + the marketplace entry, in git | `0 — Map`, in her Drive |
| Answers | *which code is she running?* | *what shape is her folder in?* |
| Changed by | us, on release | a migration, on her next session |
| Format | semver — `MAJOR.MINOR.PATCH` | a plain integer — `1`, `2`, `3` |

**They are not the same and they do not move together.** A release that only
improves wording bumps the plugin and leaves every workspace untouched. A release
that changes the folder shape bumps both. A workspace can sit on version 2 for
months while the plugin moves 0.3.0 → 0.4.0 → 0.5.0 — and everything must keep
working the whole time.

---

## Part 1 · The plugin version

### Semver, applied honestly

- **PATCH** (`0.3.0 → 0.3.1`) — a fix. Nothing about behaviour changes for her.
- **MINOR** (`0.3.0 → 0.4.0`) — new capability, backward compatible. A new room, a
  new skill, a better prompt. **Her existing workspace keeps working untouched.**
- **MAJOR** (`0.x → 1.0`, later `1.x → 2.0`) — something that was there is gone or
  works differently. **This is the only kind of release that may require a
  migration**, and it is rare by design.

We are on `0.x` deliberately: semver reserves that for "the public interface is not
yet stable." Once the first client has run for a month, we go `1.0.0` and start
meaning it.

**The practical test:** *can she upgrade and notice nothing?* Yes → PATCH or MINOR.
No → MAJOR, and it needs the ceremony in Part 3.

### Every release is a pull request with a version bump

Not process for its own sake. **It is the documented mechanism.** Anthropic's
marketplace sync fires *"when a pull request that includes a plugin version bump is
merged to the repository's default branch,"* and *"direct pushes to the default
branch don't trigger a sync."* A release pushed straight to `main` without a bump
is a release that reaches nobody.

So, every time:

1. Branch.
2. Make the change.
3. **Bump `version` in `plugin.json`** — and in the marketplace entry, which is
   documented to be overridden by `plugin.json` when both are set, so keep them
   equal to avoid confusing a human reading the catalog.
4. **Add a `CHANGELOG.md` entry** — Keep a Changelog format, grouped under `Added`,
   `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`. Written as *what
   changes for her*, never as commit history.
5. Open the PR, merge it.

### Clients float to latest

Deliberate choice. A pinned client has to be told to do something before they get
the work you already did for them — which is friction for both of you, and it means
a fix you shipped is sitting in a repo helping nobody.

Floating is only safe because of everything else in this file: additive by default,
breaking changes get the expand/migrate/contract ceremony, migrations show a diff
before they touch anything, and nothing is ever deleted. **Make "latest" safe, then
let everyone have it** — rather than making everyone opt in to safety.

The manual backstop is documented and it is one sentence to a client: *"open
Plugins, find Business OS, click Update."* Use it when you want a client on a new
release the same day.

### The operator's own workspace is the canary

Progressive delivery, at the scale we actually have. **You run every release in your
own workspace first**, before a client sees it. Not a policy — a habit that costs
nothing and catches the release that would have embarrassed you.

With more than a handful of clients, upgrade them in waves rather than all at once,
so a bad release meets two workspaces instead of twenty.

---

## Part 2 · The workspace version

Her folder has a shape, and that shape has a number. `0 — Map` carries:

```
workspace_version: 2
```

**Why an integer and not semver:** a workspace shape is either current or it isn't.
There is no "compatible minor shape." Integers also make the migration list
trivially orderable, which is the whole job.

The map also carries a migration history, because **a migration that nothing
records is the thing that actually causes chaos** — not the migration itself:

```
## Upgrade history

| To version | When | Result |
|---|---|---|
| 2 | 2026-09-21T18:04Z | done |
| 3 | 2026-10-02T09:12Z | FAILED — stopped after moving 2 of 5 docs |
```

That `FAILED` row is not decoration. Flyway, the most widely deployed database
migration tool, writes an explicit failed entry precisely so a half-applied change
is visible rather than silently pending. Rails and Django don't mark it, which is
why their docs warn that partial side effects can remain while the migration still
reads as "not run." **We mark it.** A workspace with a `FAILED` row is not touched
further until `business-os:upgrade-workspace` resolves it.

**No workspace_version at all** means the workspace predates versioning. Treat it as
version 1.

---

## Part 3 · Changing the shape of a workspace

**Never make a breaking change in one step.** This is the single most load-bearing
rule in this file, and it is not ours — it is the expand/contract pattern (also
called parallel change), which exists because some instances will always be running
older code than others.

We have no way to upgrade every client at once. There is no fleet console; a
workspace is only reachable when a session happens to run against it. So a client
who doesn't open Cowork for six weeks **is** a client running an old shape, and
nothing we do changes that. The pattern is not optional for us; it is the only thing
that works.

### Three releases, minimum

**1 · Expand** — add the new thing beside the old. Purely additive. Both shapes
work. Nothing is removed and nothing is renamed. Old code that has not updated yet
is unaffected, because everything it reads is still there.

**2 · Migrate** — the plugin now reads **both** shapes and writes the new one. A
workspace upgrades on its next session. This is where the new shape becomes the
default, and where the old one starts being unused rather than unsupported.

**3 · Contract** — the old thing is retired, and only once the migration history
shows workspaces have moved. Retired means **superseded and archived**, never
deleted.

Renaming `0 — Setup` to `0 — Map` is the worked example: expand writes both,
migrate reads either and prefers the new, contract archives `0 — Setup` with a
pointer to its replacement.

### The rule that makes this survivable

> **Make readers tolerant before you make writers strict.**

Every skill should read the old shape and the new one for at least one full release
cycle. Reading tolerantly costs a fallback branch. Reading strictly too early costs
a client a broken workspace, discovered by them, on a Monday.

### Reserved forever

A room number and a document role, once used, are **never reused for something
else**. Retire `4 — Email` and `4` stays retired; the next room takes `5`.

This is Protobuf's rule — never reuse a field number, mark removed ones `reserved`
— and it exists because old references keep resolving. Her notes, her memory, a
link in an old report and an archived document all point at "room 4." Giving that
number to Invoicing means every one of those now points at the wrong thing, and
nothing errors.

Retired numbers and roles are listed in `0 — Map` under `## Retired`.

### What may never happen

- A breaking change and its cleanup in one release.
- A migration that deletes. Supersede and archive; trash is a 30-day countdown to
  losing her history.
- A migration that cannot be safely re-run. Every step is guarded — create only if
  missing, move only if not already moved.
- A migration that restructures her folder without showing her what will change
  first. See `skills/upgrade-workspace/`.
- Reusing a retired number or role.

---

## Part 4 · Shipping a new room

The common case, and the happy one: **a new room is purely additive, so it is a
MINOR release and needs no migration at all.**

1. Add the room definition under `rooms/`.
2. Add its skills.
3. Bump MINOR, write the CHANGELOG entry, merge the PR.
4. The next time she says *"can this do email?"*, `business-os:update-the-brain`
   creates the room in her workspace and rebuilds the map.

Nothing existing is touched, so there is nothing to migrate and nothing to approve
beyond the room itself. That is the whole point of the room model — **growth should
be the cheap path**, and only reshaping should be expensive.
