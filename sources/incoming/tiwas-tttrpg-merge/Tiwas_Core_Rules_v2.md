# Tiwas — Core Rules (v2, Disambiguated)

**Status:** This document supersedes v1 for every point listed in the Changelog below. It resolves all
ambiguities raised across three independent audits (Perplexity, GPT-5.5-xhigh, GLM-5V-Turbo) and one
human meta-review. Nothing in this document invents new subsystems — combat, opposed tests, death,
equipment, magic, and GM procedure remain explicitly **Reserved / Not Yet Defined** (Section 9). This
document only closes gaps in the existing engine.

---

## 0. Changelog — Ambiguities Closed in v1

| # | Prior Ambiguity | Ruling (see relevant section) |
|---|---|---|
| 1 | Die range / meaning of "00" | §1 |
| 2 | Doubles list completeness | §1, §7 |
| 3 | Tier ≥2 cap formula | §4.2 |
| 4 | Advanced Skill cap recomputation | §7.3 |
| 5 | Skill Roll Pool persistence | §6.2 |
| 6 | Cascading vs. Cap | §6.3 |
| 7 | Skill-0 free increment | §6.4 |
| 8 | Fractional recovery rounding | §3, §5 |
| 9 | Recovery timing & clamping | §5 |
| 10 | Advanced Skill creation timing | §7.2 |
| 11 | Duplicate attributes in one formula | §7.4 |
| 12 | Duplicate Advanced Skills | §7.4 |
| 13 | Mixed-domain Advanced Skills, resource type | §7.5 |
| 14 | Maximum Tier | §7.6 |
| 15 | "Cap purchase" mechanic | §8.2 |
| 16 | Above-cap General XP procedure | §8.2 |
| 17 | Upper bound on advancement | §8.3 |
| 18 | Guaranteed success at high skill | §1 |
| 19 | Status of combat/magic/equipment/etc. | §9 |

---

## 1. Dice & Resolution

| Term | Definition |
|---|---|
| **d100** | A percentile roll producing an integer in **[1, 100]**. Physical percentile dice display the maximum result as "00"; this is read as the value **100**, never as 0. |
| **Resolution** | Success if `roll ≤ Skill`. Failure otherwise. |
| **The 100-Fumble (mandatory override)** | A roll of 100 is **always** a Failure, regardless of Skill value (even if Skill ≥ 100), and is **always** treated as a Double (Rule §7). This overrides the plain roll-under comparison. |
| **Consequence** | No Skill value, however high, ever produces a 100%-reliable test. A guaranteed minimum 1% Failure/Fumble rate exists at every Skill level. |
| **Rounding** | All fractional results round down (floor), globally, with no exceptions. |

### 1.1 Doubles (canonical list)
```
11, 22, 33, 44, 55, 66, 77, 88, 99, 100
```
Ten values (10% of the roll space). A Double only produces its special effects (Advanced Skill
eligibility) **when it is also a Failure** — see §7.1. Note that 100 is *always* a qualifying failed
double (per §1's mandatory override); the other nine qualify only when `Double > Skill`.

---

## 2. 24-Attribute Matrix

Each of the 24 attributes is generated independently: `Attribute ~ 1d100`, i.e. an integer in [1, 100].
No rule elsewhere alters this generation range — advancement (§8) is the only way attributes exceed 100.

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

Every attribute belongs to exactly one Domain: **Body** (bpp–bex, 12 attributes) or **Mind** (mpp–mex,
12 attributes). Domain is fixed and never changes.

---

## 3. Derived Statistics

| Stat | Formula | Notes |
|---|---|---|
| Health Points (HP) | Σ (all 12 Body attributes) | |
| Mental Points (MP) | Σ (all 12 Mind attributes) | |
| Physical Energy (max) | bep + bes + bee | Body test resource pool max |
| Mind Points (max, resource) | Σ (all 12 Mind attributes) | Mind test resource pool max — identical to MP; MP is both the vitality-style total *and* the Mind resource pool. This is a deliberate identity, not a naming conflict: Mind actions draw from the same total that also represents mental resilience. |
| Speed | bsp + bss + bse | |
| Energy Regen | bep + bes | |
| MP Regen | mep + mes | |
| Movement Speed | floor((bsp + bss) / 15) | |

All of the above are **live-recalculated** from current attribute values at all times — they are never
stored as frozen snapshots. If an attribute changes via General XP (§8), every derived stat that uses it
changes immediately and automatically, including all Skill Caps (§4.2) built from it.

---

## 4. Skills

### 4.1 Skill Tier
Tier = the number of distinct attributes used in a skill's cap formula. A Tier-1 skill uses exactly one
attribute; a Tier-*T* skill uses exactly *T* attributes.

**Rule:** No attribute may appear more than once within a single skill's formula. This bounds the
maximum possible Tier at 24 (one skill could theoretically incorporate every attribute in the game).

### 4.2 Skill Cap
```
Cap = floor( (A1 + A2 + ... + AT) / T )
```
This is the **floored average** of the skill's underlying attributes, applied identically at every Tier
(Tier 1 through Tier 24). Increasing Tier does not, by itself, raise a skill's expected cap — it averages
across more attributes and reduces variance, nothing more. This is intentional and confirmed, not a bug.

### 4.3 Starting Value
```
Starting Value = floor(Cap / 2)
```
This applies to Tier-1 skills exactly as written. (Advanced Skill starting values use a different rule —
see §7.3.) A skill can validly start at 0 (when its sole attribute is 1); see §6.4 for the consequence.

---

## 5. Test Resolution Procedure (canonical order of operations)

Every skill test — Body or Mind, Tier-1 or Advanced — resolves in this exact order:

1. **Roll** 1d100.
2. **Determine domain** (Body → Physical Energy; Mind → MP) from the skill being tested (§7.5 for
   Advanced Skills spanning domains).
3. **Determine outcome:** Success if `roll ≤ Skill`, **unless** roll = 100, which is always Failure
   (§1).
4. **Apply Cost** = the numeric roll, to the relevant resource pool:
   - If the pool has enough remaining, subtract the cost.
   - If not, the pool floors at 0 and the shortfall (`Overflow = cost − remaining`) becomes direct HP
     damage.
5. **If Failure:** compute Failure XP (§6.1) and, if the roll is a qualifying Double, resolve Advanced
   Skill creation (§7).
6. **Recovery (always last, always applied):** regardless of success/failure/overflow, recover
   `floor(Regen / 2)` to the same pool that was just spent, **clamped** so the pool never exceeds its
   formula-defined maximum (§3).

Recovery is unconditional — it happens after every test of every kind, including tests that caused HP
overflow.

---

## 6. Failure XP & the Skill Roll Pool

### 6.1 Failure XP
```
Failure XP = max(0, roll − Skill)
```
The `max(0, …)` clamp exists specifically for the 100-Fumble case: if Skill ≥ 100 and the mandatory
Fumble forces a Failure on a roll of 100, `100 − Skill` could be zero or negative; XP is 0 in that case,
never negative. In all ordinary failures (roll > Skill), this clamp has no effect and XP = roll − Skill
as originally defined.

### 6.2 Skill Roll Pool — Temporary, Not Persistent
**Ruling (resolves the single most-flagged ambiguity across all audits):** The Skill Roll Pool is
generated fresh from each individual failed roll and is fully resolved (spent and/or dumped to General
XP) within that same test. **Nothing carries over between tests.** A skill does not accumulate partial
progress toward its next increase across multiple failures.

### 6.3 Cascading, and the Cap Ceiling
Within a single failure's pool:
```
pool = Failure XP
while pool ≥ current Skill AND current Skill < Cap:
    pool -= current Skill
    Skill += 1
```
**The loop also stops if Skill reaches Cap**, even if pool XP remains. Natural (failure-XP-driven)
advancement can never push a skill above its own Cap. Any XP left in the pool when the loop ends
(whether because it can't afford the next level, or because Cap was reached) moves to **General XP**
in full (§8).

### 6.4 Skill Value 0 (confirmed intentional)
If Skill = 0, the cost to reach 1 is `Cost = current value = 0`. Any nonzero Failure XP pool therefore
advances a Skill-0 to at least 1 for free on the very next failed test. This is RAW, not an exploit to
be patched — it reflects "total incompetence advances fastest."

---

## 7. Doubles & Advanced Skills

### 7.1 Trigger
A Double (§1.1) triggers Advanced Skill eligibility **only when it is also a Failure.** For the nine
digit-doubles (11–99), this requires `Double > Skill`. For 100, the mandatory Fumble (§1) means it
always qualifies, at any Skill value.

### 7.2 Timing
Construction is **automatic and immediate** at the moment of the qualifying failed double — resolved as
part of that same test, not deferred to later or left as a banked "opportunity."

### 7.3 Construction Procedure
1. New Skill's Tier = failed Skill's Tier + 1.
2. Player selects one additional attribute **not already present** in the failed Skill's formula
   (§4.1's no-duplicates rule applies).
3. New Cap is computed from scratch using the **full new attribute set** (old formula's attributes +
   the newly added one), via the standard Cap formula (§4.2) at the new Tier — it is never derived by
   adjusting the old Cap.
4. Starting Value: player's choice of either **1**, or **roll 1d100 and take `min(roll, new Cap)`** as
   the starting value. (This reuses the game's only die type rather than introducing a new one.)

### 7.4 Duplicate Restrictions
- An attribute may not appear twice in one skill's formula (§4.1).
- The **same** Advanced Skill (identical base skill + identical added attribute) may not be created
  twice. If a later failed double on the same base skill has no remaining valid attribute to add
  (all have already been used across that skill's existing Advanced Skill lineage), no new skill is
  created; the Failure XP from that roll still applies normally via §6.

### 7.5 Resource Type of Advanced Skills
An Advanced Skill's resource type (Physical Energy vs. MP) is fixed by its **original Tier-1 lineage's
Domain**, not by which attributes (Body or Mind) were later added to its formula. A Body-rooted Advanced
Skill always costs Physical Energy on tests, even if a Mind attribute was added to its cap formula, and
vice versa.

### 7.6 No Maximum Tier
Any skill — including an Advanced Skill — can itself spawn a further Advanced Skill on its own failed
double, following the same procedure. There is no fixed Tier ceiling other than the natural limit of 24
(one skill cannot incorporate more attributes than exist).

---

## 8. Experience & Progression

### 8.1 General XP Pool
Receives: (a) any Skill Roll Pool remainder after §6.3 resolves, and (b) quest/GM-awarded XP.

### 8.2 Spending General XP
| Target | Cost | Notes |
|---|---|---|
| Raise an Attribute by 1 | current Attribute value | No separate "Cap purchase" mechanic exists — Caps are never bought directly (§3). Raising an Attribute automatically and immediately live-recalculates every Skill Cap built from it. |
| Raise a Skill by 1 | current Skill value | Uses the **same rule** whether the Skill is below, at, or above its Cap. General XP is the only mechanism that can push a Skill above its Cap; the Skill Roll Pool (§6.3) cannot. |

Partial increases are forbidden: General XP must cover the full cost of a step, or the increase is not
made.

### 8.3 No Upper Bound
The 1–100 range applies **only** to initial attribute generation (§2). Once advancement (via General XP
or, for Skills, the Skill Roll Pool up to Cap) begins, there is no fixed ceiling on Attribute or Skill
values. Skills above 100 remain subject to the mandatory 100-Fumble (§1) and therefore never reach
literal 100% reliability.

---

## 9. Explicitly Reserved / Not Yet Defined

The following are **not ambiguities in the existing text** — they are subsystems the current
documentation does not yet address at all. They are listed here so future audits correctly classify
them as *reserved scope*, not as defects of the engine defined above:

- Opposed tests / contested rolls
- Combat (attack, defence, initiative procedure, weapons, armour)
- Damage beyond Overflow-to-HP, healing, incapacitation, and death thresholds
- Rest action (duration, safety, action economy)
- Equipment, encumbrance, wealth/economy
- Conditions/status effects
- Environmental hazards
- Magic / special-ability construction
- NPC/enemy generation, encounter design
- Difficulty modifiers, task adjudication (e.g. "does a test require meaningful uncertainty")
- GM procedure and campaign-scale progression

No mechanic in this document should be read as implying a resolution to any item above. These remain
open for a dedicated future design phase.
