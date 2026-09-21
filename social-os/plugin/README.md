# social-os plugin — operator guide

This folder is a complete Claude plugin marketplace. When the owning GitHub account
is decided (OQ-011) and public/private is chosen (OQ-012), the contents of this
folder become the root of a new repository. Until then it lives here, next to the
reasoning that produced it.

```
plugin/                              ← becomes the repo root
├── .claude-plugin/marketplace.json  ← the catalog clients sync
└── plugins/social-os/               ← the plugin
    ├── .claude-plugin/plugin.json
    ├── .mcp.json                    ← zernio · canva · google-drive
    ├── skills/                      ← six skills, each SKILL.md + references/
    ├── agents/compliance-reviewer.md
    ├── hooks/hooks.json             ← optional PreToolUse safety net (OQ-014)
    ├── shared/                      ← guardrails, drive-conventions, post-packet, brain-layout, voice template
    └── skills/brand-onboarding/assets/  ← seed docs for the Drive brain
    └── evals/evals.json
```

## Mint the repo (once)

```bash
git init social-os && cd social-os
cp -r /path/to/AIOS-FRAMEWORK/social-os/plugin/. .
# set repository/homepage in plugins/social-os/.claude-plugin/plugin.json
git add -A && git commit -m "feat: social-os plugin v0.1.0"
git remote add origin <the venture's GitHub URL>   # never an employer org
git push -u origin main
```

## Install (what the client does, once)

In Claude: **Customize → Plugins → Personal plugins → "+" → Add marketplace →
Add from a repository** → paste the repo URL → install **Social OS**.

Then connect, when prompted or under Customize → Connectors:
1. **Google Drive** (native)
2. **Canva** (native; sign in to her Canva **Pro**)
3. **Zernio** (the plugin brings it; she signs in — no key to paste)

Then say: **"set me up"** → `brand-onboarding` runs.

## Two scheduled tasks (the client creates these in Cowork, ~1 minute)

Plugins cannot create scheduled tasks; the owner does, once:

| Name | Frequency | Prompt |
|---|---|---|
| Weekly content plan | Weekly, Sunday evening | "Run social-os:plan-week for next week, then social-os:draft-post for every planned row, stage them as drafts, and tell me what's waiting for approval and what I need to film or upload." |
| Weekly results | Weekly, Monday morning | "Run social-os:learn for last week. Lead with anything that needs me." |

## Test before a client touches it (operator is client zero)

1. Free Zernio account → connect **your own** test Instagram Business + Facebook Page.
2. Install this plugin in your own Cowork from the minted repo (or upload the plugin
   folder as a custom plugin file).
3. Run `evals/evals.json` prompts 1 → 3 → 4 → 6 in order on a dummy brand.
4. Confirm: draft created in Zernio as `isDraft`; approval promotes it (check it is
   **not** still a draft); a Canva export → Zernio post actually publishes
   (OQ-013); the compliance reviewer runs; the PreToolUse hook fires or is
   inert (OQ-014).

## What's deliberately not here

- No API keys. Zernio and Canva authenticate by OAuth sign-in.
- No Cloudinary, no Bannerbear, no Composio. Zernio hosts media; Canva Pro designs.
- No Anthropic `small-business` plugin. One plugin, tailored.
