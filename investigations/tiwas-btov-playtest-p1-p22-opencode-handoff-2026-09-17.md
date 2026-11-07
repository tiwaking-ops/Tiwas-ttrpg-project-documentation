---
document:
  title: "Tiwas — BToV Opening Solo Playtest (¶1–22) — Complete Results Handoff Report to OpenCode"
  version: "1.0"
  status: "NON-CANONICAL — advisory empirical handoff record. Reports an executed seeded playtest; makes no rulings, assigns no DEC, promotes nothing. Storage confers no authority."
provenance:
  author_llm: {name: "Buffy (Codebuff)", version: "unknown / not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "Buffy (Codebuff)", version: "unknown / not established"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
  identity_established_by: "self-reported"
---

# Tiwas — BToV Opening Solo Playtest (¶1–22): Complete Results Handoff to OpenCode

**Author:** Buffy (Codebuff) — LLM name: **Buffy**, LLM version: **unknown / not established**
(self-reported; the session exposes no non-forgeable model-version field, so the version is recorded
as unknown rather than guessed, per `governance/provenance.md`).

## Provenance note

This handoff was produced by **Buffy (Codebuff)** on **2026-09-17**. Identity is **self-reported** —
a claim by the producing model, not a verified signature. This document is NON-CANONICAL and
advisory: it reports an executed playtest and confers no authority on any mechanic it exercised.
Per `governance/status-model.md`, playtest evidence never changes status; only the 8-step Promotion
Rule does.

## 1. Status and purpose

Complete-results handoff to OpenCode (the repository's other working LLM, per the established
handoff pattern — e.g., `investigations/tiwas-repeated-defense-fatigue-reaction-architecture-handoff-2026-09-10.md`)
for the executed seeded solo playtest of **Beyond the Vale of Madness** opening (¶1–22), run
2026-09-17 under the locked Core and the ruled DEC stack. Purpose: give OpenCode the full empirical
record — every resolution, both ledgers, all findings — so downstream analysis can proceed without
re-running the harness. Companion artifacts:

- Report: `investigations/tiwas-btov-opening-solo-playtest-p1-p22-report-2026-09-17.md`
- Raw log: `investigations/tiwas-btov-opening-solo-playtest-p1-p22-raw-log-2026-09-17.json`
  (89 records, seed 20260917)

## 2. Basis and method (condensed; full detail in the companion report)

- **Harness:** Python, single seeded RNG (seed **20260917**), d100 ∈ 1–100, `00 = 100`.
- **PC:** locked generation (Canonical §3–§5): 24 × 1d100 attributes; HP = Σ Body = **593**;
  MP = Σ Mind = **666**; PE = bep+bes+bee = **68** (Regen 20); MP Regen = mep+mes = **137**;
  Movement = floor((bsp+bss)/15) = **4**. All skills at Starting Value = floor(Cap/2): Axe 42,
  First Aid 42, Torch-tending 36, Climbing 20, Stealth 17, Active Defense 17, Woodsman 15, Search 13.
- **Opponent:** Ice Troll from the DEC-077.A working conversion (v0.2 scratch §2, advisory content):
  HP **705**, PE 220 (Regen 140), Icy Claws **67** (Tier 2) / Sharktoothed Maw **75** (Tier 2);
  defense 30 = advisory fiat (no ruled NPC-construction method; Canonical §15 reserves NPC construction).
- **Route (PDF fork table):** ¶1 → #12 (cave; torch) → #9 → #44 (sneak) → #41 (perceived) →
  **#17 combat** → #21 (bandaging) → #25 → #22. Combat log capped at 8 exchanges.
- **Layer tags on every log record:** `locked` (Canonical v1.3) · `ruled` (DEC register) ·
  `locked+ruled` · `advisory` (unruled fiat, flagged) · `empirical` (ledger/summary).

## 3. Complete results

### 3.1 Outcome

**PC down (HP −18) at combat exchange 6 of 8; Ice Troll at 613/705.** The run never reaches #21's
successful bandaging or the #25/#22 exit in a surviving state; the post-combat advisory records were
still executed for completeness (failed First Aid, +2 HP token, −10 PE scenario costs).

### 3.2 Non-combat spine (locked-layer resolutions)

| ¶ | Test | Skill | Roll | Outcome | Cost | Overflow → HP | Consequence |
|---|---|---:|---:|---|---:|---:|---|
| #12 | Torch-tending (bse) | 36 | 93 | **F** | 93 | **25** | PC 593 → 568; DARKNESS keyword (advisory tag) |
| #44 | Stealth (bss) | 17 | 95 | **F** | 95 | **85** | PC 568 → 483; troll perceives → #41 → #17 |
| #21 | First Aid (mss) | 42 | 65 | F | 65 | 0 | Advisory +2 HP token (DEC-110 posture) |

### 3.3 #17 Ice Troll combat — complete exchange-by-exchange table

Both sides run a full Canonical §6 transaction per test (costs and recovery omitted from this table
for legibility; they are in the raw log record-by-record). Damage = DEC-104 contest-delta;
defense-0/mitigation-0 per DEC-097; zones = Zero-Step (§14.1) + DEC-100 quartiles.

| Ex | PC attack (Axe 42) | Troll defense (30) | Result | PC dmg to troll | Troll attack | PC defense (17) | Result | Troll dmg to PC | Zones hit (PC→Troll / Troll→PC) |
|---:|---|---:|---|---:|---|---|---|---:|---|
| 1 | 20 S | 74 F | PC wins | **22** | Icy Claws 99 F (Double, unruled creature-advancement — deferred) | 16 S | attack fails (DEC-101) | 0 | Legs / — |
| 2 | 38 S | 4 S | Quality 4 vs 26 → troll | 0 | Maw 64 S | 94 F | **11** | — / Torso (M3 wound, DEC-103) |
| 3 | 1 S | 64 F | PC wins | **41** | Icy Claws 80 F | 68 F | F/F → §13.4 repeat | 0 | Legs / — |
| 4 | 21 S | 98 F | PC wins | **21** | Maw 79 F | 45 F | F/F → §13.4 repeat | 0 | Legs / — |
| 5 | 33 S | 29 S | Quality 9 vs 1 → PC | **8** | Icy Claws 26 S | 54 F | **41** | — / Arms (M3 wound) |
| 6 | 60 F | 26 S | attack fails (DEC-101) | 0 | Maw 6 S | 50 F | **69** | — / Arms (M3 wound) |
| — | **PC down** | | | | | | | | **Troll: 613/705** |

**Troll HP ledger:** 705 − 22 − 41 − 21 − 8 = **613** (four winning strikes).
**PC HP ledger:** 593 − 490 overflow − 11 − 41 − 69 = **−18** (three winning strikes).

### 3.4 DEC-103 Wound records (every application, ruled layer; arithmetic verified)

| Ex | Attacker | Zone | Base Mag (Tier 2) | Shred (Step 1) | De-escalation (Step 2) | Surviving Effect |
|---|---|---|---:|---:|---:|---|
| 2 | Troll (Maw, T2) | Torso | 2 | +1 (Atk T2 > Def T1; gap irrelevant) | −0 (defender failed, DEC-097) | **Torso Tier-2 Wound-type Effect Mag 3** |
| 5 | Troll (Claws, T2) | Arms | 2 | +1 | −0 | **Arms Tier-2 Wound-type Effect Mag 3** |
| 6 | Troll (Maw, T2) | Arms | 2 | +1 | −0 | **Arms Tier-2 Wound-type Effect Mag 3** |

**Tier arithmetic, verified record-by-record:** the troll's attacks are Tier-2 skills; the PC's
Active Defense (bss) is Tier-1. DEC-103 Step 1: Atk > Def → Mag +1 (gap irrelevant) → base 3.
Step 2: the defender failed each time → de-escalation 0 → surviving Mag 3 in all three cases,
matching the log exactly. No correction required; the wound magnitudes are arithmetically
verified, not merely as-logged.

### 3.5 Total ledgers (verified)

| Quantity | Value | Composition |
|---|---:|---|
| PC HP lost | **611** | 490 overflow (locked §7) + 121 DEC-104 damage (ruled) |
| — overflow share | **80%** | Structural: PE 68 pool vs failing rolls 45–95, recovery floor +10/test |
| Troll HP lost | **92** | DEC-104 deltas 22+41+21+8 |
| Failure XP (PC) | **402** | Canonical §9, all failures |
| Failure XP (troll) | logged per-test | e.g., 44, 32, 34, 68 — no creature-advancement policy to consume it |
| Layer census (89 records) | locked 30 · ruled 35 · locked+ruled 7 · advisory 8 · empirical 9 | Non-canonical layers = 50 records |
| Conditions (PC) | Torso Wound M3, Arms Wound M3, Arms Wound M3 | All three arithmetically verified per DEC-103 (§3.4) |

## 4. Empirical findings (complete list; evidence, not rulings)

- **F1 — Overflow, not the monster, dominates PC death (80% of HP loss).** Starting Value = Cap/2
  means failing rolls (45–95 here) routinely exceed the entire PE pool (68); once recovery pins the
  pool at floor(Regen/2) = +10/test, every further test bleeds roll−10 into HP. The troll's claws
  dealt 121. Structural, not seed-luck.
- **F2 — Recovery pins pools at the floor mid-scene.** PC PE sat at 10 for the whole fight;
  troll PE never fell below 173. Pool attrition is neutralized as a pressure mechanism except at
  overflow spikes.
- **F3 — The DEC-103 wound channel functioned end-to-end but is entirely ruled-layer.** Every
  condition in the run is register-sourced; Canonical §15 reserves conditions/wounds/effects.
- **F4 — Both defense values are advisory fiat.** Combat outcomes are sensitive to unruled
  parameters (NPC construction Reserved; PC defense scenario-authored).
- **F5 — DEC-135 repeated-defense fatigue never fired** — its trigger parameters were never
  extracted; the PC defended all 6 exchanges. Dormant watch-item, not a result.
- **F6 — The adventure's FP economy has no carrier.** #12/#25/#22 FP costs were advisory direct-PE
  conversions; no canonical or ruled hazard mechanic was invoked.
- **F7 — Dice mechanics verified:** no 100-Fumble occurred; the troll's 99-Double surfaced the
  unruled creature-advancement question (deferred, not silently resolved); Zero-Step and quartile
  mappings hand-verified.

## 5. Harness-correction register (disclosed to OpenCode for assessment)

OpenCode is specifically asked to assess these, as the second assessor:

- **H1:** DEC-103 tier arithmetic was re-verified by hand for all three wounds (T2 attack vs T1
  defense → Mag +1; failed defense → de-escalation 0 → M3 each). Logged and verified values agree;
  an intermediate draft of this handoff briefly mis-flagged them as discrepancies (it assumed
  equal tiers) — noted here for assessment-trail honesty, no correction needed.
- **H2:** v1 of the harness had a transaction-order bug (recovery not applied; HP conflated with
  pool arithmetic). It was discarded and the reported run is corrected v2 — disclosed for method
  honesty; v1 never produced a stored log.
- **H3:** Troll "defense 30" and PC "Active Defense 17" are advisory values; no ruled construction.
- **H4:** The #44 sneak resolution modeled the troll's opposition with an advisory resistance test
  rather than a ruled Perception skill (none exists for converted creatures yet).
- **H5:** DEC-135's self-deficit (−2 PE per Tier-2 Effect) was applied as an advisory sketch of a
  partially-extracted ruling; parameters not fully extracted from the register row.
- **H6:** Single seeded run — anecdote, not statistics. No distributional claims.

## 6. Open items surfaced for downstream work

1. NPC defense construction (combat-critical gap; options-brief candidate).
2. Overflow lethality vs low-Skill characters (design question for Tiwa; F1).
3. Creature advancement policy (troll's failed Double, Failure XP sink).
4. DEC-135 parameter extraction (repeated-defense trigger; self-deficit values).
5. FP/hazard carrier for scenario costs (DEC-079/135 scaffolds exist, unmapped).

## 7. Governance and authority boundary

This handoff does not rule, promote, demote, supersede, authorize, or reopen anything. All cited
rules remain at their existing status. Findings F1–F7 and harness notes H1–H6 are advisory evidence
for the designer and OpenCode; no interpretation is silently resolved. The companion raw log is the
authoritative record of what the harness executed; where this summary and the log disagree, the log
wins (and §3.4/H1 documents exactly such a disagreement).

## 8. Source register

| Source | Function |
|---|---|
| `investigations/tiwas-btov-opening-solo-playtest-p1-p22-report-2026-09-17.md` | Companion formal report (method, findings F1–F7) |
| `investigations/tiwas-btov-opening-solo-playtest-p1-p22-raw-log-2026-09-17.json` | Verbatim 89-record execution log (seed 20260917) — authoritative record |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` | Locked layer (§2–§9, §13, §14.1, §15) |
| `_consolidation/decision-register.md` | Ruled layer (DEC-100/101/103/104/105/097/110/135; DEC-077.A) |
| `investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md` | Advisory opponent content (§2.1–2.3) |
| `Beyond-the-Vale-of-Madness-GURPS.pdf` | Scenario structure, ¶1–22 route and costs |

*End of NON-CANONICAL advisory complete-results handoff.*
