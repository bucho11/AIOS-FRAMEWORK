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
├── Templates/         the toolbox — created when the first one is needed
├── Examples/          posts she approved that worked, with why (best 10)
└── Results/           weekly performance reports
```

`Templates/` and `Examples/` appear the day they hold something, not at setup.
`learn` fills `Examples/` weekly from the top performer; anything rebuilt from
scratch during drafting is the signal for `Templates/`
(`${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md`).

## Playbooks

Every job here is **shipped** — we wrote the process, it ships in the plugin, and a
release improves it for every client at once. That is right for social: we know how
these platforms work, and a client who had to teach us that got a worse deal than
one who didn't.

A shipped playbook is a domain default, not a claim to know her business. Her first
month of corrections is the most valuable it will ever have — harvest it into the
skill, don't leave it in chat.

| Job | Skill | Origin | Checks |
|---|---|---|---|
| Plan the week | `plan-week` | shipped | — |
| Draft a post | `draft-post` | shipped | 17 · 2 blocking |
| Make a graphic | `make-graphic` | shipped | 6 · 3 blocking |
| Publish or schedule | `publish` | shipped | 11 · 7 blocking |
| Weekly report | `learn` | shipped | 7 |
| Make it sound human | `sounds-human` | shipped | judgement pass |

A job specific to *her* — a local-partnership outreach sequence, a particular kind
of caregiver spotlight she does her own way — is **interviewed**, via
`business-os:teach-it-a-job`, and lives in her Drive where no upgrade can rewrite it.

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

## Definition of done

**A post is done when it is live and its packet says so** — the live URL, the
publish time, the platform, and an evidence report with no unresolved blocking
failure. Not when the vendor accepted it; not when the caption looked good.

**A week is done** when every planned row is either published, scheduled, or
explicitly dropped with a reason, and she knows which.

## Proof

41 checks across the jobs, 12 of them blocking. Two carry the whole weight and
are blocking in three places on purpose, because a graphic can pick up a photo the
caption never mentioned:

- **a child's face with no release on file** — checked in `draft-post` and again in
  `make-graphic`
- **a claim she has not written down** — *licensed, certified, guaranteed, 100%
  safe* — checked in the caption, in the first comment, and in text baked into the
  image

Everything else is needs-a-look or informational. Blocking stays a short list: each
one buys safety with her Friday evening.

**Checks 11–17 on a draft ask whether a person wrote it** — the antithesis cadence,
hype vocabulary, em dash density, sycophancy, emotion performed through the body,
vague allusion, and a skeleton identical to the last three posts. None block; under
fix-then-re-run she never sees most of them. For a childcare brand this is not a
style layer: a parent choosing who watches their kid decides in about a second and a
half whether a human wrote the post, and copy that reads as machine-made leaks trust
in the one market where trust is the entire product
(`${CLAUDE_PLUGIN_ROOT}/shared/sounds-human.md`).

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
