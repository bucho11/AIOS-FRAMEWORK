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

### OQ-009 — Does Zernio's free tier actually publish, and does its MCP expose publish tools?
**Status:** open. **Blocks:** the whole launch stack (DEC-010).
**Why it matters:** this is now the single gate on the build. Everything else is
verified.
**What we know `[PRIMARY]`:** pricing page states 2 free accounts, full API,
webhooks, unlimited posts, no feature tiers. `docs.zernio.com` documents
`POST /v1/posts` with `scheduledFor` / `publishNow`. MCP endpoint
`https://mcp.zernio.com/mcp` returns **401** — live, auth required.
**What is unverified:** the MCP's actual tool list, direct media upload + hosted
public URL `[SECONDARY]`, and a real IG publish on the free tier.
**Test (≈10 minutes, free, no card):**
1. Sign up at zernio.com, connect **1 Instagram Business** + **1 Facebook Page**.
   Confirm that reads as 2 accounts and stays $0.
2. Copy the API key (`sk_…`).
3. Probe the MCP tool list:
   ```bash
   curl -sS -X POST https://mcp.zernio.com/mcp \
     -H "Authorization: Bearer $ZERNIO_API_KEY" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json, text/event-stream" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
   ```
   Looking for: create/schedule post, media upload, post status, accounts.
4. Upload one image via the media endpoint — **confirm it returns a public HTTPS
   URL** and that `curl -I` on that URL gives `200` + an image content-type with
   no redirect and no auth.
5. Schedule one real IG post ~15 min out. Confirm it publishes.
6. Deliberately break a media URL and confirm the error is legible, not silent.
**If it fails:** fall back to Composio (free, verified publish scopes, but Cowork's
hourly task owns the Instagram clock), or Ayrshare at $149/mo.

### OQ-010 — Does Cowork's custom-connector OAuth complete against Zernio?
**Status:** open. **Blocks:** whether she can self-connect without an API key.
**Why:** Zernio's official plugin documents the browser sign-in flow for **Claude
Code**, not Cowork. Zernio advertises OAuth 2.1 + PKCE + dynamic client
registration, which is exactly what Claude's custom-connector flow needs, so it
should work — but "should" is not verified.
**Test:** in Cowork → Customize → Connectors → Add custom connector →
`https://mcp.zernio.com/mcp` → confirm it opens Zernio's consent screen and
connects. If OAuth fails, fall back to the API-key header, which is documented
and definitely works.
**Impact if it fails:** the operator pastes an API key during setup instead of
her clicking sign-in. Slightly worse onboarding, not a blocker.

### OQ-011 — Which Claude account and GitHub org own this venture long-term?
**Status:** open. **Blocks:** nothing today; gets expensive to change later.
**Why:** the Claude account and repo currently in use are employer-associated
(`@hideitmounts.com`). DEC-013 removed the Drive exposure, but the plugin the
clients install, the skills, and this repo are the venture's IP and currently sit
in employer-adjacent homes. Skills on Pro are personal to an account and cannot be
shared person-to-person `[PRIMARY]`, so whichever Claude account publishes the
plugin marketplace is structurally the owner.
**Decide before:** publishing the plugin marketplace publicly, or onboarding the
first paying client.
**Cost of moving later:** every franchise would need to re-install from a new
marketplace URL.

### OQ-012 — Public or private marketplace repo?
**Status:** open. **Decide before:** the first client install.
**Why it matters:** `[SECONDARY]` private marketplace auth runs through org
GitHub App connections or local git credentials — documented for Claude Code and
org settings, **not** verified for an individual **Pro** user syncing a private
repo in Cowork. A private repo may put a credential step in front of a
non-technical client, or may not work at all on Pro.
**Leaning:** public. The plugin is instructions; the client's data lives in her
Drive and stays private either way. A public repo also markets itself.
**Counter:** it publishes the childcare guardrails and domain logic.
**Test if private is wanted:** create a private repo with a minimal
`marketplace.json`, then try **Customize → Plugins → Add marketplace → Add from a
repository** as a Pro user and see whether it authenticates.
**Cost of changing later:** every franchise re-installs from a new URL.

### OQ-013 — What does the Canva MCP return on export, and does it hand off cleanly to Zernio?
**Status:** open. **Blocks:** the `make-graphic` skill, not the rest of the build.
**Why:** DEC-019 routes Canva exports through Zernio's presign upload so the media
URL is durable. Unverified: whether the Canva MCP's export returns a fetchable URL
or binary content, and whether Claude can move it to Zernio without a manual
download/upload step by the user.
**Test:** with Canva Pro connected, ask Claude to create → resize → export a
design, inspect what comes back, then feed it to Zernio
`media_generate_upload_link` and confirm a permanent `publicUrl`.
**Fallback if the handoff is manual:** Canva export lands in her Drive, and the
publish skill picks it up from `3 Approved/` — one extra hop, still automatic.

### OQ-013 (refined) — Does Zernio fetch an external media URL at post creation or at publish?
**Status:** open. **Blocks:** far-out scheduling of Canva graphics only.
**Known `[PRIMARY]`:** Zernio uploads sit in temp storage 7 days and are copied to
permanent storage on publish. External `mediaItems.url` must be public HTTPS
returning the file. Canva export URLs are signed and expire (TTL undocumented).
**Test:** approve a Canva-graphic post scheduled 3 days out; after 2 hours run
`validate_media` on the Canva URL (expect expired) and `posts_get` on the Zernio
post; at publish time confirm success or `post.failed` reason.
**If it fails:** publish skill switches Canva posts to "export → owner drops the PNG
into the Zernio upload link" or schedules Canva posts ≤ 1 hour out.

### OQ-014 — Does the plugin's PreToolUse `prompt` hook fire in Cowork, and what is the bundled MCP tool name?
**Status:** open. **Blocks:** nothing — the hook is defence in depth (DEC-022).
**Known `[PRIMARY]`:** hooks run in Cowork; matcher form is `mcp__<server>__<tool>`;
`prompt`-type hooks return `hookSpecificOutput.permissionDecision`. Unknown: whether
a plugin-bundled server's tools are named `mcp__zernio__…` or namespaced; hence the
regex matcher `mcp__.*zernio.*__posts_(create|publish_now|cross_post|update)`.
**Test:** in Cowork with the plugin installed, ask Claude to list tool names, then
attempt `posts_publish_now` without approval and see whether the hook denies.

### OQ-015 — Can Cowork's Drive connector read a `.md` created with conversion disabled?
**Status:** designed around (DEC-020) — brain files are Google Docs regardless.
**Test if curious:** `create_file` with `disableConversionToGoogleType: true` and
`text/markdown`, then `read_file_content` and `download_file_content`.

### OQ-016 — The test Instagram account must be Business or Creator
**Status:** open, operator action. **Blocks:** `OQ-009` (the live publish test).
**Why `[PRIMARY]`, Zernio's Instagram page, verbatim:** *"Instagram requires a
Business or Creator account; personal accounts cannot post through the API."* Their
unsupported list names *"Posting to personal accounts (Business or Creator only)."*
Facebook likewise: *"Facebook requires a Page; personal profiles cannot post through
the API."*
**Consequence:** a personal Instagram may connect to Zernio for read access and
still fail every publish. `accounts/health` → `canPost: false` is the tell.
**Fix (free, ~30 seconds, reversible):** Instagram app → Settings → Account type
and tools → Switch to professional account → **Creator** is enough; Business also
works. No Facebook Page required when connected with Instagram Login.
**Run `social-os/tools/verify-zernio.sh` to see `canPost` before assuming.**


---

## Closed

- **OQ-009 — does Zernio publish?** ✅ 2026-09-21. Live account verified: auth, two
  healthy accounts with `canPost: true`, live quota 100, full media upload
  round-trip, and a real cross-posted `validate_post` returning
  `{"valid": true}`. Nothing published.
- **OQ-013 — Canva → Zernio handoff.** ✅ 2026-09-21. Zernio fetches external URLs
  **server-side**, proven with a `raw.githubusercontent.com` URL. A live Canva export
  URL can be passed directly as `mediaItems[].url`. The publish skill now does
  export → validate → create in one unbroken pass, and falls back to the Zernio
  upload link for schedules more than a few hours out.
- **OQ-016 — Instagram account type.** ✅ 2026-09-21. Switched to **Creator**;
  `accounts/health` reports `canPost: true`. The fix is free and reversible.

**Still open:** OQ-011 (owning GitHub account) · OQ-012 (public vs private repo) ·
OQ-014 (does the PreToolUse hook fire in Cowork) · OQ-015 (Drive `.md` read-back,
designed around).
