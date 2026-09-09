# Tiwas TTRPG — Proposed Hierarchical Location Architecture

## 1. Document Control

| Field | Value |
|---|---|
| Project | Tiwas TTRPG |
| Document Type | Formal Design / Architecture Report |
| Subject | Location System Architecture |
| Status | **PROPOSAL — NOT CANONICAL** |
| Scope | Location resolution from Tier 1 through Tier 12 |
| Primary Issue | Replacement candidate for the current flat Tier-1–5 location architecture |
| Supersession Status | No existing DEC is superseded by this document |
| Author | **GPT-5.6 Luna** |
| Date | 2026-09-08 |
| Intended Consumer | OpenCode / Tiwas Documentation Repository |
| Decision Required | Human designer review and subsequent DEC if accepted |

---

# 2. Executive Summary

This report records the complete location-system architecture developed during the current design discussion.

The principal conclusion is that Tiwas should move away from a **flat location-menu model with a separate secondary subdivision roll** and instead investigate a **hierarchical Location Address model**.

The proposed architecture has the following characteristics:

1. A location is represented as a hierarchical address within a target-specific **Location Template**.
2. A single Location Index determines the underlying location path.
3. Location resolution may extend from **Tier 1 through Tier 12**.
4. Skill-Tier determines the maximum Location Tier that the acting Skill can resolve.
5. A target does not need to possess all twelve levels.
6. Terminal anatomy may occur before Tier 12.
7. Human anatomy is one Location Template; other creatures, constructs, machines, and other targets may have different templates.
8. The architecture does not require a secondary random location roll.
9. The natural Core Test roll remains authoritative for all existing Core Test consequences.
10. Higher Location Tiers represent **greater spatial precision**, not additional Core Tests.
11. Location hierarchy permits exact parent/child matching for Effects, Armor, Wounds, equipment, and future subsystems.
12. Tier 6–12 are therefore architecturally possible while remaining rare because high resolution requires correspondingly high Skill-Tier capability.

This is a **design proposal only**. It does not modify canonical rules.

---

# 3. Existing System State

## 3.1 Current Tier-1 Location System

DEC-100 currently establishes the following Tier-1 quartile mapping:

| Natural / derived Location Index | Current Tier-1 location |
|---:|---|
| 01–25 | Legs |
| 26–50 | Torso |
| 51–75 | Arms |
| 76–100 | Head |

This is currently ruled and accepted.

The proposed architecture does **not** assume that these numerical ranges must remain unchanged.

If the hierarchical architecture is accepted, the numerical allocation should be investigated separately rather than silently inherited.

---

## 3.2 Current Tier-2+ Architecture

DEC-042 currently specifies:

- Tier-2+ subdivision uses a dedicated secondary roll.
- The secondary roll is separate from the original Zero-Step-derived number.
- The secondary roll has no Energy/MP cost.
- It is explicitly not a second Core Test.
- It does not generate independent Failure XP.
- It does not independently qualify for Double handling.
- d6/d10 resolution is used according to menu size.
- Location mismatch falls back through DEC-030.

This mechanism is therefore a major architectural dependency of the current location system.

The proposal in this document would replace that mechanism.

---

## 3.3 Current DEC-112 Architecture

DEC-112 currently defines:

| Skill-Tier | Current Location Level |
|---:|---:|
| 1 | Tier-1 coarse zone |
| 2 | Level 2 |
| 3 | Level 3 |
| 4 | Level 4 |
| 5+ | Level 5 |

Current Level-2 through Level-4 menus are cumulative.

Examples include:

- Head: Skull, Face, Eyes, Ears, Nose, Mouth, Jaw, Teeth
- Torso: Chest, Abdomen, Pelvis, Groin, Heart, Lungs, Liver, Stomach, Intestines
- Arms: Upper Arm, Lower Arm, Hand, Thumb, Index, Middle, Ring, Little
- Legs: Upper Leg, Lower Leg, Foot, Hallux, Second, Third, Fourth, Fifth
- Level 5 digits: Proximal, Intermediate, Distal phalanges, with Thumb having Proximal and Distal only.

DEC-112 explicitly establishes that no granularity above Level 5 is currently reachable.

---

## 3.4 Current DEC-113 Effect-Tier Interaction

DEC-113 currently distinguishes Location Tier from Effect Tier.

The current ruling establishes:

- Armor Bypass as the only Tier-2-eligible Effect.
- Wound, Trip, Disarm/Break Hold, and Equipment Damage as Tier-1 location Effects.
- PC-side downgrade from Armor Bypass Tier 2 to Tier 1 is permitted.
- Creature/NPC downgrade is not permitted.

This distinction should remain conceptually separate in any future architecture.

**Location Tier must not be conflated with Effect/Wound Tier.**

DEC-107 separately establishes Effect Tier and Wound Tier from the acting Skill-Tier. The proposed architecture therefore treats spatial resolution and Effect severity as independent dimensions.

---

# 4. Problem Statement

The current location architecture has reached a structural limitation.

## 4.1 Flat Menu Limitation

A flat menu treats increasingly precise anatomical locations as members of progressively larger lists.

This produces several problems:

1. Anatomical parent/child relationships are not represented directly.
2. Level 4 and Level 5 content must be manually maintained as cumulative menus.
3. Higher Skill-Tiers above 5 have no corresponding increase in spatial precision.
4. Different anatomical structures cannot naturally have different maximum depths.
5. Internal anatomy and complex creature anatomy become increasingly difficult to represent.
6. Armor coverage and location matching must rely on discrete menu membership rather than structural ancestry.
7. Extending the system beyond Level 5 requires another ad hoc menu layer.
8. The secondary roll becomes increasingly responsible for resolving anatomical specificity.

---

# 5. Proposed Core Principle

## 5.1 Location as an Anatomical Address

A location should be treated as an **address within a target's spatial topology**, rather than as an independently rolled menu result.

Conceptually:

```text
Target
└── Location Space
    └── Region
        └── Subregion
            └── Component
                └── Structure
                    └── Segment
                        └── Subsegment
                            └── Fine Structure
                                └── Microstructure
                                    └── Internal Structure
                                        └── Sub-internal Structure
                                            └── Terminal Structure
                                                └── Terminal Substructure
```

The address is therefore a path through a tree.

---

# 6. Location Resolution Model

## 6.1 Variables

| Variable | Definition |
|---|---|
| \(N\) | Natural d100 result of the Core Test |
| \(I\) | Location Index derived from the location-generation procedure |
| \(S\) | Skill-Tier of the acting Skill |
| \(L\) | Maximum Location Tier available from that Skill |
| \(D\) | Maximum authored depth of the relevant target location path |
| \(A\) | Resulting Location Address |

The proposal retains the distinction between the natural Core Test result and post-process location interpretation.

---

## 6.2 Maximum Location Resolution

Proposed relationship:

\[
L_{\max}=S
\]

subject to the architectural ceiling:

\[
L_{\max}\leq12
\]

Therefore:

| Skill-Tier | Maximum Location Tier |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |
| 11 | 11 |
| 12+ | 12 |

This does **not** create new Skills or alter the existing Skill system.

It only establishes a proposed mapping between existing Skill-Tier and spatial resolution.

---

## 6.3 Target-Depth Constraint

A target may contain fewer than twelve meaningful anatomical levels.

Therefore:

\[
L_{\text{actual}}=\min(S,D)
\]

where:

- \(S\) = available Skill-Tier
- \(D\) = authored depth of the relevant Location Template

A Skill-Tier 12 action against a structure whose Location Template terminates at Tier 7 therefore resolves at Tier 7.

It does not invent additional anatomy.

---

# 7. Proposed Tier-1 Through Tier-12 Semantics

The following is the proposed generic semantic ladder.

| Location Tier | Proposed semantic meaning |
|---:|---|
| **1** | Major anatomical region |
| **2** | Major subdivision of a region |
| **3** | Named body component |
| **4** | Named anatomical structure |
| **5** | Major segment of that structure |
| **6** | Subsegment |
| **7** | Fine anatomical structure |
| **8** | Mechanically relevant microstructure |
| **9** | Named internal structure |
| **10** | Substructure of a named internal structure |
| **11** | Terminal anatomical structure |
| **12** | Terminal substructure |

These definitions are **architectural categories**, not a claim that every creature must contain a node at every level.

---

# 8. Tier 6–12 Architecture

## 8.1 Tier 6 — Subsegment

Tier 6 represents subdivision of an existing Tier-5 segment.

Example:

```text
Right Arm
└── Forearm
    └── Hand
        └── Index Finger
            └── Proximal Phalanx
                └── Proximal Segment
```

Tier 6 does not universally mean a particular anatomical object.

It means that the Location Template has divided the Tier-5 object into a further mechanically meaningful subdivision.

---

## 8.2 Tier 7 — Fine Structure

Tier 7 identifies a smaller mechanically relevant structure within a Tier-6 location.

Possible examples include:

- a fine structural region of a bone;
- a distinct joint component;
- a discrete portion of a tendon;
- a mechanically relevant section of another structure.

The exact content is determined by the Location Template.

---

## 8.3 Tier 8 — Microstructure

Tier 8 permits mechanically relevant structures smaller than ordinary named anatomical structures.

Possible examples include:

- tendon structures;
- joint structures;
- vessel structures;
- other mechanically relevant microstructures.

The term "microstructure" is therefore a resolution category, not a universal anatomical list.

---

## 8.4 Tier 9 — Named Internal Structure

Tier 9 permits explicit identification of a named internal structure.

Examples could include:

- a particular tendon;
- a particular vessel;
- a particular nerve;
- another named internal structure.

The Location Template determines which structures exist.

---

## 8.5 Tier 10 — Internal Substructure

Tier 10 divides a Tier-9 internal structure into mechanically meaningful subdivisions.

Example:

```text
Torso
└── Abdomen
    └── Internal
        └── Liver
            └── Right Lobe
                └── Superior Region
```

The exact anatomy must be established through future content-authoring work.

---

## 8.6 Tier 11 — Terminal Structure

Tier 11 identifies a terminal structure that has mechanical significance but does not require another generic subdivision.

A Tier-11 node may therefore be the final meaningful target within one branch of the Location Template.

---

## 8.7 Tier 12 — Terminal Substructure

Tier 12 is the proposed maximum architectural resolution.

It represents the smallest authored spatial unit that Tiwas considers mechanically addressable under the Location Template.

Tier 12 is therefore not "microscopic anatomy" by definition.

It means:

> **the twelfth and final permitted address depth.**

---

# 9. Critical Mathematical Constraint

The architecture must preserve the information limits of the d100.

A single d100 produces:

\[
|\Omega|=100
\]

possible natural results.

Therefore a single Location Index cannot independently encode more than 100 distinct equiprobable location states.

This creates an important distinction:

### Location Depth ≠ Number of Possible Locations

A single Location Index can select one of 100 address paths.

Each address path can contain multiple hierarchical levels.

For example:

```text
Location Index 42

Tier 1  Torso
Tier 2  Abdomen
Tier 3  Internal
Tier 4  Liver
Tier 5  Right Lobe
Tier 6  Superior Region
Tier 7  Segment
Tier 8  Vascular Structure
Tier 9  Named Vessel
Tier 10 Terminal Branch
```

The system has therefore generated **one path**, not ten independent random outcomes.

This is a fundamental architectural constraint and must be preserved during implementation.

---

# 10. Deterministic Address Path

The proposed resolution pipeline is:

```text
CORE TEST
    │
    ▼
Natural d100
    │
    ├── Cost
    ├── Success/Failure
    ├── Failure XP
    └── Double eligibility
    │
    ▼
Location Index
    │
    ▼
Location Template
    │
    ▼
Location Address Path
    │
    ├── Tier 1
    ├── Tier 2
    ├── Tier 3
    ├── Tier 4
    ├── Tier 5
    ├── Tier 6
    ├── Tier 7
    ├── Tier 8
    ├── Tier 9
    ├── Tier 10
    ├── Tier 11
    └── Tier 12
```

No additional Core Test is introduced.

---

# 11. Repeated Use of the Same Location Index

The same Location Index must resolve consistently through the hierarchy.

For example:

```text
Location Index = 42
```

A Skill-Tier 3 resolution might expose:

```text
Torso → Abdomen → Internal
```

A Skill-Tier 6 resolution using the same Location Index might expose:

```text
Torso
→ Abdomen
→ Internal
→ Liver
→ Right Lobe
→ Superior Region
```

The underlying Location Index has not changed.

This preserves the existing invariant that the natural Core Test remains authoritative.

---

# 12. Location Templates

## 12.1 Definition

A **Location Template** is a structured target-specific hierarchy defining the spatial topology through which a Location Index can resolve.

The engine should not hard-code human anatomy.

Instead:

```text
Location Template
    ↓
Target-specific location topology
```

Possible template categories include:

- Human
- Humanoid
- Animal
- Dragon
- Construct
- Machine
- Other future target types

The exact templates are content-authoring decisions.

---

# 13. Human Location Template — Illustrative Structure

The following is an architectural example only.

It is **not canonical anatomy content**.

```text
Human
│
├── Head
│   ├── Skull
│   ├── Face
│   │   ├── Eye
│   │   ├── Ear
│   │   ├── Nose
│   │   ├── Mouth
│   │   └── Jaw
│   │
│   └── Internal Structures
│
├── Torso
│   ├── Chest
│   │   ├── Heart
│   │   ├── Left Lung
│   │   └── Right Lung
│   │
│   ├── Abdomen
│   │   ├── Liver
│   │   ├── Stomach
│   │   └── Intestines
│   │
│   └── Pelvis
│
├── Left Arm
│   ├── Upper Arm
│   ├── Forearm
│   └── Hand
│       ├── Thumb
│       ├── Index
│       ├── Middle
│       ├── Ring
│       └── Little
│
├── Right Arm
│   └── ...
│
├── Left Leg
│   ├── Thigh
│   ├── Lower Leg
│   └── Foot
│
└── Right Leg
    └── ...
```

This demonstrates the tree architecture only.

The actual human template requires separate content-authoring and validation.

---

# 14. Laterality

## 14.1 Proposed Change

Laterality should become an explicit property of the resulting Location Address where applicable.

The player-facing result should therefore be:

> Right Arm

rather than:

> Arms — Zero-Step parity indicates right.

Zero-Step may remain the mechanism used to derive or distinguish laterality if that mechanism survives the investigation.

However, **laterality should be represented as location data rather than exposed as a digit-parity rule**.

---

## 14.2 Midline Structures

Laterality must not be treated as a mandatory universal tree level.

Some structures are:

- Left
- Right
- Midline / non-lateral

For example, a heart cannot be forced into an arbitrary Left/Right branch simply because laterality exists elsewhere.

Therefore:

> Laterality is a property of applicable Location Nodes, not a mandatory address component.

---

# 15. Parent/Child Address Semantics

The hierarchical model creates a formal ancestry relationship.

Let:

- \(A\) = generated Location Address
- \(R\) = Effect's required location

A generated address satisfies a required location when:

\[
A=R
\]

or:

\[
A \text{ is a descendant of } R
\]

This allows a precise location to satisfy a broader requirement.

Example:

```text
Generated:
Right Index Proximal Phalanx

Required:
Right Index Finger
```

The generated location is a descendant of the required location.

Therefore the location is compatible.

The reverse is not automatically true:

```text
Generated:
Right Hand

Required:
Right Index Proximal Phalanx
```

The generated address is too coarse.

It cannot establish the required specific location.

---

# 16. Armor Interaction

This hierarchy provides a formal basis for location-bound Armor.

If armor coverage is attached to:

```text
Right Forearm
```

then a hit at:

```text
Right Forearm
→ Wrist
→ Hand
```

is **not automatically covered** unless the armor's coverage node includes those descendants.

Conversely, if armor coverage explicitly covers:

```text
Right Arm
```

then descendant locations may be covered according to the armor's declared coverage relationship.

This allows Armor coverage to be represented structurally rather than by an ever-expanding list of independent location names.

The existing location-bound Armor architecture should therefore be treated as a compatibility dependency for future design work, not discarded automatically. Existing project material states that Armor location matching uses the same individual-creature-template anatomy.

---

# 17. Effect Interaction

The proposed architecture preserves the existing principle that Location resolution and Effect resolution are distinct.

Location determines:

> **Where?**

Effect determines:

> **What happens there?**

Therefore:

```text
Core Test
    ↓
Location Address
    ↓
Effect applicability
    ↓
Effect consequence
```

Location Tier should not determine Effect Magnitude.

This preserves the distinction already established between Location Tier and Skill-Tier-based Effect/Wound severity.

---

# 18. Wound Interaction

Existing Wound records use a Location X / Tier-Y / Wound-Z structure.

The proposed model can preserve that representation while replacing `Location X` with a hierarchical address.

Conceptually:

```text
Location:
Right Index Proximal Phalanx

Wound:
Tier-6 Wound -6
```

The exact consequence mechanics remain governed by the existing Wound rules.

The location architecture must therefore not introduce a separate Wound engine.

---

# 19. Terminal Nodes

A Location Template must explicitly permit terminal nodes.

For example:

```text
Eye
```

may be a terminal node.

A Skill-Tier 12 action cannot force the system to invent:

```text
Eye
→ Sub-eye
→ Micro-eye
→ ...
```

if the template does not author those structures.

Therefore:

> A Location Tier represents maximum available resolution, not mandatory anatomical depth.

This is necessary for both implementation feasibility and content consistency.

---

# 20. Tier 6–12 Rarity

The proposed architecture does not require a separate "rare location" mechanic.

If:

\[
L_{\max}=S
\]

then Tier 12 spatial resolution requires a Skill-Tier 12 action.

Consequently:

| Skill-Tier | Potential spatial precision |
|---:|---|
| 1 | Broad |
| 2 | Subregional |
| 3 | Component |
| 4 | Structure |
| 5 | Segment |
| 6 | Subsegment |
| 7 | Fine structure |
| 8 | Microstructure |
| 9 | Internal structure |
| 10 | Internal substructure |
| 11 | Terminal structure |
| 12 | Terminal substructure |

High Location Tiers are therefore naturally rare if high Skill-Tiers are rare.

No additional rarity subsystem is proposed.

---

# 21. Removal of Cumulative Menus

The proposed architecture recommends eliminating the current cumulative-menu model.

Current conceptual model:

```text
Level 4 Menu
    ├── coarse item
    ├── another coarse item
    ├── structure
    ├── organ
    └── ...
```

Proposed model:

```text
Parent
└── Child
    └── Child
        └── Child
```

This is a fundamental difference.

A location's identity comes from its **path**, not merely from its membership in a menu.

---

# 22. Secondary Location Roll

## 22.1 Proposed Disposition

The hierarchical architecture recommends removing the requirement for the DEC-042 secondary location roll.

The proposed model is:

\[
Natural\ Roll
\rightarrow Location\ Index
\rightarrow Location\ Template
\rightarrow Address
\]

rather than:

\[
Natural\ Roll
\rightarrow Location\ Index
\rightarrow Secondary\ Roll
\rightarrow Subzone
\]

This would eliminate a second source of random spatial resolution.

---

## 22.2 Existing DEC-042 Conflict

This proposal directly conflicts with the currently ruled DEC-042 architecture, which mandates the secondary subdivision roll.

Therefore:

**DEC-042 must not be modified automatically.**

If this architecture survives investigation, a formal DEC amendment or supersession decision is required.

---

# 23. Existing Decision Conflicts

The following table identifies decisions requiring review if this proposal advances.

| Existing Decision | Current State | Relationship to Proposal |
|---|---|---|
| DEC-041 | Location architecture/gating | Review required |
| DEC-042 | Secondary d6/d10 subdivision | **Direct architectural conflict** |
| DEC-100 | Tier-1 quartile ranges | Numerical mapping requires review |
| DEC-112 | Level 2–5 flat granularity | **Major architectural replacement candidate** |
| DEC-113 | Effect-specific Location Tier | Review compatibility; concept can remain |
| DEC-062 | Location-bound Armor | Likely compatible with hierarchical matching |
| DEC-030 | Location mismatch fallback | Requires explicit revalidation |
| DEC-033 | Wound Location requirement | Compatible in principle |
| DEC-107 | Effect/Wound Tier = Skill-Tier | Should remain independent |
| DEC-014 | Zero-Step | Provider should remain provisional pending investigation |

The project corpus currently records anatomical mapping as closed under DEC-041, DEC-100, DEC-112, and DEC-113.

Accordingly, this report must be treated as a **reopening proposal**, not as a correction to those decisions.

---

# 24. Proposed Architectural Invariants

If this design direction is accepted, the following should become explicit invariants.

| ID | Proposed invariant |
|---|---|
| LOC-I01 | A Location Address is hierarchical. |
| LOC-I02 | Location resolution does not constitute a second Core Test. |
| LOC-I03 | The natural d100 remains authoritative for Core Test cost, Failure XP, Double eligibility, and normal Core Test consequences. |
| LOC-I04 | A Location Index is interpreted through a target-specific Location Template. |
| LOC-I05 | Skill-Tier determines maximum Location Tier. |
| LOC-I06 | Location Tier does not determine Effect Magnitude. |
| LOC-I07 | A target may terminate before Tier 12. |
| LOC-I08 | No anatomy is invented solely to satisfy a higher Skill-Tier. |
| LOC-I09 | A child location inherits the identity of its complete parent path. |
| LOC-I10 | A descendant address can satisfy a broader parent-location requirement where the Effect permits it. |
| LOC-I11 | A broader address cannot establish a requirement for a more specific descendant location. |
| LOC-I12 | Laterality is explicit location data where applicable. |
| LOC-I13 | Laterality is not a mandatory universal hierarchy level. |
| LOC-I14 | Location Templates are content data rather than hard-coded universal anatomy. |
| LOC-I15 | The maximum architectural Location Tier is 12 unless a future formal decision changes it. |
| LOC-I16 | Numerical Location Index allocation requires separate probability investigation. |

---

# 25. Numerical Allocation Is a Separate Investigation

This report intentionally does **not** establish the final mapping of the 100 Location Index states.

That must be treated as a separate design problem.

The system must determine:

1. How many Location Index states each Tier-1 region receives.
2. How those states divide between left/right structures.
3. How many states each branch receives.
4. Whether anatomical weighting is intended.
5. Whether tactical relevance is intended.
6. Whether exposed surface area should influence probability.
7. How internal structures are weighted.
8. Whether different Location Templates require different allocation strategies.
9. How the 100-state constraint affects Tier 6–12 representation.
10. Whether Zero-Step remains the best Location Index provider.

No arbitrary numerical allocation should be promoted to canonical rules before this investigation.

---

# 26. Recommended Content Model

A future Location Template should conceptually contain at least:

| Field | Purpose |
|---|---|
| Node ID | Stable unique location identifier |
| Parent ID | Hierarchical parent |
| Display Name | Player/GM-facing name |
| Depth | Location Tier |
| Terminal | Whether further authored subdivision exists |
| Laterality | Left / Right / Midline / Not Applicable |
| Children | Descendant nodes |
| Location Index Mapping | Mapping from Location Index states |
| Template ID | Target anatomy/template identity |

These are proposed data-model fields, not new character attributes.

---

# 27. Example Full Address

An eventual implementation could represent:

```text
Template: HUMAN

Location Index: 42

Address:
Tier 1  = Torso
Tier 2  = Abdomen
Tier 3  = Internal
Tier 4  = Liver
Tier 5  = Right Lobe
Tier 6  = Superior Region
Tier 7  = Segment
Tier 8  = Vascular Structure
Tier 9  = Named Vessel
Tier 10 = Vessel Segment
Tier 11 = Terminal Branch
Tier 12 = Terminal Substructure
```

This is an **illustrative address only**.

It is not an approved anatomical mapping.

---

# 28. Why Tier 12 Is a Useful Architectural Ceiling

Tier 12 is not being proposed because the project has established that real-world anatomy requires exactly twelve layers.

It is useful because it provides:

- enough room for extremely high-resolution targets;
- meaningful differentiation between Skill-Tiers 5–12;
- a fixed engine boundary;
- predictable content-authoring requirements;
- controlled maximum complexity;
- no requirement for an unbounded location tree.

The system can therefore support extremely rare high-resolution outcomes without requiring the engine to support arbitrary spatial depth.

---

# 29. Recommended Treatment of Current DEC-112

DEC-112 should **not** simply be extended with:

```text
Level 6 = X
Level 7 = Y
...
Level 12 = Z
```

That would preserve the fundamental flat-menu problem.

Instead, if the proposal survives investigation, DEC-112 should be reconsidered as an architectural decision establishing:

> **Hierarchical Location Addressing**

rather than a catalogue of anatomical menu entries.

The anatomical content itself should then become a separate content-authoring concern.

---

# 30. Recommended Investigation Sequence

The proposed architecture should be tested in the following order.

## Investigation 1 — Information Capacity

Prove that the intended Tier-1-to-Tier-12 address structure can be represented within the 100-state Location Index without unintended ambiguity.

## Investigation 2 — Numerical Allocation

Construct candidate 100-state allocations and calculate their resulting probabilities.

## Investigation 3 — Human Template

Build a complete candidate Human Location Template.

## Investigation 4 — Tier 6–12 Feasibility

Identify realistic mechanically meaningful Tier 6–12 structures without requiring arbitrary microscopic detail.

## Investigation 5 — Laterality

Test explicit left/right representation against the existing Zero-Step architecture.

## Investigation 6 — Effect Compatibility

Test:

- Armor Bypass
- Wound
- Trip
- Disarm/Break Hold
- Equipment Damage

against hierarchical addresses.

## Investigation 7 — Armor Coverage

Test parent/child coverage relationships against the existing location-bound Armor rules.

## Investigation 8 — Mismatch/Fallback

Determine whether DEC-030 remains necessary in its present form once location matching becomes hierarchical.

## Investigation 9 — Secondary Roll Removal

Run a direct comparison between:

- current DEC-042 secondary-roll architecture;
- proposed single-index hierarchical architecture.

## Investigation 10 — Playtest

Use representative attacks at Skill-Tiers 1–12 and record:

- generated locations;
- address depth;
- target validity;
- Effect applicability;
- Armor interactions;
- player comprehension;
- GM adjudication burden;
- probability distribution.

---

# 31. Proposed Decision Decomposition

Rather than attempting to approve the entire architecture in one decision, the work should be separated.

| Proposed Decision | Subject |
|---|---|
| L-001 | Hierarchical Location Address architecture |
| L-002 | Location Index provider |
| L-003 | Single-source deterministic address resolution |
| L-004 | Location Template architecture |
| L-005 | Skill-Tier → maximum Location Tier |
| L-006 | Location Tier 1–12 semantic definitions |
| L-007 | Parent/child location matching |
| L-008 | Explicit laterality representation |
| L-009 | Human Location Template |
| L-010 | 100-state numerical Location Index allocation |
| L-011 | Removal/replacement of secondary location roll |
| L-012 | Armor/location hierarchical matching |
| L-013 | Wound/location representation |
| L-014 | Location mismatch/fallback semantics |

These identifiers are **proposed working identifiers only** and must not be treated as official DEC numbers.

---

# 32. Compatibility Requirements

Any accepted replacement must preserve the following existing system properties unless explicitly amended.

### Core Test

- d100 roll-under.
- Natural roll remains authoritative.
- Exact roll determines resource expenditure.
- Overflow remains HP damage.
- Failure XP remains based on the natural roll.
- Failed doubles retain Advanced Skill implications.

### Skill System

- Skill-Tier remains defined by underlying Attribute count.
- No new Skill category is introduced.
- Location precision does not alter Skill values or caps.

### Effect System

- Location does not become a second Effect roll.
- One-Effect-per-win remains independent.
- Effect Magnitude remains governed by the existing Effect architecture.

### Wound System

- Location remains part of the Wound record.
- Wound Tier remains separate from Location Tier.
- Existing Attribute/Skill wound selection remains unaffected unless separately amended.

---

# 33. Explicit Non-Goals

This report does **not**:

1. Establish new canonical anatomy.
2. Establish final human anatomical content.
3. Establish final 1–100 location probabilities.
4. Revoke Zero-Step.
5. Revoke DEC-042.
6. Revoke DEC-100.
7. Revoke DEC-112.
8. Revoke DEC-113.
9. Create new Skills.
10. Create new Attributes.
11. Create a second Core Test.
12. Create a new resource pool.
13. Create a new damage system.
14. Establish microscopic or biological realism as a universal requirement.

---

# 34. Architectural Assessment

## 34.1 Strengths

The proposed system provides:

- genuine scalability beyond Level 5;
- deterministic hierarchical identity;
- explicit parent/child relationships;
- target-specific anatomy;
- cleaner Armor coverage;
- cleaner Effect targeting;
- meaningful Skill-Tier 6–12 progression;
- elimination of increasingly complicated cumulative menus;
- separation of location precision from Effect severity;
- preservation of the single Core Test architecture;
- controlled maximum resolution.

## 34.2 Risks

The principal risks are:

1. The 100-state Location Index imposes a hard information limit.
2. Numerical allocation may produce undesirable probabilities.
3. Human anatomy may require more authored branches than the d100 can represent distinctly.
4. Replacing DEC-042 may create substantial downstream documentation changes.
5. Existing playtest assumptions may depend on the current quartile/secondary-roll architecture.
6. Location mismatch semantics may change significantly under hierarchical matching.
7. Location Templates may become substantial content-authoring objects.

These risks require investigation rather than assumption.

---

# 35. Final Design Position

The design position emerging from this investigation is:

> **Tiwas should investigate replacing the current flat Tier-1–5 location-menu architecture with a deterministic hierarchical Location Address architecture supporting Location Tiers 1–12.**

The proposed system treats location as:

\[
Location\ Index
\rightarrow
Location\ Template
\rightarrow
Hierarchical\ Address
\]

rather than:

\[
Location\ Index
\rightarrow
Secondary\ Random\ Menu
\]

The Skill-Tier determines how deeply the address may be resolved:

\[
L_{\max}=\min(S,12)
\]

and the target's authored topology determines whether that depth actually exists:

\[
L_{\text{actual}}=\min(S,D)
\]

Tier 6–12 are therefore valid architectural resolutions without requiring every target to contain twelve levels of anatomy.

The key architectural principle is:

> **Location Tier represents spatial resolution depth, not a fixed list of anatomical objects.**

The second key principle is:

> **A Location Index identifies an address path; increasing Skill-Tier reveals greater resolution of that path rather than generating additional random location results.**

---

# 36. Required OpenCode Handling

OpenCode should process this document as a **design proposal and investigation input only**.

It MUST NOT:

- automatically modify canonical rules;
- automatically amend DEC-042;
- automatically amend DEC-100;
- automatically amend DEC-112;
- automatically amend DEC-113;
- treat the Tier-1–12 semantic table as canonical;
- treat illustrative anatomy as canonical;
- treat proposed L-001–L-014 identifiers as official decisions;
- implement the proposed architecture without explicit authorisation.

OpenCode SHOULD:

1. Record the proposal as non-canonical design work.
2. Identify all affected existing decisions.
3. Preserve existing canonical/ruling text.
4. Produce a dependency/change-impact analysis if requested.
5. Prepare investigations for the 100-state information-capacity problem.
6. Prepare candidate Location Templates separately from rule decisions.
7. Escalate contradictions or authority conflicts rather than resolving them autonomously.

---

# 37. Conclusion

The current Tier-5 ceiling is not the fundamental limitation that needs solving.

The deeper issue is the **flat representation of location itself**.

A hierarchical Location Address model provides a coherent architecture in which:

```text
Tier 1
  ↓
Region

Tier 2
  ↓
Subregion

Tier 3
  ↓
Component

Tier 4
  ↓
Structure

Tier 5
  ↓
Segment

Tier 6
  ↓
Subsegment

Tier 7
  ↓
Fine Structure

Tier 8
  ↓
Microstructure

Tier 9
  ↓
Internal Structure

Tier 10
  ↓
Internal Substructure

Tier 11
  ↓
Terminal Structure

Tier 12
  ↓
Terminal Substructure
```

can all exist within one coherent framework.

The architecture therefore supports extremely rare Tier-6–12 outcomes without requiring separate resolution engines or arbitrary additional random rolls.

**No canonical rule is changed by this report. Formal human decision is required before any existing DEC is amended or superseded.**