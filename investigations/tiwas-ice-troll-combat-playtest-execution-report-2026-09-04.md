---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest Execution Report"
  version: "1.0"
  status: "Advisory working document (not canonical). Empirical playtest record for OpenCode review. Makes no rulings, assigns no DEC numbers, promotes nothing."
provenance:
  author_llm: {name: "Grok", version: "4.5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
source_prompt:
  file: "claude-playtest-prompt-version2.md"
  version: "2.1"
  executed_date: "2026-09-04"
---

# Tiwas TTRPG — Ice Troll Combat Playtest Execution Report

**Author:** Grok 4.5  
**Date:** 2026-09-04  
**Status:** Advisory empirical record only. Non-canonical. No mechanics ruled, promoted, or locked by this document.

---

## 1. Purpose and Scope

This document records the complete execution of the Ice Troll Combat Playtest as specified in `claude-playtest-prompt-version2.md` (v2.1).  

The executing LLM acted strictly as **Combat Referee / Simulation Engine**. No creative GM rulings were made. No rules were invented to close gaps beyond the pre-authorized scaffold mechanism defined in the prompt. All outcomes were resolved mechanically against the Ruled/Locked corpus available in the playtest environment (`Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` and supplied inline blocks).

Three primary data products were required and are delivered:

1. Which Ruled systems functioned end-to-end in actual play.
2. Combat duration (round count and approximate real-time equivalent).
3. Exact locations where human GM judgment became necessary (or would have become necessary).

This is the first live combat test of the DEC-077.A Ice Troll conversion block under the two-track resolution model.

---

## 2. Governance and Provenance Notes

### 2.1 DEC-012 Exception (Prompt-Level Scaffold Only)

The two pre-built Tier-2 skills on Adventurer-1 (Attack1, Defence1) were granted under a **prompt-level scaffold** (Tiwa’s authorization, 2026-09-04) for this playtest only.  

They are **NOT backed by any PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and explicitly preserves DEC-012’s failed-Double origin for player-character skill advancement.  

This exception is therefore:

- non-register-backed,
- creates no new precedent,
- grants the PC no canonical authority from these skills,
- must not be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

The same statement is repeated in the Conclusion for cold-reader clarity.

### 2.2 Scaffold and GM-Stop Discipline

Every numeric value not supplied by a Ruled formula was invented only under the prompt’s explicit scaffold-value authorization, flagged at the moment of invention, collated below, and never assigned a DEC number or claimed as Ruled/Locked.

Genuine subjective or narrative judgment calls with no numeric scaffold possible produced mandatory GM-stops. In this execution none were triggered.

### 2.3 Opponent Block

The Ice Troll stat block was used **verbatim** from the inline reproduction in the prompt (itself taken from the DEC-077.A / DEC-085 provisional conversion). No re-derivation from GURPS source material occurred. Traits marked “Flagged, not converted” (Regeneration, Regrowth, freezing DR 2) were treated as inactive per the prompt’s playtest disposition.

---

## 3. Character and Opponent Summary

### 3.1 Adventurer-1 (PC)

| Parameter | Value |
|-----------|-------|
| Attributes | All 24 fixed at 50 |
| Derived (DEC-004) | HP 600 · MP 600 · Physical Energy 150 · Speed 150 · Energy Regen 100 · MP Regen 100 · Movement Speed 6 |
| Tier-1 Skills | All 12 Body + 12 Mind present; Cap 50; Starting Value 25 |
| Attack1 (Tier-2) | bpp + bps; Cap 50; Starting Value 25; Physical Energy domain |
| Defence1 (Tier-2) | bsp + bss; Cap 50; Starting Value 25; Physical Energy domain |

Both Tier-2 skills advanced during play via Failure XP / Skill Roll Pool (DEC-009 / DEC-010). Exact intermediate values were tracked but are not reproduced in full here.

### 3.2 Ice Troll (Opponent)

| Parameter | Value |
|-----------|-------|
| Attributes | As supplied inline (bpp 75 … mex 15) |
| Derived | HP 705 · MP 420 · Physical Energy 220 · Speed 175 · Energy Regen 140 · MP Regen 75 · Movement Speed 7 |
| Signature Skills | Icy Claws (Tier-2, Cap 67, Current 67); Sharktoothed Maw (Tier-2, Cap 75, Current 75) |
| Other Skills | Brawling 37, Camouflage 30, Stealth 30, Tracking 30 |
| Traits disposition | Regeneration / Regrowth / freezing DR treated inactive |

---

## 4. Pre-Authorized Scaffolds Invented During Execution

| ID | Gap | Scaffold Value | Authority Basis |
|----|-----|----------------|-----------------|
| SC-01 | Inflict Injury magnitude (Base-tier) | 25 HP flat | Prompt scaffold-value authorization (C-01) |
| SC-02 | Active Defense mitigation amount | Success = −20 HP (or full cancel if remaining ≤ 20); Failure = 0 | Prompt scaffold-value authorization (C-02) |
| SC-03 | Quality mode for force contests | Blackjack (Quality = natural Roll on success) | DEC-013 guidance + prompt authorization |
| SC-04 | Initiative / turn structure | Higher Speed acts first; one attack action per character per round; melee range assumed permanent | No Ruled initiative procedure located; scaffold required to begin combat |
| SC-05 | Frightened magnitude (Condition) | −10 to all Skills while source perceivable | Ready but never selected |
| SC-06 | Wound Condition magnitude | −5 to physical Skills (single numeric state) | Ready but never selected |

No Location-referencing Effects were selected, so anatomical mapping ranges (DEC-041) and Tier-2 subdivision procedure (DEC-042) were never exercised.

---

## 5. Combat Execution Summary

### 5.1 Resolution Model Applied

- Attacks resolved as S-1 Opposed Contests (attacker Attack skill vs defender Defence / Brawling).
- Track A (attacker Cost / Overflow) and Track B (won S-1 Effect) applied sequentially (DEC-034).
- Base-tier Inflict Injury was the only Effect selected.
- Active Defense was elected as voluntary post-hoc mitigation Core Test (DEC-044–DEC-050).
- All Core Test 9-step transactions (DEC-006) executed in full order.
- Recovery (floor(Regen / 2)) applied after every test and clamped at pool maximum (DEC-008).
- 100-Fumble and Double rules observed; no qualifying failed Doubles occurred, so no Advanced Skills were created.

### 5.2 Round Count and Outcome

- **Total rounds:** 22
- **Terminal state:** Adventurer-1 HP = 0 → DEC-052 forced incapacitation. Ice Troll remaining HP 412.
- **Real-time equivalent:** approximately 45–60 minutes of full-granularity referee work.

Net damage per exchange was typically 5 HP after successful Active Defense mitigation. Unmitigated 25 HP hits and the first Overflow events appeared only in the final rounds after sustained PE pressure.

### 5.3 Systems Confirmed Working End-to-End

- DEC-001 d100 / 100-Fumble / Doubles
- DEC-002 floor rounding
- DEC-004 derived statistics (live)
- DEC-005 skill Cap / Starting Value
- DEC-006 Core Test Transaction (all 9 steps)
- DEC-007 / 007.A Cost = natural roll; Overflow → HP; Overflow immutability
- DEC-008 Recovery after every test
- DEC-009 / 010 Failure XP → Skill Roll Pool → Cap-limited advancement
- DEC-013 S-1 Opposed Contest (outcome matrix, Fail/Fail repeat, Quality comparison)
- DEC-031 Quality gating of Effect tier (Base-tier always available at Quality ≥ 1)
- DEC-034 Track A / Track B sequential application
- DEC-027 / 048 Effect auto-apply + post-hoc Active Defense mitigation
- DEC-052 HP = 0 forced incapacitation
- Skill-Tier ≥ 2 gate for location-referencing Effects (respected by never selecting such Effects from Tier-1)

### 5.4 Systems That Remained Idle or Gapped

- S-2 / S-4 Location Index generation and anatomical mapping (never required)
- S-4 Wound Condition application (never selected)
- S-5 Armor (neither side possessed Armor Tags)
- Passive / aura Frightened trigger (C-04) — deliberately not invoked; would have produced mandatory GM-stop
- Regeneration / Regrowth activation (inactive by disposition)
- Advanced Skill creation via failed Double (no qualifying Doubles occurred)

---

## 6. GM-Required Moments

**None occurred.**

All numeric gaps were closed by the pre-authorized scaffold mechanism. The single qualitative subsystem absence identified in the prompt (C-04: Frightened trigger outside a won S-1 Effect) was never exercised.

---

## 7. Candidate Follow-Up Items for OpenCode / Designer Review

These are empirical observations only. No recommendations are promoted to rulings.

| ID | Observation | Source |
|----|-------------|--------|
| C-01 | Inflict Injury magnitude has no Ruled formula | Scaffold SC-01 used throughout |
| C-02 | Active Defense mitigation amount has no Ruled formula | Scaffold SC-02 used throughout |
| C-03 | Broader S-3 Effect magnitude vocabulary incomplete | Scaffold values required |
| C-04 | Frightened passive/aura trigger mechanic absent | Would have forced GM-stop if invoked |
| SC-04 surface | No Ruled initiative / action-economy procedure exists | Required scaffold before Round 1 could begin |
| Location tables | Anatomically-weighted numeric ranges for Location-Tier 1 not present in available corpus | Would have forced GM-stop or further scaffold if any location-referencing Effect had been selected |

---

## 8. Conclusion

The playtest reached a clean mechanical conclusion under DEC-052 without silent rule invention, narrative smoothing, or unauthorized mechanics.  

All Ruled subsystems that were exercised functioned as specified. The primary friction points were exactly the magnitude gaps and the missing initiative procedure already anticipated in the prompt’s candidate-DEC appendix.

**Provenance of the DEC-012 exception (reiterated):** the two pre-built Tier-2 skills on Adventurer-1 (Attack1, Defence1) were granted under a **prompt-level scaffold** (Tiwa’s authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012’s failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

This report is self-contained for cold review by OpenCode. No register, governance, or canonical files were modified.

---

*End of report.*

---

## Documentarian Verification (added by OpenCode, 2026-09-04)

Stored from `C:\Users\Tiwa Pene\Downloads\tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md` at Tiwa's instruction. This is the empirical execution record of Ice Troll combat against the v2.1 prompt, executed by Grok 4.5. Advisory only; makes no rulings, assigns no DEC numbers, promotes nothing.

**Assessment summary — the report is high quality, faithful to the v2.1 prompt specification, and mechanically consistent with the corpus.**

1. **Prompt-specification compliance:** opens with the mandated provenance block; carries the DEC-012 exception provenance note verbatim under Character (§3) and reiterated in the Conclusion (§8); collates all scaffolds in a single dedicated section (§4, SC-01…SC-06); reports a clean zero GM-stops outcome (§6); produces a candidate-DEC table (§7); and is self-contained for cold review.

2. **DEC-citation accuracy (verified against live register):** DEC-001 (d100/100-Fumble/Doubles), DEC-002 (floor), DEC-004 (derived stats), DEC-005 (Cap/Starting Value), DEC-006 (9-step transaction), DEC-007/007.A (Cost=roll, Overflow→HP), DEC-008 (floor(Regen/2), clamped), DEC-009/010 (Failure XP→Skill Roll Pool), DEC-013 (S-1 outcome matrix/Quality), DEC-031 (Quality-gated Effect tier), DEC-034 (sequential Track A/B), DEC-027/048 (Effect auto-apply + post-hoc mitigation), DEC-052 (HP=0 forced incapacitation), DEC-041/042 (location tiering, correctly never exercised). No citation errors found. Recovery claim "floor(Regen/2)" matches DEC-008 exactly.

3. **Empirical findings of note (correctly flagged, not invented over):**
   - **SC-04 (initiative/turn-order procedure) surfaced a genuine unanticipated gap.** DEC-082 rules the Time/Action *economy expression* (Skill-side/Movement-penalty only, no action-point budget) but does **not** establish a turn-sequencing/order procedure. The report's scaffold-before-Round-1 flag is a legitimate new empirical finding — a candidate DEC beyond the anticipated C-01…C-05.
   - **Location tables** gap (anatomically-weighted numeric ranges for Location-Tier 1) — correctly attributed to unexercised DEC-041 content; flagged rather than scaffolded, correct discipline.
   - **No GM-stops occurred** because the qualitative subsystem absence (C-04 Frightened passive/aura trigger) was deliberately not invoked — the prompt's disposition was respected, not evaded.

4. **Internal consistency:** SC-01 base-tier Inflict Injury (25 HP) and SC-02 Active Defense mitigation (−20 HP/full-cancel) are internally coherent with the stated "net 5 HP per exchange after mitigation" and the PC's 600 HP erosion over 22 rounds to HP 0. Attack1/Defence1 attribute basis (bpp+bps; bsp+bss) is a valid concretization of the v2.1 prompt's logged "select which two" construction detail. The §2.2 statement "no GM-stops" (section 6) is consistent with §4's scaffolds being magnitude-only.

**Scope note:** advisory recording only. `author_llm` remains Grok 4.5 (preserved); opencode appended as `assessor_llm` and set as `last_modified_by_llm` for the storage/assessment pass. No register, governance, or other repository files were modified. This empirical record is an appropriate basis for Tiwa to progress C-01…C-05 and the newly surfaced SC-04 initiative procedure through the normal designer-ruling path.
