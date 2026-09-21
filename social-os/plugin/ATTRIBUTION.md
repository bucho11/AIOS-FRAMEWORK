# Attribution and licensing

Most of this repository is original work. A few parts are adapted from other people's
thinking, and this file says which, under what terms, and what travels with it if you
redistribute.

**Read this before reselling or white-labelling.** This plugin is built to be deployed
for paying clients, which makes upstream license obligations a commercial question
rather than an academic one.

## Summary

| Part | Origin | License | What travels |
|---|---|---|---|
| Everything not listed below | original, this repo | MIT | copyright + license notice |
| `shared/sounds-human.md` — two-layer framing, the convergence trap, the structural audits | adapted from [humanizer-stack](https://github.com/NulightJens/humanizer-stack) (Jens Heitmann) | MIT | copyright + license notice |
| `skills/sounds-human/` | original, this repo, same lineage of ideas | MIT | — |
| Surface tells in `draft-post/references/checks.md` (11–16) | the underlying observations trace to [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | CC BY-SA 4.0 | attribution; see the note below |
| The copy-tell ranking (em dash first) | [vibecoded-design-tells](https://github.com/jcarterjohnson/vibecoded-design-tells) (jcarterjohnson) | MIT | copyright + license notice |
| Every statistic about human vs AI writing | Russell et al. 2026, arXiv:2604.03136 | academic citation | cite; do not relicense |

## 1 · What we deliberately did not do

**We did not vendor `skills/humanizer/SKILL.md` from humanizer-stack**, and that was a
licensing decision rather than a quality one — it is a good file.

Its pattern catalogue traces to Wikipedia's *Signs of AI writing*, which is
**CC BY-SA 4.0: a share-alike license.** The upstream repository is explicit that
redistribution of that file should carry both its notice and the Wikipedia
attribution, and that relicensing it under incompatible terms needs a legal read.

For a plugin deployed to paying clients, inheriting a share-alike obligation on a core
file is a question better avoided than answered. So instead:

- Our surface checks are **written for this system**, in our own check format, scoped
  to short childcare social copy rather than to general prose.
- They draw on the **individual observations** — that LLMs overuse em dashes, that
  "not just X, it's Y" is a tell, that hype vocabulary reads as machine-made. Those
  are facts about how language models write. Facts are not copyrightable; a
  particular selection and arrangement of them can be, which is why we made our own.
- Wikipedia is credited anyway, because the observations came from somewhere and
  WikiProject AI Cleanup did the work of noticing them.

**This is our reading, not legal advice.** If you redistribute this plugin
commercially and the question matters to you, get your own read.

## 2 · humanizer-stack (MIT)

Copyright (c) 2026 Jens Heitmann. Used under the MIT License.

What we took, and it is the valuable part: **the two-layer framing** — that surface
editing and structural editing are different jobs that must run in sequence — and
**the convergence trap**, which is the finding that a de-slopping checklist applied
uniformly builds a new detectable fingerprint, because rarity is the human signal.

Also the structural audits themselves, adapted: where the lesson sits, how emotion is
rendered, whether things get named, and whether the skeleton repeats.

**What we changed, and why:**

- **The order is inverted.** That pipeline puts a voice layer last, as something
  additive. Here the owner's voice is the *input* — drafts are written from
  `Brand voice` and her approved examples — so the final step is not adding voice but
  **checking the de-slopping did not sand it off.**
- **Four audits, not six.** Structural tidiness and reader acknowledgment need room
  to breathe; at 150 words they read as gimmick. Kept for long-form only.
- **Shape convergence runs against a real corpus.** The workspace has the last N
  published posts on disk with their packets, so "does this look like the last three"
  is an actual comparison rather than a memory exercise.
- **No vendored scanner.** Ours are checks a skill reads, not scripts — nothing in
  this system has a verified way to execute Python in a client session, and shipping
  a scanner that silently never runs would be worse than having none.

**Two defects we found in the upstream scanner while testing it**, reported here
because they are load-bearing for social copy and we had to work around them:

1. **The antithesis rule misses contractions.** Its pattern anchors on the literal
   string `not just`, which does not occur in `isn't just` — the letters *n-o-t* are
   not in that word. Social copy runs on contractions.
2. **The closer alternation is too narrow.** It accepts `it's` or `but`, so
   *"That's not just a nanny, that's a partner"* passes clean.

Measured against five realistic variants, it caught two. Our check 11 reads for the
shape rather than the string, and names the contracted forms explicitly.

**One finding about applying it here:** the upstream copy scanner fires on every em
dash, and this workspace's folder names are built from them (`1 — Brain`,
`3 — Social`). A scan of our own client-facing seed documents returned 13 hits, all of
them folder names. Our check 13 is scoped to captions only. The upstream README warns
about exactly this; we confirmed it.

## 3 · vibecoded-design-tells (MIT)

Copyright (c) jcarterjohnson. Used under the MIT License.

The finding we use: in an analysis of roughly 3.2M Reddit posts across 47 subreddits,
narrowed to ~47,000 on-topic posts, **the em dash was the single most-cited "a machine
wrote this" writing tell — ranking above every vocabulary word.** That ranking is why
check 13 exists as its own check rather than as a line inside the hype-vocabulary one.

No text or code from that project is reproduced here.

## 4 · Wikipedia: Signs of AI writing (CC BY-SA 4.0)

Portions of the surface-tell observations in `draft-post/references/checks.md`
ultimately derive from
[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup, available under the
[Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

The patterns there were catalogued from thousands of instances of AI-generated text on
Wikipedia — that observation work is real and is credited here regardless of whether
the facts themselves carry any obligation.

## 5 · StoryScope (academic citation)

> Russell, J., Rajendhran, S., Pham, C. M., Iyyer, M., and Wieting, J. (2026).
> *StoryScope: Investigating idiosyncrasies in AI fiction.* arXiv:2604.03136.
> University of Maryland and Google DeepMind.
> Code and data: https://github.com/jenna-russell/storyscope

Every human-vs-AI statistic in `shared/sounds-human.md` and in checks 11–17 comes from
this paper. **We verified the headline figures against the paper's own abstract** —
93.2% macro-F1 for human vs AI detection on narrative features alone, 68.4% for
six-way authorship attribution, 61,608 stories from 10,272 prompts. Findings are
reported; no text from the paper is reproduced.

**The caveat the paper's own scope imposes, repeated wherever it matters:** the study
examined roughly 5,000-word fiction. Applying it to a 150-word social caption is an
**inference, not a result the paper establishes.** We use the four audits whose
mechanism plainly survives the jump and say so.
