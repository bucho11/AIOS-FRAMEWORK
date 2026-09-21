# Rooms — the domains this workspace can run

A **room** is one domain of a business's work: social media, email marketing,
review replies, caregiver recruiting, invoicing. Each is a numbered folder at the
top of her workspace, and each can be added later without touching anything that
already works.

**Rooms are mostly data, not code.** That is the whole point of the model. The laws,
the map, onboarding, correction, housekeeping and upgrades already apply to every
room. A new room usually needs a definition file here, a few folders, and one or two
skills — not a new system.

| Room | Number | What it's for | Connector | Definition |
|---|---|---|---|---|
| Social | `3` | Instagram and Facebook, idea to published | Zernio · Canva | `social.md` |

**Rooms shipped: 1. Room numbers available: `4`–`8`.** The cap is deliberate —
see `${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md`.

## Retired rooms

None yet. A retired number is **never reused** — see `shared/versioning.md`.

---

## Adding a room

1. **Confirm it is a domain, not a format.** A room has its own audience, its own
   destination, and its own idea of "done." "Reels" is not a room; "Email" is.
2. **Copy `_template.md`** to `<room>.md` and fill it in.
3. **Decide shipped or interviewed** for each job in it
   (`${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md`). A domain we genuinely know → we
   write it. Anything specific to how *she* works → `business-os:teach-it-a-job`
   interviews her, and it lives in her Drive where no upgrade can rewrite it.
4. **Add the skills it needs.** Often one or two. Reuse before writing — most rooms
   want plan → draft → approve → send, and the approve-before-anything-goes-out gate
   is not social-specific.
5. **Write the checks before it runs**, not after
   (`${CLAUDE_PLUGIN_ROOT}/shared/proof.md`). Checks written a month in are written
   around the mistakes everyone got used to.
6. **Add a row above.**
7. **Bump MINOR, write the CHANGELOG entry, open the PR.** A new room is purely
   additive, so no migration and nothing for existing clients to approve.

**The brain does not fork.** Every room reads the same `Brand voice` and the same
`What we offer`. A room that genuinely needs different treatment gets a *section
inside* the existing document — never a second copy. This is the single most likely
way this system ever acquires a contradiction, so it is checked before the room is
made (`business-os:update-the-brain`).
