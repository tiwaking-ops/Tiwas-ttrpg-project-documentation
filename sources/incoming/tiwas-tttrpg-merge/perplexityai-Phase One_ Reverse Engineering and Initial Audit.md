<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Phase One: Reverse Engineering and Initial Audit

## 1. Executive Summary

Tiwas currently has a coherent **d100 roll-under engine** built around three linked ideas:

1. Characters are defined by 24 randomly generated Body and Mind attributes.
2. Skills are derived from attributes and improve primarily through failure.
3. Every test has a resource cost equal to the d100 result, creating a direct relationship between probability, exertion, failure, and advancement.

The strongest design characteristic is the system’s explicit **failure-forward progression loop**: failure produces XP, while high rolls are both more likely to fail and more expensive. This creates a distinctive risk–reward economy rather than a conventional “success always improves the character” structure.

The most serious current issues are not necessarily flaws in the concept, but unresolved rules that prevent reliable play:

- The exact legal range of attributes is unclear because the document says “rolling 1d100” but does not define whether 00 is possible or whether results are 1–100.
- Tier 2 and higher skills are not formally bounded.
- Physical Energy and MP recovery are ambiguous when the “half Regen” value is fractional.
- The XP cascading procedure is underspecified at skill value 1 and when a skill reaches or exceeds its cap.
- There is no complete opposed-test, combat, damage, defence, healing, death, equipment, condition, magic, NPC, or GM procedure framework.
- The action-cost rule makes a roll of 100 maximally expensive even though it always fails under ordinary roll-under rules.

The current audit supports several high-confidence conclusions:

- Assuming attributes are uniformly distributed from 1–100, expected HP and MP are both 606.
- Expected Physical Energy is 151.5, while expected Speed is also 151.5.
- Expected Movement Speed is approximately 6.27 squares per round.
- Failure XP declines sharply as skill increases.
- A failed double becomes progressively less likely as skill rises and is impossible at skill 99.
- Attributes contributing to multiple derived statistics—especially `bep`, `bes`, `mep`, and `mes`—are disproportionately valuable.

These findings should guide later combat and resource design, but they do not by themselves justify changing any existing rule.

***

## 2. Formal Existing Specification

The following records the rules stated in the supplied documentation without adding new mechanics.

### 2.1 Rule register

| ID | Rule | Formula / Procedure | Inputs | Outputs | Status |
| :-- | :-- | :-- | :-- | :-- | :-- |
| R01 | Resolution | Roll d100; succeed if roll ≤ skill value | d100, skill | Success/failure | Explicit |
| R02 | Rounding | Round all fractional calculations down | Fractional result | Integer | Explicit |
| R03 | Skill tier | Tier equals number of base attributes used by skill cap | Skill definition | Tier | Explicit |
| R04 | Attribute generation | Roll 1d100 for each of 24 attributes | 24 d100 rolls | Attribute matrix | Explicit, range ambiguity |
| R05 | Failure XP | XP = roll − current skill value | Roll, skill value | XP | Explicit |
| R06 | Skill Roll Pool | Failure XP is immediately applied to the failed skill | Failure XP | Skill advancement | Explicit |
| R07 | Skill advancement | Increasing a skill by 1 costs XP equal to current value | Current skill | New skill value | Explicit |
| R08 | Cascading | If the temporary pool can pay for multiple increases, apply them immediately | Skill Roll Pool | Multiple skill increases | Explicit, edge ambiguity |
| R09 | General XP | Any remaining temporary XP moves to General XP | Remaining XP | General XP | Explicit |
| R10 | General advancement | General XP may improve attributes or skills at current-value cost | General XP, target value | Increased attribute/skill | Explicit |
| R11 | Cap increase | General XP can increase skill caps | General XP, skill cap | Higher cap | Explicit but cost procedure unclear |
| R12 | Above-cap skills | General XP can raise a skill above its maximum cap | General XP, skill | Skill above cap | Explicit |
| R13 | Advanced Skill trigger | A failed roll of 11, 22, 33 … 99 creates an Advanced Skill | Failed double | New skill | Explicit; 00 excluded unless later changed |
| R14 | Advanced Skill tier | New skill is one tier higher than tested skill | Tested skill tier | New tier | Explicit |
| R15 | Advanced Skill construction | Add one additional attribute to the failed skill’s formula | Existing formula, selected attribute | New skill cap | Explicit |
| R16 | Advanced Skill starting value | Start at 1 or roll a die up to the new cap | New cap | Starting skill | Explicit |
| R17 | Body resource | Body skill tests spend Physical Energy equal to roll | Body skill, roll | Energy expenditure | Explicit |
| R18 | Mind resource | Mind skill tests spend MP equal to roll | Mind skill, roll | MP expenditure | Explicit |
| R19 | Overflow | Cost exceeding current resource becomes direct HP damage | Cost, current resource | HP damage | Explicit |
| R20 | Automatic recovery | Recover half the respective Regen stat immediately after a test | Regen stat | Energy/MP recovery | Explicit, fractional ambiguity |
| R21 | Rest | Full recovery requires a Rest action | Rest | Resource recovery | Explicit, procedure missing |

### 2.2 Attribute matrix

All 24 attributes are generated independently, according to the supplied documentation.


| Code | Animal | Category | Tier 1 skill |
| :-- | :-- | :-- | :-- |
| `bpp` | Bear | Body Power Power | Might |
| `bps` | Tiger | Body Power Speed | Impact |
| `bpe` | Elephant | Body Power Endurance | Brawn |
| `bpx` | Dragon | Body Power Social | Presence |
| `bsp` | Hawk | Body Speed Power | Agility |
| `bss` | Rat | Body Speed Speed | Reflexes |
| `bse` | Horse | Body Speed Endurance | Quickness |
| `bsx` | Monkey | Body Speed Social | Grace |
| `bep` | Badger | Body Endurance Power | Toughness |
| `bes` | Wolf | Body Endurance Speed | Stamina |
| `bee` | Ox | Body Endurance Endurance | Vitality |
| `bex` | Dog | Body Endurance Social | Poise |
| `mpp` | Stag | Mind Power Power | Cunning |
| `mps` | Snake | Mind Power Speed | Wits |
| `mpe` | Rooster | Mind Power Endurance | Willpower |
| `mpx` | Fox | Mind Power Social | Glamour |
| `msp` | Bat | Mind Speed Power | Acuity |
| `mss` | Cat | Mind Speed Speed | Perception |
| `mse` | Rabbit | Mind Speed Endurance | Alacrity |
| `msx` | Otter | Mind Speed Social | Charm |
| `mep` | Crane | Mind Endurance Power | Focus |
| `mes` | Goat | Mind Endurance Speed | Discipline |
| `mee` | Owl | Mind Endurance Endurance | Resolve |
| `mex` | Pig | Mind Endurance Social | Composure |

A Tier 1 skill appears to be associated one-to-one with a single attribute, but the document does not explicitly state the Tier 1 cap formula in a separate rule. The general cap rule implies:

$$
\text{Tier 1 Skill Cap} = \text{underlying attribute}
$$

and the starting value is:

$$
\text{Starting Skill} = \left\lfloor \frac{\text{Skill Cap}}{2} \right\rfloor
$$

### 2.3 Derived statistics

Let the 12 Body attributes be $B_i$, and the 12 Mind attributes be $M_i$.

$$
HP=\sum B_i
$$

$$
MP=\sum M_i
$$

$$
Physical\ Energy=bep+bes+bee
$$

$$
Speed=bsp+bss+bse
$$

$$
Energy\ Regen=bep+bes
$$

$$
MP\ Regen=mep+mes
$$

$$
Movement\ Speed=
\left\lfloor \frac{bsp+bss}{15} \right\rfloor
$$

The documentation states that HP represents physical vitality, while MP is the resource used by Mind skills. Physical Energy fuels Body skills.

***

## 3. Mathematical Audit

The calculations below assume the most natural interpretation of “1d100” for a roll-under system:

$$
X\sim Uniform\{1,2,\ldots,100\}
$$

This is an assumption for analysis, not a modification of the rules.

### 3.1 Individual attributes

For one uniformly generated attribute:

$$
E[X]=50.5
$$

$$
Var(X)=\frac{100^2-1}{12}=833.25
$$

$$
SD(X)\approx28.87
$$

Range:

$$
1\le X\le100
$$

Probability of an attribute at or above a threshold $t$:

$$
P(X\ge t)=\frac{101-t}{100}
$$

Examples:

- $P(X\ge90)=11\%$
- $P(X\ge95)=6\%$
- $P(X=100)=1\%$
- $P(X\le10)=10\%$


### 3.2 Body and Mind totals

Each total is the sum of 12 independent attributes.

$$
E[HP]=E[MP]=12(50.5)=606
$$

$$
Var(HP)=Var(MP)=12(833.25)=9999
$$

$$
SD(HP)=SD(MP)\approx100
$$

Legal ranges:

$$
12\le HP\le1200
$$

$$
12\le MP\le1200
$$

The calculated Body distribution has approximately:


| Percentile | Body or Mind total |
| --: | --: |
| 1st | 376 |
| 50th | 606 |
| 99th | 836 |

The distribution is approximately bell-shaped because it is a sum of 12 uniform variables, although the exact distribution is discrete and bounded.

### 3.3 Physical Energy, Speed, and regeneration

Physical Energy uses three attributes:

$$
Physical\ Energy=bep+bes+bee
$$

Therefore:

$$
E[Physical\ Energy]=3(50.5)=151.5
$$

$$
SD(Physical\ Energy)=\sqrt{3(833.25)}\approx50
$$

Range:

$$
3\le Physical\ Energy\le300
$$

Speed has the same structure:

$$
Speed=bsp+bss+bse
$$

Therefore:

$$
E[Speed]=151.5
$$

$$
SD(Speed)\approx50
$$

Range:

$$
3\le Speed\le300
$$

Energy Regen uses two attributes:

$$
Energy\ Regen=bep+bes
$$

$$
E[Energy\ Regen]=101
$$

$$
SD(Energy\ Regen)=\sqrt{2(833.25)}\approx40.82
$$

Range:

$$
2\le Energy\ Regen\le200
$$

MP Regen has the same distribution:

$$
MP\ Regen=mep+mes
$$

$$
E[MP\ Regen]=101
$$

$$
SD(MP\ Regen)\approx40.82
$$

### 3.4 Movement Speed

Movement Speed is:

$$
M=\left\lfloor\frac{bsp+bss}{15}\right\rfloor
$$

The unrounded numerator has expected value:

$$
E[bsp+bss]=101
$$

The exact expected rounded result is approximately:

$$
E[M]\approx6.27
$$

Calculated distribution summary:


| Statistic | Movement Speed |
| :-- | --: |
| Minimum | 0 |
| Maximum | 13 |
| Mean | 6.27 |
| Standard deviation | 2.74 |
| 1st percentile | 1 |
| Median | 6 |
| 99th percentile | 12 |

The maximum is 13 rather than 14 because the maximum numerator is 200 and:

$$
\left\lfloor \frac{200}{15}\right\rfloor=13
$$

#### Ambiguity

The formula is written as:

> Sum of `(bsp + bss) / 15`

This could mean either:

$$
\left\lfloor \frac{bsp+bss}{15}\right\rfloor
$$

or:

$$
\left\lfloor \frac{bsp+bss}{15}\right\rfloor
$$

with rounding applied at some later stage. Since the global rule says all fractional math is rounded down, the first interpretation is the most direct.

***

## 4. Skill Mathematics

### 4.1 Roll-under success

For skill value $s$, assuming $1\le s\le100$:

$$
P(\text{success})=\frac{s}{100}
$$

$$
P(\text{failure})=\frac{100-s}{100}
$$

The result at exactly the skill value succeeds.

Examples:


| Skill | Success | Failure |
| --: | --: | --: |
| 10 | 10% | 90% |
| 25 | 25% | 75% |
| 50 | 50% | 50% |
| 75 | 75% | 25% |
| 90 | 90% | 10% |
| 99 | 99% | 1% |
| 100 | 100% | 0% |

### 4.2 Skill caps

For a skill using $T$ attributes:

$$
Cap=\left\lfloor\frac{A_1+A_2+\cdots+A_T}{T}\right\rfloor
$$

The supplied wording says “the sum of its underlying attributes divided by its Tier.” Thus:

- Tier 1 cap = one attribute.
- Tier 2 cap = average of two attributes.
- Tier 3 cap = average of three attributes.

Because each attribute has expected value 50.5:

$$
E[Cap]\approx50
$$

for any tier, subject to rounding.

This is an important design consequence: increasing the Tier does not automatically make a skill stronger. It makes the cap depend on more attributes while preserving roughly the same expected value.

For a Tier 1 skill:

$$
Cap\in[1,100]
$$

$$
Starting\ Value=\left\lfloor\frac{Cap}{2}\right\rfloor
$$

Expected starting value is approximately 25.

#### Important ambiguity

The document describes Tier as the number of attributes used to calculate the cap, but Advanced Skills add “one additional attribute” to the formula. It does not explicitly state whether the new cap is:

$$
\frac{A_1+A_2+\dots+A_T}{T}
$$

or whether the original skill formula is summed and divided by the new Tier. The former is strongly implied, but should be formally stated.

### 4.3 Failure XP

For current skill $s$, a failed roll $r$ satisfies:

$$
r\in\{s+1,\ldots,100\}
$$

XP gained is:

$$
XP=r-s
$$

Conditional on failure, the expected roll is:

$$
E[r\mid failure]=\frac{(s+1)+100}{2}=\frac{s+101}{2}
$$

Therefore:

$$
E[XP\mid failure]
=
\frac{s+101}{2}-s
=
\frac{101-s}{2}
$$

So conditional failure XP declines linearly from approximately 50 at low skill to 1 at skill 99.

The expected XP per attempted test, including successful tests that produce no failure XP, is:

$$
E[XP\text{ per attempt}]
=
P(failure)\cdot E[XP\mid failure]
$$

$$
E[XP\text{ per attempt}]
=
\frac{100-s}{100}\cdot\frac{101-s}{2}
$$

or:

$$
\boxed{
E[XP\text{ per attempt}]
=
\frac{(100-s)(101-s)}{200}
}
$$


| Skill | Failure probability | XP per failure | XP per attempt |
| --: | --: | --: | --: |
| 1 | 99% | 50.0 | 49.50 |
| 10 | 90% | 45.5 | 40.95 |
| 20 | 80% | 40.5 | 32.40 |
| 30 | 70% | 35.5 | 24.85 |
| 40 | 60% | 30.5 | 18.30 |
| 50 | 50% | 25.5 | 12.75 |
| 60 | 40% | 20.5 | 8.20 |
| 70 | 30% | 15.5 | 4.65 |
| 80 | 20% | 10.5 | 2.10 |
| 90 | 10% | 5.5 | 0.55 |
| 99 | 1% | 1.0 | 0.01 |

### 4.4 Progression cost

The documentation says increasing a skill by one costs XP equal to its current value.

If a skill rises from $s$ to $s+1$, the cost is:

$$
Cost(s\rightarrow s+1)=s
$$

To rise from starting value $s_0$ to $s_1$, total XP required is:

$$
XP=\sum_{i=s_0}^{s_1-1}i
$$

$$
XP=\frac{(s_1-1)s_1-(s_0-1)s_0}{2}
$$

This produces an accelerating advancement cost.

#### Example

To increase a skill from 25 to 50:

$$
25+26+\cdots+49
=
\frac{49\cdot50-24\cdot25}{2}
=
925
$$

At skill 25, expected XP per attempt is:

$$
\frac{(100-25)(101-25)}{200}
=
28.5
$$

At skill 49, expected XP per attempt is:

$$
\frac{(100-49)(101-49)}{200}
=
13.26
$$

Thus advancement slows for two independent reasons:

1. Each improvement costs more.
2. Failed tests become less frequent and award less XP.

This is a strong decelerating progression curve.

### 4.5 XP cascading ambiguity

At skill value 1, the rule “increase by 1 costs XP equal to its current value” means the first increase costs 1 XP. After increasing to 2, the next costs 2 XP, and so on.

However, the documentation does not state:

- Whether a skill can be advanced beyond 100.
- Whether the Skill Roll Pool can increase the skill above its cap.
- Whether the temporary pool is applied before or after the result is classified as a failed double.
- Whether XP from a failed test can be used to increase an attribute indirectly.
- What happens if a failed roll generates enough XP to raise the skill above 100.
- Whether failure XP is calculated using the skill value before or after other effects.

These are missing rules or ambiguities rather than confirmed defects.

***

## 5. Doubles Analysis

The documented special rolls are:

$$
11,22,33,44,55,66,77,88,99
$$

There are nine possible doubles, so before considering failure:

$$
P(\text{double})=\frac{9}{100}=9\%
$$

A double creates an Advanced Skill only when it is also a failure. For skill $s$, the eligible doubles are those strictly greater than $s$.

$$
P(\text{failed double}\mid s)
=
\frac{\#\{d\in\{11,22,\ldots,99\}:d>s\}}{100}
$$


| Skill value | Eligible failed doubles | Probability per test |
| --: | :-- | --: |
| 1–10 | 11–99 | 9% |
| 11–20 | 22–99 | 8% |
| 21–30 | 33–99 | 7% |
| 31–40 | 44–99 | 6% |
| 41–50 | 55–99 | 5% |
| 51–60 | 66–99 | 4% |
| 61–70 | 77–99 | 3% |
| 71–80 | 88–99 | 2% |
| 81–90 | 99 | 1% |
| 91–99 | None | 0% |

This creates a notable progression effect:

- Low-level skills can generate Advanced Skills frequently.
- A skill at 90 can only trigger on a failed 99.
- A skill at 91 or higher can never create an Advanced Skill through failure.

That may be an intentional “early discovery” design characteristic, but it creates a hard boundary at 91.

### 5.1 Double-specific observations

The probability of each individual double before failure is:

$$
P(d)=1\%
$$

For example, a failed 55 occurs only when the skill is below 55:

$$
P(\text{failed 55})=
\begin{cases}
1\% & s<55\\
0\% & s\ge55
\end{cases}
$$

The system does not define whether a failed double creates one Advanced Skill per double, whether the player may decline creation, or whether duplicate Advanced Skills can be created.

***

## 6. Exertion and Resource Audit

### 6.1 Expected roll cost

If a test rolls an ordinary d100:

$$
E[\text{cost}]=E[r]=50.5
$$

This is true whether the test succeeds or fails, before considering overflow.

For a skill $s$, the expected cost of a successful test is:

$$
E[r\mid success]=\frac{1+s}{2}
$$

The expected cost of a failed test is:

$$
E[r\mid failure]=\frac{s+101}{2}
$$

Therefore, higher-skill characters generally succeed on lower average rolls, while failures become increasingly rare and increasingly expensive relative to the character’s opportunities.

### 6.2 Cost by outcome

| Skill | Average successful-roll cost | Average failed-roll cost |
| --: | --: | --: |
| 10 | 5.5 | 55.5 |
| 25 | 13.0 | 63.0 |
| 50 | 25.5 | 75.5 |
| 75 | 38.0 | 88.0 |
| 90 | 45.5 | 95.5 |

This supports a strong identity for Tiwas: failure is not merely a probability event. It is often an expensive event because failure occurs on high rolls.

### 6.3 Resource efficiency

The expected resource cost of a successful test, unconditional per attempt, is:

$$
E[\text{successful cost}]
=
\sum_{r=1}^{s}\frac{r}{100}
=
\frac{s(s+1)}{200}
$$

Examples:


| Skill | Expected successful-test cost per attempt |
| --: | --: |
| 10 | 0.55 |
| 25 | 3.25 |
| 50 | 12.75 |
| 75 | 28.50 |
| 90 | 40.95 |

This is not the average cost conditional on success; it is the cost contribution averaged across all attempts.

### 6.4 Overflow

Overflow occurs when the roll exceeds the remaining Energy or MP:

$$
Overflow=\max(0,r-R)
$$

where $R$ is the current relevant resource.

The overflow becomes HP damage:

$$
HP\ Damage=Overflow
$$

The document does not specify whether the resource is reduced to zero first. That is the most natural interpretation, but it should be written explicitly:

$$
R'=\max(0,R-r)
$$

$$
HP'=HP-\max(0,r-R)
$$

This resource-to-HP conversion can create a death spiral:

1. A high roll costs substantial Energy or MP.
2. The resource pool is depleted.
3. Overflow damages HP.
4. Lower HP makes continued action more dangerous.
5. Further action may produce additional HP loss.

Whether this is desirable depends on how often Rest, recovery, healing, and safe interruption are available.

### 6.5 Recovery ambiguity

The rule says the character recovers half the relevant Regen stat immediately after a test.

For an odd Regen value, such as 101:

$$
\frac{101}{2}=50.5
$$

The global rounding rule suggests:

$$
Recovery=\left\lfloor\frac{Regen}{2}\right\rfloor
$$

but this is not explicitly stated.

A second ambiguity is whether recovery occurs after:

- successful tests;
- failed tests;
- tests that cause HP overflow;
- failed doubles;
- all skill tests including non-action tests.

The current wording says “after a test,” which implies all skill tests, but a formal timing rule is required.

***

## 7. Attribute Value and Correlation Audit

Not all attributes have equal mechanical value.

### 7.1 Direct skill contribution

Every attribute appears to govern one Tier 1 skill. In that narrow role, all attributes are equivalent.

### 7.2 Derived-statistic contribution

Some attributes contribute to additional resources:


| Attribute | Direct Tier 1 skill | Additional derived statistics |
| :-- | :-- | :-- |
| `bep` | Toughness | HP, Physical Energy, Energy Regen |
| `bes` | Stamina | HP, Physical Energy, Energy Regen |
| `bee` | Vitality | HP, Physical Energy |
| `bsp` | Agility | HP, Speed, Movement Speed |
| `bss` | Reflexes | HP, Speed, Movement Speed |
| `bse` | Quickness | HP, Speed |
| `mep` | Focus | MP, MP Regen |
| `mes` | Discipline | MP, MP Regen |
| Other Body attributes | Their own Tier 1 skill | HP |
| Other Mind attributes | Their own Tier 1 skill | MP |

This creates clear multi-use attributes.

`bep` and `bes` are especially valuable because each affects:

- HP;
- Physical Energy;
- Energy Regen;
- one Tier 1 skill.

`bsp` and `bss` affect:

- HP;
- Speed;
- Movement Speed;
- one Tier 1 skill.

A character with a high `bep` or `bes` receives more survivability, more Body-test capacity, faster recovery, and a stronger associated skill simultaneously.

### 7.3 Formal classification

- **Logical consequence:** Some attributes are more valuable because they appear in more formulas.
- **Balance concern:** Attribute generation may create large differences in effective power depending on which attributes roll high.
- **Potential design characteristic:** Unequal attribute utility may be intended to create naturally differentiated characters.
- **Open decision:** Whether character creation should retain fully random attributes, permit redistribution, or use a controlled generation method.

***

## 8. Dependency Map

The existing system can be represented as follows:

```text
24 Attribute Rolls
        │
        ├── Body total ───────────────► HP
        ├── Mind total ───────────────► MP
        ├── bep + bes + bee ──────────► Physical Energy
        ├── bsp + bss + bse ──────────► Speed
        ├── bep + bes ────────────────► Energy Regen
        ├── mep + mes ────────────────► MP Regen
        ├── bsp + bss ────────────────► Movement Speed
        │
        └── Attribute combinations
                    │
                    ▼
              Skill Maximum Cap
                    │
                    ▼
              Starting Skill Value
                    │
                    ▼
                  d100 Test
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
      Success                Failure
         │                     │
         │                     ├── XP = roll − skill
         │                     ├── Possible failed double
         │                     └── Advanced Skill
         │
         └──────────────┬──────────────┘
                        ▼
                 Resource Cost
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
       Resource sufficient      Overflow
              │                   │
              ▼                   ▼
       Resource decreases      HP damage
              │
              ▼
          Recovery
              │
              ▼
        Future test capacity
```

The important feedback loop is:

```text
Skill value
   ↓
Success probability
   ↓
Failure probability and failure XP
   ↓
Skill advancement
   ↓
Higher success probability
   ↓
Less XP and fewer Advanced Skill opportunities
```

This is a **negative progression feedback loop**: the better a skill becomes, the slower it improves.

The resource loop is more complex:

```text
Roll result
   ↓
Resource cost
   ↓
Remaining capacity
   ↓
Overflow risk
   ↓
HP loss
   ↓
Reduced survival margin
```

The current rules do not specify whether HP affects skill tests, so the loop currently ends at survival rather than directly reducing competence.

***

## 9. Required Missing Systems

The following systems are necessary for Tiwas to function as a complete universal TTRPG.


| System | Required? | Existing? | Complete? | Main issue |
| :-- | :-- | --: | --: | :-- |
| Character creation | Yes | Partial | No | Generation, rerolls, identity, starting resources |
| Skill definition | Yes | Partial | No | Tier 2+ construction, skill catalogue, cap interpretation |
| Basic tests | Yes | Yes | Mostly | Modifiers and difficulty absent |
| Opposed tests | Yes | No | No | No comparison procedure |
| Time and action structure | Yes | No | No | No rounds, turns, action limits |
| Combat | Usually | No | No | No attacks, defence, damage, death |
| Movement | Yes | Partial | No | No range, terrain, engagement, movement timing |
| Damage and healing | Yes | Partial | No | HP loss exists only for overflow |
| Incapacitation and death | Yes | No | No | No thresholds or procedures |
| Equipment | Usually | No | No | Weapons, armour, tools, cost |
| Conditions | Usually | No | No | No status framework |
| Ranged conflict | Usually | No | No | Range and projectile rules absent |
| Environmental hazards | Yes | No | No | Falling, fire, drowning, pressure, disease |
| Social conflict | Yes | Partial | No | Social skills exist but no conflict procedure |
| Magic/special abilities | Setting-dependent but important | No | No | No universal construction model |
| NPCs and enemies | Yes | No | No | No generation or challenge model |
| Encounter design | Yes | No | No | No difficulty or pacing method |
| Recovery and rest | Yes | Partial | No | Rest action undefined |
| Encumbrance | Optional but useful | No | No | Physical load not modelled |
| Crafting and vehicles | Optional | No | No | Required for some genres |
| Wealth and economy | Optional | No | No | Required for campaign play |
| GM procedures | Yes | No | No | No adjudication guidance |
| Campaign progression | Yes | Partial | No | Quest XP exists but no campaign-scale framework |

The core system can support many of these, but they must be designed around the existing d100 and resource principles.

***

## 10. High-Priority Open Decisions

Before designing combat or magic, the following decisions should be resolved by the designer.

### Rules interpretation

1. Are d100 results 1–100, or can the dice produce 00 as zero?
2. Is 00 ever a double?
3. Are attributes always generated randomly, or can players assign or modify them?
4. Are attribute values allowed to exceed 100 through advancement?
5. Are skill values allowed to exceed 100?
6. Does a roll of 100 always fail, even if a skill exceeds 100?
7. Does a failed double create an Advanced Skill automatically or offer a choice?
8. Can multiple failed doubles create multiple Advanced Skills from the same base skill?
9. Can the same Advanced Skill be created more than once?

### Advancement

10. Does Skill Roll Pool XP permit advancement above the current skill cap?
11. Does the Skill Roll Pool operate under the same above-cap rules as General XP?
12. What happens when a skill begins at value 1 and receives XP?
13. Are attribute improvements also paid at the current attribute value?
14. Can General XP increase a skill cap directly, or does it increase attributes only?

### Resources

15. Is recovery exactly $\lfloor Regen/2\rfloor$?
16. Does recovery occur after every test, including failed tests and overflow?
17. Can Energy and MP exceed their maximum pools?
18. Does overflow reduce the resource to zero before damaging HP?
19. Does Rest restore all HP, all resources, or only resources?
20. Is HP damage from overflow treated differently from ordinary damage?

### Resolution

21. How are difficulty modifiers applied?
22. Are opposed tests compared by success, margin, roll, or another measure?
23. Are critical successes or critical failures distinct from doubles?
24. What happens when the skill value is below 1 or above 100?
25. Can tests be repeated without changing circumstances?

These decisions should be recorded before the system is expanded, because they affect every later subsystem.

***

## 11. Preliminary Exploit and Failure Analysis

### 11.1 Repeated low-risk testing

**Mechanism:** A player repeatedly attempts a low-consequence action to generate failure XP.

**Classification:** Potential exploit and missing procedural rule.

At skill 10, each attempt produces an expected 40.95 XP from failure. That is extremely high relative to the cost of improving a low skill.

For example, improving a skill from 5 to 10 costs:

$$
5+6+7+8+9=35\ XP
$$

At skill 5, the expected XP per attempt is:

$$
\frac{95\cdot96}{200}=45.6
$$

Therefore, a character could theoretically fund this entire five-point increase in fewer than one expected attempt if unlimited, consequence-free testing were allowed.

This does not prove the XP rule is wrong. It demonstrates that the system requires an explicit test-adjudication principle, such as:

- tests require meaningful uncertainty;
- repeated attempts change the situation;
- failure has consequences;
- time or resources limit attempts;
- the GM may refuse tests with no meaningful risk.

Whether this should be a formal rule or remain a GM principle is an open design decision.

### 11.2 Deliberate failed doubles

At low skill, failed doubles occur on up to 9% of tests. If players can repeatedly attempt trivial tasks, they may intentionally farm Advanced Skills.

**Classification:** Potential exploit.

The problem becomes less severe at higher skill because the failed-double probability falls to zero at skill 91+, but the early-game incentive remains.

### 11.3 High-roll exhaustion

A roll of 100:

- always fails under ordinary roll-under rules;
- costs 100 Energy or MP;
- may cause major HP overflow;
- does not produce a failed double under the documented list.

**Classification:** Confirmed rule and balance concern.

This may be intentionally dramatic, but it means catastrophic failure is concentrated in a result that is already guaranteed to fail. Later combat design must avoid making routine tests so frequent that high-roll exhaustion dominates play.

### 11.4 Positive resource recovery interaction

Because recovery occurs after a test, the net resource change is potentially:

$$
Net\ Change = Roll-\left\lfloor\frac{Regen}{2}\right\rfloor
$$

If the recovery amount is greater than the average roll for some type of test, characters may regain more resources than they spend.

For example, with Energy Regen 150, half-Regen is 75. Many successful low rolls would cost less than 75 and then recover 75 immediately.

**Classification:** Logical consequence and possible intentional design characteristic.

This may make high-Endurance characters effectively resource-positive on easy tests. That could be desirable for sustained specialists, but it may also make Energy nearly irrelevant outside difficult or failed tests.

***

## 12. Research Plan Before New Rules

The next phase should research and compare systems in five focused areas:

1. **Percentile resolution:** Basic Roleplaying, RuneQuest, Mythras, and Call of Cthulhu.
2. **Opposed resolution and margins:** Systems that compare success quality rather than using a fixed defence number.
3. **Resource and exhaustion mechanics:** Systems where action cost, fatigue, or spellcasting risk are central.
4. **Failure-based advancement:** Existing designs using improvement through attempted or failed actions.
5. **Universal ability construction:** GURPS, Fate, Savage Worlds, and freeform or toolkit-based systems.

The purpose should be comparative analysis, not importing mechanics. Each candidate should be evaluated against Tiwas’s distinctive features:

- roll-under probability;
- high-roll cost;
- failure XP;
- attribute-derived skill caps;
- dynamic Advanced Skills;
- Body/Mind resources;
- overflow damage.

A research-backed combat model should not be selected until those interactions are explicitly simulated.

***

## 13. Current Conclusions and Confidence

| Conclusion | Classification | Confidence |
| :-- | :-- | :-- |
| Expected individual attribute is 50.5 under 1–100 interpretation | Mathematical consequence | High |
| Expected HP and MP are 606 | Mathematical consequence | High |
| Expected Physical Energy and Speed are 151.5 | Mathematical consequence | High |
| Expected Movement Speed is approximately 6.27 | Mathematical consequence | High |
| Failure XP declines as skill rises | Mathematical consequence | High |
| Failed doubles become impossible at skill 91+ | Mathematical consequence | High |
| Multi-use attributes are more valuable | Logical consequence | High |
| Repeated consequence-free testing can accelerate advancement | Mathematical consequence | High |
| This is definitely an unintended exploit | Design judgement | Low |
| A failed double should be changed | Proposed decision | Low |
| Combat should use conventional attack-versus-defence rolls | Unsupported assumption | Low |
| Magic should use a separate subsystem | Unsupported assumption | Low |

## Recommended next phase

The next deliverable should be a **research-backed comparative report and formal test harness** covering:

- exact probability calculations;
- Monte Carlo verification;
- Tier 1–4 cap distributions;
- progression simulations;
- resource depletion and recovery;
- repeated-test exploit scenarios;
- representative Body/Mind character builds.

Only after that should candidate opposed-test, combat, and magic frameworks be designed and stress-tested.
<span style="display:none">[^1]</span>

<div align="center">⁂</div>

[^1]: Tiwas-RPG-Project-Documentation-v1.pdf

