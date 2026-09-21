# Brain layout — the owner's Drive folder

One folder per business. Plain-English names on purpose: the owner has to
understand it at a glance forever, without training. Numbers force Drive's sort
order.

```
<Business> — AI Workspace/
├── 0 — Start Here                  (Doc) how to talk to it, written for her
├── 0 — Setup                       (Doc) IDs and settings the skills read first
├── 0 — What's Installed            (Doc) which rooms are live, what they connect to
│
├── 1 — Brain/                      ── SHARED BY EVERY ROOM ──
│   ├── Told to us/                 she writes, Claude reads
│   │   ├── About the business
│   │   ├── Brand voice
│   │   ├── Who we talk to          families AND caregivers — two audiences
│   │   ├── What we offer
│   │   ├── Colors and fonts        replaces Canva Brand Kit on Pro
│   │   └── Rules for the AI        what it may do alone, what needs a yes
│   └── Learned by us/              Claude writes, she reads
│       ├── What works — Social (current)     rolling, replaced weekly
│       ├── What works — YYYY-Www             one per week, never replaced
│       ├── What works — YYYY Q#              quarterly compaction (housekeeping)
│       ├── Her preferences                   every correction, remembered
│       └── History                           dated log of what happened
│
├── 2 — Brand Assets/               ── SHARED BY EVERY ROOM ──
│   ├── Logos/   Photos/   Templates/
│   └── Photo releases/             gates any content with a real child
│
├── 3 — Social/                     ── THE FIRST ROOM ──
│   ├── 1 Ideas/
│   ├── 2 Drafts/                   waiting for her. NOTHING publishes from here.
│   ├── 3 Approved/                 she said yes; scheduled
│   ├── 4 Published/                live, with the URL (ages to Archive at ~90d)
│   ├── Content Calendar            (Doc) the truth surface for the week
│   └── Results/                    weekly performance reports
│
├── 4 — <next room>/                Email · Reviews · Recruiting · Invoicing …
│
└── 9 — Archive/                    ── SHARED ── retired from any room
```

**Two shared things, N rooms.** The brain and the brand assets are shared because
her voice and her logo do not change when the channel does. Each room holds one
domain and nothing else. Adding a room never touches a room that already works —
the rules are in `growth-and-upkeep.md`, and every skill that creates a folder or a
document reads it first.


## The `0 — Setup` doc

Created by `brand-onboarding`, read first by every other skill. Plain key: value
lines so it survives Doc conversion:

```
business_name: Lifetime of Love Nannies — Reno
timezone: America/Los_Angeles
drive_root_id: <folder id>
drive_rooms: social                 ← comma-separated; a new room appends here
drive_told_to_us_id: <folder id>
drive_learned_by_us_id: <folder id>
drive_social_id: <folder id>
drive_drafts_id: <folder id>
drive_approved_id: <folder id>
drive_published_id: <folder id>
drive_results_id: <folder id>
drive_archive_id: <folder id>
drive_releases_id: <folder id>
zernio_profile_id: <24-hex>
zernio_instagram_account_id: <24-hex>   (blank until connected)
zernio_facebook_account_id: <24-hex>    (blank until connected)
canva_available: yes | no          ← no ⇒ photo/video/text posts only, no graphics
posting_capacity_per_week: 4
reels_she_can_film_per_week: 2
recruiting_in_scope: yes | no
approval_word: approve
```

If a value is missing, the skill that needs it asks the owner once and then
**replaces the Setup doc** (per `drive-conventions.md`) so nobody asks again.

## Why this shape

- **`Told to us` / `Learned by us`** is the whole idea. Hers vs Claude's — so they
  enrich each other instead of overwriting each other.
- **`1 Ideas → 4 Published`** is an approval gate you can *see*. A file physically
  moving is an obvious act.
- **`Photo releases/`** turns a legal rule into a file Claude can check.
- **`Colors and fonts`** exists because Canva's Brand Kit is Enterprise-only; the
  hex values living here is what lets Canva Pro produce on-brand output.
