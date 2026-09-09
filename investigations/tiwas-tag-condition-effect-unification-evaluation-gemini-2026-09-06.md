# Project Documentation Report: Tag-Condition-Effect Unification Evaluation

**Author:** Gemini 2.5 Pro

**Date:** September 6, 2026

**Project:** Tiwas TTRPG Engine — Core Mechanics Consolidation

**Document Classification:** Design Evaluation & Decision Draft (Non-Canonical / Designer Ruling Level)

---

## Executive Summary

This report evaluates the proposed mechanical unification of **Tags**, **Conditions**, and **Effects** into a single system architecture.

The proposed unification is **mechanically net-negative if adopted in full**, but **strongly positive if adopted partially as a Data-Layer Schema Standard**. Standardizing data records onto a single schema ($\text{Tier } Y, \text{Magnitude } Z, \text{Location } X$) eliminates rulebook record fragmentation without violating core constraints. However, introducing dynamic runtime features—such as "Tags Counter Tags" and active tag removal—transforms a stateless, read-only vocabulary layer into an active resolution engine. This reintroduces a parallel state-tracking pipeline, increases Cognitive Table Load, and directly invalidates locked system guardrails (DEC-007.A, DEC-025, DEC-080, Invariant 17).

We recommend a **Data-Unified, Functional-Split Architecture**: adopt the universal record schema while strictly preserving the functional distinctions between Tags (read-only metadata), Effects (transactional payloads), and Conditions (stateful detriments).

---

## 1. Architectural Definition of the Unified Record Schema

"One mechanical backbone" does not mean treating a character trait, an active wound, and an instant damage application as identical runtime objects. Instead, it means that all game entities inherit from a single structural record format:

$$\text{Record Schema} = \langle \text{ID}, \text{Type}, \text{Subtype}, \text{Tier } Y, \text{Magnitude } Z, [\text{Location } X], \text{State Flags} \rangle$$

### Schema Field Specifications

* **Type Discriminator:** Categorizes functional execution (`Tag` | `Effect` | `Condition`).


* **Subtype Classification:** Domain identifier (e.g., `Equipment`, `Trait`, `Environmental`, `Harm`).


* **Tier $Y$ ($Y \in \mathbb{N}_0$):** Structural permission or complexity level ($Y=0$ Universal, $Y=1$ Skill/Equipment, $Y=2$ Advanced/Special).


* **Magnitude $Z$ ($Z \in \mathbb{Z}$):** Intensity value.


* For passive metadata (`Tag`), $Z = 0$.


* For transactional payloads (`Effect`), $Z$ represents scalar impact.


* For active detriments (`Condition`), $Z = -Y$ per DEC-079.




* **Location Index $X$ (Optional):** Zero-Step Location Index anchoring the record to a spatial or anatomical node (DEC-017, DEC-028).


* **State Flags:** System lifecycle attributes (`[Read-Only]`, `[Persistent]`, `[Transient]`, `[Transactional]`).



```
                              ┌─────────────────────────┐
                              │  UNIFIED RECORD SCHEMA  │
                              │  Type, Subtype, Tier Y, │
                              │ Magnitude Z, Location X │
                              └────────────┬────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
┌─────────────────┐               ┌─────────────────┐               ┌─────────────────┐
│       TAG       │               │     EFFECT      │               │    CONDITION    │
│  [Persistent]   │               │   [Transient]   │               │   [Transient]   │
│ Identity/Access │               │ S-1 Payload     │               │ Track B State   │
│ Z=0 (Read-Only) │               │ Applied via S-1 │               │ Z = -Y          │
└─────────────────┘               └─────────────────┘               └─────────────────┘

```

### Fiction-Level Preservation

* **Tag:** Passive metadata establishing identity, vocabulary, or environmental context. Holds $Z = 0$, `[Persistent]`, and `[Read-Only]`.


* **Effect:** The immediate outcome payload of a winning S-1 Core Test Transaction. Holds variable $Z$, `[Transactional]`, and `[Transient]`.


* **Condition:** Ongoing, trackable mechanical state modifying actor performance. Holds $Z = -Y$, `[Transient]`, and active decay/removal hooks.



---

## 2. Impact Analysis of Proposed Hypotheses

### Hypothesis 1: "Tags default to persistent; Effects default to temporary."

* **Systemic Changes:** Establishes a deterministic baseline lifespan across all game entities based on their origin.


* **Conflicts & Friction:** Conflicts with DEC-028/041 (where tags on equipment gate S-3 Effects) and DEC-060/079 (where specific tags like `Sundered` represent semi-permanent state changes requiring repair).


* **Systemic Fixes:** Eliminates ambiguous decay and duration tracking for non-Condition transactional outcomes.



### Hypothesis 2: "Effects can be made permanent via Tier/Magnitude; Tags convert via Tiers."

* **Systemic Changes:** Allows high-potency S-1 Effects to write permanent structural Tags directly onto target entities or environments.


* **Conflicts & Friction:** Violates DEC-080 and Invariant 17 (read-only tag layer) if an Effect bypasses dedicated recovery/repair engines (S-4/S-5) to mutate core entity records.


* **Systemic Fixes:** Solves permanent environmental and structural transformations (e.g., permanently sealing a doorway with ice).



### Hypothesis 3: "Tags carry Tier $Y$, Magnitude $Z$, and Location $X$."

* **Systemic Changes:** Standardizes metadata structures across items, abilities, hazards, and zones.


* **Conflicts & Friction:** None. Existing designs already rely on Location gating (DEC-028) and Tier permissions (DEC-023).


* **Systemic Fixes:** Removes structural redundancy across the code base, unifying parsing and presentation formats.



### Hypothesis 4: "Tags can Counter other Tags (e.g., Night-Vision counters darkness)."

* **Systemic Changes:** Converts static vocabulary tokens into active runtime evaluation expressions ($A \text{ negates } B$).


* **Conflicts & Friction:** **Severe.** Directly violates DEC-058, DEC-079, DEC-080, and REQ-017 (Tags must remain read-only and stateless). Forces the GM or execution engine to evaluate dynamic tag interaction matrices during play.


* **Systemic Fixes:** Bridges the interaction gap between actor capabilities and environmental hazards (`trait:night-vision` vs. `env:darkness`).



### Hypothesis 5: "Tags and Conditions are NOT distinct; Tags can be Removed."

* **Systemic Changes:** Merges Condition tracking directly into the Tag subsystem, treating Conditions as "Transient Tags".


* **Conflicts & Friction:** **Severe.** Violates Proposals §11 ("Tags are not Conditions") and DEC-079 ($Z = -Y$ math and dedicated stacking/removal pipelines). Collapses the distinction between permanent physical entity metadata (e.g., `Dwarf`) and temporary detriment (e.g., `Prone`).


* **Systemic Fixes:** Eliminates a separate record schema for tracking Track-B detriments.



---

## 3. Complexity Math & Systemic Overhead

Unification does not remove complexity; it shifts complexity between structural architecture and runtime execution.

| Dimension | Separate Subsystems (Baseline) | Fully Unified Proposal |
| --- | --- | --- |
| **Record Formats** | 3 distinct schemas (Tags, Effects, Conditions)

 | **1 universal schema**<br> |
| **Rulebook Text Surface** | ~15 pages of fragmented subsystem rules

 | **~6 pages of unified schema rules**<br> |
| **Runtime Lookup Burden** | Low (read tag $\rightarrow$ check binary permission)

 | **High** (evaluate tag tiers, counter-tags, magnitudes)

 |
| **Resolution Integrity** | Single-path via Core Test Transaction (S-1)

 | Multi-path via implicit tag-subtraction operations

 |
| **State Tracking** | Centralized in S-4 Harm / Condition pipelines

 | Distributed across all active entity tags

 |

**Evaluation:** Standardizing schema records reduces rulebook footprint by ~40%. However, enabling active tag countering and tag removal increases Cognitive Table Load by introducing continuous tag-intersection calculations on every test.

---

## 4. Tensions and Guardrail Conflicts

### A. "Tags Counter Tags" vs. The Stateless / Read-Only Guardrail

DEC-080 and Invariant 17 establish that Tags carry identity and vocabulary only; they possess no state, manage no resources, and execute no dynamic logic. Allowing Tags to counter each other transforms passive metadata into an active logic layer.

*Scope Dilemma:* If an actor's `trait:night-vision` counters `env:darkness`, does it suppress the tag globally for the zone or locally for the actor? Resolving this locally requires attaching context-sensitive state evaluations to a read-only metadata tag.

### B. "Tags and Conditions Merged" vs. $Z = -Y$ Stacking Models

Conditions require explicit operational tracking: $Z = -Y$ numerical penalties (DEC-079), tick durations, and clear clearing procedures (e.g., First Aid). Tags are static classification markers. Forcing them into a single concept forces standard Tags to carry dynamic state fields ($Z = -Y$, tick counters) or forces Conditions to lose their quantitative mathematical behavior.

### C. Permanence / Removal vs. The Single Resolution Engine

Invariant 18 mandates that all game outcomes flow through the Core Test Transaction (S-1). If Tags can be dynamically removed by named actions outside of an S-1 contest or dedicated S-4/S-5 maintenance pipeline, it creates an unmonitored back-door state modification pathway.

### D. Threat to DEC-025 (Skill-Tag Prohibition)

DEC-025 explicitly prohibited a formal tag/category system on Advanced Skills to prevent players from constructing degenerate tag-synergy builds. If Tags acquire explicit structural tiers, magnitudes, and counter-mechanics, players will inevitably demand skill-side tags to interact with the tag-countering matrix. Full unification strongly threatens DEC-025.

---

## 5. Concrete Recommended Design Draft

We recommend adopting a **Data-Unified, Functional-Split System**. This satisfies the desire for a single implementation data schema while strictly enforcing functional boundaries during play.

### 1. The Unified Data Record

All metadata, outcome payloads, and ongoing detriments inherit from a single record implementation:

$$\text{Record} = \{\text{ID}, \text{Type}, \text{Tier } Y, \text{Magnitude } Z, [\text{Location } X], \text{Flags}\}$$

* **Tags:** `Type: Tag`, $Z = 0$, `Flags: [Read-Only, Persistent]`.


* **Effects:** `Type: Effect`, $Z = \text{Value}$, `Flags: [Transactional, Transient]`.


* **Conditions:** `Type: Condition`, $Z = -Y$, `Flags: [Stateful, Transient]`.



### 2. Rejection of Dynamic "Tag-Countering"

Runtime tag-vs-tag subtraction matrices are rejected to protect DEC-080.

* **Operational Resolution:** Environmental conditions (`env:darkness`) act as **Task Difficulty Gates / Permission Requirements** checked during S-1 roll assembly, *not* as active tag interactions.


* *Example:* `env:darkness` imposes a test permission gate. `trait:night-vision` satisfies the requirement to bypass the gate. `night-vision` does not "destroy" or "counter" `darkness`; it fulfills an access check.



### 3. Preservation of Condition Architecture

Conditions remain a distinct `Type` within the universal record schema. They use $Z = -Y$ and are generated exclusively via S-1 Effects (DEC-023) or S-4 Wounds (DEC-032). Tags cannot be "removed" via routine combat actions; modifying item or entity tags requires explicit structural repair, healing, or environmental mutation actions.

### Summary of Governance Status Impacts

* **Replaces (Non-Canonical):** Draft record structures in DEC-079 / Proposals §11.


* **Preserves (Canonical/Locked):** DEC-007.A (Overflow Immutability), DEC-080 / REQ-017 (Read-Only Tags), Invariant 17 & 18 (Single Resolution Engine & Primary Resource Protection), DEC-025 (Skill-Tag System Prohibition).



---

## 6. Open Questions for Final Ruling

1. **Schema Enforcement on Equipment Traits:** Should equipment traits (`[Armor-Piercing]`) be typed as `Type: Tag` with $Z=0$, or do they carry native Magnitude $Z$ to define bypass severity directly?


2. **Environmental Mutation Life-Cycle:** When an S-1 Effect alters a zone (e.g., collapsing a bridge node), does it write a persistent `Tag` to the Location Provider or create an ongoing `Condition` on the zone?


3. **S-6 Defense Gating Integration:** If defensive gear prevents an Effect (e.g., `Locked Gauntlets` preventing `Disarm`), is this evaluated as a hard Tag-permission gate during S-1 assembly, or as an active S-6 reaction trigger?