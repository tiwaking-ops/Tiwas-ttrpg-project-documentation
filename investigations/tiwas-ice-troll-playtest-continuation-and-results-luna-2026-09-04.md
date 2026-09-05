---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest Continuation and Results Report"
  status: "Advisory working document (not canonical). Playtest evidence only; records results, designer override, continuation, and unresolved mechanics. Makes no rulings, assigns no DEC numbers, promotes nothing."
provenance:
  author_llm: {name: "GPT-5.6 Luna", version: "gpt-5.6-luna"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
---

# Tiwas TTRPG — Ice Troll Combat Playtest Continuation and Results Report

## 1. Document Control

| Field | Value |
|---|---|
| **Project** | Tiwas TTRPG |
| **Document Type** | Formal Project Documentation / Combat Playtest Results |
| **Document Status** | Recorded Result — Non-Canonical Playtest Evidence |
| **Date** | 2026-09-04 |
| **Author** | GPT-5.6 Luna |
| **Purpose** | Record the results, designer override, execution continuation, system observations, and unresolved mechanics arising from the Ice Troll combat playtest |
| **Audience** | OpenCode / Tiwas TTRPG project documentation system |
| **Authority Level** | Playtest evidence only; no new canonical mechanics established |
| **Source Context** | `claude-playtest-prompt-version2.md`, Claude combat execution, subsequent Designer Override and combat continuation |

---

# 2. Executive Summary

A combat playtest of the Tiwas TTRPG Ice Troll conversion was continued following an explicit Designer Override:

> **“Round 1, Exchange 1 — PC attacks”**

The override was applied solely to establish the opening sequence of this playtest. It does **not** establish a general Tiwas initiative, turn-order, round-structure, or action-economy rule.

The combat continuation proceeded through multiple rounds and ultimately reached:

> **Adventurer-1 HP = 0 — incapacitated.**

The recorded combat result was therefore:

> **ICE TROLL VICTORY**

The extended test exercised interactions among:

- d100 roll-under resolution;
- skill expenditure;
- Physical Energy expenditure;
- Overflow → HP;
- failure XP;
- Skill Roll Pool cascade;
- failed-double Advanced Skill creation;
- opposed contests;
- Active Defense;
- Zero-Step Location Index;
- Effect/Condition application;
- Frightened;
- Wound handling;
- HP depletion and incapacitation.

However, several combat mechanisms remained dependent upon **explicitly identified non-canonical scaffolds**.

Accordingly, this playtest must **not** be recorded as validation that the complete Tiwas combat system is canonical or complete.

---

# 3. Governing Rule

## 3.1 Designer Override

The following explicit Designer Override was issued:

> **“Round 1, Exchange 1 — PC attacks”**

For purposes of this execution, this authorises the playtest referee to begin with the PC attack.

### Scope restriction

The override is:

- specific to this playtest;
- specific to the opening sequence;
- not a general combat-order ruling;
- not a new Decision;
- not a modification of the Canonical Rules;
- not evidence establishing a permanent initiative system.

OpenCode must therefore **not promote the override into a canonical rule**.

---

# 4. Pre-Combat State

## 4.1 Adventurer-1

| Statistic | Value |
|---|---:|
| Attributes | 24 × 50 |
| HP | 600 |
| MP | 600 |
| Physical Energy | 150 |
| Attack1 | Tier 2 / Cap 50 / Start 25 |
| Defence1 | Tier 2 / Cap 50 / Start 25 |

The pre-authored Tier-2 Attack1 and Defence1 skills remain a **playtest-only prompt scaffold** and do not establish a general PC exception to the normal Advanced Skill creation rules.

---

## 4.2 Ice Troll

| Statistic | Value |
|---|---:|
| HP | 705 |
| MP | 420 |
| Physical Energy | 220 |
| Icy Claws | Tier 2 / Cap 67 / Current 67 |
| Sharktoothed Maw | Tier 2 / Cap 75 / Current 75 |
| Brawling | Tier 1 / Current approximately 37 at combat start |
| Regeneration / Regrowth | Inactive |
| DR 2 | Inactive |

The freezing-dependent abilities were not activated because the required environmental condition was not established.

---

# 5. Previously Completed Combat Segment

Before the Designer Override continuation, Claude's execution had completed four exchanges.

| Exchange | Attacker | Result | Principal Effect |
|---:|---|---|---|
| 1 | PC | PC wins | Troll −7 HP |
| 2 | Troll | Troll wins | Torso Tier-2 Wound |
| 3 | PC | Failed Double at 100 | Overflow −2 PC HP; Advanced Skill created |
| 4 | Troll | Troll wins | Frightened Tier-2 |

The state entering the continuation was recorded as:

| Statistic | Adventurer-1 | Ice Troll |
|---|---:|---:|
| HP | 585 | 698 |
| Physical Energy | 50 | 220 |
| Attack1 | 27 | — |
| Defence1 | 29 | — |

The PC remained subject to the previously applied **Frightened −2 Skill modifier**.

---

# 6. Combat Continuation

## 6.1 Execution Principle

The continuation treated the Designer Override as authorising the combat sequence and continued alternating PC and Troll attacks.

The following categories remained explicitly non-canonical where the corpus had not established a definitive numerical rule:

| Mechanism | Status |
|---|---|
| Inflict Injury magnitude | Scaffold |
| Active Defense mitigation | Scaffold |
| Creature defensive-skill substitution | Scaffold |
| Location-zone numerical ranges | Scaffold |
| Quality threshold for gated Effects | Scaffold |
| Defender-winning opposed attack consequence | Interpretive gap |
| General combat action sequencing | Not established by this override |

No such scaffold is to be promoted automatically into the canonical rules.

---

# 7. Combat Progression

The continuation produced the following principal state progression.

| Stage | Round / Exchange | PC HP | Troll HP | Principal Event |
|---|---:|---:|---:|---|
| Continuation start | — | 585 | 698 | Designer Override applied |
| First continuation phase | R1 | 556 | 681 | PC and Troll exchanges |
| Second phase | R2 | 540 | 666 | Further opposed contests |
| Mid-combat | R3–R5 | 269 | 623 | Repeated attacks, defenses and Effects |
| Later combat | R6–R8 | 106 | 587 | Additional exchanges |
| Late combat | R9–R10 | 37 | 569 | PC approaches incapacitation |
| Termination phase | R11 | **0** | **569** | PC reaches incapacitation |

The continuation therefore terminated with:

\[
HP_{PC}=0
\]

and:

\[
HP_{Troll}=569
\]

---

# 8. Advanced Skill Development During Combat

Additional failed Doubles occurred during the continuation.

The recorded results included further Advanced Skill creation.

## 8.1 First Additional Advanced Skill

A failed `99` occurred while Attack1 had an effective value of 30.

Failure XP:

\[
XP=99-30=69
\]

Skill Roll Pool cascade:

\[
30\rightarrow31
\]

Cost:

\[
30
\]

Remaining:

\[
69-30=39
\]

Second increase:

\[
31\rightarrow32
\]

Cost:

\[
31
\]

Remaining:

\[
39-31=8
\]

Therefore:

\[
Attack1=32
\]

and:

\[
GeneralXP=8
\]

The failed Double also triggered creation of a Tier-3 Advanced Skill.

The continuation recorded:

> **Skill-(29), Tier 3, Cap 70, Starting Value 34**

This naming convention is a playtest identifier and is **not a canonical skill name**.

---

# 9. Demonstrated Mechanical Interactions

The combined combat test exercised the following interactions.

| System | Exercise Status |
|---|---|
| d100 roll-under | Exercised |
| Skill success/failure | Exercised |
| Exact roll-based exertion cost | Exercised |
| Physical Energy depletion | Exercised |
| Overflow → HP | Exercised |
| Failure XP | Exercised |
| Skill Roll Pool cascade | Exercised |
| General XP remainder | Exercised |
| Failed Double | Exercised |
| Advanced Skill generation | Exercised |
| Zero-Step Location Index | Exercised |
| Opposed contest | Exercised |
| Active Defense | Exercised |
| Wound representation | Exercised |
| Frightened Condition | Exercised |
| HP reduction | Exercised |
| HP = 0 incapacitation endpoint | Exercised |

### Validation qualification

“Exercised” means that the execution reached the corresponding mechanical pathway.

It does **not** mean that every numerical parameter governing that pathway has been validated as canonical.

---

# 10. Non-Canonical Scaffolds

The following must remain explicitly classified as scaffolds.

## 10.1 Inflict Injury

The playtest used:

\[
Damage=Winner\ Margin
\]

for straightforward Success/Failure outcomes.

This is an execution scaffold, not a locked Tiwas damage rule.

---

## 10.2 Active Defense

The playtest used:

\[
Mitigation=Defender\ Margin
\]

on a successful Active Defense and:

\[
Mitigation=0
\]

on failure.

This remains a scaffold pending formal ruling.

---

## 10.3 Creature Defensive Skill

The Ice Troll's Brawling skill was used as its defensive skill because the supplied creature block did not provide a dedicated defensive skill.

This is a referee construction choice.

It must not be interpreted as establishing:

> Brawling is universally the Ice Troll's Tiwas defensive skill.

---

## 10.4 Location Zones

The continuation used the playtest zone mapping:

| Location Index | Zone |
|---:|---|
| 1–25 | Legs |
| 26–50 | Torso |
| 51–75 | Arms |
| 76–100 | Head |

These numerical ranges remain scaffolded.

---

## 10.5 Quality Threshold

The continuation used the playtest threshold:

\[
Quality\ge1
\]

for Base-tier Effects and:

\[
Quality\ge10
\]

for gated tiers.

These values were not promoted to canonical status.

---

# 11. Unresolved Mechanics

The playtest continued despite several unresolved mechanisms. These remain project investigation targets.

## 11.1 General Combat Sequencing

The Designer Override solved the immediate test-start problem only.

It did **not** resolve:

- initiative;
- permanent actor ordering;
- exchange construction;
- round construction;
- simultaneous declarations;
- ties;
- action availability;
- number of actions;
- timing of Active Defense relative to other actions.

### Status

**UNRESOLVED**

---

## 11.2 Passive Frightened Trigger

The Ice Troll's frightening appearance was identified as corresponding to a passive Fright Check in the source material, but no canonical Tiwas trigger was established for this event.

The combat therefore did not invent a passive trigger.

### Status

**GM/DESIGNER RULING REQUIRED**

---

## 11.3 Defender-Wins Attack Contest

The playtest encountered the interpretive question:

> If the defender wins an opposed attack contest, does the defender receive an Effect opportunity, or does the attack simply fail?

The conservative interpretation was:

> **Attack fails; no counter-Effect is generated.**

This was explicitly treated as interpretation rather than a new rule.

### Status

**UNRESOLVED**

---

# 12. Combat Termination

The playtest ended when:

\[
Adventurer\text{-}1\ HP=0
\]

The final recorded state was:

| Statistic | Adventurer-1 | Ice Troll |
|---|---:|---:|
| HP | **0** | **569** |
| Status | **Incapacitated** | **Active** |
| Combat Result | **Defeat** | **Victory** |

No further combat exchanges should be generated after this termination point unless a separate recovery/resolution procedure is formally invoked.

---

# 13. Evidence Classification

OpenCode must classify the results according to the following hierarchy.

| Classification | Meaning |
|---|---|
| **Canonical Rule** | Existing authoritative Tiwas rule |
| **Designer Override** | Explicit temporary authorisation for this execution |
| **Playtest Observation** | Something demonstrably occurred during the test |
| **Scaffold** | Temporary value required to execute an otherwise incomplete pathway |
| **Interpretive Gap** | Missing rule where execution required an interpretation |
| **Unresolved** | Requires future investigation/ruling |

The combat result belongs primarily to:

> **Playtest Observation / Integration Evidence**

It does **not** constitute a new Canonical Rule.

---

# 14. Governance Restrictions

OpenCode MUST NOT:

1. Promote any playtest scaffold to a DEC automatically.
2. Treat the Designer Override as a permanent combat-sequencing rule.
3. Treat Brawling as an authoritative universal defensive skill for Ice Trolls.
4. Treat the location-zone ranges as canonical.
5. Treat the Quality thresholds as canonical.
6. Treat Margin-based damage as a final damage equation.
7. Treat Margin-based Active Defense mitigation as a final mitigation equation.
8. Treat the PC's pre-authored Tier-2 skills as precedent for general PC character construction.
9. Treat the playtest's generated skill names as canonical skill names.
10. Resolve the passive Frightened trigger without explicit authority.
11. Resolve defender counter-Effects without explicit authority.
12. Rewrite the Canonical Rules solely because the combat simulation required a scaffold.

---

# 15. Formal Findings

## Finding F-01 — Core Engine Integration

The combat test demonstrated that the existing Tiwas core transaction can be driven through a multi-exchange combat scenario.

**Classification:** Playtest Observation.

---

## Finding F-02 — Failure Progression

The combat successfully exercised failure XP, cascading skill improvement, General XP remainder, and failed-Double Advanced Skill creation during live combat.

**Classification:** Playtest Observation.

---

## Finding F-03 — Resource Consequences

The combat demonstrated that high d100 results can simultaneously produce:

- large resource expenditure;
- failure;
- XP generation;
- possible Overflow;
- HP damage.

**Classification:** Playtest Observation.

---

## Finding F-04 — Combat Dependency Gaps

The combat cannot presently be regarded as fully deterministic under the complete Tiwas corpus because several combat-layer decisions remain incomplete.

**Classification:** Confirmed design gap.

---

## Finding F-05 — Designer Override Scope

The explicit instruction:

> “Round 1, Exchange 1 — PC attacks”

was sufficient to authorise the immediate test sequence but does not establish a general combat action-order system.

**Classification:** Designer Override; non-canonical.

---

## Finding F-06 — Incapacitation Endpoint

The playtest reached HP = 0 and terminated with the Adventurer incapacitated and the Ice Troll still active.

**Classification:** Playtest Observation.

---

# 16. Recommended OpenCode Record

The following status should be recorded in the project tracking system:

```yaml
playtest:
  name: "Ice Troll Combat Playtest"
  date: "2026-09-04"
  status: "COMPLETED_WITH_IDENTIFIED_RULE_GAPS"
  result:
    winner: "Ice Troll"
    loser: "Adventurer-1"
    termination: "Adventurer-1 HP reached 0"
    final_hp:
      adventurer_1: 0
      ice_troll: 569

  designer_override:
    text: "Round 1, Exchange 1 — PC attacks"
    scope: "playtest-only"
    canonical_status: "not_canonical"

  evidence:
    core_resolution: "exercised"
    failure_xp: "exercised"
    xp_cascade: "exercised"
    advanced_skill_creation: "exercised"
    overflow: "exercised"
    active_defense: "exercised_with_scaffold"
    location_index: "exercised_with_scaffold"
    wound: "exercised_with_scaffold"
    frightened: "exercised"
    incapacitation: "exercised"

  unresolved:
    - "general combat action sequencing"
    - "passive Frightened trigger"
    - "defender-wins opposed attack consequence"
    - "Inflict Injury magnitude"
    - "Active Defense mitigation"
    - "location zone numerical ranges"
    - "Quality thresholds"
    - "creature defensive-skill substitution"

  governance:
    promote_scaffolds_to_canonical: false
    create_decisions_automatically: false
    treat_override_as_general_rule: false
```

---

# 17. Final Project Status

## **ICE TROLL COMBAT PLAYTEST — COMPLETED**

### Result

**Ice Troll victory; Adventurer-1 incapacitated at HP 0.**

### Evidence value

**High for integration testing.**

### Canonical-system validation

**Partial.**

### New canonical mechanics established

**None.**

### Designer Overrides

**One — opening sequence only.**

### Scaffolds promoted

**None.**

### Outstanding investigation areas

**Multiple combat-layer gaps remain.**

---

# 18. Authoritative Interpretation for OpenCode

This document records **what happened during the playtest**.

It does not declare that every rule used during the playtest is part of Tiwas.

Where the execution required a missing numerical value, skill substitution, threshold, or interpretation, that item remains explicitly classified as a **scaffold or unresolved gap**.

The Designer Override authorised the playtest to proceed from:

> **Round 1, Exchange 1 — PC attacks**

but did not close the broader combat action-economy investigation.

**No canonical Tiwas rule is changed by this report.**

---

## Documentarian Verification (added by OpenCode, 2026-09-04)

Stored at Tiwa's instruction from the repo-root working file `Tiwas TTRPG — Ice Troll Combat Playtest Continuation and Results Report.md`, moved to `investigations/` as `tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md` (byte-identical; the root working copy was removed). A YAML provenance block was added at the top of the stored copy (the working file carried only a Document Control table) — `author_llm` set to GPT-5.6 Luna per the document's own self-declared "Author" field, with opencode appended as `assessor_llm` and `last_modified_by_llm` for the storage/assessment pass. Advisory playtest evidence only.

**Assessment summary — the report is disciplined, internally consistent, and correctly refuses to promote any scope:**

1. **Continuation lineage (IMPORTANT for cross-referencing):** This GPT-5.6 Luna report is explicitly a **continuation** of the Claude Sonnet 5 execution's abort state (Claude handoff ends PC 585 / Troll 698; Luna §5 records the same 585/698 entering-state and continues to PC 0 / Troll 569 → Ice Troll victory). This is one execution lineage (Claude→Luna), **distinct from** Grok 4.5's separate full 22-round run (`tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md`, ending Troll 412). When Tiwa reviews outcomes, the three records must be cross-referenced by lineage, not conflated.

2. **Designer Override scope correctly contained (§3.1, F-05, §14-2):** "Round 1, Exchange 1 — PC attacks" is explicitly recorded as playtest-only, opening-sequence-specific, non-canonical, and **must not** be promoted into a general combat-sequencing rule. This correctly preserves the SC-04/initiative gap as unresolved. Consistent with DEC-082 (Time/Action economy expression only; no sequencing procedure ruled).

3. **Scaffold classification (all non-canonical, correctly non-promotable):** Inflict Injury = winner's Margin; Active Defense = defender's Margin on success / 0 on failure; Brawling as the creature's defensive-skill substitute; Location zone quartiles (1–25/26–50/51–75/76–100); Quality threshold ≥1 Base / ≥10 gated; defender-wins interpretive gap (conservatively "attack fails, no counter-Effect"). All match the Claude handoff's §4 scaffolds and §5 ambiguity — **good cross-model convergence** — and all are marked non-canonical per §10/§14/§16 governance.

4. **Governance compliance (§14, §16, §18):** The report's explicit "OpenCode MUST NOT" list (no automatic scaffold promotion, no override-as-general-rule, no Brawling-universal, no zone/Quality/Margin canonisation, no auto-DEC) aligns exactly with the project's standing reconfirmation-before-recording rule and AGENTS.md authority constraints. No mechanics invented as canon.

5. **New candidate item aligned with handoff:** The Luna report's unresolved list (general combat sequencing; passive Frightened trigger; defender-wins consequence; Inflict Injury magnitude; Active Defense mitigation; location-zone ranges; Quality thresholds; creature defensive-skill substitution) maps 1:1 onto the Claude handoff's CANDIDATE-01…09. No cross-report contradiction in candidate scope.

**Open items carried forward for OpenCode/Tiwa:** (a) reconcile the three execution records by lineage before acting on any single outcome; (b) repeat CANDIDATE-01…09 back to Tiwa for per-item ruling before any register recording; (c) treat the Designer Override strictly as playtest-only, never as precedent for combat-order rules; (d) resolve the passive Frightened trigger (C-04) and defender-wins consequence (C-09) only on explicit Tiwa authority.

**Scope note:** advisory recording only. `author_llm` remains GPT-5.6 Luna (preserved). No register, governance, or other repository files were modified.