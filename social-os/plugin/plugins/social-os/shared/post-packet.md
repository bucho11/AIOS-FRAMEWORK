# The post packet — the neutral object every skill hands to `publish`

A post packet is **one Google Doc** in `3 — Content/`. It is the post's identity:
its Drive file ID is our `post_id`, and it moves `2 Drafts → 3 Approved → 4 Published`.

**Nothing in a packet names a publishing vendor.** That is the swap seam. `draft-post`
and `make-graphic` write packets; only `publish` knows what Zernio is. Changing
publishers later edits one skill and zero packets.

## Title

`YYYY-MM-DD — <platforms> — <pillar> — <short hook>`
e.g. `2026-10-02 — IG+FB — Trust & vetting — How we screen every nanny`

## Body (plain `key: value` lines, then free sections)

```
status: draft | approved | scheduled | published | failed
pillar: <one of the seven>
audience: families | caregivers | both
format: photo | carousel | reel | story | text
platforms: instagram, facebook
publish_at: 2026-10-02T09:00     (owner's local time; timezone lives in Setup)
media_source: owner-upload | canva | none
canva_design_id: <id or blank>
canva_edit_url: https://www.canva.com/design/<id>/edit   (blank if none)
media_urls: <blank until publish resolves them>
first_comment: <hashtags and/or link, or blank>
location_tag: yes | no
approval: <blank> | approved by <name> on <date>
vendor_post_id: <blank until scheduled>
published_urls: <blank until live>

## Caption
<the caption, exactly as it will post>

## Why this post
<one or two lines: which pillar, which audience, what it should make people do>

## Compliance check
<filled by compliance-reviewer before approval: pass | issues>
```

## Lifecycle

| Step | Who | What changes |
|---|---|---|
| Draft | `draft-post` (+ `make-graphic`) | Packet created in `2 Drafts/`, `status: draft` |
| Review | `compliance-reviewer` | `## Compliance check` filled |
| Approve | the owner, in chat | `publish` records `approval:`, moves to `3 Approved/` |
| Schedule | `publish` | `vendor_post_id`, `media_urls`, `status: scheduled` |
| Live | `publish` / `learn` | `published_urls`, moved to `4 Published/` |
| Failed | `publish` / `learn` | `status: failed` + reason; stays in `3 Approved/` for retry |

Because docs cannot be edited in place, each status change is a **replace-by-recreate**
(`drive-conventions.md`). Keep the title identical so the packet stays findable.
