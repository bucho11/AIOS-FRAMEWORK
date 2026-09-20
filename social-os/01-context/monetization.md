# Monetization — how this actually makes money

> `[SECONDARY]` unless tagged. Researched 2026-09-20.
> **The headline: you do not sell the plugin. Nobody does.**

---

## There is no paid plugin marketplace

Anthropic's plugin docs describe **distribution and installation only**. There is
**no** payments rail, no revenue share, no app-store sales, and no licensing
enforcement for third-party plugin developers.

**So how do plugin developers make money today?**
- Selling the **underlying product or service** the plugin connects to (SaaS
  subscription, API usage, enterprise contract)
- Using the plugin as **lead generation** for a paid plan
- **Consulting / managed services** — private or internal deployments
- Publishing free to build adoption and monetizing elsewhere

**The proof is in our own stack:** Zernio's Claude plugin is **MIT licensed and
free**. They give the plugin away and make money on the Zernio subscription.

> **Consequence for this business:** the plugin is the *delivery mechanism*, not
> the product. The revenue is the **managed service** — setup, the brain, the
> domain expertise, and running it. That is what DEC-009's "defensibility" note
> already said; this confirms it commercially.

---

## Who pays for Zernio — two models

`[PRIMARY]` Zernio: *"Accounts are counted across your whole team (owner plus
invited members), and the first 2 are free."* Profiles are free and unlimited.

### Model A — operator owns one Zernio team (**recommended**)
Every client is a **profile** inside the operator's team. Their Instagram and
Facebook connect into that profile.

| Clients | Accounts | Zernio/mo | Per client |
|---|---|---|---|
| 1 | 2 | **$0** | $0 |
| 5 | 10 | $48 | ~$10 |
| 20 | 40 | **$138** | **~$7** |

- ✅ Central control and visibility — the managed-service posture the operator chose
- ✅ Operator does the whole setup; the client clicks one OAuth link
- ✅ One invoice, marked up inside the service fee
- ⚠️ Operator holds the OAuth connections — **but not her passwords.** She can
  revoke from Meta at any time, and a profile can be handed off.

### Model B — each client owns their own Zernio account
Every client gets their **own** 2 free accounts.

- ✅ **$0 forever**, at any number of clients
- ✅ Purest form of DEC-007 — she owns everything
- ❌ No central dashboard, no cross-client reporting
- ❌ **She** has to sign up and maintain it — which breaks "she barely does anything"
- ❌ If it breaks, it is hers to fix

**Recommendation: Model A.** $7/client is immaterial against a managed-service
fee, and central control *is* the product. Model B saves $138/month and costs the
thing being sold.

**Offboarding must stay clean either way:** be able to move a profile or hand over
the connections on request. Never hold a client's accounts hostage (DEC-007).

---

## What the client pays for, itemized

| Line | Who pays | Real cost |
|---|---|---|
| Claude Cowork **Pro** | **Client**, direct to Anthropic | $20/mo |
| Google Drive | **Client** (existing Google account) | $0 |
| Zernio | **Operator**, inside the service fee | ~$7/client at 20 |
| The plugin | — | $0 |
| **Managed service** | **Client → operator** | **the business** |

The client has exactly **one** subscription to manage: Claude Pro. Everything
else is inside the operator's fee or free.

---

## Canva Enterprise — definitively closed

`[SECONDARY]`, and it now agrees from three directions:
- Canva Enterprise is **quote-based** with a **150+ contracted seat** minimum
- A **reseller/partner program exists**, but reselling means buying Enterprise
  licences — still the 150-seat floor
- **No way to get brand-template autofill without the end client being a member of
  a Canva Enterprise org.** A development-use exception can be requested at
  integration setup, but Enterprise membership remains the production requirement

**There is no seat-reselling shortcut.** DEC-016 (no image vendor in v1; Canva
stays a free manual tool) stands.

---

## Public vs private marketplace repo — open

`[SECONDARY]` Private marketplace repos are supported, but authentication runs
through **org GitHub App connections or local git credentials** — documented for
Claude Code and org settings, **not** for an individual Pro user on Cowork.

**Leaning public, for three reasons:**
1. Avoids putting a git-credential step in front of a non-technical client
2. The plugin is **instructions**, not data. The value — her brand voice, what
   works, her content history — lives in **her Drive**, which stays private.
   A public repo leaks the *method*, never the *client*.
3. A public repo is marketing.

**The counter:** it exposes the childcare guardrails and domain logic to
competitors. That is the real trade, and it is the operator's call.

Tracked as `OQ-012` — must be settled before the first client install, because
changing it later means every franchise re-installs from a new URL.
