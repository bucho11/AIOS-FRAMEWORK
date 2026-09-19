# STACK — the architecture

---

## The whole system

```
                    ┌─────────────────────────────┐
                    │      CLAUDE COWORK          │
                    │  brain · chat · approval    │
                    │        (Pro plan)           │
                    └──────────────┬──────────────┘
                                   │  all connections are MCP / connectors
          ┌────────────────┬───────┴───────┬────────────────┐
          │                │               │                │
   ┌──────▼─────┐  ┌───────▼──────┐  ┌─────▼──────┐  ┌──────▼──────┐
   │ GOOGLE     │  │  BANNERBEAR  │  │  AYRSHARE  │  │  SCHEDULED  │
   │ DRIVE      │  │   MCP        │  │    MCP     │  │   TASKS     │
   │ connector  │  │              │  │            │  │  (built in) │
   ├────────────┤  ├──────────────┤  ├────────────┤  ├─────────────┤
   │ brand      │  │ branded PNG  │  │ schedule   │  │ cloud-run   │
   │ memory     │  │ + PUBLIC URL │  │ + publish  │  │ machine off │
   │ content    │  │              │  │ IG + FB    │  │ hourly floor│
   │ calendar   │  │   $49/mo     │  │  $149/mo   │  │    $0       │
   └────────────┘  └──────────────┘  └────────────┘  └─────────────┘
                                            │
                                     ┌──────▼──────┐
                                     │  Instagram  │
                                     │  Facebook   │
                                     │ (client's)  │
                                     └─────────────┘

   COMPOSIO MCP ── connector layer for Drive + future workflows,
                   and the ready fallback publisher behind the seam
```

**Every component is a connector or a skill. There is no service to deploy, host,
monitor or patch.** That is not an aesthetic preference — Cowork has no generic
"make an HTTP request" primitive, so every external call must go through an MCP
tool. Choosing vendors that ship MCP servers is what removes custom code from
this build entirely.

## The content lifecycle

```
 1. PLAN      scheduled task, weekly
              reads Brain + what_works.md + calendar → proposes the week
                                │
 2. DRAFT     writes copy from brand voice + pillars
              picks a Bannerbear template + fills it → branded PNG + public URL
                                │
 3. STAGE     writes to Drive 2_drafts/ + calendar row
                                │
 4. ► APPROVE ◄  she reviews in Cowork chat. THE GATE. Nothing passes alone.
                                │
 5. SCHEDULE  on approval → Ayrshare with the publish time
              file moves 2_drafts/ → 3_approved/
                                │
 6. PUBLISH   Ayrshare fires it. We own no clock.
              file moves → 4_published/ with the live URL
                                │
 7. LEARN     scheduled task, weekly
              pulls performance → writes observed/what_works.md
                                └──────────► feeds step 1
```

Step 7 is what makes it compound instead of plateau. Without it this is a posting
tool; with it, it gets better every week.

## The swap seam

*Adopted from the prior research document §7, which was right.*

Nothing upstream of the publishing adapter may know which vendor publishes.
Everything above talks to five methods and nothing else:

```
schedule(post, publish_at, platforms[])  -> external_id
cancel(external_id)                      -> bool
status(external_id)                      -> queued | scheduled | published | failed
quota(platform)                          -> remaining posts in window
publish_now(post, platforms[])           -> external_id
```

Rules that keep it swappable:

- **Your own `post_id` is the primary key.** The vendor's ID is a foreign key on
  your record, never your identity. Vendors churn; your history should not.
- **No vendor-shaped payloads upstream.** The drafting skill emits a neutral post
  object — caption, media URLs, platforms, publish time, first comment. The
  adapter translates.
- **Implement `quota()` even where it stubs to `unknown`.** Having the method
  means the IG daily ceiling never surprises anyone in production.
- **Keep Facebook's native scheduler reachable through the same interface** — it
  is free and excellent, and this makes "FB native + IG via vendor" a config flag
  rather than a rewrite.
- **Log every request and response verbatim.** You will need it to prove parity
  when you swap, and to see what actually broke when Meta changes something.

In a no-code Cowork build this seam lives in **the skill's instructions** — one
publishing skill that every other skill calls, and only that skill knows the
vendor's tool names. Swapping vendors edits one file.

## Cost

| Component | Cost | Who pays |
|---|---|---|
| Claude Pro | $20/mo | Client |
| Google Drive | existing | Client |
| Ayrshare | $149/mo (1 profile) → ~$20/client at 30 | Operator |
| Bannerbear | $49/mo, shared across all clients | Operator |
| Composio | $0 (100k calls/mo) | Operator |
| Cowork scheduled tasks | $0 | — |

**Operator marginal cost:** ~$198/mo at one client; ~$35 at ten; ~$37 at twenty.
Price off the portfolio, not off client #1.
