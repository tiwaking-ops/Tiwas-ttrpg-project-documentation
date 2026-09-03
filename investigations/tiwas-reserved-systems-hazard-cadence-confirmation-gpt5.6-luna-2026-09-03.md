# Tiwas TTRPG — Reserved Systems Decision Confirmation Report

## 1. Document Control

| Field | Value |
|---|---|
| **Document Title** | Tiwas TTRPG — Reserved Systems Decision Confirmation Report |
| **Subject** | 5.5 Reserved Systems — Systemic Hazard Resolution Cadence |
| **Project** | Tiwas TTRPG |
| **Status** | **PENDING HUMAN CONFIRMATION** |
| **Author** | **GPT-5.6 Luna** |
| **Author Type** | Large Language Model |
| **Date** | 2026-09-03 |
| **Intended Consumer** | OpenCode |
| **Authority** | Advisory decision-confirmation handoff; not itself a canonical Tiwas ruling |
| **Required Action** | Ask the human designer to confirm each proposed decision before recording or promoting it |

---

# 2. Purpose

This document records the design decisions discussed during the current Tiwas TTRPG design session concerning:

> **5.5 Reserved Systems — Systemic Hazard Resolution Cadence**

The purpose of this document is to provide OpenCode with an exact, auditable record of the decisions currently proposed by the human designer and the reasoning established during the discussion.

**OpenCode MUST NOT treat the decisions in this document as independently authorised canonical changes.**

OpenCode must first present the confirmation questions in Section 7 to the human designer.

No project documentation, canonical rules, decision register, changelog, or implementation artifact may be modified solely because this report exists.

---

# 3. Scope

The discussion concerned the following fork set:

| Fork | Subject |
|---|---|
| **H1** | Systemic hazard resolution cadence |
| **H2** | Scope of the cadence decision |
| **H3** | Whether DEC-037(1) already covers terrain hazards |
| **H4** | Difficulty-grade Skill-side penalty |
| **H5** | Graded Intensity as a lookup key |

The discussion specifically addressed terrain/environmental hazards and the relationship between:

- existing Core Test resolution;
- DEC-037;
- Zero-Step Location Index derivation;
- S-3 Effect resolution;
- systemic hazards;
- difficulty grades;
- hazard intensity;
- hazard resolution cadence.

The discussion did **not** authorise redesign of Zero-Step, the Core Test Transaction, Overflow, XP, or any other closed Tiwas mechanic.

---

# 4. Evidence and Architectural Constraints

## 4.1 Existing Environmental-Hazard Architecture

The project corpus already identifies environmental hazards as an intended use case for existing Core Test infrastructure. The documented preferred structure is:

> Existing Test → Natural Cost → Outcome → Existing Effect/Condition/Harm

This explicitly favours environmental hazards being resolved through an ordinary Core Test Transaction rather than through a competing special-purpose resolution engine.

The same corpus records the governing principle that, where a Core Test exists, its natural d100 roll is available as the Zero-Step input; if no governing Core Test exists, Zero-Step has no input.

## 4.2 DEC-037 Boundary

DEC-037 provides the established non-attack physical-resolution pathway involving a failed governing Core Test and Zero-Step-derived Location Index where Location Index generation is warranted.

The existing adaptation analysis identifies DEC-037 as applicable to environmental hazards and physical risks.

However, the corpus also distinguishes **resolution architecture** from unresolved **hazard-specific content**. For example, exact fall-damage magnitudes are not established by DEC-037 and cannot be silently substituted into Overflow.

## 4.3 Current Hazard Status

The task-scoped snapshot records environmental hazards as partially addressed, with `env:hazard_physical` and `env:hazard_systemic` Tags defined while formalisation remains open.

Therefore:

> **Existing hazard resolution architecture must not be confused with complete hazard-system formalisation.**

---

# 5. Decisions Reached in This Session

## 5.1 H1-A — Systemic Hazard Resolution Represents Progress Toward Surviving

### Proposed Decision

**H1-A — ACCEPT**

A systemic hazard represents an ongoing process of **progress toward surviving the hazard**, rather than being treated as a sequence of unrelated isolated damage events.

### Architectural interpretation

A systemic hazard may therefore represent persistent attritional threats such as:

- prolonged environmental exposure;
- cold exposure;
- sustained hazardous conditions;
- other hazards whose defining property is continued exposure over time.

This interpretation does **not** create a new resource economy.

The existing Tiwas resource and Core Test machinery remains authoritative.

### Constraint

H1-A must not introduce:

- a new resource pool;
- a parallel resolution engine;
- a replacement for Physical Energy;
- a replacement for MP;
- an independent XP economy;
- an alternative to the Core Test Transaction.

---

## 5.2 H2-A — Scope to the S-3 Systemic-Hazard Effect Interface

### Proposed Decision

**H2-A — ACCEPT**

The decision is scoped to the **S-3 systemic-hazard Effect interface**.

### Scope boundary

S-3 may define the relevant consequence/effect interface, but this does **not** mean that S-3 automatically owns every aspect of environmental hazard simulation.

The following remain conceptually distinct:

| Component | Status |
|---|---|
| Hazard Effect / consequence | S-3 interface |
| Core Test | Existing Core system |
| Skill difficulty | S-8 |
| Location Index where warranted | DEC-037 / Zero-Step |
| Resource Cost | Existing Core Test Transaction |
| Overflow | Existing Core rule |
| Failure XP | Existing Core rule |
| Recovery | Existing Core rule |
| Environmental state | Not automatically transferred to S-3 |
| Complete hazard engine | Not created by this decision |

---

# 6. H3-A — Terrain Hazards Are Covered by Existing Resolution Architecture

## 6.1 Final Decision

**H3-A — ACCEPT**

The human designer's proposed interpretation is:

> Terrain hazards are instances of **environmental hazard, obstacle, or physical risk** and are therefore resolved through the existing failed-test → Zero-Step → S-3 Effect pipeline where the existing rules call for those stages.

No separate terrain-hazard resolution mechanism is required.

## 6.2 `env:terrain_*` Tags

`env:terrain_*` Tags are to be understood as:

> **Descriptive/flavour markers only, with no independent mechanical trigger.**

They do not independently initiate:

- a roll;
- a damage roll;
- a location roll;
- a resource expenditure;
- a new hazard subsystem;
- a separate cadence;
- an additional Core Test.

The presence of an `env:terrain_*` Tag therefore does not itself create a mechanical event.

## 6.3 Resolution Principle

Where an applicable terrain hazard requires an existing physical-risk resolution:

```text
Terrain/environmental hazard
        ↓
Existing applicable Core Test
        ↓
Normal Core Test Transaction
        ↓
Failure / established physical consequence
        ↓
DEC-037 / Zero-Step where Location Index is warranted
        ↓
Existing S-3 Effect pathway where applicable
```

The existing corpus explicitly supports the principle that environmental hazards should use the existing Core Test Transaction rather than a parallel hazard engine.

## 6.4 Critical Qualification

H3-A does **not** mean:

> "DEC-037 contains every terrain-specific consequence, severity value, damage magnitude, or hazard parameter."

It means:

> **The mechanism for resolving a terrain hazard does not require a new terrain-specific resolution engine.**

Specific consequence content remains governed by the appropriate existing subsystem or by future authorised content work.

For example, the corpus explicitly identifies source-specific fall-damage dice as not being a currently ruled Tiwas mechanic.

## 6.5 Correction to Earlier Assessment

The earlier assessment in this conversation initially rejected H3-A because it interpreted the phrase "fully covered" too broadly.

That interpretation is superseded.

The correct distinction is:

| Question | Result |
|---|---|
| Is the terrain-hazard **resolution architecture** already covered? | **Yes** |
| Does DEC-037 create a separate terrain-hazard subsystem? | **No** |
| Does DEC-037 specify every possible terrain consequence? | **No** |
| Are `env:terrain_*` Tags independent mechanical triggers? | **No** |
| Is additional terrain-specific content potentially required? | **Yes, where consequence content is not already defined** |

Therefore H3-A is accepted **in the narrower architectural sense stated by the human designer**.

---

# 7. H4-A — Difficulty Grade as Skill-Side Penalty

## Proposed Decision

**H4-A — ACCEPT**

Environmental/systemic hazard difficulty may use the established difficulty-grade architecture as a **Skill-side penalty**.

The penalty modifies the Effective Skill used for the Core Test.

It does **not** modify:

- the natural d100 roll;
- Cost;
- Overflow;
- Failure XP;
- XP cascade;
- Recovery;
- Physical Energy formula;
- MP formula.

The difficulty mechanism therefore remains on the Skill side of the resolution rather than becoming a separate hazard modifier engine.

---

# 8. H5-B — Graded Intensity as Lookup Key

## Proposed Decision

**H5-B — ACCEPT**

Systemic hazard **Intensity** may be graded.

However:

> **Intensity is a lookup key only.**

Intensity does not independently:

- roll dice;
- consume resources;
- modify Overflow;
- generate XP;
- create an Effect;
- replace the Core Test;
- create a second resolution transaction.

Instead:

```text
Hazard Intensity
      ↓
Lookup key
      ↓
Predefined hazard parameters
      ↓
Existing Tiwas resolution mechanisms
```

This preserves the prohibition on creating a competing resolution economy.

---

# 9. Combined Proposed Architecture

The four accepted decisions form the following proposed architecture:

```text
SYSTEMIC / TERRAIN HAZARD
│
├── Hazard classification
│     └── descriptive Tags
│
├── Intensity
│     └── lookup key only
│
├── Difficulty Grade
│     └── Skill-side penalty
│
├── Resolution Cadence
│     └── progress toward surviving
│
└── Governing Core Test
      ├── natural d100 roll
      ├── normal Cost = natural roll
      ├── normal Overflow
      ├── normal Failure XP
      ├── normal XP cascade
      ├── normal recovery
      └── existing Effect / Location pathway where warranted
```

No element of this architecture creates a second Core resolution engine.

---

# 10. Decisions That Must Not Be Inferred

OpenCode must **not** infer that the following have been newly authorised:

| Item | Status |
|---|---|
| New hazard resource | **Not authorised** |
| New hazard dice mechanic | **Not authorised** |
| New terrain trigger mechanic | **Not authorised** |
| New terrain damage formula | **Not authorised** |
| Modification of Overflow | **Not authorised** |
| Modification of Failure XP | **Not authorised** |
| Modification of Cost = Roll | **Not authorised** |
| Modification of Zero-Step mathematics | **Not authorised** |
| Replacement of Core Test | **Not authorised** |
| Automatic Location Index generation merely because terrain exists | **Not authorised** |
| Automatic S-3 Effect merely because a terrain Tag exists | **Not authorised** |
| Promotion of this report to canonical status | **Not authorised** |

---

# 11. REQUIRED OPENCode CONFIRMATION PROCEDURE

## 11.1 Mandatory Human Confirmation

Before recording these decisions as confirmed project decisions, OpenCode must ask the human designer the following questions.

### Question 1 — H1-A

> **Do you confirm H1-A: a systemic hazard represents progress toward surviving the hazard rather than a sequence of unrelated isolated damage events, with no new resource economy introduced?**
>
> **Confirm: YES / NO / MODIFY**

### Question 2 — H2-A

> **Do you confirm H2-A: the systemic-hazard decision is scoped to the S-3 systemic-hazard Effect interface and does not make S-3 the owner of the entire environmental-hazard engine?**
>
> **Confirm: YES / NO / MODIFY**

### Question 3 — H3-A

> **Do you confirm H3-A: terrain hazards are instances of environmental hazards, obstacles, or physical risks already covered by the existing resolution architecture; no new terrain-hazard resolution rule is required; and `env:terrain_*` Tags are descriptive/flavour markers only with no independent mechanical trigger?**
>
> **Confirm: YES / NO / MODIFY**

### Question 4 — H4-A

> **Do you confirm H4-A: difficulty-grade modifiers for systemic/terrain hazards operate as Skill-side penalties to the Effective Skill, without modifying the natural roll, Cost, Overflow, Failure XP, XP cascade, or recovery?**
>
> **Confirm: YES / NO / MODIFY**

### Question 5 — H5-B

> **Do you confirm H5-B: graded hazard Intensity exists only as a lookup key and does not itself roll, spend resources, generate Effects, modify Overflow, or create a competing resolution mechanism?**
>
> **Confirm: YES / NO / MODIFY**

---

# 12. Confirmation Handling Rules for OpenCode

OpenCode must process the human response as follows.

| Human response | Required OpenCode action |
|---|---|
| **YES** | Record the corresponding decision as human-confirmed |
| **NO** | Do not record it as confirmed; preserve it as rejected/unresolved pending further instruction |
| **MODIFY** | Ask the human to provide the replacement wording or clarification before recording the decision |
| Partial response | Confirm only the explicitly answered questions; ask remaining questions separately |
| Ambiguous response | Escalate for clarification; do not infer approval |
| Silence/no response | Treat as **not confirmed** |

OpenCode must not interpret the existence of this report as equivalent to a human confirmation.

---

# 13. Authority and Promotion Controls

Until explicit human confirmation is received:

**Status of all five decisions: PENDING HUMAN CONFIRMATION.**

After confirmation, OpenCode may update the appropriate project documentation **only within the explicitly confirmed scope**.

Any subsequent promotion to canonical rules must follow the project's established authority and decision-record process.

This report itself does not confer canonical authority.

---

# 14. Consistency Constraints

Any implementation or documentation update resulting from these decisions must preserve the following Tiwas invariants:

1. Resolution remains d100 roll-under.
2. Success remains `roll ≤ current Skill`.
3. Fractional results continue to round down.
4. Natural roll remains the Cost.
5. Overflow remains direct HP damage when Cost exceeds remaining applicable resource.
6. Failure XP remains `roll − current Skill`.
7. Existing XP cascade rules remain unchanged.
8. No competing resource/progression economy is introduced.
9. Zero-Step mathematics remains unchanged.
10. Existing Location Index warrant rules remain distinct from Location Index provenance.
11. Existing S-3 Effect gating remains unchanged except where an explicitly authorised decision subsequently states otherwise.

---

# 15. Final Decision State

At the conclusion of this design discussion, the proposed state is:

| Fork | Proposed status | Confirmation required |
|---|---|---|
| **H1-A** | ACCEPT | **YES** |
| **H2-A** | ACCEPT | **YES** |
| **H3-A** | ACCEPT | **YES** |
| **H4-A** | ACCEPT | **YES** |
| **H5-B** | ACCEPT | **YES** |

### Overall status

> **PROPOSED — AWAITING EXPLICIT HUMAN DESIGNER CONFIRMATION**

OpenCode's immediate task is therefore **not implementation**.

Its immediate task is to ask the five confirmation questions in Section 11 and wait for the human designer's responses.

---

# 16. Provenance Note

This document reports the decisions and clarifications reached during the current Tiwas design conversation. Supporting project-corpus evidence establishes that environmental hazards are intended to use existing Core Test infrastructure and that the existing non-attack physical-resolution architecture provides the relevant Zero-Step pathway. 
The report deliberately distinguishes:

- established architecture;
- proposed designer decisions;
- unresolved content;
- human confirmation;
- eventual canonical promotion.

No inference from metadata, filenames, or this report alone may be used to bypass the project's authority model.

---

## OpenCode Documentarian Record (added 2026-09-03)

Stored from `C:\Users\Tiwa Pene\Downloads\Tiwas TTRPG — Reserved Systems Decision Confirmation Report.md` at Tiwa's instruction. Author remains GPT-5.6 Luna; OpenCode appended as additional `assessor_llm` and set as `last_modified_by_llm` for the storage pass. **This document is an advisory confirmation-handoff; it records no authority by itself.** All five forks (H1-A, H2-A, H3-A, H4-A, H5-B) remain **PENDING HUMAN CONFIRMATION** until Tiwa responds to the five Section-11 questions. OpenCode performed a live-register consistency cross-check (see assessment): the report's architectural claims are consistent with DEC-037 (register line 63), DEC-063 (line 89), DEC-076, DEC-080 (line 107), Invariant 17, and the §5.5 Snapshot hazard status (line 512). The one genuinely new semantic assignment in the report — `env:terrain_*` Tags as "descriptive/flavour markers only, with no independent mechanical trigger" (H3-A §6.2) — is not stated anywhere in the existing corpus and requires explicit Tiwa confirmation before the DEC-080 `env:terrain_*` tags can be treated as descriptive-only.
