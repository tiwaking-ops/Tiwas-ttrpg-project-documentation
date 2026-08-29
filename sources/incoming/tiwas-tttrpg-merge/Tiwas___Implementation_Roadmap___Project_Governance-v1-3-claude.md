# Tiwas — Implementation Roadmap & Project Governance

**Document Version:** v1.3  
**Document Status:** Authoritative Project/Implementation Guidance  
**Rule Authority:** None — this document does not create game mechanics  
**Supersedes:** Implementation Roadmap & Project Governance v1.2  
**Purpose:** Define dependencies, implementation sequence, simulation gates, regression requirements and governance for completing Tiwas  
**Important:** Implementation guidance must never be mistaken for a design ruling.

---

# 0. Purpose

This document governs how the Tiwas ruleset progresses from its current locked Core and S-1 state toward a complete universal RPG system.

It exists separately from the rules so that:

- project sequencing does not become game law;
- candidate mechanics can be implemented without being declared final;
- future LLM sessions have a stable development process;
- regression requirements remain visible;
- unresolved decisions are not accidentally promoted.

---

# 1. Authority Boundary

The implementation hierarchy is:

```text
CANONICAL RULES
      ↓
PROPOSALS / WIP
      ↓
IMPLEMENTATION ROADMAP
```

The Roadmap may explain:

- what should be implemented;
- what depends on what;
- what should be simulated;
- what acceptance tests should exist.

It may not independently decide:

- numerical thresholds;
- final Quality rules;
- wound severity;
- death triggers;
- armour mechanics;
- defence costs;
- Extended Test progress;
- other unresolved designer decisions.

---

# 2. Locked Core Invariants

Every implementation must preserve:

- d100 = 1–100;
- `00` = 100;
- Roll-under resolution;
- mandatory 100-Fumble;
- 100 as a failed Double;
- floor rounding;
- Tier/attribute Cap system;
- Cost = Roll;
- Overflow → HP;
- Failure XP;
- temporary Skill Roll Pool;
- Skill Roll Pool Cap ceiling;
- General XP above Cap;
- Advanced Skill creation;
- Advanced Skill full-formula Cap recomputation;
- Advanced Skill lineage resource domain;
- live derived statistics;
- unconditional final recovery;
- no competing primary resource/progression economy.

The canonical Core Test Transaction is:

```text
Roll
→ Outcome
→ Natural Roll Cost
→ Overflow
→ Failure XP / Advanced Skill effects
→ Recovery
```

Universal Play modules must call this transaction rather than duplicate or replace it.

---

# 3. Development Priorities

All implementation decisions should preserve the current priority order:

1. Granular physical simulation where warranted.
2. Heroic resilience / low permanent character loss.
3. Minimum resolution steps without sacrificing Priority 1.

---

# 4. Residual Decision Roadmap

| Priority | ID | Decision | Current status | Dependency |
|---:|---|---|---|---|
| 1 | S-1 | Opposed Quality | **Locked** | Core |
| 2 | S-2 | Hit-location architecture | **Provider locked (evidence-strengthened) / Tier policy WIP** | S-1 |
| 3 | S-3 | Outcome Effects | Open | S-1 |
| 4 | S-4 | Wound activation/severity | Open | S-2/S-3 |
| 5 | S-5 | Armor | Open | S-3/S-4 |
| 6 | S-6 | Defense | Open | S-1 |
| 7 | S-7 | Incapacitation/death | Open | S-4 |
| 8 | S-8 | Difficulty/task adjudication | Open | Core |
| 9 | S-9 | Extended Test progress | Open | S-1 |
| 10 | S-10 | Extended Test failure loss | Open | S-9 |
| 11 | S-11 | Rest/healing | Open | S-4/S-7 |
| 12 | S-12 | NPC compression | Open | preceding systems |

The Roadmap must always reflect the current status rather than preserving obsolete status labels from earlier documents.

---

# 5. Universal Play Subsystems

| ID | System | Purpose | Main dependency |
|---|---|---|---|
| U-01 | Opposed Contest | Universal contests | S-1 |
| U-02 | Contest Outcome | Converts test results into contest result | S-1 |
| U-03 | Difficulty | Universal task difficulty | S-8 |
| U-04 | Stakes Gate | Determines when testing is meaningful | S-8 |
| U-05 | Outcome Effects | Converts success into state change | S-3 |
| U-06 | Quality/Advantage Interface | Controls additional Effects | S-3 |
| U-07 | Two-Track Harm | Resources/HP plus wounds | S-3/S-4 |
| U-08 | Wound Engine | Injury states | S-4 |
| U-09 | Location Provider | Tier 0/1/2 location architecture | S-2 |
| U-10 | Armor | Equipment/harm interaction | S-5 |
| U-11 | Defense | Passive/active defence | S-6 |
| U-12 | Conditions | Reusable state effects | S-3/S-4 |
| U-13 | Time/Action | Unified temporal framework | S-6/S-9/S-11 |
| U-14 | Equipment Tags | Interaction metadata | S-3/S-5 |
| U-15 | Extended Tests | Multi-interval tasks | S-9/S-10 |
| U-16 | Hazards | Environmental resolution | S-8 |
| U-17 | Rest/Healing | Recovery beyond normal test recovery | S-11 |
| U-18 | Death/Incapacitation | Completes harm loop | S-7 |
| U-19 | NPC Compression | Practical encounter construction | S-12 |
| U-20 | GM Procedure | Universal adjudication | S-8 |
| U-21 | Magic/Special Abilities | Setting power grammar | Advanced Skills |
| U-22 | Setting Interface | Isolate setting rules | Architecture |

---

# 6. Dependency Graph

The primary implementation path is:

```text
LOCKED CORE
    ↓
CORE TEST TRANSACTION
    ↓
S-1 / OPPOSED CONTEST
    ↓
S-3 / OUTCOME EFFECTS
    ↓
S-2 / LOCATION
    ↓
S-4 / WOUNDS + TWO-TRACK HARM
    ↓
S-5 / ARMOR
+
S-6 / DEFENSE
    ↓
TIME / ACTION ECONOMY
    ↓
S-7 / INCAPACITATION + DEATH
    ↓
S-8 / DIFFICULTY + TASK ADJUDICATION
    ↓
S-9 / S-10 EXTENDED TESTS
    ↓
CONDITIONS / TAGS / EQUIPMENT / HAZARDS
    ↓
S-11 / REST + HEALING
    ↓
MAGIC / SPECIAL ABILITIES
    ↓
S-12 / NPC COMPRESSION
    ↓
SETTING INTERFACE
    ↓
FULL INTEGRATION
```

Cross-cutting dependencies:

- Time is required for durations, Rest and ongoing Effects.
- Conditions and Tags support Effects, wounds, equipment and powers.
- NPC compression depends on the completed state model.
- Setting modules must consume the completed Universal Play layer.

---

# 7. Phase 0 — Regression Harness

Before extending the system, establish deterministic regression tests for the Core.

Required cases:

- successful low roll;
- successful high roll;
- ordinary failure;
- 100-Fumble;
- failed Double;
- sufficient resource;
- insufficient resource;
- zero resource;
- Skill 0;
- Skill at Cap;
- Skill above Cap;
- Skill above 100;
- Advanced Skill creation;
- Advanced Skill Cap recomputation;
- mixed-domain Advanced Skill;
- live derived-stat changes;
- final recovery.

Acceptance criterion:

> No Universal Play implementation may bypass the Core regression suite.

---

# 8. Phase 1 — S-1 Opposed Contest

**Status: Complete / Locked**

S-1 has already completed its validation and acceptance process.

Implementation requirements:

- two independent Core Tests;
- success/failure matrix;
- selectable Quality;
- Margin;
- Blackjack;
- Hybrid Committed;
- Failure/Failure Repeat;
- exact Quality tie Repeat;
- no second resource pool.

The natural roll remains authoritative for Cost and all Core consequences.

No further S-1 development is planned unless new evidence triggers formal reopening.

---

# 9. Phase 2 — S-2 Hit Locations

**Status: Partially locked / WIP**

The Tier-1 Location Index provider is complete: use canonical **Zero-Step**, which exchanges the tens and units digits of the attacker's natural d100 roll. It is deterministic; players do not choose between the natural and transformed results.

Remaining implementation and design work:

- Tier 0;
- Tier-2 interface;
- scene/campaign tier policy;
- anatomical mapping from Location Index to zone;
- downstream interfaces for Effects, wounds, armour and defence.

Acceptance tests:

- Zero-Step exchanges the percentile digits, including `00`/100 handling.
- Tier 1 requires no mandatory additional die.
- Zero-Step has no player-choice branch.
- Tier selection and Location Index derivation never alter the original roll or Core Test consequences.
- Tier 0 creates no location state.
- Location data can be consumed by later Effects/Wound/Armor systems without becoming an alternate Core resolution engine.

E9 usability evidence is complete: 50 participants (25 new to RPGs and 25 RPG players new to Tiwas), tested in ten groups of five with two physical d10s, reported no difficulty with rolling or digit exchange and gave positive feedback.

Comparative validation against Units-Digit is also complete (Canonical Rules §14.6): Zero-Step showed materially lower distribution error and no structurally-unreachable-zone risk across tested tables. A further usability check on derivation cost across rolling methods other than two physical d10s remains an accepted, disclosed, non-blocking residual.

The broader tier policy, anatomical mapping and downstream interaction remain open and require their own design and validation gates. Do not treat the completed Tier-1 provider decision as closure of S-2 as a whole.

---

# 10. Phase 3 — S-3/S-4 Effects and Harm

Implement the structural interface first.

Candidate Effects:

1. Injury.
2. Condition.
3. Disarm / Break Hold.
4. Movement / Position.
5. Tempo.
6. Guard Break.
7. Bleed / Drain.
8. Retreat / Yield.
9. Equipment Damage.
10. Location selection.

Implement two-track harm:

```text
Track A
PE / MP
   ↓
Overflow
   ↓
Global HP

Track B
Location
   ↓
Wound
   ↓
Condition / Disability / Death Check
```

Acceptance criteria:

- Effects create real state changes.
- Effects do not alter historical rolls.
- Empty PE/MP is not automatic defeat.
- Overflow remains HP damage.
- HP = 0 is not automatically death.
- Wounds are not a second HP pool.

Simulation gate:

Measure:

- Effect frequency;
- exchange length;
- resource expenditure;
- wound frequency;
- severe injury;
- state-change density.

Do not lock numerical thresholds without the required evidence and designer ruling.

---

# 11. Phase 4 — Armor and Defense

## 11.1 Armor

Implement:

- Armor Traits;
- Armor Tags;
- Bypass interface;
- Sunder interface;
- location interaction;
- equipment damage.

Compare candidate models for:

- bookkeeping;
- tactical value;
- simulation fidelity;
- resolution steps.

## 11.2 Defense

Implement:

- passive defense interface;
- active defense interface;
- defense as a normal contest participant;
- resource interaction;
- timing.

Compare candidates for:

- PE/MP drain;
- number of rolls;
- survivability;
- tactical decision density;
- resolution steps.

No candidate should be promoted to canonical merely because it is convenient to implement.

---

# 12. Phase 5 — Incapacitation and Death

Implement:

- HP-zero state;
- incapacitation;
- stabilization;
- survival;
- permanent injury;
- death;
- recovery from incapacitation.

Simulation target:

> Preserve heroic resilience while retaining meaningful physical consequences.

The permanent character-loss rate must be measured.

No proposed death threshold becomes canonical until the decision gate is passed.

---

# 13. Phase 6 — Difficulty and Task Adjudication

Implement:

- difficulty grades;
- Skill-side modification;
- Stakes Gate;
- meaningful-uncertainty test;
- Skill selection;
- opposed/unopposed selection.

Verify interaction with:

- Cost;
- Failure XP;
- 100-Fumble;
- Doubles;
- Advanced Skills.

Difficulty must not alter the natural die face.

---

# 14. Phase 7 — Extended Tests

Implement Extended Tests as repeated ordinary Tiwas tests.

Each interval preserves:

- Cost = Roll;
- Overflow → HP;
- Failure XP;
- failed Doubles;
- Advanced Skills;
- Recovery.

Candidate progress models:

- Margin accumulation;
- Success count.

Candidate failure models:

- stall;
- progress loss;
- complication.

Compare:

- task completion time;
- resource depletion;
- failure frequency;
- growth;
- Overflow;
- Advanced Skill generation.

Progress must never become a second currency.

---

# 15. Phase 8 — Cross-Cutting Architecture

Define:

## Time

- rounds;
- turns;
- actions;
- reactions;
- movement;
- intervals;
- ongoing timing.

## Conditions

- application;
- stacking;
- duration;
- removal;
- interaction.

## Tags

- weapon;
- armour;
- Effect;
- location;
- power;
- creature;
- setting.

## Equipment

- records;
- Traits;
- damage;
- carrying;
- encumbrance;
- repair/replacement.

## Hazards

Use:

```text
Trigger
→ Existing Test
→ Cost
→ Outcome
→ Existing Effect / Condition / Harm
```

No subsystem-specific currency should be created.

---

# 16. Phase 9 — Rest and Healing

Implement the attrition loop after harm and death rules are sufficiently stable.

Required areas:

- Rest;
- resource recovery;
- wound recovery;
- healing time;
- ongoing conditions;
- recovery from incapacitation.

Evaluate against the requirement that Rest must not trivialize the resource identity.

---

# 17. Phase 10 — Magic and Special Abilities

Implement a setting-facing power grammar around Advanced Skills.

Verify:

- Body-rooted powers;
- Mind-rooted powers;
- mixed-domain Advanced Skills;
- Overflow;
- failed Doubles;
- Conditions;
- Effects;
- Extended Tests.

Fixed spell lists may exist as setting content but must not be required by the Core.

---

# 18. Phase 11 — NPC Compression

NPC construction should compress the same underlying mechanics rather than introduce a separate NPC engine.

Evaluate:

- encounter construction time;
- mathematical compatibility;
- resource behaviour;
- survivability;
- challenge curves.

NPC packages must still resolve through the same Universal Play architecture.

---

# 19. Phase 12 — Setting Interface

A setting module may add:

- content;
- permissions;
- creatures;
- equipment;
- powers;
- technology;
- magic;
- Tags;
- Effects.

A setting module may not redefine:

- d100;
- roll-under;
- 100-Fumble;
- Cost = Roll;
- Overflow → HP;
- Failure XP;
- Skill Roll Pool;
- Advanced Skill construction;
- Core recovery.

Acceptance criterion:

> A new setting can be implemented without modifying the Core Engine.

---

# 20. Phase 13 — Full Integration Simulation

## 20.1 Opposed exchanges

Test:

- low vs high Skill;
- equal Skill;
- Skill > 99;
- both succeed;
- one succeeds;
- both fail;
- 100-Fumble;
- failed Doubles;
- resource exhaustion.

## 20.2 Combat

Test:

- locations on/off;
- location tiers;
- armour;
- defense;
- Effects;
- Conditions;
- wounds;
- incapacitation;
- death.

## 20.3 Extended Tests

Compare:

- progress models;
- failure models;
- resource drain;
- Overflow;
- Failure XP;
- Advanced Skill creation.

## 20.4 Powers

Test:

- Mind-rooted;
- Body-rooted;
- mixed-domain;
- Overflow;
- failed Doubles;
- Conditions;
- Effects.

## 20.5 Non-combat

Test:

- social contests;
- research;
- crafting;
- travel;
- hazards;
- stealth;
- technical tasks.

---

# 21. Mandatory Regression Matrix

| Invariant | Required result |
|---|---|
| Cost = Roll | Resource expenditure equals natural roll |
| 100-Fumble | 100 always fails |
| 100 Double | 100 always qualifies as failed Double |
| Overflow → HP | Resource shortfall becomes HP damage |
| Failure XP | Failed tests generate XP |
| Failure-XP clamp | XP never becomes negative |
| Skill Roll Pool | Resolved within the same failed test |
| Cascading | Multiple increases possible where affordable |
| Cap ceiling | Skill Roll Pool cannot exceed Cap |
| General XP above Cap | Above-Cap Skill advancement remains possible |
| Advanced Skill trigger | Only qualifying failed Doubles trigger |
| Advanced Tier | Tier + 1 |
| Advanced Attribute | No duplicate attribute |
| Advanced Cap | Full formula recalculation |
| Resource lineage | Original Tier-1 domain controls resource |
| Live statistics | Attribute changes propagate immediately |
| Recovery | Always last |
| No parallel currencies | No competing primary resource/progression system |

---

# 22. Acceptance Standard for a Complete Universal System

Tiwas should not be considered mechanically complete until:

- every meaningful test uses the common Core transaction;
- opposed actions use the universal contest primitive;
- successful contests can create meaningful state change;
- harm supports both resource attrition and meaningful injury;
- location granularity is configurable;
- the completed death model preserves heroic resilience;
- combat and Extended Tests share coherent time architecture;
- Conditions and Tags are reusable;
- progression remains failure-driven;
- Extended Tests do not create a second currency;
- powers use the universal Skill architecture;
- NPCs use compressed versions of the same mechanics;
- settings can be added without modifying Core invariants;
- the full regression suite passes.

---

# 23. Project Governance

## 23.1 Status transitions

The normal lifecycle is:

```text
Idea
 ↓
Proposal
 ↓
WIP
 ↓
Independent Review
 ↓
Simulation / Analysis
 ↓
Designer Ruling
 ↓
Accepted
 ↓
Locked / Canonical
```

An item may return to WIP if evidence exposes a substantive problem.

## 23.2 Evidence classes

Design documentation should distinguish:

### Mechanical fact

Directly follows from existing locked rules.

### Empirical finding

Supported by simulation, playtesting, or other explicit evidence.

### Designer ruling

A deliberate design choice not mathematically forced by the system.

### Recommendation

A proposed preference that has not yet been accepted.

### Architectural constraint

A rule governing how systems interact rather than what the game mechanic numerically does.

Future documents should label these categories where confusion is likely.

---

# 24. LLM Governance Rules

Future LLM sessions must:

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
4. Never promote a proposal because it appears repeatedly in documentation.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. Never silently resolve an open designer fork.
7. Identify contradictions between current and historical documents.
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a canonical rule.
11. Never create a parallel core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. When a subsystem is locked, update the canonical document and its changelog.
14. When a proposal is superseded, retain its historical significance but clearly mark it Superseded.
15. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

---

# 25. Documentation Maintenance Rule

The three consolidated documents should remain synchronized.

### When a rule becomes locked

Update:

1. Canonical Rules;
2. Canonical Changelog;
3. Proposal status;
4. Roadmap status/dependencies;
5. regression requirements if applicable.

### When a proposal changes

Update:

1. Proposals/WIP;
2. relevant Roadmap dependency or phase;
3. do not modify Canonical Rules.

### When an implementation decision changes

Update:

1. Roadmap;
2. relevant WIP note if it affects a design proposal;
3. do not modify Canonical Rules unless the actual game mechanic has changed through formal governance.

---

# 26. Core Project Principle

The implementation target is not merely "complete combat."

The target is:

> **A universal state-resolution architecture in which combat, social conflict, hazards, crafting, research, travel, magic and other activities reuse the same Tiwas Core transaction.**

The central architectural rule is:

> **Every Universal Play Module must be an adapter around the locked Tiwas Core transaction, never a competing resolution, resource, progression, or recovery engine.**
