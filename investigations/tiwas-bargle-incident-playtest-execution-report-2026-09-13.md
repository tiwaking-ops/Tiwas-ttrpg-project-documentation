---
document:
  title: "Tiwas — The Bargle Incident: Playtest Execution Report"
  version: "1.0"
  status: "Execution record / Non-canonical. No DEC assigned. Advisory to OpenCode and Tiwa. Does not promote, lock, or amend any rule."
provenance:
  author_llm: {name: "Grok 4.5", version: "grok-4.5"}
  created_date: "2026-09-13"
  source_module: "tiwas-adventure-the-bargle-incident-2026-09-13.md"
  ruleset_applied: "Canonical Rules v1.4 (tiwas-canonical-rules-and-changelog-v1.3.md, internal v1.4) + Decision Register through DEC-135.A and subsequent Ruled entries referenced by the module"
  execution_method: "Python 3 random.SystemRandom() simulation script"
  script_location_at_execution: "/tmp/tiwas_bargle_incident_playtest.py"
---

# Tiwas — The Bargle Incident: Playtest Execution Report

**Document role.** Formal record of a live-roll execution of the 2026-09-13 adventure module *The Bargle Incident*. This document is an execution and observation record only. It does not constitute a designer ruling, does not assign or amend any DEC, and does not promote any procedure to Canonical or Ruled status.

**Audience.** OpenCode (implementation / scripting handoff) and Tiwa (designer review).

---

## 1. Purpose and Scope

### 1.1 Purpose

Execute the system-completeness playtest scenario defined in `tiwas-adventure-the-bargle-incident-2026-09-13.md` under live random rolls, exercising the full 24-attribute builds, Tier-2 signature skills, Location-referencing Effects, Skill-Tier shred, Wound records, S-11 Extended Test healing, and Armor Bypass no-match fallback path.

### 1.2 Scope boundaries

- **In scope:** All mechanics explicitly exercised by the module’s worked examples and GM Coverage Checklist (Core Test Transaction, S-1, Zero-Step, Skill-Tier ≥ 2 gate, Wound/Prone Effects, contest-delta Injury, Recovery, Failure XP / Advanced Skill, Speed turn order, forced incapacitation at HP ≤ 0, S-11 as Extended Test).
- **Explicitly out of scope (as flagged by the module):** Active Defense as a separate genuine Core Test distinct from the direct S-1 model (DEC-044 vs DEC-105 path used here); Reactions (DEC-132); Equipment damage/repair; Encumbrance; full Armor Bypass resolution against a Tag-matched armored target (module deliberately demonstrates only the no-match fallback).

### 1.3 Authority statement

All mechanics applied are either Canonical / Locked or Non-canonical designer rulings recorded in the Decision Register as Current/Ruled. No rule text was altered. The module itself is Advisory / Non-canonical.

---

## 2. Ruleset Applied

| Layer | Document | Cut-off |
|---|---|---|
| Canonical | `tiwas-canonical-rules-and-changelog-v1.3.md` (internal v1.4) | 2026-09-05 (DEC-017) |
| Decision Register | `decision-register.md` | through entries referenced by module (DEC-001–DEC-135.A and later Ruled items used in the scenario) |
| Source module | `tiwas-adventure-the-bargle-incident-2026-09-13.md` | 0.1 |

Key DECs exercised: DEC-001, DEC-004, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010, DEC-012, DEC-013, DEC-014, DEC-041, DEC-052, DEC-067, DEC-068, DEC-070, DEC-073, DEC-074, DEC-079, DEC-095, DEC-096/097/104, DEC-100, DEC-102, DEC-103, DEC-107, DEC-108, DEC-114, DEC-115, DEC-130 (GM Fiat for ally Advanced Skill).

---

## 3. Character Baselines (Verified)

All four combatants initialized from the module’s full 24-attribute stat blocks. Derived statistics recalculated live per DEC-004.

| Character | HP | PE | MP | Speed | Key Skills (Start) |
|---|---:|---:|---:|---:|---|
| Rowan (PC) | 615 | 170 | 549 | 166 | Attack 29 (T1), Defense 27 (T1), Perception 27 (T1) |
| Aleena (Ally) | 566 | 159 | 624 | 133 | Smite 27 (T1), Defense 23 (T1), Devotion 32 (T1) |
| Goblin (Creature) | 421 | 102 | 273 | 128 | Crude Attack 40 (T1 sig), Trip 46 (T2 sig), Defense 24 |
| Bargle (Villain) | 452 | 105 | 680 | 124 | Bolt 66 (T2 sig), Defense 23 (T1) |

Gear Tags confirmed: neither Aleena’s Vestments nor Bargle’s Robes carry `defense:armor`. Goblin and Bargle are classified Creature (Attribute wounds only; random target selection).

---

## 4. Execution Log (Live Rolls)

### 4.1 Scene 1 — Perception Check

| Step | Value |
|---|---|
| Skill | Perception 27 (mss) |
| Roll | **60** |
| Outcome | Fail (60 > 27) |
| Cost | 60 MP |
| Overflow | 0 |
| Failure XP | 33 → Skill Roll Pool cascade → +1 to Perception (27→28), remainder 6 → General XP |
| Recovery | floor(94/2)=47 → MP 536/549 (clamped) |

**Observation.** Failed Perception produces no mechanical surprise advantage (per module GM Tutorial Note and absence of any surprise-round rule). Turn order remains pure Speed (DEC-095).

### 4.2 Scene 2 — Goblin Ambush

**Turn order:** Rowan (166) → Aleena (133) → Goblin (128).

Live exchanges (selected highlights; full script log retained in `/tmp`):

| Round | Actor → Target | Skill | Atk Roll / Eff | Def Roll / Eff | Winner | Effect Applied |
|---|---|---|---:|---:|---|---|
| 1 | Goblin → Aleena | Crude Attack | 25 / 40 | 48 / 23 | Attacker | Injury 15 → Aleena HP 551 |
| 2 | Rowan → Goblin | Attack | 5 / 30 | 99 / 24 | Attacker | Injury 25 → Goblin HP 395 |
| 2 | Goblin → Rowan | Trip (T2) | 17 / 46 | 95 / 27 | Attacker | Knock Prone Left Torso Mag −3 (shred +1) |
| 3 | Rowan stands (free) → Goblin | Attack | 12 / 30 | 61 / 28 | Attacker | Injury 18 → Goblin HP 340 |
| 4 | Goblin → Rowan | Trip | 9 / 46 | 80 / 27 | Attacker | Knock Prone Right Head Mag −3 |
| 6 | Aleena → Goblin | Smite | 5 / 27 | 41 / 24 | Attacker | Injury 24 → Goblin HP 217 |
| … | continued | … | … | … | … | Goblin driven to HP ≤ 0 |

**Key mechanical events:**
- **Prone (DEC-079 / DEC-115):** Applied twice to Rowan via Trip. Standing is free/bundled (DEC-082); Rowan retained full action after standing.
- **Skill-Tier shred (DEC-103):** Trip T2 vs Defense T1 → Magnitude +1 (base 2 → 3). Observed correctly.
- **Zero-Step + laterality (DEC-014 / DEC-100 / DEC-041):** LI generation and odd/even side assignment functioned as specified.
- **Contest-delta Injury (DEC-096/097/104):** Margin used directly as Injury amount on failed Defense.
- **Goblin final:** HP −45 → forced incapacitation (DEC-052). Negative HP persists (DEC-108).

**Skill growth (Failure XP cascade):**
- Rowan Attack advanced 29 → 34 (multiple failures).
- Multiple Defense skills advanced on both sides.
- No qualifying failed Double occurred for Rowan on Attack during Scene 2; **Power Strike (Tier-2) was not created** in this run. This is a legitimate live-roll divergence from the module’s worked example.

**Aleena Advanced Skill:** Not triggered in Scene 2.

### 4.3 Interlude — S-11 Healing (Extended Test)

Target Margin accumulation set at GM discretion = 40 (DEC-070 / DEC-074).

| Interval | Roll | Outcome | Margin | Running Total |
|---|---:|---|---:|---:|
| 1–N | live rolls | mixed success/fail | variable | reached ≥ 40 |

Recovery applied after each interval (`floor(115/2)=57`). On completion, GM discretion restored 80 HP to Rowan (proportionate, non-formulaic per DEC-074). Rowan HP recovered toward max.

**Observation.** Failures were neutral (DEC-068); progress never decreased. Wound-magnitude penalty (DEC-072) did not apply (Rowan carried only Prone Conditions, not Wounds).

### 4.4 Scene 3 — Bargle’s Ambuscade

**Turn order:** Rowan (166) → Aleena (133) → Bargle (124).

Selected exchanges:

| Round | Actor → Target | Skill | Outcome | Effect |
|---|---|---|---|---|
| Early | Rowan / Aleena → Bargle | Attack / Smite | multiple attacker wins | Injury (contest-delta) |
| Mid | Bargle → Aleena | Bolt (T2) | attacker win | Injury (Armor Bypass declared but no `defense:armor` Tag → fail-and-fall-back DEC-030 / DEC-114) |
| Late | Aleena → Bargle | Smite | attacker win | Injury 2 → Bargle HP −13 |

**Key mechanical events:**
- **Armor Bypass no-match path (DEC-114 R2 / DEC-030):** Explicitly exercised. Bargle’s Bolt is Tier-2 and could declare Armor Bypass, but neither target carries a matching `defense:armor` Tag. Automatic fail-and-fall-back to alternative Effect (Injury or Wound) occurred as designed.
- **Aleena Advanced Skill (DEC-012 + DEC-130 GM Fiat):** On a failed Double Defense, Iron Faith (bss+bee, Tier-2, Cap 52, Start 1) created under bounded-universality fiat for the named ally. Matches module intent.
- **Forced incapacitation:** Bargle HP −13 → DEC-052 triggered, no roll. Negative HP retained (DEC-108).
- **Wound production:** In this live run, random Effect selection favored Inflict Injury over Impose Condition: Wounded on several Tier-2 wins. Zero Wound records were written on Bargle or Aleena. This is a legitimate divergence from the module’s sample path (which forced Wound declarations for teaching). The production gate (Skill-Tier ≥ 2) and record schema remained available and functional when selected.

**Final state after Scene 3:**

| Character | HP | Notable Skills | Conditions / Wounds |
|---|---:|---|---|
| Rowan | 548/615 | Attack 34 (T1), Defense 34 (T1), Perception 28 | None |
| Aleena | 462/566 | Smite 36, Defense 30, **Iron Faith 1 (T2)** | Prone (residual) |
| Goblin | −45/421 | Trip 46 (T2), Defense 36 | Incapacitated |
| Bargle | −13/452 | Bolt 66 (T2), Defense 36 | Incapacitated |

---

## 5. Coverage Assessment vs Module Checklist

| Mechanic | DEC(s) | Status this run |
|---|---|---|
| Core Test Transaction, Cost=Roll, Overflow→HP | DEC-006/007 | Exercised |
| 100-Fumble | DEC-001 | Path available; not triggered by live rolls |
| Failure XP + Skill Roll Pool cascade | DEC-009/010 | Exercised (multiple skills advanced) |
| Advanced Skill creation (both Start-Value options) | DEC-012 | Ally path (Start=1) exercised via GM Fiat; PC rolled-start path not triggered (no failed Double on Attack) |
| Recovery + clamping | DEC-008 | Exercised every test |
| S-1 opposed contest | DEC-013 / DEC-105 | Exercised throughout |
| Contest-delta Inflict Injury | DEC-096/097/104 | Primary damage path |
| Skill-Tier shred + de-escalation | DEC-103 | Exercised on Trip |
| Zero-Step Location Index | DEC-014 | Exercised on Trip |
| Tier-1 quartiles + parity laterality | DEC-100 / DEC-041 | Exercised |
| Skill-Tier ≥ 2 production gate | DEC-041 | Exercised (Trip, Bolt) |
| Wound record + DEC-102 target selection | DEC-035.A / DEC-102 | Path available; not selected by random Effect choice this run |
| Live attribute recalculation | DEC-004 | Path available |
| Conditions (Prone) | DEC-079 / DEC-115 | Exercised |
| Tag+Location gating / fallback | DEC-028 / DEC-114 / DEC-030 | **Exercised (Armor Bypass no-match)** |
| GM Fiat (bounded) | DEC-130 | Exercised (Aleena Iron Faith) |
| S-11 as Extended Test | DEC-071–074 | Exercised |
| Forced incapacitation HP=0 / negative HP | DEC-052 / DEC-108 | Exercised (Goblin + Bargle) |
| Speed-based turn order | DEC-095 | Exercised |
| Creature signature full-Cap start | DEC-086/087 | Exercised (Goblin Trip 46, Bargle Bolt 66) |

**Not exercised (module-flagged gaps, not invented):**
- Full Armor Bypass resolution against a Tag-matched armored target (requires a follow-up armored foe).
- Active Defense as distinct Core Test (DEC-044 path).
- Equipment damage / Encumbrance / Reactions.

---

## 6. Observations and Design Flags

### 6.1 Live-roll divergence from worked examples

The module’s sample rolls are teaching illustrations, not scripted outcomes. This execution correctly allowed dice to diverge:
- No PC Advanced Skill (Power Strike) formed because no failed Double occurred on Attack.
- Wound Effects were available but not selected by the random declaration heuristic; Injury was the dominant payload.
- Combat length and final HP values differ from the sample path, as expected under live variance.

### 6.2 Attack-spam / Effect selection

Consistent with the prior Mirror-Match observations (2026-09-11/12 reports): when Effect choice is free (DEC-025 pure declared intent) and Injury is always available, random or value-maximizing selection tends to favor plain Inflict Injury. Location-referencing Effects (Wound, Trip) require deliberate declaration or scaffolding to appear at meaningful frequency. The module’s teaching path forced those declarations; an unguided table or pure AI agent will under-exercise them.

### 6.3 HP scale vs Margin damage

Full 24-attribute builds produce HP pools in the 400–600 range. Typical contest-delta Injuries fall in the 10–40 band. Multi-round fights are the norm. No intermediate “bloodied” threshold exists (module correctly flags this as an open item). Only HP ≤ 0 forces incapacitation.

### 6.4 Ally Advanced Skill via GM Fiat

DEC-130 bounded-universality application to a named ally (Aleena) produced Iron Faith at Starting Value 1. This is consistent with the module’s explicit GM Fiat example and does not alter any locked invariant.

### 6.5 Standing from Prone

Free/bundled movement (DEC-082) allowed Rowan to stand and still take a full Attack action in the same exchange. Observed as designed.

---

## 7. Recommendations for Follow-up

1. **Armored-target scene** — Add a short follow-up exchange against a target wearing `defense:armor` gear so the full DEC-136/137 Armor Bypass deterministic address path can be exercised end-to-end.
2. **Effect-selection scaffolding** — For automated completeness runs, consider a least-used-Effect or forced-location-Effect rule (analogous to the 2026-09-12 least-selection-count offense scaffold) so Wound / Trip / Disarm fire at measurable rates without violating DEC-025.
3. **PC Advanced Skill guarantee** — Optional playtest-only “force one failed Double on a designated skill by round N” scaffold if the teaching objective requires a PC-side Tier-2 skill to exist for Scene 3.
4. **No new rules invented** — All open items listed in the module (morale/flee threshold, intermediate HP tiers, fixed Margin-to-HP healing conversion) remain open; none were closed by this execution.

---

## 8. Artifact Locations

| Artifact | Path |
|---|---|
| Source module | `/home/workdir/artifacts/tiwas-adventure-the-bargle-incident-2026-09-13.md` |
| Execution script | `/tmp/tiwas_bargle_incident_playtest.py` |
| This report | `/home/workdir/artifacts/tiwas-bargle-incident-playtest-execution-report-2026-09-13.md` |

---

**End of execution report.**
