# Marky, and where real-looking images actually come from

**Date:** 2026-09-22 · Prompted by the client naming Marky's content style, and
asking about photo libraries because "AI content sometimes looks too AI."

---

## Part 1 — Marky

### What it is `[PRIMARY]`

An end-to-end social platform for **local service businesses** — the same market as
ours. Learns the brand from a website URL, generates posts, designs graphics from
templates, schedules and publishes to 7 platforms. Claims *"written in your brand
voice. Not generic AI slop."* Two-week free trial, no card.

### The finding that reframes the question `[PRIMARY]`

**Marky already ships a Claude Cowork plugin and an MCP server.**

| | |
|---|---|
| MCP | `https://api.mymarky.ai/api/mcp` |
| Marketplace | `Marky-Team/marky-skills` |
| Install | Customize → Plugins → add marketplace → add plugin → Connect |
| License | **Apache-2.0** |
| Version | 0.16.1 · **16 skills** |
| Cost | *"Free while in beta"* |
| REST | `https://api.mymarky.ai`, bearer `mk_live_…` |

They built the same distribution shape we did, and they were there first. Their
skills: `build-brand-kit`, `plan-social-content`, `suggest-topics`,
`create-post-graphic`, `create-post-carousel`, `create-post-video`,
`create-post-clips`, `create-post-countdown`, `create-post-from-image`,
`create-post-variations`, `schedule-posts`, `review-performance`, `manage-library`,
`humanize`, `marky-api`, `get-started`.

**They also have a `humanize` skill** — same Wikipedia lineage as the one we looked
at, scored 0–100 with per-pattern deductions, shipping at 90+. Convergent with ours.

### What the content style actually is, and it is not what she thinks `[PRIMARY]`

The style she admired is `create-post-graphic`, and its whole premise is a refusal:

> *"you author real HTML/CSS (**no AI image generation, no stock**), style it from the
> business's brand settings, render it headlessly, look at it, and attach it."*
>
> *"Generated imagery reads as filler and cannot hold exact text. A diagram is mostly
> **text in the right places**, and HTML is the strongest layout tool an agent has."*

Six archetypes matched to what the post *does*: **layers · flow · loop · quote+stat ·
sequence · steps.** Hard rules — 1080×1350, nothing under 25px type, one accent hue,
direct labels not legends, 5th-grade copy, *"numbers must be real, never invent a
stat to fill a slot."* And an inspect step: *"never ship a render you have not looked
at."*

**So the answer to "AI content looks too AI" is not better photos. It is fewer
photos** — designed typographic cards carrying real words in real brand colours.

### The catch that matters most to us `[PRIMARY]`

Their own renderer **does not work in Cowork**, and they say so:

> *"Some agent sandboxes (e.g. Cowork) have no Chrome/Chromium binary, no way to
> install one, and restricted network egress — so both local rendering and a
> Puppeteer/Chromium download fail."*

Their fallback is Marky's server-side media. **Ours is Canva**, which does work in
Cowork and which she already pays for. The *design thinking* transfers; the
*rendering mechanism* does not, and does not need to.

---

## Part 2 — Photo libraries

### The licences, from the licences `[PRIMARY]`

| | Unsplash | Pexels | Pixabay |
|---|---|---|---|
| API | `api.unsplash.com` | `api.pexels.com/v1` | `pixabay.com/api` |
| Free limit | 50/hr demo · 1,000/hr approved | 200/hr · 20,000/mo | 100 per 60s |
| Commercial | ✅ | ✅ | ✅ |
| Attribution | not required | not required | not required |
| Agency client work | ✅ explicitly | ✅ | ✅ |

**Prohibitions that bite us:**

- **Pexels:** *"Don't imply endorsement of your product by people or brands on the
  imagery."* · *"Identifiable people may not appear in a bad light."*
- **Pixabay:** *"You cannot use Content in a misleading or deceptive way"* and *"in
  any immoral or illegal way, especially Content which features recognisable
  people."*
- **Unsplash:** cannot *"compile images to replicate a similar or competing
  service"* — irrelevant to us, we are not building a stock site.

None of the three forbids what we would do. **All three forbid what a careless
childcare post would do.**

### Why stock is the wrong default for this client specifically `[SECONDARY]`

- A Florida Extension study found **natural photos significantly out-engaged stock**
  in social posts.
- Stock fails local service businesses on the four things that actually convert:
  **proof of presence, trust signals, differentiation, and local relevance.** Every
  agency using the same polished library looks like the same agency.
- For childcare the mismatch is sharpest, because parents are reading for safety and
  legitimacy, and a generic smiling-child photo is evidence of nothing.

### The legal wall around stock children `[SECONDARY]`

- A recognisable child in commercial content needs a **model release signed by a
  parent or guardian** — Shutterstock, Adobe and Getty all say so.
- Using a stock child so it reads as *your* enrolled family is **misleading**, which
  Pixabay's licence forbids outright and Pexels' endorsement clause reaches.
- Getty requires sensitive-context use to be labelled *"illustrative purposes only …
  the person is a model."* A childcare ad is exactly that context.

**So: never a stock child. Not as a shortcut, not "just this once."** It is the one
place where the licence risk, the ethical risk and the marketing failure all point
the same way — and our own guardrails already ban AI children for the same reason.

### Where stock genuinely earns its place

Everything with **no people in it**: blocks and toys on a rug, a tidy playroom, books,
a kitchen table, crayons, a stroller in a hallway, seasonal and weather shots, local
landmarks, and backgrounds for quote cards. Zero release risk, zero deception risk,
and it fills the gap on the weeks she has no new photos.

### Delivery is already solved, twice `[PRIMARY]`

- **Canva** `upload-asset-from-url` — all plans, brings an image in by public URL
- **Zernio** fetches external URLs server-side, past the sandbox egress limit
  (verified with a raw.githubusercontent.com URL)

So a Pexels image URL reaches a post today with **no new component**. What is missing
is only *search*.

### Search, and the honest constraint `[PRIMARY]` + `[UNVERIFIED]`

Cowork's sandbox routes all egress through a mandatory allow-list proxy, so a skill
running `curl api.pexels.com` may simply be blocked — **unverified either way.** An
MCP connector is not subject to that, since it is called through Claude's connector
infrastructure rather than the sandbox network.

Every stock-photo MCP server found is **community-built and unofficial**
(`jeanpfs/stock-images-mcp`, `xcollantes/free-stock-images-mcp`,
`VictorNain26/pexels-mcp-server`, plus a third-party-hosted Pexels endpoint). Putting
an unaffiliated server into a paying childcare client's Cowork means that operator
sees every query and sits in the trust path. **Not acceptable without a review we
have not done.**

---

## The order of preference this produces

1. **Her own photos.** The research is unambiguous and onboarding now collects them.
2. **A designed card — no photo at all.** Marky's insight, rendered through Canva.
   Quote + stat, numbered steps, a typographic headline in her colours.
3. **Stock, no people.** Texture, objects, places, backgrounds.
4. **Stock with adults, carefully.** Never implying they are her caregivers or
   families.
5. **Stock with children.** Never.
