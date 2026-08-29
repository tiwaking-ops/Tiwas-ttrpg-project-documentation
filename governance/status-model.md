---
document:
  title: "Document Status Model"
  version: "1.0"
  status: "Governance — reconstructed from source corpus"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Document Status Model

## Status vocabulary (per D1's own header)

- **Canonical / Locked** — authoritative, current, must not be contradicted by downstream design/implementation.
- **Reserved** — a known required subsystem with no settled implementation yet.
- **Historical / Superseded** — retained for understanding, no longer current.

## Expanded vocabulary used in Proposals/WIP (D3 §0)

| Status | Meaning |
|---|---|
| Proposed | A candidate rule under active consideration |
| WIP | Currently being developed or reviewed |
| Experimental | Tested/invented for exploration but explicitly excluded from the ruleset |
| Design Direction | An architectural or philosophical preference, not necessarily a mechanic |
| Reserved | Known required subsystem with no settled implementation |
| Superseded | Historical material retained for understanding but no longer current |

None of Proposed / WIP / Experimental / Design Direction / Reserved / an "observation" is a locked rule (D3 §0 explicit instruction).

## Evidence classes (D2 §23.2 / D3's implicit usage)

- **Mechanical fact** — directly follows from existing locked rules.
- **Empirical finding** — supported by simulation, playtesting, or other explicit evidence (e.g., the E9 usability playtest, the Named-Outcome 21/21 trial).
- **Designer ruling** — a deliberate choice not mathematically forced by the system.
- **Recommendation** — a proposed preference not yet accepted.
- **Architectural constraint** — governs how systems interact, not what a mechanic numerically does.

An empirical finding does not itself establish a designer ruling. An architectural constraint does not establish a numerical mechanic. This project's source material is unusually careful about labeling which evidence class a given statement belongs to (see e.g. D1 §14.5 vs §14.6; D3 §2.6 vs §2.8) — that discipline should be preserved in all future additions to this repository.

## Status lifecycle (D2 §23.1)

```text
Idea → Proposal → WIP → Independent Review → Simulation/Analysis → Designer Ruling → Accepted → Locked/Canonical
```

An item may return to WIP if evidence exposes a substantive problem.

## Promotion Rule (D3 §21) — the only path from non-canonical to canonical

1. The design question is explicitly identified.
2. Competing alternatives have been considered where appropriate.
3. Relevant simulation/analysis has been completed.
4. The human designer has accepted the ruling.
5. The mechanic is documented as a formal rule.
6. The Canonical Rules & Changelog document is updated.
7. The former proposal is marked Superseded or Locked in its source document.
8. Implementation documentation is updated.

No item currently in `proposals/` or `investigations/` in this repository has completed this process — see `_consolidation/decision-register.md` §B. A detailed proposal, however fully described, is not a rule merely because it is detailed (D3 §21).

## LLM Governance Rules (D2 §24) — binding on any LLM working in this repository going forward

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
4. Never promote a proposal because it appears repeatedly in documentation.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. Never silently resolve an open designer fork.
7. Identify contradictions between current and historical documents.
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
14. When a subsystem is locked, update the Canonical document and its changelog.
15. When a proposal is superseded, retain its historical significance but mark it Superseded.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

This consolidation has attempted to follow these same rules in reorganizing the corpus (e.g., it did not promote DEC-017–DEC-022 to canonical status merely because they are described in exhaustive detail across three documents — see `_consolidation/decision-register.md`).
