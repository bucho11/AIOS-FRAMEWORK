# Image layer — how branded graphics get made

> The operator's read: *"looks like Canva might be far fetched."* Correct. This
> file records why, and what replaces it.

---

## Why Canva Connect is out

Canva's own docs, `[PRIMARY]`:

> "To use this API, your integration must act on behalf of a user who is a member
> of a **Canva Enterprise** organization."

Plus MFA required on the acting account. **Canva Pro and Canva Teams cannot use
brand-template autofill through the API.** Composio's `canva` toolkit exposes
autofill tools, but Canva rejects the call on non-Enterprise plans — *a tool
existing in a connector catalog is not permission to call it.*

Since Claude **Pro** is the floor for every client (operator's Q11), requiring
Canva Enterprise per franchise is a non-starter. Canva stays in the workflow as a
**human design tool** — it is simply not the automation surface.

## Why AI image generation is the wrong tool here

Tempting, and wrong for this use case, for three independent reasons:

1. **Brand lock.** Exact logo placement, exact brand typography and a fixed
   layout grid are what diffusion models do not guarantee. "Close to the brand"
   is off-brand.
2. **The childcare constraint.** No AI-generated children, ever (see `RISKS.md`).
   That removes most of what a generative model would otherwise contribute.
3. **Consistency over novelty.** Social branding wins by looking *the same* every
   time. Generation optimises for the opposite.

Generative image models stay available for **backgrounds and abstract//illustrative
assets**, never for people or the layout itself.

## The proven pattern: template-fill APIs

Mature category. You design a template once in a visual editor, then call an API
with variables (`headline`, `body`, `image_url`, `logo`) and get back a finished
branded PNG **at a hosted public URL**.

| Vendor | Entry price | MCP? | Hosted public URL? | Maturity `[SECONDARY]` |
|---|---|---|---|---|
| **Bannerbear** | **$49/mo** Automate, 1,000 credits | **Yes — official** | **Yes**, standard API output | **Most established** |
| Placid | Tiers exposed, **dollar prices not on page** | Not confirmed | Not confirmed on page | Established, smaller |
| APITemplate.io | Free tier, then ~$19/$69/$139 | Not confirmed | CDN storage listed | Credible, less known |
| Abyssale | from ~$36/mo | Not confirmed | Likely | Creative-automation oriented |
| Robolly | $39 / $129 | Not confirmed | Likely | Smaller |
| Templated.io | $29–$179 | Not confirmed | CDN listed | Smaller |

## Why Bannerbear wins here

Four reasons, in order of weight:

1. **It solves two problems with one vendor.** It makes the branded image *and*
   hosts it at `https://images.bannerbear.com/...` — which is exactly the
   "publicly accessible HTTPS URL returning the file directly" that Instagram
   requires and that a **Google Drive share link cannot provide**. The prior
   research document flagged this requirement and then left it unsolved in all
   five of its stacks.
2. **It has an official MCP server.** Verbatim from their docs: *"Bannerbear
   provides an MCP server, so AI agents and assistants—such as Claude, Cursor and
   other MCP-compatible clients—can use Bannerbear directly without writing
   against the REST API."* Cowork talks to it natively. **No code.**
3. **It is the most established in the category** — the operator's "proven, not
   invented" bar.
4. **It scales across clients on one account.** $49 buys 1,000 credits/month; at
   ~40 posts/client/month that is many clients on one bill, and it is operator
   infrastructure the client never sees.

**Cost caveat to verify before quoting:** "Instant URLs" (render-on-demand from a
query string) are **Scale tier ($149) and up**. That is a *different feature* from
the standard hosted output URL, which appears on all API tiers. `OQ-003` closes
this with a live trial call.

## The workflow this produces

```
Brand assets in Drive  ──┐
                         ├─→ Bannerbear template ──→ branded PNG + public URL
Claude writes copy    ───┘         (designed once)              │
                                                                ▼
                                                    publisher takes the URL
```

**One-time setup cost, worth naming:** her templates get built in Bannerbear's
editor, not Canva's. If she has existing Canva brand templates they are recreated
once (or exported as background images and used as Bannerbear layers). That is an
hour of setup per brand, not per post — and for a franchise brand it is done
**once for all ~20 locations.**
