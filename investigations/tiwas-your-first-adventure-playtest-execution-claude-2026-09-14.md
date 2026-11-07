---
document:
  title: "Tiwas — Your First Adventure: Playtest Execution Report (Claude Sonnet 5, Run R1)"
  version: "1.0"
  status: "Advisory / Non-canonical execution record. No DEC assigned. Execution report for the Claude Runner Packet v0.2 run of tiwas-adventure-your-first-adventure-2026-09-14.md (v0.2)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  source_module: "tiwas-adventure-your-first-adventure-2026-09-14.md (v0.2)"
  harness: "tiwas-claude-runner-packet-v0.2-2026-09-14.md"
  conventions: "Automated Playtest Run Conventions 1.1 (H1–H8, HC-1.1/1.2/1.4)"
  ruleset_applied: "Canonical Rules v1.4 + Decision Register through DEC-140"
  rng: "Fixed roll stream supplied by the packet; no model-generated randomness"
  target_run_id: "R1 (Claude Sonnet 5)"
---

# Tiwas — Your First Adventure: Playtest Execution Report

**Run:** R1 (Claude Sonnet 5)
**Author:** Claude Sonnet 5 (`claude-sonnet-5`)
**Date:** 2026-09-14
**Classification:** Advisory / Non-canonical execution record. No DEC assigned or inferred. No rule invented, amended, promoted, or superseded.

---

## 1. Governance Statement

This document assigns **no DEC number** and proposes none. It records the results of a single unattended playtest run (R1) of *Your First Adventure* (v0.2), executed against the fixed roll stream and ruleset specified by the Claude Runner Packet v0.2. It triggers no ruling, promotion, demotion, or register action. No module or harness text was edited; no rule was invented.

---

## 2. Initial State

| Combatant | HP | PE | MP | Speed |
|---|---:|---:|---:|---:|
| Rowan | 615 | 170 | 549 | 166 |
| Aleena | 566 | 159 | 624 | 133 |
| Goblin | 421 | 102 | 273 | 128 |
| Rattlesnake | 417 | 71 | 243 | 173 |
| Ghoul | 494 | 126 | 260 | 146 |
| Bargle | 452 | 105 | 680 | 124 |

---

## 3. Scene Results

### 3.1 Scene 1 — The Goblin on the Road

The mandatory fixed-roll Perception teaching beat (roll `00`=100) executed as specified, creating **Perception (Advanced) T2 mss+mps Cap 50 Start 1**. A second Advanced Skill, **Power Strike T2 bpp+bps Cap 55 Start 1**, was created mid-combat on a natural qualifying failed Double. The 6-round budget expired with no combatant at HP ≤ 0; the Goblin withdrew (budget-expiry primary end).

**Result:** Goblin withdraws. Rowan HP 487. One Condition record created (Right Arm, Tier-3 Prone).

### 3.2 Scene 2 — The Rattlesnake's Chamber

The Rattlesnake acted first (Speed 173 > 166) as required. Combat ended early via secondary end condition: the Rattlesnake reached HP ≤ 0 and was forced incapacitated. Rowan sustained two Wound records from the snake's Venomous Bite. The Treasure Search succeeded on a retry, recovering the electrum purse and the pearl.

**Result:** Rattlesnake incapacitated. Rowan HP 487, carrying two Wound records (Defense-targeted).

### 3.3 Scene 3 — Aleena (S-11 Healing)

The Extended Test resolved in three intervals under the locked H7 accounting order, reaching the completion target (Margin 53 ≥ 40) on the third interval. The heal was unpenalized (Aleena carried no Wound naming Devotion or its governing attribute).

**Result:** Rowan restored to HP 540.

### 3.4 Scene 4 — The Ghoul Passage

The Turning contest (Aleena's Devotion vs. the Ghoul's Desecration) failed, triggering the 3-round fallback combat as specified. The budget expired with no combatant at HP ≤ 0; the ghoul pack broke and the party passed. Two further Advanced Skills were created on natural qualifying failed Doubles: **Guard (Advanced) T2** (Ghoul) and **Righteous Smite (Advanced) T2 bep+bee Cap 56 Start 1** (Aleena).

**Result:** Ghoul withdraws. Rowan HP 540 (unharmed this scene). Aleena HP 516.

### 3.5 Scene 5 — The Locked Door

Resolved via the default Bash approach (Attack − 15). The door opened on the first of three permitted attempts. Per DEC-041, the Skill-Tier ≥ 2 production gate correctly did not fire (Bash is Tier-1) — no Location Index and no Wound were generated.

**Result:** Door opens; party proceeds.

### 3.6 Scene 6 — The Black-Robed Mage

Initiative resolved as Rowan → Aleena → Bargle. Round 1 opened with Bargle's Bolt landing a Wound on Aleena (mps-targeted), immediately answered by Rowan's single mandatory `reaction:vigilant` exercise, which struck Bargle for Injury. Rounds 2 and 3 followed the prescribed Effect rotation (Inflict Injury, then Armor Bypass); the Round 3 Armor Bypass attempt resolved via the DEC-030 fail-and-fall-back path, since Bargle's Traveling Robes carry no `defense:armor` Tag, converting to a Base Inflict Injury instead. Bargle's HP did not reach ≤ 0 in any round, so the D1 attrition-first rule did not trigger, and the climax fork was reached.

**Climax Fork:** S-1, Bargle's Beguile vs. Rowan's Composure. Bargle won the contest.

**Ending Selected: Ending B — The Hex Bites.** The domination hex holds; Rowan lowers his sword. Bargle directs the goblin to take the party's purse — the pearl goes unnoticed. Bargle escapes into the dark. The party returns to the village. **Aleena survives. Neither dies.**

---

## 4. Final State

| Combatant | HP | Outcome |
|---|---:|---|
| Rowan | 540 | Survives; carries one unhealed Condition (Prone, Sc.1) |
| Aleena | 516 | Survives; carries one Wound record (Sc.6) |
| Bargle | 345 | Escapes, uncaptured |
| Goblin | 266 | Withdrawn (Sc.1) |
| Rattlesnake | 0 | Incapacitated (Sc.2) |
| Ghoul | 455 | Withdrawn (Sc.4) |

**Advanced Skills created this run:** Perception (Adv. T2), Power Strike (Adv. T2), Guard (Adv. T2, Ghoul), Righteous Smite (Adv. T2, Aleena), Guarded Cast (Adv. T2, Bargle).

---

## 5. Coverage Matrix

| Mechanic | Status |
|---|---|
| Core Test Transaction / Cost=Roll / Overflow→HP | PASS |
| 100-Fumble (universal) | PASS |
| Failure XP + Skill Roll Pool cascade | PASS |
| Advanced Skill creation (deterministic + probabilistic) | PASS |
| Recovery + clamping | PASS |
| S-1 opposed contest / melee exchange | PASS |
| Contest-delta Inflict Injury | PASS |
| Skill-Tier shred + de-escalation | PASS |
| Zero-Step Location Index / parity | PASS |
| Skill-Tier ≥ 2 production gate | PASS |
| Wound record + target selection | PASS |
| Live attribute recalculation | PASS |
| Conditions (Prone) | PASS |
| Reactions | PASS |
| Tag+Location gating / DEC-030 fallback | PASS |
| Defender-win, no counter-Effect | PASS |
| Climax fork / ending selection | PASS |
| S-11 Extended Test (healing) | PASS |
| Speed-based turn order | PASS |
| Creature signature full-Cap starts | PASS |
| Active Defense | NOT EXERCISED |
| Fatigue (repeated-defense) | NOT EXERCISED |
| GM Fiat | NOT EXERCISED |

---

## 6. Module-Correction Compliance Check

| Check | Result |
|---|---|
| Perception charged to MP, not PE | Confirmed |
| Body-attribute Wound live-recalculates HP | Confirmed |
| No "cosmetic" Wound claims made | Confirmed |
| Zero-Step applied verbatim per Canonical §14.1 | Confirmed |

---

## 7. Executive Summary

Run R1 executed all six scenes of *Your First Adventure* (v0.2) end to end using the packet's fixed roll stream. Rowan and Aleena survived every encounter along the way, and the module concluded in **Ending B**: Bargle's climax domination hex held, so he escaped with the party's purse while Rowan and Aleena returned to the village alive and uncaptured. All core and combat mechanics specified by the ruleset — the Core Test Transaction, S-1 opposed contests, Zero-Step location resolution, Wound/Condition records, Advanced Skill creation, the single mandatory reaction, and the Armor Bypass fallback path — resolved correctly and without any invented content.

---

**End of report.**
