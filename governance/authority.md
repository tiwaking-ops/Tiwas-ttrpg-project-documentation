---
document:
  title: "Documentation Authority Hierarchy"
  version: "1.0"
  status: "Governance — reconstructed from source corpus, self-consistent across all five source documents"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Documentation Authority Hierarchy

This restates the authority structure that the five source documents already, consistently, declare about themselves and each other (see `_consolidation/relationship-map.md` for full evidence). It is not a new decision — it is a direct transcription of self-declared status headers and explicit cross-references, corroborated across multiple documents rather than resting on any single one.

## 1. `canonical/` — Canonical Rules (D1)

The Canonical Rules & Changelog is the sole source of locked game mechanics. Per its own §0.1:

1. Canonical Rules & Changelog — current locked mechanics.
2. Proposals, WIP & Design Direction — unresolved and experimental design material.
3. Implementation Roadmap & Project Governance — implementation sequencing and project-management guidance.

The latter two "cannot override" the Canonical document. A mechanic reopens only through the formal governance process described in `governance/status-model.md`, never through implementation convenience, LLM preference, or repetition across documents.

## 2. `roadmap/` — Implementation Roadmap & Project Governance (D2)

Explicitly disclaims rule authority ("Rule Authority: None — this document does not create game mechanics"). Governs sequencing, dependencies, simulation gates, regression requirements, and LLM/documentation process rules. Must never be read as a source of game mechanics, even where it restates Canonical invariants for implementers' convenience.

## 3. `proposals/` — Proposals, WIP & Design Direction (D3)

Explicitly "Non-Canonical Design Repository... Design exploration only." Contains real designer rulings (see `decision-register.md` §B) but those rulings govern *candidate, non-canonical* material, not the Canonical ruleset, until the 8-step Promotion Rule (D3 §21, restated in `governance/status-model.md`) is completed.

## 4. `investigations/` — Design investigations feeding Proposals/WIP (D4, D5)

Evidentiary and analytical work product. Never self-executing — D4 and D5 both explicitly require designer/human ruling before anything they contain affects even the non-canonical Proposals/WIP layer, and neither claims any effect on Canonical Rules.

## Cross-document consistency

No document in the supplied corpus attempts to claim authority over another in a way that contradicts this hierarchy. See `_consolidation/conflict-register.md` for the full check.

## Application to this consolidated repository

- Only material with clear evidence of Canonical status per D1 has been placed in `canonical/`.
- `roadmap/`, `proposals/`, and `investigations/` hold their respective source documents' content, unaltered in substance, reorganized only by location.
- No promotion beyond what the corpus itself already documents has been performed by this consolidation. Where this consolidation had to choose a folder for content whose status was already unambiguous and self-declared, that placement is noted in `_consolidation/consolidation-plan.md` as a low-risk classification, still open to your review.
