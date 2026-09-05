# Tiwas TTRPG — Ice Troll Combat Playtest v3
## Unedited Playtest Execution Results

**Document Type:** Formal Project Documentation / Playtest Execution Record  
**Project:** Tiwas TTRPG  
**Playtest:** Ice Troll Combat Playtest Prompt v3  
**Prompt:** `tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md`  
**Execution Date:** 2026-09-04  
**Author:** GPT-5.6 Luna  
**Author Version:** GPT-5.6 Luna  
**Execution Status:** Completed  
**Record Status:** Unedited Execution Record  
**Purpose:** OpenCode ingestion / project documentation

---

# 1. Record Scope

This document records the playtest results generated during the current ChatGPT session.

The results are reproduced as an **execution record**.

This document does not:

- retrospectively correct numerical results;
- reinterpret individual rolls;
- replace execution decisions;
- reconcile possible inconsistencies;
- promote execution behaviour into canonical rules;
- create a new DEC;
- alter the source playtest prompt.

The purpose is to provide OpenCode with the results exactly as they were produced during this playtest session.

---

# 2. Playtest Participants

## 2.1 Adventurer-1

The executed baseline used:

| Statistic | Value |
|---|---:|
| All 24 Attributes | 50 |
| HP | 600 |
| MP | 600 |
| Physical Energy | 150 |
| Speed | 150 |
| Energy Regen | 100 |
| MP Regen | 100 |
| Movement Speed | 6 |
| Attack2 | 25 |
| Attack2 Cap | 50 |
| Defence2 | 25 |
| Defence2 Cap | 50 |

---

## 2.2 Ice Troll

The executed Ice Troll values were:

| Statistic | Value |
|---|---:|
| HP | 705 |
| MP | 420 |
| Physical Energy | 220 |
| Speed | 175 |
| Energy Regen | 140 |
| MP Regen | 75 |
| Movement Speed | 7 |
| Icy Claws | 67 |
| Sharktoothed Maw | 75 |
| Brawling | 37 |
| Camouflage | 30 |
| Stealth | 30 |
| Tracking | 30 |

The source playtest prompt provides the Ice Troll's 24 attributes, derived statistics, and skill values, including Icy Claws 67 and Sharktoothed Maw 75.

---

# 3. Initial Combat State

## 3.1 Initiative

The executed initiative comparison was:

| Combatant | Speed | Order |
|---|---:|---:|
| Ice Troll | 175 | 1 |
| Adventurer-1 | 150 | 2 |

Therefore:

> **Ice Troll acts first.**

The v3 prompt explicitly specifies highest-Speed-first sequencing and gives the same Speed values for this test.

---

# 4. Frightened State

The execution applied the passive **Frightened** scene-state modifier to Adventurer-1.

The applied effect was:

> **−1 to all Skills**

The state was treated as Tier-1.

---

# 5. Human Action-Selection Input

At the Ice Troll's first combat turn, two authored attack actions were available:

| Attack | Skill |
|---|---:|
| Icy Claws | 67 |
| Sharktoothed Maw | 75 |

The human participant explicitly selected:

> **Sharktoothed Maw**

This selection was used for the subsequent combat execution.

The source prompt identifies both attacks as the Troll's Tier-2 signature attacks.

---

# 6. Combat Execution Log

The following table reproduces the combat results generated during the session.

| Round | Turn | S-1 rolls | Result | Active Defense | HP damage |
|---:|---|---|---|---|---:|
| 1 | Troll | Shark 16 S / Defence 26 F | Troll wins | PC 51 F | **59** |
| 1 | PC | Attack 36 F / Brawl 65 F → repeat: Attack 32 F / Brawl 32 S | Troll wins | — | 0 |
| 2 | Troll | Shark 100 F / Defence 63 F → repeat: Shark 17 S / Defence 2 S | Troll wins | PC 99 F | **58** |
| 2 | PC | Attack 35 F / Brawl 87 F → repeat: 47 F / 96 F → repeat: 61 F / 67 F → repeat: 35 F / 29 S | Troll wins | — | 0 |
| 3 | Troll | Shark 69 S / Defence 36 F | Troll wins | PC 8 S | **0** |
| 3 | PC | Attack 88 F / Brawl 18 S | Troll wins | — | 0 |
| 4 | Troll | Shark 12 S / Defence 47 F | Troll wins | PC 40 F | **63** |
| 4 | PC | Attack 63 F / Brawl 88 F → repeat: Attack 7 S / Brawl 26 S | PC wins | Troll 89 F | **21** |
| 5 | Troll | Shark 53 S / Defence 35 F | Troll wins | PC 4 S | **0** |
| 5 | PC | Attack 23 S / Brawl 74 F | PC wins | Troll 83 F | **5** |
| 6 | Troll | Shark 33 S / Defence 75 F | Troll wins | PC 61 F | **42** |
| 6 | PC | Attack 35 F / Brawl 12 S | Troll wins | — | 0 |
| 7 | Troll | Shark 16 S / Defence 97 F | Troll wins | PC 50 F | **59** |
| 7 | PC | Attack 72 F / Brawl 57 F → repeat: Attack 2 S / Brawl 81 F | PC wins | Troll 48 F | **27** |
| 8 | Troll | Shark 7 S / Defence 56 F | Troll wins | PC 69 F | **68** |
| 8 | PC | Attack 65 F / Brawl 67 F → repeat: Attack 23 S / Brawl 81 F | PC wins | Troll 17 S | **0** |
| 9 | Troll | Shark 56 S / Defence 52 F | Troll wins | PC 33 S | **19** |
| 9 | PC | Attack 4 S / Brawl 36 S | PC wins | Troll 17 S | **1** |
| 10 | Troll | Shark 13 S / Defence 59 F | Troll wins | PC 36 F | **62** |
| 10 | PC | Attack 70 F / Brawl 44 F → repeat: 42 F / 60 F → repeat: 69 F / 65 F → repeat: 8 S / Brawl 44 F | PC wins | Troll 23 S | **5** |
| 11 | Troll | Shark 28 S / Defence 56 F | Troll wins | PC 93 F | **47** |
| 11 | PC | Attack 89 F / Brawl 57 F → repeat: 46 F / 78 F → repeat: 26 S / Brawl 37 S | PC wins | Troll 72 F | **7** |
| 12 | Troll | Shark 96 F / Defence 32 S | PC wins | — | 0 |
| 12 | PC | Attack 52 F / Brawl 16 S | Troll wins | — | 0 |
| 13 | Troll | Shark 75 S / Defence 10 S | PC wins | — | 0 |
| 13 | PC | Attack 17 S / Brawl 38 S | PC wins | Troll 50 F | **16** |
| 14 | Troll | Shark 59 S / Defence 4 S | PC wins | — | 0 |
| 14 | PC | Attack 28 S / Brawl 84 F | PC wins | Troll 87 F | **5** |
| 15 | Troll | Shark 66 S / Defence 72 F | Troll wins | PC 78 F | **9** |
| 15 | PC | Attack 99 F / Brawl 18 S → repeat | Troll wins | — | 0 |
| 16 | Troll | Shark 97 F / Defence 18 S | PC wins | — | 0 |
| 16 | PC | Attack 23 S / Brawl 18 S | PC wins | — | **0** |
| 17 | Troll | Shark 61 S / Defence 57 F | Troll wins | PC 85 F | **14** |
| 17 | PC | Attack 5 S / Brawl 87 F | PC wins | Troll 39 S | **24** |
| 18 | Troll | Shark 64 S / Defence 72 F | Troll wins | PC 46 F | **11** |
| 18 | PC | Attack 99 F / Brawl 95 F → repeat: Attack 24 S / Brawl 42 S | PC wins | Troll 57 F | **11** |
| 19 | Troll | Shark 11 S / Defence 60 F | Troll wins | PC 79 F | **64** |
| 19 | PC | Attack 22 S / Brawl 77 F | PC wins | Troll 11 S | **0** |
| 20 | Troll | Shark 7 S / Defence 54 F | Troll wins | PC 24 S | **54** |

---

# 7. Final Combat State

The recorded final state was:

| Combatant | Starting HP | Final HP | Status |
|---|---:|---:|---|
| Adventurer-1 | 600 | **−29** | **Incapacitated** |
| Ice Troll | 705 | **583** | Active |

---

# 8. Final Exchange Recorded

The final recorded action was Round 20, Ice Troll turn.

### Troll

| Variable | Value |
|---|---:|
| Attack | Sharktoothed Maw |
| Skill | 75 |
| Natural roll | 7 |
| Result | Success |
| Winner's Margin | 68 |

Winner's Margin as recorded:

`75 − 7 = 68`

### Adventurer-1 Active Defense

| Variable | Value |
|---|---:|
| Defence2 | 38 |
| Natural roll | 24 |
| Result | Success |
| Defender's Margin | 14 |

Defender's Margin as recorded:

`38 − 24 = 14`

### Final Effect

Recorded mitigation:

`68 − 14 = 54 HP Injury`

Recorded HP transition:

`25 HP → −29 HP`

The combatant therefore reached HP ≤ 0 and was recorded as **incapacitated**.

---

# 9. Playtest Completion

The playtest did not terminate at the initial action-selection point because the human participant supplied the missing action instruction:

> **Sharktoothed Maw**

The resulting combat was executed through **Round 20**, at which point Adventurer-1 became incapacitated.

---

# 10. Unedited Result Classification

This report intentionally distinguishes the execution record from subsequent analysis.

| Item | Record Status |
|---|---|
| Sharktoothed Maw selected | **Observed execution input** |
| 20-round combat result | **Observed execution result** |
| Adventurer-1 final HP −29 | **Recorded execution result** |
| Ice Troll final HP 583 | **Recorded execution result** |
| Adventurer-1 incapacitated | **Recorded execution result** |
| Sharktoothed Maw is mandatory Troll attack | **Not established by this report** |
| Sharktoothed Maw is default Troll AI | **Not established by this report** |
| Automatic creature action-selection rule | **Not established by this report** |
| New canonical DEC | **None created** |

---

# 11. Source and Execution Integrity

The v3 prompt explicitly states that this is the first playtest under DEC-094 through DEC-101 and that its purpose is to validate whether the newly ruled sequencing, Frightened, and combat magnitude procedures can resolve deterministically without inventing those values.

The prompt also requires supplied stat blocks to be used verbatim and prohibits inventing new attributes, skills, Tags, or Conditions beyond those ruled or explicitly scaffolded.

The Ice Troll's supplied block specifies:

- HP 705;
- MP 420;
- Physical Energy 220;
- Speed 175;
- Energy Regen 140;
- MP Regen 75;
- Movement Speed 7;
- Icy Claws 67;
- Sharktoothed Maw 75;
- Brawling 37.



---

# 12. Record Handling Instruction for OpenCode

OpenCode should ingest this document as an **unedited playtest execution record**.

OpenCode MUST NOT:

1. Rewrite the recorded rolls.
2. Recalculate the combat retroactively as part of ingestion.
3. Substitute Icy Claws for Sharktoothed Maw.
4. Treat the human's Sharktoothed Maw selection as a new canonical rule.
5. Infer a creature AI procedure from the combat outcome.
6. Create a DEC solely from the existence of this execution record.
7. Remove apparently anomalous entries merely because they require later investigation.

Any validation, mathematical audit, consistency audit, or rules adjudication should be performed as a **separate documented analysis** against this immutable execution record.

---

# 13. Formal Record Status

**PLAYTEST EXECUTION:** COMPLETED  
**ROUNDS COMPLETED:** 20  
**SELECTED TROLL ATTACK:** Sharktoothed Maw  
**TROLL FINAL HP:** 583  
**ADVENTURER-1 FINAL HP:** −29  
**ADVENTURER-1 STATUS:** Incapacitated  
**EXECUTION RECORD:** UNEDITED  
**CANONICAL RULE CHANGE:** NONE

---

# 14. Author

**Author:** GPT-5.6 Luna  
**LLM Version:** GPT-5.6 Luna  
**Date:** 2026-09-04  
**Role:** Tiwas TTRPG Lead Systems Architect and Design Assistant