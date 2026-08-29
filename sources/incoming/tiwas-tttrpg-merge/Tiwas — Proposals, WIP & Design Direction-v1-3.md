# Tiwas — Proposals, WIP & Design Direction

**Document Version:** v1.3  
**Document Status:** Non-Canonical Design Repository  
**Authority:** Design exploration only  
**Supersedes:** Proposals, WIP & Design Direction v1.2  
**Purpose:** Central repository for unresolved, proposed, experimental and directional Tiwas mechanics  
**Critical rule:** Nothing in this document is canonical merely because it is described in detail.

---

# 0. How to Read This Document

This document contains material that may become part of Tiwas but has not yet completed the locking process.

Every item should be understood according to its status:

| Status | Meaning |
|---|---|
| **Proposed** | A candidate rule under active consideration |
| **WIP** | Currently being developed or reviewed |
| **Experimental** | Tested or invented for exploration but explicitly excluded from the ruleset |
| **Design Direction** | An architectural or philosophical preference, not necessarily a mechanic |
| **Reserved** | Known required subsystem with no settled implementation |
| **Superseded** | Historical material retained for understanding but no longer current |

Only the Canonical Rules document creates current rules.

---

# 1. Locked Design Direction

The following high-level design principles are retained as the current direction for Tiwas development.

## 1.1 Identity

> Tiwas is a high-consequence percentile universal RPG in which every attempt costs resources, every failure generates growth, and every meaningful success changes the tactical or narrative state.

## 1.2 Priorities

1. Granular physical simulation where appropriate.
2. Heroic resilience / low permanent character loss.
3. Minimum resolution steps without sacrificing meaningful simulation.

## 1.3 Architecture

The intended architecture is:

```text
TIWAS CORE ENGINE
        ↓
CORE TEST TRANSACTION
        ↓
UNIVERSAL PLAY MODULES
        ↓
SETTING MODULES
        ↓
SETTING CONTENT
```

A setting should add content and permissions rather than rewrite the Core engine.

---

# 2. S-2 — Hit-Location Architecture

**Status: Partially locked / WIP**

S-2 depends on the locked S-1 opposed-contest primitive. Its Tier-1 Location Index provider is now canonical; the broader hit-location architecture remains WIP.

## 2.1 Locked S-2 decision

The Canonical Rules & Changelog v1.2 locks **Zero-Step** as the Tier-1 Location Index provider.

Zero-Step exchanges the tens and units digits of the attacker's natural d100 roll. It is deterministic: the attacker does not choose between the natural and transformed results. The transformation is a read-only post-process and does not alter the Core Test Transaction.

The canonical document is authoritative for the exact rule and its examples.

## 2.2 Purpose of remaining S-2 work

Define how Tiwas handles physical hit locations without forcing every scene to use maximum-granularity combat procedures.

## 2.3 Location-granularity tiers

| Location Tier | Model | Resolution cost | Intended use |
|---|---|---:|---|
| 0 | No location state | Lowest | Mass brawls, cinematic fighting, scenes where locations add little |
| 1 | Zero-Step Location Index from the existing attack roll | Near-zero | Standard simulation-grade play, formal duels |
| 2 | Full location / armour / surgery model | Higher | Optional gritty play |

**Important:** Location Tiers are unrelated to Skill Tier. Core Skill Tier measures attributes in a Skill Cap formula; Location Tier measures physical-location granularity.

## 2.4 Architecture retained as WIP

The intended architecture remains a read-only post-process that consumes a historical Core Test or S-1 participant roll. Tier selection must not alter Cost, Outcome, Failure XP, Double eligibility or Recovery.

Tier 0 generates no location state. Tier 2 remains a future high-granularity module; its location procedure, armour and surgery interaction, anatomical mapping and resolution cost are unresolved.

For Tier 1, the Location Index is a numeric intermediate value, not a body-part name. An anatomical mapping table is still required and is not canonical.

## 2.5 Open design questions

The following remain open:

- whether the location tier is universally fixed or selected by situation, scene or campaign;
- when Tier 1 is invoked;
- the anatomical mapping table;
- Tier-2 procedure and resolution cost;
- interaction with wounds, armour, defence and Outcome Effects.

Situation-dependent tier selection remains a design direction only, not a locked rule.

## 2.6 E9 human usability playtest

**Evidence class: Empirical finding — passed for the tested physical two-d10 method only**

The E9 playtest used two physical d10s with 50 participants in ten groups of five:

- 25 participants new to RPGs; and
- 25 RPG players new to Tiwas.

Participants reported no difficulty rolling the dice or exchanging the digits for hit location, and feedback was positive. This evidence supports usability of Zero-Step for the tested physical two-d10 method only. A single d100, digital roller, verbally announced result, and other input methods were not tested and are not covered by this finding. It did not settle the remaining architecture.

## 2.7 Future optional-rule observations

Participants asked whether they could choose the natural or swapped number. This is recorded as a design observation, not a current rule. The canonical basic rule remains deterministic and provides no such choice.

For a future optional-rule appendix, the designer may consider:

1. attacker choice granted only by an explicit special ability; and
2. defender choice.

Neither option is authorised for current play, nor does this section recommend one.

## 2.8 Comparative derivation-cost residual

Separate from E9, the completed comparison found that Units-Digit requires 0–1 additional derivation operations across the examined rolling modes, while Zero-Step requires 1–2. This is a structural comparison of derivation steps, not a human-usability result and not an additional E9 label.

The physical two-d10 playtest does not establish comparative usability for other input methods. Any future optional mode or implementation should test its own presentation method if human usability matters to that decision.

---

# 3. S-3 — Outcome Effects

**Status: Reserved / Proposed Architecture**

Tiwas is intended to resolve opposed contests into meaningful state change rather than simple HP attrition.

A short universal Effect menu is preferred.

## 3.1 Candidate Effect menu

1. Inflict Injury.
2. Impose Condition.
3. Disarm / Break Hold.
4. Force Movement / Seize Position.
5. Seize Tempo.
6. Guard Break.
7. Bleed / Ongoing Drain.
8. Open Retreat / Compel Yield.
9. Damage Equipment.
10. Choose Location.

The final menu, trigger rules, purchasing rules, and numerical thresholds remain unresolved.

## 3.2 Effect purchasing

Current proposal:

- one successful contest may produce a basic/free effect;
- additional effects may require Net Advantage / Quality bands;
- some effects may be gated by Tags;
- some exceptional effects may be tied to qualifying successes.

This is not canonical.

## 3.3 Non-negotiable architectural constraint

Effects must never modify the historical die roll.

---

# 4. S-4 — Two-Track Harm and Wounds

**Status: Reserved / WIP Direction**

The current design direction separates:

### Track A — Resources / Global HP

Physical Energy and MP are the primary endurance layer.

Resource exhaustion can create Overflow → HP damage.

### Track B — Localized Wounds / Conditions

Where locations are active, meaningful physical injury can produce localized Wounds and Conditions.

The intended Wound states are currently:

- Light;
- Serious;
- Critical.

Exact activation thresholds, severity formulas and consequences are unresolved.

## 4.1 Design constraints

- Empty PE/MP must not automatically mean defeat.
- Overflow remains HP damage.
- HP = 0 should not automatically equal death.
- Wounds are not intended to become a second conventional HP pool.
- Injury must remain consequential without producing excessive permanent character loss.

---

# 5. S-5 — Armor

**Status: Reserved / Proposed**

Current candidates include:

- Bypass-style armour interaction;
- tag-gated Sunder interaction.

The intended architecture is to use Armor Traits/Tags rather than create a second durability economy.

Final armour interaction remains unresolved.

---

# 6. S-6 — Defense

**Status: Reserved / Proposed**

Defense is intended to operate as part of the universal contest architecture.

Candidates include:

- passive defense;
- active defense;
- defense as a normal contest participant;
- resource-costed reactions.

A previous proposal suggested a Passive Guard approach based on half-Skill with no PE cost.

That is a **candidate only**, not a Tiwas rule.

The final model must be evaluated for:

- resource drain;
- number of rolls;
- survivability;
- tactical choice;
- resolution-step count.

---

# 7. S-7 — Incapacitation and Death

**Status: Reserved**

The current direction favours heroic resilience.

Important current design constraints:

- HP = 0 should not automatically mean death.
- Incapacitation should be mechanically distinct from ordinary resource depletion.
- Serious localized injury may matter where locations are active.
- Permanent character loss should remain comparatively uncommon.

Possible major-vital/death-check concepts remain proposals only.

No final death threshold is locked.

---

# 8. S-8 — Difficulty, Task Adjudication and Stakes

**Status: Reserved / WIP Direction**

A universal difficulty system is required.

The current direction is that difficulty should operate on the **Skill side** rather than altering the natural die face.

The natural roll must remain the natural roll because it determines:

- Cost;
- Failure XP;
- Double status;
- Recovery interaction.

A **Stakes Gate** is also proposed:

> Not every action needs a test. A test should occur where meaningful uncertainty and meaningful consequences exist.

Routine actions without meaningful stakes should not be turned into repetitive resource expenditure merely because a Skill exists.

Exact difficulty grades and Failure XP interaction remain unresolved.

---

# 9. S-9 / S-10 — Extended Tests

**Status: Proposed Universal Play Module**

Extended Tests are intended for:

- research;
- crafting;
- travel;
- environmental hazards;
- sieges;
- prolonged social work;
- rituals;
- technical projects;
- other multi-interval tasks.

## 9.1 Core principle

Every interval is an ordinary Tiwas test.

Therefore each interval preserves:

- Cost = Roll;
- Overflow → HP;
- Failure XP;
- failed Doubles;
- Advanced Skill creation;
- Recovery.

## 9.2 Progress

Candidate methods:

### Margin accumulation

Accumulate successful Quality/Margin values until a target is reached.

### Success count

Accumulate successful intervals until a target count is reached.

The final method is unresolved.

## 9.3 Failure behaviour

Candidates include:

- stall;
- progress loss;
- complication;
- conversion into another task state.

The current direction favours **stall as the default**, with progress loss potentially treated as an optional complication.

## 9.4 No Progress currency

Extended Test Progress must never become:

- spendable points;
- transferable currency;
- an XP substitute;
- a second advancement economy.

It is merely a running record of previous test outcomes.

---

# 10. Conditions

**Status: Reserved / Architectural Requirement**

Conditions should represent character/world state.

They must remain distinct from Tags.

Examples may include:

- Stunned;
- Prone;
- Impaired;
- Bleeding;
- Restrained.

Final condition definitions, stacking, durations and removal procedures remain unresolved.

---

# 11. Tags

**Status: Reserved / Architectural Requirement**

Tags are classification and permission metadata.

Potential consumers include:

- weapons;
- armour;
- Effects;
- locations;
- powers;
- creatures;
- settings.

Tags are not Conditions.

---

# 12. Time / Action Economy

**Status: Reserved / Architectural Requirement**

A unified temporal model is required for:

- combat rounds;
- turns;
- actions;
- reactions;
- movement;
- intervals;
- ongoing Effects;
- Conditions;
- Rest;
- Extended Tests.

The same temporal architecture should serve combat and non-combat activities.

---

# 13. Equipment

**Status: Reserved**

Required areas include:

- weapons;
- armour;
- equipment records;
- equipment Traits;
- Tags;
- encumbrance;
- carrying;
- equipment damage;
- repair/replacement;
- wealth/economy hooks.

Equipment should modify existing Universal Play systems rather than introduce a new resolution engine.

---

# 14. Environmental Hazards

**Status: Reserved / Architectural Direction**

Preferred structure:

```text
Trigger
  ↓
Existing Test
  ↓
Natural Cost
  ↓
Outcome
  ↓
Existing Effect / Condition / Harm
```

Hazards should not require hazard-specific currencies.

---

# 15. Magic and Special Abilities

**Status: Design Direction / Not Fully Defined**

Current direction is that magic and special abilities emerge through Advanced Skills.

A setting can grant permission for a Skill lineage to represent:

- magic;
- martial techniques;
- supernatural abilities;
- technology;
- psychic abilities;
- other special capabilities.

The current direction rejects a mandatory fixed spell-list system in the Core.

A setting may optionally add a spell curriculum.

## 15.1 Intended interaction

A magical or special ability should continue to use:

- the ordinary Skill test;
- Cost = Roll;
- MP or lineage-defined resource domain;
- Overflow;
- Failure XP;
- Advanced Skill creation;
- Quality;
- Effects.

This remains architectural direction rather than complete rules.

---

# 16. NPC Compression

**Status: Reserved / S-12**

NPCs should use compressed representations of the same underlying system rather than a separate NPC resolution engine.

Exact grades/packages remain unresolved.

---

# 17. Setting Modules

**Status: Design Direction**

The intended boundary is:

```text
Core
  ↓
Universal Play
  ↓
Setting Module
```

A setting may define:

- permissions;
- content;
- creatures;
- equipment;
- technologies;
- magic;
- setting-specific Tags;
- setting-specific Effects.

A setting must not redefine the Core invariants.

---

# 18. Design Direction Summary

Current architectural direction:

```text
TIWAS CORE
├── d100 roll-under
├── 100-Fumble
├── Cost = Roll
├── Overflow → HP
├── Failure XP
├── Skill Roll Pool
├── Advanced Skills
└── Core Recovery

UNIVERSAL PLAY
├── Opposed Contests
├── Difficulty / Stakes
├── Effects
├── Extended Tests
├── Time
├── Conditions
├── Tags
├── Harm / Wounds
├── Locations
├── Armor
├── Defense
├── Equipment
├── Hazards
├── Rest / Healing
└── NPC procedures

SETTING MODULES
├── Fantasy
├── Science Fiction
├── Modern
├── Horror
├── Historical
└── Cinematic
```

---

# 19. Explicitly Experimental Material

## S-1D — Committed / Guarded Stance

**Status: Experimental — excluded from canonical S-1**

This earlier tactical overlay must not be confused with Hybrid Committed.

It is retained only as historical design material.

No current Tiwas subsystem depends on it.

---

# 20. Open Residual Decision Register

| ID | Decision | Current status |
|---|---|---|
| S-2 | Broader hit-location architecture: tier policy, mapping and downstream interaction | Partially locked / WIP |
| S-3 | Effect thresholds/purchasing | Open |
| S-4 | Wound activation/severity | Open |
| S-5 | Armor interaction | Open |
| S-6 | Defense model | Open |
| S-7 | Incapacitation/death | Open |
| S-8 | Difficulty/task/stakes | Open |
| S-9 | Extended Test progress | Open |
| S-10 | Extended Test failure loss | Open |
| S-11 | Rest/healing timelines | Open |
| S-12 | NPC compression | Open |

No row in this register is a canonical rule.

---

# 21. Promotion Rule

A proposal may become canonical only after:

1. its design question is explicitly identified;
2. competing alternatives have been considered where appropriate;
3. relevant simulation/analysis has been completed;
4. the human designer has accepted the ruling;
5. the mechanic is documented as a formal rule;
6. the Canonical Rules & Changelog document is updated;
7. the former proposal is marked Superseded or Locked here;
8. implementation documentation is updated.

A detailed proposal is not a rule merely because it is detailed.
