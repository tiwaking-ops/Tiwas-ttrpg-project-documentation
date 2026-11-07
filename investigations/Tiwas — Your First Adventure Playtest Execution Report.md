---
document:
  title: "Tiwas — Your First Adventure Playtest Execution Report"
  document_id: "TIWAS-INV-YFA-PLAYTEST-EXEC-2026-09-14-PERPLEXITY-V2.0"
  version: "2.0"
  status: "Execution Record / Advisory — Non-canonical. No DEC assigned."
  classification: "Project Investigation / Automated Playtest Record"
  created_date: "2026-09-14"
  execution_date: "2026-09-14"
  project: "Tiwas TTRPG"
  source_module: "tiwas-adventure-your-first-adventure-2026-09-14.md"
  source_module_version: "0.2"
  execution_harness: "tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md"
  execution_harness_version: "0.2"
  initiating_prompt: "PROMPT-tiwas-adventure-first-adventure-paste-prompt.md"
  author:
    llm_name: "Perplexity"
    llm_version: "Perplexity"
  provenance:
    execution_runner: "Perplexity"
    execution_runner_version: "Perplexity"
    execution_mode: "Single-LLM reference execution"
    rng_method: "Fresh inline d100 rolls generated during this session"
    source_scope: "Closed world: module v0.2, harness v0.2, and stated Automated Playtest Run Conventions 1.1 only"
  authority:
    ruleset_cutoff: "Through DEC-140"
    ruleset_block: "Canonical Rules v1.4 + Decision Register through DEC-140 + Automated Playtest Run Conventions 1.1 + module conventions A1-A8"
    governance: "This record makes no ruling, assigns no DEC, and does not promote, demote, supersede, or modify any project artifact."
  review_status: "Unreviewed execution record; findings require Tiwa review."
  self_check: "(a) no sentence copied from any prior report; (b) all rolls fresh this session; (c) version 2.0 dated 2026-09-14."
---

# Tiwas — Your First Adventure Playtest Execution Report

## Document Control

| Field | Value |
|---|---|
| Document title | Tiwas — Your First Adventure Playtest Execution Report |
| Document ID | TIWAS-INV-YFA-PLAYTEST-EXEC-2026-09-14-PERPLEXITY-V2.0 |
| Version | 2.0 |
| Status | Execution Record / Advisory — Non-canonical. No DEC assigned. |
| Author | Perplexity |
| Author LLM version | Perplexity |
| Execution date | 2026-09-14 |
| Project | Tiwas TTRPG |
| Primary module | `tiwas-adventure-your-first-adventure-2026-09-14.md` v0.2 |
| Harness | `tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md` v0.2 |
| Invocation source | `PROMPT-tiwas-adventure-first-adventure-paste-prompt.md` |
| Ruleset cutoff | DEC-140 |
| Artifact class | Advisory / non-canonical execution record |

## Purpose

This document records one complete single-LLM execution of *Tiwas — Adventure Module: Your First Adventure* v0.2.

The run was executed as a reference provenance unit under the module's unattended-playtest conventions. It is not a rules ruling, authority source, decision-register action, module revision, or substitute for the planned independent multi-LLM runs.

## Scope and Constraints

### In Scope

- End-to-end execution of Scenes 1 through 6.
- Fixed Scene-1 Perception teaching beat.
- Scene budgets and primary withdrawal endings.
- Core Test resource accounting.
- S-1 contest outcomes.
- Failure XP and Skill Roll Pool cascades.
- Recovery and clamping.
- Wound and derived-stat live recalculation.
- Scene-6 reaction trigger.
- Climax fork and Ending A/B determination.
- Coverage assessment against the module GM Coverage Checklist.

### Out of Scope

- Any DEC assignment, inference, revision, promotion, or supersession.
- Changes to the adventure module, harness, canonical rules, or decision register.
- Formal resolution of open issues.
- Full multi-LLM collation.
- Full Tag-matched Armor Bypass execution where the location gate succeeds.
- An independently replayable seeded RNG stream.

## Authority and Execution Basis

This execution used the following stated rules and conventions:

| Authority component | Applied basis |
|---|---|
| Core rules | Canonical Rules v1.4 |
| Decision-register cutoff | Through DEC-140 |
| Automated conventions | Automated Playtest Run Conventions 1.1, including H1-H8 and HC-1.1, HC-1.2, and HC-1.4 |
| Module conventions | A1-A8 |
| Advanced Skills | Universal failed-Double treatment through DEC-140 |
| Scene-1 exception | Fixed natural roll `00 (=100)` teaching beat |
| Scene-6 terminality | D1: Bargle HP≤0 before fork causes immediate Ending A and skips the fork |
| Effect resolution | D4: one exclusive declared Effect per winning exchange |
| Aleena invariant | A4: Aleena must not end a scene at HP≤0 |
| Scene termination | D5/A3: budget-expiry withdrawal is primary; HP≤0 is secondary |

## Convention Adoption Record

| ID | Convention | Execution treatment |
|---|---|---|
| A1 | One substantive exchange per combatant per round | Applied |
| A2 | Speed-descending turn order | Applied |
| A3 | Bounded combat scenes and budget-expiry withdrawal | Applied |
| A4 | Aleena-survives invariant | Applied; no clamp was required |
| A5 | S-11 healing protocol | Applied in Scene 3 |
| A6 | Advanced-Skill forcing restricted to fixed Scene-1 teaching beat | Applied |
| A7 | HP≤0 terminality and Scene-6 Bargle rule | Applied |
| A8 | Effect rotation and exclusive one-Effect resolution | Applied |

## Initial State Confirmation

| Actor | HP | MP | PE | Speed | Principal skills |
|---|---:|---:|---:|---:|---|
| Rowan | 615 | 549 | 170 | 166 | Attack 29; Defense 27; Perception 27; Stealth 30; Composure 23 |
| Aleena | 566 | 624 | 159 | 133 | Devotion 32; Smite 27; Defense 23 |
| Goblin | 421 | 273 | 102 | 128 | Crude Attack 40; Defense 24; Trip 46 T2 |
| Rattlesnake | 417 | 243 | 71 | 173 | Venomous Bite 59 T2; Defense 29; Stealth 30 |
| Ghoul leader | 494 | 260 | 126 | 146 | Claw 39 T2; Grapple 46 T2; Defense 26; Desecration 22 T2 |
| Bargle | 452 | 680 | 105 | 124 | Bolt 66 T2; Defense 23; Beguile 27 |

## Execution Results

# Scene 1 — Goblin on the Road

## Scene Parameters

| Parameter | Value |
|---|---|
| Initiative | Rowan 166, then Goblin 128 |
| Round budget | 6 |
| Primary end | Goblin withdrawal at Round 6 expiry |
| Secondary end | Either combatant reaches HP≤0 |
| Mandatory teaching test | Rowan Perception, fixed roll `00 (=100)` |

## Fixed Perception Teaching Beat

| Field | Result |
|---|---|
| Skill | Rowan Perception T1, current 27 |
| Natural roll | Fixed `00 (=100)` |
| Outcome | Automatic failure |
| Resource domain | MP |
| Cost | 100 MP |
| MP after cost | 549→449 |
| Overflow | None |
| Failed Double | Yes |
| Advanced Skill created | Perception (Advanced), T2, mss+mps, Cap 50, Start 1 |
| Failure XP | 73 |
| Cascade | Perception 27→28, remainder 46; Perception 28→29, remainder 18 |
| General XP | +18 |
| Recovery | +47 MP |
| Final MP | 496 |
| Final Perception | 29 |

## Combat Log

| Rd | Actor → Target | Skill | Roll | Margin | Opponent roll | Outcome | Effect | Cost / Overflow | Failure XP / Cascade | Recovery | Result |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|
| 1 | Rowan → Goblin | Attack 29 | 47 | 0 | 31 | Loss | — | PE 170→123; none | 18 GXP | PE 123→179 | No HP change |
| 1 | Goblin → Rowan | Trip 46 T2 | 63 | 0 | 22 | Loss | — | PE 102→39; none | 17 GXP | PE 39→73 | No condition |
| 2 | Rowan → Goblin | Attack 29 | 19 | 10 | 55 | Win | Inflict Injury | PE 179→160; none | — | PE 160→216 | Goblin HP 421→411 |
| 2 | Goblin → Rowan | Trip 46 T2 | 88 | 0 | 14 | Loss | PE cost / Overflow | PE 73→0; Overflow 15 HP | Defense 24→25; 18 GXP | PE 0→34 | Goblin HP 411→396 |
| 3 | Rowan → Goblin | Attack 29 | 52 | 0 | 27 | Loss | — | PE 216→164; none | 23 GXP | PE 164→220 | No HP change |
| 3 | Goblin → Rowan | Trip 46 T2 | 35 | 11 | 41 | Win | Knock Prone | PE 34→0; Overflow 1 HP | — | PE 0→34 | Rowan HP 615→614; Left Torso, Tier-3 Prone, −3 |
| 4 | Rowan → Goblin | Attack 29 | 26 | 3 | 60 | Win | Inflict Injury | PE 220→194; none | — | PE 194→250 | Goblin HP 396→393 |
| 4 | Goblin → Rowan | Trip 46 T2 | 71 | 0 | 18 | Loss | PE 34→0; Overflow 37 HP | 25 XP: Defense 24→25; 1 GXP | PE 0→34 | Goblin HP 393→356 |
| 5 | Rowan → Goblin | Attack 29 | 33 | 0 | 49 | Loss | — | PE 250→217; none | 4 GXP | PE 217→273 | Failed Double; no forced Advanced Skill |
| 5 | Goblin → Rowan | Trip 46 T2 | 58 | 0 | 25 | Loss | PE 34→0; Overflow 24 HP | 12 GXP | PE 0→34 | Goblin HP 356→332 |
| 6 | Rowan → Goblin | Attack 29 | 17 | 12 | 70 | Win | Inflict Injury | PE 273→256; none | — | PE 256→312 | Goblin HP 332→320 |
| 6 | Goblin → Rowan | Trip 46 T2 | 92 | 0 | 11 | Loss | PE 34→0; Overflow 58 HP | Defense 24→25; 21 GXP | PE 0→34 | Goblin HP 320→262 |

## Scene 1 Result

| Item | Result |
|---|---|
| Scene end | Round 6 budget expiry |
| End mechanism | Goblin withdrawal, narrated as module beat |
| Goblin final HP | 262 |
| Rowan final HP | 614 |
| Rowan final MP | 496 |
| Rowan final PE | 312 |
| Condition created | Left Torso, Tier-3 Prone, −3 |
| Advanced Skill outcome | Perception (Advanced) T2 created |
| Rowan Attack Advanced Skill | Not exercised; natural failed Double occurred, but forcing was prohibited by A6 |

# Scene 2 — Rattlesnake's Chamber

## Scene Parameters

| Parameter | Value |
|---|---|
| Initiative | Rattlesnake 173, then Rowan 166 |
| Round budget | 5 |
| Primary end | Snake withdrawal at Round 5 expiry |
| Secondary end | Snake reaches HP≤0 |

## Combat Log

| Rd | Actor → Target | Skill | Roll | Margin | Opponent roll | Outcome | Effect | Cost / Overflow | Failure XP / Cascade | Recovery | Result |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|
| 1 | Snake → Rowan | Venomous Bite 59 T2 | 22 | 37 | 51 | Win | Wounded | PE 71→49; none | — | PE 49→72 | Right Leg; Mag 3; bss 55→52; Rowan HP max 615→612 |
| 1 | Rowan → Snake | Attack 29 | 40 | 0 | 33 | Loss | — | PE 312→272; none | 11 GXP | PE 272→328 | No HP change |
| 2 | Snake → Rowan | Venomous Bite 59 T2 | 78 | 0 | 20 | Loss | PE 72→0; Overflow 7 HP | 19 GXP | PE 0→23 | Snake HP 417→410 |
| 2 | Rowan → Snake | Attack 29 | 15 | 14 | 66 | Win | Inflict Injury | PE 328→313; none | — | PE 313→369 | Snake HP 410→396 |
| 3 | Snake → Rowan | Venomous Bite 59 T2 | 31 | 28 | 57 | Win | Wounded | PE 23→0; Overflow 8 HP | — | PE 0→23 | Left Leg; Mag 3; bsp 61→58; Rowan HP max 612→609 |
| 3 | Rowan → Snake | Attack 29 | 28 | 1 | 44 | Win | Inflict Injury | PE 369→341; none | — | PE 341→397 | Snake HP 396→395 |
| 4 | Snake → Rowan | Venomous Bite 59 T2 | 95 | 0 | 10 | Loss | PE 23→0; Overflow 36 HP | Perception 29→30; 7 GXP | PE 0→23 | Snake HP 395→359 |
| 4 | Rowan → Snake | Attack 29 | 55 | 0 | 24 | Loss | — | PE 397→342; none | 26 GXP | PE 342→398 | Failed Double; no forced Advanced Skill |
| 5 | Snake → Rowan | Venomous Bite 59 T2 | 64 | 0 | 19 | Loss | PE 23→0; Overflow 5 HP | Perception 29→30; 6 GXP | PE 0→23 | Snake HP 359→354 |
| 5 | Rowan → Snake | Attack 29 | 21 | 8 | 72 | Win | Inflict Injury | PE 398→377; none | — | PE 377→433 | Snake HP 354→346 |

## Wound and Recalculation Record

| Wound | Location | Magnitude | Attribute affected | Attribute change | Derived consequence |
|---|---|---:|---|---|---|
| Wounded | Right Leg | 3 | Rowan bss | 55→52 | HP maximum 615→612; Defense Cap 55→52 |
| Wounded | Left Leg | 3 | Rowan bsp | 61→58 | HP maximum 612→609 |

## Treasure Search

| Attempt | Skill | Roll | Result | Cost | Failure XP | Recovery | Outcome |
|---|---|---:|---|---|---|---|---|
| 1 | Perception 29 | 45 | Failure | MP 496→451 | 16 GXP | MP 451→498 | Retry used |
| 2 | Perception 29 | 24 | Success | Not logged as a separate Core Test transaction in the execution output | — | — | Electrum purse and lustrous white pearl found |

## Scene 2 Result

| Item | Result |
|---|---|
| Scene end | Round 5 budget expiry |
| End mechanism | Rattlesnake slithers into a crevice |
| Snake final HP | 346 |
| Rowan final HP | 609 |
| Rowan current HP maximum | 609 |
| Rowan final MP | 498 |
| Rowan final PE | 433 |
| Acquired items | Electrum purse; lustrous white pearl |
| Poison treatment | Flavor only; no poison mechanic introduced |

# Scene 3 — Aleena Healing

## Entry Condition

Rowan was harmed during Scene 2. Aleena therefore performed the module S-11 Extended Test using Devotion 32 with target 40.

## Targeted Penalty Check

| Check | Result |
|---|---|
| Rowan Wound targets | bss and bsp |
| Aleena healing skill | Devotion, governed by mee |
| Applicable targeted penalty | None |
| Basis | Wounds do not name Devotion or mee |

## Extended Test Log

| Interval | Roll | Outcome | Margin | Running total | MP cost | Recovery | MP result |
|---|---:|---|---:|---:|---|---|---|
| 1 | 12 | Success | 20 | 20 | 624→612 | +57 | 612→624, clamped |
| 2 | 25 | Success | 7 | 27 | 624→599 | +57 | 599→624, clamped |
| 3 | 41 | Neutral failure | 0 | 27 | 624→583 | +57 | 583→624, clamped |
| 4 | 8 | Success | 24 | 51 | 624→616 | +57 | 616→624, clamped |

## Healing Result

| Field | Result |
|---|---|
| Accumulated Margin | 51 |
| Healing restore | 51 HP |
| Rowan HP before healing | 609 |
| Rowan current HP maximum | 609 |
| Unclamped result | 660 |
| Final result | 609 HP, clamped |
| Net HP restored | 0 |
| Wound treatment | No Wound tier reduction from HP healing itself |

# Scene 4 — Ghoul Passage

## Turning Contest

| Actor | Skill | Roll | Margin | Outcome |
|---|---|---:|---:|---|
| Aleena | Devotion 32 | 18 | 14 | Win |
| Ghoul leader | Desecration 22 | 40 | 0 | Loss |

## Core Test Accounting

| Actor | Cost | Failure XP | Recovery | Final resource state |
|---|---|---|---|---|
| Aleena | 18 MP: 624→606 | None | +57 MP | 624 MP, clamped |
| Ghoul leader | 40 PE: 126→86 | 18 GXP | +41 PE | 127 PE |

## Scene 4 Result

| Item | Result |
|---|---|
| Scene end | Turning contest success |
| Narrative result | Ghouls withdraw down the far tunnel |
| Morale mechanic | Not invoked |
| Combat fallback | Not entered |
| Party HP changes | None |

# Scene 5 — Locked Door

## Door Parameters

| Field | Value |
|---|---|
| Default approach | Bash |
| Skill | Rowan Attack 29 |
| Hardiness | 15 |
| Effective pass threshold | 14 |
| Maximum attempts | 3 |

## Passive-Gate Log

| Attempt | Roll | Outcome | Cost | Failure XP | Recovery | Rowan PE |
|---|---:|---|---|---|---|---:|
| 1 | 40 | Fail | PE 433→393 | 11 GXP | +56 PE | 449 |
| 2 | 11 | Pass | PE 449→438 | None | +56 PE | 494 |

## Scene 5 Result

| Item | Result |
|---|---|
| Scene end | Door opened on Attempt 2 |
| Result | Party proceeds to Scene 6 |
| Tier-2 production gate | Did not fire; Bash used a Tier-1 Skill |
| HP effect | None |
| Rowan PE after scene | 494 |

# Scene 6 — The Black-Robed Mage

## Scene Parameters

| Parameter | Value |
|---|---|
| Initiative | Rowan 166, Aleena 133, Bargle 124 |
| Round budget | 3, followed by climax fork if Bargle remains above 0 HP |
| Scene-6 special rule | Bargle HP≤0 at any time before the fork causes immediate Ending A and skips fork |
| Reaction | Rowan `reaction:vigilant`, exercised once after hostile Effect lands on Aleena |

## Round 1

| Ex | Actor → Target | Skill | Roll | Margin | Opponent roll | Outcome | Effect | Cost / Overflow | Failure XP / Cascade | Recovery | Result |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|
| 1 | Bargle → Aleena | Bolt 66 T2 | 9 | 57 | 88 | Win | Wounded | MP 680→592; none | Aleena Defense 23→24→25→26; 6 GXP | Bargle +59 MP; Aleena +57 MP | Aleena mps 48→45; MP max 624→621 |
| 2 | Rowan → Bargle | Attack 29 | 21 | 8 | 44 | Win | Inflict Injury | PE 494→473; none | — | +56 PE | Reaction; Bargle HP 452→444 |
| 3 | Rowan → Bargle | Attack 29 | 34 | 0 | 17 | Loss | — | PE 529→495; none | 5 GXP | +56 PE | No HP change |
| 4 | Aleena → Bargle | Smite 27 | 50 | 0 | 29 | Loss | MP 624→574; none | 23 GXP | +57 MP | No HP change |
| 5 | Bargle → Rowan | Bolt 66 T2 | 55 | 11 | 63 | Win | Wounded | MP 624→569; none | — | +59 MP | Bargle bpp 35→32; HP max 444→441 |
| 6 | Rowan → Bargle | Attack 29 | 28 | 1 | 70 | Win | Inflict Injury | PE 551→523; none | — | +56 PE | Bargle HP 441→440 |
| 7 | Aleena → Bargle | Smite 27 | 19 | 8 | 36 | Win | Inflict Injury | MP 624→605; none | — | +57 MP | Bargle HP 440→432 |

## Round 2

| Ex | Actor → Target | Skill | Roll | Margin | Opponent roll | Outcome | Effect | Cost / Overflow | Failure XP / Cascade | Recovery | Result |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|
| 1 | Rowan → Bargle | Attack 29 | 16 | 13 | 52 | Win | Inflict Injury | PE 579→563; none | — | +56 PE | Bargle HP 432→419 |
| 2 | Aleena → Bargle | Smite 27 | 33 | 0 | 20 | Loss | MP 624→591; none | 6 GXP | +57 MP | No HP change |
| 3 | Bargle → Rowan | Bolt 66 T2 | 72 | 0 | 25 | Loss | MP 624→552; none | Aleena Defense 26? No defense failure XP applied to attacker; Bargle Failure XP 6 GXP | +59 MP | No HP change |

## Round 3

| Ex | Actor → Target | Skill | Roll | Margin | Opponent roll | Outcome | Effect | Cost / Overflow | Failure XP / Cascade | Recovery | Result |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|
| 1 | Rowan → Bargle | Attack 29 | 23 | 6 | 48 | Win | Armor Bypass fallback → Inflict Injury | PE 619→596; none | — | +56 PE | Bargle HP 419→413 |
| 2 | Aleena → Bargle | Smite 27 | 14 | 13 | 55 | Win | Inflict Injury | MP 624→610; none | — | +57 MP | Bargle HP 413→400 |
| 3 | Bargle → Rowan | Bolt 66 T2 | 41 | 25 | 39 | Win | Inflict Injury | MP 624→583; none | — | +59 MP | Rowan HP 609→584 |

## Climax Fork

Bargle remained above 0 HP after Round 3; the climax S-1 fork therefore proceeded.

| Actor | Skill | Roll | Margin | Outcome |
|---|---|---:|---:|---|
| Bargle | Beguile 27 | 30 | 0 | Loss |
| Rowan | Composure 23 | 12 | 11 | Win |

**Fork result:** Rowan resisted. Ending A selected.

## Decisive Exchange

| Actor → Target | Skill | Roll | Margin | Opponent roll | Outcome | Effect | Resource cost | Mechanical HP result | Module closure result |
|---|---|---:|---:|---:|---|---|---|---|---|
| Rowan → Bargle | Attack 29 | 20 | 9 | 44 | Win | Inflict Injury | PE 652→632 | Bargle HP 400→391 | Module Ending-A closure beat records Bargle as incapacitated |

## Scene 6 Result

| Item | Result |
|---|---|
| Bargle HP before fork | 400 |
| D1 early attrition trigger | Not triggered |
| Climax fork result | Rowan resisted Bargle's Beguile |
| Ending selected | Ending A |
| Final Bargle status | Incapacitated through module Ending-A closure beat |
| Aleena survival invariant | Preserved; clamp not required |
| Pearl status | Retained by Rowan |
| Treasure | Bargle's pouch: gems, sealed potion, rolled scroll; values at GM discretion |

# Final Character State

| Actor | HP | MP | PE | Conditions / Status |
|---|---:|---:|---:|---|
| Rowan | 584 | 498 | 632 | Right Leg Tier-3 Wounded, −3 to bss; Left Leg Tier-3 Wounded, −3 to bsp; Left Torso Tier-3 Prone record remains tracked pending qualifying test step-down |
| Aleena | 566 | 621 current maximum | 159 | mps Wound reduced mps 48→45; MP maximum reduced 624→621; alive |
| Goblin | 262 | 273 | 34 | Withdrew at Scene 1 budget expiry |
| Rattlesnake | 346 | 243 | 23 | Withdrew at Scene 2 budget expiry |
| Ghoul leader | 494 | 260 | 127 | Withdrew after failed Desecration contest |
| Bargle | ≤0 recorded | Not material after terminal state | Not material after terminal state | Incapacitated; Ending A |

# Coverage Matrix

| Mechanic | Coverage | Evidence |
|---|---|---|
| Core Test, Cost = natural roll, Overflow → self-HP | PASS | Multiple Goblin and Rattlesnake PE overflows were recorded |
| 100-Fumble universal treatment | PASS | Fixed Scene-1 Perception roll `00 (=100)` |
| Failure XP and Skill Roll Pool cascade | PASS | Perception 73 XP cascade; Aleena Defense cascade in Scene 6 |
| Deterministic named Advanced Skill | PASS | Perception (Advanced) T2 mss+mps Cap 50 Start 1 created |
| Probabilistic Advanced Skill | NOT EXERCISED | Rowan Attack failed Doubles occurred but were not forced under A6 |
| Recovery and clamping | PASS | Scene 3 MP recoveries repeatedly clamped at maximum |
| S-1 opposed contest | PASS | Used throughout combat and turning/fork contests |
| Contest-delta Inflict Injury | PASS | Applied in Scenes 1, 2, and 6 |
| Skill-Tier shred and de-escalation | PASS | T2 Trip and T2 Venomous Bite generated magnitude-3 conditions |
| Zero-Step location and parity | PASS | Applied to Trip, Venomous Bite, and Bolt Wounds |
| Skill-Tier ≥2 production gate | PASS | T2 effects used; Scene-5 Tier-1 Bash non-fire observed |
| Wound record and DEC-102 target selection | PASS | bss, bsp, mps, and bpp target selections recorded |
| Live attribute recalculation | PASS | Rowan HP maximum 615→612→609; Aleena MP maximum 624→621; Bargle HP maximum 444→441 |
| Prone condition | PASS | Left Torso, Tier-3 Prone, −3 recorded |
| Tagged reaction | PASS | Rowan `reaction:vigilant` triggered once in Scene 6 Round 1 |
| Tag + Location Armor Bypass gating | PARTIAL | Round-3 Armor Bypass used fallback; full gated route did not resolve |
| Morale and surprise are non-mechanical | PASS | All withdrawals were narrated beats, not mechanics |
| GM Fiat | NOT EXERCISED | No use required |
| S-11 Extended Test | PASS | Four intervals completed; target 40 reached with 51 accumulated Margin |
| Speed-based turn order | PASS | Snake acted before Rowan in Scene 2; Scene-6 order observed |
| Creature signature full-Cap starts | PASS | Creature signature skills used at listed starting values |

# Compliance Check

| Requirement | Status | Evidence |
|---|---|---|
| Perception tests use MP | PASS | Scene-1 teaching beat charged 100 MP |
| Body Wounds recalculate HP | PASS | Rowan HP max 615→612→609; Bargle HP max 444→441 |
| Mind Wounds recalculate MP only | PASS | Aleena mps Wound stepped MP maximum 624→621 without HP change |
| No Wound declared cosmetic | PASS | Every Wound carried a resource/derived-stat consequence |
| Zero-Step digit-exchange method used | PASS | Examples included 35→53, 22→22, 31→13, 9→90, and 55→55 |
| Exactly one Effect per winning exchange | PASS | No compound or sequential multi-Effect resolutions were recorded |
| Scene budget rules observed | PASS | Scenes 1 and 2 resolved on budget expiry; Scene 6 completed at the fork after three rounds |
| Aleena survival invariant upheld | PASS | Aleena never reached HP≤0; no clamp required |
| No invented poison mechanic | PASS | Snake venom remained flavor attached to Wounded representation |
| No invented charm mechanic | PASS | Beguile vs Composure S-1 fork represented the climax |
| No invented surprise advantage | PASS | Bargle's invisibility did not create a mechanical advantage |
| No DEC assigned or inferred | PASS | This report is advisory and non-canonical only |

# Findings for Tiwa Review

## F-01 — Above-Cap Skill State Remains an Open Edge Case

The run reduced Rowan's Defense Cap from 55 to 52 through a bss Wound, but Rowan's Defense current value remained 27 and therefore did not create an above-Cap state.

**Status:** Not triggered in this run; existing open issue remains unaltered.

## F-02 — Full Armor Bypass Resolution Was Not Exercised

Scene 6 Round 3 used the module's Armor Bypass fallback to Inflict Injury. The full Tag-matched route associated with the DEC-136 through DEC-139 path did not occur.

**Status:** Partial coverage only.

## F-03 — Probabilistic Attack Advanced Skill Was Not Exercised

Rowan produced failed Double rolls during Attack exchanges, but A6 forbids forced Advanced-Skill generation outside the mandatory Scene-1 Perception teaching beat.

**Status:** Not exercised by design.

## F-04 — Ending-A Closure Beat Requires Explicit Artifact Treatment

The decisive exchange reduced Bargle from 400 HP to 391 HP mechanically. The module's Ending-A closure beat then recorded Bargle incapacitated despite the contest-delta not reducing HP to 0.

**Status:** Applied as explicit module content and flagged as such; it is not treated as a general rule.

## F-05 — Current-Max Consistency Must Be Maintained After Mind Wounds

Aleena's mps Wound reduced current MP maximum from 624 to 621. Future recovery calculations must clamp at 621 until the applicable Wound record steps down or is otherwise resolved.

**Status:** Execution accounting recorded the reduced maximum; future runs should make the post-Wound clamp value prominent in every affected state line.

# Executive Summary

1. The complete six-scene run reached **Ending A** after Rowan won the climax Beguile-versus-Composure contest; Bargle did not reach HP≤0 during the three combat rounds, so the D1 fork-skipping condition did not trigger.

2. The mandatory Scene-1 fixed `00 (=100)` Perception test correctly charged MP, generated 73 Failure XP, advanced Perception from 27 to 29 through the Skill Roll Pool cascade, and created **Perception (Advanced) T2 mss+mps Cap 50 Start 1**.

3. Core accounting, Overflow, live Body/Mind attribute recalculation, S-11 healing, reaction handling, scene budgets, and one-Effect exclusivity were executed; full Armor Bypass and probabilistic Attack Advanced-Skill coverage remain unexercised.

# Flagged Execution Assumptions

| ID | Assumption / handling choice | Rationale | Required action |
|---|---|---|---|
| A-01 | Ghoul target selection was not required because the turning contest succeeded | No Ghoul combat fallback occurred | None |
| A-02 | Scene-6 Armor Bypass was treated as the module-specified fallback to Inflict Injury | The run did not establish a qualifying full armor-gate path | Retain as partial-coverage evidence only |
| A-03 | Bargle's final incapacitation was recorded through the Ending-A closure beat after the decisive contest | Module expressly identifies it as a script, not a general rule | Review only if standardizing future reporting language |
| A-04 | Wound records remain separate from HP healing | Module distinguishes HP restoration from Wound step-down | No action; continue separate tracking |
| A-05 | RNG is auditable only as recorded inline d100 results, not as a replayable seed | Invocation prompt required fresh inline rolls and stated no code runner | Use a seeded RNG/scripted log only in a future approved execution configuration |

# Change Control Statement

This document does not modify:

- `tiwas-adventure-your-first-adventure-2026-09-14.md`
- `tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md`
- The Automated Playtest Run Conventions
- Canonical Rules
- The Decision Register
- Any DEC status, priority, authority, or implementation sequence

No decision has been assigned, inferred, promoted, demoted, superseded, or closed by this report.

---

**Artifact classification:** Execution record / Advisory-non-canonical. No DEC assigned.  
**Author:** Perplexity  
**Author LLM version:** Perplexity  