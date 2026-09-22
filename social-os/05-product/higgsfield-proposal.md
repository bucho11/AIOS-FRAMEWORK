# Proposal — Higgsfield, and how we stop it looking generic

**Status:** proposal, not built. **Date:** 2026-09-22

The operator's call: try it. His concern is the right one — *"people mess this up
and get generic looks, others get crazy real looks."* That gap is not the model.
**It is the prompt**, and it is almost entirely mechanical.

---

## 1 · What we'd add

One connector and one skill.

| | |
|---|---|
| MCP | `https://mcp.higgsfield.ai/mcp` — official, first-party, verified live (401 = up, auth required) |
| Auth | browser OAuth, **no API key** |
| Skill | `make-image` — a sibling to `make-graphic`, not a replacement |

**Five tools exposed** `[PRIMARY]`:

| Tool | What it does |
|---|---|
| `generate_image` | text-to-image, 16+ models (GPT Image 2, Soul V2, Flux 2, Nano Banana Pro), to 4K |
| `generate_video` | **image-to-video** or text-to-video, ≤15s (Veo 3.1, Kling 3.0, Sora 2, Seedance 2.0, Hailuo) |
| `create_character` | trains a reusable **Soul ID** from reference images — keeps a person or product consistent across a campaign |
| `get_generation_status` | polls; **video takes 90s+** |
| `list_characters` | manages saved references |

---

## 2 · The prompt contract — this is the whole proposal

**The failure mode is writing an *aesthetic* prompt instead of a *photographic* one.**
Generic output comes from asking the model to be pretty. Real output comes from
describing a believable capture: a camera, a lens, an exposure, one light source, and
imperfection.

So the skill never accepts free text. **Every generation fills a fixed spec**, and a
missing field is a stop, not a default.

```
subject          a 30-something nanny reading to a toddler on a living-room rug
context          weekday morning, suburban Reno home, toys on the floor
camera           Sony A7R V
lens             35mm            (35 environmental · 50 natural · 85 portrait)
aperture         f/2.8
shutter          1/125s          (1/30 drift · 1/125 handheld · 1/500 frozen)
light            natural window light from camera left, overcast
stock            Kodak Portra 400
texture          visible skin texture, slight asymmetry, natural catchlights,
                 stray hair, uneven fabric folds, fine ISO grain
grade            neutral, low saturation, restrained highlights
negative         plastic skin, waxy skin, over-smoothed face, deformed hands,
                 extra fingers, unnatural symmetry, cgi, illustration,
                 oversaturated, blurry eyes, bad anatomy
```

### The banned list — these are what produce the plastic look

> **beautiful · stunning · masterpiece · ultra detailed · hyperrealistic · 4k · 8k ·
> cinematic (alone) · perfect skin · flawless · clean face · glamour shot**

They bias toward *polished beauty defaults* rather than camera realism: smoothed
skin, over-sharpened edges, overbright eyes, too-perfect symmetry. `4k` is a
resolution label, not a realism cue — it adds detail density without fixing physics.

**Replace with:** visible skin texture · natural pores · unretouched · single light
source · documentary realism · candid expression · slight asymmetry · realistic
shadow falloff.

This becomes a **check**, in the same format as the other 41: *fails when the prompt
contains a banned word, or omits camera / lens / aperture / light / negative.*

### For video, three extra fields, because motion is where uncanny lives

```
camera move      slow handheld push-in | locked-off tripod | gentle lateral dolly
blur             natural motion blur, 180-degree shutter look
continuity       same face across frames, stable clothing, consistent lighting
```

Video realism is **temporal consistency**, not per-frame prettiness. The tells are
frame-to-frame face drift, flickering textures, hand geometry that changes shape,
and background warping. `same face across frames` targets it directly.

---

## 3 · Model routing

| Job | Model | Why |
|---|---|---|
| Photo-real still of a person | **Soul V2** or **Flux 2** | strongest skin and light realism |
| Object / room / texture | any image model | no anatomy risk |
| Animate a real photo | **Kling 3.0** or **Veo 3.1**, image-to-video | best temporal stability |
| Text-to-video from nothing | **avoid for this client** | see §5 |

---

## 4 · The play that makes this actually worth it

**`create_character` trained on her own caregivers' consented reference photos.**

A Soul ID built from a real person she has a signed release for is categorically
different from a generated stranger: the subject is real, the consent is real, and
the output is *her caregiver, in her brand's world, consistent across a campaign.*

That converts Higgsfield from "fake people generator" into **a way to get twenty
usable images from one photo session** — which is the actual constraint. She can film
~2 Reels a week and shoots photos rarely.

Same for **image-to-video**: her real photo, animated. Real subject, real release,
motion added.

---

## 5 · What stays banned, and why it is not negotiable

**No AI-generated children. Ever. No exceptions, no Soul ID, no "just the back of
the head."**

This is already a blocking check (`draft-post` check 2, `make-graphic` check 1) and it
stands for three independent reasons that all survive Higgsfield being good:
a recognisable child in commercial content needs a guardian-signed release; implying
a generated child is an enrolled family is misleading; and it is the single fastest
way to lose a childcare account and the trust underneath it.

**Also banned:** generating a person and implying they are a real caregiver or a real
client. A Soul ID of a *consented, released adult* is fine. A stranger presented as
her staff is not.

**And every generated image is labelled in its packet** — `media_type: generated`,
with the model and the prompt spec stored. Not on the post; in the record. If a
question is ever asked, the answer is one lookup away.

---

## 6 · Cost

| | |
|---|---|
| Starter | $19/mo · 270 credits |
| **Plus** | **$59/mo · 1,200 credits** ← likely tier |
| Ultra | $129/mo · 3,000 credits |

`[PRIMARY]` MCP spends **plan credits**, not the developer API's dollar balance —
*"A plan neither grants API access nor changes API pricing."* The pay-as-you-go API
is a separate product ($5 min top-up; Kling 3.0 $0.112/sec, Soul 2 $0.0032/image).

**Unverified: how many credits one generation costs.** That decides whether $19 or
$59 is the right tier, and it is a 5-minute check once an account exists.

Stacked cost per client: Claude Pro ~$20 + Canva Pro ~$15 + Higgsfield $19–59.

---

## 7 · Build plan

1. `shared/generated-imagery.md` — the prompt contract, banned list, model routing,
   and the labelling rule
2. `skills/make-image/SKILL.md` — spec → generate → **poll** → inspect → upload
3. `skills/make-image/references/checks.md` — the prompt check, the no-children
   check (blocking), the no-false-staff check (blocking), the inspect-before-ship
   check
4. `.mcp.json` — add the Higgsfield server
5. Room + map + evals + CHANGELOG, as every release
6. **Order of preference updated:** her own photos → designed card → *animated real
   photo* → *generated non-people* → stock no-people → never a child

**Not built until approved.**

## Open questions

- **Credits per generation** — decides the tier
- **Does OAuth complete in Cowork?** Zernio's did; unverified here
- **Does `create_character` need a paid tier?** unverified
- **Polling in Cowork** — video takes 90s+; whether a session holds that cleanly is
  unverified, and it is the most likely practical friction
