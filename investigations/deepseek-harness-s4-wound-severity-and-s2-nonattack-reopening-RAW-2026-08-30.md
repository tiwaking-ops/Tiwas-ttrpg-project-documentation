# S-4 (Wound Activation / Severity) & S-2 Non-Attack Reopening — Formal Design Investigation & Handover Report

**Document Version:** v1.0 (Final)  
**Document Status:** Formal Design Investigation & Handover Report (Non-Canonical)  
**Target Authority:** OpenCode (Lead Documentarian & Integration Agent)  
**Authoring Context:** DeepSeek Harness (Design Assistant / Gemini 3.6 Flash)  
**Primary Governance References:** 
* `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` (D1)
* `proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md` (D3)
* `roadmap/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` (D2)
* `_consolidation/decision-register.md`
* `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` (D5)
* `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`

---

## 1. Executive Summary & Purpose

This formal report captures the design synthesis, analysis, and proposed candidate rulings resulting from the **S-4 (Wound Activation/Severity)** investigation thread. 

The S-4 decision thread represents a major convergence point between **S-2 (Hit-Location Architecture)** and **S-3 (Outcome Effects)**. This session evaluated the Two-Track Harm model, established fundamental terminology distinctions between HP damage and localized wounds, aligned wound creation with S-3 outcome effect choices, and evaluated the reopening trigger for **DEC-020 (S-2 Non-Attack Location Index Source Deferral)**.

This document is prepared specifically for **OpenCode (Lead Documentarian)** to review, audit against the live repository state, and execute any formal register updates, proposal amendments, or promotion workflow steps authorized by the Human Designer.

---

## 2. Key Designer Rulings & Outcomes (Candidate Rulings DEC-032 – DEC-037)

During this session, the Human Designer established explicit rulings overturning prior WIP directions (specifically the "repeated hits to the same location" model from DEC-029) in favor of a choice-based, S-3-integrated harm model.

### 2.1 Terminology Lock: Injury vs. Wound (`DEC-032`)
* **Injury (Track A):** Refers strictly to Hit Point (HP) damage.
* **Wound (Track B):** Refers to a localized, lasting physical state, tracked numerically, distinct from HP damage. Each individual base Wound counter is functionally equivalent.

### 2.2 Wound Activation & Trigger Logic (`DEC-033`)
* **Realized as a Condition:** A Wound is **not** a stand-alone 11th entry on the S-3 Effect menu. It is realized as the **"Wounded" Condition**, selected via S-3 Effect #2 (*Impose Condition*), belonging to the Condition/S-4 Gated Tier (`DEC-023`).
* **Overflow Never Causes Wounds:** Overflow resulting from resource (PE/MP) exhaustion is exclusively Track A (HP damage). Overflow **never** produces a Wound.
* **Location Index Requirement:** Selecting either **Inflict Injury** (Effect #1) or **Impose Condition: Wounded** (Track B) off a successful contest requires a supporting Zero-Step Location Index ("no Location Index = no Injury Effect / no Wound Condition"). Automatic Overflow → HP damage requires no Location Index.

### 2.3 Track A / Track B Interaction (`DEC-034`)
* **Sequential Concurrency:** Both Track A (Overflow → HP) and Track B (*Impose Condition: Wounded*) can resolve from a single exchange. 
* **Core Test Transaction Alignment:** The Core Test Transaction (Canonical §6) resolves resource expenditure and Overflow first. On a successful contest win, the actor then selects and applies an S-3 Effect.

### 2.4 Severity Definition & "Greater Wounds" (`DEC-035`)
* **Numerical Wound Severity:** Wound severity is purely numerical (wound counter). The terms *Light*, *Serious*, and *Critical* are descriptive aggregate categories for accumulated numerical Wounds, not distinct internal states. Specific numerical thresholds for these categories require a simulation gate prior to locking (`OPEN-006`).
* **Independent "Greater Wound" Effects:** Distinct severe elemental/type-based effects (e.g., *Serious Frost*, *Serious Fire*, *Serious Shock*) are independent, distinct Conditions selected via *Impose Condition* (gated by Quality per `DEC-031`). They do not alter or upgrade the state of lower-tier effects and operate independently of base Wound counters. Healing higher-tier Effects may require specialized procedures.

### 2.5 Reopening S-2 Non-Attack Deferral (`DEC-036`)
* **DEC-020 Reopened:** The categorical deferral of non-attack physical resolutions (falls, hazards, collapses) generating a Location Index (`DEC-020`) is **reopened**.
* **Hazard Wounds Permitted:** Non-attack hazards are capable of causing damage or Wounds via Effect selection. A non-attack Location Index generation rule is required (`OPEN-008` / `DEC-037`).

### 2.6 Non-Attack Location Index Generation (`DEC-037` / Proposed `OPEN-008` Closure)
* **Governing Test Provenance:** When a character fails a governing Core Test against an environmental hazard or physical risk (e.g., Jump, Climb, Evasion, Spot Trap), that **same failed d100 roll** supplies the digits for Zero-Step Tier-1 Location Index generation (exchanging tens and units digits per Canonical §14.1–14.2).
* **Hazard "Win":** A failed test against a physical hazard constitutes a "win" for the hazard, allowing selection of an Effect (*Inflict Injury* or *Impose Condition: Wounded*) if severity/margin gates are met.
* **Systemic Harm Exempt:** Global environmental threats acting systemically (e.g., Drowning, Suffocation, Extreme Temperature) apply direct HP damage or systemic Conditions without requiring a Location Index.
* **Passive Stub Fallback:** In the event a character suffers a physical impact without making any roll (e.g., thrown while unconscious), the system outputs a **stub numeric Location Index (e.g., `00` or `50`)** through Zero-Step, preserving the single resolution pipeline and deferring anatomical naming until Anatomical Mapping (`OPEN-003`) locks.

---

## 3. Comprehensive Analysis of Open Questions (`OPEN-006` – `OPEN-008`)

| Open Item ID | Title | Summary of Current Status |
|---|---|---|
| **`OPEN-003`** | Anatomical Mapping (Location Index → Body Component) | **Critical Blocker.** Unbuilt table in Canonical §14.3. Any localized Wound Effect relies on this table to map numeric indexes to body regions. |
| **`OPEN-006`** | Wound Severity Thresholds | Numerical count of Wounds required to enter *Light / Serious / Critical* descriptive tiers. Requires simulation gate measuring effect frequency, exchange length, and severe-injury rates. |
| **`OPEN-007`** | Wound & Greater-Wound Consequences | Mechanical disabilities and penalties associated with accumulated Wounds or specific "Greater Wound" Conditions. |
| **`OPEN-008`** | Non-Attack Location Index Generation | Proposed for closure via candidate ruling `DEC-037`. Reuses the affected character's failed interaction roll for Zero-Step index derivation. |

---

## 4. Cross-Document Dependency & Impact Assessment

The outcomes of this session impact several core documentation sections:

1. **`_consolidation/decision-register.md`:**
   * Section B (Non-Canonical Designer Rulings) requires addition of `DEC-032` through `DEC-037`.
   * `DEC-020` status updated from "Closed as a deferral" to "Reopened via DEC-036 / DEC-037".
   * Section C (Explicitly Unresolved) requires addition of `OPEN-006` and `OPEN-007`, with `OPEN-008` marked closed by `DEC-037`.

2. **`proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md`:**
   * **Section 2.5 & 2.5A (S-2 Non-Attack):** Updated to record the reopening of DEC-020 and the adoption of the governing-roll provenance rule (`DEC-037`).
   * **Section 3.4.4 (S-3/S-4 Boundary):** Updated to state that the prior "repeated hits to the same location" steer is superseded by the choice-based *Impose Condition: Wounded* model.
   * **Section 4 (S-4 Two-Track Harm and Wounds):** Completely revised to reflect Terminology Lock (`DEC-032`), Trigger Logic (`DEC-033`), Sequential Track A/B Concurrency (`DEC-034`), Numerical Severity & Greater Wounds (`DEC-035`), and Non-Attack Reopening (`DEC-036`).
   * **Section 20 (Residual Decision Register):** S-2 and S-4 rows updated.
   * **Section 25:** New Revision Record (v1.4.4) documenting all non-canonical additions.

3. **Canonical Rules (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`):**
   * **UNTOUCHED.** Per REQ-021 (8-step Promotion Rule), no canonical document was modified during this analytical pass.

---

## 5. Handover Checklist for OpenCode

OpenCode should perform the following actions upon receiving the Human Designer's final decision:

* [ ] **Audit Live Decision Register:** Verify next available DEC-xxx and OPEN-xxx IDs in `_consolidation/decision-register.md`.
* [ ] **Apply Rulings DEC-032 – DEC-037:** Record the rulings in `_consolidation/decision-register.md` Section B with exact authority and evidence annotations.
* [ ] **Update Proposals Document:** Update `proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md` Sections 2.5, 2.5A, 3.4.4, 4, 20, and append Revision Record Section 25.
* [ ] **Verify Invariants:** Ensure all added text preserves d100 roll-under, floor rounding, cost = roll, overflow = HP, and minimum resolution steps without introducing secondary dice rolls or competing resolution engines.
* [ ] **Sync Roadmap References:** Update Phase 3 and Phase 5 notes in `roadmap/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` to reference `DEC-032–DEC-037`.