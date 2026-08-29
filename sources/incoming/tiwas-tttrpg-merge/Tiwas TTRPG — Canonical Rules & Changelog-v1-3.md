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
