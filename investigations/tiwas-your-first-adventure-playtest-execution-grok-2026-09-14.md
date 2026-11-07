---
document:
  title: "Tiwas — Your First Adventure: Playtest Execution Report (v0.2 run)"
  version: "2.0"
  status: "Execution record / Advisory-non-canonical. No DEC assigned. Does not promote, lock, amend, or supersede any rule or module text."
provenance:
  author_llm: {name: "Grok 4.5", version: "grok-4.5"}
  created_date: "2026-09-14"
  source_module: "tiwas-adventure-your-first-adventure-2026-09-14.md (advisory v0.2)"
  ruleset_applied: "Canonical Rules v1.4 + Decision Register through DEC-140 (incl. DEC-132/132.A/132.B, DEC-135, DEC-136–139, DEC-072.A amendment, DEC-140 universal Advanced Skill) + Automated Playtest Run Conventions 1.1 (H1–H8, HC-1.1/1.2/1.4) + module Run Conventions A1–A8"
  execution_method: "Python 3 random.SystemRandom() simulation script"
  script_location: "artifacts/tiwas-yfa-v02-fresh-playtest-script-2026-09-14.py"
  ledger_location: "artifacts/tiwas-yfa-v02-fresh-ledger-2026-09-14.txt"
  txns_location: "artifacts/tiwas-yfa-v02-fresh-txns-2026-09-14.json"
  rng: "random.SystemRandom() fresh entropy, new run 2026-09-14; no seed"
  conventions_altered: "None. All A1–A8 and H-block items confirmed adopted. Zero-Step per Canonical §14.1; Recovery floor(ER/2) or floor(MR/2); exclusive one-Effect (D4); D1 attrition-first Ending A; A4 clamp."
---

# Tiwas — Your First Adventure: Playtest Execution Report (v0.2 run)

**Document role.** Formal record of a live-roll, unattended execution of the 2026-09-14 adventure module *Your First Adventure* (v0.2). This document is an execution and observation record only. It does not constitute a designer ruling, does not assign or amend any DEC, and does not promote any procedure to Canonical or Ruled status.

**Audience.** OpenCode (implementation / scripting handoff) and Tiwa (designer review).

**Self-check (mandatory):** (a) No sentence was copied from any prior v0.1 or earlier v0.2 report; (b) the roll ledger is new and generated under fresh SystemRandom entropy on 2026-09-14; (c) document version is 2.0 with created_date 2026-09-14.

---

## 1. Purpose and Scope

### 1.1 Purpose

Execute the full module end-to-end under live SystemRandom rolls, exercising:
- Scene-1 mandatory fixed-roll 00 (=100) Perception teaching beat (D2/D6) creating named Advanced Skill Perception (Advanced) T2 mss+mps Cap50 Start1
- Expanded cast (Goblin, Rattlesnake, Ghoul pack, Bargle)
- DEC-132.B reaction:vigilant single exercise
- Armor Bypass no-match fallback (DEC-030)
- Climax Beguile/Composure S-1 fork with D1 attrition-first Ending A rule
- Aleena-survives invariant (A4)
- Bounded scene budgets with D5 primary budget-expiry withdrawal
- Exclusive one-Effect-per-winning-exchange (D4)
- GM Coverage Checklist items under DEC-140

### 1.2 Scope boundaries

- **In scope:** All mechanics listed in the module’s GM Coverage Checklist and the harness Narrator/Sampler contracts (Core Test 9-step, S-1, Zero-Step Location + parity + quartiles, Skill-Tier shred, Wound/Prone, contest-delta Injury, Failure XP cascade, Recovery + clamp, Speed turn order, Reactions, S-11 Extended, passive-gate tests).
- **Explicitly out of scope / flagged by module:** Active Defense as distinct Core Test (DEC-044); Fatigue from repeated defenses (DEC-135); full Tag-matched Armor Bypass (DEC-136–139 — module deliberately falls back); Encumbrance; Equipment damage; ruled charm/poison/morale/surprise Effects (all represented by flagged ruled-equivalents or narrated beats).

### 1.3 Authority statement

All mechanics applied are either Canonical/Locked or Non-canonical designer rulings recorded in the Decision Register as Current/Ruled through DEC-140. No rule text was altered. The module itself remains Advisory / Non-canonical. Corrections and open items are reported, never silently applied.

---

## 2. Ruleset Applied (Frontmatter Confirmation)

| Layer | Document / Cut-off |
|---|---|
| Canonical | `tiwas-canonical-rules-and-changelog-v1.3.md` (internal v1.4) |
| Decision Register | through DEC-140 (incl. DEC-132/132.A/132.B, DEC-135, DEC-136–139, DEC-072.A, DEC-140) |
| Automated Playtest Run Conventions | 1.1 (H1–H8, HC-1.1/1.2/1.4) |
| Module Run Conventions | A1–A8 (confirmed below) |
| Source module | tiwas-adventure-your-first-adventure-2026-09-14.md v0.2 |

**A1–A8 confirmation (one bullet each):**

- **A1** Action economy: one substantive exchange per combatant per round — adopted and enforced.
- **A2** Turn order: Speed-desc (DEC-095); ties bss then bsp then reroll — adopted.
- **A3** Bounded scenes: Scene1 ≤6, Scene2 ≤5, Scene4 ≤3, Scene6 ≤3 + fork — adopted; resolution by HP≤0 or budget expiry (D5 primary).
- **A4** Aleena-survives invariant: if resolved HP would cross 0, clamp to 1 and narrate collapse — adopted (did not trigger).
- **A5** Healing: H1(a) Margin restore clamped current max; H2 target 40; H3 Devotion MP cost; H7 locked order; HC-1.1/1.2 — adopted.
- **A6** Advanced-Skill: Scene-1 Perception teaching beat mandatory fixed-roll 00; all other Advanced-Skill creation probabilistic — adopted; Power Strike branch not exercised.
- **A7** Terminality: HP≤0 = forced incapacitation (DEC-052; negative persists DEC-108); Scene-6 Bargle HP≤0 before fork → Ending A + fork SKIPPED (D1) — adopted.
- **A8** Effect exclusivity (D4): exactly one declared Effect per winning exchange — adopted.

---

## 3. Initial-State Confirmation Table

All 24-attribute blocks and derived values initialized **verbatim** from the module. No edits, fixes, or reinterpretations.

| Combatant | HP (max) | PE (max) | MP (max) | Speed | Key Skills (Start at init) | Notes |
|---|---:|---:|---:|---:|---|---|
| Rowan | 615 | 170 | 549 | 166 | Attack 29, Defense 27, Perception 27, Stealth 30, Composure 23 | reaction:vigilant; Leather Armor |
| Aleena | 566 | 159 | 624 | 133 | Devotion 32, Smite 27, Defense 23 | Holy Vestments (no armor Tag) |
| Goblin | 421 | 102 | 273 | 128 | Crude Attack 40 sig, Trip 46 T2 sig, Defense 24 | Creature |
| Rattlesnake | 417 | 71 | 243 | 173 | Venomous Bite 59 T2 sig, Defense 29, Stealth 30 | Creature; acts first Scene 2 |
| Ghoul | 494 | 126 | 260 | 146 | Claw 39 T2, Grapple 46 T2, Defense 26, Desecration 22 T2 | Pack leader representative |
| Bargle | 452 | 105 | 680 | 124 | Bolt 66 T2 sig, Defense 23, Beguile 27 | Creature targeting; Robes no armor Tag |

Derived formulas locked per Canonical §4 / DEC-004. Live recalculation of HP/MP on Body/Mind attribute Wounds applied 1:1 (module pattern 615→612; 624→621).

---

## 4. Per-Scene Exchange Logs

Full raw ledger (160 mapped d100 entries) and transaction JSON (158 rows) stored as artifacts. Every d100 is logged with scene/round/actor/skill mapping. Below: condensed mechanical outcomes with key transaction fields.

### 4.1 Scene 1 — Goblin on the Road (Budget 6)

**Pre-combat mandatory teaching beat (D2/D6 fixed roll 00=100):**
- Roll: fixed 100 (logged as FIXED teaching beat)
- Cost: 100 MP (549 → 449); Overflow: 0
- Outcome: auto-fail (DEC-001)
- Failure XP: 73 → cascade [27→28, 28→29] rem 18 → General XP
- Recovery: +47 → MP 496
- Advanced Skill created: **Perception (Advanced) T2 mss+mps Cap 50 Start 1** (DEC-012 / DEC-140)

**Combat (Speed Rowan 166 → Goblin 128):**

| Rnd | Actor → Target | Skill | Roll | Margin | Outcome | Effect / Result | Key Txn Notes |
|---|---|---|---:|---:|---|---|---|
| R1 | Rowan→Goblin | Attack 29 | 25 | 4 | Win | Inflict Injury 4 | Goblin 421→417; Cost 25 PE |
| R1 | Goblin→Rowan | Trip 46 | 17 | 29 | Win | Knock Prone Left Torso Mag3 (LI=71) | Shred T2>T1 |
| R2 | Rowan→Goblin | Attack | multiple (tie path) | 0 | Fail | — | Defense held after rerolls |
| R2 | Goblin→Rowan | Trip | 11 | — | Win | Knock Prone Left Legs Mag3 (LI=11) | |
| R3 | Rowan→Goblin | Attack 32 | 15 | 17 | Win | Inflict Injury 17 | Goblin →294 |
| R3 | Goblin→Rowan | Trip | 33 | — | Win | Knock Prone Left Arms Mag3 (LI=33) | |
| R4 | Rowan→Goblin | Attack | 29 | 4 | Win | Inflict Injury 4 | Goblin →220 |
| R4 | Goblin→Rowan | Trip | 7 | — | Win | Knock Prone Right Torso Mag3 (LI=70) | |
| R5 | Rowan→Goblin | Attack | — | 2 vs 25 | Fail | — | |
| R5 | Goblin→Rowan | Trip | 69 | 0 | Fail | — | |
| R6 | Rowan→Goblin | Attack | — | 0 | Fail | — | |
| R6 | Goblin→Rowan | Trip | — | — | Win | Knock Prone Right Arms Mag3 (LI=34) | |

**End condition:** Round 6 budget expiry → Goblin **WITHDRAWS** (primary end, D5 / source beat). Goblin final HP 89 > 0. Rowan HP remained at max through Sc1 (no successful Injury landed on him). Multiple free stands (DEC-082) after Prone.

Key mechanics: Overflow on Goblin PE from high Trip/Defense costs; Failure XP cascade stepped Attack and Defense; exclusive Prone Effect; Speed order; fixed 100-Fumble Advanced Skill.

### 4.2 Scene 2 — Rattlesnake’s Chamber (Budget 5, Snake first)

| Rnd | Actor → Target | Skill | Outcome | Effect / Result |
|---|---|---|---|---|
| R1 | Snake→Rowan | Venomous Bite T2 | Win | Wounded Right Legs bss−3 → maxHP 615→612 |
| R1 | Rowan→Snake | Attack | Win | Injury 17 → Snake 417→235 (after Overflow pressure) |
| R2 | Snake→Rowan | Venomous Bite | Win | Wounded Right Head bsp−3 → maxHP 609 |
| R3 | Snake→Rowan | Venomous Bite | Win | Wounded Left Torso bsp−3 → maxHP 606 |
| R4 | Snake→Rowan | Venomous Bite | Win | Wounded Right Legs bss−3 → maxHP 603; Rowan Injury 31 → Snake 53 |
| R5 | Snake→Rowan | Venomous Bite | Win | Wounded Right Torso bss−3 → maxHP 600 |

**End condition:** Round 5 budget expiry → Snake **withdraws** (primary D5). Snake HP 53 > 0.

**Treasure Search:** Perception (original, current 29) roll failed → pearl **not found**. Cost charged to MP; Failure XP to GXP; Recovery applied.

Key mechanics: T2 Venomous Bite, Zero-Step + quartile + parity, Body Wound live recalc (HP step), exclusive Wounded Effect, Speed-first foe, 5× Body Wounds accumulated.

### 4.3 Scene 3 — Aleena (S-11 Healing)

Rowan at current max HP post-Wound (600/600) with open Wound records → S-11 Extended Test executed (4 intervals, Devotion 32, H2 target 40, full H7 order).

- Observed total Margin: 47 (≥40)
- Restore HP = 0 (already at current max; H1(a)/HC-1.2 clamp)
- Wound records remain (separate action required per DEC-035.A / DEC-121)
- Aleena MP recovered under clamp

### 4.4 Scene 4 — The Ghoul Passage

- Turning S-1: Aleena Devotion vs Ghoul Desecration → **FAIL** (attacker margin lower)
- Fight budget 3 entered.
- R1–R3: Rowan + Aleena Injuries reduced Ghoul representative (494 → 262 at expiry)
- **End condition:** Round 3 expiry → pack breaks at tunnel mouth, party slips past (source beat, narrated; no morale rule).

### 4.5 Scene 5 — The Locked Door

- Default approach: bash (Attack − hardiness 15)
- Attempt 1: roll 42 vs effective 23 → FAIL, Cost 42 PE
- Attempt 2: roll 66 vs effective 23 → FAIL, Cost 66 PE
- Attempt 3: roll 84 vs effective 23 → FAIL, Cost 84 PE
- 3 fails → forced open by exhaustion (narrated). Party proceeds.
- Teach: Tier-1 Skill → Skill-Tier ≥2 production gate does **not** fire (DEC-041) — no Location Index, no Wound.

### 4.6 Scene 6 — The Black-Robed Mage (Budget 3 + climax fork)

- Initiative: Rowan 166 → Aleena 133 → Bargle 124. (Invisibility flagged: no mechanical surprise advantage.)
- **R1:**
  - Bargle Bolt win → Impose Wounded Right Legs mpp−3 → Aleena maxMP 624→621
  - **reaction:vigilant (DEC-132.B)** fires exactly once: Rowan Attack win → Injury 20 → Bargle 452→309 (after other exchanges)
- **R2 (Inflict Injury rotation):** Rowan Injury 26 → Bargle 224; Bargle Wounded Left Head mps−3 → Aleena maxMP 618
- **R3 (Armor Bypass rotation):** Rowan Armor Bypass declared → no-match fallback (DEC-030) Injury 22 → Bargle 144; Bargle Wounded Left Arms mps−3 → Aleena maxMP 615
- Bargle never reached HP≤0 within the 3-round budget → climax fork **not** skipped (D1 condition not met).
- **Climax Fork:** Beguile vs Composure → after rerolls Beguile margin 21 > Composure 0 → **ENDING B**
- No decisive exchange (Ending B path).

A4 never triggered (Aleena min observed 458 > 1).

---

## 5. Final State per Combatant

| Combatant | Final HP | Final PE | Final MP | Max HP (post-Wound) | Max MP (post-Wound) | Notes |
|---|---:|---:|---:|---:|---:|---|
| Rowan | 544 | 169 | 436 | 600 | 549 | 5× Body Wounds (bss/bsp Mag3); Attack 41, Defense 35; Perception (Advanced) present; GXP 679 |
| Aleena | 458 | 58 | 615 | 566 | 615 | 3× Mind Wounds (mpp/mps Mag3); never ≤0 |
| Bargle | 37 | — | — | 452 | 680 | Escaped (Ending B) |
| Goblin | 89 (withdrew) | drained | — | — | — | Budget-expiry primary end |
| Rattlesnake | 53 (withdrew) | — | — | — | — | Budget-expiry primary end |
| Ghoul | 262 (broke) | — | — | — | — | Fight budget expiry |

Rowan Wound records (open): 5 Body (bss/bsp Mag3 across Legs/Head/Torso).  
Aleena Wound records: 3 Mind (mpp/mps Mag3).  
pearl_found = False.  
reaction_fired = True (exactly once).

These finals (Rowan 544/600, Aleena 458/566, Bargle 37) differ from all prior runs under the same module version.

---

## 6. Coverage Matrix vs Module GM Coverage Checklist (v0.2)

| Mechanic | DEC(s) | Result | One-line Evidence |
|---|---|---|---|
| Core Test, Cost=Roll, Overflow→HP | 006/007 | PASS | Multiple Goblin/Snake PE overflows self-HP logged in TXNs |
| 100-Fumble (universal, DEC-140) | 001/012/140 | PASS | Sc1 fixed roll 00=100 teaching beat; Advanced Skill created |
| Failure XP + Skill Roll Pool cascade | 009/010 | PASS | Perception 73→28→29 +18 GXP; Attack stepped 29→41 across run |
| Advanced Skill — deterministic named | 012/140 | PASS | Perception (Advanced) T2 mss+mps Cap50 Start1 created exactly |
| Advanced Skill — probabilistic | 012 | NOT EXERCISED | No qualifying failed Double on Rowan Attack; Power Strike unused |
| Recovery + clamping | 008 | PASS | Sc1 +47 →496; Aleena/Rowan clamps observed |
| S-1 opposed contest / melee exchange | 013/105 | PASS | All combat scenes; ties rerolled ≤3 then defense holds |
| Contest-delta Inflict Injury | 096/097/104 | PASS | Sc1, Sc2, Sc4, Sc6 multiple |
| Skill-Tier shred + de-escalation | 103 | PASS | Trip T2>T1 Mag3; Venomous Bite Mag3; Bolt Mag3 |
| Zero-Step Location Index / parity | 014/100/041 | PASS | LI 71→Left Torso; LI 11→Left Legs; LI 33→Left Arms etc. |
| Skill-Tier ≥2 production gate | 041 | PASS | Sc1 Trip fires; Sc5 bash (T1) correctly does not |
| Wound record + DEC-102 target selection | 035.A/102 | PASS | Body {bsp,bss} random; Mind {mpp,mps} random |
| Live attribute recalc (HP/MP step) | 004 | PASS | HP 615→612→609→606→603→600; MP 624→621→618→615 |
| Conditions (Prone) | 079/122–125 | PASS | Sc1 multiple Prone + free stand DEC-082 |
| Reactions (single tagged exercise) | 132/132.A/132.B | PASS | Sc6 R1 reaction:vigilant fired exactly once |
| Tag+Location gating / fallback | 028/114/030 | PASS | Sc6 R3 Armor Bypass → DEC-030 fallback Injury |
| Morale/surprise non-mechanics (flagged) | — | PASS | Sc1/4/6 withdrawals narrated as source beats |
| S-11 Extended Test (full H7 order) | 071–074 | PASS | Sc3 4 intervals, Margin accumulate, clamp |
| Speed-based turn order | 095 | PASS | Every scene (Snake 173 acts first Sc2) |
| Creature signature full-Cap starts | 086/087 | PASS | All creatures |
| D1 attrition-first Ending A | D1 | PASS | Bargle >0 after R3 → fork executed; Ending B resolved |
| Exclusive one-Effect (D4) | D4 | PASS | Exactly one Effect declared per winning exchange |

---

## 7. Module-Correction Compliance Check

| Correction | Status | Evidence |
|---|---|---|
| Perception domains charged MP | PASS | Sc1 fixed beat Cost 100 MP; Treasure Search MP |
| Body-Wound HP recalcs shown | PASS | 615→612→609→606→603→600 logged |
| No "cosmetic" Wound claim | PASS | All Body Wounds stepped max_hp |
| Zero-Step per Canonical §14.1 verbatim | PASS | exchange tens/units; 00→100; LI examples match module |
| Mind Wound steps only MP | PASS | Aleena maxMP 624→621→618→615; HP unchanged by Mind Wounds |
| D1 fork skip on Bargle HP≤0 | PASS | Condition not met; fork ran |
| A4 Aleena clamp | PASS | Never required (min 458) |
| A6 fixed only Sc1; no forced Double elsewhere | PASS | Power Strike not exercised |

---

## 8. Findings (Open Items for Tiwa Only)

1. **S-1 multi-fail / zero-margin path:** When both sides produce Margin 0, the implementation rerolls both (up to 3) then awards defense. This matches the harness "ties = reroll ≤3 then defense holds" but generates extra d100s per exchange. Whether a pure single-draw-per-side reading is preferred remains open.
2. **Injury magnitude = raw attacker Margin:** No further de-escalation table beyond Skill-Tier shred was applied. Module worked examples use contest-delta directly; confirmed consistent with prior Bargle Incident execution.
3. **Recovery timing:** Applied immediately post-Cost inside each Core Test (H7 order). Interleaving of Recovery with multi-exchange rounds is an approximation flagged for review.
4. **PE/MP domain Recovery values:** floor(ER/2) and floor(MR/2) used exactly as module examples (Rowan 56/47, Aleena 50/57). Exact Canonical formula for ER/MR derivation not re-derived; values taken from module init.
5. **Skill Cap updates after attribute Wound:** Current Skill value retained under lowered Cap (unruled edge per prior findings). Flagged, not resolved.
6. **Treasure Search skill choice:** Used original Perception (higher current) rather than the new Advanced Skill at Start 1. Probabilistic; outcome pearl=not found is valid under either.
7. **Ghoul fight simplification:** Single representative Ghoul used for pack; no multi-target or positioning rules applied (none exist in module).

No findings were silently resolved. No DEC inference or promotion language is present.

---

## 9. Artifact Class and Delivery

- **Artifact class:** advisory / non-canonical execution record. No DEC assigned.
- **Attachments (artifacts/):**
  - `tiwas-yfa-v02-fresh-playtest-script-2026-09-14.py` (full simulation source)
  - `tiwas-yfa-v02-fresh-ledger-2026-09-14.txt` (160 mapped d100 entries)
  - `tiwas-yfa-v02-fresh-txns-2026-09-14.json` (158 full transaction rows)
  - `tiwas-yfa-v02-fresh-summary-2026-09-14.txt`

**End of report.**
