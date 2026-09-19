# Client folder template — the Google Drive structure

> The deliverable. One folder per client, cloned from this spec.
> Names are deliberately boring and jargon-free: **she has to understand it at a
> glance, forever, without training.**

---

## Structure

```
Lifetime of Love — AI Assistant/          ← she connects this one folder
│
├── 📌 START HERE.md                      ← how to talk to it. Written for a non-technical reader.
│
├── 1 — Brain/                            ← what the AI knows. The compounding asset.
│   ├── Told to us/                       ← SHE owns these. Edit any time.
│   │   ├── About the business.md
│   │   ├── Brand voice.md
│   │   ├── Who we talk to.md             ← families AND nannies. Two audiences.
│   │   ├── What we offer.md
│   │   └── Rules for the AI.md           ← the trust contract. What it may do alone.
│   └── Learned by us/                    ← THE AI owns these. She reads, rarely edits.
│       ├── What works.md                 ← performance → strategy. The compounding loop.
│       ├── Her preferences.md            ← every correction she makes, remembered
│       └── History.md                    ← running log of what happened
│
├── 2 — Brand Assets/
│   ├── Logos/
│   ├── Photos/                           ← approved, release-cleared imagery only
│   ├── Colors and fonts.md
│   └── Photo releases/                   ← ⚠️ gates any content with a real child
│
├── 3 — Content/
│   ├── 1 Ideas/
│   ├── 2 Drafts/                         ← waiting for her. NOTHING publishes from here.
│   ├── 3 Approved/                       ← she said yes. Scheduled.
│   ├── 4 Published/                       ← live, with the URL
│   └── Content Calendar.md               ← the one truth surface
│
├── 4 — Results/                          ← weekly performance reports
│
└── 5 — Archive/
```

## Why it is shaped this way

| Choice | Reason |
|---|---|
| **Numbered top-level folders** | Drive sorts alphabetically. Numbers force the order you read them in. |
| **`Told to us` / `Learned by us`** | The single most important split. Hers vs the AI's — so they enrich each other instead of overwriting each other. This is what makes it compound rather than drift. |
| **`1 Ideas → 4 Published`** | An approval gate you can *see*. Nothing publishes from `2 Drafts`. Moving a file is a physical, obvious act. |
| **`Rules for the AI.md`** | The trust contract. Starts conservative, graduates as trust is earned. |
| **`What works.md`** | Where performance data becomes strategy. Without it this is a posting tool, not a system. |
| **`Photo releases/`** | Makes the COPPA constraint a *file the AI can check* rather than a rule someone must remember. |
| **Plain-English names, spaces and all** | She is not technical and never will be. That is a design input. |

## Seed content

Every file ships pre-written with **guided prompts, not blank pages**. A blank
`Brand voice.md` gets skipped forever. The onboarding skill fills these in
conversation — she should never face an empty file.

## `Rules for the AI.md` — the starting contract

Ships at maximum caution. Graduates by category, never wholesale.

| The AI may... | At launch |
|---|---|
| Research ideas and draft posts | ✅ on its own |
| Create branded images from approved templates | ✅ on its own |
| Write to `1 Ideas` and `2 Drafts` | ✅ on its own |
| Update `Learned by us/` | ✅ on its own |
| Move a file to `3 Approved` | ❌ **only after she says yes** |
| Publish or schedule anything | ❌ **only after she says yes** |
| Post anything with a child's face | ❌ **never without a release on file** |
| Make a safety, credential or pricing claim | ❌ **never unless it's in `Told to us`** |

## Per-client cloning

1. Copy the template folder → rename for the client.
2. Run the **onboarding skill** — it fills `Told to us/` in conversation.
3. Drop brand assets into `2 — Brand Assets/`.
4. Build their Bannerbear templates (once per brand — for a franchise, once for
   **all** locations).
5. Connect their IG + FB in the publisher.
6. Share the folder: **client owns, operator is Editor** (DEC-007).
7. Install the skills in her Claude, add the connectors.
8. Run one end-to-end test post before going live.
