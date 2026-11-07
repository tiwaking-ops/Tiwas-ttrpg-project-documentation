---
document:
  title: "Tiwas — BToV Full-Route Solo Playtest (¶1–60) — Complete Results Handoff Report to OpenCode"
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

# Tiwas — BToV Full-Route Solo Playtest (¶1–60): Complete Results Handoff to OpenCode

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
handoff pattern — e.g.,
`investigations/tiwas-btov-playtest-p1-p22-opencode-handoff-2026-09-17.md`) for the executed
seeded solo playtest of the **complete** *Beyond the Vale of Madness* adventure (¶1–60), run
2026-09-17 under the locked Core and the ruled DEC stack. Purpose: give OpenCode the full empirical
record — every resolution across all five PASS A attempts, the completing run's ledgers, the
treasure table, the award schedule, and the PASS B system-exercise pass — so downstream analysis
can proceed without re-running the harness.

Companion artifacts:

- Formal executed-run report:
  `investigations/tiwas-btov-full-route-playtest-p1-p60-report-2026-09-17.md`
- Raw log (authoritative record): 
  `investigations/tiwas-btov-full-route-playtest-p1-p60-raw-log-2026-09-17.json`
  (401 records; **403 test transactions** across six PCs, five seeds + one PASS B PC)
- Prior partial-route run (method baseline, seed 20260917):
  `investigations/tiwas-btov-opening-solo-playtest-p1-p22-report-2026-09-17.md`
- Prior handoff for that run:
  `investigations/tiwas-btov-playtest-p1-p22-opencode-handoff-2026-09-17.md`

## 2. Basis and method (condensed; full detail in the companion report)

- **Harness:** Python, single seeded RNG per run, d100 ∈ 1–100, `00 = 100`; corrected v2 engine
  (pay → overflow → recovery order from the start; the ¶1–22 v1 transaction-order bug never
  existed in this engine).
- **PC generation:** locked (Canonical §3–§5): 24 × 1d100 attributes; HP = Σ Body; MP = Σ Mind;
  PE = bep+bes+bee; MP Regen = mep+mes; Movement = floor((bsp+bss)/15). All skills at Starting
  Value = floor(Cap/2).
- **Route (PDF fork table):** #1→#12→#54→#27→#37→#32→#9→#49→#17(troll)→#21→#47→#43→#2→#14→#16→#24→#33→#23→#57→#55→#7→#38(BM)→#48/#56→#60.
- **Opponents (advisory, DEC-077.A working conversion v0.2 scratch):** Ice Troll HP **705**,
  PE 220, Regen 140, Icy Claws **67** (Tier 2) / Sharktoothed Maw **75** (Tier 2); Blood Man HP
  **650**, PE 175, Regen 110, Claws 65 (T2), Move-equivalent 9. **Blood Seep is NOT mechanized**
  (flagged in the scratch §1.5/§4); troll Regeneration/Regrowth and DR were not simulated. Both
  defenses 30 = advisory fiat (no ruled NPC-construction method; Canonical §15 reserves NPC
  construction).
- **Combat cap:** 12 exchanges per fight; cap-exit treated as disengage/withdraw (PDF-legal at
  both fights per #15/#21 and #46/#53) and logged **INCONCLUSIVE**, not victory.
- **Layer tags on every log record:** `locked` (Canonical v1.3) · `ruled` (DEC register) ·
  `locked+ruled` · `advisory` (unruled fiat, flagged) · `empirical` (ledger/summary).

## 3. Complete results

### 3.1 PASS A attempt outcomes (documented checkpoint policy: on PC death or route-failure
before #60, re-execute under the next sequential seed; all attempts logged)

| Seed | PC HP | Tracking skill | Outcome |
|---|---:|---:|---|
| 20260918 | 602 | 8 (+3) | **Failed #27 Tracking gate** — maze lost, RESCUER path unreachable |
| 20260919 | 734 | 1 (+3) | Failed #27 gate |
| 20260920 | 593 | 25 (+3) | Failed #27 gate |
| 20260921 | 445 | 4 (+3) | Failed #27 gate |
| **20260922** | **725** | **39 (+3)** | **Reached #60** — full route completed |

**Zero combat deaths across all five attempts** — every PASS A failure was the #27 skill gate.
(Run 1 of the ¶1–22 partial route, seed 20260917, remains the only combat death recorded across
the BToV executions.)

### 3.2 The completing run (seed 20260922) — verified HP ledger

Start 725 → troll fight end **573** → final at #60 **244**. The ledger closes exactly:

**725 − 266 (DEC-104 combat damage) − 213 (locked §7 Overflow) + 2 (bandaging) − 4 (scenario
flat costs #16/#55) = 244.**

| Fight | Exchanges | Foe HP | PC HP | Verdict |
|---|---:|---|---:|---|
| #17 Ice Troll | 12 (cap) | 705 → **611** (94 dealt) | 725 → 573 | **INCONCLUSIVE at cap** → disengage per PDF #15/#21 |
| #38 Blood Man | 12 (cap) | 650 → **548** (102 dealt) | 573 → 244 | **INCONCLUSIVE at cap** → withdraw per PDF #46/#53 |

**Conditions carried at #60:** 5 surviving Wound Effects, all Mag 3 (Head ×2, Legs ×3 — DEC-103:
T2 attack vs T1 defense → Shred +1; failed defenses → de-escalation 0; arithmetic hand-verified).
One DEC-103 negation also occurred (de-escalation floored a third application to 0).

### 3.3 Treasure table and award schedule (#60)

**Full table (PASS B census; 12 items, $1,450 total):** Glass dagger $50 · Silver tiara $300 ·
Antique mace $80 · Blue chemise $20 · Ice troll teeth $15 · Guard's signet ring $150 · Medium
bear shield $100 · Amethyst ring $200 · Maiden tapestry $100 · Axe tapestry $10 · Silver-glass
scepter $400 · Chariot toy $25.

| Item | Value ($) | Acquired in PASS A |
|---|---:|---|
| Amethyst ring (#32, from the rescued warrior) | 200 | ✔ |
| Ice troll teeth (#21) | 15 | ✔ |
| Glass dagger (#24) | 50 | ✔ (Deft success, no injury) |
| Maiden tapestry (#23→#51) | 100 | ✔ (Merchant failed; ST-14 carry check unmapped — one tapestry taken, advisory) |
| Antique mace (#2) | 80 | ✘ (Willpower failed — mace abandoned) |
| Silver-glass scepter (#56) | 400 | ✘ (unreachable — BM not slain) |
| **PASS A loot total** | **365** | below the $500 loot-bonus threshold |

**Awards (PDF #60 schedule, advisory conversion):** base 2 characters; monster bonus **0**
(none slain); loot bonus **0** ($365 ≤ $500) → **2 characters total**. RESCUER earned →
**+$500 silver talents + Martyrs of War invitation** (narrative; no currency system). GURPS
"characters" → Tiwas General XP conversion is unmapped; an advisory ×10 reading is flagged in
§6, not adopted.

**PASS B exercise (both branches, non-outcome):** max-route loot **$845** exceeds the $500
threshold → **4-character branch reachable in principle**. BM exercise fight (fresh PC, seed
20260925, HP 733): 12 exchanges, BM 650→553 (97 dealt), PC took 112; #58 Fright Check at −2
**failed** → Frightened M1 exercised under the DEC-094 advisory mapping.

### 3.4 Layer census (401 records)

locked 162 (40%) · ruled 146 · locked+ruled 27 · advisory 29 · empirical 37
(census sums to 401 ✓). Layer tags classify the authority basis each resolution drew from
(`locked` = Canonical v1.3; `ruled` = DEC register; `advisory` = unruled fiat, flagged;
`empirical` = ledger/summary) — every record remains part of this non-canonical advisory
log regardless of tag. The census is reported as logged; the handoff does not re-derive it.

## 4. Empirical findings (complete list; evidence, not rulings)

- **G1 — Neither boss fight is resolvable in 12 exchanges; the HP scale makes them practically
  unwinnable by attrition.** The PC dealt 94 HP in 12 exchanges vs the troll (≈7.8/exchange
  against a 705 pool → ~90 exchanges to kill) and 102 vs the BM (≈8.5 vs 650 → ~77 exchanges).
  Cause is structural: DEC-077.A conversions inflate creature HP ~43–47× the GURPS source
  (15 HP → 650–705) while DEC-104 damage is skill-margin scale (single digits to ~40). GURPS's
  15-HP fight becomes a multi-hundred-exchange siege. Run 1's PC death came from overflow, not
  foe damage — no starting-value PC has yet *lost* a Tiwas-converted boss fight to weapon
  damage, and none could *win* one either. The fights end by cap, gate, or resource collapse.
- **G2 — The #27 Tracking gate killed 4 of 5 runs — scenario gates dominate combat as the
  failure mode.** With Starting Value = Cap/2, a +3-difficulty gate needs effective skill ≈42,
  i.e., Cap ≈78+, which starting PCs reach only on high attribute draws (4/5 PCs had Tracking
  1–25). Under DEC-100's skill-side difficulty convention, a single required roll functions as a
  hard route filter. The adventure's "avoidable" fights are behind it.
- **G3 — Overflow remains the top single damage source but scales with pool size.** PASS A
  overflow 213 of 481 total HP lost (44%), versus run 1's 80% — because this PC's PE pool was
  164, not 68. The mechanism is pool-relative; lethality varies inversely with the attribute
  draw that also drives skills.
- **G4 — Every surviving wound is Mag 3** (T2 attacker vs T1 defense, failed defense):
  DEC-103's tier-shred makes wound magnitude near-constant across the run. Five accumulated
  wounds on one PC with no wound-severity/activation rules (Reserved) — their mechanical weight
  is currently nil beyond record-keeping.
- **G5 — The Fright Check maps and fires** (DEC-094 self-trigger extension, advisory): 1 failure
  in PASS A (#38, held — no effect on the fight's INCONCLUSIVE verdict), 1 failure in PASS B
  (#58 at −2). BM ran in light both times; the DARKNESS −3 branch went unexercised.
- **G6 — The award schedule resolves cleanly without a currency system** as long as the $500
  threshold is read narratively; but the monster bonus is unreachable under current combat scale
  (G1), so the schedule's middle branch is dead code in practice.
- **G7 — Blood Seep's absence matters:** the scratch explicitly did not mechanize it; the BM
  therefore lacks its signature grapple+corrode kill pattern. PASS B's BM fight (97 dealt / 112
  taken over 12 exchanges) is a shadow of the GURPS design. Any playtest conclusion about the BM
  is provisional on that flag.
- **G8 — Troll Regeneration/Regrowth and DR were not simulated** (no timescale mechanic, no
  armor layer — both flagged "not converted" upstream). The troll's effective 705 HP is
  therefore *conservative*: with freezing-condition regeneration it never bleeds down at all.

## 5. Harness-correction register (disclosed to OpenCode for assessment)

OpenCode is specifically asked to assess these, as the second assessor:

- **E1:** v1 of the ¶1–22 harness (transaction-order bug) remains superseded; this engine was
  built clean with pay → overflow → recovery order from the start.
- **E2:** Two defects in the *ad-hoc analysis* commands (not the engine): a path quirk
  (Windows-Python wrote the log to `C:\c\tmp\`) and a filter leak that initially double-counted
  PASS B's 112 damage into PASS A totals. Both caught by ledger reconciliation; reported
  corrected figures only (PASS A PC took 266, not 378).
- **E3:** Exchange-cap "INCONCLUSIVE" verdicts are a harness policy choice (PDF-legal
  disengagement), not a game outcome; flagged wherever used.
- **E4:** The ×10 XP reading of the award is an unadopted proposal; the schedule is otherwise
  executed as written.

## 6. Guesses I had to make

1. **Route policy** — fight-preferring, treasure-max, RESCUER path; legal per the PDF fork table
   (verified link-by-link). Confidence: high (legality), medium (representativeness).
2. **Cap-exit = disengage** at #17/#38 — PDF offers retreat/withdraw branches at both fights;
   mapping the harness cap to them is interpretive. Confidence: medium.
3. **Skill substitutions** — Willpower (mpe) for Will/Fright; Deft (bss) for DX tasks;
   Torch-tending (bse) for torch relight; Merchant (mps) for the #23 haggle; Willpower for the
   #2 mace lift. No canonical skill list exists; Tier-1 Cap-floor stand-ins chosen for
   determinism. Confidence: medium.
4. **Flat HP tokens** for 1d-4/1d-3 rolls (#16: 2, #55: 2, dagger-fail: 3) — deterministic
   advisory tokens; the PDF's variance is unmapped. Confidence: high of labeling, low of fidelity.
5. **×10 XP per GURPS "character"** — flagged as an unadopted proposal only; General XP's
   cost curve (current-value cost) makes the true conversion a designer question.
6. **Single-PC-per-seed anecdote discipline** — no distributional claims; G1/G2 attrition and
   gate-rate figures are arithmetic consequences of the logged exchanges, not Monte-Carlo
   estimates.

## 7. Open items surfaced for downstream work

1. NPC defense construction (combat-critical gap; options-brief candidate).
2. Overflow lethality vs low-Skill characters (design question for Tiwa; G3).
3. Creature advancement policy (Failure XP sink; troll's unruled Double from run 1).
4. DEC-135 parameter extraction (repeated-defense trigger; self-deficit values).
5. FP/hazard carrier for scenario costs (DEC-079/135 scaffolds exist, unmapped).
6. Blood Seep mechanization for the Blood Man (scratch-flagged, unresolved; G7).
7. Regeneration/Regrowth timescale and DR/armor layer (G8) — both reserved upstream, both
   material to the troll's true lethality.
8. Wound severity/activation rules (Reserved) — G4's five M3 wounds currently carry no weight.
9. GURPS "characters" → Tiwas General XP conversion for the #60 schedule (unmapped; §3.3).

## 8. Governance and authority boundary

This handoff does not rule, promote, demote, supersede, authorize, or reopen anything. All cited
rules remain at their existing status. Findings G1–G8, corrections E1–E4, and guesses 1–6 are
advisory evidence for the designer and OpenCode; no interpretation is silently resolved. The
companion raw log is the authoritative record of what the harness executed; where this summary
and the log disagree, the log wins.

## 9. Source register

| Source | Function |
|---|---|
| `investigations/tiwas-btov-full-route-playtest-p1-p60-raw-log-2026-09-17.json` | Verbatim 401-record log (seeds 20260918–20260922, 20260925) — authoritative record |
| `investigations/tiwas-btov-full-route-playtest-p1-p60-report-2026-09-17.md` | Companion formal executed-run report (method, findings G1–G8) |
| `investigations/tiwas-btov-opening-solo-playtest-p1-p22-report-2026-09-17.md` | Prior partial-route run (seed 20260917; method baseline) |
| `investigations/tiwas-btov-playtest-p1-p22-opencode-handoff-2026-09-17.md` | Prior handoff (house handoff format precedent) |
| `Beyond-the-Vale-of-Madness-GURPS.pdf` | Full route, #38/#48/#56, treasure table, #60 award schedule |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` | Locked layer (§2–§9, §13, §14.1, §15) |
| `_consolidation/decision-register.md` | Ruled layer (DEC-094/097/100/103/104/105/110/135; DEC-077.A; DEC-078 A2 convention) |
| `investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md` | Advisory creature content incl. the Blood Seep / DR / Regen flags |

*End of NON-CANONICAL advisory complete-results handoff.*
