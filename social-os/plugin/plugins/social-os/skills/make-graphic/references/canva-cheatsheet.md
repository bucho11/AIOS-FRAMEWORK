# Canva MCP cheat-sheet — verified against Canva's MCP docs, 2026-09-20

Server: `https://mcp.canva.com/mcp` (declared in `.mcp.json`; the owner signs in
with her Canva account when the plugin connects).

## Plan gating (the part that matters)

| Capability | Free | **Pro** | Enterprise |
|---|---|---|---|
| generate · create · edit · search · export · upload assets · comments · folders | ✅ | ✅ | ✅ |
| Export quality | standard | **lossless PNG, transparent bg** | ✅ |
| `resize-design` | ❌ | ✅ | ✅ |
| `search-brand-templates` · `list-brand-kits` · `create-design-from-brand-template` | ❌ | ✅ | ✅ |
| `autofill-design` · `get-brand-template-dataset` | ❌ | ❌ | ✅ |

Pro users **can** create Brand Templates in the Canva UI and instantiate them via
MCP. What Pro cannot do is *autofill* them in one call — so we instantiate, then
`replace_text` each element. Same result, no Enterprise contract.

## Tools (names are exact)

| Tool | Use | Rate |
|---|---|---|
| `generate-design` | prompt + design type/preset (+ dimensions, brand kit, candidate count) → `job.result.generated_designs[]` each with `candidate_id`, `url`, `thumbnails` | 20/min |
| `create-design-from-candidate` | takes the generate **job id** + a `candidate_id` → editable design | 20/min |
| `search-brand-templates` / `create-design-from-brand-template` | Pro+: find and instantiate her templates | 100 · 20/min |
| `search-designs` · `get-design` · `get-design-pages` · `get-design-content` | discovery; `get-design-content` returns **element ids** for editing | 100/min |
| `start-editing-transaction` → `perform-editing-operations` → `commit-editing-transaction` (`cancel-editing-transaction` to abort) | the edit loop | 20 · 50 · 20/min |
| `upload-asset-from-url` · `get-assets` | bring in an image by public URL | 30 · 100/min |
| `resize-design` | Pro+: new dimensions from an existing design | 20/min |
| `export-design` | `design`, `format`, optional `quality`/`size`/`width`/`height`/`lossless` → `job.urls[]` | 20/min |
| `copy-design` · `import-design-from-url` · folders · comments | housekeeping | — |

## Editing operations (documented)

```json
{ "type": "replace_text", "element_id": "<from get-design-content>", "text": "New headline" }
```
On **responsive** pages use `find_and_replace_text` instead of `replace_text`.
Media replacement and text formatting operations exist per Canva's docs; read the
operation schema the tool exposes at run time rather than assuming field names.

## Export

- Returns a **signed download URL that expires** — Canva: *"use them immediately,
  and don't store or share them."* Exact TTL undocumented. This is why `publish`
  exports at approval time, never at draft time.
- Pro → lossless PNG, transparent backgrounds. Free → standard.
- `license_required` = a premium element is in the design; swap it.

## Handoff — Canva's own rule

Always surface the edit URL, before or alongside any export:
`https://www.canva.com/design/{design_id}/edit`. "Don't end the workflow at export."
For us that maps perfectly onto approve-then-publish: she can adjust in Canva,
then say the approval word.
