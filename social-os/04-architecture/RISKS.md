# RISKS

---

## 🔴 Child imagery — the one that can end the client's business

*Adopted from the prior research document §9, which was its best work.*

**The legal position `[SECONDARY]`**
- The FTC treats **photos, videos and audio containing a child's image or voice
  as personal information** under COPPA.
- Commercial use of a child's likeness needs a **written guardian release**
  naming the platforms, the duration, and **explicitly covering paid advertising**
  — not just organic posts.
- Where parental responsibility is shared, the safe practice is **both parents'
  consent**. Custody disputes over posted images are live litigation.
- State right-of-publicity and "sharenting" laws add a second, varying layer.

**The platform position `[SECONDARY]`**
- Meta runs zero tolerance on child exploitation content and applies it to
  **AI-generated material identically to real material**.
- Enforcement tightened materially in 2026.
- A false positive does not get a warning. It kills the account — **the client's,
  not yours.**

**Hard rules for the build**

1. **Never generate AI images of children.** Not photoreal, not stylised, not
   "obviously cartoon." Downside catastrophic, upside zero.
2. **No identifiable child's face without a release on file.** The skill checks a
   release registry and **refuses to draft**, names the reason, and offers the
   alternative framing.
3. **Default visual language:** staff, parents, homes, hands, toys, backs of
   heads, wide shots from behind, empty play spaces, graphics and quote cards.
4. **Disclose AI illustration** where it could read as depicting real clients.

**This is not a handicap — it is the winning strategy.** Childcare converts on
trust signals: real staff on camera, transparent vetting, credentials, parent
testimonials, community presence. Children's faces convert nothing and risk
everything.

## 🔴 Worker classification

Nannies are **W-2 household employees, not 1099 contractors**, in essentially all
standard placements. Content implying 1099 treatment is a real liability for the
client. Goes in the skill's banned-claims list.

## 🟠 Claims a childcare brand cannot make

Banned without documentary backing, enforced in the skill:
- Safety guarantees ("100% safe", "guaranteed")
- Unverified credential claims (certifications, licences, insurance)
- Background-check claims beyond what is actually performed
- Any comparison implying a competitor is unsafe
- Pricing or guarantee terms not confirmed by the client

## 🟠 Vendor concentration

Ayrshare holds the publish path; Bannerbear holds image + hosting. Mitigated by
the swap seam (`STACK.md`), Composio kept warm as a ready fallback, and Facebook's
native scheduler always reachable. **Never run two publish paths at once** —
double-posting is worse than an outage.

## 🟠 Meta API drift

Meta deprecates aggressively — unprefixed Instagram Login scopes were deprecated
2025-01-27, legacy IG v1.0 endpoints retired through 2025. Using a vendor's
reviewed app means the vendor absorbs most of this. Do not wire to anything a
connector marks `*_DEPRECATED`.

## 🟡 Instagram publish quota

25 vs 50 per rolling 24h — sources conflict. **Design for 25** and read the real
quota at runtime (`INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT`) rather than
trusting any number in any document, including this one.

## 🟡 Licensing — AIOS is GPL-2.0-or-later

The AIOS framework repo is **GPL-2.0-or-later** across `skills/aios/`,
`templates/aios/`, `plugins/aios/`, root docs and AIOS-built MCPs. Copying those
files into a product sold to franchises attaches GPL obligations — including
offering source under the same terms.

**Mitigation (DEC-008):** everything in `social-os/` is original text. It borrows
*structural ideas* — declared/observed context split, trust contract, decision
log, index discipline — which are not copyrightable. **No AIOS source files are
copied into this tree.** Also note Anthropic's `docx`/`pdf`/`pptx`/`xlsx` skills
are proprietary and must never be vendored.

## 🟡 Comprehension debt

The operator will resell a system he did not hand-write. When it breaks in front
of a client, he has to debug it. Mitigation: this folder, and specifically
`DECISIONS.md` carrying the *why* and the *reversal trigger* for every choice.
