# Open questions

> Unknowns that gate the build. **Each carries the exact test that closes it.**
> Never build on an open question — either close it, or write the assumption
> into the design where it can be seen.
>
> When you close one, move the finding to the relevant research file, record it
> in `VERIFIED-FACTS.md`, and delete the entry here.

---

## Blocking the build

### OQ-001 — Does Composio's managed Meta OAuth actually publish?
**Status:** substantially closed, not proven. **Blocks:** the Composio fallback path.
**What we know `[PRIMARY]`:** the managed Instagram config requests
`instagram_business_content_publish`; the managed Facebook config requests
`pages_manage_posts` + `business_management`. A managed app requesting a scope it
was never granted would be a broken product.
**What remains:** requesting a scope ≠ Meta having granted Advanced Access.
**Test:** connect a **throwaway IG Business account** via Composio managed OAuth,
then (a) call `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` — a 200 with a quota
payload means business scope is live; (b) `INSTAGRAM_POST_IG_USER_MEDIA` with a
public HTTPS image URL, then `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`.
**Not blocking launch** if DEC-005 (Ayrshare) is confirmed.

### OQ-002 — Is her Instagram a Business/Creator account, linked to the Facebook Page?
**Status:** open. **Blocks:** everything.
**Why:** Composio and every vendor reject personal accounts `[PRIMARY]`.
**Test:** ask her, or look at the account. If personal, converting it is step zero.

### OQ-003 — Does Bannerbear's $49 tier return a usable hosted public URL?
**Status:** open. **Blocks:** DEC-006 cost.
**Why:** API docs show hosted output (`https://images.bannerbear.com/...`) as
standard, but "Instant URLs" are a **Scale-tier ($149)** feature. Need to confirm
the standard hosted URL on Automate is permanent and publicly fetchable.
**Test:** free trial (30 credits). Generate one image, take the returned URL,
`curl -I` it from an unauthenticated context, confirm 200 + `image/png` and no
redirect. Then feed that exact URL to a real IG media-container call.

### OQ-004 — Which market/franchise is the client, and whose IG does she post to?
**Status:** open. **Blocks:** the whole setup shape.
**Why:** if she posts to the **main brand account**, this is a corporate-level
build with approval politics. If she has her **own location account**, it is the
clean franchise case we designed for.
**Test:** ask.

### OQ-005 — Is there a photo/video release process for client families?
**Status:** open. **Blocks:** any imagery containing real children.
**Why:** COPPA. A release must name platforms, duration, and **paid advertising**
explicitly. This is a business process, not a software feature.
**Test:** ask. If none exists, the default visual language (no faces) is not a
limitation — it ships as the standard and is the better strategy anyway.

## Verify before spending money

### OQ-006 — Confirm Ayrshare's current pricing and profile definition
All Ayrshare prices here are `[SECONDARY]`. Confirm on ayrshare.com before quoting
a client. Specifically: what counts as one "social profile", and how many social
accounts a profile holds.

### OQ-007 — Confirm the Instagram daily publish cap
Sources conflict: 25 vs 50 per rolling 24h. **Design for 25.** Read the current
Meta doc, and prefer the runtime quota call over any number in a document.

### OQ-008 — Confirm Facebook's `scheduled_publish_time` window
Reported 10 minutes – 75 days; older guides say 30 days. Read Meta's current
Page/feed reference.
