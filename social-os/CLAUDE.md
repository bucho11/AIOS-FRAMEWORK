# CLAUDE.md — How to work this project

Read this before doing anything in `social-os/`.

---

## What you are building

A **resellable social content operating system** that a non-technical franchise
owner runs from **Claude Cowork** plus **one Google Drive folder**.

Two products, do not confuse them:

| | What it is | Who owns it |
|---|---|---|
| **The template** | Folder structure + skills + connector setup. The thing that gets cloned per client. | Bucho (the operator). This is the IP. |
| **The instance** | One client's live folder with their brand, content, and history. | The client. |

A change to the template must be portable to every instance. A change to an
instance must never leak client specifics back into the template.

---

## Non-negotiable rules

1. **No guessing. Ever.** Every factual claim about a vendor, API, limit, or
   price must be verified and recorded in `03-research/VERIFIED-FACTS.md` with a
   provenance tag. If you cannot verify it, it goes in `OPEN-QUESTIONS.md` with
   the exact test that would close it — never into a design as an assumption.

2. **Provenance tags are not decorative.**
   - `[PRIMARY]` — fetched from the vendor's own live docs/API this session.
   - `[SECONDARY]` — research citing third parties. Directionally right; verify before spending money or writing code against it.
   - `[UNVERIFIED]` — named open question. **Do not build on it.**

3. **Approve-then-publish is a hard gate.** Nothing reaches a live social account
   without explicit human approval. This is a childcare brand; one bad post is an
   existential event, not a metric dip. See `04-architecture/RISKS.md`.

4. **Never generate or post AI images of children, and never post an identifiable
   child's face without a signed release on file.** This outranks every growth
   tactic. See `04-architecture/RISKS.md` § Child imagery.

5. **Keep the publisher behind a seam.** Nothing upstream of the publishing
   adapter may know which vendor publishes. Vendors churn. See `STACK.md`.

6. **Update the decision log when you decide.** A decision without a recorded
   *why* and a *reversal trigger* is a decision that will be silently re-litigated
   in three weeks.

7. **Do not copy AIOS source files into this tree.** Borrow structure, write
   original text. See `README.md` § Licensing.

---

## Session ritual

**At start:**
1. Read `PROJECT.md` → Current State table. It is the only authoritative source
   for paths, status, and what's next. Never use paths from memory.
2. Read `02-decisions/OPEN-QUESTIONS.md`. If your task depends on an open
   question, close it first or state loudly that you are assuming.
3. Skim `02-decisions/DECISIONS.md` for anything your task would contradict.

**At end:**
1. Update `PROJECT.md` Current State + Next actions.
2. Append any new decision to `DECISIONS.md` with why + reversal trigger.
3. Append new verified facts to `VERIFIED-FACTS.md` with tag + date.
4. Move any question you closed out of `OPEN-QUESTIONS.md` into the research file.
5. Commit. Never end with uncommitted work — this folder's entire job is to survive.

---

## Research tooling available in this environment

- **Perplexity API** — key in `$PERPLEXITY_API_KEY`. **Use model `sonar` only.**
  Larger models time out past 60s. Helper pattern:
  ```bash
  curl -sS --max-time 150 https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" -H "Content-Type: application/json" \
    -d "$(jq -n --arg q "$1" '{model:"sonar",messages:[{role:"user",content:$q}]}')" \
    | jq -r '.choices[0].message.content'
  ```
  Perplexity output is `[SECONDARY]`. Always.

- **Composio API** — key in `$COMPOSIO_API_KEY`. Query it directly for ground
  truth rather than reading docs about it. This is `[PRIMARY]`:
  ```bash
  curl -sS https://backend.composio.dev/api/v3/toolkits/<slug> -H "x-api-key: $COMPOSIO_API_KEY"
  curl -sS "https://backend.composio.dev/api/v3/tools?toolkit_slug=<slug>&limit=60" -H "x-api-key: $COMPOSIO_API_KEY"
  ```
  v1/v2 endpoints are retired. Use v3.

- **WebFetch** — for vendor pricing/doc pages. Help-center pages that are
  JS-rendered will return navigation chrome under plain `curl`; use WebFetch.

---

## Voice when writing for the client

Plain language. Short sentences. No jargon, no framework vocabulary. She is not
technical and never will be — that is a design input, not a problem to fix.
Anything she must read is written for someone who has never heard the word "API".
