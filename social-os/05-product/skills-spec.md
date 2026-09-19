# Skills spec

> Six skills. One is the centrepiece.
>
> Operator: *"that onboarding skill is everything, we need that thing perfect and
> really doing a lot of heavy lifting."* This spec reflects that weighting.

---

## The set

| # | Skill | Runs | Priority |
|---|---|---|---|
| **1** | **`brand-onboarding`** | Once per client, resumable | 🔴 **THE CENTREPIECE** |
| 2 | `plan-week` | Weekly, scheduled | High |
| 3 | `draft-post` | On demand + from plan | High |
| 4 | `make-image` | Called by draft-post | Medium |
| 5 | `publish` | On approval | High — **holds the swap seam** |
| 6 | `weekly-report` | Weekly, scheduled | Medium — **closes the learning loop** |

---

# 1 · `brand-onboarding` — the centrepiece

**Job:** turn a non-technical owner who *cannot articulate her brand* into a
complete, high-quality `1 — Brain/Told to us/` — in one warm conversation she
enjoys, not a form she abandons.

## Design principles (research-backed `[SECONDARY]`)

1. **Interview, don't interrogate.** One question at a time. Plain language.
   Never a wall of fields.
2. **Evidence beats self-report.** *"If your brand were a person, how would it
   behave?"* produces a worse answer than reading three posts she likes. **Ask for
   samples first, adjectives last.**
3. **Golden examples.** 3–5 pieces she thinks sound right beat a hundred she's
   unsure about. Ask *"which of these do you like, and which feels off?"*
4. **Adjectives → operating rules.** "Professional" is unusable. Convert it:
   sentence length, vocabulary, emoji policy, directness, formality, CTA style.
5. **Progressive disclosure.** Establish basics, then ask follow-ups *only where
   ambiguity or contradiction is detected.*
6. **Research first, ask second.** Read her site and IG **before** the interview.
   Arrive with a hypothesis to confirm — *"I looked at your Instagram, it reads
   warm and family-first, is that right?"* — not a blank page. **This is the
   heavy lifting the operator asked for.**
7. **Confirm in her words.** Summarise the voice back in plain English and let
   her correct it. Her edits always win.
8. **Stop when you have enough.** Do not collect brand trivia the system will
   never use.
9. **Resumable.** She will get interrupted — she runs a business. Save after
   every section; re-entry says what's done and what's left.

## Flow

```
0 · PREP (silent, before hello)
    read her website · read her IG (recent posts, bio, top performers)
    read corporate brand material if supplied
    → arrive with a hypothesis, never a blank page

1 · WELCOME                      2 min
    what this is, why it matters, how long, that she can stop anytime

2 · THE BUSINESS                 5 min
    confirm researched facts: market, services, what makes her different
    ask only what research could not answer

3 · THE TWO AUDIENCES            5 min
    ⚠️ families AND nannies — most agencies forget the supply side
    who they are, what they worry about, what makes them choose her

4 · VOICE — FROM EVIDENCE        10 min
    show 3 sample captions in different voices → "which sounds like you?"
    show one that's wrong → "why is this wrong?"   ← the sharpest question
    extract: warmth · pace · formality · sentence length · emoji · CTA style
    extract the BANNED list — words, claims, tones

5 · OFFERS AND CTAs              5 min
    what she sells, what the next step is, how leads actually reach her today

6 · THE RULES                    5 min
    what the AI may do alone. Start conservative.
    ⚠️ the child-imagery rule, explained plainly, and the release process

7 · PILLARS — PROPOSED           5 min
    propose 5–7 pillars derived from research + her answers
    she edits. Never present as final.

8 · CONFIRM AND WRITE
    plain-English summary → her corrections win → write all files
    → draft 3 sample posts so she sees it working TODAY
```

**~40 minutes, and she gets three real posts at the end.** Ending with visible
output is what makes it feel like a beginning rather than paperwork.

## Hard requirements

- ❌ Never presents a blank file
- ❌ Never asks something research could answer
- ❌ Never uses jargon ("pillars", "voice matrix", "API") without plain-English framing
- ❌ Never accepts an adjective without converting it to a rule
- ✅ Always resumable
- ✅ Always ends with working sample posts
- ✅ Always explains the child-imagery rule warmly and clearly — it is a safety
  feature she will thank you for, not a restriction

## Output

Writes every file in `1 — Brain/Told to us/`, plus a first-pass
`Learned by us/Her preferences.md` seeded from corrections she made **during the
interview** — the system starts learning inside the onboarding itself.

---

# 2 · `plan-week`
Weekly scheduled task. Reads Brain + `What works.md` + calendar + seasonal/local
hooks → proposes the week across pillars, balancing **both audiences**. Writes to
`Content Calendar.md`. Never repeats an angle used in the last 60 days.

# 3 · `draft-post`
Writes copy in her voice, per platform (IG caption vs FB copy differ). Runs the
banned-claims check. Picks the pillar and format. Calls `make-image`. Writes to
`2 Drafts/`. **Refuses and explains** if the idea needs a child's face with no
release on file.

# 4 · `make-image`
Picks the right Bannerbear template for pillar + format. Fills headline, body,
photo, logo. Returns the **hosted public URL** — the thing Instagram requires and
a Drive link cannot provide. Enforces the no-AI-children rule.

# 5 · `publish` — **the swap seam**
The **only** skill that knows the vendor's tool names. Everything else calls this
with a neutral post object. Implements `schedule` / `cancel` / `status` / `quota` /
`publish_now`. Checks remaining IG quota before scheduling. Moves the file
`3 Approved/` → `4 Published/` with the live URL. **Swapping publishers edits this
file and nothing else.**

# 6 · `weekly-report`
Weekly scheduled task. Pulls performance, writes a plain-English report to
`4 — Results/`, and — the part that matters — **updates `What works.md`** so next
week's plan is better than this week's. This is the loop that makes the system
compound instead of plateau.

---

## Build order

1. `brand-onboarding` — everything downstream depends on its output quality
2. `make-image` + `publish` — prove the plumbing end-to-end with one real post
3. `draft-post`
4. `plan-week`
5. `weekly-report`

Prove one real post reaches Instagram before building the planning layer. A
beautiful planner over broken plumbing is the classic failure here.
