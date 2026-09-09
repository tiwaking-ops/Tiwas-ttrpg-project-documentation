---
document:
  title: "Tiwas DEC-088 Formal Proposal — Graded Temperature and Scene-State Tracking"
  version: "1.0"
  status: "Non-Canonical Design Proposal"
  authority: "Proposal only; does not modify Canonical Rules"
  decision_id: "DEC-088"
  author:
    name: "GPT-5.6 Luna"
    version: "GPT-5.6 Luna"
  date: "2026-09-08"
  target_consumer: "OpenCode"
  supersedes: null
  related_decisions:
    - "DEC-080"
    - "DEC-088"
    - "DEC-089"
    - "DEC-090"
    - "DEC-092"
    - "DEC-093"
    - "DEC-114"
    - "DEC-115"
    - "DEC-116"
    - "DEC-117"
  canonical_sources:
    - "canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md"
  primary_working_sources:
    - "decision-register.md"
    - "tiwas-proposals-wip-and-design-direction-v1.4.3.md"
    - "Tiwas-Alpha-Playtest-Corpus-2026-09-08.md"
---

# 1. Executive Summary

## 1.1 Purpose

This document formally proposes resolution of the two items deliberately left open by DEC-088:

1. **Graded temperature:** whether environmental temperature should remain a binary `env:freezing` state or support graded temperature states such as cold, freezing and extreme/arctic conditions.
2. **Scene-state tracking:** how persistent environmental state should be represented without creating a separate temperature engine or competing Hazards/environment resolution engine.

## 1.2 Proposed Decision

The proposal is:

> **Adopt a single ordered environmental Temperature Grade as scene state, while retaining `env:freezing` as a derived Boolean compatibility predicate. Store environmental state using the unified StateRecord architecture rather than creating a dedicated temperature tracker.**

The proposed temperature grades are:

| Grade | Proposed name | Mechanical purpose |
|---:|---|---|
| 0 | Normal | No cold state |
| 1 | Cold | Cold conditions are mechanically relevant |
| 2 | Freezing | Freezing conditions; activates `env:freezing` |
| 3 | Extreme Cold | Extreme cold; also activates `env:freezing` |

The proposal deliberately **does not establish physical temperature thresholds** in degrees Celsius.

`Arctic` should not be adopted as a formal temperature-grade name because it describes a geographic/climatic environment rather than an intrinsic temperature measurement. It may remain a setting/content descriptor.

## 1.3 Scene-State Proposal

Environmental state should be represented through the unified StateRecord architecture established by DEC-115–117.

No dedicated:

- `TemperatureTracker`;
- `EnvironmentTracker`;
- `HazardTracker`; or
- parallel environmental resolution engine

should be introduced.

Environmental state describes the current scene.

Hazard rules determine whether that state creates a mechanical resolution.

---

# 2. Authority and Status

## 2.1 Current DEC-088 Status

DEC-088 is currently a **Non-canonical designer ruling**.

It already established:

- `env:freezing`;
- Boolean presence/absence;
- GM declaration per scene;
- Conditional-Trait Binding;
- read-only/stateless condition evaluation.

The same DEC explicitly carried two matters forward as unresolved:

- graded temperature;
- the scene-state tracking mechanism / full Hazards-environment subsystem.

The decision register records this boundary explicitly. `env:freezing` is currently a seventh Environment-namespace Tag, and its semantics are Boolean rather than graded. 

This document therefore proposes an **extension of DEC-088**, not a replacement of its existing ruling.

## 2.2 Canonical Boundary

Nothing in this proposal is Canonical.

Implementation or promotion must not modify the Canonical Rules merely because this proposal is accepted as a design direction.

If adopted by the human designer, the resulting decision remains non-canonical until the project's required promotion procedure is completed.

---

# 3. Existing Architecture That Constrains This Proposal

## 3.1 DEC-088 Existing `env:freezing`

Current semantics:

```text
env:freezing
    = current scene/zone is at freezing temperature or colder
```

Properties:

| Property | Existing ruling |
|---|---|
| Namespace | `env:` |
| Type | Scene-state Tag |
| Value | Boolean presence/absence |
| Authority | GM-declared |
| Scope | Current scene/zone |
| Numeric temperature | None |
| Automatic roll | None |
| Resource expenditure | None |
| New resource pool | None |

DEC-088 also permits a creature Trait or Tag-granted Effect to contain:

```text
Active only while [env:X] is present
```

The condition is read-only and is evaluated when the relevant mechanic would apply. 

## 3.2 DEC-089 — Systemic Hazard Cadence

Systemic hazards are already ruled to represent an ongoing process of progress toward surviving the hazard rather than unrelated isolated damage events.

They use the existing Core Test and resource machinery.

No new:

- resource pool;
- parallel resolution engine;
- XP economy; or
- replacement for the Core Test

is permitted.

## 3.3 DEC-090 — S-3 Boundary

The systemic-hazard decision is scoped to the S-3 systemic-hazard Effect interface.

S-3 does not own the entire environmental simulation.

Core Test, difficulty, location, resource cost, Overflow, Failure XP and Recovery remain separate concerns.

## 3.4 DEC-092 — Hazard Difficulty

Environmental/systemic hazard difficulty uses the existing difficulty-grade architecture as a Skill-side penalty.

It does not modify:

- the natural roll;
- Cost;
- Overflow;
- Failure XP;
- XP cascade;
- Recovery;
- Physical Energy;
- MP.

No separate hazard-modifier engine is permitted.

## 3.5 DEC-093 — Hazard Intensity

Hazard Intensity may be graded, but Intensity is explicitly a **lookup key only**.

The established architecture is:

```text
Hazard Intensity
    ↓
Predefined parameter lookup
    ↓
Existing Tiwas resolution mechanism
```

Intensity itself does not roll, consume resources, modify Overflow, generate XP, create Effects, or replace the Core Test.

---

# 4. Problem Definition

The current DEC-088 architecture is sufficient for the Ice Troll use case because the creature only needs a Boolean predicate:

```text
env:freezing = present / absent
```

However, the architecture does not currently distinguish:

```text
cold
freezing
extreme cold
```

Consequently, future environmental content requiring different cold severities would either need:

1. multiple independent Boolean Tags;
2. arbitrary numeric temperature;
3. a new temperature subsystem; or
4. an extension of scene-state semantics.

Options 1–3 introduce avoidable architectural problems.

The proposal therefore extends the existing scene-state architecture rather than introducing another subsystem.

---

# 5. Graded Temperature Proposal

## 5.1 Proposed Model

Temperature should be represented by **one ordered Grade**, not by multiple simultaneous Boolean temperature Tags.

Proposed state:

```text
Temperature Grade ∈ {Normal, Cold, Freezing, Extreme Cold}
```

Formally:

```text
TemperatureGrade ∈ {0, 1, 2, 3}
```

where:

| Value | Name |
|---:|---|
| 0 | Normal |
| 1 | Cold |
| 2 | Freezing |
| 3 | Extreme Cold |

The integer representation is an implementation representation of an ordered grade. It is not intended to become a general-purpose numeric temperature mechanic.

## 5.2 Ordering

The grades have an explicit ordinal relationship:

```text
Normal < Cold < Freezing < Extreme Cold
```

This permits future content to state thresholds such as:

```text
requires Freezing or colder
requires Extreme Cold
```

without creating independent Boolean states.

## 5.3 `env:freezing` Compatibility Predicate

The existing `env:freezing` Tag should be retained.

Its proposed relationship to Temperature Grade is:

| Temperature Grade | `env:freezing` |
|---|---|
| Normal | Absent |
| Cold | Absent |
| Freezing | Present |
| Extreme Cold | Present |

Formally:

```text
env:freezing = present
    iff
TemperatureGrade >= Freezing
```

This preserves all existing DEC-088 content.

Existing content therefore requires no knowledge of the graded system.

For example:

```text
Trait:
    Regeneration

Condition Clause:
    Active only while [env:freezing] is present
```

continues to function unchanged.

---

# 6. Why Multiple Temperature Tags Are Rejected

The following model is not recommended:

```text
env:cold
env:freezing
env:arctic
```

as three independent Boolean states.

## 6.1 State-Consistency Problem

Independent Tags create potentially invalid combinations:

| `cold` | `freezing` | `arctic` | Problem |
|---|---|---|---|
| Absent | Present | Absent | Valid |
| Present | Present | Absent | Is this cumulative or hierarchical? |
| Present | Absent | Present | What does this mean? |
| Present | Present | Present | Are all three active? |
| Absent | Absent | Present | Is Arctic automatically freezing? |

The rules would then require additional precedence and exclusivity rules merely to describe temperature.

That is unnecessary.

## 6.2 Architecture Conflict

The project has repeatedly favoured Tags as declarative state/predicate information rather than independent numeric or resolution engines.

The later unified StateRecord architecture also treats Tags, Effects and Conditions as a common record shape while preserving their distinct fiction-level classifications. DEC-116 explicitly establishes vocabulary-only defaults for Tags unless a ruling supplies numeric fields, while DEC-117 establishes the unified StateRecord model. 

A single Temperature Grade is therefore preferable to a collection of mutually dependent Tags.

---

# 7. Why Numeric Degrees Celsius Are Not Proposed

The proposal rejects a continuous/numeric physical-temperature model.

For example, the following is outside scope:

```text
Temperature = -37°C
```

as an input directly consumed by mechanics.

## 7.1 Reasons

A physical temperature value would create questions that the current subsystem does not need to answer:

- How does −17°C differ mechanically from −18°C?
- Are effects continuous or thresholded?
- How are changing temperatures tracked?
- How frequently does temperature update?
- Does character exposure time become a separate variable?
- Does equipment modify actual temperature?
- Does body temperature become tracked?
- Does wind chill become a second temperature?
- Does shelter modify temperature or exposure?
- Does temperature itself initiate tests?

These are environmental-simulation questions, not required to resolve the current DEC-088 problem.

The Tiwas architecture already provides a more appropriate abstraction:

```text
environmental state
    ↓
grade
    ↓
predefined hazard/content parameters
    ↓
existing resolution machinery
```

This matches DEC-093's explicit Intensity-as-lookup-key architecture.

---

# 8. `Arctic` Terminology

## 8.1 Proposed Ruling

`Arctic` should **not** be adopted as the formal name of Temperature Grade 3.

Recommended formal term:

> **Extreme Cold**

## 8.2 Rationale

"Arctic" describes a geographic/climatic context.

It does not logically mean:

```text
Arctic = a specific temperature
```

An Arctic scene may contain different temperatures and conditions.

The rules should therefore distinguish:

| Concept | Example |
|---|---|
| Geographic/environmental descriptor | Arctic |
| Mechanical temperature grade | Extreme Cold |

A setting can therefore declare:

```text
Environment:
    Arctic tundra

Temperature:
    Extreme Cold
```

without conflating geography and temperature.

---

# 9. Scene-State Tracking Proposal

## 9.1 Required Architecture

Environmental state should be stored in the existing **unified StateRecord architecture**.

DEC-115–117 already establish a common StateRecord model for Tags, Effects and Conditions and extend that architecture across characters, items, environments and scenes. 

Therefore:

> **Temperature should be another environmental state represented through the existing state architecture, not a separate tracker.**

## 9.2 Proposed Conceptual Representation

Conceptually:

```text
Scene
└── Environmental State
    ├── Temperature Grade = Extreme Cold
    ├── env:freezing = Present
    ├── env:hazard_systemic = Present
    └── other environment state
```

The exact implementation representation should be determined during implementation design and must not introduce mechanics beyond the ruling.

## 9.3 State Ownership

Temperature belongs to the **scene/environment state**, not to individual characters.

A character is affected because a rule consults the current environmental state.

This maintains the existing DEC-088 model:

```text
Scene State
    ↓
Condition Clause
    ↓
Trait / Effect applicability
```

rather than copying the temperature value onto every character.

---

# 10. State Lifetime

The proposed Temperature Grade is a **persistent scene state**.

It remains active until the environmental state changes.

Example:

```text
Scene starts:
    Temperature = Cold

Weather changes:
    Temperature = Freezing

Shelter established:
    Temperature = Cold
```

The transition changes scene state.

It does not itself:

- roll;
- deal damage;
- spend resources;
- generate XP;
- create Conditions;
- trigger a Core Test.

Those consequences remain owned by the appropriate downstream rule.

---

# 11. Environmental State Versus Hazard

The proposal requires a strict separation between **state** and **hazard**.

## 11.1 Environmental State

Answers:

> What is the current environment?

Example:

```text
Temperature = Extreme Cold
```

## 11.2 Environmental Tag

Answers:

> Does a particular environmental predicate hold?

Example:

```text
env:freezing = Present
```

## 11.3 Hazard

Answers:

> Does this environmental state constitute an active mechanical hazard for this actor?

Example:

```text
Extreme Temperature Hazard
```

## 11.4 Resolution

Answers:

> What happens mechanically?

Existing Core Test / S-3 / difficulty / Effects / Conditions machinery determines this.

The resulting architecture is:

```text
┌──────────────────────────┐
│       SCENE STATE        │
│                          │
│ Temperature = Extreme    │
│ Cold                     │
└────────────┬─────────────┘
             │
             ├──────────────► env:freezing
             │
             │
             ▼
┌──────────────────────────┐
│     HAZARD CONTENT       │
│                          │
│ Extreme Temperature      │
│ Intensity = Extreme Cold │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ EXISTING TIWAS MECHANICS │
│                          │
│ Difficulty → Core Test   │
│ → Cost → XP → Recovery   │
│ → Effects / Conditions   │
└──────────────────────────┘
```

---

# 12. No Automatic Environmental Resolution

This proposal explicitly prohibits the following interpretation:

> "The scene is Extreme Cold, therefore every character automatically makes a test."

Temperature state alone does not initiate a transaction.

This is necessary to preserve:

- DEC-088 read-only scene-state semantics;
- DEC-089 systemic hazard architecture;
- DEC-092 difficulty architecture;
- DEC-093 lookup-key-only intensity;
- Invariant 17;
- the Core Test's ownership of resolution.

DEC-114 similarly establishes that environmental hazard Tags are consulted by adjudication and do not independently initiate rolls, damage, resource expenditure or a new engine. 

---

# 13. Temperature Grade as Hazard Intensity

The Temperature Grade may also serve as the **content lookup key** for a systemic temperature hazard.

Example:

```text
Temperature Grade
       ↓
Extreme Cold
       ↓
Extreme Temperature Hazard parameters
       ↓
Existing Difficulty / Core Test / Effect rules
```

This is explicitly compatible with DEC-093.

The grade itself does not perform the resolution.

It merely identifies which predefined hazard parameters apply.

---

# 14. Interaction With Existing `env:freezing`

The proposed architecture produces two related but distinct representations.

| Representation | Purpose |
|---|---|
| Temperature Grade | Provides ordered environmental severity |
| `env:freezing` | Provides existing Boolean compatibility predicate |

This is intentional.

### Example

```text
Temperature = Extreme Cold
```

implies:

```text
env:freezing = present
```

Therefore:

```text
Ice Troll:
    Regeneration
        condition:
            Active only while [env:freezing] is present
```

remains valid.

No replacement of the existing DEC-088 grammar is required.

---

# 15. Interaction With Unified StateRecord

DEC-117 establishes that Tags, Effects and Conditions use a unified StateRecord shape, including fields such as:

```text
Type
Tier Y
Magnitude Z
Location X
id
source
duration
removal_tags
counters
```

with the appropriate defaults and restrictions. 

This proposal does **not** introduce another record schema.

The environmental temperature representation should use the existing state architecture.

Any implementation-specific field required to represent the ordered Temperature Grade must therefore be treated as a schema implementation question and separately reviewed against DEC-115–117 before being locked.

The proposal does not authorise creation of a general-purpose numeric Tag system.

---

# 16. Compatibility With DEC-080

DEC-080 established an open, extensible, namespace-based Tag ontology.

`env:freezing` was explicitly added as an Environment namespace extension under DEC-088. 

The proposal therefore preserves:

```text
env:
```

as the environment namespace.

No new namespace is required.

No replacement of the Tag ontology is required.

---

# 17. Compatibility With DEC-114

DEC-114 already distinguishes:

```text
env:hazard_physical
env:hazard_systemic
```

and establishes that environmental Tag presence is GM-declared per scene and does not itself initiate resolution. 

The temperature proposal therefore does not change hazard routing.

Specifically:

```text
Temperature Grade
```

does **not** determine whether a hazard is physical or systemic.

That remains the responsibility of the relevant hazard classification.

For example:

```text
Extreme Temperature
    → systemic hazard
```

remains a content/routing determination under the existing architecture.

---

# 18. Proposed Formal Rules

If the designer adopts this proposal, the following rule text is recommended for the DEC-088 extension.

## 18.1 Temperature Grade

> **Environmental Temperature may be represented as an ordered scene-state Grade: Normal, Cold, Freezing, or Extreme Cold. The Grade represents environmental severity and is not a continuous physical-temperature measurement. Exact physical temperature thresholds are content-authoring and are not established by this rule.**

## 18.2 `env:freezing`

> **The existing `env:freezing` scene-state Tag remains valid. It is present whenever the current Temperature Grade is Freezing or Extreme Cold, and absent otherwise. Existing Conditional-Trait Binding rules continue to reference `env:freezing` without modification.**

## 18.3 Scene State

> **Environmental Temperature is scene/environment state and is represented through the unified StateRecord architecture. No dedicated temperature-tracking subsystem is created.**

## 18.4 State Changes

> **Temperature Grade persists as scene state until the GM changes the environmental state. A change in Temperature Grade does not itself initiate a Core Test, consume resources, generate XP, inflict HP damage, create a Condition, or create an Effect.**

## 18.5 Hazard Resolution

> **Where Temperature Grade is used as the Intensity of an environmental/systemic hazard, the Grade functions only as a lookup key into predefined hazard parameters. Resolution proceeds through existing Tiwas mechanics.**

## 18.6 No New Resolution Engine

> **Temperature Grade and environmental scene state do not create a separate resolution engine, resource pool, XP economy, damage mechanism, or automatic test cadence.**

---

# 19. Explicitly Deferred Matters

This proposal should **not** be interpreted as resolving the following.

| Matter | Status |
|---|---|
| Exact Celsius thresholds | Open |
| Exposure duration | Open |
| Wind chill | Open |
| Shelter/insulation mechanics | Open |
| Clothing/equipment protection | Open |
| Character acclimatisation | Open |
| Cold-resistance content | Open |
| Exact Extreme Temperature hazard parameters | Open |
| Systemic hazard cadence details beyond DEC-089 | Existing ruling applies; content remains to be built |
| Exact environmental-state implementation schema | Implementation work |
| Full Hazards subsystem | Unbuilt |
| Full Environment subsystem | Unbuilt |
| Whether all environmental states require persistent StateRecords | Not decided by this proposal |
| Scene-wide versus zone-local environmental boundaries | Open implementation/content question |
| Temperature transition rules | Open content question |

This proposal resolves the **architecture**, not every future environmental mechanic.

---

# 20. Rejected Alternatives

## 20.1 Alternative A — Remain Binary Forever

```text
env:freezing = present / absent
```

### Rejected

This is sufficient for current Ice Troll content but provides no clean representation for future severity-dependent temperature hazards.

## 20.2 Alternative B — Independent Temperature Tags

```text
env:cold
env:freezing
env:arctic
```

### Rejected

Creates state-combination and precedence problems.

## 20.3 Alternative C — Continuous Numeric Temperature

```text
Temperature = -27°C
```

### Rejected

Introduces unnecessary physical simulation and threshold questions.

## 20.4 Alternative D — Dedicated Temperature Tracker

```text
TemperatureTracker
```

### Rejected

Duplicates the existing unified StateRecord / scene-state architecture and creates unnecessary subsystem boundaries.

## 20.5 Alternative E — Automatic Temperature Tests

```text
Temperature = Extreme Cold
        ↓
automatic Core Test
```

### Rejected

Violates the separation between environmental state and resolution and risks creating implicit resolution cadence.

---

# 21. Architectural Invariants Preserved

The proposal preserves the following existing constraints.

| Constraint | Result |
|---|---|
| Core Test remains universal resolution mechanism | Preserved |
| Natural roll remains authoritative | Preserved |
| Cost = natural roll | Preserved |
| Overflow → HP | Preserved |
| Overflow immutability | Preserved |
| Failure XP | Preserved |
| Recovery | Preserved |
| No new resource pool | Preserved |
| No parallel XP economy | Preserved |
| Hazard difficulty uses existing difficulty architecture | Preserved |
| Hazard Intensity is lookup-only | Preserved |
| Tags do not initiate resolution | Preserved |
| `env:freezing` compatibility | Preserved |
| Unified StateRecord architecture | Extended, not replaced |
| DEC-025 Skill-side Tag prohibition | Preserved |

The proposal therefore introduces **state representation**, not a competing mechanical engine.

---

# 22. Implementation Guidance for OpenCode

OpenCode should treat this document as a proposal and **must not silently modify Canonical Rules**.

If the proposal is subsequently approved by the designer, implementation should proceed in the following order:

1. Record the designer ruling against DEC-088.
2. Preserve the existing `env:freezing` definition.
3. Add the ordered Temperature Grade concept to the non-canonical design documentation.
4. Establish the relationship:
   ```text
   Freezing ≤ Extreme Cold → env:freezing
   ```
5. Map environmental temperature state to the existing Scene/Environment StateRecord architecture.
6. Do not create a dedicated temperature tracker.
7. Do not create automatic temperature resolution.
8. Do not define Celsius thresholds unless separately authorised.
9. Do not define hazard damage/effects merely as a consequence of adopting the Grade.
10. Update hazard-content documentation only through separately authorised subsystem work.
11. Preserve the distinction between Temperature Grade and Hazard Intensity.
12. Run the project's required promotion process before modifying Canonical Rules.

---

# 23. Proposed Decision Record

## DEC-088 Extension

| Field | Proposed value |
|---|---|
| Decision | Graded environmental temperature and scene-state architecture |
| Temperature model | Ordered Grade |
| Grades | Normal / Cold / Freezing / Extreme Cold |
| `env:freezing` | Retained |
| `env:freezing` threshold | Freezing and colder |
| Physical temperature values | Not mechanically represented |
| `Arctic` | Content descriptor, not formal grade |
| Scene state | Unified StateRecord architecture |
| Dedicated tracker | Rejected |
| Automatic resolution | Prohibited |
| Hazard Intensity use | Lookup key only |
| Hazard engine | Not created |
| Canonical status | Not Canonical |
| Required next authority | Human designer ruling |

---

# 24. Final Recommendation

**RECOMMENDATION: ADOPT THE PROPOSAL.**

The strongest architecture is:

```text
                  SCENE
                    │
                    ▼
          Temperature Grade
       ┌────────┬──────────┬───────────┐
       │        │          │           │
    Normal    Cold     Freezing   Extreme Cold
                            │           │
                            └─────┬─────┘
                                  ▼
                           env:freezing
                                  │
                                  ▼
                    Conditional-Trait Binding
                                  │
                                  ▼
                         Existing mechanics
```

and, where a temperature hazard exists:

```text
Temperature Grade
       ↓
Hazard Intensity lookup
       ↓
Predefined hazard parameters
       ↓
Existing Difficulty / Core Test
       ↓
Existing Effects / Conditions
```

This closes the architectural gap without creating a second environmental engine.

The central design principle is:

> **Scene state describes the environment; Tags expose predicates; hazard parameters interpret environmental severity; the existing Tiwas resolution engine performs the mechanical resolution.**

That separation is the key reason this proposal is preferable to either a collection of Boolean temperature Tags or a dedicated environmental simulation subsystem.

---

# 25. Governance Note

This document is a **formal design proposal only**.

It does not:

- promote DEC-088 to Canonical;
- modify the Canonical Rules;
- close unrelated Hazard questions;
- define the full Environment subsystem;
- define physical temperature thresholds;
- define exposure damage;
- define new resources;
- define a new resolution method.

Any designer approval should be recorded as a distinct ruling and then processed through the project's established promotion workflow before Canonical modification.

---

# 26. Source Basis

The proposal was evaluated against the current project corpus, including:

- `decision-register.md`;
- `tiwas-proposals-wip-and-design-direction-v1.4.3.md`;
- `Tiwas-Alpha-Playtest-Corpus-2026-09-08.md`;
- Canonical Rules v1.4 / `tiwas-canonical-rules-and-changelog-v1.3.md`.

Relevant existing rulings include DEC-080, DEC-088–093, DEC-114–117. The current register explicitly records DEC-088's graded-temperature and scene-tracking questions as carried open, while later decisions establish the unified StateRecord and hazard architecture used by this proposal. 