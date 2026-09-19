# Claude Cowork — what it is and what it can hold

> All `[PRIMARY]` from Anthropic docs, 2026-09-19. Facts in `VERIFIED-FACTS.md`;
> this file is the interpretation.

---

## The two modes, and why it matters

| | Cloud session | Local session |
|---|---|---|
| Agent loop runs | Anthropic's servers | The device |
| Files | Stored in the member's Claude account | Only folders the member connects |
| Works with machine off | ✅ | ❌ |

## The rule that shapes the whole architecture

Cowork's **scheduled tasks**:

> "Scheduled tasks run remotely, so they run on their cadence even when your
> computer is asleep or the Claude Desktop app is closed."
>
> "...they work with your **connectors** and the files saved to your Claude
> account. **They can't be tied to a folder on your computer.**"

Read those two sentences together and the design is settled:

- ✅ **Unattended automation works.** Machine off is fine.
- ❌ **A local folder is invisible to it.**
- ➡️ **Therefore the filesystem must be a connector.** Google Drive, reached
  through the Drive connector — not a Drive-for-Desktop local mirror.

This is the reason DEC-002 chose Drive-as-connector. A local folder gives richer
filesystem access in interactive sessions and then **goes dark for every
automated run** — the exact half of the system the client is paying for.

## What Cowork can hold

- **Skills** — `SKILL.md` packages that extend it.
- **Plugins** — bundle skills + connectors + sub-agents into one installable unit.
  **This is the franchise clone mechanism.**
- **Custom MCP connectors** — added at *Customize → Connectors* with a server
  URL. Available on **Pro**. This is how Ayrshare, Bannerbear and Composio attach.
- **Scheduled tasks** — hourly / daily / weekly / weekdays / manual. Pro and up.
- **Projects** — task organisation.

## Constraints to design around

| Constraint | Consequence |
|---|---|
| Scheduling floor is **hourly** | Post on the hour. Never promise 3:07 PM. |
| Scheduled tasks can't see local folders | Drive connector, always |
| **Pro is the floor** for every client | Nothing may require Team/Enterprise |
| No generic "make an HTTP request" primitive | Every external call goes through an MCP tool or connector. **Choosing vendors that ship MCP servers is not a preference — it is what removes custom code from the build.** |

That last row is the quiet reason the recommended stack is what it is: Ayrshare,
Bannerbear and Composio **all ship MCP servers**, so the entire system is
connectors and skills with no service to deploy, host, monitor or patch.
