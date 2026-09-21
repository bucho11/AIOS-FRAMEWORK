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

### OQ-017 — Does Cowork substitute `${CLAUDE_PLUGIN_ROOT}` in skill content?
**Status:** open. **Mitigated, not blocking.**
**Known `[PRIMARY]`:** Anthropic documents `${CLAUDE_PLUGIN_ROOT}`,
`${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}` and `${CLAUDE_PLUGIN_DATA}` as
substituted in skill and agent content — described in the **Claude Code** docs.
Cowork is a different surface and the substitution is not separately documented there.
**Mitigation already shipped (DEC-024):** the four hard safety rules are inlined in
`draft-post`, `make-graphic` and `publish`, so a substitution failure costs depth,
never safety. `brand-onboarding`'s templates now live in its own `assets/`, which
resolves by plain relative path regardless.
**Test:** on the first real onboarding, ask Claude to quote a line from
`${CLAUDE_PLUGIN_ROOT}/shared/guardrails.md`. If it cannot, the fallback is to move
`shared/` content into each skill's own `references/` and accept the duplication.


### OQ-018 — Is there a length limit on Cowork Project instructions?
**Status:** open, low risk. **Blocks:** nothing; worth knowing before scaling.
Anthropic's Cowork Projects documentation describes project instructions as
"standing guidance applied to every session in the project" and **states no
character limit**. Our bootstrap block (`shared/project-instructions.md`) is ~30
lines / ~1.8 KB, which is small by any plausible ceiling — but "no documented
limit" is not "no limit," and a silently truncated bootstrap would drop rule 7
(nothing publishes without a yes) with no error.
**Test that closes it:** at the first client setup, paste the block, start a fresh
session, and ask Claude to repeat the project instructions back verbatim. Truncation
shows immediately. Thirty seconds, once.

### OQ-019 — Do Cowork Project instructions survive a plugin update or a connector re-auth?
**Status:** open, low risk. **Blocks:** nothing.
Project instructions are a Cowork project field, not plugin content, so they should
be untouched by `claude plugin update` or a Drive/Zernio re-auth. Not verified.
**Test that closes it:** after the first plugin update on a live client, open the
project's instructions and confirm the block is still there. If it ever isn't, the
bootstrap needs a check at session start — which is awkward, since the bootstrap is
what would carry that check.

### OQ-020 — Does `update-the-brain` actually fire on pushback, or only on an explicit ask?
**Status:** open, **the most important untested thing in this build**. **Blocks:**
confidence in the whole contradiction discipline.
Skills are selected by matching the user's words to the skill `description`. An
explicit "change my brand voice" will match. What is untested is whether *"why does
everything have exclamation points"* or *"I already told you"* reliably selects it,
rather than being answered conversationally. The bootstrap (rule 4) is the belt to
the description's braces, but neither is verified.
**Test that closes it:** evals 8, 9 and 11 in `evals/evals.json`, run against a real
workspace. If pushback does not select the skill, the fix is not a longer
description — it is making rule 4 of the bootstrap more explicit, since that text is
in context before any skill is chosen.

### OQ-021 — Do PERSONAL plugins on Cowork auto-update, and on what trigger?
**Status:** open. **Blocks:** nothing structural — DEC-037's manual-Update backstop
works either way — but it decides whether the operator has to tell each client to
click Update after every release.
What is verified `[PRIMARY]` applies to **organization** marketplaces: auto-sync is
opt-in per marketplace, fires when *"a pull request that includes a plugin version
bump is merged to the repository's default branch,"* and *"direct pushes to the
default branch don't trigger a sync."* The **personal plugins** help page documents
*"Add from a repository: Sync a marketplace from a GitHub repository or git URL"*
and says **nothing at all** about updating, syncing, refreshing or versions.
**Test that closes it:** install the marketplace as a personal plugin, note the
version shown, ship a MINOR release through a PR with a bump, and check the next day
whether the installed version moved without anyone clicking Update.
**Until it closes:** assume manual. The runbook tells the operator to say one
sentence to the client — *"open Plugins, find Business OS, click Update."*

### OQ-022 — Does Cowork dereference symlinks inside a plugin directory?
**Status:** open, **do not build on it**. **Blocks:** any future split into
multiple plugins (DEC-036).
Claude Code's documentation says a plugin may share files with siblings in the same
marketplace via symlinks, which are *"dereferenced"* at install. That is **Claude
Code** documentation; Cowork's plugin loader is a separate implementation and this
is unverified there. A symlink that is not dereferenced is a file reference that
resolves to nothing — the exact silent failure class of DEC-024, where every skill
ran without its guardrails and nothing errored.
**Test that closes it:** ship a throwaway two-plugin marketplace where plugin B
symlinks a file from plugin A, install it in Cowork, and ask a skill in B to read
that file.
**Until it closes:** one plugin, many rooms (DEC-036).

### OQ-023 — Has any migration ever been run, and has any rollback ever been performed?
**Status:** open. **Blocks:** confidence in DEC-038/039.
`migrations/001` is written, listed, and validated structurally. It has never been
executed, because no version-1 workspace exists to run it against. Its rollback is
documented and has never been performed. **A rollback that has never been run is a
hypothesis.**
**Test that closes it:** build a throwaway workspace in the version-1 shape by hand
(`0 — Setup`, `0 — What's Installed`, `Her preferences`), run
`business-os:upgrade-workspace` against it, confirm the plan is shown before
anything moves, confirm every superseded document is readable in `9 — Archive/`,
then perform the documented rollback and confirm the workspace returns to version 1.
Also interrupt it mid-run once and confirm the `FAILED` row lets it resume.

### OQ-024 — The four prompt texts from the Delegation Loop guide are unread
**Status:** ✅ **closed 2026-09-21** — the operator supplied all four. They produced
**thirteen hardenings** to what had been built from the topics alone (DEC-049…054),
the three sharpest being: **fix what fails and re-run before she sees anything**
(v0.4.0 only reported failures, which is a complaints department); **more than two
failures on the first pass means stop and diagnose the process** rather than patching
individually; and **the second occurrence earns a preventive rule, not a reminder** —
a note saying *"remember to…"* is an apology written down.
Also folded in: the two interview gates, the two closing questions (*what did I get
wrong* / *what did you forget to tell me*), `if X then Y` decisions, no dates or
versions in template filenames, a filled-in example under every template, *when not
to use it*, the never-save list, the active rebuild test, and never reporting a write
that failed.
**Original status text follows, for the record.**
**Status:** open, easily closed by the operator. **Blocks:** nothing built — the
architecture came through, the wording did not.
The guide body is behind an email gate. Fetching it returned the **structure and
concepts** — all eleven headings, the three layers, what each of the four prompts
does, the folder shape, the five mistakes, the loop steps, the worked example and the
eight interview topics — but declined to reproduce the text on copyright grounds.
**What is missing specifically:** the literal wording of the four prompts (one per
layer plus the correction prompt). Our `teach-it-a-job` interview was written from
the eight *topics*, not from their prompt. Theirs has been used by 30,000+ readers
and ours has been used zero times, so their phrasing is worth reading.
**Test that closes it:** the operator signs up (free) and pastes the four prompts.
Then compare against `skills/teach-it-a-job/SKILL.md` and fold in anything sharper.

### OQ-025 — No check has ever been run
**Status:** open. **Blocks:** confidence in the entire proof layer.
34 checks are written across five jobs, each with a concrete *fails when* line. None
has been executed. The failure modes that matter are not whether a check is
well-worded but whether it can actually get its evidence: can a skill reliably read
`Photo releases/` and match a family name; can it fetch a published URL from inside
Cowork's egress allow-list; does `read_file_content` on a Google Doc return text
clean enough for a verbatim claim match.
**That last one is the real risk.** The claim check and the banned-claims check both
depend on **verbatim matching against a Google Doc read back as text**. If conversion
mangles quotes, dashes or line breaks, a claim that *is* documented reads as *not
found* — and a blocking check that false-positives will be overridden habitually
within two weeks, at which point it is worse than no check.
**Test that closes it:** build a workspace, write a caption stating a price that IS in
`What we offer`, and confirm the check passes. Then change one character and confirm
it fails. Both directions, or it is not tested.

### OQ-026 — Does an override actually get recorded, and is it readable later?
**Status:** open. **Blocks:** the audit value of the proof layer.
A blocking check may be overridden in words, and the override is supposed to land in
the evidence report inside the packet, with her reason and the date. Never tested.
An override that is acted on but not written down turns the blocking tier into a
speed bump and removes the one artifact that would explain, a year later, how
something got out.
**Test that closes it:** trigger a blocking failure, override it in conversation,
then read the packet back in a fresh session and confirm the override, the reason and
the date are all there.
