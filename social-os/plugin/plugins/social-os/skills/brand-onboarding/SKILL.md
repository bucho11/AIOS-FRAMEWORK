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

Read `../../shared/drive-conventions.md` and `../../shared/brain-layout.md` before
writing anything to Drive. `references/research-first.md` is what to look at before
saying hello, `references/interview.md` is the questions, and
`references/build-the-brain.md` is the exact creation sequence for Phase 8 —
folder-tree order, seed-doc mapping, the Zernio connect flow, and the health check
that must pass before you tell her it worked.

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
  emoji policy, how direct the ask is. See `../../shared/voice-profile-template.md`.
- **Resumable.** She runs a business and will be interrupted. Save after every
  section (create the Drive doc as soon as a section is confirmed). On re-entry,
  read what exists and say what is done and what is left — never re-ask.
- **End with output.** Three drafted posts make it feel like a beginning, not
  paperwork.

## Detect where she is

1. Search Drive for a folder named `<Business> — Social OS`. If she hasn't named the
   business yet, ask that one thing first.
2. Folder exists and `0 — Setup` exists → **return visit**. Read Setup and the docs in
   `Told to us/`. Say what's in place, ask what she wants to change, run only that
   section. Do not re-interview.
3. Nothing exists → **first run**. Go to Phase 0.

## The eight phases

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
list. Fill `Brand voice` from `../../shared/voice-profile-template.md`.

**5 · Offers and CTAs (5 min)** — what she sells, the next step she wants, how leads
actually reach her today (DM? call? form?). Capture exact, documented facts about
screening, credentials, guarantees — these are the only claims `draft-post` may make.

**6 · The rules (5 min)** — what the AI may do alone. Start conservative; it graduates
later by category. Explain the child-imagery rule warmly: it protects her account.
Ask whether photo releases exist for client families. Fill `Rules for the AI`.

**7 · Topics, proposed (5 min)** — propose 5–7 topics derived from research + her
answers (see `../plan-week/references/pillars-and-cadence.md`). She edits. Never
present as final.

**8 · Build and prove** — create everything (below), then run `social-os:draft-post`
three times on the first three calendar ideas, so she sees real posts today.

## What Phase 8 creates

**Follow `references/build-the-brain.md` step by step** — it has the folder-tree
order (parents before children, holding each returned ID), the bundled-seed-doc to
Drive-title mapping, and the account-health check. Summary:

1. **Drive folder tree** per `brain-layout.md` — root, then every subfolder.
2. **Docs in `Told to us/`** — `About the business`, `Brand voice`, `Who we talk to`,
   `What we offer`, `Colors and fonts`, `Rules for the AI` — from her answers, in
   plain English. Seed text lives in `../../drive-template/`; never leave a blank doc.
3. **`Colors and fonts`** — ask for her website link and pull logo, primary colours
   and fonts from it; or take a plain-words description ("forest green and cream").
   Never ask for hex codes; work them out and write them down. This doc is what
   lets Canva Pro stay on-brand without an Enterprise Brand Kit.
4. **`Learned by us/Her preferences`** — seed it with every correction she made
   *during this interview*. The system starts learning inside the onboarding.
5. **Zernio profile** — `profiles_list`; if none is hers, `profiles_create` with the
   business name. Record the ID.
6. **Connect links** — use `search_tools` for the connect endpoint, then `call_tool`
   `GET /v1/connect/instagram?profileId=…` and the same for `facebook`. Hand her
   both `authUrl`s. Instagram must be a **Business or Creator** account; Instagram
   Login needs no Facebook Page. Facebook needs a Page she admins. When she says
   done, `accounts_list` and record the account IDs.
7. **`0 — Setup` doc** — every ID and setting per `brain-layout.md`.
8. **`0 — Start Here` doc** — from `../../drive-template/0 — Start Here.md`, with her
   name and the approval word she chose.
9. **Three drafts** via `social-os:draft-post`.

Then close: one line on what exists now, the exact phrase to approve a post, and
the two weekly rhythms to set up as Cowork scheduled tasks (see the plugin README).

## Hard requirements

- Never present a blank document.
- Never ask something research could answer.
- Never accept an adjective without converting it to a rule.
- Never write a claim into `What we offer` she did not state as fact.
- Always explain the child-imagery rule as protection, not restriction.
- Always end with three real drafts.
