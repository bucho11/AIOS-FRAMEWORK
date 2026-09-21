# Map

*This one is for Claude, not for you — but nothing here is a secret, so read it
any time you're curious what it knows.*

*Every session starts by reading this document. It holds every folder, every
setting, and every rules document with the one job that document does — so Claude
goes straight to what it needs instead of hunting through your folder, and so it
can always tell whether a document for a job already exists.*

**workspace_version:** 2
**Last rebuilt:** {{date}}

## Settings

```
business_name: {{business_name}}
timezone: {{timezone}}
approval_word: {{approval_word}}
posting_capacity_per_week: {{posting_capacity_per_week}}
reels_she_can_film_per_week: {{reels_per_week}}
canva_available: {{canva_available}}
recruiting_in_scope: {{recruiting_in_scope}}
zernio_profile_id: {{zernio_profile_id}}
zernio_instagram_account_id: {{zernio_instagram_account_id}}
zernio_facebook_account_id: {{zernio_facebook_account_id}}
```

## Folders

| Folder | Drive ID |
|---|---|
| root | {{root_id}} |
| 1 — Brain/Told to us | {{told_id}} |
| 1 — Brain/Learned by us | {{learned_id}} |
| 2 — Brand Assets | {{assets_id}} |
| 2 — Brand Assets/Photo releases | {{releases_id}} |
| 3 — Social/1 Ideas | {{ideas_id}} |
| 3 — Social/2 Drafts | {{drafts_id}} |
| 3 — Social/3 Approved | {{approved_id}} |
| 3 — Social/4 Published | {{published_id}} |
| 3 — Social/Results | {{results_id}} |
| 9 — Archive | {{archive_id}} |

## Rules documents

One job per row. **Two rows may never do the same job** — that is the rule that
keeps this system from ever holding two different answers to the same question.

| Document | The one question it answers | Drive ID | claude_wrote |
|---|---|---|---|
| About the business | what this business is and where | {{id}} | {{ts}} |
| Brand voice | how she sounds | {{id}} | {{ts}} |
| Who we talk to | who we are speaking to | {{id}} | {{ts}} |
| What we offer | what she sells and for how much | {{id}} | {{ts}} |
| Colors and fonts | what it looks like | {{id}} | {{ts}} |
| Rules for the AI | what the AI may do without asking | {{id}} | {{ts}} |
| How she likes to work | how she wants to be worked with | {{id}} | {{ts}} |

## Rooms

| Room | What it's for | Connector | Added | Last used |
|---|---|---|---|---|
| 3 — Social | Instagram and Facebook, idea to published | Zernio{{canva_line}} | {{date}} | {{date}} |

## Connections

| Service | What it does | Status |
|---|---|---|
| Google Drive | holds this workspace | connected |
| Zernio | publishes and schedules, hosts your photos | connected |
| Canva | branded graphics | {{canva_status}} |

## Rhythms

| When | What happens |
|---|---|
| Sunday evening | next week gets planned and drafted |
| Monday morning | last week's results, and anything that needs you |
| Monthly | a tidy-up and safety check — say "housekeeping" any time |

## Upgrade history

*What shape this workspace has been in, and when it changed. Claude keeps this — it's
how it knows a change finished properly.*

| To version | When | Result |
|---|---|---|
| 2 | {{ts}} | done |

## Retired

*Names that are never reused, so old notes and old links keep meaning what they meant.*

| Name | Retired | Replaced by |
|---|---|---|
| — | — | — |

## Want to add something?

Just say what you want. Email marketing, replying to reviews, finding caregivers,
chasing invoices — each becomes its own room in here, and nothing that already
works has to change. Your voice, your offers and your logos are shared across every
room, so a new one already knows who you are on day one.
