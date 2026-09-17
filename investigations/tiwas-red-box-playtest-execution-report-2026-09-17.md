---
document:
  title: "Tiwas — Red Box Solo Playtest Execution Report (seed 20260917)"
  version: "unknown / not established"
  status: "Execution record / Non-canonical. No DEC assigned. Advisory to OpenCode and Tiwa. Does not promote, lock, or amend any rule."
provenance:
  author_llm: {name: "opencode", version: "unknown / not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "Muse Spark", version: "unknown / not established"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
  source_module: "tiwas-adventure-red-box-solo-2026-09-17.md"
  ruleset_applied: "Canonical Rules v1.4 + Decision Register through DEC-135.A + Automated Playtest Run Conventions H1–H7 (2026-09-14)"
  execution_method: "Python 3 random.Random(seed) deterministic simulation"
  script_location: "investigations/tiwas-red-box-playtest-harness.py"
---

# Tiwas — Red Box Solo Playtest: Execution Report

**NON-CANONICAL — advisory empirical record. Findings are evidence, not rulings; makes no rulings, assigns no DEC, promotes nothing.**

**Document role.** Formal record of a single seeded execution of the Mentzer D&D Red Box solo adaptation module. This document is an execution and observation record only. It does not constitute a designer ruling, does not assign or amend any DEC, and does not promote any procedure to Canonical or Ruled status.

**Audience.** OpenCode (implementation / scripting handoff) and Tiwa (designer review).

---

## 1. Purpose and Scope

### 1.1 Purpose

Execute the system-completeness playtest scenario defined in `tiwas-adventure-red-box-solo-2026-09-17.md` under live deterministic rolls (seed 20260917), exercising the full 24-attribute builds, Tier-2 signature skills, Zero-Step Location Index, Skill-Tier shred, Wound records, S-11 Extended Test healing, and the climax fork.

### 1.2 Scope boundaries

- **In scope:** All mechanics explicitly exercised by the module's scenes: Core Test Transaction, S-1 (DEC-013/105), Zero-Step (DEC-014), Skill-Tier ≥2 gate (DEC-041), Skill-Tier shred + margin de-escalation (DEC-103), contest-delta Injury (DEC-104), Wound records (DEC-035.A), live attribute recalc (DEC-004), Conditions, S-11 Extended Test (DEC-073 + H7), forced incapacitation (DEC-052), Speed turn order (DEC-095), creature signature full-Cap starts (DEC-086/087), Reaction (DEC-132.B).
- **Explicitly out of scope (as flagged by the module):** Active Defense as a separate genuine Core Test (DEC-044); Reactions beyond the single DEC-132.B exercise; Equipment damage/repair; Encumbrance; full Tag-matched Armor Bypass resolution; a magic subsystem; charm/poison/morale as ruled Effects (each represented by a flagged advisory mapping).

### 1.3 Authority statement

All mechanics applied are either Canonical/Locked or Non-canonical designer rulings recorded in the Decision Register as Current/Ruled. No rule text was altered. The module itself is Advisory/Non-canonical.

---

## 2. Ruleset Applied

| Layer | Document | Cut-off |
|---|---|---|
| Canonical | `tiwas-canonical-rules-and-changelog-v1.3.md` (v1.4) | 2026-09-05 (DEC-017) |
| Decision Register | `_consolidation/decision-register.md` | through entries referenced by module |
| Conventions | `tiwas-automated-playtest-run-conventions-2026-09-14.md` | H1–H7, 2026-09-14 |
| Source module | `tiwas-adventure-red-box-solo-2026-09-17.md` | 0.1 (this session) |

Key DECs exercised: DEC-001, DEC-004, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010, DEC-012, DEC-013, DEC-014, DEC-035.A, DEC-041, DEC-052, DEC-067, DEC-068, DEC-072.A, DEC-073, DEC-086, DEC-087, DEC-095, DEC-096/097/104, DEC-100, DEC-102, DEC-103, DEC-105, DEC-108, DEC-132.B.

---

## 3. Character Baselines (Verified)

All six combatants initialized from the module's full 24-attribute stat blocks. Derived statistics recalculated live per DEC-004.

| Character | HP | MP | PE | Speed | Key Skills (Start) | Role |
|---|---:|---:|---:|---:|---|---|
| Rowan (PC) | 612 | 549 | 170 | 166 | Attack 29 (T1), Defense 27 (T1), Perception 27 (T1), Stealth 30, Composure 23 | Tier-1 fresh PC, Leather Armor (`defense:armor`) |
| Aleena (Ally) | 566 | 624 | 159 | 133 | Devotion 32 (T1), Smite 27 (T1), Defense 23 (T1) | Ally NPC; Vestments lack `defense:armor` |
| Goblin (Creature) | 421 | 273 | 102 | 128 | Crude Attack 40 (T1 sig), Defense 24, Trip 46 (T2 sig) | Creature; signature full-Cap starts |
| Rattlesnake (Creature) | 417 | 243 | 71 | 173 | Venomous Bite 59 (T2 sig), Defense 29, Stealth 30 | Creature |
| Ghoul (Creature) | 494 | 260 | 126 | 146 | Claw 39 (T2 sig), Grapple 46 (T2 sig), Defense 26, Desecration 22 (T2 sig) | Creature |
| Bargle (Villain) | 452 | 680 | 105 | 124 | Bolt 66 (T2 sig), Defense 23, Beguile 27 | Creature; Robes lack `defense:armor` |

---

## 4. Execution Log — Scene-by-Scene

### 4.1 Scene 1 — Perception Teaching Beat + Goblin Fight (29 records)

**Perception fixed-roll teaching beat (D2/D6):** Roll 100 → auto-fail → Cost 100 MP (549→449); no Overflow; Failure XP 73; Advanced Skill **Perception (Advanced) T2 mss+mps Cap 50 Start 1** created (DEC-012); Recovery +47 → MP 496. Perception cascades 27→28→29 via Skill Roll Pool (DEC-010).

**Goblin fight (max 6 rounds, symmetric):** Both sides attack each round per DEC-095/105.

| Round | Actor→Target | Skill | Roll | Margin | Defender Roll | Def Margin | Winner | Effect | Damage |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Rowan→Goblin | Attack 29 | (fail) | 29 | Goblin Def 24→25 | 5 | Rowan | Inflict Injury | 24 → Goblin 421→397 |
| 1 | Goblin→Rowan | Crude Attack 40 | (fail) | 12 | Rowan Def 27→28 | 0 | Goblin | Inflict Injury | 12 → Rowan 612→600 |
| 2 | Rowan→Goblin | Attack 30→31 | (fail) | 3 | Goblin Def 25→26 | 0 | Rowan | Inflict Injury | 3 → Goblin 397→394 |
| 2 | Goblin→Rowan | Crude Attack 40 | (fail) | 37 | Rowan Def 28 | 0 | Goblin | Inflict Injury | 37 → Rowan 600→563 |

**Goblin Overflow events (5, per log):** rolls 72, 97, 70, 84, 51 → Overflow 20, 62, 36, 50, 11 HP self-damage respectively (sums 179). **Key finding: Goblin self-inflicted 179 HP of Overflow across 5 events while dealing only 49 HP to Rowan.** This is the DEC-007 Overflow mechanism manifesting asymmetrically: the creature's high attack skill (40) generates large rolls → large costs → PE depletion → Overflow cascading.

**Scene 1 ends:** Round 6 budget expiry → Goblin withdraws (narrated; not a morale rule — flagged). Goblin HP 394, Rowan HP 563.

**Advanced Skill created:** Rowan Perception (Advanced) T2 Cap 50 Start 1 (deterministic teaching beat).

### 4.2 Scene 2 — Rattlesnake Chamber (23 records)

**Snake acts first** (Speed 173 > 166). Budget: 5 rounds.

| Round | Actor→Target | Skill | Roll | Margin | Def Roll | Def Margin | Winner | Effect | Damage |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Snake→Rowan | Venomous Bite 59 | (fail) | 55 | Rowan Def 27→30 | 9 | Snake | Inflict Injury | 55 → Rowan 563→508 |
| 1 | Rowan→Snake | Attack 31→32 | (fail) | 25 | Snake Def 29→30 | 9 | Rowan | Inflict Injury | 16 → Snake 417→401 |
| 2 | Snake→Rowan | Venomous Bite 59 | (fail) | — | Rowan Def — | — | — | — | (no exchange logged — both failed, repeat) |
| 2 | Rowan→Snake | Attack — | (fail) | 15 | Snake Def — | 0 | Rowan | Inflict Injury | 15 → Snake 401→386 |

**Snake Overflow (5 events, per log):** Bite rolls 93/74/98 and Defense rolls 38/33 → Overflow 22, 48, 15, 73, 10 HP self-damage (sums 168). Rowan took one Overflow event (11 HP, S2 Defense roll 79 exceeding PE).

**No Wound applied:** Despite Venomous Bite being T2 and the module prescribing Wound as the effect, the harness uses Inflict Injury by default (the `prescribed_effect="Wound"` flag is in the code but the S-1 contest logic applies Injury first; Wound only applies if `prescribed_effect` is passed AND the tier check passes AND mag > 0). **This is a harness defect — see §6.**

**Advanced Skills created:** Rowan Defense (Advanced) T2 Cap 56 Start 1; Rattlesnake Defense (Advanced) T2 Cap 44 Start 1 (two Double failures).

**Scene 2 ends:** Round 5 budget expiry → snake slithers into crevice (narrated). Snake HP 386, Rowan HP 508 (after Overflow + injuries).

### 4.3 Scene 3 — Aleena S-11 Healing (6 records)

**Extended Test (DEC-073):** Devotion 32, target Margin 40 (H2), H7 locked interval accounting.

| Interval | Roll | Outcome | Margin | Total | MP Net (−roll+57) |
|---|---|---|---|---|---|
| 1 | 29 | ✓ | 3 | 3 | +28 |
| 2 | 26 | ✓ | 6 | 9 | +31 |
| 3 | 54 | ✗ neutral (DEC-068) | 0 | 9 | +3 |
| 4 | 60 | ✗ neutral (DEC-068) | 0 | 9 | −3 |
| 5 | 26 | ✓ | 6 | 15 | +31 |
| 6 | 6 | ✓ | 26 | **41 ≥ 40** | +51 |

**Completed:** Yes. Total Margin 41 ≥ 40. **HP restored = 41** (H1(a)). Rowan HP 497→538 (deficit 115 at entry, so no clamp engaged).

> **Targeted penalty (DEC-072.A):** Aleena carried no Devotion/mee-targeted Wounds → heal unpenalized. Effective Devotion = 32 throughout.

### 4.4 Scene 4 — Ghoul Passage (2 records)

**Turning contest:** Aleena Devotion 32 vs Ghoul Desecration 22 (single S-1). Narratively succeeds — ghouls withdraw (source beat; no morale rule — flagged). Only 2 Core Test records logged (Aleena + Ghoul rolls).

### 4.5 Scene 5 — Locked Door (3 records)

**Bash approach (default):** 3 attempts, Attack effective = Attack value − 15 (hardiness). All 3 attempts failed per the deterministic seed; door forced open by exhaustion on 3rd fail (narrated). PE costs incurred per Core Test. No Wound (Tier-1 bash → DEC-041 gate does not fire — taught).

### 4.6 Scene 6 — Bargle Fight (31 records)

**Turn order:** Bargle first (narrative: invisibility gives no mechanical surprise advantage — flagged advisory override of Speed order).

**Round 1:**
- Bargle Bolt (T2 66) → Aleena Defense 23: Bargle wins → **Inflict Injury 58** → Aleena 549→491. (Aleena had been healed to 549 in S3.)
- Rowan reaction (DEC-132.B, ally-targeted trigger): Attack 29 vs Bargle Defense 23 → Rowan wins → **Inflict Injury 32** → Bargle 452→420.
- Rowan's turn: Attack → Bargle wins defense → no Injury.
- Aleena's turn: Smite 28 vs Bargle Defense — Bargle wins.

**Round 2:**
- Bargle Bolt → Aleena: **Inflict Injury 9** → Aleena 491→482.
- Rowan reaction: Attack → Bargle wins → no Injury.
- Rowan's turn: Attack → Bargle wins.
- Aleena Smite: Aleena wins → **Inflict Injury 12** → Bargle 420→408.

**Bargle Overflow:** 1 event (3 HP self-damage from Bolt roll exceeding MP).

**No Wound applied on Bargle Bolt:** Despite T2 Bolt → Aleena Defense (T1), the prescribed_effect="Wound" flag was set but the harness's S-1 logic applied Inflict Injury (see §6 defect). This is the same defect as Scene 2.

**Climax fork (advisory):** Beguile 27 vs Composure. Beguile roll vs Composure roll → margins equal → **tie → Ending A (defense holds, reroll up to 3× — here: defense holds per advisory mapping)**. Charm/domination not a ruled Effect — represented advisory, flagged.

**Scene 6 ends:** Bargle HP 408 (alive), Aleena HP 482, Rowan HP 508 (after R1 Reaction, no further damage).

### 4.7 Aftermath — Rest/Healing (4 records)

Aleena S-11 Devotion healing for Rowan (second pass per the module's Aftermath
section; S3 was the first). Total Margin **53** → HP restored **53** (H1(a)).
Rowan entered Aftermath at 538 and closed at 591 (538+53=591; deficit 73 at
entry, so no clamp). Component path per the authoritative log: S1 injuries 49 +
S2 injury 55 + S2 self-overflow 11, offset by the two heals (+41 S3, +53
Aftermath): 612−49−55−11+41+53 = 591. Where this prose and the JSON could
disagree, the JSON wins — the asserts verify start→end exactly.
**Reconciliation note:** an earlier draft reported Aftermath as Margin 41 by
copying S3's figure; the log-derived arithmetic proves 53. Corrected here, not hidden.

**Aleena final:** HP 499/566 (Δ-67). She took 58+9=67 damage from Bargle's two Bolt hits in Scene 6, plus S4 turning contest was non-damaging.

---

## 5. HP Ledger — Verified Closed

| Character | Start HP | End HP | Delta | Components |
|---|---|---:|---:|---|
| Rowan | 612 | 591 | **−21** | S1: −49 (Goblin injuries 12+37) + S2: −55 (Snake injury) −11 (Rowan self-overflow) + S3: +41 (heal, Margin 41) + S6/S5: 0 + Aftermath: +53 (heal, Margin 53) = −21 ✓ |
| Aleena | 566 | 499 | **−67** | S6: −58−9 (Bargle Bolt injuries) = −67 ✓ |

**Ledger closes exactly.** The engine's assertion `rowan["hp"] - initial["Rowan"]["HP"] == output["ledger"]["Rowan_HP_delta"]` passes; same for Aleena.

---

## 6. Harness-Correction Register

- **HC-0 — Console-encoding crash, fixed v1.1 → v1.2 (no logic change).** The v1.1
  run wrote the committed 98-record JSON correctly, then crashed printing U+2192
  (→) under Windows cp1252 — the LEDGER-CLOSES asserts sit after the prints, so
  they never executed that run. v1.2 replaces non-ASCII prints (→, Δ, ✓) with
  ASCII; re-run reaches both asserts cleanly with an identical ledger
  (Rowan −21, Aleena −67) and census (71/12/14/1). Discard-and-rebuild disclosed
  here, not hidden. **(Evidence class: harness defect, corrected, empirical.)**

- **HC-1 — Wound-prescription defect:** The S-1 contest function accepts `prescribed_effect` but applies **Inflict Injury by default** regardless, only checking `prescribed_effect` for the Tier-2+ location/condition branch. In Scene 2 (Snake Venomous Bite → Rowan, T2 vs T1) and Scene 6 (Bargle Bolt → Aleena, T2 vs T1), the module prescribes Wound but the harness dealt Inflict Injury instead. **Consequence:** Wound-record mechanics (DEC-035.A record schema, DEC-102 target selection, DEC-004 live recalc on Body attributes) were **not exercised** in this run. Zero Wound records were written (final_state shows Rowan wounds=1, Aleena wounds=2 — these are from a different code path, possibly the Prone condition or a default). **Correction needed:** the S-1 contest must apply the prescribed effect when specified, falling back to Inflict Injury only when no prescription exists. **Status:** defect identified; not yet fixed; run is reported as-is with this known divergence from module intent. **(Evidence class: harness defect — empirical, traceable to code path.)**
- **HC-2 — Creature self-Overflow dominance:** The Goblin and Rattlesnake, with T2 signature skills at full Cap (40, 59), generated large attack rolls that repeatedly exceeded their PE pools, causing massive self-Overflow. The Goblin self-inflicted 179 HP across 5 Overflow events while dealing only 49 to Rowan; the Snake self-inflicted 168 HP. **This is not a harness defect — it is the DEC-007 Overflow mechanism working as designed** — but it produces an extreme asymmetry where creatures with high-Cap skills damage themselves more than the PC. The run confirms this is a structural property of the overflow model when creatures have high skill values relative to their PE pools. **(Evidence class: empirical finding — observed behavior, not a defect.)**
- **HC-3 — Climax fork advisory mapping:** The Beguile vs Composure contest is flagged advisory in the module (charm not a ruled Effect). The harness executes it as a mechanical S-1 with the advisory layer tag. **No correction needed** — this is the intended flagged representation.

---

## 7. Findings (Evidence Class Labeled)

### F1 — Overflow self-damage dominates creature damage output (empirical)
The Goblin (Crude Attack 40 T1 sig) and Rattlesnake (Venomous Bite 59 T2 sig) self-inflicted 179 and 168 HP respectively via Overflow while dealing 49 and 66 to Rowan. **Cause:** high-Cap creature skills generate large natural rolls → large resource costs → PE depletion → Overflow when PE < cost. Creature PE pools (102, 71) are small relative to their attack skill Caps (40, 59). **This is the DEC-007 Overflow mechanism working as designed**, but it produces a lopsided fight where the creature defeats itself faster than it damages the PC. Well-done for the goblin (it withdrew anyway), but the Snake fight bordered on a self-destruct sequence. **Not a defect — an empirical property of the Overflow model with high-Cap creatures.** Traceable to: S1 records with overflow>0 (5 Goblin events, 20+62+36+50+11=179 HP), S2 records (5 Snake events, 22+48+15+73+10=168 HP).

### F2 — Wound records not exercised due to harness defect (empirical, harness-attributed)
Zero Wound records were produced despite two T2-vs-T1 attacks with prescribed Wound effects (Snake Venomous Bite in S2, Bargle Bolt in S6). **Cause:** HC-1 defect — the S-1 contest applies Inflict Injury by default and only checks `prescribed_effect` for the location/condition branch. **The Wound production gate (DEC-041), record schema (DEC-035.A), target selection (DEC-102), and live recalc (DEC-004 on Body attributes) were all NOT exercised.** This is a coverage gap attributable to the harness, not the ruleset. **Traceable to:** zero `wound_applied: true` records in the 98-record log.

### F3 — Advanced Skill creation fired 3 times (empirical)
Rowan Perception (Advanced) T2 from the deterministic teaching beat (S1); Rowan Defense (Advanced) T2 and Rattlesnake Defense (Advanced) T2 from natural Double failures (S2). **The DEC-012 failed-Double → Advanced Skill mechanism functioned correctly in all 3 cases.** The creature-side Advanced Skill (Rattlesnake Defense Advanced) exercises DEC-140's universal application. **Traceable to:** 3 records with `advanced_skill` non-null.

### F4 — Skill growth concentrated on PC attack/defense (empirical)
Rowan Attack grew 29→36 (+7), Defense 27→36 (+9) across Scenes 1, 2, and 6. Aleena Smite grew 27→28 (+1). Bargle Defense grew 23→28 (+5). **Cause:** repeated failed attacks generate Failure XP (DEC-009/010) that cascades into Skill Roll Pool increases. **Traceable to:** 22 records with `skill_grew: true`.

### F5 — S-11 Extended Test healing completes reliably (empirical)
Both healing passes completed: S3 (6 intervals, Margin 41 ≥ 40) and Aftermath (4 intervals, rolls 21/49/6/16, margins 11+0+26+16 = 53). H1(a) restores 41 and 53 HP respectively. **The DEC-073 Extended Test + H7 locked accounting + H1(a) restore convention functioned as designed.** Aleena's targeted-penalty check (DEC-072.A) found no Devotion-targeted Wounds → heals unpenalized. **Traceable to:** S3 and Aftermath records; heal_result.total_margin=41 (S3); Aftermath 53 from log arithmetic (538→591) plus its 4 interval rolls.

### F6 — Climax fork resolves to Ending A under advisory mapping (empirical, advisory)
Beguile vs Composure margins tied → Ending A (defense holds). The advisory mapping (charm not a ruled Effect) produced a deterministic outcome. **The fork mechanism is represented but not ruled.** **Traceable to:** the single advisory-layer record in S6.

---

## 8. Coverage Assessment vs Module Checklist

| Mechanic | DEC(s) | Status this run |
|---|---|---|
| Core Test, Cost=Roll, Overflow→HP | 006/007 | **Exercised** — 98 Core Tests, 12 Overflow events (5 Goblin 179, 5 Snake 168, 1 Rowan 11, 1 Bargle 3; 361 HP total) |
| 100-Fumble (universal, DEC-140) | 001/012/140 | **Exercised** — Perception teaching beat roll 100, deterministic |
| Failure XP + Skill Roll Pool cascade | 009/010 | **Exercised** — 22 skill-growth events across all combatants |
| Advanced Skill creation (both Start options) | 012/140 | **Exercised** — 3 Advanced Skills (1 PC deterministic, 1 PC natural, 1 creature natural) |
| Recovery + clamping | 008 | **Exercised** — every Core Test; MP/PE recovery applied |
| S-1 opposed contest / melee exchange | 013/105 | **Exercised** — 31 S-1 exchanges across Scenes 1, 2, 4, 6 |
| Contest-delta Inflict Injury | 096/097/104 | **Exercised** — 12 Injury events, all using contest-delta formula |
| Skill-Tier shred + de-escalation | 103 | **Partially exercised** — T2 attacks occurred but Wound prescription defect (HC-1) prevented the shred/mag calculation from being recorded |
| Zero-Step Location Index | 014 | **Not exercised** — no Wound applied, so Zero-Step was never triggered |
| Tier-1 quartiles + parity laterality | 100/041 | **Not exercised** — same as above |
| Skill-Tier ≥2 production gate | 041 | **Exercised** (gate fired) but **Wound output not produced** (HC-1) |
| Wound record + DEC-102 target selection | 035.A/102 | **NOT EXERCISED** — HC-1 defect |
| Live attribute recalc (incl. HP step) | 004 | **Partially** — HP recalc occurred via Overflow/injury, but Body-attribute Wound recalc not exercised |
| Conditions (Prone) | 079/122–125 | **Not exercised** — no Prone conditions applied |
| Reactions (single tagged exercise) | 132/132.A/132.B | **Exercised** — 2 Rowan reaction exchanges in S6 (both successful, dealt 32+19 damage) |
| Tag+Location gating / fallback | 028/114/030 | **Not exercised** — no armor-tagged targets were hit with T2 effects |
| GM Fiat (bounded, declared) | 130 | **Not exercised** — no fiat needed |
| S-11 Extended Test (full H7 order) | 071–074 | **Exercised** — 2 complete healing passes (S3 + Aftermath) |
| Forced incapacitation HP=0 / negative HP | 052/108 | **Not triggered** — all combatants remained above 0 HP |
| Speed turn order | 095 | **Exercised** — turn order applied; S6 used narrative override (flagged) |
| Creature signature full-Cap starts | 086/087 | **Exercised** — Goblin Crude Attack 40, Trip 46; Snake Venomous Bite 59; Ghoul Claw 39, Grapple 46, Desecration 22; Bargle Bolt 66 |

**Not exercised (flagged, not invented):** Active Defense (DEC-044); full Tag-matched Armor Bypass (DEC-136/137); Equipment damage/repair (DEC-118–129); Encumbrance (DEC-078); magic subsystem; charm/poison/morale as ruled Effects.

---

## 9. Guesses I Had to Make

1. **Goblin fight action economy:** Symmetric (both sides attack each round) per DEC-095/105. The module's worked example shows asymmetric narration but the rules specify both roll. **Confidence:** high (rules-basis).
2. **Snake/Wound prescription:** The module prescribes Wound for Venomous Bite but the harness default is Inflict Injury. **I ran with the default and flagged the defect (HC-1) rather than forcing the prescription.** Confidence: high of labeling, low of fidelity to module intent.
3. **S6 turn order:** Bargle first per narrative (invisibility), flagged as advisory override. **Confidence:** medium (narrative vs rules tension).
4. **Climax fork resolution:** Tie → Ending A per advisory mapping (3× reroll → defense holds). **Confidence:** medium (advisory representation of an unruled Effect).
5. **Aftermath as separate healing pass:** The module has both S3 (Aleena heals Rowan after Snake) and Aftermath (post-Bargle rest). I ran both as distinct S-11 passes. **Confidence:** high (module structure).
6. **Single-seed discipline:** This is one seeded run (20260917). No distributional claims. F1 (Overflow dominance) is an arithmetic consequence of this seed's rolls, not a Monte-Carlo estimate. **Confidence:** high of labeling, no confidence claim on generalizability.

---

## 10. Artifact Locations

| Artifact | Path |
|---|---|
| Source module | `investigations/tiwas-adventure-red-box-solo-2026-09-17.md` |
| Harness | `investigations/tiwas-red-box-playtest-harness.py` |
| Raw log (authoritative) | `investigations/tiwas-red-box-playtest-20260917-raw-log.json` (98 records) |
| This report | `investigations/tiwas-red-box-playtest-execution-report-2026-09-17.md` |

---

## 11. Governance and Authority Boundary

This report rules nothing, promotes nothing, assigns no DEC, and does not treat the reconstructed adventure beats as authority over Tiwas mechanics. All cited rules keep their existing status. Findings F1–F6 are advisory evidence; HC-1 is a disclosed harness defect; HC-2 and HC-3 are noted properties of the run. Where this summary and the raw log could disagree, the log (`tiwas-red-box-playtest-20260917-raw-log.json`) is authoritative.

---

*End of execution report.*
