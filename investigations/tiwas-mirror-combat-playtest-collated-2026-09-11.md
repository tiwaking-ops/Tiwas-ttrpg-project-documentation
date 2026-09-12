---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test — Collated Playtest Package (Luna 2026-09-11)"
  version: "1.0"
  status: "Collated storage copy / Advisory / Non-canonical. Verbatim collation; confers no authority."
provenance:
  author_llm: {name: "Muse Spark", version: "muse-spark-1.3-contributor-free"}
  assessor_llm: {name: "Muse Spark", version: "muse-spark-1.3-contributor-free"}
  last_modified_by_llm: {name: "Muse Spark", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-11"
  last_modified_date: "2026-09-11"
---

# 0. Storage Note (collation wrapper — not part of the playtest record)

## 0.1 What this file is

Single-file collated storage copy of the GPT-5.6 Luna Mirror-Match Combat Stress Test package dated 2026-09-11 (seed `20260911`, 250 mirror combats). Created per designer request; the four separate source files are retained untouched alongside this file.

## 0.2 Components collated (verbatim, unedited)

| # | Source file (repo root, untracked) | Size (bytes) | SHA-256 |
|---|---|---:|---|
| A | `Tiwas — Mirror-Match Combat Stress Test — Complete Playtest Results and OpenCode Handoff.md` | 23391 | (see Part A; original retained at root) |
| B | `tiwas-mirror-combat-playtest-report-2026-09-11.md` | 5891 | `66B8E88C05C1A10F5407B2DACF541B6B4139F3B5F8CC2FF222947EF2E2BB93E9` |
| C | `tiwas-mirror-combat-playtest-summary-2026-09-11.json` | 1025 | `D5C3993FE0E111FB27403B4685C525AF38ACB752FB9B36A549DE9D8E4E1DB3FA` |
| D | `tiwas-mirror-combat-playtest-log-2026-09-11.csv` | 3018450 | `7AB5864AF4A955FD82A10FDD80F65FCE3C8D3ED507FC57DA73DCC5D54482060D` |

Parts A–C below are verbatim copies (original front matter of Part A omitted; recorded here: title `Tiwas — Mirror-Match Combat Stress Test — Complete Playtest Results and OpenCode Handoff`, version `1.0`, status `Playtest Results / Advisory / Non-canonical`, date `2026-09-11`, project `Tiwas TTRPG`, author `GPT-5.6 Luna`, source_design_brief `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`, execution_seed `20260911`). Part D is a digest + reference per designer instruction (full 3.0 MB CSV retained as companion file, not embedded).

## 0.3 Verification performed at collation

- CSV log: 31,986 data rows across 250 combats (`combat` 1–250); outcome counts `attacker-wins` 7001 / `defender-wins` 10496 / `repeat` 14489 — exactly matching the JSON summary and reproducing 21.89% / 32.81% / 45.30%.
- JSON `winner_counts` (Alpha 115 / Beta 134 / tie 1), `mean_exchanges` 127.944, `median_exchanges` 127.5, `full_set_armor_bypass_blocked` 244, `block_exchange_median` 17.0 — consistent with Parts A and B.
- This package is NOT a duplicate of `tiwas-mirror-combat-playtest-execution-report-2026-09-11.md` (Grok 4.5 companion run: different author, method, and Armor Bypass scaffolding). The Grok report is intentionally excluded from this collation per designer scope choice.

## 0.4 Known errata (stored verbatim; no silent fix applied)

Part A §9.2 (repeated in §19 and §22) mixes two levels in one table: Alpha 115 / Beta 134 / 1 unresolved are **combat-level** counts (46.0% / 53.6% / 0.4% of 250 combats), while 21.89% / 32.81% / 45.30% are **exchange-level** S-1 outcome rates (Part B §3.2; verified against CSV/JSON). Correction requires the author; this file preserves the original wording.

## 0.5 Authority

Advisory / non-canonical playtest evidence only. This collation creates, promotes, amends, or supersedes no DEC and no Canonical rule (Promotion Rule REQ-021 unaffected). Source design brief: `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md` (root + `investigations/`). Assessment at collation: authority handling compliant (DEC-112 preferred over stale DEC-042 wording; DEC-106 multi-attack used; mandatory Defense kept as test convention per DEC-105; no DEC-135 claim; no invented anatomy).

---

# Part A — Complete Playtest Results and OpenCode Handoff (verbatim)

# 1. Purpose

This document records the complete result of the Tiwas mirror-match combat playtest based on:

`tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`

The purpose was to exercise the currently available combat stack across:

- S-1 opposed combat resolution;
- Active Defense;
- contest-delta HP damage;
- Effect Tier/Magnitude;
- Zero-Step Location Index generation;
- Tier-1 location resolution;
- Tag + Location gating;
- Grapple;
- Trip;
- Disarm;
- Equipment Damage;
- Armor Bypass;
- Advanced Skill creation;
- Physical Energy expenditure, Overflow, and Recovery;
- Failure XP and Skill Roll Pool progression.

The playtest is an **observation and validation exercise only**.

It does **not** create, promote, amend, or supersede any DEC or Canonical rule.

The source design brief itself was explicitly advisory/non-canonical and identified unresolved issues before execution.

---

# 2. Authority and Evidence Classification

## 2.1 Authority hierarchy applied

The execution used the latest available decision state rather than blindly executing stale wording from the 2026-09-10 design brief.

The relevant source corpus distinguishes:

| Material | Treatment |
|---|---|
| Canonical Rules / Locked Core | Authoritative |
| Current ruled DEC entries | Current non-canonical designer rulings |
| Open / deferred material | Not to be silently invented |
| Design-brief conventions | Scenario-specific unless separately ruled |
| Playtest observations | Evidence only; no automatic authority |

The Alpha Playtest Corpus explicitly states that the live register is authoritative over earlier wording and that compilation or playtest material does not itself promote mechanics.

## 2.2 Critical authority correction during execution

The design brief contained a stale Armor Bypass dependency:

- DEC-113's older wording referenced the DEC-042 secondary roll.
- The later DEC-112 ruling superseded the secondary-roll architecture with the hierarchical Location Address model.
- DEC-112 also deferred actual creature-specific Location Template content to content authoring.

The current register confirms that DEC-112 replaced the prior architecture with deterministic hierarchical addresses and explicitly removed the secondary roll.

Therefore the playtest **did not invent a Tier-2 anatomical resolution**.

---

# 3. Test Scenario

## 3.1 Combatants

Two identical automated combatants:

- Alpha
- Beta

All 24 Attributes were fixed at:

`50`

This follows the design brief's deliberately symmetric mirror configuration.

## 3.2 Derived statistics

| Statistic | Formula | Value |
|---|---:|---:|
| HP | Σ 12 Body Attributes | 600 |
| MP | Σ 12 Mind Attributes | 600 |
| Physical Energy | bep + bes + bee | 150 |
| Speed | bsp + bss + bse | 150 |
| Energy Regen | bep + bes | 100 |
| MP Regen | mep + mes | 100 |
| Movement Speed | floor((bsp + bss) / 15) | 6 |

These values are directly specified by the design brief.

## 3.3 Skills

All scenario combat skills were Tier 2.

With both underlying Attributes at 50:

`Cap = floor((50 + 50) / 2) = 50`

`Starting Value = floor(50 / 2) = 25`

| Skill | Attributes | Tier | Cap | Start | Resource | Scenario Effect |
|---|---|---:|---:|---:|---|---|
| Attack | bpp + bps | 2 | 50 | 25 | PE | Inflict Injury |
| Defense | bss + bse | 2 | 50 | 25 | PE | Defensive roll |
| Grapple | bpp + bsp | 2 | 50 | 25 | PE | Grappled |
| Trip | bsp + bss | 2 | 50 | 25 | PE | Prone |
| Disarm | bss + bsx | 2 | 50 | 25 | PE | Disarm/Break Hold |
| Armor Bypass | bps + bpe | 2 | 50 | 25 | PE | Armor Bypass |
| Equipment Damage | bpp + bpe | 2 | 50 | 25 | PE | Equipment Damage |

The Attribute-pair assignments were explicitly identified by the brief as scenario choices rather than general Tiwas skill definitions.

---

# 4. Equipment and Tags

Each combatant possessed:

### Weapon

```text
slot:main_hand
state:held
offense:melee
damage:slashing
handling:light
```

### Body Armor

```text
slot:body
state:worn
defense:armor
```

These were intended to make the Tag-gated Effects executable.

DEC-114 specifies:

- Disarm requires the relevant held item;
- Equipment Damage can target held/worn equipment at the relevant coarse zone;
- Armor Bypass requires armor/shield at the relevant location;
- a location/tag mismatch falls back to Base Inflict Injury.

---

# 5. Combat Procedure Executed

## 5.1 Action selection

For the automated mirror test, each combatant used the authored legal attack actions according to the automated-creature procedure:

1. highest currently applicable Skill;
2. then lower applicable Skills;
3. each authored attack is a separate combat exchange;
4. attacks occur back-to-back on that creature's turn.

This follows DEC-106's automated-creature exception to the base one-action economy.

The design brief's 1:1 Skill → Effect mapping was retained as a **scenario convention**, because DEC-025 does not actually make Skill names mechanically determine Effects.

## 5.2 Defense

The playtest used the design brief's mandatory-Defense convention.

This is important:

> This was a **playtest execution convention**, not a claim that live-play Defense is universally mandatory.

DEC-105 records the distinction:

- playtests: Defense mandatory;
- live play: Defense voluntary;
- declined Defense produces an ordinary unopposed Core Skill Test.



## 5.3 S-1 exchange

Each exchange used one opposed contest:

| Attacker | Defender |
|---|---|
| selected offensive Skill | Defense |

Both rolled.

Resolution followed DEC-105:

| Attacker | Defender | Result |
|---|---|---|
| Success | Failure | Attacker wins |
| Failure | Success | Defender wins; attack fails |
| Success | Success | Higher Margin/Quality wins |
| Failure | Failure | Repeat |
| Exact successful tie | — | Repeat |

The defender receives no counter-Effect merely for winning the opposed attack contest.

## 5.4 HP resolution

For Inflict Injury:

`HP Damage = Winner Margin − Defender Margin`

The HP channel remains separate from Effect mitigation.

## 5.5 Non-HP Effects

For the scenario's Tier-2 Skills:

`Effect Tier = 2`

`Initial Magnitude = 2`

Because attacker and defender had equal Skill-Tiers, DEC-103's first mitigation step reduced Magnitude by 1 before Defender Margin de-escalation.

The resulting Effect can cascade:

```text
Magnitude reaches 0
        ↓
Tier − 1
        ↓
Magnitude = new Tier
        ↓
repeat as required
        ↓
Tier 0 = Effect negated
```

DEC-103 applies this machinery to Effects, not HP.

---

# 6. Location Resolution

## 6.1 Tier-1 Effects

The following used Tier-1 coarse location:

- Trip;
- Disarm;
- Equipment Damage.

The scenario used DEC-100's quartiles:

| Zero-Step Index | Coarse Zone |
|---:|---|
| 1–25 | Legs |
| 26–50 | Torso |
| 51–75 | Arms |
| 76–100 | Head |



## 6.2 Laterality

The scenario retained the existing Zero-Step parity mechanism for left/right.

## 6.3 Armor Bypass

Armor Bypass is the only Tier-2 Effect in the scenario.

The playtest **did not fabricate a Tier-2 Human Location Template**.

The current DEC-112 architecture requires creature-type-authored hierarchical Location Templates, while the actual human template remains deferred content-authoring.

This became the principal execution blocker.

---

# 7. Initial Full-Set Execution

The complete six-effect attack set was initially exercised.

The run was deliberately stopped when a successful Armor Bypass required the unresolved Tier-2 location content.

### Result

| Metric | Result |
|---|---:|
| Full-set mirror combats attempted | 250 |
| Combats encountering Armor Bypass blocker | 244 |
| Full-set runs not blocked at that point | 6 |

The 244/250 value is **not a combat win-rate statistic**.

It is an execution-dependency statistic showing how often the current combat configuration reached a mechanic whose required content could not be deterministically resolved.

No anatomy was invented to force completion.

---

# 8. Executable Statistical Slice

Because Armor Bypass could not be legitimately resolved without inventing content, a second statistical run was performed using the currently executable Effects:

- Attack;
- Grapple;
- Trip;
- Disarm;
- Equipment Damage.

Armor Bypass was excluded from the statistical slice.

This preserved the existing rules rather than introducing a temporary anatomical model.

## 8.1 Run parameters

| Parameter | Value |
|---|---:|
| Mirror combats | 250 |
| Random seed | `20260911` |
| Maximum exchanges per combat | 20,000 |
| Combatant configuration | Alpha/Beta identical |
| Starting HP | 600 each |
| Starting PE | 150 each |
| Starting combat Skills | 25 |
| Armor Bypass | excluded from statistical slice |
| Advanced Skills | created when qualifying; excluded from attack selection |
| Defense | mandatory under playtest convention |

## 8.2 Corrected execution

The executable slice was rerun after identifying and correcting an equipment/location assumption.

The corrected model treated:

- held weapon → arm/main-hand location;
- body armor → torso location;
- Disarm → succeeds only when the relevant coarse zone is Arms and the weapon is present;
- Equipment Damage → succeeds against Arms with weapon present or Torso with armor present;
- a Tag-gated miss → DEC-030 fallback to Base Inflict Injury.

The corrected results below supersede the preliminary run.

---

# 9. Statistical Results

## 9.1 Combat duration

| Statistic | Result |
|---|---:|
| Mean exchanges/combat | **127.94** |
| Median exchanges/combat | **127.5** |

## 9.2 Combat outcomes

| Outcome | Count | Rate |
|---|---:|---:|
| Alpha wins | 115 | 21.89% |
| Beta wins | 134 | 32.81% |
| Repeat / unresolved exchange outcome | — | 45.30% |
| Combat unresolved at configured cap | 1 | — |

The percentages are calculated from the corrected 250-combat run.

The unusually high Repeat proportion is therefore a direct observed property of this symmetric test configuration and should not be generalized to asymmetric characters or final creature content without further testing.

---

# 10. Important Observations

## 10.1 Mirror symmetry did not produce equal aggregate wins

The two combatants were mechanically identical, but the corrected run produced:

- Alpha: 115 wins;
- Beta: 134 wins;
- one unresolved combat at cap.

This is an observed stochastic result, not evidence that the underlying rules inherently favor Beta.

The asymmetry requires further replication before being treated as statistically meaningful.

## 10.2 Repeat outcomes are substantial

Approximately:

`45.30%`

of exchanges resulted in Repeat rather than an immediate decisive attacker/defender result.

This is a major characteristic of the current mirror configuration.

It should be treated as a balance/tempo observation, not a rules defect by itself.

## 10.3 Combat duration is finite but long

The median was:

`127.5 exchanges`

with a mean of:

`127.94 exchanges`.

This indicates that the mirror configuration can produce prolonged combat despite each successful HP exchange potentially reducing HP.

Further testing should determine whether this duration is desirable for:

- identical combatants;
- ordinary asymmetric combat;
- creature-versus-PC combat;
- multi-action creatures.

No design change is implied by this observation.

---

# 11. Advanced Skill Handling

The playtest included qualifying failed-Double handling.

When applicable:

1. a failed Double created an Advanced Skill;
2. the new Skill received the additional Attribute;
3. the new Skill was Tier +1;
4. Starting Value was set to 1 for this playtest;
5. the new Skill was excluded from offense selection for the remainder of the test.

This last exclusion was a **test constraint**, not a new Tiwas rule.

The design brief explicitly requested that incidental Advanced Skills not influence the battle.

---

# 12. Recovery, Cost, Overflow and XP

The execution retained the Core resource transaction:

- natural d100 result = test cost;
- Body Skills use Physical Energy;
- insufficient Energy produces immediate HP Overflow;
- Recovery occurs after the test;
- Failure XP is calculated for failed tests;
- Skill Roll Pool progression is applied;
- remainder proceeds to General XP.

No alternative resource system was introduced.

These mechanics remain part of the locked Core architecture identified by the project corpus.

---

# 13. Repeated-Defense Fatigue

DEC-135 was reviewed as part of the current decision state.

DEC-135 now supersedes DEC-075 and defines repeated defensive activity through the existing Fatigued Condition:

| Defense in continuous sequence | Result |
|---|---|
| First | No Fatigued |
| Second | Fatigued Tier 1 |
| Third | Fatigued Tier 2 |
| Fourth | Fatigued Tier 3 |
| etc. | Tier continues to escalate |

The Condition applies its existing global Body-Skill and Movement-Speed penalties rather than creating a hidden defense counter.

However, the mirror simulation treated each exchange as a separate exchange boundary and did **not** model an accumulating continuous defensive sequence across multiple independent exchanges.

Therefore:

**This playtest does not provide evidence for or against DEC-135's repeated-defense fatigue behavior.**

No conclusion about DEC-135 should be drawn from the combat statistics.

---

# 14. Current Location-System Finding

The strongest concrete system-readiness finding is the Armor Bypass dependency.

## 14.1 Existing architecture

DEC-112 now defines:

- hierarchical Location Address;
- deterministic Zero-Step source;
- single-source resolution;
- no secondary location roll;
- per-creature Location Templates;
- Tier 1 = coarse zones;
- deeper tiers = greater spatial precision;
- parent/child matching;
- location-bound armor;
- hierarchical mismatch fallback.



## 14.2 Missing content

The architecture explicitly leaves these items to content authoring:

- Human Location Template;
- 100-state numerical allocation;
- specific anatomical content lists.



Therefore the present problem is **not evidence that the Location Address architecture is mechanically invalid**.

It is evidence that the architecture is not yet fully instantiated for the Human template required by this test.

---

# 15. Brief-vs-Current-Corpus Conflicts Identified

| Issue | Design Brief | Current State | Treatment |
|---|---|---|---|
| Armor Bypass Tier-2 resolution | References DEC-042 secondary roll | DEC-112 supersedes secondary roll | Current DEC-112 used |
| Human Tier-2 anatomy | Not available | Deferred content-authoring | No invention |
| Skill → Effect identity | 1:1 | DEC-025 permits declared Effect independent of Skill name | 1:1 retained as scenario convention |
| Automated attack sequence | Brief asks highest current Skill | DEC-106 says automated creatures use all authored legal attacks, high-to-low | Current DEC-106 used |
| Defense | Mandatory | Mandatory for playtests; voluntary in live play | Mandatory retained as test convention |
| Defense fatigue | Not operationalized in run | DEC-135 now defines it | Not tested across exchange boundaries |
| Location Tier-1 | Quartiles | DEC-100 ruled quartiles | Used |
| Equipment location | Required for gating | Equipment state supplies relevant location semantics | Corrected before final run |

---

# 16. Design-Quality Findings

## Finding F-01 — Armor Bypass is currently not end-to-end executable

**Severity:** High for full combat-stack execution.

The full six-Effect mirror scenario cannot currently be executed without either:

1. authoring the required Human Location Template; or
2. introducing non-canonical scaffolding.

Neither should be silently performed.

**Recommendation:** complete the Human Location Template and 100-state allocation before claiming full Tier-2 Armor Bypass playtest coverage.

---

## Finding F-02 — The mirror configuration is highly symmetric

**Severity:** Informational.

All Attributes, Skills, derived statistics, equipment, and legal Effects are substantially symmetric.

This makes the scenario useful for detecting:

- stochastic asymmetry;
- Repeat frequency;
- combat duration;
- resource depletion;
- multi-attack interaction.

It is not sufficient to validate:

- asymmetric Attribute distributions;
- different Skill values;
- unequal Speed;
- asymmetric equipment;
- asymmetric armor;
- movement advantages;
- creature-specific anatomy.

---

## Finding F-03 — The scenario's Skill→Effect mapping is not a general rule

**Severity:** Medium.

The design brief itself correctly identifies the 1:1 mapping as a scenario convention because DEC-025 does not make Skill names determine Effects.

Therefore the combat statistics must not be interpreted as proving that:

```text
Attack → Inflict Injury
Grapple → Grappled
Trip → Prone
...
```

is a universal Tiwas mapping.

It was a test harness constraint.

---

## Finding F-04 — Movement was not meaningfully exercised

Both combatants had:

`Movement Speed = 6`

and no seeded positional asymmetry.

The design brief itself flagged this limitation.

Consequently, this playtest provides little evidence about:

- movement bands;
- positional advantages;
- chase;
- forced movement;
- Zone of Control;
- movement-denial interactions.

These require a separate scenario.

---

## Finding F-05 — The 45.30% Repeat rate warrants targeted follow-up

This is the most notable statistical observation from the executable slice.

The next test should determine whether the Repeat frequency remains high when:

- Attributes differ;
- Skill values differ;
- defense values differ;
- creature multi-attacks interact with resource depletion;
- Armor Bypass is available;
- Conditions alter effective Skills.

No rule change should be inferred from the current statistic alone.

---

# 17. What Was Not Changed

The playtest did **not**:

- create a new DEC;
- modify the Canonical Core;
- modify DEC-105;
- modify DEC-106;
- modify DEC-112;
- modify DEC-113;
- modify DEC-114;
- modify DEC-135;
- create a new resource pool;
- create a new resolution engine;
- invent anatomy;
- promote any scenario convention into a Tiwas rule.

The playtest therefore has **evidence status only**.

---

# 18. Recommended OpenCode Actions

## Priority 1 — Human Location Template

Create the actual Human Location Template required by DEC-112.

Required closure areas:

1. hierarchical anatomical structure;
2. Tier-2 allocation;
3. 100-state numerical mapping;
4. laterality handling;
5. parent/child coverage;
6. armor-location matching;
7. mismatch fallback.

Do not create a temporary canonical rule merely to make the current playtest executable.

---

## Priority 2 — Rerun Full Combat Stack

After the Human Location Template exists:

- restore Armor Bypass;
- rerun the 250-combat mirror sample;
- retain seed/version metadata;
- compare against the five-Effect executable baseline.

Required comparison:

| Metric | Current baseline | Full-stack rerun |
|---|---:|---:|
| Mean exchanges | 127.94 | TBD |
| Median exchanges | 127.5 | TBD |
| Alpha wins | 115 | TBD |
| Beta wins | 134 | TBD |
| Repeat rate | 45.30% | TBD |
| Cap unresolved | 1 | TBD |
| Armor Bypass execution | Blocked | TBD |

---

## Priority 3 — Asymmetric Combat

Run a separate asymmetric matrix.

At minimum vary:

- Attribute values;
- Attack Skills;
- Defense Skill;
- Speed;
- Equipment;
- armor coverage.

Do not alter the mirror dataset when doing this; retain the mirror test as a regression baseline.

---

## Priority 4 — Defense/Fatigue Test

Run a dedicated DEC-135 test with a clearly defined continuous defensive sequence.

Required observations:

- first Defense;
- second Defense;
- third Defense;
- escalating Fatigued Tier;
- Body-Skill penalty;
- Movement-Speed penalty;
- resource expenditure;
- Recovery;
- healing/removal;
- sequence termination.

This should be a separate test rather than retroactively altering the mirror-combat statistics.

---

# 19. Final Assessment

## Overall status

**PARTIALLY EXECUTABLE — STATISTICALLY USEFUL, FULL-STACK BLOCKED**

The current combat stack successfully supported a substantial executable mirror-combat test.

The corrected five-Effect statistical slice completed:

**250 mirror combats**

with:

- **127.94** mean exchanges;
- **127.5** median exchanges;
- **21.89%** Alpha wins;
- **32.81%** Beta wins;
- **45.30%** Repeat rate;
- **1** combat unresolved at the configured cap.

The full six-Effect scenario remains blocked by the unresolved Tier-2 Human Location Template required for Armor Bypass.

The correct engineering conclusion is therefore:

> **The combat core exercised in the executable slice is testable, but the complete specified combat stack is not yet content-complete for Tier-2 Armor Bypass resolution.**

No unsupported anatomy or temporary rule was introduced to conceal that dependency.

---

# 20. Generated Playtest Artifacts

The execution generated the following artifacts:

1. `tiwas-mirror-combat-playtest-report-2026-09-11.md`
2. `tiwas-mirror-combat-playtest-log-2026-09-11.csv`
3. `tiwas-mirror-combat-playtest-summary-2026-09-11.json`

These artifacts contain the detailed report, raw exchange data, and machine-readable summary respectively.

---

# 21. Source References

Primary design and governance sources used for this handoff:

- `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`
- `decision-register.md`
- `Tiwas-Alpha-Playtest-Corpus-2026-09-08.md`
- `PROJECT_CONTEXT.md`
- `tiwas-proposals-wip-and-design-direction-v1.4.3.md`
- `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`

The design brief explicitly identifies itself as advisory/non-canonical and records its unresolved Armor Bypass/location issue.

The Alpha corpus explicitly preserves the distinction between Canonical/Locked, non-canonical designer rulings, open material, and playtest observations.

---

# 22. OpenCode Handoff Summary

```text
PLAYTEST:
    Mirror Combat Stress Test
    Date: 2026-09-11
    Seed: 20260911

STATUS:
    Five-Effect statistical slice = EXECUTED
    Full six-Effect stack = BLOCKED by Tier-2 Human Location Template

RESULT:
    250 combats
    Mean = 127.94 exchanges
    Median = 127.5 exchanges
    Alpha wins = 115 / 21.89%
    Beta wins = 134 / 32.81%
    Repeat = 45.30%
    Unresolved at cap = 1

PRIMARY FINDING:
    Armor Bypass cannot currently be resolved end-to-end without
    inventing deferred Human Location Template content.

SECONDARY FINDING:
    Mirror configuration produces a high Repeat rate and long combats;
    this is an observation requiring asymmetric follow-up, not a ruling.

GOVERNANCE:
    No DEC created.
    No canonical rule changed.
    No anatomy invented.
    No scenario convention promoted to rule.

NEXT:
    1. Complete Human Location Template.
    2. Rerun full six-Effect stack.
    3. Preserve current five-Effect run as regression baseline.
    4. Run asymmetric combat matrix.
    5. Run dedicated DEC-135 repeated-defense fatigue test.
```

**End of report.**

---

# Part B — Detailed Playtest Report (verbatim)

# Tiwas — Mirror-Match Combat Stress Test Playtest Report

**Author:** GPT-5.6 Luna
**Date:** 2026-09-11
**Status:** Advisory / Non-canonical empirical playtest record
**Source brief:** `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`
**Random seed:** 20260911
**Combats:** 250
**Executable stress-slice exchange cap:** 20000

## 1. Execution basis

The supplied brief was executed against the latest available Tiwas decision state, not blindly against stale wording in the brief.

Important current-state corrections:

| Item | Brief | Executed interpretation |
|---|---|---|
| Automated combatant economy | Highest-valued offense selected | **Current DEC-106 creature rule:** automated playtest Characters are creatures and use all authored legal attacks on their turn, highest-applicable-Skill → lowest |
| Active Defense | Mandatory in the brief | Brief convention retained for this stress test; this is not the current voluntary-defense default |
| Armor Bypass Tier-2 location | Brief flags contradiction | **Execution blocked at the first successful Armor Bypass requiring Tier-2 template resolution**; no anatomy was invented |
| Location architecture | Brief references secondary roll | Current DEC-112 hierarchical single-source address model supersedes the former secondary-roll architecture |
| Fatigue | Brief predates DEC-135 | DEC-135 now exists, but this mirror run's one Defense per exchange does not create a repeated-defense sequence under the stated sequence boundary |

The current corpus explicitly leaves human-authored Location Template content and the 100-state allocation as content-authoring material. Therefore a Tier-2 Armor Bypass cannot be fully resolved from the supplied corpus without inventing content.

## 2. Baseline

Both combatants:

| Stat | Value |
|---|---:|
| All 24 attributes | 50 |
| HP | 600 |
| MP | 600 |
| Physical Energy | 150 |
| Speed | 150 |
| Energy Regen | 100 |
| Movement Speed | 6 |
| Tier-2 combat Skill Cap | 50 |
| Starting combat Skill | 25 |

## 3. Executable stress slice

To obtain meaningful end-to-end combat statistics without inventing the unresolved Tier-2 anatomy, the primary statistical run used:

`Attack, Grapple, Trip, Disarm, Equipment Damage`

Equipment/Tag matching was corrected to the authored loadout: the held weapon is an arm/main-hand item; body armor is torso-bound. A Tag-gated Effect that misses its required location falls back to Base Inflict Injury.

### 3.1 Combat outcomes

| Measure | Result |
|---|---:|
| Combats | 250 |
| Alpha wins | 115 |
| Beta wins | 134 |
| Unresolved at cap | 1 |
| Mean exchanges/combat | 127.94 |
| Median exchanges/combat | 127.5 |
| Min exchanges | 45 |
| Max exchanges | 221 |

### 3.2 S-1 outcomes

| Outcome | Count | Rate |
|---|---:|---:|
| Attacker wins | 7001 | 21.89% |
| Defender wins | 10496 | 32.81% |
| Repeat | 14489 | 45.30% |

### 3.3 Effect-path coverage

| Skill / Effect | Exchanges | Wins | Tag fallback | Location generated |
|---|---:|---:|---:|---:|
| Attack / Inflict Injury | 6497 | 1428 | 0 | 0 |
| Grapple / Grappled | 6440 | 1434 | 0 | 1434 |
| Trip / Prone | 6399 | 1397 | 0 | 1397 |
| Disarm / Disarm | 6353 | 1366 | 1117 | 1366 |
| Equipment Damage / Equipment Damage | 6297 | 1376 | 776 | 1376 |

## 4. Armor Bypass blocker probe

The full brief-defined attack set was also executed until the first Armor Bypass win requiring Tier-2 resolution.

| Measure | Result |
|---|---:|
| Full-set combats attempted | 250 |
| Runs blocked by Tier-2 Armor Bypass template | 244 |
| Median exchange at blocker | 17.0 |

**Finding:** the supplied/current corpus does not provide enough creature-specific Location Template content to resolve the Tier-2 address deterministically. DEC-112 makes the template a content-authoring dependency. The correct playtest behavior is therefore to stop/flag the branch rather than invent a mapping.

## 5. Mechanical observations

1. **The mirror baseline is mechanically symmetric.** Any systematic Alpha/Beta difference should arise from initiative and stochastic rolls rather than stat construction.
2. **The current creature multi-action rule materially changes the brief's intended combat loop.** A creature/automated character does not simply choose one highest-valued attack; it uses all authored legal attacks in descending applicable-Skill order.
3. **The brief's 1:1 Skill→Effect mapping remains a scenario convention.** It is not a general Tiwas Skill identity gate.
4. **Tag-gated Effects visibly exercise fallback behavior.** Disarm can fall back to Base Inflict Injury when the struck coarse zone does not contain the required held main-hand object.
5. **Armor Bypass is the principal execution blocker.** Its Tier-2 location resolution depends on content that the current corpus explicitly leaves open.
6. **No invented anatomy was used.** This preserves the authority boundary and makes the blocker itself a valid playtest finding.

## 6. Evidence / inference / ruling separation

### Empirical findings
- 250 mirror combats were executed in the executable slice.
- S-1 outcome frequencies and combat lengths are recorded in the attached CSV.
- Armor Bypass Tier-2 resolution reached a corpus-supported execution boundary and was not fabricated beyond it.

### Design inference
- The current automated-creature multi-action rule makes a mirror match exercise the interaction of multiple consecutive S-1 exchanges much more strongly than the original one-action brief.
- The unresolved creature Location Template is a genuine blocker to claiming that the entire six-effect stack was executed end-to-end.

### No new ruling
This playtest does **not** change, supersede, promote, or create any DEC.

## 7. Artifacts

- Raw exchange log: `tiwas-mirror-combat-playtest-log-2026-09-11.csv`
- Machine-readable summary: `tiwas-mirror-combat-playtest-summary-2026-09-11.json`

---

# Part C — Machine-Readable Summary (verbatim)

```json
{
  "author": "GPT-5.6 Luna",
  "date": "2026-09-11",
  "seed": 20260911,
  "combats": 250,
  "winner_counts": {
    "Alpha": 115,
    "Beta": 134,
    "tie": 1
  },
  "mean_exchanges": 127.944,
  "median_exchanges": 127.5,
  "outcomes": {
    "attacker-wins": 7001,
    "repeat": 14489,
    "defender-wins": 10496
  },
  "effects": {
    "Attack": {
      "n": 6497,
      "wins": 1428,
      "fallback": 0,
      "damage": 18944,
      "loc": 0
    },
    "Grapple": {
      "n": 6440,
      "wins": 1434,
      "fallback": 0,
      "damage": 0,
      "loc": 1434
    },
    "Trip": {
      "n": 6399,
      "wins": 1397,
      "fallback": 0,
      "damage": 0,
      "loc": 1397
    },
    "Disarm": {
      "n": 6353,
      "wins": 1366,
      "fallback": 1117,
      "damage": 15283,
      "loc": 1366
    },
    "Equipment Damage": {
      "n": 6297,
      "wins": 1376,
      "fallback": 776,
      "damage": 10306,
      "loc": 1376
    }
  },
  "full_set_armor_bypass_blocked": 244,
  "block_exchange_median": 17.0
}
```

---

# Part D — Raw Exchange Log Digest (reference; full CSV retained as companion)

- Companion file: `tiwas-mirror-combat-playtest-log-2026-09-11.csv` (repo root, retained; 3,018,450 bytes; SHA-256 `7AB5864AF4A955FD82A10FDD80F65FCE3C8D3ED507FC57DA73DCC5D54482060D`).
- Data rows: 31,986 across 250 combats (`combat` 1–250), verified at collation.
- Outcome counts: `attacker-wins` 7001 (21.89%) / `defender-wins` 10496 (32.81%) / `repeat` 14489 (45.30%) — matching Part C.
- Columns (27): `actor, atk_margin, atk_overflow, atk_roll, atk_skill_before, atk_skill_gain, atk_xp, combat, def_margin, def_overflow, def_roll, def_skill_before, def_skill_gain, def_xp, defender, effect, effect_mag_after_ad, effect_tier, exchange, hp_after_actor, hp_after_defender, hp_damage, location_index, outcome, skill, tag_check, zone`.
- Sample (header + first 4 data rows):

```csv
actor,atk_margin,atk_overflow,atk_roll,atk_skill_before,atk_skill_gain,atk_xp,combat,def_margin,def_overflow,def_roll,def_skill_before,def_skill_gain,def_xp,defender,effect,effect_mag_after_ad,effect_tier,exchange,hp_after_actor,hp_after_defender,hp_damage,location_index,outcome,skill,tag_check,zone
Alpha,23,0,2,25,0,0,1,,0,58,25,1,33,Beta,Inflict Injury,,,1,600,577,23,,attacker-wins,Attack,,
Alpha,13,0,12,25,0,0,1,,0,85,26,2,59,Beta,Grappled,1,2,2,600,577,,21,attacker-wins,Grapple,pass,Legs
Alpha,2,0,23,25,0,0,1,,0,65,28,1,37,Beta,Prone,1,2,3,600,577,,32,attacker-wins,Trip,pass,Torso
Alpha,,0,53,25,1,28,1,,0,42,29,0,13,Beta,Disarm,,,4,600,577,,,repeat,Disarm,,
```

**End of collated package.**
