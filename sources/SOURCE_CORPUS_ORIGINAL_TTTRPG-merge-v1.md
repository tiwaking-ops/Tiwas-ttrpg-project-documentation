# Files

## Tiwas TTRPG — Canonical Rules & Changelog-v1-3.md

```markdown
# Tiwas — Canonical Rules & Changelog

**Document Version:** v1.3  
**Document Status:** Canonical Source of Truth  
**Document Role:** Authoritative statement of the current Tiwas ruleset  
**Supersedes:** Canonical Rules & Changelog v1.2 and previous standalone Core Rules and locked subsystem documents for any material incorporated here  
**Historical material:** Preserved in compressed changelog form  
**Rule status vocabulary:** `Canonical / Locked`, `Reserved`, `Historical / Superseded`

---

## 0. Authority and Governance

This document is the authoritative source for Tiwas mechanics that have been formally locked.

Future Tiwas documentation must not contradict this document without an explicit rules-governance decision.

A mechanic appearing here is **Canonical / Locked** unless explicitly identified as Reserved.

### 0.1 Authority hierarchy

Within the consolidated Tiwas documentation:

1. **Canonical Rules & Changelog** — current locked mechanics.
2. **Proposals, WIP & Design Direction** — unresolved and experimental design material.
3. **Implementation Roadmap & Project Governance** — implementation sequencing and project-management guidance.

The latter two documents cannot override this document.

### 0.2 Locked does not mean permanently immutable

"Locked" means:

> The mechanic is part of the current Tiwas ruleset and must be treated as authoritative by downstream design and implementation.

A locked mechanic may be reopened only through normal Tiwas design governance, normally because new simulation evidence, playtesting, conversion work, or another substantive design finding demonstrates a problem.

A proposal, recommendation, implementation convenience, or LLM preference does not by itself reopen a locked rule.

---

# 1. Tiwas Core Identity

Tiwas is a high-consequence percentile universal RPG in which:

- every meaningful attempt uses the common resolution engine;
- every test costs resources;
- failure generates mechanical growth;
- meaningful success changes the tactical or narrative state.

The system's locked design priorities are:

1. **Granular physical simulation where the situation warrants it.**
2. **Heroic resilience / low permanent character loss rate.**
3. **Minimum resolution steps per exchange without sacrificing Priority 1.**

---

# 2. Core Dice and Resolution

## 2.1 d100

A Tiwas d100 produces an integer from **1–100**.

Physical percentile dice displaying `00` represent **100**, never zero.

## 2.2 Roll-under

A skill test succeeds when:

`Roll <= Skill`

unless the 100-Fumble rule applies.

## 2.3 100-Fumble

A roll of **100 always fails**, regardless of Skill value.

A roll of 100 is also always treated as a qualifying Double.

Therefore no Skill value produces literal 100% test reliability.

## 2.4 Doubles

The canonical Double values are:

`11, 22, 33, 44, 55, 66, 77, 88, 99, 100`

A Double produces its special Advanced Skill effect only when the roll is also a Failure.

The nine digit-doubles qualify when the Double exceeds the tested Skill.

100 always qualifies because 100 is always a Failure.

## 2.5 Rounding

All fractional calculations use floor rounding.

There are no general exceptions to this rule.

---

# 3. The 24-Attribute Matrix

Characters possess 24 independently generated attributes.

Each attribute is generated as:

`1d100`

The attributes are divided into twelve Body attributes and twelve Mind attributes.

| Code | Animal | Category | Tier-1 Skill |
|---|---|---|---|
| bpp | Bear | Body / Power / Power | Might |
| bps | Tiger | Body / Power / Speed | Impact |
| bpe | Elephant | Body / Power / Endurance | Brawn |
| bpx | Dragon | Body / Power / Social | Presence |
| bsp | Hawk | Body / Speed / Power | Agility |
| bss | Rat | Body / Speed / Speed | Reflexes |
| bse | Horse | Body / Speed / Endurance | Quickness |
| bsx | Monkey | Body / Speed / Social | Grace |
| bep | Badger | Body / Endurance / Power | Toughness |
| bes | Wolf | Body / Endurance / Speed | Stamina |
| bee | Ox | Body / Endurance / Endurance | Vitality |
| bex | Dog | Body / Endurance / Social | Poise |
| mpp | Stag | Mind / Power / Power | Cunning |
| mps | Snake | Mind / Power / Speed | Wits |
| mpe | Rooster | Mind / Power / Endurance | Willpower |
| mpx | Fox | Mind / Power / Social | Glamour |
| msp | Bat | Mind / Speed / Power | Acuity |
| mss | Cat | Mind / Speed / Speed | Perception |
| mse | Rabbit | Mind / Speed / Endurance | Alacrity |
| msx | Otter | Mind / Speed / Social | Charm |
| mep | Crane | Mind / Endurance / Power | Focus |
| mes | Goat | Mind / Endurance / Speed | Discipline |
| mee | Owl | Mind / Endurance / Endurance | Resolve |
| mex | Pig | Mind / Endurance / Social | Composure |

An attribute belongs permanently to either Body or Mind.

---

# 4. Derived Statistics

Derived statistics are live calculations.

Changing an attribute immediately changes every derived statistic and Skill Cap that depends upon it.

| Statistic | Formula |
|---|---|
| Health Points (HP) | Sum of all 12 Body attributes |
| Mental Points (MP) | Sum of all 12 Mind attributes |
| Physical Energy | bep + bes + bee |
| Speed | bsp + bss + bse |
| Energy Regen | bep + bes |
| MP Regen | mep + mes |
| Movement Speed | floor((bsp + bss) / 15) |

MP is simultaneously the Mind resource pool and the total derived from the twelve Mind attributes. This identity is intentional.

---

# 5. Skills

## 5.1 Skill Tier

A Skill's Tier is the number of **distinct attributes** used in its Cap formula.

A Tier-1 Skill uses one attribute.

A Tier-T Skill uses T attributes.

No attribute may appear more than once within a Skill formula.

The theoretical maximum Tier is therefore 24.

## 5.2 Skill Cap

`Cap = floor((A1 + A2 + ... + AT) / T)`

The Cap is the floored average of the underlying attributes.

Increasing Tier does not inherently increase expected Cap; it averages additional attributes and reduces variance.

## 5.3 Starting Skill

A normal Skill begins at:

`Starting Value = floor(Cap / 2)`

A Skill may therefore legitimately begin at 0.

---

# 6. Canonical Test Transaction

Every Skill test follows this order:

1. Roll 1d100.
2. Determine the Skill's resource domain.
3. Determine Success or Failure.
4. Pay Cost equal to the natural roll.
5. Apply Overflow if the resource pool cannot pay the full cost.
6. Resolve Failure XP.
7. Resolve qualifying failed Double / Advanced Skill effects.
8. Recover the appropriate resource.
9. End the test.

No Universal Play subsystem may replace this transaction with an alternative resolution engine.

---

# 7. Resource Cost and Overflow

Every test costs the exact number rolled.

### Body Skill

Cost is paid from Physical Energy.

### Mind Skill

Cost is paid from MP.

If the available resource is insufficient:

`Overflow = Cost - Remaining Resource`

The resource pool falls to zero and the Overflow becomes direct HP damage.

Overflow does not create a second resource pool.

---

# 8. Recovery

Recovery occurs **after every test** and is always the final stage.

The recovered amount is:

`floor(Regen / 2)`

Recovery applies to the resource pool just spent and is clamped at that pool's maximum.

Recovery occurs regardless of:

- success;
- failure;
- Overflow;
- failed Double;
- Advanced Skill creation.

A full Rest action remains Reserved and is not defined by the Core.

---

# 9. Failure XP

Failure XP is:

`max(0, Roll - Skill)`

The clamp prevents negative XP when the 100-Fumble forces a failure against Skill 100 or higher.

---

# 10. Skill Roll Pool

Failure XP first enters a temporary Skill Roll Pool.

The pool exists only for the current failed test.

It does not persist between tests.

Within the failed test:

```text
while Pool >= Current Skill
and Current Skill < Cap:

    Pool -= Current Skill
    Skill += 1
```

The process stops when:

- the remaining pool cannot afford another increase; or
- the Skill reaches its Cap.

Any remaining pool becomes General XP.

## 10.1 Skill at 0

If a Skill is 0, the cost of increasing it to 1 is zero.

Therefore a failed test with nonzero Failure XP raises a Skill-0 to at least 1 immediately.

This is intentional.

---

# 11. General XP

General XP receives:

- Skill Roll Pool remainder;
- GM/quest/adventure awards.

General XP may increase:

- Attributes;
- Skills.

The cost of increasing a value by 1 is its current value.

General XP must cover the entire cost of an increase.

Partial advancement is not permitted.

## 11.1 Above-Cap advancement

General XP may raise a Skill above its current Cap.

Skill Roll Pool advancement may not.

## 11.2 Advancement ceiling

The initial 1–100 range applies to attribute generation.

Advancement has no fixed upper bound.

Skills above 100 remain subject to the mandatory 100-Fumble.

---

# 12. Advanced Skills

A qualifying failed Double immediately creates an Advanced Skill.

## 12.1 Creation

1. New Skill Tier = failed Skill Tier + 1.
2. Add one attribute not already present in the failed Skill formula.
3. Recalculate the new Cap from the complete attribute set.
4. Choose either:
   - starting value 1; or
   - roll 1d100 and use `min(Roll, New Cap)`.

## 12.2 Duplicate restrictions

An attribute cannot appear twice within a single Skill formula.

The same Advanced Skill — defined by the same base Skill and added attribute — cannot be created twice.

## 12.3 Resource domain

An Advanced Skill retains the resource domain of its original Tier-1 lineage.

A Body-rooted lineage remains Physical Energy based even if later attributes include Mind attributes.

A Mind-rooted lineage remains MP based even if later attributes include Body attributes.

## 12.4 Advancement depth

Advanced Skills may themselves generate further Advanced Skills.

There is no arbitrary Tier ceiling beyond the natural 24-attribute limit.

---

# 13. Universal Opposed Contest — S-1

**Status: Canonical / Locked**

S-1 is the universal opposed-contest primitive.

Each participant performs an ordinary Core Test independently.

The contest layer does not alter the underlying test.

## 13.1 Outcome matrix

| Participant A | Participant B | Result |
|---|---|---|
| Success | Failure | A wins |
| Failure | Success | B wins |
| Success | Success | Compare Quality |
| Failure | Failure | Repeat contest |

Each participant pays their own natural roll cost and resolves their own Failure XP, Double eligibility and Recovery.

## 13.2 Quality measures

The Quality measure is selected by contest type.

| Mode | Formula | Primary identity |
|---|---|---|
| Margin | `Skill - Roll` | Efficiency / precision |
| Blackjack | `Roll` | Commitment / force |
| Hybrid Committed | `Roll + max(0, Skill - 99)` | Commitment with continued high-Skill scaling |

Quality only compares already-rolled successful tests.

It never modifies:

- the historical roll;
- Cost;
- Failure XP;
- Double eligibility;
- Recovery.

## 13.3 Quality selection

Current guidance:

| Situation | Default |
|---|---|
| Precision / efficiency | Margin |
| Force / commitment | Blackjack |
| Mixed / uncertain | Hybrid |

Blackjack and Hybrid's distinctive identity becomes meaningful primarily once relevant Skills are sufficiently high. At low Skill, the success/failure gate dominates.

The GM may override situational guidance where the fiction demands another Quality measure.

## 13.4 Failure/Failure

Both participants repeat the contest.

Both tests have already incurred all normal Core consequences before the repeat occurs.

## 13.5 Exact Quality tie

An exact Quality tie causes the contest to repeat.

The repeat is a fresh contest round.

## 13.6 S-1 validation

S-1 has been validated through simulation across Skill 10–250 and Skill gaps up to 151.

The empirical validation and designer rulings are retained as historical design evidence rather than treated as mathematical rules themselves.

---

# 14. S-2 — Tier-1 Location Index Provider

**Status: Canonical / Locked — limited S-2 decision**

This section locks only the Tier-1 Location Index provider. It does not complete the broader hit-location subsystem.

## 14.1 Zero-Step

When a rule calls for a Tier-1 Location Index, use **Zero-Step**.

Zero-Step derives the Location Index by exchanging the tens and units digits of the attacker's natural d100 roll. Interpret `00` as `100` under the normal d100 rule after the exchange.

Examples:

| Natural d100 roll | Zero-Step Location Index |
|---:|---:|
| 37 | 73 |
| 10 | 1 |
| 1 | 10 |
| 100 (`00`) | 100 (`00`) |

For physical percentile dice, exchange the displayed tens and units digits. For another rolling method, express the natural roll as its two percentile digits before exchanging them.

## 14.2 Determinism and player choice

Zero-Step is deterministic. The attacker does not choose between the natural roll and the transformed result.

The natural roll remains authoritative for every Core Test consequence, including outcome, Cost, Overflow, Failure XP, failed-Double eligibility, Advanced Skill effects and Recovery. The transformed result is used only as the Tier-1 Location Index.

## 14.3 Scope retained for later S-2 work

The following are not established by this ruling:

- whether and when a scene uses Tier 0, Tier 1 or Tier 2 location granularity;
- Tier-0 and Tier-2 procedures;
- anatomical mapping from a Location Index to a zone;
- wound, armour, defence and Outcome Effect interaction;
- whether any later rule may select, modify or consume a Location Index.

These matters remain non-canonical until separately resolved through governance.

## 14.4 Future optional-rule observations

Playtest participants suggested choosing between the natural and swapped values. That suggestion is not part of the basic rule and creates no player choice in current Tiwas.

The designer may later consider, in an optional-rule appendix only:

- an attacker choice granted by an explicit special ability; and
- a defender choice.

Neither observation is a current rule, a permission, or a design commitment.

## 14.5 E9 human usability playtest record

**Evidence class: Empirical finding — passed for the tested physical two-d10 method only.**

The E9 usability playtest used two physical d10s and 50 participants: 25 participants new to RPGs and 25 RPG players new to Tiwas. Participants reported no difficulty rolling the dice or exchanging the digits for hit location, and feedback was positive.

This evidence supports usability of Zero-Step for that tested physical two-d10 method. Other input methods, including a single d100, a digital roller, and a verbally announced result, were not tested and are not covered by this finding. E9 supports the designer ruling but does not resolve the remaining S-2 architecture.

## 14.6 Comparative derivation-cost residual

Separate from E9, the completed comparative analysis found that Units-Digit requires 0–1 additional derivation operations across the examined rolling modes, while Zero-Step requires 1–2. This is a comparative structural observation about derivation steps, not a human-usability finding and not an additional E9 status.

The completed physical two-d10 playtest establishes usability only for its tested method. Any relative cost or usability conclusion for other input methods remains outside that playtest's evidence.

---

# 15. Reserved Systems

The following remain outside the locked Core unless separately incorporated into this document through formal governance:

- hit-location rules, except the Tier-1 Zero-Step Location Index provider in Section 14;
- wound activation/severity;
- Outcome Effects;
- armor;
- active/passive defense;
- incapacitation;
- death;
- healing;
- Rest;
- equipment;
- encumbrance;
- conditions;
- environmental hazards;
- difficulty grades;
- task/stakes adjudication;
- Extended Tests;
- NPC construction;
- magic/special-ability implementation;
- GM procedure;
- campaign procedures;
- setting-specific content.

Where a separate Universal Play subsystem has already been locked, such as S-1, its current rules supersede the older "Reserved" classification.

---

# 16. Core Architectural Invariants

Every future Tiwas subsystem must preserve:

1. d100 produces 1–100.
2. 100 always fails.
3. 100 is a qualifying failed Double.
4. All fractions floor.
5. Success is roll-under.
6. Cost equals the natural roll.
7. Overflow becomes HP damage.
8. Failure XP uses `max(0, Roll - Skill)`.
9. Skill Roll Pool is temporary.
10. Skill Roll Pool advancement cannot exceed Cap.
11. General XP can exceed Cap.
12. Failed Doubles can create Advanced Skills.
13. Advanced Skill Caps are recalculated from the full attribute set.
14. Advanced Skill resource domain follows lineage.
15. Derived statistics are live.
16. Recovery occurs last.
17. No Universal Play subsystem may introduce a competing primary resource or progression economy.
18. Universal Play modules must build on the Core Test Transaction rather than replace it.

---

# 17. Changelog

## Core v1 → Core v2

The following ambiguities were formally closed in Core Rules v2:

1. d100 range and interpretation of `00`.
2. Complete Double list.
3. Tier ≥2 Cap calculation.
4. Advanced Skill Cap recomputation.
5. Skill Roll Pool persistence.
6. Cascading advancement.
7. Skill-0 advancement.
8. Fractional recovery rounding.
9. Recovery timing and clamping.
10. Advanced Skill creation timing.
11. Duplicate attributes.
12. Duplicate Advanced Skills.
13. Mixed-domain Advanced Skill resource type.
14. Maximum Tier.
15. Removal of a separate Cap-purchase mechanic.
16. General XP above Cap.
17. Advancement upper bound.
18. Guaranteed success at high Skill.
19. Status of undeveloped subsystems.

## S-1 v1 → v1.1

The locked S-1 closure pass:

1. Clarified wording around Skills above 99.
2. Extended validation of the cost-asymmetry identity through Skill 250.
3. Added the canonical quick-reference procedure.
4. Locked exact Quality ties as Repeat.
5. Locked Failure/Failure as Repeat.
6. Confirmed the Skill-gating caveat for Blackjack and Hybrid.
7. Kept the S-1D stance experiment explicitly outside canonical S-1.

## S-2 v1.1 → v1.2

1. Locked Zero-Step as the Tier-1 Location Index provider.
2. Locked Zero-Step as deterministic: players do not choose between the natural and transformed results.
3. Confirmed that Zero-Step is a read-only post-process and does not alter any Core Test consequence.
4. Recorded the E9 human usability playtest as supporting empirical evidence.
5. Retained the broader S-2 architecture, including tier policy and anatomical mapping, as unresolved.
6. Recorded attacker special-ability choice and defender choice only as future optional-rule observations.

## S-2 documentation reconciliation v1.3

1. Clarified that the completed E9 playtest passes only for the tested physical two-d10 method.
2. Explicitly recorded that single-d100, digital, and verbally announced input methods remain untested.
3. Separated the comparative derivation-cost residual from E9 so that structural comparison and human evidence do not receive conflicting labels.
4. Preserved Zero-Step as the deterministic canonical Tier-1 provider; preserved the broader S-2 architecture as unresolved.

## Consolidation change

The former Core statement that opposed tests were Reserved is now historical because S-1 formally closes that subsystem.

The original Tiwas v1 documentation remains historical and superseded by Core Rules v2.

```

## Tiwas___Implementation_Roadmap___Project_Governance-v1_4_3.md

```markdown
# Tiwas — Implementation Roadmap & Project Governance

**Document Version:** v1.4.3
**Document Status:** Authoritative Project/Implementation Guidance
**Rule Authority:** None — this document does not create game mechanics
**Supersedes:** Implementation Roadmap & Project Governance v1.4.2 (Phase 2 / §9 and the S-2 row of §4 only; all other content carried forward unchanged)
**Purpose:** Define dependencies, implementation sequencing, simulation gates, regression requirements and governance for completing Tiwas
**Important:** Implementation guidance must never be mistaken for a design ruling.

**Change note (v1.4.3):** Phase 2 (§9) and §4's S-2 row updated to record the designer ruling closing the S-2 Non-Attack Location Index Source investigation: non-attack physical resolutions generate no Tier-1 Location Index until S-4, S-7, or S-8 explicitly reopens the question. Implementation guidance only, non-canonical; the underlying ruling is recorded in Proposals/WIP v1.4.3 §2.5A. See that section for the full investigation and revision record.

---

# 0. Purpose

This document governs how the Tiwas ruleset progresses from its current locked Core and S-1 state toward a complete universal RPG system.

It exists separately from the rules so that:

- project sequencing does not become game law;
- candidate mechanics can be implemented without being declared final;
- future LLM sessions have a stable development process;
- regression requirements remain visible; and
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

The Roadmap may explain what should be implemented, what depends on what, what should be simulated, and what acceptance tests should exist. It may not independently decide numerical thresholds, final Quality rules, wound severity, death triggers, armour mechanics, defence costs, Extended Test progress, or other unresolved designer decisions.

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
- unconditional final recovery; and
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

| Priority | ID | Decision | Current status | Decision dependency |
|---:|---|---|---|---|
| 1 | S-1 | Opposed Quality | **Locked** | Core |
| 2 | S-2 | Hit-location architecture | **Tier-1 provider: Locked (Zero-Step). Attack-side invocation/warrant policy: Candidate accepted, non-canonical (S-2 Design Investigation v1–v5). Non-attack Location Index generation: RULED — deferred, none generated until S-4/S-7/S-8 reopens the question. Tier policy (which tier a scene/campaign uses), anatomical mapping, and Tier 2 procedure: all still fully Open.** | S-1 |
| 3 | S-3 | Outcome Effects | Open | S-1 |
| 4 | S-4 | Wound activation/severity | Open — **also a reopening trigger for the S-2 non-attack deferral** | S-2 and S-3 |
| 5 | S-5 | Armor | Open | S-3 and S-4 |
| 6 | S-6 | Defense | Open | S-1 |
| 7 | S-7 | Incapacitation/death | Open — **also a reopening trigger for the S-2 non-attack deferral** | S-4 |
| 8 | S-8 | Difficulty/task adjudication | Open — **flagged as the most likely reopening trigger for the S-2 non-attack deferral** | Core |
| 9 | S-9 | Extended Test progress | Open | S-1 |
| 10 | S-10 | Extended Test failure loss | Open | S-9 |
| 11 | S-11 | Rest/healing | Open | S-4 and S-7 |
| 12 | S-12 | NPC compression | Open | Preceding systems |

These are **decision dependencies**, not a mandatory calendar or implementation order. S-2 and S-3 are parallel workstreams after S-1; their respective unresolved decisions converge at S-4. The Roadmap must always reflect current status rather than preserve obsolete labels.

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

**Note (v1.4.3):** U-16 (Hazards) does not currently produce Location Provider (U-09) output for any non-attack resolution, per the S-2 non-attack deferral. This is an implementation consequence of the ruling, not an independent architectural decision — U-16's own design is otherwise unaffected.

---

# 6. Dependency Architecture and Implementation Sequencing

## 6.1 Decision architecture

```text
LOCKED CORE
    ↓
CORE TEST TRANSACTION
    ↓
S-1 / OPPOSED CONTEST
    ↓
    ┌────────────────────────┐
    ▼                        ▼
S-2 / HIT LOCATIONS     S-3 / OUTCOME EFFECTS
    │                        │
    └───────────┬────────────┘
                ▼
     S-4 / WOUNDS + TWO-TRACK HARM
                ↓
        S-5 / ARMOR and S-6 / DEFENSE
                ↓
    TIME / ACTION, CONDITIONS, TAGS, EQUIPMENT
                ↓
  S-7 / INCAPACITATION + DEATH; S-8 / ADJUDICATION
                ↓
         S-9 / S-10 EXTENDED TESTS
                ↓
     S-11 / REST + HEALING; POWERS; S-12 / NPCs
                ↓
         SETTING INTERFACE → FULL INTEGRATION
```

S-2 is not a prerequisite for the general S-3 Effect design, and S-3 is not a prerequisite for the general S-2 architecture. A location-selecting Effect may consume a location-provider interface, but that local interface dependency does not make either whole workstream sequential.

## 6.2 Implementation sequencing

Implementation may sequence, interleave, or prototype parts of S-2, S-3, and their interfaces according to practical need. A useful sequence is: establish the interface contracts; implement non-location-dependent Effects; implement the location provider and tier policy; then integrate the location-dependent Effects and test the combined harm path.

Interface prototypes between S-3 and S-4 are permitted and encouraged where they expose requirements. They are not a ruling on S-4 wound activation, severity, disability, death, or other unresolved S-4 design. Prototype values and behaviours remain WIP unless separately accepted through the governance process.

Cross-cutting dependencies:

- Time is required for durations, Rest, and ongoing Effects.
- Conditions and Tags support Effects, wounds, equipment, and powers.
- NPC compression depends on the completed state model.
- Setting modules must consume the completed Universal Play layer.

---

# 7. Phase 0 — Regression Harness

Before extending the system, establish deterministic regression tests for the Core.

Required cases: successful low and high rolls; ordinary failure; 100-Fumble; failed Double; sufficient, insufficient, and zero resource; Skill 0, at Cap, above Cap, and above 100; Advanced Skill creation and Cap recomputation; mixed-domain Advanced Skill; live derived-stat changes; and final recovery.

> **Acceptance criterion:** No Universal Play implementation may bypass the Core regression suite.

---

# 8. Phase 1 — S-1 Opposed Contest

**Status: Complete / Locked**

S-1 has completed validation and acceptance. Its implementation requires two independent Core Tests; the success/failure matrix; selectable Quality; Margin; Blackjack; Hybrid Committed; Failure/Failure Repeat; exact Quality-tie Repeat; and no second resource pool. The natural roll remains authoritative for Cost and all Core consequences.

No further S-1 development is planned unless new evidence triggers formal reopening.

---

# 9. Phase 2 — S-2 Hit Locations

**Status: Tier-1 provider locked (Zero-Step, evidence-backed) / Attack-side invocation policy: candidate accepted, non-canonical / Non-attack Location Index generation: RULED — deferred / Tier 0/2 policy and broader architecture: WIP**

Unchanged: the Tier-1 Location Index provider (Zero-Step) remains complete and locked as previously documented.

**Invocation/Warrant Policy — Attack-Side (Candidate, Non-Canonical):**

The S-2 Design Investigation (v1–v5) produced a candidate policy for when a Location Index is generated at all, summarized in Proposals/WIP §2.1A. Implementation-relevant summary:

- Location Index generation requires an explicitly stated, distinct outcome beyond ordinary damage, whose location-dependence is already established under current design (not merely anticipated), and which current rules can resolve.
- A four-state internal classification (Established & Resolvable / Established, Not Yet Resolvable / Outcome Plausible but Location-Dependence Unresolved / No Distinct Consequence) underlies this test but is not intended as a GM-facing procedure — implementation should expose the single collapsed question, not the four states, at the point of play.
- A W3 reference cache exists as a maintained shorthand, not an independent authorization source; implementation should ensure novel/uncached cases still route through the underlying test rather than defaulting to "no" for lack of a cache entry.
- **Confirmed procedural rules to implement (empirical finding, replicated across independent trial rounds):** disjunctive compound-objective evaluation; stale-objective invalidation (re-check the fictional state against the category's rationale at time of use, not just at declaration); S-1 winner-only Location Index eligibility.
- **Additional procedural rule to implement, different evidence class** *(design inference, provisionally adopted — not separately stress-tested at the table, unlike the three rules above)*: lazy evaluation. Location Index may be derived at the point a downstream stage needs it, not mandatorily at declaration time, since Zero-Step only needs the already-recorded natural roll. The reasoning is sound architecturally (Zero-Step is a read-only post-process of an already-recorded roll), but implementation should not treat this rule as carrying the same confidence as the three replicated rules above.

**Non-Attack Location Index Source — Designer Ruling (New in v1.4.3, Non-Canonical Governing Position):**

A follow-on investigation (S-2 Non-Attack Location Index Source, starter brief v1.1) examined whether, and whose, natural roll supplies a Location Index for non-attack physical resolutions (falls, hazards, structural collapses with no adversarial "attacker"). The investigation produced a provenance-only candidate rule (H0: derive from an existing governing Core Test's natural roll, or generate no index if none exists) plus two riders, but the invocation/warrant question for non-attack cases was resolved separately by explicit designer ruling before the provenance candidate was promoted to an operative rule:

> **Non-attack physical resolutions generate no Tier-1 Location Index under current design, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution.**

Implementation-relevant consequences:

- Any hazard/fall/collapse resolution path — including one that already routes through an ordinary Core Test (e.g., a Reflexes test to dodge, an Agility test to catch a ledge) — must not call the Location Provider (U-09). This is a categorical exclusion, not conditional on GM narration or declared stakes.
- The H0 provenance candidate (governing-Core-Test-roll-or-none) and its two riders (no cross-character roll sharing; tie-break for multi-test causal chains) remain documented as an inert candidate design for future reference, but must not be implemented as active logic. Implementing H0 now would generate Location Index output the ruling explicitly forbids.
- This deferral is explicitly tied to reopening triggers, not a permanent exclusion: revisit when S-4 (Wound activation/severity), S-7 (Incapacitation/death), or S-8 (Difficulty/Stakes Gate) reaches a design stage that makes hazard-location relevant. S-8 is flagged as the most likely natural trigger. Implementation should not pre-build hazard-location hooks in anticipation of this — per Roadmap §24 Rule 6, do not silently resolve an open designer fork, and this fork (whether/how non-attack location eventually works) is explicitly still open, just not currently active.

**Acceptance tests:**

- Zero-Step exchanges the percentile digits, including `00`/100 handling.
- Tier 1 requires no mandatory additional die.
- Zero-Step has no player-choice branch.
- Tier selection and Location Index derivation never alter the original roll or Core Test consequences.
- Tier 0 creates no location state.
- Location data can be consumed by later Effects/Wound/Armor systems without becoming an alternate Core resolution engine.
- The Named-Outcome Test correctly separates bare location narration from stated distinct consequences (attack-side only).
- Conditional phrasing does not defeat definiteness of a stated objective (attack-side only).
- Compound objectives are evaluated disjunctively (attack-side only).
- A stale objective (fictional state no longer supports the category) voids an otherwise-matching case (attack-side only).
- Only the S-1 contest winner's natural roll is eligible for Location Index generation.
- No currently-State-3 concept (Disarm, Equipment Damage, Function Impairment, Armor Bypass, Incapacitation) generates a Location Index under the current candidate policy, regardless of declaration frequency or plausibility, until a future subsystem (S-3/S-5/S-7/S-10) makes an explicit design choice that location is the delivery mechanism for that outcome — not merely until that subsystem locks in any form.
- Novel, uncached structural cases resolve correctly via the underlying test rather than requiring literal cache membership.
- **New (v1.4.3): no non-attack physical resolution (hazard, fall, structural collapse) generates a Location Index under any circumstance, including where a governing Core Test exists and/or the GM states a specific consequence in advance.**

E9 usability evidence is complete **for the tested physical two-d10 method only**: 50 participants (25 new to RPGs and 25 RPG players new to Tiwas) reported no difficulty with rolling or digit exchange and gave positive feedback. A single d100, digital roller, verbally announced result, and other input methods remain untested; do not treat E9 as evidence for them.

The comparative derivation-cost residual is recorded separately from E9: across the examined rolling modes, Units-Digit required 0–1 additional derivation operations and Zero-Step required 1–2. This is a structural comparison, not a second E9 result or a substitute for input-method-specific usability testing.

**Remaining implementation and design work:**

- Tier 0 and Tier-2 interface — open.
- Scene/campaign tier policy — **partially informed by the candidate invocation policy, but still open.** The candidate policy determines when a location result is warranted for a given resolution; it does not determine whether a scene or campaign uses Tier 0, Tier 1, or Tier 2 in the first place. That selection question remains unresolved and is not narrowed to "Tier 2 only" by this policy.
- Anatomical mapping from Location Index to zone — open, untouched. Structural Weak Points is classified **State 2** (Established, Not Yet Resolvable), precisely because this mapping doesn't exist yet: location-dependence is anchored, but no Location Index currently generates for this category in play until the mapping is built.
- Downstream interfaces for Effects, Wounds, Armor, and Defence — open; directly informed by the investigation's State-3 findings, which flag that Disarm, Equipment Damage, Function Impairment, Armor Bypass, and Incapacitation are not currently anchored to location as a mechanism, and that S-3/S-5/S-7/S-10 each contain at least one plausible design path (Margin/Tag-gated triggering) that would not require location at all. Future subsystem design work should treat this as an open fork, not a settled assumption in either direction.
- **Non-attack Location Index source — RESOLVED AS A DEFERRAL (v1.4.3).** No longer an open implementation question in the "undecided mechanism" sense; the mechanism question (H0 and riders) is on record but inactive, and the category is categorically off until S-4/S-7/S-8 reopens it.

The broader tier policy, anatomical mapping, and downstream interaction remain open and require their own design and validation gates. Do not treat the completed Tier-1 provider decision, the candidate invocation policy, or the non-attack deferral ruling as closure of S-2 as a whole.

---

# 10. Phase 3 — S-3 Outcome Effects and S-3/S-4 Interface Prototyping

**S-3 status: Open. S-4 status: Open.**

Implement the structural Effect interface first. Candidate Effects include Injury; Condition; Disarm / Break Hold; Movement / Position; Tempo; Guard Break; Bleed / Drain; Retreat / Yield; Equipment Damage; and Location selection.

S-3 work may prototype how an Effect passes harm or state information to a prospective S-4 Wound Engine. Such a prototype is an architectural exercise, not a lock on S-4. In particular, it must not silently establish wound severity thresholds, activation triggers, disability effects, or death checks.

The prospective two-track harm interface is:

```text
Track A                         Track B
PE / MP                         Location
   ↓                               ↓
Overflow                        Wound
   ↓                               ↓
Global HP                       Condition / Disability / Death Check
```

Acceptance criteria:

- Effects create real state changes.
- Effects do not alter historical rolls.
- Empty PE/MP is not automatic defeat.
- Overflow remains HP damage.
- HP = 0 is not automatically death.
- Wounds are not a second HP pool.

Simulation gate: measure Effect frequency, exchange length, resource expenditure, wound frequency, severe injury, and state-change density. Do not lock numerical thresholds without required evidence and a designer ruling.

---

# 11. Phase 4 — Armor and Defense

## 11.1 Armor

Implement Armor Traits and Tags, Bypass and Sunder interfaces, location interaction, and equipment damage. Compare candidates for bookkeeping, tactical value, simulation fidelity, and resolution steps.

## 11.2 Defense

Implement passive and active defense interfaces, defense as a normal contest participant, resource interaction, and timing. Compare candidates for PE/MP drain, number of rolls, survivability, tactical decision density, and resolution steps.

No candidate should be promoted to Canonical merely because it is convenient to implement.

---

# 12. Phase 5 — Incapacitation and Death

Implement HP-zero state, incapacitation, stabilization, survival, permanent injury, death, and recovery from incapacitation.

> **Simulation target:** Preserve heroic resilience while retaining meaningful physical consequences.

The permanent character-loss rate must be measured. No proposed death threshold becomes Canonical until the decision gate is passed.

**Note (v1.4.3):** this phase is one of the two subsystems flagged as a reopening trigger for the S-2 non-attack Location Index deferral (Proposals/WIP §2.5A). When incapacitation/death design work reaches a stage where hazard severity plausibly needs location-level resolution, that should be raised as an explicit reopening of the S-2 non-attack question, not silently assumed.

---

# 13. Phase 6 — Difficulty and Task Adjudication

Implement difficulty grades, Skill-side modification, Stakes Gate, meaningful-uncertainty test, Skill selection, and opposed/unopposed selection. Verify interaction with Cost, Failure XP, 100-Fumble, Doubles, and Advanced Skills. Difficulty must not alter the natural die face.

**Note (v1.4.3):** this phase (specifically the Stakes Gate) is flagged as the **most likely** reopening trigger for the S-2 non-attack Location Index deferral (Proposals/WIP §2.5A). When Stakes Gate design work reaches a stage where hazard-stakes framing is formally defined, that should be raised as an explicit reopening of the S-2 non-attack question, not silently assumed or folded in as a side effect of Stakes Gate's own design.

---

# 14. Phase 7 — Extended Tests

Implement Extended Tests as repeated ordinary Tiwas tests. Each interval preserves Cost = Roll, Overflow → HP, Failure XP, failed Doubles, Advanced Skills, and Recovery.

Candidate progress models are Margin accumulation and Success count. Candidate failure models are stall, progress loss, and complication. Compare task completion time, resource depletion, failure frequency, growth, Overflow, and Advanced Skill generation. Progress must never become a second currency.

---

# 15. Phase 8 — Cross-Cutting Architecture

Define Time (rounds, turns, actions, reactions, movement, intervals, ongoing timing); Conditions (application, stacking, duration, removal, interaction); Tags (weapon, armour, Effect, location, power, creature, setting); and Equipment (records, Traits, damage, carrying, encumbrance, repair/replacement).

Hazards use:

```text
Trigger
→ Existing Test
→ Cost
→ Outcome
→ Existing Effect / Condition / Harm
```

No subsystem-specific currency should be created.

**Note (v1.4.3):** per the S-2 non-attack deferral, the "Existing Effect / Condition / Harm" step above does not currently include Location Index output, even where the Trigger→Existing Test step produces a genuine Core Test roll. See Proposals/WIP §2.5A.

---

# 16. Phase 9 — Rest and Healing

Implement the attrition loop after harm and death rules are sufficiently stable: Rest, resource recovery, wound recovery, healing time, ongoing conditions, and recovery from incapacitation. Evaluate against the requirement that Rest must not trivialize the resource identity.

---

# 17. Phase 10 — Magic and Special Abilities

Implement a setting-facing power grammar around Advanced Skills. Verify Body-rooted and Mind-rooted powers, mixed-domain Advanced Skills, Overflow, failed Doubles, Conditions, Effects, and Extended Tests. Fixed spell lists may exist as setting content but must not be required by the Core.

---

# 18. Phase 11 — NPC Compression

NPC construction should compress the same underlying mechanics rather than introduce a separate NPC engine. Evaluate encounter construction time, mathematical compatibility, resource behaviour, survivability, and challenge curves. NPC packages must still resolve through the same Universal Play architecture.

---

# 19. Phase 12 — Setting Interface

A setting module may add content, permissions, creatures, equipment, powers, technology, magic, Tags, and Effects. It may not redefine d100, roll-under, 100-Fumble, Cost = Roll, Overflow → HP, Failure XP, Skill Roll Pool, Advanced Skill construction, or Core recovery.

> **Acceptance criterion:** A new setting can be implemented without modifying the Core Engine.

---

# 20. Phase 13 — Full Integration Simulation

## 20.1 Opposed exchanges

Test low versus high and equal Skill; Skill > 99; both succeed, one succeeds, and both fail; 100-Fumble; failed Doubles; and resource exhaustion.

## 20.2 Combat

Test locations on/off and location tiers; armour; defense; Effects; Conditions; wounds; incapacitation; and death.

## 20.3 Extended Tests

Compare progress and failure models, resource drain, Overflow, Failure XP, and Advanced Skill creation.

## 20.4 Powers

Test Mind-rooted, Body-rooted, and mixed-domain powers; Overflow; failed Doubles; Conditions; and Effects.

## 20.5 Non-combat

Test social contests, research, crafting, travel, hazards, stealth, and technical tasks.

**Note (v1.4.3):** hazard testing in this phase should confirm the absence of Location Index generation for non-attack cases, consistent with the S-2 non-attack deferral, unless that deferral has been explicitly reopened and superseded by then.

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

Tiwas should not be considered mechanically complete until every meaningful test uses the common Core transaction; opposed actions use the universal contest primitive; successful contests can create meaningful state change; harm supports both resource attrition and meaningful injury; location granularity is configurable; the completed death model preserves heroic resilience; combat and Extended Tests share coherent time architecture; Conditions and Tags are reusable; progression remains failure-driven; Extended Tests do not create a second currency; powers use the universal Skill architecture; NPCs use compressed versions of the same mechanics; settings can be added without modifying Core invariants; and the full regression suite passes.

---

# 23. Project Governance

## 23.1 Status transitions

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

- **Mechanical fact:** directly follows from existing locked rules.
- **Empirical finding:** supported by simulation, playtesting, or other explicit evidence.
- **Designer ruling:** a deliberate choice not mathematically forced by the system.
- **Recommendation:** a proposed preference not yet accepted.
- **Architectural constraint:** governs how systems interact rather than what a mechanic numerically does.

Evidence must be recorded with its scope and limitations. An empirical finding does not itself establish a designer ruling; an architectural constraint does not establish a numerical mechanic. Future documents should label these categories wherever confusion is likely.

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
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
14. When a subsystem is locked, update the Canonical document and its changelog.
15. When a proposal is superseded, retain its historical significance but clearly mark it Superseded.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

---

# 25. Documentation Maintenance Rule

The three consolidated documents should remain synchronized.

## When a rule becomes locked

Update Canonical Rules, the Canonical Changelog, Proposal status, Roadmap status/dependencies, and regression requirements if applicable.

## When a proposal changes

Update Proposals/WIP and the relevant Roadmap dependency or phase. Do not modify Canonical Rules.

## When an implementation decision changes

Update the Roadmap and any relevant WIP note if it affects a design proposal. Do not modify Canonical Rules unless the actual game mechanic has changed through formal governance.

---

# 26. Core Project Principle

The implementation target is not merely “complete combat.” The target is:

> **A universal state-resolution architecture in which combat, social conflict, hazards, crafting, research, travel, magic and other activities reuse the same Tiwas Core transaction.**

The central architectural rule is:

> **Every Universal Play Module must be an adapter around the locked Tiwas Core transaction, never a competing resolution, resource, progression, or recovery engine.**

```

## Tiwas___Proposals__WIP___Design_Direction-v1_4_3.md

```markdown
# Tiwas — Proposals, WIP & Design Direction

**Document Version:** v1.4.3
**Document Status:** Non-Canonical Design Repository
**Authority:** Design exploration only
**Revision nature:** §2.5 updated to record the designer ruling closing the S-2 Non-Attack Location Index Source investigation (deferred, not resolved as a mechanic). No other content changed from v1.4.2. This is not a promotion to Canonical status — see §21 and §23.
**Supersedes:** Proposals, WIP & Design Direction v1.4.2 (§2.5 only; all other content carried forward unchanged)
**Purpose:** Central repository for unresolved, proposed, experimental and directional Tiwas mechanics
**Critical rule:** Nothing in this document is canonical merely because it is described in detail.

**Version-number note:** This file is labelled **v1.4.3**. Earlier minor-revision files in this series used a `1.4x` filename pattern by accident. Later files use the correct `x.y.z` format.

**Authority boundary:** This document records design state; it does not determine design state. Where this document conflicts with the Canonical Rules or a current governance decision, the Canonical Rules and the explicit governance decision prevail.

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

Do not treat **Design Direction**, **WIP**, **Proposed**, or an **observation** as locked rules. An observation is an evidence/design note, not a lifecycle status.

Only the Canonical Rules document creates current rules.

---

# 1. Current Design Direction

The following high-level design principles are retained as the current direction for Tiwas development. They are not canonical rules by virtue of appearing in this heading.

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

**Status: Partially locked / WIP — Tier-1 Location Index provider locked. Invocation/warrant policy: Candidate policy accepted for further development; not yet promoted to Canonical. Non-attack Location Index generation: Ruled deferred (see §2.5A).**

**Zero-Step is locked; the broader S-2 architecture, including the warrant policy below, is not.**

The Canonical Rules record a **Canonical / Locked — limited S-2 decision**: only the Tier-1 Location Index provider (Zero-Step) is locked. Tier policy, anatomical mapping, and downstream interactions remain unresolved. A separate, extensive non-canonical investigation (S-2 Design Investigation v1–v5) has produced a **candidate invocation/warrant policy**, summarized below and detailed in the investigation record (see `Tiwas_S2_Design_Investigation_v5_synthesis_CORRECTED.md`). This candidate policy is accepted as the current working direction for S-2's invocation question but has not completed the promotion process in §21 and does not modify this document's non-canonical status.

A follow-on investigation (S-2 Non-Attack Location Index Source, starter brief v1.1) examined a narrower question — whether, and whose, natural roll supplies a Location Index for non-attack physical resolutions (falls, hazards, structural collapses). That investigation concluded with a designer ruling; see §2.5A.

## 2.1 Limited locked S-2 decision

Unchanged from v1.4.2 — Zero-Step remains the locked Tier-1 provider per Canonical Rules §14.1–§14.2. Not reopened by this update.

## 2.1A S-2 Candidate Invocation Policy (Non-Canonical)

Unchanged from v1.4.2. This policy governs attack-side invocation only. See §2.5A for the separate, now-closed, non-attack question.

The S-2 Design Investigation (v1–v5) proposes the following as a candidate answer to "when should Tiwas generate a Tier-1 Location Index":

**Four-state classification (internal/documentation architecture):**

1. **Established & Resolvable** — location-dependence is conceptually anchored and current rules can act on it → generate.
2. **Established, Not Yet Resolvable** — anchored, but no current rule can act on the result yet → do not generate; record as pending.
3. **Outcome Plausible, Location-Dependence Unresolved** — the named consequence is a reasonable future outcome, but whether location specifically delivers it is an open design fork, not just an unimplemented detail → do not generate.
4. **No Distinct Consequence** — no distinct outcome named → do not generate.

**GM-facing procedure (simplified, draft):**

> Generate a Location Index only when the player has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design (not merely plausible or anticipated), and current rules can actually resolve it.

**Warrant test (Named-Outcome Test):** a declared objective is definite — and Warrant-eligible — only if the player explicitly names a distinct consequence, other than ordinary damage, tied to the specified location. Conditional phrasing does not defeat definiteness; stated purpose/motivation without a named distinct outcome does not establish it.

**Designer rulings adopted into this candidate policy:**
- **Explicit-only objectives.** The GM does not infer an unstated distinct objective from location or fictional context alone.

**Procedural riders (carried into the candidate policy):**
- Compound objectives evaluated disjunctively.
- Stale objectives (fictional state no longer supports the category's rationale) void an otherwise-matching case.
- In S-1 opposed contests, only the winning participant's natural roll is eligible for Location Index generation (per Canonical §13.2 — Quality never alters either participant's historical roll).
- Location Index evaluation may be deferred (lazy evaluation) to whenever a downstream stage first needs the answer, since Zero-Step is a read-only post-process of an already-recorded roll (Canonical §14.2). *(Design inference, provisionally adopted — not separately stress-tested at the table, unlike the three procedural riders above.)*

**Conceptual Anchor findings (current, subject to revision as S-3/S-5/S-7/S-10 develop):**

**Note:** the table below reflects design inference tested against source documents (the Conceptual Anchor Challenge), not blind-trial data. It does not carry the same evidentiary weight as the Named-Outcome Test above, which was validated against 21/21 trial cases.

| Concept | State | Basis |
|---|---|---|
| Structural weak points (hinges, supports, load-bearing components) | **2 (Established, Not Yet Resolvable)** | Location-dependence is anchored and narratively distinguishable — no competing non-location mechanism is proposed for this concept, unlike the State-3 rows below — but current rules do not yet provide a settled Location Index→component mapping or downstream resolution mechanism (see §2.5). Not currently an Active/Generate entry. |
| Disarm / Break Hold | **3** | §3.2 below already contemplates Margin/Tag-gated triggering as an alternative to location; location-mechanism unresolved |
| Equipment damage | **3** | Same basis |
| Function impairment (blindness, movement) | **3** | §10 Conditions have no stated activation mechanism |
| Armor bypass | **3** | §5 below documents Tag/Trait-based interaction as the current design direction — a documented alternative mechanism, which is what this table's Anchor test requires for Unanchored/State-3 status. §5 emphasizes Tags and does not itself address whether location also participates; that is a gap, not a stated contradiction. |
| Incapacitation / kill | **3, circularly** | §4.1/§7 below condition localized injury on locations already being active — this concept cannot be resolved independently of the S-2 decision itself |

**Important:** entries at State 3 are *not* Watch-list entries pending implementation. They record an unresolved design fork (is location the mechanism at all), not merely missing numbers. They should be revisited only when the relevant future subsystem makes an explicit choice that location is how the outcome is delivered — not merely when that subsystem locks in any form.

**W3 cache role:** the cache is a maintained shorthand for situations already established at State 1 or 2 by the policy above. It does not independently establish Warrant or Anchor status. Novel, uncached situations are still evaluated directly against the policy (confirmed by two independent novel-case trials during the investigation, both resolving correctly without cache membership). At present, no candidate sits at State 1; Structural Weak Points is the sole State-2 entry (see table above), and no Location Index currently generates for it in play.

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

- whether the location tier is universally fixed or selected by situation, scene or campaign — **still open.** The candidate invocation policy determines *when a Location Index is warranted within whatever tier is in use*; it does not determine *whether a scene/campaign uses Tier 0, Tier 1, or Tier 2* in the first place. The candidate policy is a relevant input to that future decision, not a resolution of it.
- when Tier 1 is invoked (attack-side) — **the mechanism for this is now addressed** (the candidate invocation policy directly answers "does this specific resolution warrant a Location Index"), but this is narrower than the scene/campaign tier-selection question above, which remains open.
- **whose roll, if any, supplies a Location Index for non-attack physical resolutions (hazards, falls, structural interactions with no adversarial "attacker") — RESOLVED BY DESIGNER RULING (see §2.5A immediately below). No longer an open question in the "undecided" sense; it is a closed deferral pending an explicit future reopening trigger.**
- the anatomical mapping table (numeric Location Index → structural/anatomical component) — still open, untouched by this investigation. This includes the structural-destruction case in §2.1A's Conceptual Anchor table: its State-2 status establishes narrative resolvability only, not a settled mapping.
- Tier-2 procedure and resolution cost — still open, untouched.
- interaction with wounds, armour, defence and Outcome Effects — still open; the investigation's State-3 findings (Disarm, Equipment, Impairment, Armor Bypass, Incapacitation all currently unanchored to location) are directly relevant inputs to this future work.
- final GM-facing wording for the simplified invocation procedure (§2.1A) — drafted, not yet separately validated.

## 2.5A Non-Attack Location Index Source — Designer Ruling (New in v1.4.3)

**Status: Designer Ruling. Closes the S-2 Non-Attack Location Index Source investigation (starter brief v1.1) as a deferral. Not a Canonical change; recorded here as the current non-canonical governing position until formally promoted.**

> **Ruling: Non-attack physical resolutions (falls, hazards, structural collapses, and other non-adversarial physical events) generate no Tier-1 Location Index under current design — categorically, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution. This is a deferral, not a claim that non-attack location is impossible in principle.**

This applies regardless of:

- whether an underlying Core Test exists for the resolution;
- who made that test (the affected character, the causing character, a third party);
- whether the hazard was caused intentionally or accidentally;
- how specifically the GM narrates the physical consequence;
- the severity of the consequence.

**Zero-Step Location Index generation remains attack-side only** under current design. The canonical Zero-Step mechanism itself (Canonical §14.1–§14.2) is entirely untouched by this ruling — this ruling only concerns whether non-attack resolutions are eligible to invoke it at all, and the answer is currently no.

**Investigation record retained, not deleted:**

| Item | Status |
|---|---|
| H0 (governing Core Test provenance rule) | Retained as an inert candidate record — a starting hypothesis if this question is reopened, not a validated operative rule |
| H0 Rider A (no cross-character roll-sharing) | Retained, inert, tied to H0 |
| H0 Rider B (multi-test causal-chain tie-break) | Retained, inert, tied to H0 — two sub-options were identified but never adjudicated against each other |
| GM-authored hazard warrant (rejected candidate direction) | Rejected for now, not deleted from the record |
| Named-Outcome/Warrant Test transfer to non-attack cases | Deferred, not resolved — moot while non-attack generation is off entirely |
| Blind provenance trial | Not authorized — correctly withheld, since the category is closed |

**Reopening conditions.** This ruling is a deferral tied to specific future work, not a permanent architectural conclusion. It should be **explicitly reopened**, not silently inherited, when:

- **S-4** (Wound activation/severity) reaches a design stage where localized non-attack injury becomes relevant;
- **S-7** (Incapacitation/death) reaches a design stage where hazard severity needs finer resolution than flat damage;
- **S-8** (Difficulty/Stakes Gate) reaches a design stage where hazard-stakes framing is formally defined — flagged as the most likely natural reopening trigger.

When reopened, H0 and its riders serve as a starting hypothesis to re-validate against whatever S-4/S-7/S-8 actually specify — not a pre-approved answer to carry forward unexamined.

**Does not affect:** Zero-Step (attack-side), S-1, the attack-side invocation/warrant policy (§2.1A), Structural Weak Points' State-2 classification, the W3 cache, or Tier 0/1/2 scene-selection policy. None of these are reopened by this ruling.

## 2.6 E9 human usability playtest

**Evidence class: Empirical finding — passed for the tested physical two-d10 method only.**

The E9 playtest used two physical d10s with 50 participants in ten groups of five:

- 25 participants new to RPGs; and
- 25 RPG players new to Tiwas.

Participants reported no difficulty rolling the dice or exchanging the digits for hit location, and feedback was positive.

This evidence supports usability of Zero-Step **for the tested physical two-d10 method only**. It does **not** establish usability for:

- a single d100;
- a digital roller;
- verbally announced results;
- other input methods.

Those methods were not tested and are not covered by this finding. E9 did not settle the remaining S-2 architecture.

## 2.7 Future optional-rule observations

**Observation ≠ proposal ≠ rule.**

Participants asked whether they could choose the natural or swapped number. That remark is a design observation only. It is not a proposal under active consideration, and it is not a current rule. The canonical basic rule remains deterministic and provides no such choice.

For a future optional-rule appendix, the designer may consider:

1. attacker choice granted only by an explicit special ability; and
2. defender choice.

Neither option is authorised for current play, nor does this section recommend one. This observation is retained, not expanded.

## 2.8 Comparative derivation-cost residual

Separate from E9, the completed comparison found that Units-Digit requires 0–1 additional derivation operations across the examined rolling modes, while Zero-Step requires 1–2.

This is a **structural comparison of derivation steps, not a human-usability result** and not an additional E9 label. It cannot substitute for input-method-specific usability testing.

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

**Note (v1.4.3):** the closed S-2 Non-Attack Location Index Source ruling (§2.5A) flags S-8 as its most likely reopening trigger, since Stakes Gate is the natural home for deciding when a hazard resolution carries enough mechanical weight to warrant location-level detail. This is a cross-reference only; it does not narrow or predetermine S-8's own design.

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

**Note (v1.4.3):** per §2.5A, hazards resolved through this structure do not currently generate a Tier-1 Location Index, regardless of how the Outcome is narrated. This is unchanged by the present section and is cross-referenced here only for clarity.

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
| S-2 | Broader hit-location architecture: tier policy, mapping and downstream interaction. Zero-Step (Tier-1 Location Index provider) is locked. **Invocation/warrant policy (attack-side): candidate accepted (S-2 Design Investigation v1–v5), non-canonical, pending promotion. Non-attack Location Index generation: RULED — deferred, none generated until S-4/S-7/S-8 reopens the question (§2.5A).** Anatomical mapping, Tier-2 procedure remain fully open. | Partially locked / WIP — Tier-1 provider locked; candidate invocation policy accepted for further development; non-attack question closed as a deferral |
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

No row in this register is a canonical rule. Status labels here do not promote a proposal, observation, or design direction into a locked mechanic.

---

# 21. Promotion Rule

This section is a **governance clarification**, not a change to game mechanics.

A proposal in this document may become canonical only after all of the following:

1. its design question is explicitly identified;
2. competing alternatives have been considered where appropriate;
3. relevant simulation/analysis has been completed;
4. the human designer has accepted the ruling;
5. the mechanic is documented as a formal rule;
6. the Canonical Rules & Changelog document is updated;
7. the former proposal is marked Superseded or Locked here;
8. implementation documentation is updated.

A detailed proposal is not a rule merely because it is detailed. A detailed LLM draft is not a rule. Locked mechanics in the Canonical Rules can be reopened only through normal design governance and substantive evidence.

Until those steps are complete, material in this repository remains non-canonical regardless of how fully it is described.

---

# 22. v1.4.1 Revision Record

v1.3 remains the authoritative baseline for subsystem content, candidate mechanics, status classifications, architecture, residual decisions, and S-1D historical treatment.

v1.4.1 does not adopt the proposed v1.4 draft as a new design state. It incorporates selected documentation and governance corrections:

- heading **Locked Design Direction** replaced with **Current Design Direction**, so this repository is not read as a second lock file;
- explicit cross-document authority statement added at the head of the document;
- S-2 status wording aligned with the Canonical limited lock: Zero-Step / Tier-1 Location Index provider locked; S-2 unfinished;
- E9 limited to the tested physical two-d10 method, with other input methods explicitly untested;
- derivation-cost comparison kept separate from E9 and labelled as structural, not a human-usability result;
- observation / proposal / rule distinction stated for the attacker-choice / defender-choice remark, without expanding that material;
- promotion process retained as an eight-step governance rule, not a mechanical change;
- Canonical Rules citation in §2.1 updated to v1.3;
- evidence is explicitly distinguished from the designer ruling/mechanic that may later be informed by that evidence.

No unresolved subsystem is advanced to canonical status by this revision.

---

# 23. v1.4.2 Revision Record

Section 2 (S-2 — Hit-Location Architecture) replaced with the S-2 Design Investigation v1–v5 candidate invocation/warrant policy — a four-state internal classification, the Named-Outcome Test, the Conceptual Anchor findings table, and the revised W3 cache role — accepted as the current non-canonical working direction for S-2's invocation question. This is **not** a promotion to Canonical status; see §21.

§2.5 open-questions list updated to reflect what the investigation resolved (when Tier 1 is invoked, for a given resolution) versus what it explicitly did not (scene/campaign tier selection; anatomical mapping; non-attack Location Index source; final GM-facing wording). §20's S-2 row updated to match.

Two designer rulings recorded by this candidate policy: explicit-only objectives (the GM does not infer a distinct mechanical objective from location or context alone), and acceptance of the synthesis itself as the current non-canonical candidate.

Corrections applied to the incoming investigation material after independent review, before this merge:

- Armor Bypass basis reworded — no longer overclaims a "contradiction" the cited source text (§5, this document) doesn't actually contain. State/Anchor classification unchanged (still State 3 / Unanchored — a documented alternative mechanism is what the test requires, and one exists).
- Lazy evaluation flagged as design inference, not an empirically confirmed procedural rule like the other three riders in §2.1A.

**Second correction round, same v1.4.2 pass (designer ruling, not a wording fix):** Structural Weak Points reclassified from **State 1 to State 2** (Established, Not Yet Resolvable) in §2.1A's Conceptual Anchor table. The State-1 definition requires current rules to provide a mechanism to act on the result, not merely that a GM could narrate one — "ordinary narration" is available to every category and cannot be what distinguishes State 1, or the State 1/2/3 distinction collapses entirely. Structural Weak Points remains Anchored (no competing non-location mechanism is proposed for it, unlike Disarm/Armor Bypass), but anchored-without-a-resolution-mechanism is what State 2 is for. Practical effect: Zero-Step does not currently generate a Location Index for this category; the W3 cache now has zero State-1 (Active/Generate) entries, which is an accurate reflection of current design completeness rather than a defect.

No Canonical Rules changed. S-2 remains unlocked beyond the existing Zero-Step Tier-1 provider lock (Canonical §14.1–§14.2). Nothing in this revision is promoted to Canonical status.

The former Section 2 text (as it stood in v1.4.1) is superseded by the text above but retains historical significance as the pre-investigation state of S-2 documentation.

---

# 24. v1.4.3 Revision Record

A follow-on, narrower investigation (S-2 Non-Attack Location Index Source, starter brief v1.1) examined whether, and whose, natural roll supplies a Location Index for non-attack physical resolutions (falls, hazards, structural collapses with no adversarial "attacker"). The investigation proceeded through a provenance-only stress test (candidate rule H0: "governing Core Test's roll, or no index," plus two riders on cross-character and multi-test causal-chain cases) while deliberately keeping the separate warrant-transfer question (whether the existing player-declaration-based Named-Outcome Test can be satisfied by a GM-stated hazard consequence) unresolved and unscored.

**Designer ruling (this revision):** Non-attack physical resolutions generate no Tier-1 Location Index under current design — categorically, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution. This is recorded in the new §2.5A. It is a deferral, not a claim that non-attack location is impossible in principle, and it is explicitly tied to reopening triggers: S-4 (Wound activation/severity), S-7 (Incapacitation/death), and S-8 (Difficulty/Stakes Gate), with S-8 flagged as the most likely natural trigger.

Direct effects of this ruling:

- The GM-authored-stakes candidate for warrant transfer is rejected for now (not deleted from the record).
- The H0 provenance rule and its two riders are retained as an inert candidate record — a starting hypothesis if this question is reopened, not a validated operative rule.
- No blind provenance trial was run, correctly, since the ruling makes warrant-eligibility categorically "never" for the affected category, leaving nothing live to stress-test.
- §2.5's open-questions list updated to move this item from open to resolved-as-deferral.
- §20's S-2 row and §14 (Environmental Hazards) updated with a cross-reference.
- §8 (S-8) annotated with a cross-reference to the reopening-trigger flag; S-8's own design scope is not narrowed or predetermined by this note.

This ruling does not reopen, alter, or narrow: Zero-Step (attack-side, Canonical §14.1–§14.2), S-1, the attack-side invocation/warrant policy (§2.1A), the Structural Weak Points State-2 classification, the W3 cache, or Tier 0/1/2 scene-selection policy. No Canonical Rules changed. Nothing in this revision is promoted to Canonical status; see §21.

The former §2.5 non-attack bullet (as it stood in v1.4.2, "still open") is superseded by the ruling recorded in §2.5A but retains historical significance as the pre-ruling open-question state.

```

## Tiwas___S2_Hit_Location_Investigation_v5_Synthesis.md

```markdown
# Tiwas S-2 Design Investigation v5 — Non-Canonical Synthesis (Correction Pass)

**Status: S-2 Candidate Policy — Accepted by designer ruling for further development/testing. NON-CANONICAL. S-2 remains unlocked per Canonical §14.3. Cannot modify Canonical Rules under any circumstance; may inform Proposals/WIP and Roadmap updates per §11 (added below).**

**Correction pass (this revision, supersedes the uploaded v5 synthesis):** Three wording/evidence-labeling corrections applied after independent external review and independent re-verification against this document's own citations. **No classification, ruling, or open/closed status changed** — only overclaiming basis text was reworded. Each fix is marked inline with a `[Corrected this revision]` tag at point of change.

1. §4 / §6 — **Armor Bypass** basis reworded. "Directly contradicted"/"textual contradiction" overclaimed against Proposals §5's actual text, which favors Tags but never addresses location at all — that is silence with a stated preference, not contradiction. Reworded to state only what §5 actually says. The Unanchored/State-3 classification itself is unchanged and correctly supported (an alternative non-location mechanism does exist in the documented design space, which is the actual test in §4). The "most strongly"/"most firmly" ranking is removed, since it rested entirely on the overstated contradiction claim.
2. §4 / §6 — **Structural Destruction (State 1)** given a clarifying note. "Resolvable through ordinary physical narration" refers to narrative differentiation only. It does not mean the numeric Location Index → structural-component mapping is itself established — that mapping is part of the still-open anatomical mapping question (Canonical §14.3). The original wording risked implying the latter was also settled; it wasn't and isn't.
3. §5 — Section header and lead-in corrected. The lazy-evaluation row is explicitly tagged `[Design inference, ... not separately stress-tested]`, so the section header's blanket claim of "Confirmed Across Multiple Rounds" overstated that one row's evidence class. Header now points to the per-row tags instead of asserting uniform confirmation.
4. §4 / §6 — **Structural Weak Points reclassified from State 1 to State 2** (Established, Not Yet Resolvable). Correction #2 above already established that only narrative differentiation exists, not a settled Index→component mechanism — but it stopped short of following that through to the classification itself. Per the four-state model's own definitions, State 1 requires current rules to provide a mechanism to act on the result, not merely that a GM could narrate something. "Ordinary GM narration" is available for every category (including the State-3 ones), so it cannot be what qualifies something for State 1 without collapsing the State 1/2/3 distinction entirely. Structural Weak Points remains **Anchored** (§4) — no competing non-location mechanism is proposed for it, unlike Disarm/Armor Bypass/etc. — but anchored-without-a-resolution-mechanism is exactly what State 2 is for. **This is a designer ruling, not a wording fix**: it changes table behavior (Zero-Step does not currently fire for this category) and was decided as option A of two presented alternatives. The W3 cache (§6) accordingly now has zero State-1 (Active/Generate) entries.

**Designer rulings recorded this revision:**
- **Explicit-only objectives — RULED.** The GM does not infer a distinct mechanical objective from location, description, or fictional context alone; the player must state the distinct consequence. Formerly §8 item 1 ("Open"); reclassified below as a Designer Ruling, not an empirical finding.
- **This synthesis — ACCEPTED** as the current non-canonical S-2 candidate policy. Not a lock. Subject to revision if S-3/S-5/S-7/S-10 design work, the still-open non-attack-resolution scope question, or future evidence materially changes it.
- **Structural Weak Points — RULED State 2, not State 1.** Anchored, but current rules do not yet provide a mechanism (an Index→component mapping) to act on the result. See correction #4 above for full reasoning.

**Supersedes (as a synthesis only, not as a record):** consolidates findings from v1–v4 and the six-round interactive investigation (falsification test, two blind table-practice tests, the Declared Objective Boundary Test, and the Conceptual Anchor Challenge). Those documents/rounds remain the evidentiary record; this document is the proposed policy built from them.

**Not touched:** Zero-Step derivation mechanics (Canonical §14.1–§14.2, locked, not reopened), S-1 (locked, not reopened), anatomical mapping, Tier-2 mechanics, and all S-3/S-4/S-5/S-7 numerical rules.

---

## 1. What This Document Is and Isn't

This is a **proposed answer to the open half of S-2** — the invocation/warrant policy that Canonical Rules §14.3 explicitly leaves unresolved. It is built entirely from the investigation record: two falsification rounds, two independent blind table-practice trials (14 items, then 21 items), and a document-grounded conceptual challenge. It does not, by itself, lock anything. Adoption requires your explicit ruling, and even then only Proposals/WIP and the Roadmap update — Canonical Rules change only through the eight-step promotion process already defined there (Proposals §21).

---

**[Architectural constraint — clarified this revision]** This synthesis answers *when a Location Index is warranted for a given resolution*. It does not answer, and should not be read as narrowing, the separate question of *whether a scene or campaign uses Tier 0, Tier 1, or Tier 2 in the first place* (Canonical §14.3, Proposals §2.3/§2.5). That tier-selection question remains fully open; this policy is an input to it, not a resolution of it.

---

## 2. Core Policy — The Four-State Model

**[Design inference, synthesized from the full investigation]** Every resolution that could plausibly involve a physical impact is classified into exactly one of four states:

| State | Definition | Generate Location Index? |
|---|---|---|
| **1 — Established & Resolvable** | Location-dependence is conceptually anchored (not contingent on an unmade design choice) **and** current Tiwas rules provide a mechanism to act on the result | **Yes** |
| **2 — Established, Not Yet Resolvable** | Location-dependence is anchored, but no current rule can act on the result yet | **No** — record as a pending dependency |
| **3 — Outcome Plausible, Location-Dependence Unresolved** | The named consequence itself is a reasonable future Tiwas outcome, but whether *location specifically* is the mechanism that delivers it is an open design question, not merely an unimplemented one | **No** — do not treat as warranted; this is not a subsystem-completeness gap, it's an unmade design fork |
| **4 — No Distinct Consequence** | The declared action names no consequence beyond ordinary damage, or names none at all | **No** |

**[Architectural constraint, carried through every round of this investigation]** State 3 must never be quietly merged into State 2. Round 5's Conceptual Anchor Challenge exists specifically because the earlier cache draft (v4) had done exactly that — treating "Disarm is a plausible outcome" as equivalent to "location is how Disarm gets triggered," when the documents themselves (Proposals §3.2, §5) support at least one fully plausible alternative (Margin/Tag-gated triggering) that doesn't reference location at all.

---

## 3. The Warrant Test — Named-Outcome Rule

**[Empirical finding, single-designer trial, 21/21 consistent]**

> A declared objective is **definite** — and therefore Warrant-eligible — if and only if the player explicitly names a distinct consequence, other than ordinary damage, whose resolution depends on the specified location. Purpose or motivation language ("to really hurt him," "to get through his defenses") does not by itself create definiteness unless the named result is itself distinct from ordinary damage. Conditional phrasing ("if I get the chance...") does not defeat definiteness; only the presence or absence of a named distinct outcome matters.

This closes both confirmed cross-round instabilities (the armor-gap divergence and the conditional-objective divergence) — both were shown to be instances of the same underlying variable (definiteness of named outcome), not two separate problems.

---

## 4. Conceptual Anchor — Prerequisite to Warrant

**[Design inference, tested against source documents via the Conceptual Anchor Challenge, not against blind-trial data. This table's evidence class is distinct from — and does not carry the same weight as — the 21/21 Named-Outcome trial result in §3.]**

> A named outcome's location-dependence is **anchored** if the Tiwas design documents do not contain a stated or clearly plausible alternative mechanism (e.g., Margin/Quality threshold, Tag-gated trigger) that would deliver the same outcome without reference to struck location. It is **unanchored** if such an alternative exists in the documented design space, whether or not that alternative is the one eventually chosen.

| Concept | Anchor status | Basis |
|---|---|---|
| Structural destruction (hinges, supports, weak points) | **Anchored** | No competing non-location mechanism is proposed for this concept, unlike the Unanchored rows below. **[Corrected this revision, round 2]** Anchor status establishes location-dependence only — it does not by itself establish State-1 resolvability. Narrative differentiation is possible today; the numeric Location Index → structural-component mapping remains a separate, still-open question (Canonical §14.3, Proposals §2.5). See §6: this concept is classified **State 2**, not State 1. |
| Disarm / Break Hold | **Unanchored** | Proposals §3.2 explicitly contemplates Margin/Quality-band and Tag-gated Effect triggering as alternatives to location |
| Equipment damage | **Unanchored** | Same basis as Disarm |
| Function impairment (blindness, movement) | **Unanchored** | Conditions (§10) have no stated activation mechanism; nothing ties them to location specifically |
| Armor bypass | **Unanchored** | **[Corrected this revision]** Proposals §5 documents Tag/Trait-based interaction as the current design direction — a documented alternative mechanism, which is what the Anchor test above actually requires for Unanchored status. §5 emphasizes Tags and simply does not address whether location also participates; that is a gap, not a stated contradiction. |
| Incapacitation / kill | **Unanchored, circularly** | Proposals §4.1/§7 condition localized injury mattering on locations already being active — S-7's own language depends on this S-2 decision, not the reverse |

**[Recommendation, updated this revision]** Structural Destruction currently qualifies for **State 2** (Established, Not Yet Resolvable) — anchored, but no settled resolution mechanism exists yet. It is the only entry in this table that is anchored at all. Everything else sits in **State 3** until the relevant future subsystem (S-3, S-5, S-7, S-10) makes an explicit design choice that location is the delivery mechanism — at which point, and only then, it may be re-evaluated for promotion. Nothing in this table currently qualifies for State 1.

---

## 5. Procedural Rules

**[Evidence class varies per row — empirical finding, architectural constraint, or design inference, as tagged in the right-hand column. Not all rows below carry the same evidentiary weight; see the lazy-evaluation row specifically. `[Corrected this revision]`: the section previously carried a blanket "(Confirmed Across Multiple Rounds)" header, which overstated the lazy-evaluation row's actual evidence class.]**

| Rule | Basis |
|---|---|
| **Compound objectives** are evaluated disjunctively — if any named branch of a multi-part declaration satisfies the Named-Outcome Test, Warrant is established for that branch, regardless of how the rest of the declaration reads | Confirmed twice (Round 1 #9-analog, Round 3 #15) |
| **Stale objectives void the match** — a category or Named-Outcome match is invalid if the fictional state on record no longer supports its rationale (e.g., declaring a disarm against an already-empty hand) | Confirmed (Round 1 #5, Round 2 #10) |
| **S-1 winner-only** — in an opposed contest, only the winning participant's natural roll is ever eligible for Location Index generation; per Canonical §13.2, Quality never alters either participant's historical roll, and the losing roll has no consumer for a Location Index under any current or proposed rule | Confirmed (Round 1 #10, Round 2 #11) — [Architectural constraint, Canonical §13.2] |
| **Lazy evaluation** — because Zero-Step is a read-only post-process of an already-recorded natural roll (Canonical §14.2), Warrant/Resolvability evaluation does not need to occur at declaration time; it may be deferred to whenever a downstream stage first requires the answer | [Design inference, Phase 2 finding D, not separately stress-tested at the table] |
| **Explicit-only objective boundary** — the GM does not infer an unstated distinct objective from location or fictional context alone; only stated objectives are Warrant-eligible | **[Designer ruling.]** Tested cleanly (21/21, Round 3, including the #16/#17 minimal pair); adopted by explicit designer decision, not derived from the test result alone |

---

## 5A. GM-Facing Procedure (Simplified) vs. Internal Architecture

**[Design inference, incorporating designer guidance this revision]** The four-state model in §2 is retained as the **internal/documentation architecture** — it explains *why* a given case resolves the way it does, and it is what the Anchor Challenge and the cache in §6 are built from. It is **not** intended as something a GM consciously walks through at the table. Per the second blind test's own result (`Generate = Warrant ∧ Resolvable`, holding exactly across all 14 trial cases with no independent third judgment needed at the point of play), the GM-facing rule collapses to one question:

> **Generate a Location Index only when the player has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design (not merely plausible or anticipated), and current rules can actually resolve it.**

Conceptual Anchor (§4) does real work in *determining* whether a given category's location-dependence counts as "already established," but a GM applying the rule in play is not asked to separately classify something as "State 3" — that classification work is front-loaded into which entries the W3 cache (§6) is allowed to contain. This keeps the table-facing rule to a single test while preserving the more careful internal distinctions that produced it. **This wording is a draft implementing the designer's stated direction, not yet separately validated at the table** — worth a light review pass before being treated as final phrasing, though it does not require another blind test to adopt provisionally.

---

## 6. W3's Role — Reference Layer, Not Independent Authority

**[Design inference, corrected from v4's original framing]** The investigation's early rounds treated W3 as a semi-independent gate ("Active cache entries authorize generation"). The evidence no longer supports that. Round 3's novel-instantiation cases (#8, #12 — a lantern-and-support-beam and a castle-wall breach, neither a verbatim cache entry) generated correctly by applying the *underlying* four-state test, not by cache lookup. **W3's corrected role: a maintained shorthand recording situations for which States 1 or 2 have already been established by the policy above, so recurring cases don't require re-deriving the answer from scratch at the table.** It never establishes Warrant or Anchor status on its own authority.

### Current cache (revised, honest framing per your approval)

**[Reclassified this revision, round 2]** Following the Structural Weak Points reclassification below, this cache currently contains **zero State-1 (Active/Generate) entries**. That is an accurate reflection of current design completeness, not a defect the cache should paper over — a cache implying resolvability that doesn't yet exist would be worse than an honestly empty one.

| Category | State | Notes |
|---|---|---|
| Structural weak points (hinges, supports, load-bearing components) | **2 (Established, Not Yet Resolvable)** | Location-dependence is anchored (§4) and narratively distinguishable, but no settled Location Index→component mapping or downstream resolution mechanism exists yet. Not currently an Active/Generate entry — recorded as pending. |
| Disarm | **3** | Outcome plausible; location-mechanism unresolved (§4) — not cache-eligible as a warrant until S-3 makes a locational design choice |
| Equipment damage | **3** | Same |
| Function impairment | **3** | Same |
| Armor bypass | **3** | **[Corrected this revision]** Proposals §5's current direction (Armor Traits/Tags) is a documented alternative mechanism, sufficient for State 3 under §4's test; §5 does not itself address whether location also participates — not a stated contradiction |
| Incapacitation/kill | **3, circularly** | Cannot be resolved independently of this S-2 decision |
| Bare called shots, no named outcome | **4** | Rejected consistently, all rounds |
| "Formal duel" as bare category | **Rejected pattern** | Location-dependence must attach to the duel's stated win condition, not duel status itself |
| Cinematic/tonal framing as a trigger or suppressor | **Rejected as a category; correctly treated as context, not warrant** | Confirmed — tonal framing never overrode the four-state test in trial data |
| Uniform-consequence hazards | **4** | No location-dependent branching by design |

---

## 7. Open Scope Gap — Not Resolved Here

**[Unresolved, carried forward, not solved by this synthesis]** Zero-Step's canonical wording (§14.1) is built around "the attacker's natural d100 roll," which presumes an adversarial impact. Non-combat physical resolutions (the rope-bridge fall, tested twice, State 3 both times on independent grounds) expose that hazards and similar non-attack physical events have no natural "attacker" whose roll Zero-Step consumes. This synthesis does not resolve **whose roll, if any, supplies the Location Index for a non-attack physical resolution** — that remains open and should be treated as a distinct, narrower question for a future investigation, not folded into the warrant policy above.

---

## 8. Designer Decisions — Ruled and Still Open

| # | Decision | Status |
|---|---|---|
| 1 | Explicit-only vs. inferred objectives | **RULED — Explicit-only** (this revision) |
| 2 | Whether this synthesis is accepted as the current S-2 candidate | **RULED — Accepted, non-canonical, S-2 remains unlocked** (this revision) |
| 3 | GM-facing presentation of the four-state model | **Directionally ruled — retain four states internally, simplify to one operational question for the table (§5A).** Exact wording in §5A is a draft implementing that direction, not yet separately validated; a light review pass is worth doing before treating the phrasing as final, but this does not block adoption or require another blind test |
| 4 | Whose roll supplies a Location Index for non-attack physical resolutions (§7) | **Open** — flagged by both parties as a separate, narrower rules-architecture question, not a playtest question |
| 5 | Whether/when State-3 entries (Disarm, Equipment, Impairment, Armor Bypass, Incapacitation) should be revisited | **Open**, dependent on S-3/S-5/S-7/S-10 locking a *location-specific* mechanism, not merely locking numbers |
| 6 | Multi-GM usability validation beyond the current single-evaluator record (two trials, 35 scenario-responses) | **Open, optional** — not required to understand what the rule means, per the investigation's own established framing; may be pursued later if desired |
| 7 | Structural Weak Points — Anchor/State classification | **RULED — State 2 (Established, Not Yet Resolvable), not State 1** (this revision, correction round 2). Anchored, but no settled Index→component resolution mechanism exists yet |

---

## 9. Acceptance Tests (If Adopted)

In the style of Roadmap §9's existing S-2 acceptance criteria, extended:

- The Named-Outcome Test correctly separates bare location narration from stated distinct consequences (validated, 21/21, single trial).
- Conditional phrasing does not defeat definiteness (validated).
- Compound objectives are evaluated disjunctively (validated, two independent instances).
- Stale objectives void an otherwise-matching category (validated, two independent instances).
- Only the S-1 contest winner's roll is eligible for Location Index generation (validated, two independent instances; grounded in Canonical §13.2).
- No State-3 concept generates a Location Index under the current ruleset, regardless of how plausible or frequently-declared (validated by construction, cross-checked against Proposals §3.2/§5).
- Novel, uncached structural cases correctly resolve via the underlying test rather than requiring cache membership (validated, two independent novel instances).

---

## 10. Governance Impact If You Approve This

**Canonical Rules:** No change. §14.3 remains open exactly as written; this document does not claim to close it, only to propose an answer.

**Proposals/WIP:** Section 2 (S-2 — Hit-Location Architecture) would be updated to record this synthesis as a **pending candidate ruling**, with the current "Open design questions" list (§2.5) narrowed to reflect what this investigation actually resolved versus what remains open per §8 above.

**Roadmap:** Phase 2 (S-2) acceptance-test language would gain the four-state model and the acceptance tests in §9 above as implementation guidance, and the W3 cache-maintenance protocol would be updated to the corrected reference-layer framing (§6) rather than the earlier confidence-tier approach.

**No document is modified by this synthesis itself.** These are the changes that *would* follow your ruling, not changes made now.

```

## Tiwas___S2_Non_Attack_Location_Source-CLOSURE_RECORD-v1_2.md

```markdown
# Tiwas — S-2 Non-Attack Location Index Source — Closure Record

**Document Version:** v1.2 (Final — supersedes Starter Brief v1.1 as the status record for this investigation thread)
**Document Status:** Closure record for a completed non-canonical design investigation
**Rule Authority:** None — this document creates no game mechanics
**Governing ruling recorded in:** Proposals/WIP v1.4.3 §2.5A (authoritative non-canonical location); Roadmap v1.4.3 §9 (implementation-relevant summary)
**Purpose:** Preserve the investigation's reasoning and evidence trail so a future session reopening this question does not have to reconstruct it from scratch.

---

## 1. Designer Ruling (Binding, Non-Canonical)

> **Non-attack physical resolutions (falls, hazards, structural collapses, and other non-adversarial physical events) generate no Tier-1 Location Index under current design — categorically, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution.**

This applies regardless of:

- whether an underlying Core Test exists for the resolution;
- who made that test (the affected character, the causing character, a third party);
- whether the hazard was caused intentionally or accidentally;
- how specifically the GM narrates the physical consequence;
- the severity of the consequence.

**This is a deferral, not a claim that non-attack location is impossible in principle.**

Zero-Step (Canonical §14.1–§14.2) itself is entirely untouched. This ruling concerns only whether non-attack resolutions are eligible to invoke it — and the answer is currently no.

---

## 2. Investigation Timeline

| Stage | Content | Outcome |
|---|---|---|
| Starter Brief v1.1 | Framed the question: whose roll, if any, supplies a Location Index when there's no "attacker"; explicitly scoped out reopening Zero-Step, S-1, the attack-side invocation policy, or the Structural Weak Points State-2 ruling | Question opened |
| Round 1 | Candidate analysis: rejected ad-hoc GM rolls (Candidate B) as architecturally excluded (violates Canonical Invariant 18 / no competing resolution engine); collapsed remaining candidates into a single provenance rule | H0 drafted |
| Cross-review (external) | Confirmed A/C/D collapse; proposed broadening "Core Test belonging to a character" to "existing governing Core Test" for forward-compatibility; flagged that Direction 2 (default all non-attack cases to State 3/4) improperly conflates "no player declaration" with "location-dependence unresolved" | H0 refined; Direction 2 flagged as flawed |
| Round 2 | Provenance-only stress test across 14 scenarios; confirmed H0 holds in 11/14 cases; surfaced two riders (no cross-character roll-sharing; tie-break needed for multi-test causal chains); Warrant column deliberately left unscored throughout | H0 + Rider A confirmed as consistent; Rider B drafted as unadjudicated candidate |
| Cross-review (external) | Confirmed H0 wording, confirmed Candidate B exclusion, confirmed Direction 2 withdrawal, endorsed strict sequencing (provenance first, warrant transfer only after) | Sequencing confirmed |
| Designer input requested | Two live decision points identified: (1) GM-authored-stakes substitute vs. categorical exclusion for warrant transfer; (2) blind-trial timing | Clarification requested from designer |
| **Designer ruling** | **Option 2 selected: categorical exclusion, no non-attack Location Index generation until S-4/S-7/S-8 reopens the question** | **Investigation closed as a deferral** |

---

## 3. What Was Resolved vs. What Remains Inert

| Item | Final status |
|---|---|
| Whether non-attack resolutions currently generate a Location Index | **Resolved: no, categorically, until reopened** |
| H0 (governing Core Test provenance rule) | **Inert candidate record.** Not validated as an operative rule — the warrant question closed before H0 needed to become operative. Retained as the starting hypothesis if this question is reopened. |
| H0 Rider A (no cross-character roll-sharing) | Inert, tied to H0. Confirmed as a consistent extension of the existing attack-side pattern (Canonical §14.1 already allows attacker's roll → target's body), not a new problem. |
| H0 Rider B (multi-test causal-chain tie-break) | Inert, tied to H0. Two sub-options were identified (governing test = the one that determines the affected character's own outcome, vs. the first causally-relevant test) — only the first was drafted as a candidate; **never adjudicated against each other.** If reopened, this needs its own resolution, not an assumed default. |
| Direction 1 (GM-stated consequence as declaration-equivalent for Warrant) | Rejected for now, not deleted. This was the substantive alternative to the ruling actually made. |
| Direction 2 (default non-attack cases to State 3/4 via the existing four-state model) | **Withdrawn during cross-review**, prior to the final ruling — found to improperly conflate "no player declaration" with "location-dependence unresolved." Distinct from, and should not be confused with, the final ruling's categorical exclusion, which is a deferral by designer choice, not a four-state classification outcome. |
| Blind provenance trial | Not run. Correctly withheld — the ruling makes warrant-eligibility categorically "never," leaving nothing live to test. |

---

## 4. Reopening Conditions

This investigation is closed **pending**, not closed **permanently**. Reopen explicitly — do not silently inherit this ruling — when:

- **S-4** (Wound activation/severity) reaches a design stage where localized non-attack injury becomes relevant;
- **S-7** (Incapacitation/death) reaches a design stage where hazard severity needs finer resolution than flat damage;
- **S-8** (Difficulty/Stakes Gate) reaches a design stage where hazard-stakes framing is formally defined — **flagged as the most likely natural trigger.**

When reopened:

1. Start from H0 and its two riders as a **starting hypothesis to re-validate**, not a pre-approved answer.
2. Re-run or extend the Round 2 stress-test scenario set (§5 below) against whatever S-4/S-7/S-8 actually specify — they may introduce constraints H0 was never tested against.
3. Separately and explicitly decide the Warrant-transfer question (Direction 1, or a new alternative) — do not assume the old rejection still applies if the underlying subsystem has changed the shape of the question.
4. Adjudicate H0 Rider B's two sub-options against each other, since the original investigation never did.

---

## 5. Stress-Test Scenario Set (Preserved for Reuse)

| # | Scenario |
|---|---|
| 1 | Character reacts to a fall, attempts to catch self |
| 2 | Character fails to react to a fall, no test offered |
| 3 | Character deliberately causes a hazard affecting themself |
| 4 | Hazard affects its creator vs. affects a different character |
| 5 | Environmental hazard with a resistance test |
| 6 | Trap with a Perception/Reflexes reaction test |
| 7 | Automatic trap, no test offered |
| 8 | Collapsing structure, test exists |
| 9 | Collapsing structure resolved entirely by narration |
| 10 | Extended Test interval produces the physical consequence |
| 11 | Multiple affected characters, independent tests |
| 12 | One character's test causes the event; a different character's test resolves its impact |
| 13 | An S-1 opposed contest is involved |
| 14 | Trap resolved retroactively via a Stakes Gate–style reaction |

---

## 6. What This Investigation Explicitly Did Not Touch

Confirmed unchanged throughout, per the original scope guards:

- Zero-Step's derivation mechanism (Canonical §14.1–§14.2)
- S-1 Opposed Contest (Canonical §13)
- The attack-side invocation/warrant policy (Proposals §2.1A)
- Structural Weak Points' State-2 classification
- The W3 reference cache
- Tier 0/1/2 scene/campaign selection policy
- Anatomical mapping, Tier-2 mechanics, or any Wound/Armor/Effect numerical rule

---

## 7. Cross-Document Consistency

This ruling is now recorded in three places, kept synchronized:

| Document | Location | Role |
|---|---|---|
| Proposals/WIP v1.4.3 | §2.5A (new); §2.5 updated; §20 S-2 row updated; §8 cross-reference; §14 cross-reference | Authoritative non-canonical governing position |
| Implementation Roadmap v1.4.3 | §4 S-2 row; §9 Phase 2 (new subsection); §12, §13, §15, §20 cross-references | Implementation-relevant consequences |
| This document | Full record | Investigation history and reopening reference |

No Canonical Rules document is affected. Nothing in this investigation or its closure is promoted to Canonical status (Proposals §21 eight-step process not invoked).

```

