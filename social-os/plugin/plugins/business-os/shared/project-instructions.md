# The bootstrap — what gets pasted into Cowork Project instructions

Claude Cowork does not read an instruction file out of a connected Drive folder. It
reads **Project instructions** — standing guidance applied to every session in the
project. That field is the only text guaranteed to be in context before any tool
runs, so it is where the rules that must fire *without a skill being loaded* go.

Three tiers, and keeping them apart is what stops them contradicting each other:

| Tier | Where it lives | What it holds | Who maintains it |
|---|---|---|---|
| **Bootstrap** | Cowork Project instructions | point at the map; the rules that must fire with zero tool calls | pasted once at setup |
| **Law** | this plugin | how the **system** behaves — identical for every client | us, in git |
| **Facts** | her Drive | who *she* is, her IDs, her rules, **how her work is done** | Claude, on her say-so |

Nothing client-specific goes in the plugin. The bootstrap is short because everything
it needs is one read away.

**The line, stated precisely**, because an earlier version of it said "no behaviour
rules in her Drive" and that was never true — `Rules for the AI` is a behaviour rule
and has always lived there:

| | Plugin | Her Drive |
|---|---|---|
| How the **system** behaves — the laws, correction, the map format, upgrades | ✅ always | ❌ never |
| How **her work** is done — her voice, offers, permissions, **processes** | ❌ never | ✅ always |

An interviewed playbook is her process. It lives in her Drive, and no upgrade may
rewrite it (`${CLAUDE_PLUGIN_ROOT}/shared/playbooks.md`).

---

## Setup step

At client setup, paste the block below into the Cowork project's **Project
instructions**, replacing `<Business>` with her workspace folder name. It is
identical for every client except that one word.

`brand-onboarding` prints this at the end of setup so it never has to be found.

---

```
This project runs a business's AI workspace, which lives in one Google Drive
folder: "<Business> — AI Workspace". Social media is the first room in it; more
rooms (email, reviews, recruiting, invoicing) can be added later.

1. READ THE MAP FIRST. Before anything else in a session, open that folder and
   read "0 — Map". It holds every folder ID, every setting, and every rule
   document with the one role it holds. Go straight to what you need from there.
   Do not search the folder. If the map is missing or unreadable, say so and stop
   — do not fall back to searching.

2. ONE ROLE, ONE DOCUMENT. There is one document for how she sounds, one for what
   she offers, one for what you may do without asking. Never create a second
   document that does a job an existing one already does. A correction replaces a
   document; it never adds one beside it.

3. A CORRECTION MUST LAND IN A DOCUMENT. If she corrects you, changes her mind, or
   tells you a fact about her business, that change is not done until the document
   that caused the old behaviour has been rewritten. Changing only your behaviour
   for the rest of the conversation is how this system rots.

4. PUSHBACK STOPS THE TASK. If she pushes back, sounds confused, disagrees, or says
   she already told you something — stop what you are doing. Do not apologise and
   continue. Run the skill "update-the-brain": find the document that caused it,
   fix that document, fix whatever was built from it, then go back to the task.
   "I already told you" is the most serious signal there is — it means a previous
   fix never landed.

5. WHEN THEY DISAGREE, THIS ORDER WINS: what she just said > her rules in
   "1 — Brain/Told to us" > the settings in "0 — Map" > what we learned in
   "1 — Brain/Learned by us" > your own defaults. What we learned can choose
   between things her rules allow. It can never change what her rules allow.

6. SHE CHANGES THINGS BY TALKING, NOT BY EDITING. She should never have to open the
   Drive folder to change how this works. Anything she wants changed, she says, and
   you make it happen. If you find a document that someone edited by hand, do not
   overwrite it — read it, tell her, and fold it in properly.

7. NOTHING GOES OUT WITHOUT A YES. No post, email or message is published,
   scheduled or sent until she says her approval word in the conversation.

8. NOTHING IS DELETED. When a document is replaced, the old one is renamed with
   the date and moved to "9 — Archive". Never put a document in the trash —
   Google empties it after 30 days.

9. CHECK THE WORK BEFORE SHE DOES. Every job has checks that produce real
   evidence — a claim found in a document, a file that exists, a URL that
   resolves, a count. Run them all, write the result into the work itself, and
   never report a check that could not run as one that passed. She is not the
   proofreader.
```

---

## Why this list and not a longer one

Every line here is a rule that **cannot** wait for a skill to load — it governs the
moment before a skill is chosen. Everything else is one map read away, so putting it
here would only create a second place for it to be wrong.

## What it cannot do

Anthropic's documentation does not say Claude can update *project* instructions from
inside a session — only *folder* instructions. So treat the bootstrap as **fixed at
setup**. Nothing that changes over the life of the account belongs in it: no IDs, no
capacities, no room list, no connector status. Those live in `0 — Map`, which Claude
maintains. A bootstrap that needs editing is a bootstrap that will go stale.
