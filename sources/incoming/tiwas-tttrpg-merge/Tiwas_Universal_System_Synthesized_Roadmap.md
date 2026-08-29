# Tiwas Universal System — Synthesized Mechanical Gap Audit & Implementation Roadmap

## 0. Purpose and Authority

This document synthesizes the Tiwas Core Rules v2, the Comparative Design Direction Brief, the prior systems audit, and Grok's gap/roadmap analysis.

### Authority hierarchy

1. **Tiwas Core Rules v2** is authoritative for all already-locked core mechanics.
2. **Comparative Design Direction Brief** is authoritative for architectural direction and ranked residual decisions.
3. This document resolves only the **organization, dependency analysis, implementation sequencing, and acceptance/regression structure** needed to complete the system.
4. It does **not** silently resolve open designer forks or invent numerical thresholds.

The Core explicitly states that combat, opposed tests, damage beyond Overflow-to-HP, healing, incapacitation/death, rest, equipment, conditions, hazards, magic, NPCs, difficulty/task adjudication and GM procedure remain reserved rather than already-defined mechanics.

---

# 1. Locked Core Baseline

The following are treated as immutable implementation invariants:

- d100 produces **1–100**; `00` means 100.
- Success is `Roll <= Skill`, except that **100 always fails**.
- 100 is always a qualifying failed Double.
- All fractional calculations floor.
- Skills use the defined Tier/attribute Cap system.
- Every test costs the natural die face: **Cost = Roll**.
- Insufficient PE/MP produces direct **Overflow → HP**.
- Failure XP is `max(0, Roll - Skill)`.
- The Skill Roll Pool is generated and resolved within the same failed test; it does not persist.
- Skill Roll Pool advancement cascades up to Cap.
- General XP can raise Skills above Cap.
- Failed Doubles can create Advanced Skills under the locked construction rules.
- Advanced Skill resource type follows the original Tier-1 lineage.
- Derived statistics are live recalculations.
- Recovery is unconditional and occurs last after every test.
- No subsystem may introduce a parallel primary resource or progression currency.

The canonical Core test transaction is therefore:

**Roll → Determine outcome → Pay natural Roll cost → Apply Overflow → Resolve Failure XP / Advanced Skill effects → Recover last**

Every Universal Play Module must invoke this transaction rather than replace it.

---

# 2. Design Priorities

The system must preserve the Brief's locked priority ranking:

1. **Granular physical simulation** where the situation warrants it.
2. **Heroic resilience / low permanent character loss rate.**
3. **Minimum resolution steps per exchange without sacrificing Priority 1.**

The implementation target is therefore not simply "complete combat." It is a universal state-resolution architecture in which combat, social conflict, hazards, crafting, research, travel, magic and other activities reuse the same core transaction.

---

# 3. Complete Gap Inventory

The gaps fall into three categories:

- **Residual decisions** explicitly ranked S-1 through S-12.
- **Universal Play subsystems** required to implement those decisions.
- **Architectural completion layers** required for a genuinely complete universal system but not themselves separate S-residuals.

## 3.1 Ranked Residuals

| Priority | ID | Gap | Status | Primary dependency |
|---:|---|---|---|---|
| 1 | **S-1** | Opposed quality measure selection: Margin / Blackjack / Hybrid | Open | None |
| 2 | **S-2** | Hit-location policy: Tier 0 / 1 / 2 and situation use | Open | S-1 |
| 3 | **S-3** | Outcome Effect trigger thresholds / effect purchasing | Open | S-1 |
| 4 | **S-4** | Wound activation threshold and severity | Open | S-2, S-3 |
| 5 | **S-5** | Armor interaction: Bypass / tag-gated Sunder | Open | S-3, S-4 |
| 6 | **S-6** | Passive vs Active defense and resource cost | Open | S-1 |
| 7 | **S-7** | Exact incapacitation/death pathway | Open | S-4 |
| 8 | **S-8** | Difficulty grades and Failure XP interaction | Open | Core |
| 9 | **S-9** | Extended Test progress: Margin sum vs success count | Open | S-1 |
| 10 | **S-10** | Extended Test progress loss on failure | Open | S-9 |
| 11 | **S-11** | Rest/healing timelines | Open | S-4, S-7 |
| 12 | **S-12** | NPC compression packages | Open | All preceding systems |

The Brief explicitly recommends simulation before locking these choices. In particular, S-1 must be evaluated through contest win-rate/resource-drain behavior, while numerical Quality, wound, Effect and Extended Test thresholds remain unfinalized.

---

## 3.2 Universal Play Subsystems

| ID | System | Why it is required | Residuals |
|---|---|---|---|
| U-01 | Universal opposed contest primitive | Makes contests reusable across combat and non-combat | S-1 |
| U-02 | Contest outcome/tie procedure | Converts two tests into a state result | S-1 |
| U-03 | Difficulty grades | Makes task difficulty universal | S-8 |
| U-04 | Stakes gate/task adjudication | Determines when a test is meaningful | S-8 |
| U-05 | Outcome Effect engine | Converts quality into state change | S-3 |
| U-06 | Net Advantage / Quality-band interface | Controls additional effects | S-3 |
| U-07 | Two-track harm engine | Separates resource/global endurance from localized injury | S-3/S-4 |
| U-08 | Wound-state engine | Defines Light/Serious/Critical and consequences | S-4 |
| U-09 | Location provider interface | Supports Tier 0/1/2 without changing Core | S-2 |
| U-10 | Armor interaction | Connects equipment to harm | S-5 |
| U-11 | Defense engine | Makes defense a normal contest participant | S-6 |
| U-12 | Conditions engine | Provides reusable state effects | S-3/S-4 |
| U-13 | Time/turn/action framework | Supports combat, durations, rest and Extended Tests | S-6/S-9/S-11 |
| U-14 | Equipment/weapon/armor tags | Gates Effects and interactions | S-3/S-5 |
| U-15 | Extended Test engine | Handles prolonged tasks through repeated normal tests | S-9/S-10 |
| U-16 | Environmental hazard engine | Applies existing tests/effects to hazards | S-8 |
| U-17 | Rest/healing engine | Completes resource and wound recovery loop | S-11 |
| U-18 | Death/incapacitation engine | Completes Priority-2 resilience model | S-7 |
| U-19 | NPC compression | Makes encounter construction practical | S-12 |
| U-20 | GM adjudication procedure | Operationalizes universal play | S-8 |
| U-21 | Magic/special-ability grammar | Applies Advanced Skills to setting powers | Advanced Skills / Setting |
| U-22 | Setting-module interface | Prevents setting rules from modifying Core invariants | Architecture |

---

## 3.3 Architectural Completion Gaps

These are not new residual decisions. They are implementation contracts required for completeness.

### A. Core/Module boundary

The Universal Play layer must call the Core transaction rather than duplicate it.

### B. Conditions vs Tags

These must remain distinct:

- **Conditions** = character/world state.
- **Tags** = classification/permission/interaction metadata.

### C. Universal/Setting boundary

A Setting Module may define content and permissions but must not redefine:

- d100 resolution;
- Cost = Roll;
- 100-Fumble;
- Overflow → HP;
- Failure XP;
- Skill Roll Pool;
- Advanced Skill construction;
- Core recovery transaction.

### D. Character-generation completion

The Core defines attribute generation and starting Skill mathematics, but a playable implementation still requires an ordered character-generation procedure, derived-stat initialization, starting resources, and setting-specific starting packages.

### E. Campaign progression procedure

The XP mechanics are locked; the surrounding procedure for when and how General XP is awarded/spent remains a usability layer rather than a new progression economy.

---

# 4. Dependency Graph

The correct implementation dependency is:

**Core invariants**
→ **Core Test Transaction**
→ **S-1 Opposed Primitive**
→ **S-3 Outcome Effects**
→ **S-2 Location Interface**
→ **S-4 Wounds / Two-Track Harm**
→ **S-5 Armor + S-6 Defense**
→ **Time / Action Economy**
→ **S-7 Death / Incapacitation**
→ **S-8 Difficulty + Task Adjudication**
→ **S-9/S-10 Extended Tests**
→ **Conditions / Tags / Equipment / Hazards**
→ **S-11 Rest / Healing**
→ **Magic / Special Abilities**
→ **S-12 NPC Compression**
→ **Setting Interface**
→ **Full Integration Simulation**

Some dependencies are cross-cutting:

- Time is required before durations, rest and ongoing effects are finalized.
- Conditions and Tags support Effects, wounds, equipment and magic.
- The NPC layer depends on the final state model but must still use the same Core transaction.

---

# 5. Residual-to-Roadmap Mapping

| Residual | Resolution phase | What is implemented | What remains deliberately open until simulation/design ruling |
|---|---|---|---|
| **S-1** | Phase 1 | Selectable opposed-quality interface | Global choice among Margin / Blackjack / Hybrid |
| **S-2** | Phase 2 | Tier 0/1/2 location providers | Campaign-wide default / situational policy |
| **S-3** | Phase 3 | Effect engine and quality interface | Exact thresholds/bands |
| **S-4** | Phase 3 | Wound-state engine | Exact activation/severity thresholds |
| **S-5** | Phase 4 | Armor interaction framework | Bypass/Sunder final policy |
| **S-6** | Phase 4 | Passive/active defense framework | Exact cost/default model |
| **S-7** | Phase 5 | Incapacitation/death framework | Exact death triggers |
| **S-8** | Phase 6 | Difficulty/task framework | Final grades and detailed XP interaction |
| **S-9** | Phase 7 | Both Extended progress models | Final progress method |
| **S-10** | Phase 7 | Stall/loss alternatives | Final failure-loss model |
| **S-11** | Phase 9 | Rest/healing framework | Final timelines |
| **S-12** | Phase 11 | NPC compression architecture | Final grades/packages |

This is a crucial distinction:

**Implementation support is not the same as deciding the final rule.**

The system should be coded so an open residual can be simulated without downstream rewrites.

---

# 6. Phased Implementation Roadmap

## Phase 0 — Freeze Invariants and Build the Regression Harness

### Deliverables

- Formalize the Core Test Transaction.
- Create deterministic test-state inputs/outputs.
- Establish regression fixtures for:
  - Cost = Roll;
  - 100-Fumble;
  - 100 as failed Double;
  - Overflow → HP;
  - Failure XP;
  - temporary Skill Roll Pool;
  - cascading;
  - Cap ceiling;
  - General XP above Cap;
  - Advanced Skill creation;
  - Advanced Skill Cap recomputation;
  - mixed-domain Advanced Skills;
  - live derived statistics;
  - unconditional final recovery.

### Acceptance criteria

No Universal Play module can bypass or duplicate the Core transaction.

### Mandatory regression

Test Body and Mind actions at:

- successful low roll;
- successful high roll;
- ordinary failure;
- 100-Fumble;
- failed Double;
- sufficient resource;
- partial resource;
- zero resource;
- Skill 0;
- Skill at/above Cap;
- Skill above 100.

---

# Phase 1 — S-1 Universal Opposed Contest Primitive

## Objective

Create one contest primitive that supports all three candidate quality measures without selecting one globally.

### Deliverables

- Opposed-test input structure.
- Acting/opposing Skill handling.
- Two independent Core test transactions.
- Success/failure combination matrix.
- Tie handling.
- Quality calculation interface.
- Margin implementation.
- Blackjack implementation.
- Hybrid Committed implementation.
- Contest-result structure.
- Configurable situation flag.

### Acceptance criteria

- Both rolls retain natural die-face costs.
- Failure XP is independently generated.
- Failed Doubles remain eligible for Advanced Skill creation.
- 100 remains a mandatory failure.
- Quality does not modify the historical die face.
- No second resource cost is generated by the contest layer.

### Simulation gate

Compare Margin, Blackjack and Hybrid across representative Skill bands, including high Skill and Skill > 99.

Measure:

- win probability;
- PE/MP expenditure;
- contest duration;
- quality distribution;
- high-Skill behavior;
- 100-Fumble behavior.

**Do not lock S-1 before this comparison.**

---

# Phase 2 — S-2 Location Architecture

### Deliverables

Implement interchangeable location providers:

- Tier 0 — no locations.
- Tier 1 — near-zero-step derivation from the existing attack roll.
- Tier 2 — full location/armor/surgery-capable module.

Add a situation/campaign configuration mechanism.

### Acceptance criteria

- No extra die is mandatory for Tier 1.
- Tier 0 works without any location state.
- Tier 2 can support granular injury.
- Location selection never changes the original attack roll.
- Location policy can change without changing the Core transaction.

### Simulation gate

Compare:

- resolution steps;
- wound frequency;
- location distribution;
- lethality;
- Priority-1 simulation fidelity.

**Do not impose a universal Tier 0/1/2 default at this stage.**

---

# Phase 3 — S-3/S-4 Effects and Two-Track Harm

## 3.1 Outcome Effect Engine

### Deliverables

Implement the universal Effect architecture supporting the candidate menu:

1. Inflict Injury
2. Impose Condition
3. Disarm / Break Hold
4. Force Movement / Seize Position
5. Seize Tempo
6. Guard Break
7. Bleed / Ongoing Drain
8. Open Retreat / Compel Yield
9. Damage Equipment
10. Choose Location

Effects are gated by Tags and available only where the relevant situation permits.

### 3.2 Effect purchasing

Implement:

- free-effect handling;
- additional-effect interface;
- Quality/Net Advantage input;
- effect compatibility;
- stacking;
- duration;
- removal.

### 3.3 Two-track harm

Implement:

**Track A:** PE/MP → Overflow → Global HP.

**Track B:** localized wounds/conditions where the location module is active.

### 3.4 Wound engine

Implement:

- wound activation;
- Light/Serious/Critical states;
- consequences;
- stacking;
- location interaction;
- condition generation.

### Acceptance criteria

- Effects produce actual state change.
- Effects never rewrite historical die results.
- PE/MP depletion remains meaningful.
- Empty PE/MP does not automatically equal defeat.
- Overflow remains direct HP damage.
- HP = 0 does not automatically equal death.
- Wounds are not a parallel HP pool.

### Simulation gate

Determine:

- Effect frequency;
- exchange length;
- resource expenditure;
- wound frequency;
- severe injury frequency;
- state-change density.

No numerical Effect or wound thresholds are locked by roadmap fiat.

---

# Phase 4 — S-5 Armor and S-6 Defense

## 4.1 Armor

### Deliverables

- Armor traits.
- Armor tags.
- Bypass interaction.
- Sunder-capable interface.
- Location interaction.
- Equipment damage interaction.

### Acceptance criteria

Armor modifies existing harm resolution rather than creating a second durability/resource economy.

### Decision gate

Compare Bypass and Sunder for:

- bookkeeping;
- simulation fidelity;
- tactical value;
- step count.

Do not hard-lock the final policy until evaluated.

---

## 4.2 Defense

### Deliverables

- Passive defense interface.
- Active defense interface.
- Defense as a normal contest participant.
- Resource-cost handling.
- Defense failure/success outcomes.
- Reaction timing.

### Acceptance criteria

Defense does not create a separate resolution engine.

### Decision gate

Evaluate candidate passive/active models for:

- PE/MP drain;
- number of rolls per exchange;
- survivability;
- tactical decision density;
- Priority 3 step minimization.

The candidate Passive Guard model remains a **candidate**, not a locked rule.

---

# Phase 5 — S-7 Incapacitation, Death and Heroic Resilience

### Deliverables

- HP-zero state.
- Incapacitation procedure.
- Stabilization.
- Survival/death checks.
- Vital-location interaction.
- Permanent injury.
- Death procedure.
- Recovery from incapacitation.

### Acceptance criteria

- HP = 0 is not automatic death.
- Localized injury can matter where locations are active.
- Death remains mechanically distinct from ordinary resource depletion.
- Permanent loss rate is measurable.

### Simulation gate

Optimize against Priority 2:

**Heroic resilience / low permanent character loss**

while retaining meaningful consequences and Priority-1 injury granularity.

Do not lock the proposed major-vital/death-check pathway without simulation.

---

# Phase 6 — S-8 Difficulty, Task Adjudication and Stakes

### Deliverables

- Difficulty-grade interface.
- Skill-side difficulty application.
- Stakes Gate.
- Meaningful uncertainty procedure.
- Task/Skill selection procedure.
- Opposed/unopposed selection.
- Difficulty/Failure XP interaction.
- Difficulty/100-Fumble interaction.
- Difficulty/Advanced Skill interaction.

### Acceptance criteria

- Difficulty does not modify the natural die face.
- Cost remains the natural Roll.
- Failure XP remains governed by the Core-defined Skill basis.
- 100 remains a Fumble.
- Routine/consequence-free actions can avoid unnecessary tests.
- Difficulty cannot be used to circumvent Failure XP or Advanced Skill rules.

---

# Phase 7 — S-9/S-10 Extended Tests

### Deliverables

- Extended Test declaration.
- Explicit time increment.
- Interval test.
- Progress recording.
- Margin-sum implementation.
- Success-count implementation.
- Failure stall implementation.
- Optional failure-loss implementation.
- Existing-condition/hazard/resource complication interface.

### Acceptance criteria

Every interval is an ordinary Tiwas test.

Each interval therefore preserves:

- Cost = Roll;
- Overflow → HP;
- Failure XP;
- failed Doubles;
- Advanced Skill creation;
- recovery.

Progress is only a **running record of existing outcomes**.

It is never:

- spendable;
- transferable;
- bankable as currency;
- a replacement for XP.

### Simulation gate

Compare:

- Margin sum;
- success count;
- stall;
- progress loss.

The final choice remains S-9/S-10.

---

# Phase 8 — Cross-Cutting Support Architecture

## 8.1 Time / Turns / Action Economy

Define:

- rounds;
- turns;
- actions;
- reactions;
- movement;
- simultaneous resolution;
- intervals;
- ongoing-effect timing.

This must be one temporal model usable by combat and Extended Tests.

## 8.2 Conditions

Define:

- condition state;
- application;
- stacking;
- duration;
- removal;
- interaction with Skills and Effects.

## 8.3 Tags

Define the universal metadata grammar for:

- weapons;
- armor;
- Effects;
- locations;
- powers;
- creatures;
- settings.

## 8.4 Equipment

Define:

- equipment records;
- weapon traits;
- armor traits;
- equipment damage;
- encumbrance;
- carrying;
- repair/replacement interface;
- wealth/economy setting hook.

## 8.5 Hazards

Use:

**Trigger → existing Test → Cost → Outcome → existing Effect/Condition/Harm**

No hazard-specific currency is introduced.

### Acceptance criteria

All support systems consume existing Core and Universal Play primitives rather than creating competing subsystems.

---

# Phase 9 — S-11 Rest, Healing and Attrition

### Deliverables

- Rest action.
- Rest duration.
- Safety requirements.
- PE/MP restoration.
- Wound recovery.
- Condition recovery.
- Long-term injury recovery.
- Stabilization.
- Time advancement.

### Acceptance criteria

- No parallel healing currency.
- No D&D-style short-rest reset loop.
- Recovery operates through explicit time.
- Wounds retain meaningful consequences.
- Automatic post-test recovery remains unchanged.

### Simulation gate

Measure:

- PE/MP steady-state;
- resource depletion;
- encounter-to-encounter recovery;
- wound persistence;
- long-task recovery;
- attrition.

The objective is to preserve the resource identity, not maximize recovery.

---

# Phase 10 — Magic and Special Abilities

### Deliverables

Define a power grammar based on Advanced Skills:

- setting permission;
- activation;
- range;
- targets;
- duration;
- Effects;
- opposition;
- Conditions;
- resource domain;
- Overflow;
- failed-double advancement.

### Acceptance criteria

- No mandatory fixed spell list.
- No parallel spell-point economy.
- Ability use remains a Skill test.
- Resource type follows Advanced Skill lineage.
- Overflow remains possible.
- Failed Doubles retain Advanced Skill implications.

Fixed spell lists may exist only as optional setting curricula.

---

# Phase 11 — S-12 NPC Compression

### Deliverables

- NPC attribute packages.
- Skill packages.
- Resource packages.
- Equipment packages.
- Condition packages.
- Effect subsets.
- Role packages.
- Encounter construction templates.

### Acceptance criteria

NPC compression changes presentation/bookkeeping, not resolution mathematics.

NPCs must use:

- the same d100;
- the same Cost = Roll;
- the same Failure XP logic where applicable;
- the same harm model;
- the same Effects;
- the same Core transaction.

### Simulation gate

Validate NPC packages against player encounter survival, resource drain and action economy.

---

# Phase 12 — Universal/Setting Boundary

### Deliverables

Define a formal Setting Module contract.

### Setting Modules may add

- skills;
- Advanced Skill permissions;
- equipment;
- creatures;
- powers;
- Effect tags;
- Conditions;
- hazards;
- location tables;
- setting-specific curricula;
- wealth/economy rules;
- NPC content.

### Setting Modules may not redefine

- d100;
- roll-under;
- 100-Fumble;
- Cost = Roll;
- Overflow → HP;
- Failure XP;
- Skill Roll Pool;
- Advanced Skill construction;
- Core recovery ordering.

### Acceptance criteria

A new setting can be implemented without modifying the Core Engine.

---

# Phase 13 — Full Integration and Simulation Suite

## Scenario families

### A. Opposed exchanges

Test:

- low vs high Skill;
- equal Skills;
- Skill > 99;
- both succeed;
- one succeeds;
- both fail;
- 100-Fumble;
- failed Doubles;
- resource exhaustion.

### B. Combat

Compare:

- locations on/off;
- different location tiers;
- armor variants;
- passive/active defense;
- Conditions;
- Effects;
- wounds;
- incapacitation;
- death.

### C. Extended Tests

Compare:

- Margin progression;
- success-count progression;
- failure stall;
- failure loss;
- PE/MP depletion;
- Overflow;
- Failure XP;
- Advanced Skill creation.

### D. Magic

Test:

- Mind-rooted;
- Body-rooted;
- mixed-domain Advanced Skills;
- Overflow;
- failed Doubles;
- Conditions;
- Effects.

### E. Non-combat

Test:

- social contests;
- research;
- crafting;
- travel;
- environmental hazards;
- stealth;
- technical tasks.

---

# 7. Mandatory Regression Matrix

Every phase must pass the invariant suite.

| Regression | Required result |
|---|---|
| **Cost = Roll** | Resource expenditure equals natural d100 result |
| **100-Fumble** | 100 always fails |
| **100 Double** | 100 always qualifies as failed Double |
| **Overflow → HP** | Shortfall becomes direct HP damage |
| **Failure XP** | Failed tests generate Core-defined XP |
| **100-Fumble XP** | XP cannot become negative |
| **Skill Roll Pool** | Generated and resolved within the same failed test |
| **Cascading** | Multiple increases possible within one pool where affordable |
| **Cap ceiling** | Skill Roll Pool cannot exceed Cap |
| **General XP above Cap** | General XP remains the mechanism for above-Cap Skills |
| **Advanced Skill trigger** | Only qualifying failed Doubles trigger creation |
| **Advanced Tier** | New Tier = failed Tier + 1 |
| **Advanced Attribute** | Added attribute cannot duplicate an existing formula attribute |
| **Advanced Cap** | New Cap is recalculated from full attribute set |
| **Advanced resource domain** | Original Tier-1 lineage controls resource type |
| **Live derived stats** | Attribute changes immediately update dependent derived values |
| **Recovery ordering** | Recovery always occurs last |
| **No parallel currencies** | Universal Play introduces no competing primary resource/progression currency |

---

# 8. Acceptance Criteria for a Complete Universal Tiwas System

Tiwas is mechanically complete only when all of the following are true.

## Core

The existing Core Rules v2 remain unchanged.

## Resolution

Every meaningful test invokes the same Core Test Transaction.

## Contests

Opposed actions use a common primitive with configurable quality measure.

## State change

Success can produce meaningful tactical/narrative state change through the universal Effect architecture.

## Harm

Resource expenditure, Overflow, Global HP, wounds and Conditions interact through the two-track model.

## Granularity

Hit-location fidelity can be selected by situation without rewriting the Core.

## Resilience

The completed harm/death model preserves heroic resilience without making injury consequence-free.

## Time

Combat, Extended Tests, Conditions, rest and ongoing effects use a coherent temporal model.

## Progression

Failure XP, cascading Skill Roll Pool and Advanced Skills remain the primary organic growth engine.

## Extended Tasks

Long-term work uses repeated ordinary Tiwas tests without a new Progress economy.

## Powers

Magic and special abilities use Advanced Skills rather than a mandatory parallel spell system.

## NPCs

NPCs use compressed representations of the same mechanics.

## Settings

Settings add content and permissions without modifying Core invariants.

---

# 9. Non-Negotiable Design Constraints

The following rules apply to every future implementation phase:

1. **Do not lock S-1 prematurely.**
2. **Do not lock S-2 prematurely.**
3. Do not invent wound, Effect, Quality or Extended Test numerical thresholds outside simulation.
4. Do not turn recommended approaches into mandatory rules without an explicit designer ruling.
5. Do not modify the historical die face after rolling.
6. Do not introduce a second primary resource economy.
7. Do not introduce a second progression currency.
8. Do not convert Extended Test Progress into spendable points.
9. Do not replace Overflow → HP with a different exhaustion model.
10. Do not replace Failure XP with milestone-only advancement.
11. Do not make 100 a success at high Skill.
12. Do not remove failed-double Advanced Skill creation.
13. Do not allow Universal Play Modules to bypass the Core Test Transaction.
14. Do not make HP a conventional escalating primary combat-health system.
15. Do not use rest as a rapid resource-reset mechanism that collapses the resource identity.
16. Do not create bespoke resolution engines for combat, magic, NPCs or hazards.

---

# 10. Final Synthesis

The strongest synthesis of the two audits is:

### Grok's contribution retained

- direct S-1 → S-12 sequencing;
- compact residual mapping;
- explicit simulation gates;
- implementation phases;
- strong regression emphasis;
- explicit preservation of Universal Play as the main completion layer.

### Earlier audit contribution retained

- broader mechanical gap inventory;
- Core Test Transaction as an architectural contract;
- distinction between Conditions and Tags;
- explicit Universal/Setting boundary;
- character-generation and campaign-procedure completeness;
- detailed contest/tie/outcome requirements;
- cross-cutting Time architecture;
- explicit distinction between implementation support and final residual rulings.

### Critical corrections applied

- S-1 remains open.
- S-2 remains open.
- S-5 remains open until evaluated.
- S-6 remains open until evaluated.
- S-7 remains open until evaluated.
- S-9/S-10 remain open until evaluated.
- S-11 remains open until evaluated.
- No example numerical threshold is promoted into a rule.
- Candidate recommendations remain candidates.

The resulting architecture is:

**TIWAS CORE ENGINE**
→ **CORE TEST TRANSACTION**
→ **UNIVERSAL CONTEST / STATE / HARM / TIME PRIMITIVES**
→ **UNIVERSAL PLAY MODULES**
→ **SETTING MODULE INTERFACE**
→ **SETTING CONTENT**

The governing implementation principle is:

> **Every Universal Play Module must be an adapter around the locked Tiwas Core transaction, never a competing resolution, resource, progression, or recovery engine.**

This preserves the defining Tiwas loop:

**Attempt → Roll → Pay natural die-face cost → Resolve success/failure → Apply state change or Overflow → Generate failure growth → Recover**

while leaving the explicitly designer-controlled forks open until simulation provides sufficient evidence to resolve them.
