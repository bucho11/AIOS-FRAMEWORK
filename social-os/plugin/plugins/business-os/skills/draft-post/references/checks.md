# Checks — draft-post

Run every one before the packet is staged, and write the evidence report into the
packet. Contract, severity tiers and report format:
`${CLAUDE_PLUGIN_ROOT}/shared/proof.md`.

Two of these are **blocking**. Both are the kind of mistake that ends an account or
starts a lawsuit for a childcare business, and neither is recoverable by apologising
afterwards.

---

### 1 · Banned claims
**Tier:** blocking
**Evidence:** the caption, first comment and alt text, matched against the banned
list — *licensed · certified · accredited · bonded · insured · guaranteed ·
100% safe · zero risk · vetted by the state*
**Fails when:** any of those words appears **and** that exact claim is not written in
`Told to us/What we offer`
**Report as:** the word, where it appeared, and whether it was found in
`What we offer` — quote the line if found

A claim she has actually earned is fine and should be used. A claim nobody wrote
down is a regulatory problem wearing marketing copy.

### 2 · Child imagery and releases
**Tier:** blocking
**Evidence:** the media attached to this packet, and the files in
`2 — Brand Assets/Photo releases/`
**Fails when:** the media shows an identifiable child's face **and** no file in
`Photo releases/` names that family — **or** the image is AI-generated and depicts a
child, which is never allowed regardless of releases
**Report as:** the media filename, and either the release file that covers it or
`no release found for "<family>"`

An unreadable releases folder is `could not check`, not a pass. Do not stage on a
`could not check` here — ask.

### 3 · Worker classification
**Tier:** blocking
**Evidence:** the caption and first comment
**Fails when:** the copy describes caregivers as contractors, 1099, self-employed,
freelance, or "your own boss" in a way that implies they are not employees
**Report as:** the phrase and its sentence

This is a wage-and-hour exposure, not a wording preference.

### 4 · Fact check
**Tier:** needs-a-look
**Evidence:** every price, rate, timeframe, service name, ratio and number in the
caption, matched against `Told to us/What we offer` and `About the business`
**Fails when:** a stated fact does not appear in either document
**Report as:** the claim, and the line it was found on — or `not found`

This is the check that catches a price the brain never knew changed. It is
needs-a-look rather than blocking because she is allowed to know something the
document doesn't yet — and when she approves anyway, that is the signal to update
`What we offer` (`update-the-brain`).

### 5 · Caption length
**Tier:** needs-a-look
**Evidence:** character count per platform, against the platform's limit
**Fails when:** over the limit, or under 50 characters
**Report as:** `1,840 of 2,200`

### 6 · Hashtags
**Tier:** needs-a-look
**Evidence:** the hashtags in the first comment
**Fails when:** the count falls outside 3–5, or a tag is not in the local set the
brain has learned
**Report as:** the count and the tags

### 7 · Alt text
**Tier:** needs-a-look
**Evidence:** the packet's alt text field
**Fails when:** missing, empty, or under 20 characters
**Report as:** present with its length, or `missing`

Accessibility, and it is also how the platform understands the image.

### 8 · One call to action
**Tier:** needs-a-look
**Evidence:** the caption's closing lines
**Fails when:** there is no call to action, or more than one distinct ask
**Report as:** the CTA found, or `none` / `two: "DM us" and "call today"`

### 9 · Audience named
**Tier:** informational
**Evidence:** the packet's audience field, against `Told to us/Who we talk to`
**Fails when:** the packet does not say whether this post is for families or for
caregivers
**Report as:** the audience

Both audiences matter and the mix is what `plan-week` balances. An unlabelled post
is invisible to that balance.

### 10 · Hook carries the market
**Tier:** informational
**Evidence:** the first 125 characters
**Fails when:** the market or city name from `About the business` does not appear
**Report as:** the first 125 characters

---

## If a check cannot run

The brain document could not be read, the releases folder returned an error, the
media is not attached yet. Report `SKIP` with the reason and surface it like a
needs-a-look. **Never a pass.** A swallowed error is how a proof layer becomes
decoration.

## When a blocking check fails

Do not stage the packet. Say what failed, with the evidence, and offer the nearest
version that would pass:

> ⛔ I can't stage this one — there's no photo release on file for the Ruiz family.
> Want me to use the hands-and-toys framing instead? That version needs no release
> and it's been our second-best performer.

She can override, in words, and the override goes into the evidence report with her
reason and the date. An override is a decision, and decisions are recorded.

---

# Sounds-human checks (11–17)

The reader's first question is not *is this true* but *did a person write this* — and
for a childcare brand those are the same question, because trust is the product. Why
this layer exists, the evidence behind it, and **the trap**:
`${CLAUDE_PLUGIN_ROOT}/shared/sounds-human.md`.

**None of these block.** They are style, and blocking is reserved for what ends an
account. They are needs-a-look, which under the fix-then-re-run rule means **you fix
them and she never sees them** — the report records what was caught.

The deeper structural work is `business-os:sounds-human`. These are the mechanically
checkable slice.

### 11 · The antithesis cadence
**Tier:** needs-a-look
**Evidence:** the caption and first comment, matched for negate-then-assert
**Fails when:** any of these shapes appears —

| Shape | Example |
|---|---|
| `it's not just X, it's Y` | It's not just childcare, it's peace of mind |
| **contracted: `isn't / aren't / wasn't just X, it's Y`** | This **isn't** just childcare, it's peace of mind |
| **closer other than `it's`** | That's not just a nanny, **that's** a partner |
| `not only X, but Y` | Not only do we screen, but we train |
| `not because X. Because Y.` | Not because it's easy. Because it matters |

**Report as:** the sentence and which shape

**The contracted forms are the ones that get missed**, and they are the common ones in
social copy, which runs on contractions. Measured against a published scanner for this
exact tell: it caught `It's not just X, it's Y` and `Not only X, but Y`, and missed
all three of `isn't just`, `It isn't just`, and a `that's` closer — three of five
realistic variants. A regex anchored on the literal string `not just` cannot see
`isn't`, because the letters *n-o-t* do not occur in it. **Read for the shape, not
the string.**

**Fix:** lead with the real claim and drop the negation. The negation is almost always
there to inflate a thin point, so if what remains is thin, that is the actual problem.

### 12 · Hype vocabulary
**Tier:** needs-a-look
**Evidence:** the caption, first comment and alt text
**Fails when:** any of — *transform your · supercharge · unleash · effortlessly ·
unlock your potential · dive in · deep dive · delve · elevate your · in today's
fast-paced world · game-changer · revolutionary · world-class · cutting-edge ·
best-in-class · take it to the next level · reimagined · seamless · empower*
**Report as:** the word and its sentence

**Fix:** write what the thing literally does. *"Supercharge your search"* says nothing;
*"most families meet three candidates in the first week"* says something checkable —
and it doubles as a fact that check 4 can then verify.

### 13 · Em dash density
**Tier:** needs-a-look
**Evidence:** count of em dashes between words in the caption and first comment
**Fails when:** more than one in a caption under 200 words
**Report as:** the count and each sentence

The single most-cited "a machine wrote this" writing tell, above any vocabulary word.
**Fix:** a comma, a full stop, or brackets. Not a colon — readers flag that as the
same reflex in a different hat.

**One may stay if `Brand voice` says it is hers**, or if an approved example in the
room uses the same pause. Her voice outranks the tell; say which you kept and why.

**This check does not apply to internal documents.** Our own folder names contain em
dashes (`1 — Brain`, `3 — Social`), so run this against captions only. Measured: a
scan of our own client-facing seed documents returned 13 hits, every one a folder
name.

### 14 · Sycophancy and signposting
**Tier:** needs-a-look
**Evidence:** the opening and closing lines
**Fails when:** the copy opens with *great question · I hope this helps · of course ·
absolutely* or closes with *in conclusion · in summary · at the end of the day ·
ultimately*
**Report as:** the phrase and where it sat

A wrap-up line restating what the reader just read is the written form of the stated
lesson — audit 1 in `sounds-human`.

### 15 · Emotion performed through the body
**Tier:** needs-a-look
**Evidence:** every emotional moment in the caption
**Fails when:** more than one renders feeling physically rather than naming it —
*chest tightened · breath caught · heart sank · a knot in her stomach · swallowed
hard · hands shaking · something shifted · a weight lifted*
**Report as:** each instance

**The largest human-AI gap in the research: 81% of AI text against 38% of human.**
And the one this brand is most exposed to, because caregiver stories are written under
"show, don't tell" by reflex — which the data now says is a machine signature.

**Fix:** name the feeling. *"honestly, that first day scared her."* One earned
embodied moment per post is fine; it is the default that fails.

### 16 · Vague allusion where a name belongs
**Tier:** needs-a-look
**Evidence:** the caption's claims and references
**Fails when:** it contains *experts say · studies show · research shows · a popular
book · a well-known approach · some parents say · it's often said · recently* without
naming the thing
**Report as:** the phrase

Humans name real things at **47% against 24%**. **Fix:** name it, date it, price it —
or cut it. Then run the new specific past check 4, because anything specific enough to
name is specific enough to be wrong.

### 17 · Shape convergence
**Tier:** informational
**Evidence:** the last three packets in `4 Published/` — opener type, arc, emotion
mode, closer, CTA shape
**Fails when:** this draft's skeleton matches all three
**Report as:** the shared skeleton

**The audit we can run better than almost anyone**, because the corpus is on disk with
its packets. Informational rather than needs-a-look because the fix is a rewrite, not
an edit — hand it to `business-os:sounds-human` rather than patching it here.

**And apply it to the fix, too.** If every post now opens mid-scene and ends
unresolved, that is a new fingerprint. **Rarity is the signal; a uniformly applied
checklist destroys it.**
