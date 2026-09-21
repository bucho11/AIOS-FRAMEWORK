# Social

**Number:** `3`
**Connector:** Zernio (publishing, scheduling, media hosting) · Canva Pro (graphics, optional)
**Added:** v0.1.0

## What it's for

Instagram and Facebook, from an idea to a published post, in the owner's voice.
She plans a week, reviews drafts, says her approval word, and posts go out on
schedule. Every week the results come back and change what gets planned next.

"Done" is a post live on the platform with its URL recorded in its packet.

## Folders

```
3 — Social/
├── 1 Ideas/
├── 2 Drafts/          waiting for her. NOTHING publishes from here.
├── 3 Approved/        she said yes; scheduled
├── 4 Published/       live, with the URL (ages to Archive at ~90d)
├── Content Calendar   (Doc) the truth surface for the week
└── Results/           weekly performance reports
```

## Skills

| Skill | What it does |
|---|---|
| `plan-week` | Plans the week across topics and both audiences, from real performance |
| `draft-post` | Writes one post in her voice and stages it for approval |
| `make-graphic` | Designs on-brand graphics in Canva Pro, sized per platform |
| `publish` | The only skill that knows the publisher. Approve → schedule → live |
| `learn` | Weekly: results → what works → next week is better |

## What it reads from the brain

`Brand voice` · `Who we talk to` · `What we offer` · `Colors and fonts` ·
`Rules for the AI` · `How she likes to work`

**All shared.** This room has no voice document of its own and never will.

## What it learns

`1 — Brain/Learned by us/What works — Social (current)`, rewritten weekly, plus a
dated weekly document that is never replaced.

## Guardrails

`${CLAUDE_PLUGIN_ROOT}/shared/guardrails.md` — written for childcare brands, and the
two hard ones outrank everything:

- **Never post an identifiable child's face** without a signed release in
  `2 — Brand Assets/Photo releases/`. Never generate an AI image of a child.
- **Never claim** "licensed", "certified", "guaranteed" or "100% safe" unless that
  exact fact is written in `What we offer`.

An independent `compliance-reviewer` agent reads every draft before it can be
approved, and it cannot write.

## Setup

- A Zernio account (free at two connected accounts) and a profile for this business
- Instagram must be a **Business or Creator** account — personal accounts connect
  but can never publish
- Facebook needs a **Page** she administers
- Canva Pro is optional. Without it, `canva_available: no` in `0 — Map` and the room
  runs on photos, video and text posts only.
