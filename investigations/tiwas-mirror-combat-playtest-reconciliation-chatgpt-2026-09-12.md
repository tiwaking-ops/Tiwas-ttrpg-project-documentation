---
document:
  title: "Mirror-Match Combat Stress Test — Reconciliation Finding (ChatGPT cross-check)"
  version: "1.0 (as-provided)"
  document_type: "Reconciliation / LLM cross-check of the stored playtest report"
  status: "Advisory / Non-canonical"
  authority: "Non-authoritative LLM analysis"
  canonical_status: "No canonical rule change"
  dec_status: "No DEC assigned or proposed by this document"
  registry_status: "No Decision Register action"
provenance:
  author_llm:
    name: "ChatGPT"
    version: "not stated"
  assessed_by_llm:
    name: "opencode"
    version: "big-pickle"
  source_report: "Tiwas — Mirror-Match Combat Stress Test_ Complete Playtest Results.md (stored investigation)"
  source_log: "tiwas-mirror-combat-playtest-results-v0.2.md (stored investigation)"
  source_design_brief: "tiwas-playtest-mirror-combat-design-brief-2026-09-10.md"
  created_date: "2026-09-12"
  last_modified_by_llm:
    name: "opencode"
    version: "big-pickle"
  last_modified_date: "2026-09-12"
---

# Reconciliation Finding

> **NON-CANONICAL ADVISORY CROSS-CHECK.** This document is a verbatim
> transcription of an LLM reconciliation (ChatGPT) of the stored playtest report
> `Tiwas — Mirror-Match Combat Stress Test_ Complete Playtest Results.md` and its
> associated log. It is not a Tiwas rule proposal, DEC, ruling, or registry
> action. LLM analysis does not establish authority.

The execution summary in the previous report is **not internally reliable as written**. The main problem is that the report treated the 100-exchange run as though it simultaneously followed the brief's combat procedure and the newer ruled DEC-103/105 architecture. Those are not fully compatible.

The source brief itself says that its exchange uses a **single pair of rolls**, with no separate Active Defense roll.  However, the current Decision Register states that DEC-103 requires a **separate voluntary Active Defense roll for an applied Effect**, while DEC-105 says each Effect gets its own independent AD roll and that defense is voluntary in live play but mandatory for playtests.

Therefore the previous report overstated what Objectives 3, 4, and 7 demonstrated.

## 1. The 100-exchange result is not a termination result

The report states:

> `Exchanges executed = 100`

and final HP:

> Alpha 142 / Beta 250

The source brief says the default termination condition is **first HP ≤ 0**, but explicitly leaves the actual stopping convention to the eventual execution.

The run therefore evidently used a **100-exchange execution cap**, because neither combatant reached 0 HP.

That is not inherently invalid, but the report failed to state that clearly.

**Correct interpretation:**

| Item                          | Correct status                                        |
| ----------------------------- | ----------------------------------------------------- |
| 100 exchanges                 | Executed                                              |
| Combat reached HP termination | **No**                                                |
| Alpha incapacitated           | No                                                    |
| Beta incapacitated            | No                                                    |
| 100-exchange cap              | **Execution parameter**, not source-brief termination |
| Final HP 142/250              | Valid state at imposed execution boundary             |

The report must not describe the run as having followed first-HP≤0 termination.

## 2. Objective 2 Is Valid

The Exchange 2 calculation is internally consistent:

* Beta Attack = 25
* Roll = 7
* Attacker Margin = 18
* Alpha Defense = 25
* Roll = 33
* Defender Margin = −8
* Damage = `18 − (−8) = 26`

This matches the brief's contest-delta formulation and DEC-104.

**Objective 2: FIRED.**

## 3. Objective 3 Was Only Partially Tested

The previous report said Objective 3:

> Effect Tier/Magnitude = Skill Tier — FIRED

That needs qualification.

The execution did establish the **initial Effect Tier/Magnitude assignment**:

`Skill Tier 2 → Effect Tier 2 / initial Magnitude 2`

That is supported by the brief.

However, the report treated the subsequent mitigation processing as though the complete DEC-103 mechanism had been executed.

It was not.

DEC-103 requires:

1. Effect is applied.
2. Defender may make an **independent Active Defense roll**.
3. That AD roll supplies the Defender's Margin for Effect mitigation.
4. Skill-Tier shred occurs.
5. AD Margin de-escalation occurs.
6. Floor/cascade rules are applied.

The execution instead used the **S-1 contest's Defense roll** as the only defender roll, exactly as the source brief instructed. The brief explicitly says there is no separate third Active Defense roll.

Therefore:

**Objective 3: PARTIALLY FIRED — initial Tier/Magnitude assignment demonstrated; complete DEC-103 Effect-mitigation path not demonstrated.**

## 4. Objective 4 Is Not Validly Fired

This is the largest mechanical error in the previous report.

The report claimed:

> Exchange 9: Trip won with attacker Margin 16 and successful Defense Margin 3.

and then used that `3` as the mitigation Margin.

But the row shows:

`Trip 25 vs roll 9 → attacker Margin 16`

and:

`Defense 28 vs roll 25 → defender Margin 3`

That `3` is the **S-1 contest Defense Margin**.

Under DEC-103, however, the Effect's mitigation Margin comes from the **separate Active Defense roll**, not the S-1 contest-participant roll.

No such independent AD roll occurred.

Consequently the reported sequence:

`2 → 1 → -2 → Tier cascade`

is not a valid execution of DEC-103.

There is an additional numerical error in the prose. Starting from Magnitude 1:

`1 − 3 = −2`

The report then says this invokes the floor/cascade rule, but the resulting stated record is inconsistent with the canonical rule because the actual DEC-103 process requires the AD roll and its Margin first. The report cannot simply substitute the S-1 Defense Margin.

**Objective 4 must therefore be changed from FIRED to:**

> **NOT VALIDLY TESTED — execution conflated the S-1 contest Defense roll with the separate DEC-103 Active Defense roll.**

This is a **procedural execution defect**, not evidence that DEC-103 itself failed.

## 5. Objective 7 Has the Same Problem

The report states:

> Exchange 4: Grappled Tier 2 / Magnitude -2.

But Exchange 4 was:

`Grapple 25, roll 20 → Margin 5`

against:

`Defense 25, roll 54 → Margin -29`

The report then says:

> Equal Tier-2 shred: Magnitude 2 → 1.

That part is the initial Skill-Tier shred.

But it then says:

> Defender Margin -29 is negative, so margin de-escalation increases the working magnitude to 30

which is **not a legitimate substitute for the DEC-103 AD process**.

The current ruled architecture says the defender's mitigation Margin comes from the independent Active Defense roll.

Therefore the correct finding is:

| Grappled component                           | Result                         |
| -------------------------------------------- | ------------------------------ |
| Successful S-1 Grapple contest               | **Yes**                        |
| Grappled Effect selected/applied in scenario | **Yes**                        |
| Initial Tier 2 / Magnitude 2                 | **Yes**                        |
| Equal-Tier shred                             | **Yes, as initial processing** |
| Independent AD mitigation                    | **Not executed**               |
| Valid final DEC-103 Grappled StateRecord     | **No**                         |
| Break-Hold escape                            | Out of scope                   |

Thus Objective 7's requested **Grappled-imposition half** fired at the S-1/Effect-selection level, but the previous report was wrong to present the resulting `Magnitude -2` record as fully validated.

## 6. Objective 6 Remains Valid, With One Boundary

The Tag/location evidence is internally coherent.

For example, Exchange 8:

`21 → Zero-Step 12 → Legs / Right`

followed by Tag mismatch and fallback to Injury.

The source brief explicitly defines that fallback path.

Exchange 42 similarly records:

`62 → Arms / Right → Tag pass`

Therefore:

**Objective 6: FIRED.**

The Tag/location gate itself does not depend on inventing the missing Armor Bypass Tier-2 machinery.

## 7. Objective 5 Remains Valid

Exchange 8 correctly demonstrates:

`Natural roll 21 → Zero-Step 12 → Legs / Right`

This is within the brief's Tier-1 location procedure.

**Objective 5: FIRED.**

## 8. Objective 9 Remains Plausible but Needs Correct Wording

The run recorded **16 Advanced Skills**.

The important constraint was that generated Advanced Skills were excluded from offense selection.

That was respected by the execution.

However, the previous report should avoid implying that Advanced Skill creation itself proves every downstream Advanced Skill rule. What was actually exercised was:

* qualifying failed doubles;
* Advanced Skill creation;
* random unused Attribute selection;
* Tier increase;
* starting value 1;
* exclusion from the scenario's offense-selection pool.

The source brief explicitly requires those execution behaviors.

**Objective 9: FIRED**, limited to those recorded behaviors.

## 9. The Offense-Coverage Result Is Valid

This part of the previous report remains useful.

The six offense Skills were distributed across the run:

| Skill            | Alpha | Beta |
| ---------------- | ----: | ---: |
| Attack           |     8 |    8 |
| Grapple          |     9 |    8 |
| Trip             |     8 |    9 |
| Disarm           |     8 |    9 |
| Armor Bypass     |     9 |    8 |
| Equipment Damage |     8 |    8 |

So the scenario-only minimum-use selection correction **did achieve its intended experimental purpose**: it prevented permanent single-Skill lock-in.

That is a legitimate playtest observation.

It should, however, be described as evidence about the **scenario-selection scaffold**, not evidence for a Tiwas rule.

## 10. Armor Bypass Status Is Correct

Armor Bypass was selected, including attacker-win cases, but the Tier-2 location path was not resolved.

That is consistent with the source brief's explicit §8.5 unresolved contradiction.

Therefore:

**Objective 10: OUT OF SCOPE / NOT EXECUTED.**

It should not be called "unreachable" in the strongest sense, because Armor Bypass itself was reachable as a selected Effect. What was unavailable was **valid Tier-2 resolution**.

The more precise label is:

> **Reachable as a selected Effect; Tier-2 resolution deliberately not executed because required location machinery is unresolved.**

## 11. Corrected Objective Matrix

The previous report should therefore be reconciled to:

|  # | Objective                               | Correct status            | Reason                                                                                     |
| -: | --------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------ |
|  1 | S-1 melee exchange                      | **FIRED**                 | S-1 exchanges and repeat branches occurred.                                                |
|  2 | Contest-delta HP                        | **FIRED**                 | Exchange 2 provides valid contest-delta evidence.                                          |
|  3 | Effect Tier/Magnitude                   | **PARTIALLY FIRED**       | Initial Skill-Tier assignment occurred; complete DEC-103 mitigation did not.               |
|  4 | Skill-Tier shred + margin de-escalation | **NOT VALIDLY TESTED**    | S-1 Defense Margin was incorrectly substituted for independent AD Margin.                  |
|  5 | Zero-Step + Tier-1 location             | **FIRED**                 | Valid Tier-1 location examples occurred.                                                   |
|  6 | Tag + Location gating/fallback          | **FIRED**                 | Both pass and fallback occurred.                                                           |
|  7 | Grappled imposition                     | **FIRED — partial**       | Grapple win occurred; complete post-application DEC-103 mitigation was not validly tested. |
|  8 | Wound target selection                  | **UNREACHABLE BY DESIGN** | No Wound Effect was declared.                                                              |
|  9 | Advanced Skill creation                 | **FIRED**                 | 16 qualifying creations recorded; excluded from selection.                                 |
| 10 | Armor Bypass Tier-2                     | **OUT OF SCOPE**          | Tier-2 location resolution deliberately not executed.                                      |

## 12. Corrected Execution Summary

The authoritative summary should therefore read:

| Metric                         |                            Correct interpretation |
| ------------------------------ | ------------------------------------------------: |
| Exchanges executed             |                                           **100** |
| Execution boundary             |                              **100-exchange cap** |
| HP termination reached         |                                            **No** |
| Final Alpha HP                 |                                           **142** |
| Final Beta HP                  |                                           **250** |
| S-1 repeats                    |                                            **52** |
| Defender wins                  |                                            **28** |
| Attacker wins                  |                                            **20** |
| Tag passes                     |                                             **3** |
| Tag fail-and-fallback          |                                             **6** |
| Advanced Skills created        |                                            **16** |
| Overflow events                |                                            **28** |
| Permanent single-Skill lock-in | **Prevented by scenario-only selection scaffold** |

The counts reconcile:

`52 + 28 + 20 = 100`

and:

`3 + 6 = 9` Tag-gated attacker-win events.

## 13. Most Important Correction

The previous report should **not** say:

> "Objectives 1–6 and 9 fired. Objective 7's Grappled-imposition half fired."

without qualification.

The defensible conclusion is:

> **Objectives 1, 2, 5, 6, and 9 fired. Objective 3 was partially exercised at the initial Effect Tier/Magnitude stage. Objective 4 was not validly tested because the execution conflated the S-1 Defense roll with the separate DEC-103 Active Defense roll. Objective 7's Grappled-imposition event occurred, but its complete Effect-resolution result was not validly tested for the same reason. Objective 8 was unreachable by design. Objective 10 was deliberately left unresolved/out of scope.**

This is the key reconciliation.

The underlying problem is **not merely wording in the report**: the executed procedure itself needs to be distinguished from the current ruled DEC-103/105 architecture. The source brief explicitly prescribed a single defender roll, while the later ruled architecture requires the independent Active Defense roll.

That discrepancy should be preserved as an **execution/provenance issue**, not silently corrected retroactively.

---

# Appendix — OpenCode verification note (2026-09-12)

> The key factual claims of the reconciliation above were checked by OpenCode
> against the stored artifacts and confirmed:

- **Brief §4.2** (`tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`,
  lines 109–113): single S-1 contest supplies both Margins; "there is no
  separate third 'Active Defense' roll".
- **Brief §4.3** (lines 143–148): default stopping condition "first HP ≤ 0";
  **no round cap set** — a fixed cap is the executor's choice.
- **DEC-103 register row** (`_consolidation/decision-register.md`, line 134):
  mitigation uses a voluntary DEC-044 Active Defense roll; Margin =
  AD Skill − Roll; failed AD → mitigation 0.
- **Artifact log** (`tiwas-mirror-combat-playtest-results-v0.2.md`): Ex4
  (line 382) Grapple roll 20 / Margin 5 vs Defense roll 54 / Margin −29;
  Ex9 (line 392) Trip roll 9 / Margin 16 vs Defense roll 25 / Margin 3;
  Ex100 (line 574) shows final HP Alpha 142 / Beta 250. The log contains **no
  independent AD roll column** — the S-1 Defense roll is the only defender roll.
- **Report §11** (`Tiwas — Mirror-Match Combat Stress Test_ Complete Playtest
  Results.md`, lines 354–363): Objective 3, 4, 7 all claimed "FIRED" — the
  overstated claims the reconciliation corrects.

This reconciliation preserves the execution/provenance discrepancy; it does not
retroactively rewrite the stored report or log. Neither this document nor the
report and log carry authority; no DEC is created or inferred.