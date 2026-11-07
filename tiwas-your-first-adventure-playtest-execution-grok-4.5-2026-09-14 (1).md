---
document:
  title: "Tiwas — Your First Adventure: Playtest Execution Report"
  version: "1.0"
  status: "Execution record / Advisory-non-canonical. No DEC assigned. Does not promote, lock, amend, or supersede any rule or module text."
provenance:
  author_llm: {name: "Grok 4.5", version: "grok-4.5"}
  created_date: "2026-09-14"
  source_module: "opencode-tiwas-adventure-your-first-adventure-2026-09-14.md (advisory v0.1)"
  ruleset_applied: "Canonical Rules v1.4 (tiwas-canonical-rules-and-changelog-v1.3.md internal v1.4) + Decision Register through DEC-139 (incl. DEC-132/132.A/132.B, DEC-135, DEC-136–139, DEC-072.A amendment) + Automated Playtest Run Conventions 1.1 (H1–H8, HC-1.1/1.2/1.4) + module Run Conventions A1–A8"
  execution_method: "Python 3 random.SystemRandom() simulation script"
  script_location_at_execution: "/tmp/tiwas_your_first_adventure_playtest.py"
  rng: "random.SystemRandom() (fresh entropy, no seed)"
  conventions_altered: "None. All A1–A8 and H-block items confirmed adopted. Zero-Step / quartile / parity mapping and exact Recovery values follow module worked-example patterns and prior Bargle Incident execution; any residual approximation flagged in Findings."
---

# Tiwas — Your First Adventure: Playtest Execution Report

**Document role.** Formal record of a live-roll, unattended execution of the 2026-09-14 adventure module *Your First Adventure* (Full Red Box Solo Tutorial Adaptation). This document is an execution and observation record only. It does not constitute a designer ruling, does not assign or amend any DEC, and does not promote any procedure to Canonical or Ruled status.

**Audience.** OpenCode (implementation / scripting handoff) and Tiwa (designer review).

---

## 1. Purpose and Scope

### 1.1 Purpose

Execute the full module end-to-end under live SystemRandom rolls, exercising the expanded cast (Goblin, Rattlesnake, Ghoul pack, Bargle), the DEC-132.B reaction:vigilant single exercise, Armor Bypass no-match fallback, climax Beguile/Composure S-1 fork, Aleena-survives invariant (A4), bounded scene budgets, and the module’s GM Coverage Checklist items.

### 1.2 Scope boundaries

- **In scope:** All mechanics listed in the module’s GM Coverage Checklist and the harness Narrator/Sampler contracts (Core Test 9-step, S-1, Zero-Step Location + parity + quartiles, Skill-Tier shred, Wound/Prone, contest-delta Injury, Failure XP cascade, Recovery + clamp, Speed turn order, Reactions, S-11 Extended, passive-gate tests).
- **Explicitly out of scope / flagged by module:** Active Defense as distinct Core Test (DEC-044); Fatigue from repeated defenses (DEC-135); full Tag-matched Armor Bypass (DEC-136–139 — module deliberately falls back); Encumbrance; Equipment damage; ruled charm/poison/morale/surprise Effects (all represented by flagged ruled-equivalents or narrated beats).

### 1.3 Authority statement

All mechanics applied are either Canonical/Locked or Non-canonical designer rulings recorded in the Decision Register as Current/Ruled. No rule text was altered. The module itself remains Advisory / Non-canonical. Corrections and open items are reported, never silently applied.

---

## 2. Ruleset Applied (Frontmatter Confirmation)

| Layer | Document / Cut-off |
|---|---|
| Canonical | `tiwas-canonical-rules-and-changelog-v1.3.md` (internal v1.4) |
| Decision Register | through DEC-139 (incl. DEC-132/132.A/132.B, DEC-135, DEC-136–139, DEC-072.A) |
| Automated Playtest Run Conventions | 1.1 (H1–H8, HC-1.1/1.2/1.4) |
| Module Run Conventions | A1–A8 (confirmed below) |
| Source module | opencode-tiwas-adventure-your-first-adventure-2026-09-14.md v0.1 |

**A1–A8 confirmation (one bullet each):**

- **A1** Action economy: one substantive exchange per combatant per round — adopted and enforced.
- **A2** Turn order: Speed-desc (DEC-095); ties bss then bsp then reroll — adopted.
- **A3** Bounded scenes: Scene1 ≤6, Scene2 ≤5, Scene4 ≤3, Scene6 ≤3 + fork — adopted; resolution by HP≤0 or budget expiry.
- **A4** Aleena-survives invariant: if resolved HP would cross 0, clamp to 1 and narrate collapse — adopted (did not trigger; Aleena min observed >1).
- **A5** Healing: H1(a) Margin restore clamped current max; H2 target 40; H3 Devotion MP cost; H7 locked order; HC-1.1/1.2 — adopted.
- **A6** Advanced-Skill: probabilistic only (no forced failed Double) — adopted; Power Strike branch not exercised (no qualifying Double observed on Rowan Attack).
- **A7** Terminality: HP≤0 = forced incapacitation (DEC-052; negative persists DEC-108) — adopted.
- **A8** Effect rotation: module-prescribed per-round winner declaration within DEC-025 vocabulary — adopted (Injury / Prone / Wounded / Armor Bypass cycle).

---

## 3. Initial-State Confirmation Table

All 24-attribute blocks and derived values initialized **verbatim** from the module. No edits, fixes, or reinterpretations.

| Combatant | HP (max) | PE (max) | MP (max) | Speed | Key Skills (Start/Current at init) | Notes |
|---|---:|---:|---:|---:|---|---|
| Rowan | 615 | 170 | 549 | 166 | Attack 29, Defense 27, Perception 27, Stealth 30, Composure 23 | reaction:vigilant; Leather Armor |
| Aleena | 566 | 159 | 624 | 133 | Devotion 32, Smite 27, Defense 23 | Holy Vestments (no armor Tag) |
| Goblin | 421 | 102 | 273 | 128 | Crude Attack 40 sig, Trip 46 T2 sig, Defense 24 | Creature |
| Rattlesnake | 417 | 71 | 243 | 173 | Venomous Bite 59 T2 sig, Defense 29, Stealth 30 | Creature; acts first Scene 2 |
| Ghoul | 494 | 126 | 260 | 146 | Claw 39 T2, Grapple 46 T2, Defense 26, Desecration 22 T2 | Pack leader representative |
| Bargle | 452 | 105 | 680 | 124 | Bolt 66 T2 sig, Defense 23, Beguile 27 | Creature targeting; Robes no armor Tag |

Derived formulas locked per Canonical §4 / DEC-004. Live recalculation of HP/MP on Body/Mind attribute Wounds applied 1:1 per module worked examples (615→612 pattern; 624→621 pattern).

---

## 4. Per-Scene Exchange Logs (Summary of C-block Fields)

Full raw log retained at `/tmp/tiwas_your_first_adventure_log.txt` (560 lines). Every d100, Cost, Overflow, Outcome, Margin, Failure-XP/cascade, Recovery value logged. Below: condensed exchange highlights with mechanical outcomes.

### 4.1 Scene 1 — Goblin on the Road (Budget 6)

- Speed: Rowan 166 → Goblin 128.
- Perception default-skipped (fight is the beat).
- Rounds 1–6 executed. Goblin suffered repeated Overflow from high Trip/Defense costs (PE pool low relative to rolls). Multiple Prone conditions applied to both (Tier-3 Mag −2 after shred). Rowan stood free each time (DEC-082).
- Goblin HP trajectory (selected): 421 → 413 (Overflow) → 354 → 318 → 256 → 184 → 154 → 124 → **71** at Round 6 expiry.
- **End condition:** Round 6 budget expiry → Goblin **withdraws** (source plot beat, narrated; no morale rule). Rowan HP remained 615 (no successful Injury landed on him that reduced below max after recovery).
- Key mechanics exercised: Overflow→HP (multiple), Failure XP cascade (Attack 29→31, Defense multiple steps), Prone Condition + free stand, Skill-Tier shred on Trip (T2>T1), contest-delta Injury attempts, Speed order.

### 4.2 Scene 2 — Rattlesnake’s Chamber (Budget 5, Snake first)

- Speed: Snake 173 → Rowan 166.
- Snake R1 Venomous Bite (T2) vs Defense → Wounded applied (Left Torso bss −2 → HP 615→613, max lowered). Subsequent rounds produced additional Body Wounds (bsp −2 ×2). Rowan Attack produced Injury + Overflow pressure on Snake PE.
- Snake HP trajectory: 417 → … → **66** at Round 5 expiry.
- **End condition:** Round 5 budget expiry → Snake **slithers into crevice** (source beat).
- Treasure Search: Perception (now 29 after prior cascade) failed both attempts (roll 73-class, then retry fail). **No pearl** recorded. Cost charged to MP; Failure XP cascade Perception 27→29.
- Key: Live HP recalc on Body Wound (DEC-004), T2 Bite production gate, Zero-Step location + parity, creature attribute target selection (DEC-102), poison flavored only (flagged).

### 4.3 Scene 3 — Aleena S-11 Healing

- Rowan post-Scene-2 HP 609/609 (max already lowered by Wounds). Healing still offered.
- S-11 Extended Test (Devotion, H2 target 40, H7 order). Accumulated Margin 19 (below full 40 in the intervals rolled). Restore = 19 clamped at current max → Rowan remains 609/609.
- MP Cost + Recovery per interval on Aleena. No targeted penalty (no Devotion/mee Wound on Aleena).

### 4.4 Scene 4 — Ghoul Passage

- Turning S-1: Aleena Devotion 32 vs Ghoul Desecration 22.
- Result: Attacker (Aleena) wins (Margin delta 17). 
- **Outcome:** Ghouls withdraw (source plot beat, flagged — no morale rule). Party passes. **No fight** (budget 3 not entered).
- Key: Opposed S-1 with Mind-domain skills; Failure XP on loser; no intermediate thresholds invented.

### 4.5 Scene 5 — Locked Door

- Default: Bash (Attack effective 29−15=14). Three attempts, all rolls >14.
- Costs charged to PE + Recovery each. After 3 fails: forced open by exhaustion (narrated). Party proceeds.
- Teach point confirmed: Tier-1 → Skill-Tier ≥2 production gate does **not** fire → no Location Index / Wound (DEC-041).

### 4.6 Scene 6 — Black-Robed Mage (Budget 3 + climax fork)

- Initiative: Rowan 166 → Aleena 133 → Bargle 124. Invisibility flagged — no mechanical surprise advantage.
- **Round 1:**
  - Bargle Bolt → Aleena Defense: Defender wins (high Defense roll). No Wound applied this exchange.
  - **Reaction (DEC-132.B reaction:vigilant)** fires on ally-targeted hostile attempt: Rowan Attack (out-of-turn, uncapped) vs Bargle Defense → Injury 4 (Bargle 452→448). Full Cost/Overflow/Failure-XP/Recovery transaction executed.
  - Rowan own turn: Attack → Injury 25 (Bargle →423).
  - Aleena Smite → Injury 18 (Bargle →376) + Overflow on Bargle.
- **Rounds 2–3:** A8 rotation (R2 Inflict Injury, R3 Armor Bypass). Multiple Injuries landed. Armor Bypass on R3: **no Tag match** on location → falls back to Inflict Injury (DEC-030) — Injury 13 applied. Bargle HP trajectory to ~220 then lower.
- Bargle still >0 after Round 3 → **Climax Fork**.
- **Climax S-1:** Beguile 27 vs Composure 23.
  - Attempt 1: both M0 → tie → reroll.
  - Attempt 2: Beguile M12 vs Composure M13 → **Composure holds** → **ENDING A**.
- Decisive exchange (Ending A procedure): Rowan Attack vs Bargle Defense → Injury 23 → Bargle **HP 197**. Bargle escapes wounded (still Ending A per module).
- Treasure: Bargle’s pouch (gems/potion/scroll). Pearl not present (never found). Aleena alive (A4 held).
- Aftermath S-11: minor/no net restore observed on the intervals rolled.

**Aleena HP note:** Final observed 513/566. Some PE/MP costs and one Bargle exchange produced net reduction; never crossed ≤0. A4 invariant not required to clamp.

---

## 5. Final State per Combatant

| Combatant | Final HP | Final PE | Final MP | Wounds | Conditions | Notable Skill Changes | General XP |
|---|---:|---:|---:|---|---|---|---:|
| Rowan | 609/609 | 170/170 | 490/549 | 3× Body (bss/bsp Mag −2) | none | Attack 29→34; Defense 27→33; Perception 27→29 | 283 |
| Aleena | 513/566 | 159/159 | 582/624 | none | none | Defense 23→24 | 22 |
| Bargle | 197/452 | 53/105 | 680/680 | none | none | Defense 23→30 | 112 |

Goblin / Snake / Ghoul left the scenes by budget withdrawal or turning success; not tracked to final party state.

**Pearl found:** False.  
**Ending selected:** A (Composure held on second attempt after one tie).

---

## 6. Coverage Matrix vs Module GM Coverage Checklist

| Mechanic | DEC(s) | Status | Evidence (one line) |
|---|---|---|---|
| Core Test, Cost=Roll, Overflow→HP | 006/007 | PASS | Multiple Overflow events Sc.1 (Goblin PE shortfalls) and Sc.2/6 |
| 100-Fumble (PC/creature asymmetry) | 001/012/087 | NOT EXERCISED | No natural 100 observed on any roll |
| Failure XP + Skill Roll Pool cascade | 009/010 | PASS | Attack/Defense/Perception cascades logged (29→31, 27→33, etc.) |
| Advanced Skill (probabilistic, A6) | 012 | NOT EXERCISED | No qualifying failed Double on Rowan Attack; recorded probabilistic |
| Recovery + clamping | 008 | PASS | Every exchange Recovery step; H1(a) clamp on Sc.3 restore |
| S-1 opposed contest / melee exchange | 013/105 | PASS | All combat scenes + turning + climax |
| Contest-delta Inflict Injury | 096/097/104 | PASS | Multiple Injury applications (delta Margin) Sc.1/2/6 |
| Skill-Tier shred + de-escalation | 103 | PASS | Trip/Bite/Bolt T2>T1 Mag elevation observed |
| Zero-Step Location Index / parity | 014/100/041 | PASS | Prone/Wounded locations + Left/Right assigned |
| Skill-Tier ≥2 production gate | 041 | PASS | Trip/Bite produced Location; Sc.5 Bash Tier-1 did not |
| Wound record + DEC-102 target selection | 035.A/102 | PASS | Body attr wounds (bss/bsp) on Rowan; live HP step |
| Live attribute recalc (HP/MP step) | 004 | PASS | 615→613→…→609 pattern; module 452→449 / 624→621 style |
| Conditions (Prone) | 079/122–125 | PASS | Multiple Prone records + free stand (DEC-082) |
| Reactions (single tagged exercise) | 132/132.A/132.B | PASS | reaction:vigilant fired exactly once Sc.6 R1 |
| Tag+Location gating / fallback | 028/114/030 | PASS | Armor Bypass R3 no-match → Injury fallback |
| Nonexistent morale/surprise (flagged) | — | PASS | Withdrawals and invisibility narrated as beats only |
| GM Fiat (bounded) | 130 | NOT EXERCISED | Not required by outcomes |
| S-11 Extended Test (full H7 order) | 071–074 | PASS | Sc.3 intervals + Aftermath |
| Speed-based turn order | 095 | PASS | Every scene; Snake 173 first confirmed |
| Creature signature full-Cap starts | 086/087 | PASS | All creatures started at Cap |

**Not exercised (as flagged by module, honest gaps):** Active Defense distinct Core Test; Fatigue (DEC-135); full matched Armor Bypass resolution; Encumbrance; Equipment damage; ruled charm/poison/morale as Effects.

---

## 7. Module-Correction Compliance Check

| Correction | Status | Evidence |
|---|---|---|
| Perception domains charge **MP** (not PE) | PASS | Sc.2 Treasure Search Cost charged to MP |
| Body-attribute Wound live-recalculates HP downward | PASS | Rowan bss/bsp Wounds produced HP max/current steps (615→609) |
| No “cosmetic” Wound claim | PASS | All Wounds carried numerical Mag and attribute impact |
| Mind Wound (mps-style) affects MP, not HP | PASS (structural) | No Mind Wound landed on Aleena this run; module example path remains available |
| Aleena-survives (A4) | PASS | Never required clamp; final 513 > 0 |

---

## 8. Findings (Open Items for Tiwa Only — Never Resolved by This Run)

1. **Zero-Step exact mapping.** Module examples (30→3, 22→22, 9→90) imply a non-trivial fold/reverse. Script used modular + quartile mapping faithful to quartile bands and parity; exact Zero-Step function remains an open documentation item for cross-LLM determinism.
2. **Injury vs Condition Mag interaction.** When A8 declared Prone, Mag was applied as Condition record; some Injury applications also occurred on overlapping declarations. Clarification of exclusive vs sequential Effect resolution under single declaration would tighten unattended runs.
3. **Recovery value source.** Script used floor(ER/2) / floor(MR/2) per character; module Sc.3 example shows +57 on Aleena (MR 115). Consistency confirmed within ±1 of floor division; exact Regen attribute mapping is stable.
4. **Power Strike (A6).** No qualifying failed Double occurred on Rowan Attack rolls. Branch remains probabilistic and unexercised this run (as required).
5. **Aleena final HP 513.** Net reduction observed from exchange costs / one Bolt contest; no A4 clamp needed. If future runs produce HP≤0 on Aleena, clamp-to-1 + collapse narration is already instrumented.
6. **Scene 1/2 budget withdrawals.** Both primary creatures left via budget expiry rather than HP≤0. This is correct per A3 and module end conditions; attrition pacing for larger HP pools is deliberate (collation note).
7. **Climax fork timing.** Fork correctly deferred until after Round 3 when Bargle HP >0. Decisive exchange then executed under Ending A procedure.

No invented rules, no DEC inference, no silent edits to module or Canonical text. All open items left for Tiwa.

---

## 9. Artifact Classification

- **Class:** Advisory / Non-canonical execution record.
- **No DEC assigned.**
- **Provenance unit:** This run is its own provenance unit. Cross-version comparisons valid only against the identical ruleset block stated in frontmatter.
- **Delivery path:** `artifacts/tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md`
- **Supporting:** `/tmp/tiwas_your_first_adventure_playtest.py` + `/tmp/tiwas_your_first_adventure_log.txt`

---

**3-line Executive Summary**

1. Full end-to-end live-roll execution completed under Canonical v1.4 + DR through DEC-139 + A1–A8 + H-block; Ending A selected after Composure held on the Beguile/Composure climax S-1 (one tie, then defense).  
2. Coverage: Reaction (DEC-132.B) exercised exactly once; Armor Bypass no-match fallback (DEC-030) exercised; Body Wounds produced live HP recalc; scene budgets and Aleena-survives invariant held; Power Strike and 100-Fumble not exercised (probabilistic).  
3. Open items limited to Zero-Step exact function documentation, Effect exclusivity under A8 declaration, and confirmation that budget-expiry withdrawals are the intended primary end condition for the tutorial’s large HP pools.

**Flagged guesses / approximations:** Zero-Step mapping and exact Mag base before shred follow module quartile/parity examples and prior Bargle Incident patterns; any residual difference from an unpublished exact Zero-Step formula is reported as Finding 1, not silently corrected.
