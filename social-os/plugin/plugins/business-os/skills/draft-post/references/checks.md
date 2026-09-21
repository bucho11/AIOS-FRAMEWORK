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
