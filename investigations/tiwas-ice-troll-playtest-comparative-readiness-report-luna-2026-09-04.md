---
document:
  title: "Tiwas TTRPG â€” Cross-LLM Combat Playtest Comparative Systems Readiness Report"
  version: "1.0"
  status: "Advisory working document (not canonical). Cross-playtest empirical assessment; makes no rulings, assigns no DEC numbers, promotes nothing."
provenance:
  author_llm: {name: "GPT-5.6 Luna", version: "gpt-5.6-luna"}
  assessor_llm: [{name: "opencode", version: "big-pickle"}]
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
---

# Tiwas TTRPG â€” Cross-LLM Combat Playtest Comparative Systems Readiness Report

## 1. Executive Summary

### 1.1 Purpose

This report collates, contrasts, and cross-references the three Ice Troll combat-playtest execution records contained within the merged playtest corpus:

1. **Claude Sonnet 5** â€” short execution / abort.
2. **Grok 4.5** â€” independent full execution to PC incapacitation.
3. **GPT-5.6 Luna** â€” continuation of the Claude execution through PC incapacitation.

The purpose is to determine:

- which Tiwas systems have demonstrated functional operation;
- which systems remain incomplete;
- which systems require scaffolding;
- which systems produced contradictory or non-comparable evidence;
- which systems require further development before a full Tiwas playtest;
- whether the present Tiwas combat architecture is sufficiently mature for broader full-system playtesting.

### 1.2 Principal Finding

The three records produce a consistent high-level result:

> **Tiwas's Core resolution engine is demonstrably operational in live combat, but the combat consequence layer is not yet fully deterministic without non-canonical scaffolding.**

The following are supported by repeated empirical execution:

- d100 roll-under resolution;
- natural-roll resource expenditure;
- Overflow â†’ HP;
- Recovery;
- Failure XP;
- Skill Roll Pool advancement;
- S-1 opposed contests;
- failed-Double processing when actually triggered;
- HP depletion;
- HP = 0 incapacitation;
- the general Track A / Track B combat architecture.

However, the executions also demonstrate unresolved dependencies around:

- combat sequencing;
- Effect magnitude;
- Active Defense magnitude;
- gated Effect thresholds;
- defender-winning opposed contests;
- creature defensive-skill assignment;
- location-zone ranges;
- passive Frightened triggering;
- complete integration of S-3/S-4/S-5/S-6 combat consequences.

Accordingly:

> **Tiwas is ready for continued controlled subsystem/integration playtesting, but the evidence does not yet support declaring the complete combat system full-playtest-ready without scaffolding.**

---

# 2. Source Records and Evidence Classification

## 2.1 Three Combat Records

| Record | LLM | Execution Type | Terminal State | Evidence Role |
|---|---|---|---|---|
| A | Claude Sonnet 5 | Independent execution | Explicit abort after 2 rounds / 4 exchanges | Initial integration evidence |
| B | Grok 4.5 | Independent execution | PC HP 0; Troll HP 412 | Independent full-combat evidence |
| C | GPT-5.6 Luna | Continuation of A | PC HP 0; Troll HP 569 | Continuation/integration evidence |

The Claude and Luna records are **one execution lineage**:

`Claude â†’ Luna`

Grok is a **separate execution lineage**.

The merged corpus explicitly warns that these records must be compared by lineage rather than treating all three terminal states as one experiment.

## 2.2 Evidence Classes

This report uses the following classifications:

| Classification | Meaning |
|---|---|
| **Confirmed Working** | Mechanism was exercised successfully and no execution failure was recorded |
| **Working but Scaffold-Dependent** | The architecture executed, but a non-canonical value or interpretation was required |
| **Partially Tested** | Some aspect was exercised but the full subsystem was not |
| **Untested / Idle** | Relevant mechanism existed but the combat did not exercise it |
| **Confirmed Gap** | Execution exposed a missing or insufficiently specified mechanism |
| **Interpretive Gap** | Existing rules do not uniquely determine the required outcome |
| **GM-Required** | Execution encountered a situation for which no authorised mechanical resolution existed |
| **Content Dependency** | Framework exists but required creature/content authoring is incomplete |

These classifications are evidence classifications only. They do not alter Tiwas authority status.

---

# 3. Execution-Lineage Analysis

## 3.1 Claude Sonnet 5

Claude's execution covered two rounds and four exchanges.

| Measure | Result |
|---|---:|
| Rounds | 2 |
| Exchanges | 4 |
| Starting PC HP | 600 |
| Ending PC HP | 585 |
| Starting Troll HP | 705 |
| Ending Troll HP | 698 |
| Termination | Explicit abort |

Claude exercised both attack/defence contest pathways, Overflow, a 100-Fumble, Wound creation, Frightened, Active Defense, Zero-Step location processing, and Advanced Skill creation.

However, Claude also identified a genuine GM-required stop concerning the passive Frightened trigger and an unresolved defender-wins interpretation.

### Assessment

Claude provides strong evidence that the combat architecture can be traversed, but also strong evidence that it cannot yet be considered completely deterministic.

---

## 3.2 Grok 4.5

Grok conducted an independent 22-round execution.

| Measure | Result |
|---|---:|
| Rounds | 22 |
| Exchanges | Full combat |
| PC terminal HP | 0 |
| Troll terminal HP | 412 |
| Duration estimate | 45â€“60 minutes |
| Result | Troll victory |

Grok reported successful operation of the Core Test, S-1, Failure XP, resource expenditure, Overflow, Recovery, Track A/B processing, Effect application, Active Defense, and HP=0 incapacitation.

Grok reported **no GM-required stops**, because the numeric gaps were handled under the prompt's explicit scaffold authorisation and the passive Frightened trigger was not invoked.

### Assessment

Grok provides the strongest evidence that the **scaffolded combat pipeline can sustain a complete combat to termination**.

It does **not**, however, establish that the scaffold values themselves are valid Tiwas mechanics.

---

## 3.3 GPT-5.6 Luna

Luna continued directly from Claude's state:

| Measure | Claude End | Luna Start |
|---|---:|---:|
| PC HP | 585 | 585 |
| Troll HP | 698 | 698 |
| PC Physical Energy | 50 | 50 |
| Attack1 | 27 | 27 |
| Defence1 | 29 | 29 |

Luna continued for 11 additional rounds and reached:

| Statistic | Final |
|---|---:|
| PC HP | 0 |
| Troll HP | 569 |
| Result | Troll victory |

The merged corpus explicitly verifies this continuation relationship.

### Assessment

Luna provides important evidence that the Claude execution could be resumed from its exact recorded state and driven to a terminal condition.

The combined Claude â†’ Luna lineage therefore demonstrates:

> **2-round initial execution + 11-round continuation = 13-round combat lineage**

but this must **not** be conflated with Grok's independent 22-round combat.

---

# 4. Cross-Report System Comparison

## 4.1 Core Resolution Layer

| System | Claude | Grok | Luna | Cross-Report Assessment |
|---|---|---|---|---|
| d100 roll-under | Exercised | Exercised | Exercised | **Confirmed Working** |
| 100-Fumble | Exercised | Exercised | Exercised | **Confirmed Working** |
| Floor rounding | Exercised | Exercised | Exercised | **Confirmed Working** |
| Skill Cap / Starting Value | Exercised | Exercised | Exercised | **Confirmed Working** |
| 9-step Core Test | Exercised | Exercised | Exercised | **Confirmed Working** |
| Natural-roll Cost | Exercised | Exercised | Exercised | **Confirmed Working** |
| Overflow â†’ HP | Exercised | Exercised | Exercised | **Confirmed Working** |
| Overflow immutability | Exercised | Exercised | Exercised | **Confirmed Working** |
| Recovery | Exercised | Exercised | Exercised | **Confirmed Working** |
| Failure XP | Exercised | Exercised | Exercised | **Confirmed Working** |
| Skill Roll Pool | Exercised | Exercised | Exercised | **Confirmed Working** |
| Failed-Double Advanced Skill | Exercised | Not triggered | Exercised | **Confirmed Working** |

### Finding

This is the strongest area of cross-report convergence.

The merged evidence explicitly records the Core Test, Failure XP, resource consequences, and progression as successfully exercised.

**Assessment:**

> **The Tiwas Core Engine has passed its first meaningful multi-exchange combat integration test.**

No evidence from these three executions indicates that the Core Test itself is the principal blocker to broader playtesting.

---

# 5. Opposed Resolution

## 5.1 S-1 Universal Opposed Contest

| Observation | Claude | Grok | Luna |
|---|---|---|---|
| S-1 used | Yes | Yes | Yes |
| Success/Failure matrix | Exercised | Exercised | Exercised |
| Quality comparison | Exercised | Exercised | Exercised |
| Defender success | Yes | Yes | Yes |
| Fail/Fail behaviour | Tested/available | Tested | Continued |
| Resource costs preserved | Yes | Yes | Yes |

### Assessment

**S-1 is strongly supported as an operational primitive.**

The unresolved issue is not whether S-1 works.

The unresolved issue is:

> **What additional rights or consequences arise from particular S-1 outcomes in combat?**

Most importantly:

### Defender-Wins Question

When an attacker loses an opposed attack contest because the defender succeeds, the corpus does not explicitly determine whether:

1. the attack simply fails; or
2. the defender receives an opportunity to declare a counter-Effect.

Claude identified this as an interpretive gap, and the conservative execution treated the attack as failing without generating a counter-Effect.

**Status: Confirmed Interpretive Gap.**

---

# 6. Combat Consequence Layer

This is where the greatest concentration of unresolved issues occurs.

## 6.1 S-3 Effects

The combat architecture successfully selected and applied Effects.

However, the **numeric magnitude of Effects was not fully specified**.

The principal scaffold was:

> **Inflict Injury magnitude = winner's Margin**

This was explicitly a session scaffold and not a canonical rule.

### Assessment

| Question | Status |
|---|---|
| Can an Effect be selected? | **Demonstrated** |
| Can an Effect be applied? | **Demonstrated** |
| Is the magnitude determined canonically? | **No** |
| Does the combat pipeline therefore remain scaffold-dependent? | **Yes** |

**Status: Working but Scaffold-Dependent.**

---

## 6.2 Active Defense

Active Defense was exercised successfully.

However, the magnitude of mitigation required a scaffold.

The execution used:

> Defender's Margin on successful Defense; 0 on failed Defense.

This was explicitly non-canonical.

### Assessment

| Question | Status |
|---|---|
| Does Active Defense execute? | Yes |
| Does it interact with the attack pipeline? | Yes |
| Is its mitigation magnitude canonically determined? | No |
| Is its governing defensive skill completely resolved for all creatures? | No |

**Status: Working but Scaffold-Dependent.**

---

# 7. Location and Wound Systems

## 7.1 Location

Claude's execution exercised Zero-Step Location processing.

However, the numerical Tier-1 coarse-zone ranges were scaffolded:

| Range | Session Scaffold |
|---|---|
| 1â€“25 | Legs |
| 26â€“50 | Torso |
| 51â€“75 | Arms |
| 76â€“100 | Head |

The merged corpus explicitly records that DEC-041 leaves the ranges directional rather than locked.

### Assessment

The **Location mechanism exists sufficiently to execute the pathway**, but the anatomical mapping is not yet fully specified.

**Status: Working but Incomplete.**

---

## 7.2 Wounds

Claude exercised Wound creation.

Grok's independent run did not select a Wound-producing Effect and therefore did not validate the complete Wound pipeline.

Luna inherited a state containing the Claude-created Wound but did not thereby independently validate the Wound-generation process.

### Assessment

| Component | Status |
|---|---|
| Wound creation pathway | **Exercised** |
| Location interaction | **Partially exercised** |
| Wound consequence magnitude | **Not fully established** |
| Complete Wound lifecycle | **Not demonstrated** |

**Status: Partially Tested / Requires Further Development.**

---

# 8. Armor

Neither side's combat state required actual Armor Tag interaction in the full Grok run.

The merged evidence identifies S-5 Armor as a continuing disagreement across the broader readiness corpus: some reports regard the Tags-based architecture as sufficient for alpha play, while others regard missing Tag content as a design-stage dependency.

For these **three combat executions specifically**:

> **Armor was not meaningfully validated.**

**Status: Untested.**

This is important because a system cannot be classified as "working" merely because its architecture exists.

---

# 9. Conditions

## 9.1 Frightened

Frightened produced two different kinds of evidence.

### Mechanical Effect pathway

Claude successfully applied Frightened as a won S-1 Effect.

Therefore:

> The **Condition application pathway** can execute when Frightened is explicitly selected as an Effect.

### Passive trigger pathway

The source scenario also contains a fear-inducing passive trigger.

Tiwas does not define a trigger mechanism for imposing Frightened merely because a character perceives a frightening creature.

Claude therefore reached a genuine GM-required stop when this pathway was considered.

Grok avoided this pathway entirely and consequently reported no GM stop.

### Assessment

| Frightened Component | Status |
|---|---|
| Condition exists | Working |
| Condition as won Effect | Demonstrated |
| Passive/aura trigger | **Missing** |
| Trigger resolution | **GM/Designer decision required** |

**Status: Partially Working; Trigger Subsystem Missing.**

This distinction is critical.

---

# 10. Combat Sequencing

## 10.1 Opening Sequence

The combat began under the explicit Designer Override:

> **"Round 1, Exchange 1 â€” PC attacks"**

This allowed the execution to begin.

However, the override was explicitly limited to the opening sequence and did not establish:

- initiative;
- actor ordering;
- exchange construction;
- round construction;
- simultaneous declarations;
- ties;
- action availability;
- number of actions;
- timing of Active Defense.

The merged corpus explicitly identifies this as an additional empirical gap surfaced by the combat test.

### Assessment

The combat simulations were able to proceed because the prompt supplied a sequencing instruction.

Therefore:

> **The simulations demonstrate combat resolution, but not a complete canonical combat sequencing procedure.**

**Status: Confirmed Gap.**

This is one of the most important findings for full playtest readiness.

---

# 11. Creature / NPC Integration

## 11.1 Ice Troll

The Ice Troll was successfully supplied as a table-ready converted block.

This represents progress compared with the earlier *Beyond the Vale of Madness* readiness audits, which had identified creature content as a major blocker.

However, the combat exposed another content-level issue:

> The Ice Troll block did not contain a dedicated defensive skill appropriate to the combat pipeline.

A Brawling skill was therefore used as the defensive substitute.

This became **CANDIDATE-06** in the subsequent documentation.

### Assessment

| Component | Status |
|---|---|
| Creature attribute block | Working |
| Derived statistics | Working |
| Offensive skills | Working |
| Creature content format | Working |
| Dedicated defensive skill | **Unresolved** |
| Special Traits | Partially unresolved |
| Regeneration | Not exercised |
| Regrowth | Not exercised |
| Cold-dependent DR | Not exercised |

**Status: Content Framework Working; Creature Template Requires Further Development.**

---

# 12. Regeneration / Regrowth

The Ice Troll's freezing-dependent regeneration and regrowth were deliberately inactive.

Consequently:

> None of the three combat executions validates the actual regeneration/regrowth mechanics.

The merged records explicitly state that these abilities remained inactive because their environmental condition was not established.

**Status: Untested.**

This should not be counted as a passed subsystem.

---

# 13. Quality and Gated Effects

A further gap was exposed by the combat execution.

DEC-031 establishes Quality-based Effect gating, but the exact numeric threshold for unlocking gated Effects was not established.

The session therefore used:

| Quality | Session Interpretation |
|---|---|
| â‰¥1 | Base-tier Effect |
| â‰¥10 | Gated-tier Effect |

These values were explicitly scaffolds.

This became **CANDIDATE-07**.

**Status: Confirmed Numeric Specification Gap.**

---

# 14. Cross-Report Agreement Matrix

| System | Evidence Strength | Agreement | Final Assessment |
|---|---|---|---|
| Core d100 | Very High | Strong | **Working** |
| 100-Fumble | High | Strong | **Working** |
| Resource Cost | Very High | Strong | **Working** |
| Overflow | Very High | Strong | **Working** |
| Recovery | Very High | Strong | **Working** |
| Failure XP | Very High | Strong | **Working** |
| Skill progression | High | Strong | **Working** |
| Advanced Skills | Mediumâ€“High | Claude/Luna exercised | **Working** |
| S-1 Opposed Contest | Very High | Strong | **Working** |
| Track A/B | High | Strong | **Working** |
| Basic Effect application | High | Strong | **Working with scaffolding** |
| Active Defense | High | Strong | **Working with scaffolding** |
| HP damage | High | Strong | **Working with scaffolding** |
| HP=0 incapacitation | High | Strong | **Working** |
| Location | Medium | Partially divergent | **Incomplete** |
| Wounds | Medium | Partial | **Further testing required** |
| Armor | Low | Not exercised | **Untested** |
| Frightened Condition | Medium | Partial | **Incomplete** |
| Passive fear trigger | High | Gap confirmed | **Missing** |
| Combat sequencing | High | Gap confirmed | **Missing** |
| Creature defence skill | Medium | Gap surfaced | **Incomplete** |
| Quality gated threshold | High | Gap confirmed | **Missing numeric specification** |
| Regeneration | Low | Not exercised | **Untested** |
| Regrowth | Low | Not exercised | **Untested** |
| Cold-dependent traits | Low | Not exercised | **Untested** |

---

# 15. What the Three Reports Actually Prove

## 15.1 Strongly Demonstrated

The following conclusion is justified by the evidence:

> **Tiwas's Core Test and underlying resource/progression architecture can operate repeatedly inside combat without the Core engine itself breaking down.**

The Grok execution alone ran for 22 rounds, while the Claude â†’ Luna lineage successfully continued from an interrupted state to terminal incapacitation.

This is meaningful integration evidence.

---

## 15.2 Demonstrated but Not Yet Canonically Deterministic

These systems can execute, but execution currently depends on scaffolding:

1. Inflict Injury magnitude.
2. Active Defense mitigation magnitude.
3. Gated Effect threshold.
4. Location-zone numerical ranges.
5. Creature defensive-skill substitution.
6. Certain S-3 Effect magnitudes.

The merged candidate register explicitly identifies these unresolved items.

---

## 15.3 Not Yet Demonstrated

The following have insufficient evidence from these three executions:

- Armor interaction;
- regeneration;
- regrowth;
- freezing-dependent Traits;
- complete Wound lifecycle;
- complete location/anatomical mapping;
- complete equipment interaction;
- complete environmental interaction;
- full combat sequencing.

These should remain **untested**, not incorrectly classified as failures.

---

# 16. Contradictions Between the Reports

## 16.1 "Combat Works" vs "Combat Is Incomplete"

There is no actual contradiction.

Grok demonstrates:

> **The combat pipeline can execute to completion when scaffolds are authorised.**

Claude demonstrates:

> **The combat pipeline encounters genuine unresolved rules when scaffolding cannot legitimately answer the question.**

Luna demonstrates:

> **A previously interrupted combat state can be resumed and driven to terminal resolution under the same scaffolded execution regime.**

Therefore the correct synthesis is:

> **Combat execution works; complete combat specification does not yet.**

This distinction should be preserved in future project documentation.

---

## 16.2 Different Terminal Troll HP Values

| Execution | Troll HP at Termination |
|---|---:|
| Claude | 698 |
| Luna continuation | 569 |
| Grok | 412 |

These values are **not contradictory results from one combat**.

Claude â†’ Luna is one lineage.

Grok is independent.

Different d100 sequences and execution histories therefore produce different outcomes.

The values should not be averaged or combined into a statistical combat-balance conclusion.

---

# 17. Systems Requiring Further Development

## Priority P0 â€” Required for Deterministic Full Combat

| Priority | System | Reason |
|---|---|---|
| P0 | Combat sequencing | No general initiative/order procedure |
| P0 | Inflict Injury magnitude | Damage currently requires scaffold |
| P0 | Active Defense magnitude | Mitigation currently requires scaffold |
| P0 | Defender-wins consequence | S-1 attack outcome is interpretively incomplete |
| P0 | Gated Effect threshold | Numeric Quality threshold unresolved |
| P0 | Creature defensive skill | Ice Troll required Brawling substitution |

These are directly demonstrated combat-layer deficiencies.

---

## Priority P1 â€” Required for Broad Combat Fidelity

| Priority | System | Reason |
|---|---|---|
| P1 | Location zone ranges | Current numerical ranges are not locked |
| P1 | Wound consequences | Complete Wound behaviour remains insufficiently tested |
| P1 | S-3 Effect catalogue | More Effects require defined magnitudes |
| P1 | Armor | No meaningful end-to-end test yet |
| P1 | Condition triggers | Frightened demonstrates trigger-layer absence |
| P1 | Equipment | Combat benchmark has not yet tested equipment interaction |

---

## Priority P2 â€” Required for Full Adventure Playtesting

| Priority | System | Reason |
|---|---|---|
| P2 | Regeneration/Regrowth | Ice Troll special abilities remain untested |
| P2 | Environmental hazard cadence | Required by the original adventure |
| P2 | Darkness/light | Required by Blood Man route |
| P2 | Encumbrance | Required by climbing/equipment branches |
| P2 | Magic | Required if magical pre-generated character is used |
| P2 | Economy/loot | Required for complete adventure completion |

The broader adventure analysis independently identified environmental hazards, equipment, darkness, creature content, magic, and economy as major readiness dependencies.

---

# 18. Full-Playtest Readiness Assessment

## 18.1 Combat-Only Readiness

### Current State

**Controlled alpha combat testing: YES**

**Deterministic full combat without scaffolds: NO**

The evidence supports continued combat testing specifically to gather empirical evidence about unresolved systems.

---

## 18.2 Full Tiwas Adventure Readiness

### Current State

**NO â€” not yet ready for a full-fidelity adventure playtest.**

This conclusion is not because the Core Test failed.

It is because the external benchmark exposes missing or incomplete systems surrounding the Core.

The broader readiness evidence consistently identifies:

- environmental hazards;
- equipment;
- creature content;
- darkness/sensory conditions;
- magic;
- damage/consequence specification;
- Wounds;
- combat integration

as remaining development areas.

---

# 19. Recommended Development Sequence

The three combat reports suggest a more precise sequence than simply "finish everything."

## Phase 1 â€” Close the Combat Execution Interface

Resolve, through the project's normal investigation/ruling process:

1. General combat sequencing.
2. Inflict Injury magnitude.
3. Active Defense mitigation.
4. Defender-wins consequence.
5. Quality â†’ gated Effect threshold.
6. Creature defensive-skill assignment.
7. Location Tier-1 ranges.

These are the issues that directly prevented the combat test from being fully deterministic.

---

## Phase 2 â€” Complete the Combat Consequence Layer

Then complete:

1. S-3 Effect magnitude vocabulary.
2. S-4 Wound consequences.
3. S-5 Armor interaction.
4. S-6 complete defence integration.
5. Condition triggers.
6. Creature special-ability execution.

The objective should be:

> **One complete combat in which no numeric scaffold is required.**

---

## Phase 3 â€” Expand Beyond Combat

After the combat pipeline is deterministic:

1. Equipment.
2. Encumbrance.
3. Environmental hazards.
4. Darkness/light.
5. Regeneration/environmental Traits.
6. Healing/Wound interaction.
7. Magic, if in benchmark scope.
8. Economy/loot.

---

## Phase 4 â€” Full Benchmark Playtest

Only after Phases 1â€“3 should *Beyond the Vale of Madness* be treated as a **full-fidelity Tiwas playtest**, rather than an integration diagnostic.

---

# 20. Final Findings

## F-01 â€” Core Resolution

**Finding:** The Core Test is operational under repeated combat use.

**Evidence:** Claude, Grok, and Luna executions.

**Classification:** Empirical finding.

---

## F-02 â€” Resource/Progression Integration

**Finding:** Natural-roll resource expenditure, Overflow, Recovery, Failure XP, and skill progression can operate within repeated combat exchanges.

**Classification:** Empirical finding.

---

## F-03 â€” S-1 Integration

**Finding:** S-1 is capable of supporting repeated attack/defence contests.

**Classification:** Empirical finding.

---

## F-04 â€” Combat Consequence Specification

**Finding:** The combat architecture requires non-canonical scaffolds for several consequence magnitudes.

**Classification:** Confirmed design gap.

---

## F-05 â€” Combat Sequencing

**Finding:** The combat prompt required a Designer Override to establish the initial actor order. This demonstrates that the existing Time/Action expression does not itself constitute a complete combat sequencing procedure.

**Classification:** Confirmed design gap.

---

## F-06 â€” Condition Trigger Layer

**Finding:** The Frightened Condition can operate as an Effect, but the passive trigger pathway is not specified.

**Classification:** Confirmed subsystem gap.

---

## F-07 â€” Creature Content

**Finding:** The Ice Troll can now be represented sufficiently to conduct combat testing, but the absence of a dedicated defensive skill exposed a content/template dependency.

**Classification:** Content/integration gap.

---

## F-08 â€” Full Combat Readiness

**Finding:** The combat engine is **integration-testable but not yet scaffold-free deterministic**.

**Classification:** Empirical project-readiness finding.

---

# 21. Overall Project Verdict

## Current Tiwas State

| Layer | Assessment |
|---|---|
| Core resolution engine | **READY FOR EXTENDED PLAYTESTING** |
| Resource/progression engine | **READY FOR EXTENDED PLAYTESTING** |
| S-1 opposed contests | **READY FOR EXTENDED PLAYTESTING** |
| Basic combat pipeline | **FUNCTIONAL** |
| Combat consequence layer | **INCOMPLETE** |
| Combat sequencing | **MISSING / UNRESOLVED** |
| Creature integration | **FUNCTIONAL BUT INCOMPLETE** |
| Conditions | **PARTIALLY FUNCTIONAL** |
| Location/Wounds | **PARTIALLY TESTED** |
| Armor | **UNTESTED** |
| Environmental systems | **INCOMPLETE** |
| Equipment | **INCOMPLETE** |
| Full adventure readiness | **NOT READY** |

### Final Assessment

The three combat reports provide a substantially stronger result than the earlier readiness audits alone:

> **Tiwas does not need a replacement Core resolution engine.**

The live combat evidence instead indicates that development effort should now concentrate on the **interfaces between resolution and consequence**:

`Core Test â†’ S-1 â†’ Effect â†’ Defense â†’ Location â†’ Wound/Condition â†’ Incapacitation`

The Core portion of this chain has now received meaningful empirical support.

The consequence portion has not yet reached the same level of determinism.

Therefore the appropriate next project state is:

> **Continue targeted combat-system development and repeat combat integration tests until the combat pipeline can execute from opening sequence to terminal condition without non-canonical scaffolds or interpretive gaps.**

This report makes **no new mechanics canonical**, does not assign DEC numbers, and does not supersede any existing ruling.

---

# 22. Governance and Provenance Restrictions

The following restrictions apply to this report:

1. No scaffold in any of the three playtests is a Tiwas rule.
2. No terminal combat result establishes balance.
3. Claude and Luna must be treated as one execution lineage.
4. Grok must be treated as an independent execution.
5. No numerical scaffold may be promoted automatically.
6. The Designer Override must not be interpreted as a general initiative rule.
7. Brawling must not automatically become the universal creature defensive skill.
8. Session location ranges must not be treated as canonical.
9. Session Quality thresholds must not be treated as canonical.
10. Margin-based damage must not be treated as the final damage formula.
11. Margin-based Active Defense mitigation must not be treated as the final mitigation formula.
12. Passive Frightened triggering remains unresolved.
13. Defender counter-Effect rights remain unresolved.
14. The three combat results must not be statistically combined as though they were repeated rounds of the same combat.
15. Any future canonical change must proceed through the project's established Promotion Rule.

---

# 23. Source Register

| Source | Role |
|---|---|
| `merged-combat-reports-playtest1.md` | Primary merged evidence corpus |
| Claude Sonnet 5 Ice Troll execution | Independent short execution / initial lineage |
| Grok 4.5 Ice Troll execution | Independent 22-round full execution |
| GPT-5.6 Luna Ice Troll continuation | Claude-lineage continuation to terminal state |
| `claude-playtest-prompt-version2.md` v2.1 | Common execution specification |
| `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` | Baseline Tiwas mechanics and authority boundaries |
| *Beyond the Vale of Madness* | External mechanical benchmark underlying the broader readiness work |

The merged corpus confirms the three execution records and their lineage relationships.

---

# 24. Final Readiness Statement

> **Tiwas has passed the Core combat integration threshold but has not yet passed the full deterministic combat-system threshold.**

The next meaningful milestone is therefore **not another generic full adventure playtest**.

It is:

> **A scaffold-free combat regression playtest in which the complete combat sequence, Effect magnitudes, Defense magnitudes, sequencing, location mapping, creature defence, and contested-outcome consequences are all resolved by established Tiwas rules.**

Until that milestone is achieved, a full-fidelity *Beyond the Vale of Madness* playtest should remain classified as **not ready**, while targeted combat integration testing should continue as valid and high-value empirical work.

**No canonical Tiwas mechanics were created, promoted, or modified by this report.**

---

**Documentarian Verification (2026-09-04, opencode/big-pickle):**
- Factual claims verified against the three source execution reports and the decision register.
- Lineage structure, comprehensive 24-section structure, evidence-class system, and all 8 final findings accurately reported.
- No DEC numbers assigned. No rulings made. Classification preserved: advisory.
- **Assessor_llm updated** from empty to opencode/big-pickle; **last_modified_by_llm** updated to opencode/big-pickle.
- NOTE: Source filename on disk uses en-dash (–); provenance in header uses em-dash (—); this is a harmless encoding artifact of the source authoring tool.
