# Checks — make-graphic

A graphic is the one output nobody re-reads before it goes out, because it looks
finished. Contract: `${CLAUDE_PLUGIN_ROOT}/shared/proof.md`.

---

### 1 · No child's face without a release
**Tier:** blocking
**Evidence:** every image placed into the design, and
`2 — Brand Assets/Photo releases/`
**Fails when:** a placed photo shows an identifiable child's face and no release
names that family — or any element depicting a child was AI-generated
**Report as:** the asset, and the release covering it or `none found`

Same rule as the caption path, checked again here, because a graphic can pick up a
photo the caption never mentioned.

### 2 · The export resolves
**Tier:** blocking
**Evidence:** an HTTP request to the export URL
**Fails when:** it does not return an image, or it has already expired
**Report as:** the URL's status and content type

Export URLs are signed and expire. A scheduled post pointing at an expired URL fails
at publish time, quietly, when nobody is watching. **Export at approval time, not at
draft time**, and re-check here.

### 3 · Brand colours
**Tier:** needs-a-look
**Evidence:** the hex values used in the design, against
`Told to us/Colors and fonts`
**Fails when:** a colour is used that is not in that document and is not a neutral
**Report as:** each colour used, and whether it was found

This document mirrors her Canva Brand Kit and adds the rules a Brand Kit cannot hold.
Check against the document rather than the Brand Kit, because it is the one source
every room shares — email and print have no Canva to read from.

### 4 · Dimensions match the destination
**Tier:** needs-a-look
**Evidence:** the exported dimensions, against the platform and placement in the
packet
**Fails when:** the aspect ratio is wrong for where it is going
**Report as:** the dimensions and the expected ratio

### 5 · Text fits
**Tier:** needs-a-look
**Evidence:** the text elements after substitution
**Fails when:** a replaced string is longer than the element it went into, or any
placeholder remains unsubstituted
**Report as:** each element and its final text

An unreplaced `{{business_name}}` on a published graphic is the most embarrassing
possible failure and it is entirely mechanical to catch.

### 6 · Claims on the image count as claims
**Tier:** blocking
**Evidence:** every word rendered into the graphic
**Fails when:** it contains a banned claim that is not written in
`Told to us/What we offer` — the same list the caption is checked against
**Report as:** the word and the element it was in

Text baked into an image is not reviewed by the caption checks. It is the obvious
gap, so it is closed here explicitly.
