# DEC-080: Tags Vocabulary — Formal Decision Record

**Document Type:** Formal Project Documentation Report  
**Project:** Tiwas Tabletop Role-Playing Game (Tiwas TTRPG)  
**Document ID:** DEC-080  
**Document Version:** v1.0  
**Document Status:** Proposed — Pending Human Approval  
**Date:** 2026-09-03 09:55 NZST  
**Author:** Perplexity AI (Model: Perplexity)  
**Reviewer:** Tiwaking (Human)  

---

## 1. Executive Summary

This document records the formal design decision **DEC-080 (Tags Vocabulary)** for the Tiwas TTRPG project. The decision establishes an open, extensible, namespace-based ontology for Tags, adopts a 34-tag alpha vocabulary as the foundational set, permits future extensions through normal project governance, separates Tag identity from mechanical effects, and allows multiple Tags to coexist on the same object, entity, or scene.

**Decision Status:** Awaiting human confirmation via structured approval questions.

---

## 2. Decision Context

### 2.1 Background

Tags serve as a first-class metadata layer in the Tiwas architecture, supporting the Universal Play Module pattern (e.g., U-12 Conditions, U-14 Equipment Tags). [cite:1][cite:2] Prior documentation reserved Tags as an architectural requirement without locking vocabulary or ontology rules. [cite:2]

### 2.2 Problem Statement

The Tiwas TTRPG project requires a formal, auditable decision record that:

1. Defines the Tag ontology structure.
2. Locks the initial Tag vocabulary.
3. Establishes governance for future Tag additions.
4. Clarifies the separation between Tag identity and mechanical effects.
5. Specifies Tag coexistence rules.

### 2.3 Authority Boundary

This decision record creates no game mechanics. It defines vocabulary and architectural constraints only. Mechanical effects are defined by consuming subsystems (Equipment, Conditions, Outcome Effects, etc.) through separate governance decisions. [cite:1][cite:2]

---

## 3. Decision Record

### 3.1 Decision Questions and Rulings

| Question ID | Question | Decision | Rationale |
|---|---|---|---|
| **Q1** | Namespace ontology | **YES** — Open, extensible, namespace-based ontology | Enables qualified names (e.g., `alpha:fire`, `setting:tc_industries:corporate`) to prevent collisions across subsystems and settings. Supports the Core/Universal Play/Setting architecture. [cite:2] |
| **Q2** | Alpha vocabulary | **YES** — Adopt the exact 34-tag alpha vocabulary | Establishes the foundational Tag set for initial implementation. All future Tag additions must follow the normal promotion process (Proposals → Canonical Rules → Manifest update). [cite:1][cite:2] |
| **Q3** | Extensibility | **YES** — Alpha vocabulary may be extended through normal project governance | Ensures the Tag system can evolve without requiring architectural changes. Extensions follow the standard eight-step promotion process defined in project governance documentation. [cite:1][cite:2] |
| **Q4** | Tag semantics | **YES** — DEC-080 defines Tag identity/vocabulary; consuming subsystems define mechanical effects | Maintains separation of concerns. DEC-080 locks *what Tags exist*, not *what they do*. Mechanical effects are defined by subsystems such as Equipment, Conditions, or Outcome Effects. [cite:1][cite:2] |
| **Q5** | Tag coexistence | **YES** — Multiple Tags may coexist on the same object/entity/scene | Enables compound metadata (e.g., an item can be `alpha:fire` + `alpha:fragile` + `setting:weapon`), supporting the granular simulation priority stated in design direction. [cite:2] |

---

## 4. Architectural Implications

### 4.1 Namespace Ontology (Q1)

- Tags are identified by **qualified names** using colon-separated namespaces.
- Example format: `namespace:tag_name` or `namespace:subnamespace:tag_name`.
- Prevents naming collisions between Core Tags, setting-specific Tags, and third-party extensions.
- Consistent with the setting module architecture where settings add content and permissions rather than rewrite the Core engine. [cite:2]

### 4.2 Alpha Vocabulary (Q2)

- The **34-tag alpha vocabulary** becomes the foundational Tag set.
- All Tags in this set are available for immediate use in Universal Play Modules.
- Future additions require explicit approval, incorporation into Canonical Rules, and Manifest updates. [cite:1]

### 4.3 Extensibility (Q3)

- New Tags may be added through the standard promotion process:
  1. Proposed in `TTTRPG — Proposals, WIP & Design Direction`.
  2. Approved by human reviewer.
  3. Incorporated into `TTTRPG — Canonical Rules & Changelog`.
  4. Manifest updated to reflect locked status. [cite:1][cite:3]
- No architectural changes required for vocabulary extensions.

### 4.4 Tag Semantics (Q4)

- **DEC-080 scope:** Defines Tag identity and vocabulary only.
- **Out of scope:** Mechanical effects, which are defined by consuming subsystems.
- Example: `alpha:fire` as a Tag is defined here; its interaction with Armor (U-10), Conditions (U-12), or Outcome Effects (U-05) is defined elsewhere. [cite:1]

### 4.5 Tag Coexistence (Q5)

- Multiple Tags may be applied to the same object, entity, or scene.
- Enables rich metadata combinations for granular simulation.
- Example: A weapon might carry Tags `alpha:fire`, `alpha:fragile`, `setting:tc_industries:corporate_asset`. [cite:2]

---

## 5. Implementation Guidance

### 5.1 Required Actions

1. **Human Approval** — Reviewer must confirm all five decisions via structured questions (Section 7).
2. **Canonical Rules Update** — Incorporate DEC-080 into the next version of `TTTRPG — Canonical Rules & Changelog`.
3. **Manifest Update** — Record DEC-080 locked status in `MANIFEST.md`.
4. **Proposals Document Update** — Move Tags from "Reserved" to "Locked (DEC-080)" in `TTTRPG — Proposals, WIP & Design Direction`. [cite:1][cite:2][cite:3]

### 5.2 Downstream Dependencies

The following Universal Play Modules may consume DEC-080 Tags:

- **U-12 Conditions** — Reusable state effects. [cite:1]
- **U-14 Equipment Tags** — Interaction metadata. [cite:1]
- **U-05 Outcome Effects** — Converts success into state change. [cite:1]
- **U-10 Armor** — Equipment/harm interaction. [cite:1]
- **U-22 Setting Interface** — Isolate setting rules. [cite:1]

### 5.3 Regression Requirements

No Core regression tests are affected by DEC-080, as it defines vocabulary only. However, any subsystem implementing Tag-based mechanics must preserve:

- d100 = 1–100; `00` = 100.
- Roll-under resolution.
- Mandatory 100-Fumble; 100 as failed Double.
- Floor rounding.
- Core resource and Overflow rules. [cite:1]

---

## 6. Governance Compliance

### 6.1 Authority Hierarchy

This decision record complies with the Tiwas authority hierarchy:

1. **Canonical Rules & Changelog** — DEC-080 will be incorporated here upon approval.
2. **Proposals, WIP & Design Direction** — Tags status updated post-approval.
3. **Implementation Roadmap & Project Governance** — Implementation sequencing guidance only. [cite:1][cite:2][cite:3]

### 6.2 Promotion Process

DEC-080 follows the standard promotion rule:

1. Explicit approval by human reviewer. [cite:2]
2. Incorporation into Canonical Rules. [cite:1][cite:2]
3. Manifest update. [cite:2]

No other process (including detailed description in this document, simulation success, or LLM consensus) creates Canonical status. [cite:2]

---

## 7. Approval Questions for Human Reviewer

**OpenCode must present the following questions to the human reviewer (Tiwaking) to confirm this decision record before it becomes Canonical:**

---

### Approval Question 1: Namespace Ontology

> **Q1.** Do you approve the adoption of an **open, extensible, namespace-based ontology** for Tags, where Tags are identified by qualified names (e.g., `alpha:fire`, `setting:tc_industries:corporate`) to prevent collisions across subsystems and settings?
>
> - [ ] **YES** — Approve as stated.
> - [ ] **NO** — Revise decision.
> - [ ] **DEFER** — Require further investigation.

---

### Approval Question 2: Alpha Vocabulary

> **Q2.** Do you approve the adoption of the **exact 34-tag alpha vocabulary** as the foundational Tag set for Tiwas TTRPG, with all future Tag additions requiring the normal promotion process (Proposals → Canonical Rules → Manifest update)?
>
> - [ ] **YES** — Approve as stated.
> - [ ] **NO** — Revise decision.
> - [ ] **DEFER** — Require further investigation.

---

### Approval Question 3: Extensibility

> **Q3.** Do you approve that the **alpha vocabulary may be extended through normal project governance**, ensuring the Tag system can evolve without requiring architectural changes?
>
> - [ ] **YES** — Approve as stated.
> - [ ] **NO** — Revise decision.
> - [ ] **DEFER** — Require further investigation.

---

### Approval Question 4: Tag Semantics

> **Q4.** Do you approve that **DEC-080 defines Tag identity/vocabulary only**, while **consuming subsystems define mechanical effects** (e.g., Equipment, Conditions, Outcome Effects)?
>
> - [ ] **YES** — Approve as stated.
> - [ ] **NO** — Revise decision.
> - [ ] **DEFER** — Require further investigation.

---

### Approval Question 5: Tag Coexistence

> **Q5.** Do you approve that **multiple Tags may coexist on the same object, entity, or scene**, enabling compound metadata (e.g., `alpha:fire` + `alpha:fragile` + `setting:weapon`)?
>
> - [ ] **YES** — Approve as stated.
> - [ ] **NO** — Revise decision.
> - [ ] **DEFER** — Require further investigation.

---

## 8. Document Control

| Field | Value |
|---|---|
| **Document ID** | DEC-080 |
| **Document Type** | Formal Decision Record |
| **Project** | Tiwas TTRPG |
| **Version** | v1.0 |
| **Status** | Proposed — Pending Human Approval |
| **Author** | Perplexity AI (Model: Perplexity) |
| **Reviewer** | Tiwaking (Human) |
| **Date Created** | 2026-09-03 09:55 NZST |
| **Date Approved** | [Pending] |
| **Supersedes** | None |
| **Superseded By** | [None — Current Version] |
| **Related Documents** | `TTTRPG — Canonical Rules & Changelog`, `TTTRPG — Proposals, WIP & Design Direction`, `MANIFEST.md`, `TTTRPG — Implementation Roadmap & Project Governance` [cite:1][cite:2][cite:3] |

---

## 9. References

[cite:1] Tiwas TTRPG — Canonical Rules & Changelog (v1.3 and v2.0 consolidated material).  
[cite:2] TTTRPG — Proposals, WIP & Design Direction (v2.0).  
[cite:3] TTTRPG — Implementation Roadmap & Project Governance (v1.4.3 and v2.0).  
[cite:4] MANIFEST.md (Tiwas TTRPG project governance).  

---

**End of DEC-080 Formal Decision Record**
