---
document:
  status: Advisory / Non-canonical. No DEC assigned. No registry action.
  title: "Tiwas --- Mirror-Match Combat Stress Test: Revised Playtest
    Results"
  version: 0.2 (executed advisory playtest)
provenance:
  author_llm:
    name: GPT-5.6 Luna
    version: GPT-5.6 Luna
  execution_date: 2026-09-11
  execution_rng: random.SystemRandom()
  source_brief: tiwas-playtest-mirror-combat-design-brief-2026-09-10.md
---

# Tiwas --- Mirror-Match Combat Stress Test

## Revised Playtest Results

> **NON-CANONICAL ADVISORY PLAYTEST.** This document records an
> execution of the uploaded design brief after applying a scenario-only
> AI-selection correction. It is not a Tiwas rule proposal, DEC, ruling,
> or registry action.

## 1. Execution Scope

  -----------------------------------------------------------------------
  Constraint                          Execution treatment
  ----------------------------------- -----------------------------------
  Combatants                          Alpha and Beta remained
                                      mechanically identical; all 24
                                      Attributes = 50.

  New actions                         None.

  New Skill→Effect pairings           None. Existing brief pairings
                                      retained.

  Core mechanics                      Scenario followed the uploaded
                                      brief's stated exchange procedure.

  Randomness                          `random.SystemRandom()` for all
                                      random rolls/tie
                                      selections/attribute selections.

  Armor Bypass                        Explicitly unresolved/out of scope;
                                      no Tier-2 location resolution
                                      performed.

  Grappled escape                     Structurally out of scope; only
                                      Grappled imposition was tested.

  Wound targeting                     Structurally unreachable because no
                                      Wound Effect was declared.
  -----------------------------------------------------------------------

## 2. Scenario-Only AI Selection Correction

### 2.1 Defect being isolated

The original brief required the acting combatant to select the currently
highest-valued offense skill. Under failure-only skill growth, once one
skill differentiated upward, strict highest-value selection could
permanently select that skill and prevent the other skills from being
exercised.

### 2.2 Non-canonical correction

For this playtest only, offense selection used a **minimum-use coverage
constraint**:

1.  Determine the minimum number of prior selections among the six
    offense skills.
2.  Restrict candidates to skills at that minimum.
3.  Among those candidates, select the highest current numeric Skill
    value.
4.  Break remaining ties randomly using `random.SystemRandom()`.
5.  Advanced Skills are never candidates.

This preserves numeric Skill value as the priority *within the currently
least-used set*, while preventing a single early failure from
permanently monopolizing offense selection. It is **AI-selection
scaffolding only** and must not be interpreted as a Tiwas mechanic.

## 3. Baseline

  Stat                Alpha   Beta
  ----------------- ------- ------
  HP                    600    600
  MP                    600    600
  Physical Energy       150    150
  Speed                 150    150
  Energy Regen          100    100
  Movement Speed          6      6

All six offense Skills and Defense began at 25 with Tier 2 / Cap 50.

## 4. Execution Summary

  Metric                           Result
  ------------------------------ --------
  Exchanges executed                  100
  S-1 repeats                          52
  Defender wins                        28
  Attacker wins                        20
  Tag passes                            3
  Tag fail-and-fallback events          6
  Overflow events                      28
  Advanced Skills created              16
  Final Alpha HP                      142
  Final Beta HP                       250

### 4.1 Offense coverage

  Skill                Alpha selections   Beta selections
  ------------------ ------------------ -----------------
  Attack                              8                 8
  Grapple                             9                 8
  Trip                                8                 9
  Disarm                              8                 9
  Armor Bypass                        9                 8
  Equipment Damage                    8                 8

The correction prevented the original permanent single-skill lock-in:
every offense skill was selected repeatedly by both combatants.

## 5. Objective Coverage

  ---------------------------------------------------------------------------------------
                \# Objective            Status          First evidence Result
  ---------------- -------------------- ------------- ---------------- ------------------
                 1 S-1 melee-exchange   FIRED                        1 Exchange 1 was a
                   algorithm /                                         Both-Fail → Repeat
                   mandatory-defense                                   S-1 branch;
                   convention                                          mandatory Defense
                                                                       roll was present.

                 2 Contest-delta HP     FIRED                        2 Exchange 2:
                   resolution                                          attacker Margin 18
                                                                       − defender Margin
                                                                       −8 = 26 HP.

                 3 Effect               FIRED                        4 Exchange 4: Tier-2
                   Tier/Magnitude =                                    Grappled effect;
                   Skill-Tier                                          equal-tier shred
                                                                       applied before
                                                                       margin
                                                                       de-escalation.

                 4 Skill-Tier shred +   FIRED                        9 Exchange 9: Tier
                   margin de-escalation                                2, Magnitude 2 → 1
                                                                       after equal-tier
                                                                       shred → 1 after
                                                                       defender Margin 3;
                                                                       Tier cascaded to
                                                                       1.

                 5 Zero-Step + Tier-1   FIRED                        8 Exchange 8:
                   quartile location                                   natural 21 →
                                                                       Zero-Step 12 →
                                                                       Legs/Right.

                 6 Tag+Location         FIRED                       42 Passes=3;
                   gating +                                            fallbacks=6. Both
                   fail-and-fall-back                                  branches occurred.

                 7 Grappled imposition  FIRED                        4 Exchange 4:
                                                                       Grappled Tier 2 /
                                                                       Magnitude -2.
                                                                       Break-Hold escape
                                                                       was not executed.

                 8 Wound target         UNREACHABLE /              --- No Wound Effect
                   selection            OUT OF SCOPE                   was declared in
                                                                       this scenario;
                                                                       therefore no wound
                                                                       target-selection
                                                                       event can occur.

                 9 Incidental Advanced  FIRED                        2 16 Advanced Skills
                   Skill creation,                                     were created; all
                   non-influencing                                     were excluded from
                                                                       offense selection.

                10 Armor Bypass Tier-2  UNREACHABLE /              --- Armor Bypass
                   path                 OUT OF SCOPE                   resolution was
                                                                       explicitly halted
                                                                       at the unresolved
                                                                       location-path
                                                                       boundary; no
                                                                       Tier-2 Armor
                                                                       Bypass location
                                                                       resolution was
                                                                       performed.
  ---------------------------------------------------------------------------------------

## 6. Key Evidence

### 6.1 S-1 and contest-delta HP

-   **Exchange 2**: Beta Attack succeeded (`7` ≤ 25) with Margin 18;
    Alpha Defense failed (`33` \> 25) with Margin -8.
-   Contest-delta HP = `18 − (-8) = 26`.

### 6.2 Grappled

-   **Exchange 4**: Beta won with Grapple (`20`), against Defense `54`.
-   Equal Tier-2 shred: Magnitude 2 → 1.
-   Defender Margin `-29` is negative, so margin de-escalation increases
    the working magnitude to `30`; the surviving record is
    `Grappled / Tier 2 / Magnitude -2`.
-   Break-Hold escape was not attempted because it is structurally
    outside this scenario's execution scope.

### 6.3 Location + Tag gating

-   **Exchange 8**: Equipment Damage generated Zero-Step Location Index
    `12` → `Legs/Right`; required target Tag was absent at that coarse
    location, so the Effect failed and fell back to Base Inflict Injury.
-   **Exchange 42**: Disarm generated Location Index `62` →
    `Arms/Right`; required Tag matched and the Effect applied.

### 6.4 Skill-Tier shred + margin de-escalation

-   **Exchange 9**: Trip won with attacker Margin 16 and successful
    Defense Margin 3. Starting Effect Tier/Magnitude = 2/2.
-   Equal Skill-Tier shred reduced Magnitude 2 → 1.
-   Defender Margin 3 reduced Magnitude 1 → -2, invoking the unified
    carry rule: Tier 2 → Tier 1 and Magnitude reset to 1.
-   Result: `Prone / Tier 1 / Magnitude -1 / Location 90`.

## 7. Advanced Skills

Total Advanced Skills created: **16**.

  ----------------------------------------------------------------------------
  Combatant   Base skill Added                 Tier Starting value Selection
              lineage    attribute                                 status
  ----------- ---------- ----------- -------------- -------------- -----------
  Alpha       Defense    mpe                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Alpha       Grapple    mex                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Alpha       Defense    mpp                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Alpha       Defense    mep                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Alpha       Trip       bex                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Alpha       Defense    mee                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Alpha       Defense    bsp                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Armor      mse                      3              1 Excluded
              Bypass                                               from
                                                                   offense
                                                                   selection

  Beta        Disarm     bps                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Defense    bpp                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Defense    bsp                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Disarm     bex                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Attack     mex                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Armor      msp                      3              1 Excluded
              Bypass                                               from
                                                                   offense
                                                                   selection

  Beta        Grapple    mpp                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection

  Beta        Trip       bes                      3              1 Excluded
                                                                   from
                                                                   offense
                                                                   selection
  ----------------------------------------------------------------------------

No Advanced Skill influenced offense selection.

## 8. Explicitly Unreachable / Out-of-Scope Objectives

### Objective 8 --- Wound target selection

**UNREACHABLE BY DESIGN.** The scenario contains no declared Wound
Effect. Therefore DEC-102 wound-target selection cannot fire without
introducing a new Effect declaration or changing the scenario's Effect
mapping, both prohibited by the stated constraints.

### Objective 10 --- Armor Bypass Tier-2 path

**OUT OF SCOPE BY DESIGN.** Armor Bypass remains excluded from
executable Tier-2 location resolution because the uploaded brief
identifies the live contradiction between DEC-113's older DEC-042 path
and the newer hierarchical Location architecture, while the required
human location template is not available. The run did not invent a
replacement template or silently resolve that contradiction.

Armor Bypass was selected on two attacker-win exchanges by the coverage
policy, but the resolution stopped at the explicit out-of-scope
boundary; no Armor Bypass Tier-2 location result was produced.

## 9. Assessment

### 9.1 Selection-lock defect

The scenario-only minimum-use coverage constraint successfully prevented
permanent single-skill lock-in. All six offense skills were repeatedly
selected on both sides despite asymmetric failure-XP growth.

This demonstrates that the defect is located in the interaction between
the brief's strict `highest current value` selection policy and
failure-only growth, rather than being an unavoidable consequence of the
underlying skill-growth arithmetic.

### 9.2 Mechanical coverage

Objectives 1--6 and 9 fired in the executed run. Objective 7's
Grappled-imposition half fired. Objective 8 was unreachable by
construction. Objective 10 was deliberately not resolved.

### 9.3 Scope warning

The playtest's selection correction is a scenario-only AI policy. It
does not amend, supersede, or propose changing Tiwas offense-selection
rules. Any future rule-level treatment of AI action selection must be
considered separately through the project's governance process.

## 10. Complete Exchange Log

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  exchange   actor   defender   offense_skill_chosen   offense_skill_value   defense_value   atk_roll   def_roll   atk_margin   def_margin   outcome         effect_declared   location_index   zone    laterality   tag_check            effect_applied   fallback   hp_damage   hp_alpha   hp_beta   pe_alpha   pe_beta   failure_xp_actor   failure_xp_defender   overflow_actor   overflow_defender
  ---------- ------- ---------- ---------------------- --------------------- --------------- ---------- ---------- ------------ ------------ --------------- ----------------- ---------------- ------- ------------ -------------------- ---------------- ---------- ----------- ---------- --------- ---------- --------- ------------------ --------------------- ---------------- -------------------
  1          Alpha   Beta       Disarm                 25                    25              87         64         -62          -39          repeat                                                                  n/a                  False            False      0           600        600       113        136       62                 39                    0                0

  2          Beta    Alpha      Attack                 25                    25              7          33         18           -8           attacker-wins   Inflict Injury                                          n/a                  False            False      26          574        600       130        150       0                  8                     0                0

  3          Alpha   Beta       Attack                 25                    26              73         95         -48          -69          repeat                                                                  n/a                  False            False      0           574        600       107        105       48                 69                    0                0

  4          Beta    Alpha      Grapple                25                    25              20         54         5            -29          attacker-wins   Grappled                                                n/a                  True             False      0           574        600       103        135       0                  29                    0                0

  5          Alpha   Beta       Grapple                25                    28              55         24         -30          4            defender-wins                                                           n/a                  False            False      0           574        600       98         150       30                 0                     0                0

  6          Beta    Alpha      Disarm                 25                    26              83         74         -58          -48          repeat                                                                  n/a                  False            False      0           574        600       74         117       58                 48                    0                0

  7          Alpha   Beta       Armor Bypass           25                    28              97         36         -72          -8           repeat                                                                  n/a                  False            False      0           551        600       50         131       72                 8                     23               0

  8          Beta    Alpha      Equipment Damage       25                    27              21         100        4            -73          attacker-wins   Equipment Damage  12               Legs    Right        fail-and-fall-back   False            True       77          424        600       50         150       0                  73                    0                50

  9          Alpha   Beta       Trip                   25                    28              9          25         16           3            attacker-wins   Prone                                                   n/a                  True             False      0           424        600       91         150       0                  0                     0                0

  10         Beta    Alpha      Trip                   25                    29              32         94         -7           -65          repeat                                                                  n/a                  False            False      0           421        600       50         150       7                  65                    0                3

  11         Alpha   Beta       Equipment Damage       25                    28              21         32         4            -4           attacker-wins   Equipment Damage  12               Legs    Right        fail-and-fall-back   False            True       8           421        592       79         150       0                  4                     0                0

  12         Beta    Alpha      Armor Bypass           25                    31              88         5          -63          26           defender-wins                                                           n/a                  False            False      0           421        592       124        112       63                 0                     0                0

  13         Alpha   Beta       Disarm                 27                    28              48         54         -21          -26          repeat                                                                  n/a                  False            False      0           421        592       126        108       21                 26                    0                0

  14         Beta    Alpha      Armor Bypass           27                    31              22         58         5            -27          attacker-wins   Armor Bypass                                            out-of-scope         False            False      0           421        592       118        136       0                  27                    0                0

  15         Alpha   Beta       Armor Bypass           27                    28              75         73         -48          -45          repeat                                                                  n/a                  False            False      0           421        592       93         113       48                 45                    0                0

  16         Beta    Alpha      Disarm                 27                    31              66         62         -39          -31          repeat                                                                  n/a                  False            False      0           421        592       81         97        39                 31                    0                0

  17         Alpha   Beta       Grapple                26                    29              54         64         -28          -35          repeat                                                                  n/a                  False            False      0           421        592       77         83        28                 35                    0                0

  18         Beta    Alpha      Attack                 25                    32              85         6          -60          26           defender-wins                                                           n/a                  False            False      0           421        590       121        50        60                 0                     2                0

  19         Alpha   Beta       Attack                 26                    30              28         32         -2           -2           repeat                                                                  n/a                  False            False      0           421        590       143        68        2                  2                     0                0

  20         Beta    Alpha      Equipment Damage       25                    32              54         88         -29          -56          repeat                                                                  n/a                  False            False      0           421        590       105        64        29                 56                    0                0

  21         Alpha   Beta       Trip                   25                    30              55         14         -30          16           defender-wins                                                           n/a                  False            False      0           421        590       100        100       30                 0                     0                0

  22         Beta    Alpha      Trip                   25                    33              8          41         17           -8           attacker-wins   Prone                                                   n/a                  True             False      0           421        590       109        142       0                  8                     0                0

  23         Alpha   Beta       Equipment Damage       25                    30              12         49         13           -19          attacker-wins   Equipment Damage  21               Legs    Left         fail-and-fall-back   False            True       32          421        558       147        143       0                  19                    0                0

  24         Beta    Alpha      Grapple                25                    33              23         97         2            -64          attacker-wins   Grappled                                                n/a                  True             False      0           421        558       100        150       0                  64                    0                0

  25         Alpha   Beta       Armor Bypass           28                    30              39         57         -11          -27          repeat                                                                  n/a                  False            False      0           421        558       111        143       11                 27                    0                0

  26         Beta    Alpha      Disarm                 28                    34              72         14         -44          20           defender-wins                                                           n/a                  False            False      0           421        558       147        121       44                 0                     0                0

  27         Alpha   Beta       Disarm                 27                    30              29         93         -2           -63          repeat                                                                  n/a                  False            False      0           421        558       150        78        2                  63                    0                0

  28         Beta    Alpha      Attack                 27                    34              84         47         -57          -13          repeat                                                                  n/a                  False            False      0           421        552       150        50        57                 13                    6                0

  29         Alpha   Beta       Grapple                27                    32              84         100        -57          -68          repeat                                                                  n/a                  False            False      0           421        502       116        50        57                 68                    0                50

  30         Beta    Alpha      Armor Bypass           27                    34              83         78         -56          -44          repeat                                                                  n/a                  False            False      0           421        469       88         50        56                 44                    33               0

  31         Alpha   Beta       Trip                   26                    34              19         42         7            -8           attacker-wins   Prone                                                   n/a                  True             False      0           421        469       119        58        0                  8                     0                0

  32         Beta    Alpha      Equipment Damage       26                    35              31         17         -5           18           defender-wins                                                           n/a                  False            False      0           421        469       150        77        5                  0                     0                0

  33         Alpha   Beta       Attack                 26                    34              59         89         -33          -55          repeat                                                                  n/a                  False            False      0           421        457       141        50        33                 55                    0                12

  34         Beta    Alpha      Trip                   25                    35              36         89         -11          -54          repeat                                                                  n/a                  False            False      0           421        457       102        64        11                 54                    0                0

  35         Alpha   Beta       Equipment Damage       25                    35              58         70         -33          -35          repeat                                                                  n/a                  False            False      0           421        451       94         50        33                 35                    0                6

  36         Beta    Alpha      Grapple                25                    36              19         77         6            -41          attacker-wins   Grappled                                                n/a                  True             False      0           421        451       67         81        0                  41                    0                0

  37         Alpha   Beta       Grapple                29                    36              75         87         -46          -51          repeat                                                                  n/a                  False            False      0           413        445       50         50        46                 51                    8                6

  38         Beta    Alpha      Armor Bypass           29                    37              51         68         -22          -31          repeat                                                                  n/a                  False            False      0           395        444       50         50        22                 31                    1                18

  39         Alpha   Beta       Armor Bypass           28                    37              8          53         20           -16          attacker-wins   Armor Bypass                                            out-of-scope         False            False      0           395        441       92         50        0                  16                    0                3

  40         Beta    Alpha      Attack                 29                    37              52         27         -23          10           defender-wins                                                           n/a                  False            False      0           395        439       115        50        23                 0                     2                0

  41         Alpha   Beta       Attack                 27                    37              3          8          24           29           defender-wins                                                           n/a                  False            False      0           395        439       150        92        0                  0                     0                0

  42         Beta    Alpha      Disarm                 29                    37              26         81         3            -44          attacker-wins   Disarm            62               Arms    Right        pass                 True             False      0           395        439       119        116       0                  44                    0                0

  43         Alpha   Beta       Disarm                 27                    37              31         39         -4           -2           repeat                                                                  n/a                  False            False      0           395        439       138        127       4                  2                     0                0

  44         Beta    Alpha      Equipment Damage       26                    38              84         26         -58          12           defender-wins                                                           n/a                  False            False      0           395        439       150        93        58                 0                     0                0

  45         Alpha   Beta       Equipment Damage       26                    37              18         97         8            -60          attacker-wins   Equipment Damage  81               Head    Left         fail-and-fall-back   False            True       68          395        367       150        50        0                  60                    0                4

  46         Beta    Alpha      Grapple                25                    38              83         60         -58          -22          repeat                                                                  n/a                  False            False      0           395        334       140        50        58                 22                    33               0

  47         Alpha   Beta       Trip                   26                    38              70         21         -44          17           defender-wins                                                           n/a                  False            False      0           395        334       120        79        44                 0                     0                0

  48         Beta    Alpha      Trip                   25                    38              50         33         -25          5            defender-wins                                                           n/a                  False            False      0           395        334       137        79        25                 0                     0                0

  49         Alpha   Beta       Grapple                30                    38              94         28         -64          10           defender-wins                                                           n/a                  False            False      0           395        334       93         101       64                 0                     0                0

  50         Beta    Alpha      Disarm                 29                    38              83         83         -54          -45          repeat                                                                  n/a                  False            False      0           395        334       60         68        54                 45                    0                0

  51         Alpha   Beta       Armor Bypass           28                    38              61         37         -33          1            defender-wins                                                           n/a                  False            False      0           394        334       50         81        33                 0                     1                0

  52         Beta    Alpha      Attack                 29                    39              52         71         -23          -32          repeat                                                                  n/a                  False            False      0           373        334       50         79        23                 32                    0                21

  53         Alpha   Beta       Trip                   27                    38              56         47         -29          -9           repeat                                                                  n/a                  False            False      0           367        334       50         82        29                 9                     6                0

  54         Beta    Alpha      Armor Bypass           29                    39              52         56         -23          -17          repeat                                                                  n/a                  False            False      0           361        334       50         80        23                 17                    0                6

  55         Alpha   Beta       Attack                 27                    38              91         39         -64          -1           repeat                                                                  n/a                  False            False      0           320        334       50         91        64                 1                     41               0

  56         Beta    Alpha      Equipment Damage       28                    39              36         80         -8           -41          repeat                                                                  n/a                  False            False      0           290        334       50         105       8                  41                    0                30

  57         Alpha   Beta       Disarm                 27                    38              56         18         -29          20           defender-wins                                                           n/a                  False            False      0           284        334       50         137       29                 0                     6                0

  58         Beta    Alpha      Grapple                27                    40              60         72         -33          -32          repeat                                                                  n/a                  False            False      0           262        334       50         127       33                 32                    0                22

  59         Alpha   Beta       Equipment Damage       26                    38              70         65         -44          -27          repeat                                                                  n/a                  False            False      0           242        334       50         112       44                 27                    20               0

  60         Beta    Alpha      Trip                   26                    40              98         97         -72          -57          repeat                                                                  n/a                  False            False      0           195        334       50         64        72                 57                    0                47

  61         Alpha   Beta       Grapple                32                    38              41         91         -9           -53          repeat                                                                  n/a                  False            False      0           195        307       59         50        9                  53                    0                27

  62         Beta    Alpha      Disarm                 30                    41              1          62         29           -21          attacker-wins   Disarm            10               Legs    Right        fail-and-fall-back   False            True       50          142        307       50         99        0                  21                    0                3

  63         Alpha   Beta       Attack                 29                    39              19         6          10           33           defender-wins                                                           n/a                  False            False      0           142        307       81         143       0                  0                     0                0

  64         Beta    Alpha      Armor Bypass           29                    41              7          4          22           37           defender-wins                                                           n/a                  False            False      0           142        307       127        150       0                  0                     0                0

  65         Alpha   Beta       Armor Bypass           29                    39              95         66         -66          -27          repeat                                                                  n/a                  False            False      0           142        307       82         134       66                 27                    0                0

  66         Beta    Alpha      Attack                 29                    41              32         47         -3           -6           repeat                                                                  n/a                  False            False      0           142        307       85         150       3                  6                     0                0

  67         Alpha   Beta       Disarm                 28                    39              60         51         -32          -12          repeat                                                                  n/a                  False            False      0           142        307       75         149       32                 12                    0                0

  68         Beta    Alpha      Trip                   28                    41              76         24         -48          17           defender-wins                                                           n/a                  False            False      0           142        307       101        123       48                 0                     0                0

  69         Alpha   Beta       Trip                   28                    39              62         90         -34          -51          repeat                                                                  n/a                  False            False      0           142        307       89         83        34                 51                    0                0

  70         Beta    Alpha      Equipment Damage       28                    41              30         60         -2           -19          repeat                                                                  n/a                  False            False      0           142        307       79         103       2                  19                    0                0

  71         Alpha   Beta       Equipment Damage       27                    40              4          17         23           23           repeat                                                                  n/a                  False            False      0           142        307       125        136       0                  0                     0                0

  72         Beta    Alpha      Grapple                28                    41              84         24         -56          17           defender-wins                                                           n/a                  False            False      0           142        307       150        102       56                 0                     0                0

  73         Alpha   Beta       Grapple                32                    40              79         35         -47          5            defender-wins                                                           n/a                  False            False      0           142        307       121        117       47                 0                     0                0

  74         Beta    Alpha      Disarm                 30                    41              67         80         -37          -39          repeat                                                                  n/a                  False            False      0           142        307       91         100       37                 39                    0                0

  75         Alpha   Beta       Armor Bypass           31                    40              45         83         -14          -43          repeat                                                                  n/a                  False            False      0           142        307       96         67        14                 43                    0                0

  76         Beta    Alpha      Armor Bypass           29                    41              5          5          24           36           defender-wins                                                           n/a                  False            False      0           142        307       141        112       0                  0                     0                0

  77         Alpha   Beta       Attack                 29                    41              3          25         26           16           attacker-wins   Inflict Injury                                          n/a                  False            False      10          142        297       150        137       0                  0                     0                0

  78         Beta    Alpha      Grapple                29                    41              23         64         6            -23          attacker-wins   Grappled                                                n/a                  True             False      0           142        297       136        150       0                  23                    0                0

  79         Alpha   Beta       Disarm                 29                    41              7          20         22           21           attacker-wins   Disarm            70               Arms    Right        pass                 True             False      0           142        297       150        150       0                  0                     0                0

  80         Beta    Alpha      Attack                 29                    41              53         46         -24          -5           repeat                                                                  n/a                  False            False      0           142        297       150        147       24                 5                     0                0

  81         Alpha   Beta       Trip                   29                    41              50         13         -21          28           defender-wins                                                           n/a                  False            False      0           142        297       150        150       21                 0                     0                0

  82         Beta    Alpha      Trip                   29                    41              51         35         -22          6            defender-wins                                                           n/a                  False            False      0           142        297       150        149       22                 0                     0                0

  83         Alpha   Beta       Equipment Damage       27                    41              3          81         24           -40          attacker-wins   Equipment Damage  30               Torso   Right        pass                 True             False      0           142        297       150        118       0                  40                    0                0

  84         Beta    Alpha      Equipment Damage       28                    41              78         11         -50          30           defender-wins                                                           n/a                  False            False      0           142        297       150        90        50                 0                     0                0

  85         Alpha   Beta       Grapple                33                    41              19         5          14           36           defender-wins                                                           n/a                  False            False      0           142        297       150        135       0                  0                     0                0

  86         Beta    Alpha      Disarm                 31                    41              99         55         -68          -14          repeat                                                                  n/a                  False            False      0           142        297       145        86        68                 14                    0                0

  87         Alpha   Beta       Armor Bypass           31                    41              5          2          26           39           defender-wins                                                           n/a                  False            False      0           142        297       150        134       0                  0                     0                0

  88         Beta    Alpha      Attack                 29                    41              33         63         -4           -22          repeat                                                                  n/a                  False            False      0           142        297       137        150       4                  22                    0                0

  89         Alpha   Beta       Disarm                 29                    41              11         34         18           7            attacker-wins   Disarm            11               Legs    Left         fail-and-fall-back   False            True       11          142        286       150        150       0                  0                     0                0

  90         Beta    Alpha      Armor Bypass           29                    41              33         47         -4           -6           repeat                                                                  n/a                  False            False      0           142        286       150        150       4                  6                     0                0

  91         Alpha   Beta       Attack                 29                    41              41         73         -12          -32          repeat                                                                  n/a                  False            False      0           142        286       150        127       12                 32                    0                0

  92         Beta    Alpha      Trip                   29                    41              84         31         -55          10           defender-wins                                                           n/a                  False            False      0           142        286       150        93        55                 0                     0                0

  93         Alpha   Beta       Trip                   29                    41              32         78         -3           -37          repeat                                                                  n/a                  False            False      0           142        286       150        65        3                  37                    0                0

  94         Beta    Alpha      Grapple                29                    41              33         94         -4           -53          repeat                                                                  n/a                  False            False      0           142        286       106        82        4                  53                    0                0

  95         Alpha   Beta       Equipment Damage       27                    41              52         7          -25          34           defender-wins                                                           n/a                  False            False      0           142        286       104        125       25                 0                     0                0

  96         Beta    Alpha      Equipment Damage       29                    42              36         46         -7           -4           repeat                                                                  n/a                  False            False      0           142        286       108        139       7                  4                     0                0

  97         Alpha   Beta       Grapple                33                    41              95         62         -62          -21          repeat                                                                  n/a                  False            False      0           142        286       63         127       62                 21                    0                0

  98         Beta    Alpha      Disarm                 33                    42              89         28         -56          14           defender-wins                                                           n/a                  False            False      0           142        286       85         88        56                 0                     0                0

  99         Alpha   Beta       Armor Bypass           31                    41              70         74         -39          -33          repeat                                                                  n/a                  False            False      0           142        286       65         64        39                 33                    0                0

  100        Beta    Alpha      Trip                   30                    42              100        45         -70          -3           repeat                                                                  n/a                  False            False      0           142        250       70         50        70                 3                     36               0
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 11. Final State

  Skill/Stat           Alpha   Beta
  ------------------ ------- ------
  Attack                  29     29
  Grapple                 34     29
  Trip                    29     32
  Disarm                  29     34
  Armor Bypass            32     29
  Equipment Damage        27     29
  Defense                 42     41
  HP                     142    250

**Disposition:** Advisory playtest evidence only. No DEC inferred. No
canonical rule change made.
