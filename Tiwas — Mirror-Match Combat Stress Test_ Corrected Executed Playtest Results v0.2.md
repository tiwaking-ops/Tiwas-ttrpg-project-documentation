---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test: Corrected Executed Playtest Results"
  version: "0.2"
  document_type: "Executed Playtest Results / Formal Project Documentation"
  status: "Advisory / Non-canonical"
  authority: "Non-authoritative playtest evidence"
  canonical_status: "No canonical rule change"
  dec_status: "No DEC created, amended, superseded, or proposed by this document"
  registry_status: "No Decision Register action"
provenance:
  author_llm:
    name: "GPT-5.6 Luna"
    version: "GPT-5.6 Luna"
  execution_artifact: "tiwas-mirror-combat-playtest-results-v0.2.md"
  execution_artifact_status: "Machine execution record; source of truth for run statistics"
  execution_date: "2026-09-11"
  report_correction_date: "2026-09-12"
  execution_rng: "random.SystemRandom()"
  source_design_brief: "tiwas-playtest-mirror-combat-design-brief-2026-09-10.md"
  correction_basis:
    - "Verified 100-exchange execution log"
    - "Current Tiwas Decision Register / ruling corpus"
    - "Reconciliation performed after OpenCode audit"
  supersedes:
    - "Earlier internally inconsistent v0.2 report summary"
---

# Tiwas — Mirror-Match Combat Stress Test

## Corrected Executed Playtest Results v0.2

> **NON-CANONICAL ADVISORY PLAYTEST DOCUMENT**
>
> This document records the executed mirror-match playtest and its corrected analysis. It does not establish, modify, supersede, or promote any Tiwas rule.
>
> The machine execution artifact is the authoritative record for the numerical results of the run. This report corrects summary and final-state fields that were copied incorrectly into the preceding formal report.

---

# 1. Executive Summary

The mirror-match playtest was executed with two mechanically identical combatants over **100 exchanges**.

The run successfully demonstrated that the original scenario's strict:

`select currently highest-valued offense Skill`

policy produces a single-Skill lock-in problem when combined with failure-driven Skill growth.

A **scenario-only AI-selection coverage scaffold** was therefore used:

1. Select from the least-used eligible offense Skills.
2. Within that set, select the highest current Skill value.
3. Resolve remaining ties with `random.SystemRandom()`.
4. Exclude Advanced Skills from offense selection.

This successfully distributed offense selection across all six intended offense Skills for both combatants.

The verified execution statistics are:

| Metric | Verified result |
|---|---:|
| Exchanges executed | **100** |
| S-1 repeats | **52** |
| Defender wins | **28** |
| Attacker wins | **20** |
| Tag passes | **3** |
| Tag fail-and-fallback events | **6** |
| Overflow events | **28** |
| Advanced Skills created | **16** |
| Final Alpha HP | **142** |
| Final Beta HP | **250** |

The primary execution arithmetic reconciles:

`52 + 28 + 20 = 100`

The run therefore ended at the **100-exchange execution boundary**, not because either combatant reached HP ≤ 0.

---

# 2. Critical Documentation Correction

## 2.1 Previous report error

The preceding formal report contained summary statistics that did not match its own referenced machine execution artifact.

The error affected the report's summary/final-state sections but not the underlying 100-exchange machine log.

The verified artifact was manually re-tallied during OpenCode review.

## 2.2 Corrected values

| Metric | Incorrect previous report | Correct artifact value |
|---|---:|---:|
| S-1 repeats | 19 | **52** |
| Defender wins | 41 | **28** |
| Attacker wins | 40 | **20** |
| Tag passes | 8 | **3** |
| Tag fail-and-fallback | 7 | **6** |
| Overflow events | 0 | **28** |
| Final Alpha HP | 0 | **142** |
| Final Beta HP | 0 | **250** |
| Selections per combatant | 100 | **50** |
| Final Skills | all 25 | **Diverged through Failure XP** |

The exchange-level evidence in the preceding report was derived from the correct artifact; the error was therefore a **documentation-summary integrity failure**, not a second combat execution.

## 2.3 Correct source-of-truth rule for this document

For this playtest:

`Machine execution log > derived report summary`

Where a narrative summary conflicts with an individual recorded exchange, the recorded exchange and machine tally take precedence.

---

# 3. Execution Boundary

The run executed exactly:

**100 exchanges**

Neither combatant reached zero HP during those 100 exchanges.

Therefore:

| Question | Result |
|---|---|
| Did Alpha reach HP ≤ 0? | **No** |
| Did Beta reach HP ≤ 0? | **No** |
| Did HP-based combat termination occur? | **No** |
| Why did execution stop? | **100-exchange execution boundary** |
| Final Alpha HP | **142** |
| Final Beta HP | **250** |

The 100-exchange boundary is an execution parameter of this playtest record. It must not be represented as a Tiwas combat-termination rule.

---

# 4. Scenario Scope

## 4.1 Combatants

Alpha and Beta were mechanically identical.

No combatant asymmetry was introduced.

| Property | Alpha | Beta |
|---|---:|---:|
| All 24 Attributes | 50 | 50 |
| HP | 600 | 600 |
| MP | 600 | 600 |
| Physical Energy | 150 | 150 |
| Speed | 150 | 150 |
| Energy Regen | 100 | 100 |
| Movement Speed | 6 | 6 |

## 4.2 Starting combat Skills

All relevant Skills began at:

- Tier 2
- Cap 50
- Starting value 25

The six offense Skills were:

| Skill | Starting Value |
|---|---:|
| Attack | 25 |
| Grapple | 25 |
| Trip | 25 |
| Disarm | 25 |
| Armor Bypass | 25 |
| Equipment Damage | 25 |

Defense also began at 25.

---

# 5. Randomness and Execution Method

The execution used:

`random.SystemRandom()`

This was used for random choices where the scenario permitted random selection, including:

- remaining offense-selection ties;
- Advanced Skill Attribute selection;
- other explicitly random scenario choices.

No deterministic seed was imposed.

---

# 6. Scenario-Only AI Selection Correction

## 6.1 Problem

The original scenario instructed the automated combatant to select the offense Skill with the highest current numeric value.

This interacts poorly with failure-driven Skill progression.

If one Skill becomes higher than the others:

1. It becomes the highest-valued candidate.
2. It is selected again.
3. It receives additional opportunities to generate Failure XP.
4. Lower Skills cease being selected.
5. The higher Skill therefore maintains its selection advantage.

This creates permanent single-Skill lock-in after the first meaningful differentiation.

The earlier mirror-match executions demonstrated this behavior.

## 6.2 Experimental correction

For this execution only:

| Step | Selection rule |
|---:|---|
| 1 | Determine previous selection count for each eligible offense Skill. |
| 2 | Identify the minimum selection count. |
| 3 | Restrict candidates to Skills at that minimum. |
| 4 | Select the highest current numeric Skill among those candidates. |
| 5 | Resolve remaining ties with `random.SystemRandom()`. |
| 6 | Exclude Advanced Skills from the offense-selection pool. |

## 6.3 Authority status

This correction is:

**NON-CANONICAL AI-SELECTION SCAFFOLDING**

It is not:

- a Tiwas rule;
- a player-selection rule;
- an AI rule for general Tiwas play;
- a DEC;
- a designer ruling;
- a proposed canonical mechanic.

Its sole purpose was to make this particular scenario exercise all intended offense branches.

---

# 7. Offense Coverage

The correction succeeded.

Each combatant received exactly 50 actor turns during the 100-exchange run.

| Offense Skill | Alpha | Beta |
|---|---:|---:|
| Attack | 8 | 8 |
| Grapple | 9 | 8 |
| Trip | 8 | 9 |
| Disarm | 8 | 9 |
| Armor Bypass | 9 | 8 |
| Equipment Damage | 8 | 8 |
| **Total** | **50** | **50** |

Thus:

`8 + 9 + 8 + 8 + 9 + 8 = 50`

for Alpha, and:

`8 + 8 + 9 + 9 + 8 + 8 = 50`

for Beta.

No offense Skill became permanently inaccessible.

This is the principal successful result of the scenario-only selection correction.

---

# 8. Verified Outcome Distribution

The 100 recorded exchanges reconcile as follows:

| S-1 result | Count |
|---|---:|
| Both Fail → Repeat | **52** |
| Defender Wins | **28** |
| Attacker Wins | **20** |
| **Total** | **100** |

This is internally consistent with the verified machine artifact.

The high number of repeats is itself relevant evidence: the mirror-match starting Skills were only 25, so the S-1 success/failure structure produced frequent mutual failures.

---

# 9. Tag-Gated Effect Results

The execution recorded:

| Tag-gating outcome | Count |
|---|---:|
| Tag Pass | **3** |
| Fail-and-Fallback | **6** |
| **Total Tag-gated events** | **9** |

Verified pass exchanges:

- Exchange 42
- Exchange 79
- Exchange 83

Verified fallback exchanges:

- Exchange 8
- Exchange 11
- Exchange 23
- Exchange 45
- Exchange 62
- Exchange 89

The fallback behavior is the declared scenario behavior:

`Tag/Location mismatch → declared Effect fails → Base Inflict Injury`

No residual Effect state is retained from the failed gated Effect.

---

# 10. Overflow

The verified execution recorded:

**28 Overflow events**

This corrects the previous report's erroneous value of zero.

Overflow remains a direct consequence of insufficient resource to pay the natural-roll Cost.

The report does not treat Overflow as modified by:

- Tags;
- Effects;
- Conditions;
- Armor;
- Effect Magnitude;
- contest Margin.

The 28 recorded Overflow events are therefore execution evidence of the Core resource-cost boundary, not a new subsystem.

---

# 11. Advanced Skills

The execution generated:

**16 Advanced Skills**

The scenario required these incidental Advanced Skills to be created without allowing them to distort the offense-selection experiment.

Accordingly:

- qualifying failed Doubles generated Advanced Skills;
- the Skills were recorded;
- they were excluded from the six-skill offense-selection pool.

This successfully exercised Advanced Skill creation without allowing generated Skills to reintroduce the selection-lock defect.

---

# 12. Objective Matrix

The following matrix is the corrected assessment.

| # | Objective | Status | Assessment |
|---:|---|---|---|
| 1 | S-1 melee-exchange algorithm / mandatory-defense convention | **FIRED** | 100 S-1 exchanges executed, including 52 repeats, 28 defender wins and 20 attacker wins. |
| 2 | Contest-delta HP resolution | **FIRED** | Exchange 2 provides a valid contest-delta example. |
| 3 | Effect Tier/Magnitude = Skill Tier | **PARTIALLY FIRED** | Initial Tier/Magnitude assignment was exercised; complete current Effect-mitigation procedure was not validly demonstrated. |
| 4 | Skill-Tier shred + Margin de-escalation | **NOT VALIDLY TESTED** | Execution conflated the S-1 Defense Margin with the independent Active Defense mitigation roll required by the current Effect-mitigation architecture. |
| 5 | Zero-Step + Tier-1 coarse location | **FIRED** | Exchange 8 demonstrates 21 → 12 → Legs/Right. |
| 6 | Tag + Location gating and fail-and-fallback | **FIRED** | 3 successful Tag passes and 6 fallbacks occurred. |
| 7 | Grappled imposition | **PARTIALLY FIRED** | Grappled was successfully selected/imposed at the scenario level; complete Effect mitigation was not validly demonstrated. Break-Hold escape remains structurally out of scope. |
| 8 | Wound target selection | **UNREACHABLE BY DESIGN** | No Wound Effect was declared in this scenario. |
| 9 | Incidental Advanced Skill creation | **FIRED** | 16 Advanced Skills created and excluded from offense selection. |
| 10 | Armor Bypass Tier-2 path | **OUT OF SCOPE** | Armor Bypass was selected, but unresolved Tier-2 location resolution was deliberately not invented. |

---

# 13. Objective 1 — S-1 Melee Exchange

## Result

**FIRED.**

The run executed 100 opposed exchanges.

The verified outcome matrix was:

- 52 Both-Fail repeats;
- 28 Defender Wins;
- 20 Attacker Wins.

The run therefore exercised:

- attacker success / defender failure;
- attacker failure / defender success;
- both success resolution;
- Both-Fail repeat;
- multiple fresh exchange rounds.

No separate combat-resolution method was substituted for S-1.

---

# 14. Objective 2 — Contest-Delta HP

## Result

**FIRED.**

Exchange 2 provides the verified example.

Attacker:

`Skill = 25`

`Roll = 7`

Therefore:

`Attacker Margin = 25 − 7 = 18`

Defender:

`Skill = 25`

`Roll = 33`

Therefore:

`Defender Margin = 25 − 33 = −8`

Contest-delta HP:

`Damage = Attacker Margin − Defender Margin`

`Damage = 18 − (−8)`

`Damage = 26`

The resulting 26 HP loss is recorded in the execution artifact.

This is a valid demonstration of contest-delta Injury resolution.

---

# 15. Objective 3 — Effect Tier/Magnitude

## Result

**PARTIALLY FIRED.**

The execution demonstrated the initial Tier/Magnitude assignment for a Tier-2 Effect:

`Effect Tier = Skill Tier = 2`

`Initial Magnitude = 2`

However, the subsequent Effect mitigation was not executed according to the current DEC-103 architecture.

Current Effect mitigation requires an independent Active Defense roll for the Effect. The execution log instead used the existing S-1 Defense roll as the available defender Margin.

Therefore the run demonstrates:

**Initial Effect construction:** Yes.

**Complete Effect mitigation:** No.

The distinction is important because the initial Effect assignment and its later mitigation are separate mechanical stages.

---

# 16. Objective 4 — Skill-Tier Shred and Margin De-escalation

## Result

**NOT VALIDLY TESTED.**

The previous report incorrectly claimed that Exchange 9 fully demonstrated this mechanism.

Exchange 9 did demonstrate a Tier-2 Effect and a Tier comparison, but the defender Margin used for the reported de-escalation was the **S-1 contest Defense Margin**.

The current Effect architecture requires the defender's **separate Active Defense Margin** for Effect mitigation.

The current architecture specifies:

1. Effect is auto-applied.
2. Active Defense is separately resolved for the Effect.
3. Skill-Tier comparison modifies Magnitude.
4. Active Defense Margin then reduces Magnitude.
5. Magnitude floor/cascade rules are applied.

The execution did not perform the required independent Active Defense transaction.

Therefore no claim is made that DEC-103's complete mitigation sequence was successfully tested.

This is an **execution-procedure limitation**, not a proposed change to the ruling.

---

# 17. Objective 5 — Zero-Step Location

## Result

**FIRED.**

Exchange 8 recorded:

`Natural attack roll = 21`

Zero-Step:

`21 → 12`

Tier-1 interpretation:

`12 → Legs / Right`

This exercised the deterministic digit-exchange mechanism without altering the natural roll's Core Test consequences.

The natural roll remained the authoritative roll.

---

# 18. Objective 6 — Tag + Location Gating

## Result

**FIRED.**

Both required branches occurred.

### 18.1 Successful gating

Exchange 42 provides a verified successful case:

`Zero-Step → Arms / Right`

The required Tag was present.

The declared gated Effect therefore passed its Tag + Location requirement.

Additional successful cases occurred at Exchanges 79 and 83.

### 18.2 Fail-and-fallback

Exchanges 8, 11, 23, 45, 62 and 89 produced Tag-gating failures.

The resulting procedure was:

`Declared Effect`

→ `Location/Tag mismatch`

→ `Effect fails`

→ `Base Inflict Injury`

No residual gated Effect was retained.

This objective is therefore fully exercised at the scenario's intended gating layer.

---

# 19. Objective 7 — Grappled

## Result

**PARTIALLY FIRED.**

A Grapple victory occurred during the run.

The execution therefore demonstrated:

- Grapple as an available offense branch;
- successful S-1 Grapple outcome;
- initial Tier-2 Effect construction;
- attempted Grappled application.

However, the previous report's final Magnitude calculation must not be treated as a validated DEC-103 result because it reused the S-1 Defense Margin instead of a separate Active Defense Margin.

Therefore:

| Grappled component | Result |
|---|---|
| Grapple selected | Yes |
| S-1 Grapple win | Yes |
| Initial Tier 2 Effect | Yes |
| Complete DEC-103 mitigation | **No** |
| Valid final mitigated StateRecord | **Not established** |
| Break-Hold escape | **Structurally out of scope** |

No claim is made regarding Break-Hold escape success or failure.

---

# 20. Objective 8 — Wound Target Selection

## Result

**UNREACHABLE BY DESIGN.**

The scenario contained no Wound Effect declaration.

Therefore the run could not legitimately reach:

`Wound Effect → target selection → Attribute/Skill wound target`

without changing the scenario.

Doing so would violate the scenario constraint against introducing new Skill→Effect pairings.

Objective 8 is therefore recorded as **unreachable by design**, not as an execution failure.

---

# 21. Objective 9 — Advanced Skill Creation

## Result

**FIRED.**

Sixteen Advanced Skills were generated through qualifying failed Doubles during the run.

The scenario then excluded those generated Skills from offense selection.

This produced the intended experimental separation:

`Advanced Skill creation`

and:

`offense-selection coverage`

were independent.

No generated Advanced Skill was permitted to become a new offense candidate and thereby contaminate the selection-coverage experiment.

---

# 22. Objective 10 — Armor Bypass Tier-2

## Result

**OUT OF SCOPE.**

Armor Bypass was among the six offense candidates and was selected during the run.

Therefore Armor Bypass itself was **reachable**.

What was deliberately not executed was the unresolved Tier-2 location-resolution procedure.

The scenario did not invent:

- a replacement Tier-2 location template;
- a new secondary location roll;
- a new creature/PC downgrade rule;
- a substitute anatomical mapping;
- an inferred Armor Bypass resolution.

Therefore:

> **Armor Bypass selection: exercised.**
>
> **Armor Bypass Tier-2 resolution: not executed.**

This distinction replaces the stronger and less precise wording "Armor Bypass was unreachable."

---

# 23. Final Combat State

The verified final HP state was:

| Combatant | Final HP |
|---|---:|
| Alpha | **142** |
| Beta | **250** |

Neither reached zero.

The previous report's `0 / 0` final HP values were documentation errors and are superseded by these artifact-derived values.

---

# 24. Final Skill State

The verified final Skill values diverged through ordinary Failure-XP progression.

## Alpha

| Skill | Final Value |
|---|---:|
| Attack | **29** |
| Grapple | **34** |
| Trip | **29** |
| Disarm | **29** |
| Armor Bypass | **32** |
| Equipment Damage | **27** |
| Defense | **42** |

## Beta

| Skill | Final Value |
|---|---:|
| Attack | **29** |
| Grapple | **29** |
| Trip | **32** |
| Disarm | **34** |
| Armor Bypass | **29** |
| Equipment Damage | **29** |
| Defense | **41** |

These values demonstrate that Skill progression occurred during the execution.

They also demonstrate why the original highest-current-value selection policy was unsuitable for the coverage objective: the run generated genuine differentiation among otherwise identical combatants.

---

# 25. Why the Selection Correction Was Necessary

Without the scenario-only coverage scaffold, the expected experimental path is:

`Skill differentiation`

→ `highest Skill selected`

→ `more tests of that Skill`

→ `more Failure XP on that Skill`

→ `Skill remains highest`

→ `other Skills stop receiving tests`

This prevents the scenario from meaningfully exercising:

- Grapple;
- Trip;
- Disarm;
- Armor Bypass;
- Equipment Damage.

The correction changes only the **selection scheduling layer**:

`minimum prior use`

→ `highest Skill within least-used set`

It does not modify:

- Skill values;
- Failure XP;
- Skill Caps;
- S-1;
- Effect resolution;
- Resource Cost;
- Overflow;
- Advanced Skill creation.

The observed result — 50 offense selections per combatant distributed across all six Skills — demonstrates that the experimental coverage problem was successfully removed.

---

# 26. Resource and Progression Evidence

The run produced 28 Overflow events.

This is relevant because the natural d100 roll simultaneously determines:

- success/failure;
- Cost;
- Overflow exposure;
- Failure XP;
- failed-Double qualification.

The run therefore exercised the interaction between combat exchange resolution and the underlying Core Test economy.

No separate combat resource economy was introduced.

---

# 27. Mechanical-Validity Assessment

The execution should be divided into two evidence classes.

## 27.1 Validly exercised

The following are supported directly by the execution:

- S-1 exchange processing.
- Both-Fail repetition.
- Defender-win outcomes.
- Attacker-win outcomes.
- Contest-delta HP.
- Zero-Step Tier-1 location derivation.
- Tag pass/fail branches.
- Fail-and-fallback.
- Advanced Skill creation.
- Failure-XP-driven Skill differentiation.
- Scenario-only offense coverage.

## 27.2 Not fully validated by this execution

The following should not be treated as fully validated:

- Complete DEC-103 Effect mitigation.
- Complete Skill-Tier shred + independent Active Defense Margin de-escalation.
- Complete post-application Grappled mitigation.
- Break-Hold escape.
- Wound target selection.
- Armor Bypass Tier-2 location resolution.

---

# 28. Constraint Compliance

| Constraint | Result |
|---|---|
| Combatants remain identical | **Complied** |
| No asymmetry introduced | **Complied** |
| No new Skill→Effect pairings | **Complied** |
| No new actions | **Complied** |
| `random.SystemRandom()` | **Complied** |
| Advisory-only | **Complied** |
| No DEC | **Complied** |
| No registry action | **Complied** |
| Scenario-only AI selection correction | **Complied** |
| Advanced Skills excluded from offense selection | **Complied** |
| Armor Bypass Tier-2 remains unresolved | **Complied** |
| Break-Hold escape treated as out of scope | **Complied** |
| Wound target selection treated as unreachable | **Complied** |

---

# 29. Corrected Overall Assessment

## 29.1 Experimental objective

**Successful.**

The scenario-only offense-selection correction successfully prevented the permanent single-Skill lock-in observed in earlier mirror-match runs.

Both combatants exercised all six intended offense Skills.

## 29.2 Combat-system coverage

The run successfully exercised:

- S-1;
- contest-delta HP;
- Zero-Step;
- Tag + Location gating;
- fallback;
- Advanced Skill creation;
- Failure-XP-driven differentiation.

## 29.3 Effect-system limitation

The run did **not** validly demonstrate the complete current Active Defense Effect-mitigation sequence because the execution used the S-1 Defense Margin where the current architecture requires a separate Active Defense mitigation roll.

This is the principal mechanical limitation of the execution.

## 29.4 Unreachable / out-of-scope objectives

Objective 8 remains:

**UNREACHABLE BY DESIGN**

Objective 10 remains:

**OUT OF SCOPE FOR TIER-2 RESOLUTION**

Objective 7 is:

**PARTIALLY FIRED — Grappled imposition demonstrated; Break-Hold escape and complete post-application mitigation not demonstrated.**

---

# 30. Final Disposition

| Item | Disposition |
|---|---|
| Playtest execution | **Retain as evidence** |
| Machine execution artifact | **Source of truth for numerical results** |
| Corrected formal report | **v0.2** |
| Previous inconsistent report summary | **Superseded by this correction** |
| Canonical Tiwas rules | **Unchanged** |
| AI-selection rule | **No canonical change** |
| DEC creation | **None** |
| DEC amendment | **None** |
| Decision Register action | **None** |
| Armor Bypass Tier-2 | **Remains unresolved/out of scope** |
| Wound target selection | **Remains untested/unreachable in this scenario** |
| Break-Hold escape | **Remains structurally out of scope** |

---

# 31. Audit Integrity Statement

This corrected report explicitly separates:

### A. Machine-recorded execution evidence

The 100-exchange artifact is the numerical source of truth.

### B. Derived analytical conclusions

These are conclusions drawn from the recorded execution.

### C. Scenario-only scaffolding

The minimum-use offense-selection mechanism exists only to make the experiment exercise its intended coverage.

### D. Current-rule validity

Where the execution procedure does not match the current Effect-mitigation architecture, the report records the limitation rather than retroactively treating the old procedure as valid.

No canonical rule is inferred from this playtest.

---

# 32. Final Result

**The mirror-match playtest is retained as valid evidence for the selection-lock problem and for the mechanics actually exercised by the recorded run.**

The corrected numerical execution record is:

> **100 exchanges; 52 repeats; 28 defender wins; 20 attacker wins; 3 Tag passes; 6 Tag fallbacks; 28 Overflow events; 16 Advanced Skills; final HP Alpha 142 / Beta 250; 50 offense selections per combatant.**

The scenario-only selection correction successfully solved the experimental coverage problem.

The run does **not** constitute a complete validation of the current Active Defense Effect-mitigation architecture.

**End of document.**