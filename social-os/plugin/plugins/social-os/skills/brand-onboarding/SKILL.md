---
name: brand-onboarding
description: >
  Set up Social OS for a business owner in one warm conversation: research their
  website and Instagram first, interview them (one question at a time) about the
  business, its two audiences, brand voice, offers, and rules, then build their
  Google Drive brain, create their Zernio profile, hand them the Instagram and
  Facebook connect links, and draft three real posts so they see it working today.
  Use this whenever an owner is new, says "set me up", "get started", "onboard me",
  "connect my accounts", "you don't know my brand yet", asks what this can do, or
  when any other social-os skill cannot find the owner's Setup doc in Drive. Also
  use it to revisit one section later — "update my brand voice", "we added a
  service", "change my rules" — it is resumable and re-runnable by section.
---

# Brand onboarding

Turn an owner who *cannot articulate her brand* into a complete, usable brain — in
about 40 minutes she enjoys, not a form she abandons. Everything downstream reads
what this captures, so quality here is the ceiling for every future post.

Read `${CLAUDE_PLUGIN_ROOT}/shared/drive-conventions.md` and `${CLAUDE_PLUGIN_ROOT}/shared/brain-layout.md` before
writing anything to Drive. `references/research-first.md` is what to look at before
saying hello, `references/interview.md` is the questions, and
`references/build-the-brain.md` is the exact creation sequence for Phase 8 —
folder-tree order, seed-doc mapping, the Zernio connect flow, and the health check
that must pass before you tell her it worked.

Read `${CLAUDE_PLUGIN_ROOT}/shared/growth-and-upkeep.md` before creating any folder or document the layout does not already name — especially if the owner asks for something that is not social media.


## The stance

- **Research first, ask second.** Read her website and Instagram *before* the first
  question so you arrive with a hypothesis to confirm, never a blank page. Asking
  something the website answers wastes her time and signals you didn't look.
- **Evidence beats self-report.** "If your brand were a person…" produces worse voice
  than three posts she likes. Ask for samples first, adjectives last.
- **One question at a time, plain words.** She is not technical and never will be.
  Never say "pillars", "voice matrix", "API", "connector". Say "topics", "how you
  sound", "your accounts".
- **Adjectives → rules.** "Professional" is unusable. Convert it: sentence length,
  emoji policy, how direct the ask is. See `${CLAUDE_PLUGIN_ROOT}/shared/voice-profile-template.md`.
- **Resumable.** She runs a business and will be interrupted. Save after every
  section (create the Drive doc as soon as a section is confirmed). On re-entry,
  read what exists and say what is done and what is left — never re-ask.
- **End with output.** Three drafted posts make it feel like a beginning, not
  paperwork.

## Detect where she is

1. Search Drive for a folder named `<Business> — AI Workspace`. If she hasn't named the
   business yet, ask that one thing first.
2. Folder exists and `0 — Map` exists → **return visit**. Read the map and the docs in
   `Told to us/`. Say what's in place, ask what she wants to change, run only that
   section. Do not re-interview.
3. Nothing exists → **first run**. Go to Phase 0.

## The phases

Detailed questions and scripts are in `references/interview.md`. Summary:

**0 · Prep (silent)** — `references/research-first.md`. Fetch her website and
Instagram. Note services, markets, tone, recurring words, what she posts most,
what gets engagement. If Instagram cannot be fetched, plan to ask for five
favourite captions in Phase 4.

**1 · Welcome (2 min)** — what this is, how long, that she can stop anytime and pick
up later, and that she'll have three posts at the end.

**2 · The business (5 min)** — confirm what research found. Ask only what it could
not answer: which location/market is hers, what makes her different, timezone,
how many posts a week she can realistically support, how many Reels she can film.

**3 · Two audiences (5 min)** — families (demand) **and** caregivers/nannies
(supply). Most agencies forget the second. Ask if recruiting is in scope. Who are
they, what do they worry about, what makes them choose her.

**4 · Voice from evidence (10 min)** — show three sample captions in different
voices; "which sounds like you?" Show one that's *wrong*; "why is this wrong?" —
the sharpest question. Extract the sliders, mechanics, vocabulary, and the banned
list. Fill `Brand voice` from `${CLAUDE_PLUGIN_ROOT}/shared/voice-profile-template.md`.

**5 · Offers and CTAs (5 min)** — what she sells, the next step she wants, how leads
actually reach her today (DM? call? form?). Capture exact, documented facts about
screening, credentials, guarantees — these are the only claims `draft-post` may make.

**6 · The rules (5 min)** — what the AI may do alone. Start conservative; it graduates
later by category. Explain the child-imagery rule warmly: it protects her account.
Ask whether photo releases exist for client families. Fill `Rules for the AI`.

**6b · How she wants to be worked with (2 min)** — when she wants drafts, whether to
ask or decide, when she reviews, what would annoy her. Fill `How she likes to work`.
Every later correction about *how you work with her* comes back to this one document.

**7 · Topics, proposed (5 min)** — propose 5–7 topics derived from research + her
answers (see `${CLAUDE_PLUGIN_ROOT}/skills/plan-week/references/pillars-and-cadence.md`). She edits. Never
present as final.

**8 · Build and prove** — create everything (below), then run `social-os:draft-post`
three times on the first three calendar ideas, so she sees real posts today.

## What Phase 8 creates

**Follow `references/build-the-brain.md` step by step** — it has the folder-tree
order (parents before children, holding each returned ID), the bundled-seed-doc to
Drive-title mapping, and the account-health check. Summary:

1. **Drive folder tree** per `brain-layout.md` — root, then every subfolder.
2. **Docs in `Told to us/`** — `About the business`, `Brand voice`, `Who we talk to`,
   `What we offer`, `Colors and fonts`, `Rules for the AI`, `How she likes to work`
   — from her answers, in plain English. Seed text lives in `assets/`; never leave a
   blank doc. **Seven documents, seven jobs, no overlaps** — every later correction
   has to land in exactly one of them (`${CLAUDE_PLUGIN_ROOT}/shared/the-law.md`).
3. **`Colors and fonts`** — ask for her website link and pull logo, primary colours
   and fonts from it; or take a plain-words description ("forest green and cream").
   Never ask for hex codes; work them out and write them down. This doc is what
   lets Canva Pro stay on-brand without an Enterprise Brand Kit.
4. **Fold this interview's corrections into the rule documents themselves.** She
   corrected you a dozen times in the last forty minutes — that is the first real
   test of the discipline. Each correction goes into the document that owns that
   job: voice corrections into `Brand voice`, what-you-may-do into `Rules for the
   AI`, how-to-work-with-her into `How she likes to work`. **Never into a separate
   notes or preferences document** — that is a second source of truth on day one,
   and every correction after it lands in one of two files at random.
5. **Zernio profile** — `profiles_list`; if none is hers, `profiles_create` with the
   business name. Record the ID.
6. **Connect links** — use `search_tools` for the connect endpoint, then `call_tool`
   `GET /v1/connect/instagram?profileId=…` and the same for `facebook`. Hand her
   both `authUrl`s. Instagram must be a **Business or Creator** account; Instagram
   Login needs no Facebook Page. Facebook needs a Page she admins. When she says
   done, `accounts_list` and record the account IDs.
7. **`0 — Map` doc** — every folder ID, every setting, and one row per rule document
   naming the single job it holds. Format: `${CLAUDE_PLUGIN_ROOT}/shared/the-map.md`.
   This is the document every future session reads first, and the reason it never
   has to search her folder.
8. **`0 — Start Here` doc** — from `assets/0 — Start Here.md`, with her
   name and the approval word she chose.
9. **Three drafts** via `social-os:draft-post`.

Then close with three things:
- one line on what exists now, and the exact phrase to approve a post
- **the Project instructions block** — print the block from
  `${CLAUDE_PLUGIN_ROOT}/shared/project-instructions.md` with her folder name filled
  in, and say where it goes. Without it, a future session does not know to read the
  map first or to stop on pushback.
- the two weekly rhythms to set up as Cowork scheduled tasks (see the plugin README)

## If she pushes back during the interview

She will — that is the interview working. A correction here is worth more than one
later, because nothing has been built on the wrong version yet.

Take it into **the document being built**, immediately, in her words. Never into a
scratch list, never into a "notes" document, never only into your own head for the
rest of the session. If the document that owns it doesn't exist yet, note it against
that document's name and write it when you create it in Phase 8.

If she pushes back on something already written, or says "I already told you", run
`social-os:update-the-brain` — even mid-interview. Especially mid-interview.

## Hard requirements

- Never present a blank document.
- Never ask something research could answer.
- Never accept an adjective without converting it to a rule.
- Never write a claim into `What we offer` she did not state as fact.
- Never create two documents that answer the same question. One voice document, one
  offers document, one rules document — forever. Every correction for the next three
  years depends on this being true on day one.
- Always explain the child-imagery rule as protection, not restriction.
- Always end with three real drafts.
