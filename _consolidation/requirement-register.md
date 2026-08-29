---
document:
  title: "Requirement Register"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Phase 2 — Requirement Register

Requirements are grouped by whether they bind game mechanics (Canonical) or bind implementation/process/documentation behavior (non-canonical but still real constraints per the corpus).

## Canonical architectural requirements (binding on every future subsystem)

| ID | Requirement | Source | Status | Satisfied? |
|---|---|---|---|---|
| REQ-001 | d100 must produce 1–100; `00`=100 | D1 §16.1 | Canonical | N/A — definitional |
| REQ-002 | 100 always fails | D1 §16.2 | Canonical | N/A |
| REQ-003 | 100 is always a qualifying failed Double | D1 §16.3 | Canonical | N/A |
| REQ-004 | All fractions floor | D1 §16.4 | Canonical | N/A |
| REQ-005 | Success is roll-under | D1 §16.5 | Canonical | N/A |
| REQ-006 | Cost equals the natural roll | D1 §16.6 | Canonical | N/A |
| REQ-007 | Overflow becomes HP damage | D1 §16.7 | Canonical | N/A |
| REQ-008 | Failure XP = max(0, Roll − Skill) | D1 §16.8 | Canonical | N/A |
| REQ-009 | Skill Roll Pool is temporary (single failed test only) | D1 §16.9 | Canonical | N/A |
| REQ-010 | Skill Roll Pool advancement cannot exceed Cap | D1 §16.10 | Canonical | N/A |
| REQ-011 | General XP can exceed Cap | D1 §16.11 | Canonical | N/A |
| REQ-012 | Only failed Doubles create Advanced Skills | D1 §16.12 | Canonical | N/A |
| REQ-013 | Advanced Skill Caps recalculated from the full attribute set | D1 §16.13 | Canonical | N/A |
| REQ-014 | Advanced Skill resource domain follows original lineage | D1 §16.14 | Canonical | N/A |
| REQ-015 | Derived statistics are live | D1 §16.15 | Canonical | N/A |
| REQ-016 | Recovery always occurs last | D1 §16.16 | Canonical | N/A |
| REQ-017 | No Universal Play subsystem may introduce a competing primary resource/progression economy | D1 §16.17; reiterated D2 §2, §14 (Extended Test Progress), §17 | Canonical | N/A |
| REQ-018 | Universal Play modules must build on the Core Test Transaction, not replace it | D1 §16.18; D2 §2, §26 | Canonical | N/A |

These 18 requirements are, in effect, the acceptance criteria every subsystem in Sections B onward of the Roadmap (D2) must satisfy. D2 §21 restates them as the "Mandatory Regression Matrix."

## Implementation/process requirements (non-canonical, but binding on how work proceeds per D2/D3)

| ID | Requirement | Source | Status |
|---|---|---|---|
| REQ-019 | No Universal Play implementation may bypass the Core regression suite (Phase 0) | D2 §7 | Non-canonical, project-process |
| REQ-020 | Roadmap may not independently decide numerical thresholds, final Quality rules, wound severity, death triggers, armour mechanics, defence costs, or other unresolved designer decisions | D2 §1 | Non-canonical, self-limiting on D2 itself |
| REQ-021 | A proposal may become canonical only after the 8-step Promotion Rule (design question identified → alternatives considered → simulation/analysis complete → designer acceptance → formal documentation → Canonical update → prior status marked Superseded/Locked → implementation docs updated) | D3 §21 | Non-canonical process requirement — governs *this consolidation's* own Phase 3/4 gates as well |
| REQ-022 | LLM sessions must never silently resolve an open designer fork (16-item list) | D2 §24 | Non-canonical, LLM-governance requirement — directly relevant to this consolidation's own conduct |
| REQ-023 | Documentation Maintenance Rule: when a rule locks / a proposal changes / an implementation decision changes, specific documents must be updated and Canonical Rules must not be touched except through formal governance | D2 §25 | Non-canonical, documentation-process requirement |
| REQ-024 | E9 usability evidence must not be treated as covering untested input methods (single d100, digital roller, verbal) | D1 §14.5–§14.6; D3 §2.6, §2.8 | Canonical-adjacent evidentiary-scope requirement — repeated verbatim in both Canonical Rules and Proposals/WIP, so both documents agree it binds interpretation of E9 |
| REQ-025 | Comparative derivation-cost residual (Units-Digit 0–1 ops vs. Zero-Step 1–2 ops) must be kept labeled as a structural comparison, never as a second usability finding | D1 §14.6; D3 §2.8 | Same as REQ-024 |

## Contradictory-requirement check

No pair of requirements in this register was found to directly contradict another. The closest candidate — REQ-017/REQ-018 (no competing resource/progression economy) versus D3 §9's Extended Test "Progress" concept — is explicitly resolved *within the corpus itself*: D3 §9.4 states Progress "must never become... a second advancement economy," i.e., the proposal was written to comply with REQ-017, not to violate it. Recorded here for traceability, not as an open conflict.
