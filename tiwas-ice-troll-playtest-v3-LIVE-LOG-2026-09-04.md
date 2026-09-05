# Tiwas TTRPG — Ice Troll Combat Playtest — LIVE COMBAT LOG (v3 execution)

```yaml
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
```

**Executing this run:** Claude Sonnet 5, acting as Combat Referee / Simulation Engine per the v3 prompt. All d100 rolls generated via `random.SystemRandom()` (OS entropy) at execution time — not authored or curated. Full transaction math computed in Python per the exact Core Test Transaction (DEC-006), S-1 (DEC-013), and DEC-094–DEC-101. Raw run data: `combat_results.json`.

**Governance note (unchanged from prompt):** the DEC-012 exception (Adventurer-1's pre-built Attack2/Defence2) is a non-register-backed, prompt-level scaffold for this playtest only — see the verbatim provenance note in the Final Report.

---

## Round 1
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **15** → SUCCESS; Cost 15, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 24, domain PE): Roll **44** (Double) → FAIL; Cost 44, Overflow 0, Failure XP 20, spillover Gen.XP 20, Recovery +50 (pool→150) **[Qualifying Failed Double → Advanced Skill]** → Skill-27 (Tier 3, Cap 50, lineage: Defence2)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 52 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Impose Condition: Wounded (Location tier, demonstration)
  - Location Index (Zero-Step off attacker's natural roll, DEC-014): **51** → Tier-1 zone (DEC-100 quartile): **Arms**, laterality **left** (odd/even digit-parity, DEC-041 §3)
  - **[SCAFFOLD — see Scaffold Log]** Wound Tier 1, Value -1 applied to Adventurer-1's **Defence2** skill
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 23, domain PE): Roll **21** → SUCCESS; Cost 21, Overflow 0, Failure XP 0, Recovery +50 (pool→150)
  - Mitigation (Defender's Margin, DEC-097): **2**
  - **Final HP damage to Adventurer-1: 0** (HP now 600/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 24, domain PE): Roll **65** → FAIL; Cost 65, Overflow 0, Failure XP 41, Skill 25→26, Recovery +50 (pool→135)
- Ice Troll — **Brawling** (Eff.Skill 38, domain PE): Roll **12** → SUCCESS; Cost 12, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 2
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **6** → SUCCESS; Cost 6, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 23, domain PE): Roll **75** → FAIL; Cost 75, Overflow 0, Failure XP 52, Skill 24→26, Recovery +50 (pool→110)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 69 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **69**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 25, domain PE): Roll **15** → SUCCESS; Cost 15, Overflow 0, Failure XP 0, Recovery +50 (pool→145)
  - Mitigation (Defender's Margin, DEC-097): **10**
  - **Final HP damage to Adventurer-1: 59** (HP now 541/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 1)
- Adventurer-1 — **Attack2** (Eff.Skill 25, domain PE): Roll **24** → SUCCESS; Cost 24, Overflow 0, Failure XP 0, Recovery +50 (pool→150)
- Ice Troll — **Brawling** (Eff.Skill 38, domain PE): Roll **77** (Double) → FAIL; Cost 77, Overflow 0, Failure XP 39, Skill 38→39, Recovery +70 (pool→213) **[Qualifying Failed Double → Advanced Skill]** → Skill-7 (Tier 2, Cap 75, lineage: Brawling)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 1 → Base-tier only (≥1, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **1**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 39, domain PE): Roll **98** → FAIL; Cost 98, Overflow 0, Failure XP 59, Skill 39→40, Recovery +70 (pool→185)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 1** (HP now 704/705)

---

## Round 3
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **28** → SUCCESS; Cost 28, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 25, domain PE): Roll **4** → SUCCESS; Cost 4, Overflow 0, Failure XP 0, Recovery +50 (pool→150)
- **S-1 Outcome:** Attacker wins on Quality (Margin 39 vs 21)
- **Quality (Margin, DEC-013 §13.2):** 39 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **39**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 25, domain PE): Roll **1** → SUCCESS; Cost 1, Overflow 0, Failure XP 0, Recovery +50 (pool→150)
  - Mitigation (Defender's Margin, DEC-097): **24**
  - **Final HP damage to Adventurer-1: 15** (HP now 526/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 4)
- Adventurer-1 — **Attack2** (Eff.Skill 29, domain PE): Roll **28** → SUCCESS; Cost 28, Overflow 0, Failure XP 0, Recovery +50 (pool→88)
- Ice Troll — **Brawling** (Eff.Skill 40, domain PE): Roll **9** → SUCCESS; Cost 9, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins on Quality (Margin 31 vs 1) — DEC-101: attack fails, no counter-Effect

---

## Round 4
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **11** (Double) → SUCCESS; Cost 11, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 25, domain PE): Roll **26** → FAIL; Cost 26, Overflow 0, Failure XP 1, spillover Gen.XP 1, Recovery +50 (pool→112)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 64 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **64**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 25, domain PE): Roll **60** → FAIL; Cost 60, Overflow 0, Failure XP 35, Skill 26→27, Recovery +50 (pool→102)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 64** (HP now 462/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 30, domain PE): Roll **7** → SUCCESS; Cost 7, Overflow 0, Failure XP 0, Recovery +50 (pool→116)
- Ice Troll — **Brawling** (Eff.Skill 40, domain PE): Roll **25** → SUCCESS; Cost 25, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Attacker wins on Quality (Margin 23 vs 15)
- **Quality (Margin, DEC-013 §13.2):** 23 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **23**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 40, domain PE): Roll **72** → FAIL; Cost 72, Overflow 0, Failure XP 32, spillover Gen.XP 32, Recovery +70 (pool→218)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 23** (HP now 681/705)

---

## Round 5
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **98** → FAIL; Cost 98, Overflow 0, Failure XP 31, spillover Gen.XP 31, Recovery +70 (pool→190)
- Adventurer-1 — **Defence2** (Eff.Skill 26, domain PE): Roll **23** → SUCCESS; Cost 23, Overflow 0, Failure XP 0, Recovery +50 (pool→143)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 3)
- Adventurer-1 — **Attack2** (Eff.Skill 31, domain PE): Roll **89** → FAIL; Cost 89, Overflow 0, Failure XP 58, Skill 32→33, Recovery +50 (pool→63)
- Ice Troll — **Brawling** (Eff.Skill 41, domain PE): Roll **16** → SUCCESS; Cost 16, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 6
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **51** → SUCCESS; Cost 51, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 26, domain PE): Roll **44** (Double) → FAIL; Cost 44, Overflow 0, Failure XP 18, spillover Gen.XP 18, Recovery +50 (pool→69) **[Qualifying Failed Double → Advanced Skill]** → Skill-28 (Tier 3, Cap 50, lineage: Defence2)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 24 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **24**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 26, domain PE): Roll **95** → FAIL; Cost 95, Overflow 26 (→26 HP dmg), Failure XP 69, Skill 27→29, Recovery +50 (pool→50)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 24** (HP now 412/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 1)
- Adventurer-1 — **Attack2** (Eff.Skill 32, domain PE): Roll **66** (Double) → FAIL; Cost 66, Overflow 16 (→16 HP dmg), Failure XP 34, Skill 33→34, Recovery +50 (pool→50) **[Qualifying Failed Double → Advanced Skill]** → Skill-29 (Tier 3, Cap 50, lineage: Attack2)
- Ice Troll — **Brawling** (Eff.Skill 41, domain PE): Roll **29** → SUCCESS; Cost 29, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 7
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 2)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **55** (Double) → SUCCESS; Cost 55, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 28, domain PE): Roll **53** → FAIL; Cost 53, Overflow 0, Failure XP 25, spillover Gen.XP 25, Recovery +50 (pool→89)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 12 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **12**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 28, domain PE): Roll **70** → FAIL; Cost 70, Overflow 0, Failure XP 42, Skill 29→30, Recovery +50 (pool→69)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 12** (HP now 384/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 34, domain PE): Roll **76** → FAIL; Cost 76, Overflow 26 (→26 HP dmg), Failure XP 42, Skill 35→36, Recovery +50 (pool→50)
- Ice Troll — **Brawling** (Eff.Skill 41, domain PE): Roll **12** → SUCCESS; Cost 12, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 8
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **67** → SUCCESS; Cost 67, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 29, domain PE): Roll **6** → SUCCESS; Cost 6, Overflow 0, Failure XP 0, Recovery +50 (pool→94)
- **S-1 Outcome:** Defender wins on Quality (Margin 23 vs 8) — DEC-101: attack fails, no counter-Effect

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 5)
- Adventurer-1 — **Attack2** (Eff.Skill 39, domain PE): Roll **82** → FAIL; Cost 82, Overflow 32 (→32 HP dmg), Failure XP 43, Skill 40→41, Recovery +50 (pool→50)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **18** → SUCCESS; Cost 18, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 9
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **48** → SUCCESS; Cost 48, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 29, domain PE): Roll **42** → FAIL; Cost 42, Overflow 0, Failure XP 13, spillover Gen.XP 13, Recovery +50 (pool→58)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 19 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **19**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 29, domain PE): Roll **57** → FAIL; Cost 57, Overflow 0, Failure XP 28, spillover Gen.XP 28, Recovery +50 (pool→51)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 19** (HP now 203/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 40, domain PE): Roll **33** (Double) → SUCCESS; Cost 33, Overflow 0, Failure XP 0, Recovery +50 (pool→70)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **21** → SUCCESS; Cost 21, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins on Quality (Margin 22 vs 7) — DEC-101: attack fails, no counter-Effect

---

## Round 10
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **61** → SUCCESS; Cost 61, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 29, domain PE): Roll **74** → FAIL; Cost 74, Overflow 4 (→4 HP dmg), Failure XP 45, Skill 30→31, Recovery +50 (pool→50)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 14 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **14**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 30, domain PE): Roll **53** → FAIL; Cost 53, Overflow 3 (→3 HP dmg), Failure XP 23, spillover Gen.XP 23, Recovery +50 (pool→50)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 14** (HP now 182/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 1)
- Adventurer-1 — **Attack2** (Eff.Skill 40, domain PE): Roll **37** → SUCCESS; Cost 37, Overflow 0, Failure XP 0, Recovery +50 (pool→63)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **61** → FAIL; Cost 61, Overflow 0, Failure XP 18, spillover Gen.XP 18, Recovery +70 (pool→220)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 3 → Base-tier only (≥1, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **3**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **66** (Double) → FAIL; Cost 66, Overflow 0, Failure XP 23, spillover Gen.XP 23, Recovery +70 (pool→220) **[Qualifying Failed Double → Advanced Skill]** → Skill-11 (Tier 2, Cap 75, lineage: Brawling)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 3** (HP now 678/705)

---

## Round 11
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **65** → SUCCESS; Cost 65, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 30, domain PE): Roll **66** (Double) → FAIL; Cost 66, Overflow 3 (→3 HP dmg), Failure XP 36, Skill 31→32, Recovery +50 (pool→50) **[Qualifying Failed Double → Advanced Skill]** → Skill-30 (Tier 3, Cap 50, lineage: Defence2)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 2 → Base-tier only (≥1, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **2**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 31, domain PE): Roll **47** → FAIL; Cost 47, Overflow 0, Failure XP 16, spillover Gen.XP 16, Recovery +50 (pool→53)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 2** (HP now 177/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 40, domain PE): Roll **93** → FAIL; Cost 93, Overflow 43 (→43 HP dmg), Failure XP 53, Skill 41→42, Recovery +50 (pool→50)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **30** → SUCCESS; Cost 30, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 12
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **33** (Double) → SUCCESS; Cost 33, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 31, domain PE): Roll **2** → SUCCESS; Cost 2, Overflow 0, Failure XP 0, Recovery +50 (pool→98)
- **S-1 Outcome:** Attacker wins on Quality (Margin 42 vs 29)
- **Quality (Margin, DEC-013 §13.2):** 42 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **42**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 31, domain PE): Roll **14** → SUCCESS; Cost 14, Overflow 0, Failure XP 0, Recovery +50 (pool→134)
  - Mitigation (Defender's Margin, DEC-097): **17**
  - **Final HP damage to Adventurer-1: 25** (HP now 104/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 41, domain PE): Roll **20** → SUCCESS; Cost 20, Overflow 0, Failure XP 0, Recovery +50 (pool→150)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **43** → SUCCESS; Cost 43, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Attacker wins on Quality (Margin 21 vs 0)
- **Quality (Margin, DEC-013 §13.2):** 21 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **21**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **79** → FAIL; Cost 79, Overflow 0, Failure XP 36, spillover Gen.XP 36, Recovery +70 (pool→211)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 21** (HP now 657/705)

---

## Round 13
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **37** → SUCCESS; Cost 37, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 31, domain PE): Roll **16** → SUCCESS; Cost 16, Overflow 0, Failure XP 0, Recovery +50 (pool→150)
- **S-1 Outcome:** Attacker wins on Quality (Margin 30 vs 15)
- **Quality (Margin, DEC-013 §13.2):** 30 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **30**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 31, domain PE): Roll **76** → FAIL; Cost 76, Overflow 0, Failure XP 45, Skill 32→33, Recovery +50 (pool→124)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 30** (HP now 74/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 42, domain PE): Roll **11** (Double) → SUCCESS; Cost 11, Overflow 0, Failure XP 0, Recovery +50 (pool→120)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **2** → SUCCESS; Cost 2, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- **S-1 Outcome:** Defender wins on Quality (Margin 41 vs 31) — DEC-101: attack fails, no counter-Effect

---

## Round 14
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **22** (Double) → SUCCESS; Cost 22, Overflow 0, Failure XP 0, Recovery +70 (pool→220)
- Adventurer-1 — **Defence2** (Eff.Skill 32, domain PE): Roll **74** → FAIL; Cost 74, Overflow 0, Failure XP 42, Skill 33→34, Recovery +50 (pool→96)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 53 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **53**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 33, domain PE): Roll **76** → FAIL; Cost 76, Overflow 0, Failure XP 43, Skill 34→35, Recovery +50 (pool→70)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 53** (HP now 21/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 1)
- Adventurer-1 — **Attack2** (Eff.Skill 42, domain PE): Roll **39** → SUCCESS; Cost 39, Overflow 0, Failure XP 0, Recovery +50 (pool→81)
- Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **72** → FAIL; Cost 72, Overflow 0, Failure XP 29, spillover Gen.XP 29, Recovery +70 (pool→218)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 3 → Base-tier only (≥1, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **3**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 43, domain PE): Roll **63** → FAIL; Cost 63, Overflow 0, Failure XP 20, spillover Gen.XP 20, Recovery +70 (pool→220)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 3** (HP now 654/705)

---

## Round 15
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **94** → FAIL; Cost 94, Overflow 0, Failure XP 27, spillover Gen.XP 27, Recovery +70 (pool→196)
- Adventurer-1 — **Defence2** (Eff.Skill 34, domain PE): Roll **31** → SUCCESS; Cost 31, Overflow 0, Failure XP 0, Recovery +50 (pool→100)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 2)
- Adventurer-1 — **Attack2** (Eff.Skill 42, domain PE): Roll **13** → SUCCESS; Cost 13, Overflow 0, Failure XP 0, Recovery +50 (pool→144)
- Ice Troll — **Brawling** (Eff.Skill 44, domain PE): Roll **92** → FAIL; Cost 92, Overflow 0, Failure XP 48, Skill 44→45, Recovery +70 (pool→150)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 29 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **29**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 45, domain PE): Roll **66** (Double) → FAIL; Cost 66, Overflow 0, Failure XP 21, spillover Gen.XP 21, Recovery +70 (pool→154) **[Qualifying Failed Double → Advanced Skill]** → Skill-12 (Tier 2, Cap 75, lineage: Brawling)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 29** (HP now 625/705)

---

## Round 16
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **74** → SUCCESS; Cost 74, Overflow 0, Failure XP 0, Recovery +70 (pool→150)
- Adventurer-1 — **Defence2** (Eff.Skill 34, domain PE): Roll **51** → FAIL; Cost 51, Overflow 0, Failure XP 17, spillover Gen.XP 17, Recovery +50 (pool→143)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 1 → Base-tier only (≥1, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **1**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 34, domain PE): Roll **81** → FAIL; Cost 81, Overflow 0, Failure XP 47, Skill 35→36, Recovery +50 (pool→112)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 1** (HP now 20/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 1)
- Adventurer-1 — **Attack2** (Eff.Skill 42, domain PE): Roll **49** → FAIL; Cost 49, Overflow 0, Failure XP 7, spillover Gen.XP 7, Recovery +50 (pool→113)
- Ice Troll — **Brawling** (Eff.Skill 45, domain PE): Roll **32** → SUCCESS; Cost 32, Overflow 0, Failure XP 0, Recovery +70 (pool→188)
- **S-1 Outcome:** Defender wins (DEC-101: attack fails, no counter-Effect)

---

## Round 17
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Icy Claws vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Icy Claws** (Eff.Skill 67, domain PE): Roll **51** → SUCCESS; Cost 51, Overflow 0, Failure XP 0, Recovery +70 (pool→207)
- Adventurer-1 — **Defence2** (Eff.Skill 35, domain PE): Roll **84** → FAIL; Cost 84, Overflow 0, Failure XP 49, Skill 36→37, Recovery +50 (pool→79)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 16 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **16**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 36, domain PE): Roll **76** → FAIL; Cost 76, Overflow 0, Failure XP 40, Skill 37→38, Recovery +50 (pool→53)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Adventurer-1: 16** (HP now 4/600)

**Exchange 2: Adventurer-1 attacks Ice Troll** (Attack: Attack2 vs Defend: Brawling; S-1 contest repeats: 1)
- Adventurer-1 — **Attack2** (Eff.Skill 42, domain PE): Roll **27** → SUCCESS; Cost 27, Overflow 0, Failure XP 0, Recovery +50 (pool→76)
- Ice Troll — **Brawling** (Eff.Skill 45, domain PE): Roll **80** → FAIL; Cost 80, Overflow 0, Failure XP 35, spillover Gen.XP 35, Recovery +70 (pool→197)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 15 → Gated-tier eligible (≥10, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **15**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Ice Troll — **Brawling** (Eff.Skill 45, domain PE): Roll **65** → FAIL; Cost 65, Overflow 0, Failure XP 20, spillover Gen.XP 20, Recovery +70 (pool→202)
  - Mitigation (Defender's Margin, DEC-097): **0**
  - **Final HP damage to Ice Troll: 15** (HP now 610/705)

---

## Round 18
**Turn order (SC-04, DEC-095):** Ice Troll (Speed 175) → Adventurer-1 (Speed 150)

**Exchange 1: Ice Troll attacks Adventurer-1** (Attack: Sharktoothed Maw vs Defend: Defence2; S-1 contest repeats: 1)
- Ice Troll — **Sharktoothed Maw** (Eff.Skill 75, domain PE): Roll **66** (Double) → SUCCESS; Cost 66, Overflow 0, Failure XP 0, Recovery +70 (pool→206)
- Adventurer-1 — **Defence2** (Eff.Skill 37, domain PE): Roll **98** → FAIL; Cost 98, Overflow 22 (→22 HP dmg), Failure XP 61, Skill 38→39, Recovery +50 (pool→50)
- **S-1 Outcome:** Attacker wins
- **Quality (Margin, DEC-013 §13.2):** 9 → Base-tier only (≥1, DEC-099)
- **Effect declared:** Inflict Injury — magnitude (Winner's Margin, DEC-096) = **9**
- **Active Defense (DEC-044/046/097, voluntary — invoked):** Adventurer-1 — **Defence2** (Eff.Skill 38, domain PE): Roll **34** → SUCCESS; Cost 34, Overflow 0, Failure XP 0, Recovery +50 (pool→66)
  - Mitigation (Defender's Margin, DEC-097): **4**
  - **Final HP damage to Adventurer-1: 5** (HP now 0/600)

---

## Combat Conclusion
- **Winner:** Ice Troll
- **Total rounds:** 18
- **Adventurer-1 final HP:** 0 / 600 → **DEC-052: HP=0, forced incapacitation, no roll.**
- **Ice Troll final HP:** 610 / 705, PE 206/220
- **Frightened Condition (DEC-094):** active on Adventurer-1 (-1 all Skills) for the entire combat — the Troll was never incapacitated, so the scene-state binding never terminated.

## Scaffold Values Used (non-canonical, this run only)
- Round 1: Wound Tier magnitude — DEC-035.B ties wound tier to the 'Quality-gated Effect tier' but gives no numeric Quality→Tier conversion table; no formula exists to convert a Margin-based Quality value directly into a Wound Tier integer. SCAFFOLDED (non-canonical, this playtest only): Wound Tier = 1 (minimum), Value = -1, applied to Adventurer-1's Defence2 skill. Flagged for Tiwa's ruling — the C-03/OPEN-007-adjacent Quality-to-Wound-Tier numeric mapping is a genuine open gap, not resolved by DEC-096/097/099/100/101.

## GM-Required Moments
- None recorded — no genuinely open procedural gap forced a stop during this run.