---
document:
  title: "Provenance Rules"
  version: "1.0"
  status: "Governance"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
    - {name: "nemotron-3-super-120b-a12b:free", version: "unknown"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-31"
---

# Provenance Rules

## Mandatory metadata block

Every document created by an LLM in this repository must open with a metadata block identifying `author_llm`, `assessor_llm`, and `last_modified_by_llm` (each with `name` and `version`), plus `created_date` and `last_modified_date`. Use `unknown` or `not established` rather than inventing a value — see below. `assessor_llm` may be a **list** when more than one assessment pass has been performed (e.g., an original authoring-session assessment followed by an independent second-model assessment appended later); each entry represents one assessment, earliest first.

## Role distinction

- **author_llm** — the original creator. Never overwritten by later editors, even if they substantially rewrite the document.
- **assessor_llm** — reviews for factual/documentary consistency, canonical-status accuracy, provenance, or structure. An assessment is not a human decision and does not confer authority. Where an additional independent assessment is later performed, the independent assessor is **appended** to this field as another entry — the original assessor record is preserved, not overwritten (e.g., per Priority-7 §4.4, the 2026-08-31 append of the nemotron-3-super-120b independent assessor).
- **last_modified_by_llm** — the most recent substantive editor. Updated on material changes; formatting-only changes may be handled per future project policy, not yet defined here.

## This consolidation's own provenance

All newly created documents in this initial consolidation (everything outside `sources/`) were authored, assessed, and last-modified by the same model in a single pass:

```yaml
author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
```

This is recorded honestly rather than treated as more robust than it is: a single model authoring and "assessing" its own output is a weaker form of review than an independent second pass. Future stewardship should consider having a separate session/model perform the `assessor_llm` role for consequential changes, particularly before anything is promoted out of `_consolidation/proposed/` into `canonical/`.

### Independent second-model assessment (appended 2026-08-31)

Per Priority-7 §4.4 and the human approval of 2026-08-31, an **independent second-model assessment** (nemotron-3-super-120b-a12b:free, fresh session — see `audits/INDEPENDENT-ASSESSMENT-2026-08-29.md`) was accepted as satisfying the mandatory independent-assessment gate. Where that assessment covered a document, the independent assessor is appended to that document's `assessor_llm` as a second entry (the original Claude Sonnet 5 assessor record is preserved, not overwritten). Appending an assessor confers no authority — assessment remains review, not promotion.

## Original source document provenance

The author LLM/human and version for D1–D5 (the five source documents) are **not established** — none of the five documents carries in-document authorship metadata, and no separate provenance record accompanied the corpus. This is recorded as `not established` throughout `_consolidation/document-inventory.md` rather than inferred from writing style, formatting, or any other indirect signal, per the governing specification's explicit prohibition on inferring authorship from style.

## Historical/archive documents

No documents have been moved to `archive/` in this consolidation pass (see `archive/README.md` for why). If and when material is archived in the future, any needed provenance metadata must be attached as an external wrapper around the preserved historical content — never edited into the historical text itself.
