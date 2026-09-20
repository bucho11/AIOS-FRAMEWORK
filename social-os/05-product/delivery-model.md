# Delivery model — where everything lives and what order it's built in

> `[PRIMARY]` from Anthropic support docs, 2026-09-20. Answers: *where does the
> system live, what comes first, and how does the client receive it?*

---

## The four homes

Nothing lives in one place. Four homes, each with a different job:

| What | Home | Who owns it | Why there |
|---|---|---|---|
| **Master template + research + decisions** | **This GitHub repo** | Operator | Version control. Survives sessions. This is the IP. |
| **Skills + connector config** | **A plugin repo** (GitHub) | Operator | `[PRIMARY]` "Users can... sync marketplaces from GitHub repositories" — one-step install for every client |
| **The brain** (brand, content, calendar, history) | **Her Google Drive** | **Client** | Hers, portable, she can read and correct it (DEC-007) |
| **Her social accounts** | **Her Zernio profile** | Client | Free at 2 accounts; profiles are free and unlimited |

**The repo is the factory. Her Drive is the product. The plugin is the shipping box.**

---

## Verified rules that force this shape

### Skills are account-level. They do NOT load from a connected folder.
`[PRIMARY]` Skills load from **Customize → Skills**. Anthropic's docs describe no
mechanism for a connected folder to supply skills to Cowork. The
`.claude/skills/` project-root discovery is a **Claude Code** feature, not Cowork.

> **Consequence:** we cannot put `SKILL.md` in her Drive folder and have it work.
> Skills must be installed into her Claude account.

### Skill format
`[PRIMARY]` A ZIP whose **root is the skill folder**:
```
my-skill.zip
└── my-skill/
    ├── SKILL.md          ← YAML frontmatter: name, description
    └── resources/
```
Available on **Free, Pro, Max, Team, Enterprise**. Requires code execution enabled.

### Skill sharing is Team/Enterprise only — this is the trap
`[PRIMARY]` Direct sharing, group sharing and org-wide publishing are **Team and
Enterprise features**. On **Free, Pro and Max**, *"skills remain personal to your
account."*

> **Consequence:** on Pro — which is every client — the operator **cannot share a
> skill with her.** Uploading zips one by one would be the manual path.

### Plugins are the way out, and they work on Pro
`[PRIMARY]` *"Each plugin bundles skills, connectors, and sub-agents into a single
package."* Available to **all paid plans (Pro, Max, Team, Enterprise)**. They work
in **Cowork** (sub-agents and hooks are Cowork-only). Installed from the Customize
menu, and **users can sync marketplaces from GitHub repositories** or upload a
custom plugin file.

> **This is the distribution mechanism.** One plugin repo → every franchise
> installs in one step → they get the skills *and* the connector config together.
> Zernio ships their own product exactly this way
> (`zernio-dev/zernio-claude-plugin`, MIT).

---

## Build order

### Phase 1 — Factory (no client, no accounts needed)
1. Template folder written as plain `.md` in this repo — version controlled
2. The four skills written as `SKILL.md` files in the repo
3. Packaged as a **plugin repo** with `.claude-plugin/plugin.json` + marketplace manifest
4. Materialize the template into the **operator's own Drive** as the master copy

*Everything here is buildable right now. Nothing waits on the client.*

### Phase 2 — Operator is client zero (needs a free Zernio account)
5. Operator creates Zernio, connects **his own** test Instagram + Facebook
6. Installs his own plugin in his own Cowork
7. Connects Drive + Zernio, runs the onboarding skill on a dummy brand
8. **Publishes one real post end to end**

> **Never test on the client's accounts.** A childcare brand's Instagram is not a
> staging environment. The operator's own accounts are.

### Phase 3 — Client setup (~30 minutes, live with her)
9. Copy the master template → a new folder; **she owns it**, operator is Editor
10. She installs the plugin (one step), connects Google Drive, connects Zernio
11. Run `brand-onboarding` — fills the brain, ends with 3 sample posts
12. Approve and publish one real post together
13. Set the two Cowork scheduled tasks (weekly plan, weekly report)

### Phase 4 — Clone (each additional franchise)
14. Copy template folder → their Drive
15. New Zernio **profile** (free) + connect their 2 accounts
16. They install the same plugin
17. Run onboarding

*Steps 1–8 happen once, ever. Steps 9–13 are the repeatable ~30-minute install.*

---

## What she actually does

1. Install one plugin
2. Connect Google Drive
3. Connect Instagram + Facebook through Zernio's sign-in
4. Answer the onboarding interview once (~40 min, she gets 3 posts out of it)

Then forever after: **open Cowork, read the drafts, say yes.**
