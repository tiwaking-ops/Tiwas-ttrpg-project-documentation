---
document:
  title: "Tiwas — Red Box Solo Playtest (seed 20260917): Complete Results Handoff to OpenCode"
  version: "1.1"
  status: "NON-CANONICAL — advisory empirical handoff record. Reports an executed seeded playtest; makes no rulings, assigns no DEC, promotes nothing. Storage confers no authority."
provenance:
  author_llm: {name: "opencode", version: "unknown / not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "Muse Spark", version: "unknown / not established"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
  identity_established_by: "self-reported"
---

# Tiwas — Red Box Solo Playtest: Complete Results Handoff to OpenCode

**Author:** opencode (v1.0) — revised v1.1 by **Muse Spark** (version unknown /
not established — self-reported; the session exposes no non-forgeable
model-version field, per `governance/provenance.md`). NON-CANONICAL advisory:
evidence, not rulings. Per `governance/status-model.md`, playtest evidence never
changes status; only the 8-step Promotion Rule does.

## 1. Status and purpose

Complete-results handoff for the seeded solo playtest of the **Mentzer D&D Red
Box solo adaptation** (reconstructed from general knowledge: character-creation
walkthrough, road encounters, Aleena/Bargle finale), run 2026-09-17 under the
locked Core + ruled DEC stack. Purpose: give OpenCode the full empirical record
— resolutions, ledgers, skill progression, correction register — without re-running.

Companion artifacts: module `tiwas-adventure-red-box-solo-2026-09-17.md` (v1.1) ·
harness `tiwas-red-box-playtest-harness.py` (v1.2) · raw log
`tiwas-red-box-playtest-20260917-raw-log.json` (98 records, authoritative) ·
report `tiwas-red-box-playtest-execution-report-2026-09-17.md`.

**Fidelity discipline:** every adventure beat is a reconstruction from general
knowledge + the two research sources (beat skeleton only, never quoted). The
module keeps the full fidelity-limits list; this handoff inherits it. The module
shares characters — not content — with the repo's existing Aleena/Bargle modules;
no stat block was imported from them (divergence evidence, not source).

## 2. Basis and method (condensed)

- **Harness:** Python, single seeded RNG (`random.Random(20260917)`), d100 1–100
  (`00`=100). H1(a) restore = accumulated Margin capped at current max; H2 target
  40; H3 Devotion-only, MP cost = natural roll, HP-only; H4 targeted penalty; H5
  wound-record healing excluded; H6 negative-HP terminal; H7 locked order.
- **PC/NPCs (locked derivation §4/DEC-004):** Rowan HP 612 / MP 549 / PE 170;
  Aleena HP 566 / MP 624; Goblin 421; Snake 417; Ghoul 494; Bargle 452. PC skills
  start floor(Cap/2); creature signatures at full Cap (DEC-086/087). **All Defense
  values advisory fiat** (NPC construction Reserved, Canonical §15; DEC-077.A
  workflow used analogically — its ruled scope is GURPS-BToV only, flagged).
- **Route:** S1 teaching beat + Goblin (6-round budget, symmetric) → S2 Snake
  (5 rounds, snake first) → S3 Aleena S-11 → S4 turning → S5 door (3 bash) →
  S6 Bargle (3 rounds + fork) → Aftermath heal. Injury = contest-delta (DEC-104).
- **Opponents (DEC-077.A-analogous, all defenses fiat):** Goblin HP 421, Crude
  Attack 40 T1 sig, Trip 46 T2 sig; Snake HP 417, Venomous Bite 59 T2 sig;
  Ghoul HP 494, Claw 39 / Grapple 46 / Desecration 22 (all T2 sig); Bargle HP
  452, Bolt 66 T2 sig, Beguile 27. Poison/charm/morale unruled (advisory).
- **Checkpoint policy (disclosed):** single-life run; on PC death the run would
  stop (H6 terminal, no re-seed). No death occurred, so the policy never fired.
- **Layer tags:** `locked+ruled` 71 · `empirical` 12 · `locked` 14 · `advisory` 1
  (sums 98 ✓; no pure-`ruled` records — contests always pair locked + ruled).

## 3. Complete results

**Seed 20260917 — single life, no re-seed.** All scenes resolved; no death; every
fight ended by budget-expiry withdrawal, never HP≤0 (Goblin 215/421, Snake
218/417, Bargle 386/452 alive at end). Climax fork → Ending A (tie → defense holds).

| Checkpoint | Result |
|---|---|
| S1 Perception teaching beat | Fixed 00=100 → fail; Perception (Advanced) T2 created (DEC-012) |
| S1 Goblin fight (29 records) | 6-round budget → withdrawal (narrated); Goblin 215/421 alive |
| S2 Snake fight (23 records) | 5-round budget → retreat (narrated); Snake 218/417 alive |
| S3 Aleena healing (6 records) | Margin 41 ≥ 40 → Rowan +41 HP |
| S4 Ghoul turning (2 records) | Devotion 32 vs Desecration 22 → narrative success (flagged) |
| S5 Locked door (3 records) | 3 bash fails → forced open by exhaustion (narrated) |
| S6 Bargle fight (31 records) | 3-round budget; Bargle 386/452 alive; Aleena −67 |
| Climax fork (1 advisory record) | Beguile vs Composure tie → Ending A |
| Aftermath (4 records) | Margin 53 → Rowan +53 HP |

**Verified HP ledger (log wins; asserts pass):**
Rowan **612 → 591 (Δ −21):** −49 S1 (Goblin 12+37) −55 S2 (Snake) −11 S2
self-overflow (Defense roll 79) +41 S3 (Margin 41: rolls 29/26/54/60/26/6) +53
Aftermath (Margin 53: rolls 21/49/6/16 → 11+0+26+16). 612−49−55−11+41+53 = 591 ✓.
Aleena **566 → 499 (Δ −67):** S6 Bolt injuries 58+9 = 67 ✓.

**Overflow census (12 events, 361 HP):** Goblin 5/179 (rolls 72/97/70/84/51) ·
Snake 5/168 (Bite 93/74/98, Defense 38/33 → 22/48/73/15/10) · Rowan 1/11 ·
Bargle 1/3. Creature self-damage = 347 of 361 (96%).

**Skill progression:** Rowan Attack 29→36, Defense 27→36, Perception 27→29;
Perception (Advanced) T2 + Defense (Advanced) T2 created; Snake Defense
(Advanced) T2 created (3 = DEC-012/140 ✓). Aleena Smite +1, Defense +1; Bargle
Defense +5. 22 `skill_grew` cascades. Rowan max_hp 612→611 (1 Body wound applied
to state, unlogged — HC-1); Aleena wounds 2 in state, same cause.

## 4. Empirical findings (evidence, not rulings)

- **F1 — Creature Overflow self-damage dominates (empirical, structural).** Goblin
  179 + Snake 168 self-inflicted vs 49 + 66 dealt. High-Cap signatures (40/59)
  vs small PE pools (102/71) make Overflow the dominant creature damage channel.
  DEC-007 working as designed; balance is Tiwa's question. Trace: 10 S1/S2 records.
- **F2 — Wound mechanics ran but left almost no log trace (empirical,
  harness-attributed, HC-1).** Zero `wound_applied` records, yet Rowan max_hp
  −1 and Aleena wounds 2 prove state writes happened. DEC-041/102/035.A/004 fired
  invisibly. Coverage real but forensic-poor.
- **F3 — Advanced-Skill creation fired 3×, all correct (empirical).** Deterministic
  100-fumble + 2 natural Doubles, incl. creature-side (DEC-140 universal ✓).
- **F4 — Failure-as-growth front-loaded on the losing PC (empirical).** Rowan
  +7/+9 vs Aleena +1/+1 — successes (Devotion heals) generate no XP by design.
- **F5 — S-11 heals cleanly under H1(a)/H7 (empirical).** S3 Margin 41, Aftermath
  Margin 53; DEC-072.A found no Devotion-targeted wounds → unpenalized.
- **F6 — Climax fork resolves advisory-only (empirical, advisory).** Beguile vs
  Composure tie → Ending A. Charm unruled; mapping flagged.
- **F7 — Budgets, not HP, ended every fight (empirical, single-run).** No
  survival-rate claim from one seed.
- **F8 — Door bash teaches DEC-041 correctly (empirical).** 3 failed Tier-1 bashes,
  PE cost, no Location Index, no Wound.

## 5. Harness-correction register (for OpenCode assessment)

- **HC-0 — Console-encoding crash, fixed v1.1→v1.2 (no logic change).** v1.1 wrote
  the JSON then crashed on non-ASCII prints (cp1252); asserts never ran. v1.2 uses
  ASCII prints; re-run reaches both asserts with identical ledger/census.
  Discard-and-rebuild disclosed, not hidden.
- **HC-1 — Wound logging defect (code, not rules).** `s1_contest` applies
  prescribed Wounds to state but appends no log record. Rules operated; the
  authoritative log does not capture it. Fix: log every state write.
- **HC-2 — Overflow asymmetry is construction-level (empirical, not a defect).**
  Full-Cap signatures (DEC-086/087) + small PE pools → self-damage. Fix, if
  wanted, is in stat-block construction, not harness or rules.
- **HC-3 — Climax fork advisory by design.** No correction; charm remains unruled.
- **HC-4 — Report prose corrected to the log (v1.1).** Aftermath 41→53, overflow
  11/358→12/361, Goblin rolls corrected, S3 intervals tabulated verbatim. Log won.

## 6. Guesses (confidence in label)

1. Symmetric combat both-roll (high — DEC-095/105). 2. HC-1 run-as-is, wound real
   via max_hp evidence (high). 3. S6 Bargle-first narrative override of Speed
   (medium). 4. Fork tie → Ending A (medium — advisory). 5. Aftermath as second
   S-11 pass (high — module structure). 6. Single-seed, no distributions (high).
7. DEC-077.A analogical reuse for D&D beats (medium) — workflow ruled for
   GURPS-BToV only; **human question (module §Authority): does DEC-077.A extend
   to non-GURPS sources, or is a separate path needed?** Stopping here.

## 7. Open items for downstream work

1. HC-1 fix (log every wound state-write) — forensic gap, not rules gap.
2. Creature PE vs full-Cap signature balance (F1/HC-2) — consider a PE-floor
   convention for creatures, or accept self-damage as a creature weakness.
3. Wound forensic logging — if wounds matter downstream, the log must capture
   record schema, target attribute, and recalc deltas per event.
4. Charm/mental-influence subsystem — advisory placeholder only; needs a ruled
   proposal (with its own DEC path) if the fork is ever to be more than narrative.
5. Poison / morale / invisibility / treasure-value mappings — all advisory;
   each needs either a ruled subsystem or a standing fiat convention.
6. DEC-077.A scope ruling (see §6.7) — blocks the module's claim to workflow
   coverage until Tiwa answers.
7. Reaction frequency under uncapped R3 — exercised once here; heavier use
   (multi-party simultaneous reactions, DEC-132.A R4) is untested.
8. S-11 wound-record healing (H5) — excluded by convention; the HP/Wound
   two-track teaching (module Aftermath) is asserted, not executed.

## 8. Governance and authority boundary

No ruling, promotion, demotion, supersession, or reopening. All rules keep existing
status. F1–F8, HC-0–HC-4, guesses 1–7 are advisory evidence. Raw log is
authoritative; summary disagreements resolve to the log.

## 9. Source register

| Source | Function |
|---|---|
| `…/tiwas-red-box-playtest-20260917-raw-log.json` | 98-record log (seed 20260917) — authoritative |
| `…/tiwas-red-box-playtest-harness.py` (v1.2) | Seeded deterministic harness |
| `…/tiwas-red-box-playtest-execution-report-2026-09-17.md` | Formal report (F1–F8, HC-0–HC-4) |
| `…/tiwas-adventure-red-box-solo-2026-09-17.md` (v1.1) | Adaptation module |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` (content v1.4) | Locked layer |
| `_consolidation/decision-register.md` | Ruled layer (DEC-001…142, incl. 072.A/077.A/140) |
| `…/tiwas-automated-playtest-run-conventions-2026-09-14.md` | H1–H7 conventions |
| `tsr01011b…v2.md` + `DnD - Basic Rules Boxed Set Adventure.md` | Research sources (beat skeleton only; never quoted) |
| `governance/authority.md`, `status-model.md`, `provenance.md`, `AGENTS.md` | Governance in force |

*End of NON-CANONICAL advisory complete-results handoff (v1.1).*
