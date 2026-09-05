# Tiwas TTRPG — Ice Troll Combat Playtest v3
## Action-Selection Decision and Execution Record

**Document Type:** Formal Project Documentation / Playtest Finding  
**Project:** Tiwas TTRPG  
**Test:** Ice Troll Combat Playtest Prompt v3  
**Date:** 2026-09-04  
**Author:** GPT-5.6 Luna  
**Author Version:** GPT-5.6 Luna  
**Target Consumer:** OpenCode  
**Status:** Pending Human Confirmation  
**Authority:** Playtest finding; no new canonical rule created by this document

---

# 1. Purpose

This document records the results of the Ice Troll combat playtest execution performed during the current Tiwas TTRPG project session.

The specific issue examined is **creature combat action selection**: the Ice Troll possesses multiple authored attack skills, but the playtest execution required the human participant to select which attack the Troll would use.

The purpose of this document is to:

1. Record what occurred during the playtest.
2. Distinguish existing Tiwas rules from execution decisions.
3. Identify the resulting system-level gap.
4. Prevent OpenCode from silently converting an execution choice into a new rule.
5. Require OpenCode to obtain explicit human confirmation before recording any resulting decision as authoritative.

---

# 2. Source Basis

The primary source is:

`tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md`

The prompt explicitly supplies the Ice Troll's combat statistics and two signature attacks:

| Attack | Tier | Current Skill |
|---|---:|---:|
| Icy Claws | 2 | 67 |
| Sharktoothed Maw | 2 | 75 |

The prompt also states that both attacks are Tier-2 and therefore Wound-capable under the applicable Tier gate.

The v3 prompt explicitly defines combat sequencing as highest-Speed-first, with one substantive combat action/test per combatant per round.

The project decision register also confirms that pre-authored Tier-2 creature skills are permitted as a creature/NPC authoring convention.

---

# 3. Relevant Existing Rules

## 3.1 Combat Sequencing

DEC-095 establishes:

1. Determine current Speed.
2. Highest Speed acts first.
3. Each combatant receives one combat turn per round.
4. A combat turn permits one substantive combat action/test.
5. After all combatants act, the round ends.
6. Speed is recalculated if its underlying Attributes change.
7. Speed ties are resolved by natural d100 comparison.
8. Initiative itself is not a Core Test and has no resource cost.

For this test:

| Combatant | Speed |
|---|---:|
| Ice Troll | 175 |
| Adventurer-1 | 150 |

Therefore, the Ice Troll acts first.

The v3 prompt explicitly states this result for the test.

---

## 3.2 Ice Troll Attack Availability

The Ice Troll has two authored Tier-2 attacks:

| Attack | Skill | Domain |
|---|---:|---|
| Icy Claws | 67 | Physical Energy |
| Sharktoothed Maw | 75 | Physical Energy |

Both are valid combat actions.

The v3 prompt does **not**, in the supplied material, state an attack-selection priority between these two attacks.

---

# 4. Playtest Execution Event

At the beginning of Round 1, the Ice Troll had the first combat turn because its Speed was 175 versus the Adventurer's Speed of 150.

The execution therefore reached the following decision point:

> **Ice Troll must select a substantive combat action.**

Two authored legal attacks were available:

- Icy Claws — 67
- Sharktoothed Maw — 75

The human participant explicitly selected:

> **Sharktoothed Maw**

This supplied the action-selection input required to continue the combat.

---

# 5. Important Interpretation

The selection of **Sharktoothed Maw was an execution instruction**, not evidence that Tiwas currently contains a rule stating that the Ice Troll must use Sharktoothed Maw.

This distinction is critical.

| Statement | Status |
|---|---|
| Ice Troll has Icy Claws | Ruled/test stat block |
| Icy Claws has Skill 67 | Supplied playtest value |
| Ice Troll has Sharktoothed Maw | Ruled/test stat block |
| Sharktoothed Maw has Skill 75 | Supplied playtest value |
| Troll acts before Adventurer-1 | Ruled by DEC-095 |
| Troll must use Sharktoothed Maw | **Not established** |
| Troll should automatically select its highest Skill | **Not established** |
| Troll should randomly select an attack | **Not established** |
| GM/LLM should invent tactical behaviour | **Not established** |
| Human may explicitly select the Troll's action for the test | **Demonstrated in this execution** |

The v3 prompt also imposes derivation discipline and prohibits inventing new mechanics or content beyond what is ruled or explicitly scaffolded.

---

# 6. Counterfactual: If No Attack Had Been Selected

If the participant had **not** selected Sharktoothed Maw, the Combat Referee should not silently select an attack.

For example, the following would be unauthorised:

```text
Troll chooses Sharktoothed Maw because it has the higher Skill.
```

There is no supplied rule establishing that priority.

Likewise, the following would be unauthorised:

```text
Troll randomly chooses between Icy Claws and Sharktoothed Maw.
```

No random attack-selection rule has been supplied.

Likewise:

```text
Troll chooses the attack that is tactically optimal.
```

No tactical optimisation procedure has been established.

Therefore, absent an explicit action-selection instruction or an existing authored creature behaviour rule, execution should stop at the action-selection boundary and escalate to the human monitor.

---

# 7. Identified System Gap

## SC-XX — Creature/NPC Action Selection

The playtest exposed a distinct subsystem requirement:

> **Given a creature/NPC with multiple legal combat actions, what determines which substantive action it selects on its combat turn?**

The current combat sequencing rule determines **when** the creature acts.

It does not, by itself, determine **which legal action** the creature chooses.

This is a different problem.

| Question | Current Coverage |
|---|---|
| Who acts first? | **Covered — DEC-095** |
| How many substantive actions? | **Covered — DEC-095** |
| What constitutes the substantive action? | **Covered — S-1 exchange** |
| What attacks does the creature possess? | **Covered for this test creature** |
| Which attack does the creature choose? | **Not established by the evidence reviewed** |
| What happens if no choice is supplied? | **Requires explicit project decision** |

This should therefore be treated as a **candidate system gap**, not silently filled by OpenCode.

---

# 8. Result of the Actual Combat Execution

The human explicitly selected **Sharktoothed Maw**.

The combat was consequently allowed to proceed using:

```text
Ice Troll attack:
Sharktoothed Maw
Skill = 75
```

The subsequent combat execution was therefore conditional upon that explicit human action-selection instruction.

The combat result recorded in the session was:

| Combatant | Starting HP | Final HP | Result |
|---|---:|---:|---|
| Adventurer-1 | 600 | −29 | Incapacitated |
| Ice Troll | 705 | 583 | Active |

The v3 prompt defines Inflict Injury magnitude as the winner's Margin and Active Defense mitigation as the defender's Margin.

**Important:** The numerical combat outcome must not be interpreted as evidence that Sharktoothed Maw is the Troll's canonical/default attack. The outcome is the result of the explicitly selected attack path.

---

# 9. Design Significance

This finding is important because the distinction between **combat sequencing** and **creature decision-making** is now demonstrable in execution.

The existing sequencing rule answers:

> "When does the Troll act?"

It does not necessarily answer:

> "What does the Troll do?"

A simulation-grade combat engine cannot safely infer the second question from the first.

The playtest therefore identifies a potential missing interface between:

```text
Creature/NPC Stat Block
        ↓
Available Actions
        ↓
[ ACTION-SELECTION PROCEDURE ]
        ↓
S-1 Combat Exchange
        ↓
S-3 Effect
        ↓
S-5 Armour
        ↓
S-6 Active Defence
        ↓
S-4 Wound
        ↓
S-7 Incapacitation/Death
```

The missing element is specifically the **action-selection procedure**.

---

# 10. OpenCode Handling Requirements

OpenCode must **not** automatically create a DEC from this report.

This document records an observed execution issue and a proposed interpretation.

OpenCode must:

1. Present the finding to the human decision-maker.
2. Ask the confirmation questions in §11.
3. Record the answers exactly.
4. Only create or modify a decision record after explicit confirmation.
5. Avoid treating the previous selection of Sharktoothed Maw as a permanent creature AI rule.
6. Avoid modifying canonical rules merely because the playtest required an execution choice.
7. Preserve the distinction between:
   - playtest execution input;
   - observed system gap;
   - proposed design solution;
   - confirmed designer ruling.

---

# 11. Mandatory Human Confirmation Questions

**OpenCode MUST ask the following questions before promoting this finding into a project decision.**

## Q1 — Round 1 Action

> **For this completed Ice Troll playtest, do you confirm that the Round 1 Troll action was intentionally set to _Sharktoothed Maw (Skill 75)_?**

Expected confirmation:

- **YES** — retain the recorded combat execution.
- **NO** — do not treat the recorded execution as valid for the intended test.

---

## Q2 — No-Selection Behaviour

> **When a creature/NPC has multiple legal combat actions and no authored action-selection rule or explicit action instruction determines which one it uses, do you confirm that the Combat Referee/LLM must STOP and request human input rather than selecting an action itself?**

Expected confirmation:

- **YES** — establish this as the execution/governance behaviour.
- **NO** — do not assume an alternative action-selection mechanism; escalate the unresolved design question for a separate ruling.

---

## Q3 — New System Decision

> **Do you want the absence of a creature/NPC action-selection procedure to be recorded as a formal Tiwas system gap requiring a future decision, rather than being solved implicitly during playtests?**

Expected confirmation:

- **YES** — register as an open system decision/gap.
- **NO** — provide the authorised existing rule or decision that already resolves creature action selection.

---

# 12. Recommended Decision Boundary

No new mechanical action-selection algorithm should be invented by OpenCode as part of processing this report.

If Q3 is confirmed **YES**, the appropriate project state is:

```text
Creature Action Selection
        ↓
OPEN SYSTEM QUESTION
        ↓
Future investigation / designer ruling
```

It should **not** become:

```text
Creature Action Selection
        ↓
Highest Skill automatically selected
```

unless the designer explicitly rules that behaviour.

---

# 13. Formal Findings

| ID | Finding | Classification |
|---|---|---|
| ITC-F-001 | Ice Troll possesses two legal authored attacks | Confirmed test data |
| ITC-F-002 | Sharktoothed Maw was explicitly selected by the human for Round 1 | Confirmed execution event |
| ITC-F-003 | Sharktoothed Maw is not established as the mandatory/default Troll attack by this evidence | Confirmed interpretation |
| ITC-F-004 | Combat sequencing establishes turn order but does not establish attack-selection priority in the reviewed v3 material | System gap candidate |
| ITC-F-005 | Automatically selecting an attack without an authorised rule would constitute an unauthorised design assumption | Governance finding |
| ITC-F-006 | Human escalation is required if no authorised action-selection mechanism exists | Pending Q2 confirmation |
| ITC-F-007 | Creature/NPC action selection may require a dedicated future ruling | Pending Q3 confirmation |

---

# 14. Status

**Current Status: PENDING HUMAN CONFIRMATION**

No new canonical Tiwas rule is created by this document.

The completed combat remains an execution branch based on the explicit human selection:

> **Sharktoothed Maw**

The broader question of how a creature selects among multiple legal actions remains unresolved unless and until the human decision-maker explicitly confirms a ruling.

---

# 15. OpenCode Instruction

**Do not close this issue autonomously.**

Before modifying the decision register, canonical rules, roadmap, or other authoritative project documentation, OpenCode must present **Q1, Q2, and Q3 from §11** to the human decision-maker and obtain explicit answers.

OpenCode must then record the answers and proceed only within the scope explicitly authorised by those answers.

---

# 16. Author

**Author:** GPT-5.6 Luna  
**Version:** GPT-5.6 Luna  
**Role:** Lead Systems Architect and Design Assistant — Tiwas TTRPG  
**Document Date:** 2026-09-04