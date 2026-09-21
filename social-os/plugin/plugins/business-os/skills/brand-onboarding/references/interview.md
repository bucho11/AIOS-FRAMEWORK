# The interview — questions, scripts, and what each answer feeds

One question at a time. Wait for the whole answer. One follow-up if vague, then
move on. If she is pressed for time, the minimum set is marked ★ — never fewer.

## Phase 1 · Welcome

> This takes about forty minutes and you can stop any time — I save as we go. By the
> end you'll have three real posts ready to look at. I've already read your site and
> Instagram, so I'll mostly be checking what I found.

## Phase 2 · The business  (→ `About the business`, `0 — Map`)

★ Which location is yours, and what's the area you actually serve?
★ In one sentence, why do families pick you over the other options?
- What's your timezone? (needed for scheduling; confirm rather than assume)
★ Realistically, how many posts a week can you keep up with? (default 4)
★ How many short videos could you film on your phone in a typical week? (default 2)
- Is there anything corporate requires or forbids in your posts?

## Phase 3 · Two audiences  (→ `Who we talk to`)

★ Tell me about the families who hire you — what are they worried about when they
  first reach out?
- What makes a family say yes?
★ Do you also need to attract nannies? (If yes:) What do great caregivers want from
  an agency, and what do they worry about?

If recruiting is in scope, both audiences get weekly content. Say so.

## Phase 4 · Voice from evidence  (→ `Brand voice`)

Show three short sample captions written in distinctly different voices for the
same idea (e.g. an availability post): one warm-conversational, one polished-premium,
one punchy-playful.

★ Which of these sounds most like you? What's close, and what's off?
★ Here's one that's wrong on purpose. *[a caption with corporate filler, "circle
  back", three exclamation marks]* What bothers you about it?  ← the sharpest question
- Say a phrase you'd never use. Say one you use all the time.
- Emoji: none, a couple, or freely?
- When you post about something sensitive — safety, a hard story — how does your
  tone change?

If Instagram couldn't be read: *"Paste me five posts you were happy with."*

Fill the template in `${CLAUDE_PLUGIN_ROOT}/shared/voice-profile-template.md`. Play it back in plain
English: *"So: short lines, 'we' not 'I', one emoji at most, never 'don't miss
out', always end with an invitation rather than an order. Right?"*

## Phase 5 · Offers and CTAs  (→ `What we offer`)

★ What exactly do you sell? (full-time nannies, sitters, overnight, travel care…)
★ When someone's interested, what do you want them to do — DM, call, book, fill a form?
★ Walk me through your screening — every step, exactly as it happens. (These
  become the only screening claims allowed. Write them as she says them.)
- Any credentials, insurance, or guarantees you hold and can show? (Only what she
  can document goes in.)
- Rough pricing you're happy to say publicly, or "never mention price"?

## Phase 6 · The rules  (→ `Rules for the AI`)

> A few things I'll always check with you on, and a few I'll just do. You can tighten
> or loosen any of these later.

- Drafting posts and ideas: I'll do that on my own and show you.
- Publishing or scheduling anything: only after you say the word. What word do you
  want to use? (default: "approve")
★ Photos of children: I'll never post a child's face unless there's a signed release
  on file — it protects your account and your families. Do you have releases from
  client families today? Where do they live?
- Anything else you never want to see in a post?

Explain the child-imagery rule as protection: Meta removes accounts over this
without warning, and parents trust an agency that visibly guards their kids.

## Phase 6b · How she wants to be worked with  (→ `How she likes to work`)

Two minutes, four questions. Cheap to ask now, and it is what stops the system
being annoying in a way she never quite articulates.

> Last couple on how *we* work together, not on the posts.

- When I bring you drafts — do you want them all at once, or as they're ready?
- If I'm unsure about something, should I ask you, or make a call and tell you?
- When's a good time for you to look at things? (this becomes the weekly rhythm)
- Anything that would annoy you? Long messages, three options to choose from,
  being asked twice about the same thing?

Write the answers in her words. **When she later corrects you about how you work
with her — "stop sending me three options", "just tell me on Monday" — that
correction goes back into this document.** Never into a separate notes file: two
documents about how to work with her is exactly the split this system is built to
prevent (`${CLAUDE_PLUGIN_ROOT}/shared/the-law.md`).

## Phase 6a · What she already built in Canva  (silent — before Phase 4, ideally)

**Do this before asking her how her brand looks.** Two calls, no questions, and it
can make half of the voice-and-look interview unnecessary.

- `list-brand-kits` — if she has a Brand Kit, that is her **real** palette and fonts,
  chosen on purpose, and it beats anything inferred from her website.
- `search-brand-templates` — templates she built and already trusts. These are a
  toolbox that exists on day one, and `make-graphic` should instantiate them rather
  than generate something new that looks almost like her.
- Recent designs — what she has actually published, which is style evidence rather
  than style aspiration.

Both are **Pro+**, not Enterprise. Only *autofill* is Enterprise, and we never need
it — the edit loop fills a template on any plan.

**Then show her what you found**, because it is the fastest trust you will build all
call:

> You've already got a brand kit in Canva — forest green, cream, Poppins for
> headlines. I'll use that. And four templates, including the availability one you
> seem to post most. I'll use those rather than making new ones.

**What a Brand Kit cannot tell you, so still ask:**

- **When** each colour is used — is the dark green for headlines or backgrounds?
- What the logo must **never** sit on.
- Photo style: warm or bright, posed or candid, faces or hands.
- What a post of hers must **never** look like.

**If she has no Canva Pro, or no Brand Kit:** say so plainly and run the normal
questions. `Colors and fonts` is then built from her website and her answers, and it
works — it is the one source every room reads anyway. A missing Brand Kit costs
five minutes of interview, not a feature.

## Phase 6c · The actual files  (→ `2 — Brand Assets/`)

Three minutes, and **skipping it breaks things later** — the folders exist, and if
nothing goes in them the system is missing the raw material it needs.

> Last practical bit. I've made you a folder for your logo, photos and release forms.
> You don't have to do it while we're on the call, but it's five minutes and it saves
> a lot later.

**Ask for these, in this order:**

1. **Logo** — the highest-resolution file she has, ideally a PNG with a transparent
   background. If she only has it inside a Canva design or on her website, say so and
   note it; a screenshot is not a logo and will look like one.
2. **Ten to twenty photos she already owns and is happy to post.** Caregivers at
   work, hands and toys, her office, her team. **Not stock.** This is what the first
   month of posts is built from, and it is the difference between real content and
   filler.
3. **Her photo release form** — the one she has families sign. If she does not have
   one, that is a real finding: say it plainly, because the child-imagery rule means
   **no post can show an identifiable child until a signed release exists on file.**
   Offer to note it as a to-do; do not draft a legal form for her.
4. **Any signed releases she already holds** — one file per family, named so the
   family is findable: `Ruiz family — 2026-03.pdf`.

**Tell her how to hand them over**, because she will not guess:

> Open the Drive folder, go to **2 — Brand Assets**, and drag them into the right
> subfolder. Logos in Logos, photos in Photos, signed releases in Photo releases.
> That's the one part of the folder you *should* put things into.

**This is the exception to "don't touch the folder", and say so**, or she will not do
it. That rule is about *documents that tell the system how to behave*. Dropping a
photo into a folder is supplying raw material, not editing a rule. Nothing can
contradict a logo.

**Record what is missing**, in `Rules for the AI` and in your close: no logo yet, no
release form yet, only four photos. Missing assets are not a failure — they are a
to-do list with real consequences, and she should know which post types are blocked
until each one lands.

## Phase 7 · Topics, proposed  (→ `Content Calendar` seed)

Propose 5–7 topics from research + answers, each with one example post idea. Use
the seven in `${CLAUDE_PLUGIN_ROOT}/skills/plan-week/references/pillars-and-cadence.md` as the starting
set, renamed in her words. She strikes, adds, reorders.

## Phase 8 · Build, then prove

Build everything per SKILL.md. Then draft three posts and show them. Close with:

> Your brain is built. From now on, when you want posts, just say "plan my week"
> and I'll bring you drafts. To publish one, say "<approval word> <post name>".
> Nothing goes live without that word.
>
> One more thing: **you never have to open that folder to change anything.** If
> something's wrong — the wording, the price, what I'm allowed to do — just tell me
> and I'll change it in the right place. If you ever say "I already told you," that
> means I got something wrong at the source, and I'll go find it.
