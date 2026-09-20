---
name: publish
description: >
  The only skill that talks to the publishing vendor. Turns an approved post packet
  into a scheduled Instagram and Facebook post: exports the Canva design if there
  is one, resolves media, validates it, checks the Instagram daily quota, creates
  or promotes the Zernio post with the exact publish time, records the vendor id,
  and moves the packet through 3 Approved → 4 Published. Also hands the owner an
  upload link for her own photos and Reels, retries failed posts, and reports
  status. Use whenever the owner says the approval word ("approve <post>"),
  "schedule this", "post it", "what's scheduled", "did it go out", "retry",
  "reschedule", or "cancel that post". Never publishes without the owner's explicit
  approval in the current conversation.
---

# Publish

Everything upstream is vendor-neutral. This file is where the vendor lives. If the
publisher ever changes, this file changes and nothing else does.

Read `../../shared/post-packet.md`, `../../shared/guardrails.md`, and
`references/zernio-cheatsheet.md` (tool names, fields, limits — all verified).
Read `0 — Setup` for `timezone`, profile and account ids, and the approval word.

## The gate

A post moves only when the owner has used the approval word **in this
conversation**, naming the post. Approval of a plan is not approval of a post.
`publish_now` is used only when she literally asks to post right now. If
`compliance-reviewer` left issues in the packet's `## Compliance check`, surface
them and stop — she can override, but only explicitly.

## Approve → schedule

1. **Find the packet** in `2 Drafts/` by title. Read it.
2. **Resolve media.**
   - `media_source: canva` → `export-design` now (PNG; lossless on Pro) for each
     size the post needs. Export URLs are signed and short-lived — go straight to
     step 3, never park them.
   - `media_source: owner-upload` → `media_generate_upload_link`; give her the link
     ("drop the photo or Reel here, it's good for 30 minutes"); when she says done,
     `media_check_upload_status(token)` → `media_urls`. Uploads live 7 days in
     temp storage and are made permanent when the post publishes, so the publish
     time must be within 7 days.
   - Reject Google Drive / Dropbox links outright — they return HTML, not the file.
3. **Validate.** `call_tool` the media validator with each URL (checks reachability,
   type, and per-platform size). Fix before continuing.
4. **Quota.** For Instagram, read the publishing limit for the account and compare
   `quotaUsage` to `quotaTotal` (never hardcode a number). Near the cap → propose a
   later time.
5. **Create or promote.**
   - If no `vendor_post_id`: `posts_create` — content, `platform`/`account_id` for
     each target (or `posts_cross_post`), `media_urls`, and scheduling. For exact
     times use the REST shape through `call_tool` with `scheduledFor` + the Setup
     `timezone`; `schedule_minutes` is fine for "in an hour". Put the packet's Drive
     file ID in `metadata` — that is our primary key.
   - If a Zernio **draft** already exists: promote with `isDraft: false` **and**
     `scheduledFor`. Sending only `scheduledFor` returns 200 and leaves it a draft —
     this is the single most common silent failure.
   - Instagram extras go in `platformSpecificData`: `firstComment` (links and
     hashtags), `locationId` (numeric Page id with location), `contentType:
     "story"` for Stories, `shareToFeed`, `isAiGenerated` when relevant.
   - Send a fresh UUID as `x-request-id`. If Zernio answers **409**, identical
     content already went to that account within 24 hours — don't retry; tell her.
   - Refused for an ambiguous account → `accounts_list`, pick the right id, retry.
6. **Record.** Replace the packet with `status: scheduled`, `vendor_post_id`,
   `media_urls`, `approval: approved by <name> on <date>`; move it to `3 Approved/`.
7. **Confirm** in one line: what, where, when (her local time).

## After publish

- `posts_get` shows `published` → replace packet with `published_urls`, move to
  `4 Published/`.
- `failed` → keep in `3 Approved/`, set `status: failed` with Zernio's reason.
  `ACCOUNT_DISCONNECTED` means a token expired (Facebook does this often): give her
  the reconnect link via the connect endpoint and retry after. A dead media URL
  means re-export and `posts_update`. Otherwise `posts_retry`.
- `posts_list status=failed` and `posts_list_failed` are the weekly sweep;
  `learn` runs them.

## Status questions

"What's scheduled?" → `posts_list status=scheduled` for her profile, in her
timezone. "Cancel" → `posts_delete` and move the packet back to `2 Drafts/`.
"Reschedule" → `posts_update` with the new `scheduledFor`.

## Comment-to-DM automations

When a post's CTA is "DM CARE", offer to create the matching automation so the
promise is kept automatically: `call_tool` create-comment-automation with
`profileId`, `accountId`, `name`, `keywords: ["CARE"]`, `matchMode: "word"`,
`typoTolerance: true`, `alsoMatchInDms: true`, a warm `dmMessage` in her voice
(≤ 640 chars if buttons), optional `commentReply`. One automation per keyword; they
stack account-wide.

## Rules

- Approval word, in this conversation, naming the post — or nothing moves.
- Never `publish_now` unless she asked for now.
- Never schedule > 7 days after a Zernio upload.
- Never pass a Drive link as media.
- Never store an API key anywhere in Drive.
