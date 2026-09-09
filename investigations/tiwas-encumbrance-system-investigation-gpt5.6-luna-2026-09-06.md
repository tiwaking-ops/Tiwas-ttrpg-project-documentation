# Tiwas TTRPG — Encumbrance System Investigation Report

**Document Type:** Formal Project Investigation Report  
**Project:** Tiwas TTRPG  
**Subject:** Relative Encumbrance and Carrying Capacity  
**Status:** Investigation / Non-Canonical  
**Authority:** No canonical rule change authorised by this report  
**Author:** GPT-5.6 Luna  
**Date:** 2026-09-06  
**Target Consumer:** OpenCode / Tiwas TTRPG Project Repository  

---

# 1. Executive Summary

This investigation examined a candidate encumbrance model for Tiwas TTRPG using the following baseline:

- `bpe = 20`
- `bee = 20`
- Bodyweight ≈ `65 kg`
- Candidate carrying capacity = `20 kg`
- Clothing **does count against carrying capacity**
- Tiwas is intended to be an ultra-crunch, simulation-grade system.

The investigation first examined a proposed carrying-capacity relationship:

\[
C=\left\lfloor\frac{bpe+bee}{2}\right\rfloor
\]

For the baseline character:

\[
C=\left\lfloor\frac{20+20}{2}\right\rfloor=20\text{ kg}
\]

The resulting capacity is:

\[
\frac{20}{65}\times100=30.77\%
\]

of bodyweight.

A representative equipment calculation was then attempted using estimated masses for clothing, tools, weapons, packs, food, and water.

The resulting representative load was approximately:

\[
L=10.8\text{ kg}
\]

which represents:

\[
\frac{10.8}{20}=0.54
\]

or **54% of the candidate carrying capacity**.

The principal architectural conclusion is that Tiwas should investigate a **relative encumbrance model**, rather than a universal flat kilogram-band system.

The proposed architecture is:

\[
\boxed{
\text{Individual Capacity}
\rightarrow
\text{Actual Total Load}
\rightarrow
\text{Load / Capacity Ratio}
\rightarrow
\text{Mechanical Consequences}
}
\]

This is a **design recommendation for further investigation**, not a canonical rule.

No encumbrance thresholds, penalties, capacity formula, or other new mechanical rules are authorised by this report.

---

# 2. Investigation Scope

## 2.1 Questions Investigated

The investigation addressed:

1. Whether `bpe = 20` and `bee = 20` can reasonably produce a `20 kg` carrying capacity.
2. How much mass ordinary clothing, tools, weapons, packs, food, and water could represent.
3. Whether clothing should count against capacity.
4. Whether Tiwas should use relative rather than flat encumbrance.
5. Whether other TTRPGs use relative encumbrance systems.
6. Whether a relative system is compatible with Tiwas's attribute-derived architecture.
7. What remains unresolved before formalisation.

## 2.2 Explicit User Ruling

The following question was explicitly resolved during the investigation:

> **Does clothing count against carrying capacity?**

**Ruling: YES.**

Therefore, the total Tiwas load calculation must include clothing unless a future formally adopted rule explicitly establishes a different treatment.

---

# 3. Authority and Canonical Status

This investigation does **not** modify the Tiwas Canonical Rules.

The following items remain candidates/investigative findings:

| Element | Status |
|---|---|
| Clothing counts toward load | **User-ratified design direction** |
| Item mass represented in kg | Candidate architecture |
| Total load equals sum of component masses | Candidate architecture |
| Capacity derived from `bpe` + `bee` | Candidate |
| `C = floor((bpe + bee) / 2)` | Candidate |
| Encumbrance calculated relative to capacity | Strong candidate architecture |
| Exact encumbrance thresholds | **Undetermined** |
| Encumbrance penalties/effects | **Undetermined** |
| Bodyweight-to-capacity relationship | **Undetermined** |
| Flat universal kilogram bands | Not recommended as primary architecture |
| Any new canonical encumbrance subsystem | **Not established** |

No DEC, Canonical Rules amendment, or implementation requirement should be inferred from these findings.

---

# 4. Baseline Character

## 4.1 Defined Variables

| Variable | Definition |
|---|---|
| `bpe` | Body Power Endurance |
| `bee` | Body Endurance Endurance |
| `BW` | Bodyweight in kilograms |
| `C` | Carrying capacity in kilograms |
| `L` | Total worn/carried load in kilograms |
| `E` | Relative encumbrance ratio |

Baseline:

| Variable | Value |
|---|---:|
| `bpe` | 20 |
| `bee` | 20 |
| `BW` | ≈65 kg |
| `C` | 20 kg |

---

# 5. Candidate Carrying-Capacity Formula

The investigated candidate formula is:

\[
C=\left\lfloor\frac{bpe+bee}{2}\right\rfloor
\]

This is equivalent to taking the arithmetic mean of the two Endurance-related Body attributes, with Tiwas's mandatory round-down rule applied.

For the baseline:

\[
C=\left\lfloor\frac{20+20}{2}\right\rfloor
\]

\[
C=20\text{ kg}
\]

## 5.1 Attribute Scaling

Under this candidate:

| `bpe` | `bee` | Candidate Capacity |
|---:|---:|---:|
| 10 | 10 | 10 kg |
| 20 | 20 | 20 kg |
| 25 | 25 | 25 kg |
| 30 | 30 | 30 kg |
| 40 | 40 | 40 kg |
| 50 | 50 | 50 kg |
| 100 | 100 | 100 kg |

This produces linear scaling with the two underlying attributes.

## 5.2 Important Compatibility Observation

The candidate formula cannot simultaneously produce:

- `bpe = 20`, `bee = 20` → `20 kg`
- `bpe = 25`, `bee = 25` → `20 kg`

using the same simple proportional-average formula.

The earlier `25/25 → 20 kg` proposal used:

\[
C=\left\lfloor(bpe+bee)\times0.4\right\rfloor
\]

whereas the current `20/20 → 20 kg` proposal requires:

\[
C=\left\lfloor(bpe+bee)\times0.5\right\rfloor
\]

Therefore, these are mutually different calibration assumptions.

---

# 6. Bodyweight Relationship

With:

\[
BW\approx65kg
\]

and:

\[
C=20kg
\]

the capacity-to-bodyweight ratio is:

\[
\frac{C}{BW}\times100
=
\frac{20}{65}\times100
=
30.77\%
\]

Therefore the candidate baseline capacity is approximately:

> **30.8% of bodyweight.**

This is an observed consequence of the candidate Tiwas model.

It is **not** currently a Tiwas rule that carrying capacity must equal approximately 30% of bodyweight.

The bodyweight relationship requires independent investigation before being used as a governing constraint.

---

# 7. Load Model

Because clothing has been explicitly ruled to count, the candidate total-load model is:

\[
L=\sum_{i=1}^{n}m_i
\]

where:

- `L` = total worn/carried mass
- `m_i` = mass of individual item `i`
- `n` = number of worn/carried items.

The candidate load decomposition is:

\[
L=
L_{clothing}
+
L_{belt}
+
L_{tools}
+
L_{weapons}
+
L_{pack}
+
L_{food}
+
L_{water}
+
L_{other}
\]

This is a candidate mathematical architecture, not yet a canonical equipment rule.

---

# 8. Clothing

Clothing was treated as a real physical load rather than being mechanically excluded.

An engineering estimate used during the investigation was approximately:

| Clothing Component | Working Estimate |
|---|---:|
| Undergarment / shirt | 0.3 kg |
| Trousers / legwear | 0.6 kg |
| Tunic | 0.8 kg |
| Belt | 0.2 kg |
| Cloak / outer garment | 0.5 kg |
| Footwear | 0.8 kg |
| Miscellaneous | 0.1 kg |
| **Estimated total** | **3.3 kg** |

The investigation explicitly treated this as an **engineering estimate**, not a historically verified universal clothing mass.

A simplified representative clothing value of approximately **2.5 kg** was also used in an earlier loadout calculation.

Therefore:

> Clothing mass remains an empirical input requiring future historical/physical validation.

---

# 9. Tools

A representative working tool load was estimated at approximately **2 kg**.

Example components:

| Tool | Working Mass |
|---|---:|
| Knife | 0.1 kg |
| Small hand tool | 0.3 kg |
| Hand axe | ~1.0 kg |
| Rope | ~0.5 kg |
| Miscellaneous tools | ~0.5 kg |

These values are illustrative rather than universal equipment standards.

The investigation noted that historical axes and similar tools can have masses around the sub-kilogram to approximately kilogram range, supporting the general magnitude but not establishing exact Tiwas equipment values.

---

# 10. Weapons

The investigation examined representative historical weapon masses.

Approximate working ranges included:

| Weapon | Working Mass |
|---|---:|
| Knife | 0.1–0.3 kg |
| Club | 0.5–1.5 kg |
| Hand axe | 0.8–1.2 kg |
| One-handed sword | 1.0–1.5 kg |
| Large/two-handed sword | 2.3–3.0 kg |

A representative ordinary weapon load of approximately **1 kg** was used in the baseline load calculation.

Historical museum evidence was consulted to establish plausible magnitude.

This does **not** establish Tiwas equipment masses.

---

# 11. Pack

A small civilian pack/satchel was provisionally estimated at approximately:

\[
1.0-1.5kg
\]

A representative value of:

\[
1.0kg
\]

was used in the baseline loadout.

Modern military rucksacks were examined as an upper-bound comparison, but were explicitly recognised as inappropriate as direct values for an ordinary Tiwas peasant.

---

# 12. Food

Food is inherently time-dependent.

A provisional working model was:

| Duration | Approximate Mass |
|---|---|
| Several hours/local work | 0.25–0.5 kg |
| 1 day | ~1 kg |
| 2 days | ~2 kg |
| 3 days | ~3 kg |
| 7 days | ~7 kg |

This produced an important architectural observation:

> Food should potentially be represented as inventory mass that changes with time and consumption, rather than as a permanently fixed equipment burden.

No food-mass rule has been adopted.

---

# 13. Water

Water provides a relatively straightforward physical relationship:

\[
1L\ water\approx1kg
\]

Therefore:

| Water | Approximate Mass |
|---:|---:|
| 0.5 L | 0.5 kg |
| 1 L | 1 kg |
| 1.5 L | 1.5 kg |
| 2 L | 2 kg |
| 3 L | 3 kg |
| 4 L | 4 kg |

A representative baseline of:

\[
2L=2kg
\]

was used.

No universal Tiwas hydration requirement has been established.

---

# 14. Representative Baseline Load

An initial representative loadout was:

| Component | Mass |
|---|---:|
| Clothing | 2.5 kg |
| Belt/pouches | 0.5 kg |
| Tools | 2.0 kg |
| Weapon | 1.0 kg |
| Pack | 1.0 kg |
| Food | 1.0 kg |
| Water | 2.0 kg |
| **Total** | **10.0 kg** |

A later, more granular clothing estimate produced approximately:

| Component | Mass |
|---|---:|
| Clothing | 3.3 kg |
| Belt/pouches | 0.5 kg |
| Tools | 2.0 kg |
| Weapon | 1.0 kg |
| Pack | 1.0 kg |
| Food | 1.0 kg |
| Water | 2.0 kg |
| **Total** | **10.8 kg** |

Both values are investigative estimates.

The more granular **10.8 kg** figure was used to demonstrate the relative calculation.

---

# 15. Relative Encumbrance Calculation

The candidate relative encumbrance measure is:

\[
E=\frac{L}{C}
\]

where:

- `E` = relative encumbrance ratio
- `L` = actual total load in kg
- `C` = character-specific carrying capacity in kg.

For:

\[
L=10.8kg
\]

and:

\[
C=20kg
\]

then:

\[
E=\frac{10.8}{20}
\]

\[
E=0.54
\]

or:

\[
E=54\%
\]

Therefore:

> The representative load consumes **54% of the baseline character's candidate carrying capacity**.

---

# 16. Comparative Character Scaling

The same physical load produces different relative burdens for characters with different capacities.

Using a constant:

\[
L=10.8kg
\]

the candidate results are:

| Character | Capacity | Load | Relative Load |
|---|---:|---:|---:|
| Weak | 10 kg | 10.8 kg | 108% |
| Average | 20 kg | 10.8 kg | 54% |
| Strong | 40 kg | 10.8 kg | 27% |
| Exceptional | 80 kg | 10.8 kg | 13.5% |

This demonstrates the principal advantage of relative encumbrance.

The physical equipment remains constant:

\[
L=10.8kg
\]

while the burden changes according to the character's physical capability.

---

# 17. Alternative Load Profiles

Several representative load profiles were constructed for investigation.

| Loadout | Clothing | Tools | Weapon | Pack | Food | Water | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Local peasant | 2.5 | 1.0 | 0.2 | 0.5 | 0.5 | 1.0 | **5.7 kg** |
| Travelling civilian | 2.5 | 1.0 | 1.0 | 1.0 | 1.0 | 2.0 | **8.5 kg** |
| Adventurer baseline | 2.5 | 2.0 | 1.2 | 1.0 | 1.0 | 2.0 | **9.7 kg** |
| Well-equipped adventurer | 2.5 | 3.0 | 1.5 | 1.5 | 2.0 | 3.0 | **13.5 kg** |
| Heavy expedition | 3.0 | 4.0 | 2.5 | 2.0 | 4.0 | 4.0 | **19.5 kg** |
| Over-capacity example | 3.0 | 5.0 | 3.0 | 2.5 | 5.0 | 5.0 | **23.5 kg** |

Relative to the baseline:

\[
C=20kg
\]

these correspond to:

| Load | Capacity Utilisation |
|---:|---:|
| 5.7 kg | 28.5% |
| 8.5 kg | 42.5% |
| 9.7 kg | 48.5% |
| 13.5 kg | 67.5% |
| 19.5 kg | 97.5% |
| 23.5 kg | 117.5% |

These percentages are **analytical outputs**, not adopted encumbrance categories.

---

# 18. Relative Versus Flat Encumbrance

## 18.1 Flat System

A flat system might define:

| Load | Effect |
|---:|---|
| 0–10 kg | Light |
| 11–15 kg | Moderate |
| 16–20 kg | Heavy |
| 21–25 kg | Extreme |

The principal problem is that identical absolute loads have radically different physiological significance for characters with different capabilities.

## 18.2 Relative System

A relative system instead calculates:

\[
E=\frac{L}{C}
\]

Therefore:

| Character | Capacity | 15 kg Load | Relative Load |
|---|---:|---:|---:|
| Weak | 10 kg | 15 kg | 150% |
| Average | 20 kg | 15 kg | 75% |
| Strong | 40 kg | 15 kg | 37.5% |
| Exceptional | 80 kg | 15 kg | 18.75% |

This is substantially more compatible with Tiwas's character-specific attribute architecture.

---

# 19. External TTRPG Precedents

The investigation established that relative encumbrance is not unique to Tiwas.

## 19.1 GURPS

GURPS is the clearest identified precedent.

Its encumbrance system evaluates carried weight relative to the character's Strength/Basic Lift rather than using one universal kilogram threshold.

GURPS Lite historically defines progressively larger load multiples, producing different encumbrance levels as the character's physical capability changes.

This establishes a strong precedent for:

\[
\text{Load relative to capability}
\]

rather than:

\[
\text{Universal absolute load}
\]

Tiwas should **not copy GURPS thresholds** merely because the architecture has precedent.

## 19.2 GemStone IV

GemStone IV provides another relevant precedent.

Its encumbrance/carrying system incorporates character physical characteristics, including bodyweight and Strength-related capability, and evaluates load relative to the character.

This is conceptually close to the Tiwas investigation because the system attempts to represent:

\[
\text{Physical capability}
\rightarrow
\text{Carrying capability}
\rightarrow
\text{Actual load}
\rightarrow
\text{Encumbrance}
\]

## 19.3 RuneQuest

RuneQuest provides a contrasting model.

It commonly uses equipment ENC values and sums those values rather than directly calculating total physical kilograms relative to an individually calculated carrying capacity.

This demonstrates that an RPG can model encumbrance through an abstraction rather than direct mass.

However, this is less aligned with the current Tiwas simulation objective.

## 19.4 Mythras

Mythras also provides an equipment ENC approach, with equipment burden represented mechanically rather than requiring every effect to derive directly from kilograms.

Again, this is a useful precedent but is not identical to the candidate Tiwas architecture.

---

# 20. Architectural Finding

The investigation's strongest design finding is:

> **Tiwas should investigate encumbrance as a relative quantity derived from actual physical mass and individual carrying capability.**

The proposed architecture is:

\[
\boxed{
m_i
\rightarrow
L=\sum m_i
\rightarrow
C=f(bpe,bee)
\rightarrow
E=\frac{L}{C}
\rightarrow
\text{Mechanical Consequence}
}
\]

Where:

- `m_i` = individual item mass
- `L` = total load
- `C` = individual carrying capacity
- `E` = relative encumbrance ratio.

This separates **physical reality** from **character capability**.

---

# 21. Why This Architecture Fits Tiwas

The relative approach aligns with several existing Tiwas principles.

## 21.1 Attribute-Derived Capability

Tiwas already derives mechanical capabilities from character attributes.

A character's ability to carry weight should therefore logically vary with relevant physical attributes rather than being universally identical.

## 21.2 No Universal Character Assumption

A 10 kg load is not equally burdensome to all characters.

Relative calculation preserves this distinction.

## 21.3 Granularity

Actual physical masses can remain granular:

- clothing
- individual weapons
- individual tools
- individual food quantities
- individual water quantities
- pack mass
- carried materials
- loot
- bodies
- other physical objects.

The resulting burden can then be calculated mechanically.

## 21.4 Simulation Compatibility

The architecture supports dynamic loads.

For example:

\[
L_{new}=L_{old}+m_{item}
\]

and after consumption:

\[
L_{new}=L_{old}-m_{consumed}
\]

This allows food and water to change encumbrance as inventory changes.

---

# 22. Critical Design Distinction

The investigation identified three different concepts that should not be conflated.

| Concept | Meaning |
|---|---|
| **Mass** | Objective physical mass of an object |
| **Capacity** | Character-specific physical carrying capability |
| **Encumbrance** | Relationship between current load and capability |

Thus:

\[
Mass\neq Capacity\neq Encumbrance
\]

A sword has a mass.

A character has a carrying capacity.

The sword contributes to encumbrance according to the relationship between those quantities.

This distinction is important for maintaining mechanical clarity.

---

# 23. What Has Not Been Established

The investigation did **not** establish:

1. The final carrying-capacity formula.
2. Whether `bpe` and `bee` are the only attributes involved.
3. Whether bodyweight should explicitly enter the formula.
4. The exact meaning of `20 kg capacity`.
5. Whether capacity represents:
   - maximum sustainable load,
   - maximum functional load,
   - maximum load before mechanical impairment,
   - or another physical boundary.
6. Exact encumbrance thresholds.
7. Encumbrance penalties.
8. Whether encumbrance affects:
   - Movement Speed,
   - Speed,
   - Physical Energy,
   - skill tests,
   - recovery,
   - action economy,
   - or another subsystem.
9. Whether exceeding capacity should have one consequence or multiple escalating consequences.
10. Whether equipment bulk, volume, awkwardness, or distribution should modify a pure mass calculation.
11. Whether worn armour requires a separate interaction model.
12. Whether carrying another person should use their full bodyweight.
13. Whether carried objects can be dragged rather than lifted/carried.
14. Whether temporary loads should be treated differently.
15. Exact historical clothing/tool/weapon/food values.

These remain investigation items.

---

# 24. Important Constraint: Do Not Import Thresholds Without Validation

An earlier investigation noted conventional real-world load-carriage percentages around the approximate 30% bodyweight region.

The current baseline independently produces:

\[
20kg/65kg=30.77\%
\]

This coincidence is potentially useful evidence.

However:

> **The 30% figure must not automatically become a Tiwas rule.**

Likewise, example relative thresholds such as:

- 25%
- 50%
- 75%
- 100%
- 125%
- 150%

must not be treated as canonical merely because they provide convenient mathematical bands.

Any such threshold requires independent investigation, evidence, testing, and formal authority progression.

---

# 25. Recommended Investigation Direction

The strongest next investigation is:

## Relative Load Threshold Investigation

Determine whether real-world human load-carriage evidence supports meaningful physiological or operational transitions at particular fractions of individual carrying capability.

The investigation should examine:

1. Standing with load.
2. Walking with load.
3. Sustained walking.
4. Running/movement.
5. Climbing.
6. Combat movement.
7. Lifting.
8. Repeated exertion.
9. Fatigue.
10. Balance/stability.
11. Injury risk.
12. Recovery requirements.

The results should then be tested against multiple Tiwas characters rather than only the 20/20 baseline.

---

# 26. Required Calibration Matrix

A future investigation should test at minimum:

| Character | `bpe` | `bee` | Capacity Candidate |
|---|---:|---:|---:|
| Very low | 5 | 5 | 5 kg |
| Low | 10 | 10 | 10 kg |
| Below average | 15 | 15 | 15 kg |
| Baseline | 20 | 20 | 20 kg |
| Above average | 30 | 30 | 30 kg |
| Strong | 40 | 40 | 40 kg |
| Very strong | 60 | 60 | 60 kg |
| Exceptional | 80 | 80 | 80 kg |
| Maximum | 100 | 100 | 100 kg |

Each should then be tested against identical physical loads.

---

# 27. Required Equipment Test Matrix

A future playtest should test at least:

| Load Category | Example |
|---|---|
| Clothing | Ordinary clothing |
| Personal effects | Belt/pouches |
| Tool | Knife |
| Tool | Axe |
| Tool kit | Multiple tools |
| Weapon | Sword |
| Weapon | Heavy weapon |
| Shield | Shield |
| Pack | Empty pack |
| Pack | Loaded pack |
| Food | 1 day |
| Food | Multi-day |
| Water | 1 L |
| Water | 2 L |
| Water | 4 L |
| Armour | Light |
| Armour | Heavy |
| Trade goods | 5–20 kg |
| Loot | Variable |
| Body | Unconscious person |
| Oversized object | Awkward load |

This will determine whether a pure mass model remains sufficient.

---

# 28. Design Recommendation

Based on this investigation:

## Recommended Architecture

Investigate and, subject to validation, adopt a system where:

\[
\boxed{
\text{Total Physical Load}
\div
\text{Individual Carrying Capacity}
=
\text{Relative Encumbrance}
}
\]

with:

\[
L=\sum m_i
\]

and candidate capacity:

\[
C=\left\lfloor\frac{bpe+bee}{2}\right\rfloor
\]

The candidate relative ratio is:

\[
E=\frac{L}{C}
\]

This is the recommended **investigation architecture**, not a canonical rule.

---

# 29. Formal Findings

| ID | Finding | Status |
|---|---|---|
| ENC-F01 | Clothing counts toward total load. | **User-ratified** |
| ENC-F02 | A `bpe=20`, `bee=20` character is being investigated with a 20 kg capacity baseline. | **Investigation baseline** |
| ENC-F03 | `C=floor((bpe+bee)/2)` produces 20 kg at 20/20. | **Candidate formula** |
| ENC-F04 | The 20 kg baseline equals approximately 30.8% of a 65 kg bodyweight. | **Observed consequence** |
| ENC-F05 | Representative clothing/tools/weapon/pack/food/water load can plausibly reach approximately 10–11 kg under the working estimates. | **Engineering estimate** |
| ENC-F06 | A 10.8 kg load represents 54% of a 20 kg capacity. | **Calculated result** |
| ENC-F07 | The same physical load produces different burdens for characters with different capacities. | **Validated mathematical property** |
| ENC-F08 | Relative encumbrance is more compatible with Tiwas's attribute-derived architecture than universal flat kilogram bands. | **Design finding** |
| ENC-F09 | Relative encumbrance has established TTRPG precedents, particularly GURPS and GemStone IV. | **Research finding** |
| ENC-F10 | Exact relative encumbrance thresholds remain unresolved. | **Open** |
| ENC-F11 | Encumbrance penalties/effects remain unresolved. | **Open** |
| ENC-F12 | Bodyweight's role in the capacity formula remains unresolved. | **Open** |

---

# 30. Final Conclusion

The investigation supports a clear architectural direction:

> **Tiwas should investigate relative encumbrance rather than a universal flat kilogram encumbrance table.**

The physical model should preserve actual item mass:

\[
L=\sum m_i
\]

while the character model determines individual capacity:

\[
C=f(bpe,bee)
\]

and encumbrance is then evaluated relationally:

\[
E=\frac{L}{C}
\]

Under the current baseline:

\[
bpe=20
\]

\[
bee=20
\]

\[
C=20kg
\]

\[
BW\approx65kg
\]

and a representative fully equipped load of approximately:

\[
L=10.8kg
\]

produces:

\[
E=0.54=54\%
\]

The model therefore gives Tiwas a potentially powerful simulation architecture in which **the equipment has objective physical mass while the character's attributes determine how burdensome that mass is**.

The investigation does **not** authorise exact encumbrance bands, penalties, movement modifications, fatigue rules, or a final capacity formula.

Those require a separate evidence-backed investigation and formal Tiwas promotion process.

---

# 31. Source / Evidence Record

The external-research portion of the investigation consulted material concerning:

- GURPS Lite encumbrance and Basic Lift.
- GemStone IV encumbrance and carrying capacity.
- RuneQuest equipment ENC.
- Mythras equipment ENC.
- Historical weapon mass examples from museum collections.
- US Army load-carriage/loadout material.
- Historical and military water/load examples.

External evidence was used to establish **precedent and plausible physical magnitudes**, not to silently convert external rules into Tiwas mechanics.

The external systems' numerical thresholds are therefore **reference evidence only**.

---

# 32. Open Investigation Queue

The next formal investigation should address:

1. **ENC-I01 — Carrying Capacity Formula Validation**
2. **ENC-I02 — Bodyweight Relationship**
3. **ENC-I03 — Relative Encumbrance Thresholds**
4. **ENC-I04 — Encumbrance Mechanical Consequences**
5. **ENC-I05 — Mass Versus Bulk**
6. **ENC-I06 — Armour and Equipment Interaction**
7. **ENC-I07 — Food/Water Temporal Mass**
8. **ENC-I08 — Carrying/Dragging Other Creatures**
9. **ENC-I09 — Real-World Load-Carriage Calibration**
10. **ENC-I10 — Multi-character Simulation / Statistical Validation**

No item in this queue is authorised for implementation merely by appearing in this document.

---

# 33. Authority Statement

**This document is an investigative design report.**

It does not amend the Tiwas Canonical Rules.

The only explicit design ruling established during this chat is:

> **Clothing counts against carrying capacity.**

All other numerical formulas, masses, ratios, thresholds, categories, penalties, and architectural proposals remain **non-canonical investigation material** until subjected to the project's formal authority and promotion process.