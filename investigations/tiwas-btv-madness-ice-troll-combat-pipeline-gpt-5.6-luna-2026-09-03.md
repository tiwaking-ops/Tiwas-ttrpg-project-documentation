# Tiwas TTRPG — Beyond the Vale of Madness Creature Adaptation
## Ice Troll Combat-Pipeline Development Report

---

## 1. Document Control

| Field | Value |
|---|---|
| **Document Title** | Tiwas TTRPG — Beyond the Vale of Madness Creature Adaptation: Ice Troll Combat-Pipeline Development Report |
| **Document Type** | Formal Project Development Report |
| **Project** | Tiwas TTRPG |
| **Adaptation Target** | *Beyond the Vale of Madness* — GURPS adventure module |
| **Primary Creature** | Ice Troll |
| **Status** | **ADVISORY / NON-CANONICAL DEVELOPMENT RECORD** |
| **Author** | **GPT-5.6 Luna** |
| **Author LLM Version** | **GPT-5.6 Luna** |
| **Intended Recipient** | Claude — further Tiwas creature-development work |
| **Development Date** | 2026-09-03 |
| **Authority** | Advisory analysis only; does not amend canonical Tiwas rules |
| **Source Conversion Baseline** | Claude Sonnet 5 Ice Troll/Blood Man conversion scratch document |
| **Canonical Authority** | Existing Tiwas canonical rules and recorded Designer Decisions only |

---

# 2. Executive Summary

This report records the development made during the current Tiwas TTRPG creature-adaptation work concerning the **Ice Troll** from *Beyond the Vale of Madness*.

Claude's existing creature conversion was accepted as the **working baseline** rather than being replaced or regenerated from first principles.

The primary development objective was to determine whether the proposed Ice Troll can actually traverse the current Tiwas combat architecture and to identify the precise point at which the conversion encounters an existing Tiwas system dependency.

The investigation established the following:

1. Claude's proposed **24-attribute Ice Troll matrix is internally consistent** with the Tiwas attribute and derived-stat formulas.
2. Claude's derived statistics were independently recalculated and confirmed.
3. The proposed **Tier-2 Icy Claws and Sharktoothed Maw** construction is compatible with the existing Skill-Tier gate for anatomical Location generation.
4. The Troll's d100 roll remains its **resource expenditure**, not target damage.
5. **Attack-roll cost, Overflow damage, and target Injury are separate quantities and must not be conflated.**
6. `Inflict Injury` is an established Tiwas Effect; the corpus does **not** supply a numerical rule determining how much target HP that Effect removes.
7. The Wound pathway is substantially more completely specified than ordinary target HP Injury.
8. The Troll's GURPS **DR 2, freezing only** cannot currently be imported as numeric DR; it requires a Tiwas-compatible Armour/Tag representation.
9. Regeneration, Regrowth, conditional freezing protection, and Appearance/Fright interaction remain unresolved.
10. A complete Ice Troll combat test should therefore first use the **Wound pathway without inventing a target-damage formula**, before addressing missing Injury magnitude and creature-specific armour.

No canonical Tiwas rule has been changed by this work.

---

# 3. Scope

## 3.1 In Scope

This report covers:

- validation of Claude's Ice Troll conversion;
- validation of its 24 attributes;
- validation of derived statistics;
- validation of proposed Skill construction;
- validation of the Tier-2 attack decision;
- mapping of the Ice Troll into the current Tiwas combat pipeline;
- separation of attacker resource expenditure from target Injury;
- identification of the current Injury-magnitude boundary;
- identification of the current Armour boundary;
- identification of unresolved creature traits;
- definition of the next creature-development/testing sequence.

## 3.2 Out of Scope

This report does **not**:

- create a new Tiwas damage formula;
- create a new Armour system;
- create new Attributes;
- create new universal Skills;
- redefine S-1, S-2, S-3, S-4, S-5, S-6 or S-7;
- promote Claude's proposed creature values to canonical status;
- resolve Regeneration or Regrowth;
- resolve Fright/Appearance mechanics;
- import GURPS combat mechanics into Tiwas;
- establish a universal GURPS→Tiwas conversion formula.

---

# 4. Authority and Provenance

## 4.1 Creature Conversion Authority

The Claude creature-conversion document is explicitly an:

> Advisory scratch/editable conversion

and is not a definitive template, canonical rule, or Designer Decision.

Accordingly, its numerical creature values are treated as **proposed S-12 content**.

## 4.2 Canonical-System Authority

The current Tiwas rules remain authoritative for:

- resolution;
- Attributes;
- Skills;
- Skill Tier;
- Skill Cap;
- resource expenditure;
- Overflow;
- Effects;
- Location;
- Wounds;
- Defence;
- Armour architecture;
- Incapacitation;
- progression;
- governance.

Where creature conversion and existing Tiwas mechanics intersect, **the existing Tiwas mechanics take precedence**.

## 4.3 No Silent Rule Creation

Where the current Tiwas rules do not specify a required conversion, this report records the gap rather than creating an inferred rule.

In particular:

> **GURPS damage dice must not be silently converted into Tiwas HP damage.**

---

# 5. Ice Troll Baseline

## 5.1 Source Creature

The GURPS source provides the following Ice Troll profile:

| Property | GURPS Value |
|---|---:|
| ST | 15 |
| DX | 12 |
| IQ | 7 |
| HT | 12 |
| HP | 15 |
| Will | 11 |
| Per | 12 |
| FP | 12 |
| Speed | 6.5 |
| Move | 6 |
| DR | 2 |
| Icy Claws | 13 |
| Sharktoothed Maw | 13 |
| Brawling | 13 |
| Camouflage | 12 |
| Stealth | 10 |
| Tracking | 11 |

Source traits include:

- Sharp Claws;
- Hideous Appearance;
- Bad Temper;
- Fast Regeneration, freezing only;
- Regrowth, freezing only;
- DR 2, freezing only.

The GURPS numerical values are **source-system values**, not Tiwas targets.

---

# 6. Proposed Tiwas Attribute Matrix

Claude's proposed Ice Troll matrix remains the current working baseline.

| Code | Attribute | Value | Code | Attribute | Value |
|---|---|---:|---|---|---:|
| bpp | Might | 75 | mpp | Cunning | 45 |
| bps | Impact | 65 | mps | Wits | 30 |
| bpe | Brawn | 70 | mpe | Willpower | 55 |
| bpx | Presence | 55 | mpx | Glamour | 10 |
| bsp | Agility | 60 | msp | Acuity | 40 |
| bss | Reflexes | 55 | mss | Perception | 60 |
| bse | Quickness | 60 | mse | Alacrity | 35 |
| bsx | Grace | 20 | msx | Charm | 5 |
| bep | Toughness | 75 | mep | Focus | 45 |
| bes | Stamina | 65 | mes | Discipline | 30 |
| bee | Vitality | 80 | mee | Resolve | 50 |
| bex | Poise | 25 | mex | Composure | 15 |

### Classification

These values are:

**PROPOSED CREATURE CONTENT**

They are not:

**DERIVED GURPS→TIWAS CONVERSION VALUES.**

No locked mathematical GURPS→24-attribute mapping currently exists.

---

# 7. Derived-Statistic Validation

The proposed attributes produce the following results.

## 7.1 Definitions

Let:

- `HP` = Health Points;
- `MP` = Mental Points;
- `PE` = Physical Energy;
- `Speed` = Tiwas Speed statistic;
- `ER` = Energy Regen;
- `MR` = MP Regen;
- `MS` = Movement Speed.

The current Tiwas formulas are:

\[
HP=\sum Body\ Attributes
\]

\[
MP=\sum Mind\ Attributes
\]

\[
PE=bep+bes+bee
\]

\[
Speed=bsp+bss+bse
\]

\[
ER=bep+bes
\]

\[
MR=mep+mes
\]

\[
MS=\left\lfloor\frac{bsp+bss}{15}\right\rfloor
\]

## 7.2 Validation

| Statistic | Calculation | Result |
|---|---:|---:|
| HP | 75+65+70+55+60+55+60+20+75+65+80+25 | **705** |
| MP | 45+30+55+10+40+60+35+5+45+30+50+15 | **420** |
| Physical Energy | 75+65+80 | **220** |
| Speed | 60+55+60 | **175** |
| Energy Regen | 75+65 | **140** |
| MP Regen | 45+30 | **75** |
| Movement Speed | floor((60+55)/15) | **7** |

**Validation result: PASS.**

No derived-stat formula conflict was identified.

---

# 8. Skill Validation

## 8.1 Signature Attacks

Claude proposes:

| Skill | Tier | Underlying Attributes | Cap | Current |
|---|---:|---|---:|---:|
| Icy Claws | 2 | bsp 60 + bpp 75 | 67 | 67 |
| Sharktoothed Maw | 2 | bpp 75 + bep 75 | 75 | 75 |

The Skill Cap formula is:

\[
Cap=\left\lfloor\frac{\sum Underlying\ Attributes}{Tier}\right\rfloor
\]

Therefore:

\[
IcyClawsCap=\left\lfloor\frac{60+75}{2}\right\rfloor=67
\]

and:

\[
MawCap=\left\lfloor\frac{75+75}{2}\right\rfloor=75
\]

Both calculations are valid.

## 8.2 Current Values

The canonical Starting Value is:

\[
StartingValue=\left\lfloor\frac{Cap}{2}\right\rfloor
\]

Therefore:

| Skill | Cap | Canonical Starting Value | Proposed Current |
|---|---:|---:|---:|
| Icy Claws | 67 | 33 | 67 |
| Sharktoothed Maw | 75 | 37 | 75 |

The full-Cap current values are acceptable only as **creature-content authoring decisions**.

They must not be represented as ordinary Starting Values.

Recommended documentation label:

> `Current Skill: GM/content-author choice; not Starting Value.`

---

# 9. General Skill Validation

| Skill | Tier | Attribute | Cap | Starting Value | Proposed Current |
|---|---:|---|---:|---:|---:|
| Brawling | 1 | bpp 75 | 75 | 37 | **37** |
| Camouflage | 1 | mss 60 | 60 | 30 | **30** |
| Stealth | 1 | bse 60 | 60 | 30 | **30** |
| Tracking | 1 | mss 60 | 60 | 30 | **30** |

**Validation result: PASS.**

---

# 10. Tier-2 Attack Decision

Claude's conversion makes the signature attacks Tier 2.

This remains the preferred working construction.

The reason is mechanical:

- Tier 2 is required to access the relevant anatomical Location pathway;
- the Ice Troll's signature attacks are intended to support localized consequences;
- therefore Tier 2 provides the necessary Skill-Tier gate.

This should **not** be generalized into a universal rule that all dangerous attacks or creatures require Tier 2.

The correct classification is:

> **Ice Troll S-12 content construction using existing Skill-Tier rules.**

---

# 11. Attack Resource Transaction

This distinction is mandatory for future creature conversions.

Let:

- `R` = exact d100 attack roll;
- `PE_before` = attacker's Physical Energy before the test;
- `PE_after` = attacker's Physical Energy after the test;
- `Overflow` = resource excess converted to attacker HP damage.

For a Body-domain attack:

\[
Cost=R
\]

If:

\[
R\leq PE_{before}
\]

then:

\[
PE_{after}=PE_{before}-R
\]

If:

\[
R>PE_{before}
\]

then:

\[
Overflow=R-PE_{before}
\]

and Overflow is applied to the **attacker's HP**.

## 11.1 Example

If:

\[
PE=220
\]

and:

\[
R=42
\]

then:

\[
PE=178
\]

and:

\[
Overflow=0
\]

If instead:

\[
PE=40
\]

and:

\[
R=91
\]

then:

\[
PE=0
\]

and:

\[
Overflow=51
\]

Therefore the Troll suffers **51 HP damage** from its own resource overflow.

---

# 12. Critical Conversion Rule: Attack Cost Is Not Target Damage

The following distinction must be preserved in all future creature conversions.

| Quantity | Applies to |
|---|---|
| d100 roll | Test resolution |
| d100 result as resource cost | **Attacker** |
| Overflow | **Attacker HP** |
| Declared Effect | **Target consequence** |
| Inflict Injury | **Target HP Injury** |
| Wound | **Target localized lasting state** |

Therefore:

> An Icy Claws roll of 63 does **not** mean the target automatically takes 63 HP damage.

Likewise:

> GURPS `1d+2 cut` cannot be replaced by the d100 result without a specific Tiwas rule authorising that mapping.

This is a correction to the ambiguous statement in the original Claude conversion that described damage in terms of attack cost/Overflow plus Effect.

---

# 13. Combat Pipeline

The current working pipeline for the Ice Troll is:

```text
Icy Claws
    ↓
S-1 Opposed Contest
    ↓
Troll wins
    ↓
Declare eligible Effect
    ↓
Quality / Effect gates
    ↓
S-2 Location where required
    ↓
S-6 Active Defence
    ↓
S-5 Armour interaction
    ↓
S-4 Injury/Wound consequence
    ↓
S-7 Incapacitation / Death where applicable
```

This should be tested as a pipeline rather than by importing GURPS attack mechanics.

---

# 14. Inflict Injury Finding

## 14.1 Established

The current Tiwas rules establish:

- `Inflict Injury` as an Effect;
- Base-tier status;
- HP-only consequence;
- distinction between Injury and Wound;
- automatic application of a declared Effect after a successful contest;
- Location requirements where applicable.

## 14.2 Missing

The current supplied Tiwas corpus does **not** provide a numerical rule establishing:

> **How many target HP are removed when `Inflict Injury` successfully applies.**

This is a precise gap.

It is **not** evidence that `Inflict Injury` itself is undefined.

The correct finding is:

> **The Effect exists; its target-HP payload magnitude is not currently supplied by the available rules.**

---

# 15. Track Separation

Tiwas currently distinguishes two relevant consequence tracks.

## Track A — Resource Overflow

\[
AttackRoll > RemainingResource
\]

causes excess resource cost to become **attacker HP damage**.

## Track B — Target Effect

A successful attack may produce an Effect against the target.

These tracks must remain independent.

They must not be combined into:

> `Target Damage = Attack Roll / Cost / Overflow`

unless a future authoritative rule explicitly establishes such a relationship.

---

# 16. Wound Pathway

The Wound pathway is substantially more defined.

The current architecture establishes:

\[
WoundMagnitude=-Tier
\]

and:

> Quality is the hard ceiling on Wound Tier.

Skill Tier supplies the production gate for anatomical Location generation.

Therefore a Tier-2 Icy Claws attack is structurally capable of producing a Tier-2 Wound **if the relevant Effect and Quality requirements are satisfied**.

A representative structure is:

```text
Location X Tier-2 Wound -2 (Attribute or Skill)
```

The specific Location and affected Attribute/Skill depend on the declared Effect and resulting resolution.

---

# 17. Location Resolution

For Icy Claws:

\[
SkillTier=2
\]

Therefore the anatomical Location gate is satisfied.

The current Location architecture provides:

| Tier | Function |
|---|---|
| Tier 0 | Default/no additional anatomical granularity |
| Tier 1 | Zero-Step Location Index |
| Tier 2 | Secondary Location resolution |

The Tier-2 secondary roll does not impose an additional resource cost.

This supports Claude's decision to construct the signature attack as Tier 2.

---

# 18. Quality Constraint

Tier 2 does **not** mean that every successful Icy Claws attack automatically creates a Tier-2 Wound.

Two separate constraints must remain distinct:

### Production Gate

\[
SkillTier\geq2
\]

permits the required Location generation.

### Severity Ceiling

\[
WoundTier\leq QualityGatedEffectTier
\]

Quality therefore determines the maximum Wound tier available from the relevant successful resolution.

This distinction must be retained in future creature conversions.

---

# 19. Active Defence

The current S-6 architecture supports:

- defender Active Defence;
- voluntary defence decline;
- defence as a Core Test;
- post-hoc mitigation;
- separate mitigation for applicable Effects.

The GURPS Ice Troll's Dodge/Parry values should **not** be copied into the Tiwas creature block.

The defender uses Tiwas's own defensive mechanism.

The Ice Troll conversion therefore does not need a GURPS-style:

> Dodge 9

or:

> Parry 10

stat.

---

# 20. Armour Boundary

The GURPS source provides:

> **DR 2, freezing only.**

This cannot currently be converted to:

> `DR 2`

inside the Tiwas creature block.

Current Tiwas Armour architecture is Tag/Traits based rather than a GURPS numeric DR pool.

Therefore the Ice Troll requires a future or existing Tiwas Armour Tag that can express its conditional freezing protection.

Until such a Tag/mechanism is established:

> **Do not invent a numeric DR translation.**

Recommended status:

**Design-Stage Dependency / Adaptation Mapping Required.**

---

# 21. Other Unresolved Traits

| GURPS Trait | Tiwas Status | Required Treatment |
|---|---|---|
| Sharp Claws | Provisional `damage:slashing` mapping | Retain provisionally |
| Bad Temper | Behavioural | Retain as creature behaviour |
| Hideous Appearance | No established Fright/reaction mechanism | Flag unresolved |
| Fast Regeneration, freezing only | No established equivalent | Flag unresolved |
| Regrowth, freezing only | No established equivalent | Flag unresolved |
| DR 2, freezing only | No concrete Tiwas equivalent | Flag unresolved |

No new universal mechanics should be created inside the creature conversion to solve these.

---

# 22. Behavioural Conversion

The source Ice Troll behaviour can be retained as **creature-specific behaviour**.

| Trigger | Working Tiwas Behaviour |
|---|---|
| Encounter | Rush opponent |
| Normal combat | Use Icy Claws and/or Sharktoothed Maw |
| HP reaches 0 | Apply existing Tiwas incapacitation state |
| Source retreat/fight decision | Preserve as creature-specific decision |
| Retreat result | Retreat through tunnel |
| Fight-to-death result | Continue combat |
| Fight-to-death attack behaviour | Use both claws without importing GURPS action-economy terminology |

The GURPS "All-Out Attack" rule should not be imported as a universal Tiwas action rule.

Only the creature's observed/source behaviour should be retained.

---

# 23. First Integrated Test Recommended

The first executable test should **not** attempt to solve every unresolved creature trait.

Use a controlled test:

### Test Objective

Validate:

\[
S\text{-}1
\rightarrow
S\text{-}3
\rightarrow
S\text{-}2
\rightarrow
S\text{-}6
\rightarrow
S\text{-}4
\rightarrow
S\text{-}7
\]

while deliberately excluding unresolved S-5 armour content.

### Test Conditions

1. Ice Troll uses Icy Claws 67.
2. Troll has PE = 220.
3. Defender has a fully specified Tiwas defensive profile.
4. Defender has no armour for the first test.
5. Attack roll is recorded.
6. PE cost is applied exactly.
7. S-1 determines contest outcome.
8. On Troll win, declare a legal Effect.
9. Quality is recorded.
10. Tier-2 Location is generated where required.
11. S-6 Active Defence is resolved.
12. Resulting Wound/Effect consequence is recorded.
13. HP/incapacitation consequences are recorded where applicable.
14. No missing HP-damage formula is invented.

---

# 24. Second Integrated Test

After the first pipeline succeeds:

### Test Objective

Add the Ice Troll's conditional freezing protection.

Pipeline:

\[
S\text{-}1
\rightarrow
S\text{-}3
\rightarrow
S\text{-}2
\rightarrow
S\text{-}6
\rightarrow
S\text{-}5
\rightarrow
S\text{-}4
\rightarrow
S\text{-}7
\]

This test should not proceed until a valid Tiwas representation of:

> **DR 2, freezing only**

exists.

---

# 25. Injury-Magnitude Development Boundary

The missing target-HP Injury magnitude should be treated as a **Tiwas engine/adaptation boundary**, not as a hidden property of the Ice Troll.

The creature conversion should not decide among possibilities such as:

- attack roll = damage;
- Skill Margin = damage;
- Quality = damage;
- GURPS damage dice converted directly;
- fixed creature damage;
- Attribute-derived damage;

unless an authoritative Tiwas decision establishes one.

Any such choice requires explicit project authority.

---

# 26. Current Ice Troll Readiness Matrix

| Component | Status |
|---|---|
| 24 Attributes | **Provisional / usable** |
| Derived Statistics | **Validated** |
| General Skills | **Validated** |
| Icy Claws | **Provisional / mechanically compatible** |
| Sharktoothed Maw | **Provisional / mechanically compatible** |
| Tier-2 construction | **Compatible with Location gate** |
| PE expenditure | **Defined** |
| Overflow | **Defined** |
| S-1 | **Available for testing** |
| S-3 Effects | **Available structurally** |
| S-2 Location | **Available** |
| S-4 Wound architecture | **Defined structurally** |
| Wound magnitude | **Defined** |
| S-6 Defence | **Available structurally; integrated test required** |
| S-5 Armour | **Concrete Ice Troll mapping unavailable** |
| Target HP Injury magnitude | **Not supplied** |
| Regeneration | **Unresolved** |
| Regrowth | **Unresolved** |
| Conditional freezing protection | **Unresolved** |
| Appearance/Fright | **Unresolved** |
| Creature behaviour | **Usable as provisional content** |
| Fully executable encounter creature | **NOT YET** |

---

# 27. Development Conclusions

## Finding F-01 — Claude's Attribute Baseline Is Retained

**Decision:** Retain Claude's proposed 24-attribute Ice Troll matrix as the current working baseline.

**Classification:** Provisional S-12 content.

**Reason:** Internally coherent and compatible with Tiwas derived-stat formulas.

---

## Finding F-02 — Derived Statistics Validate

**Decision:** No changes required.

**Result:**

- HP = 705
- MP = 420
- Physical Energy = 220
- Speed = 175
- Energy Regen = 140
- MP Regen = 75
- Movement Speed = 7

---

## Finding F-03 — Tier-2 Signature Attacks Retained

**Decision:** Retain Tier 2 for Icy Claws and Sharktoothed Maw.

**Reason:** Existing anatomical Location gating supports the construction.

**Constraint:** This remains creature content, not a universal creature-design rule.

---

## Finding F-04 — Attack Cost Must Not Be Treated as Target Damage

**Decision:** Correct the conversion methodology.

**Rule:**

\[
AttackRoll=ResourceCost
\]

not:

\[
AttackRoll=TargetDamage
\]

Overflow damages the attacker, not the target.

---

## Finding F-05 — Inflict Injury Payload Is a Current Boundary

**Decision:** Do not invent a target HP damage formula.

**Finding:** `Inflict Injury` exists, but its numerical target-HP magnitude is not supplied by the currently available Tiwas rules.

---

## Finding F-06 — Wound Pathway Is Suitable for Immediate Testing

**Decision:** Use the Wound pathway as the first integrated creature-combat test.

**Reason:** Location, Wound Tier and Wound Magnitude are sufficiently specified to test the architecture without inventing an Injury-damage formula.

---

## Finding F-07 — Ice Troll Freezing DR Remains Unresolved

**Decision:** Do not translate GURPS DR 2 numerically.

**Required future work:** Establish or identify the appropriate Tiwas Armour/Tag representation.

---

## Finding F-08 — GURPS Traits Must Remain Separated from Tiwas Mechanics

**Decision:** Preserve unresolved traits as explicit adaptation flags rather than silently creating mechanics.

---

# 28. Recommended Next Work for Claude

Claude should use this report as the current development boundary and proceed in the following order.

## Priority 1 — Execute Controlled Ice Troll Wound Test

Construct a fully specified Tiwas defender and execute:

\[
IcyClaws
\rightarrow
S\text{-}1
\rightarrow
Effect
\rightarrow
S\text{-}2
\rightarrow
S\text{-}6
\rightarrow
S\text{-}4
\]

Do not invent target HP Injury magnitude.

## Priority 2 — Record Every Integration Failure

For each step, record:

| Field | Requirement |
|---|---|
| Rule invoked | Exact Tiwas rule |
| Input | Exact numerical/state input |
| Roll | Exact d100 result |
| Resource cost | Exact roll value |
| Effect | Exact declared Effect |
| Quality | Exact result/method |
| Location | Exact Location result |
| Defence | Exact defence result |
| Mitigation | Exact mitigation |
| Wound | Exact resulting Wound |
| Missing rule | Explicitly identified |
| Authority required | Yes/No |

## Priority 3 — Isolate S-5

Determine precisely what existing Tiwas Armour content can represent:

> **Ice Troll — freezing-only DR 2**

without inventing numeric DR.

## Priority 4 — Isolate Injury Magnitude

Treat target HP Injury magnitude as a separate engine/adaptation investigation.

Do not solve it inside the Ice Troll stat block.

## Priority 5 — Return to Creature Completeness

Only after the combat pipeline is validated should the following be addressed:

1. Regeneration;
2. Regrowth;
3. freezing-only protection;
4. Appearance/Fright;
5. final creature presentation.

---

# 29. Non-Canonical Status Statement

This entire report is advisory.

Nothing in this document:

- modifies canonical Tiwas rules;
- creates a new Designer Decision;
- promotes Claude's creature attributes to canonical content;
- authorises a new damage formula;
- authorises a new Armour mechanic.

Any future system-level change identified during testing must proceed through the project's established governance/promotion process.

---

# 30. Handoff Statement for Claude

**Claude should treat this report as the current working baseline for further Ice Troll and subsequent creature development.**

The principal methodological rule is:

> **Adapt creatures to the existing Tiwas engine; do not silently adapt the Tiwas engine to make the creature work.**

Where the existing engine is sufficient, execute and document the conversion.

Where the engine is insufficient, isolate and report the dependency.

Where creature-specific content is required, mark it as provisional S-12 content.

Where a universal mechanical rule would be required, stop the creature conversion at that boundary and escalate the issue through the appropriate Tiwas design process.

---

## 31. Final Status

**Ice Troll Conversion: PROVISIONALLY VALIDATED AT STAT-BLOCK LEVEL; COMBAT-PIPELINE VALIDATION IN PROGRESS.**

The next authoritative development target is the **controlled Tier-2 Icy Claws → Wound combat test**, followed by isolated resolution of the S-5 Armour and target-Injury-magnitude dependencies.