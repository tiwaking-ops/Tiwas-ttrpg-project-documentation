---
document:
  title: "Provenance Rules"
  version: "1.0"
  status: "Governance"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Provenance Rules

## Mandatory metadata block

Every document created by an LLM in this repository must open with a metadata block identifying `author_llm`, `assessor_llm`, and `last_modified_by_llm` (each with `name` and `version`), plus `created_date` and `last_modified_date`. Use `unknown` or `not established` rather than inventing a value — see below.

## Role distinction

- **author_llm** — the original creator. Never overwritten by later editors, even if they substantially rewrite the document.
- **assessor_llm** — reviews for factual/documentary consistency, canonical-status accuracy, provenance, or structure. An assessment is not a human decision and does not confer authority.
- **last_modified_by_llm** — the most recent substantive editor. Updated on material changes; formatting-only changes may be handled per future project policy, not yet defined here.

## This consolidation's own provenance

All newly created documents in this initial consolidation (everything outside `sources/`) were authored, assessed, and last-modified by the same model in a single pass:

```yaml
author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
```

This is recorded honestly rather than treated as more robust than it is: a single model authoring and "assessing" its own output is a weaker form of review than an independent second pass. Future stewardship should consider having a separate session/model perform the `assessor_llm` role for consequential changes, particularly before anything is promoted out of `_consolidation/proposed/` into `canonical/`.

## Original source document provenance

The author LLM/human and version for D1–D5 (the five source documents) are **not established** — none of the five documents carries in-document authorship metadata, and no separate provenance record accompanied the corpus. This is recorded as `not established` throughout `_consolidation/document-inventory.md` rather than inferred from writing style, formatting, or any other indirect signal, per the governing specification's explicit prohibition on inferring authorship from style.

## Historical/archive documents

No documents have been moved to `archive/` in this consolidation pass (see `archive/README.md` for why). If and when material is archived in the future, any needed provenance metadata must be attached as an external wrapper around the preserved historical content — never edited into the historical text itself.
