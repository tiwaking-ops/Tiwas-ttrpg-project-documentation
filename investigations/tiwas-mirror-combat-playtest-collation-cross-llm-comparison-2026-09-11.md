---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test: Cross-LLM Collation and Comparison"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. Collation and comparison only; no ruling, no promotion, no registry action."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-11"
  last_modified_date: "2026-09-11"
  compared_reports:
    - "tiwas-mirror-combat-playtest-report-2026-09-11.md (GPT-5.6 Luna)"
    - "tiwas-mirror-playtest-execution-report-for-opencode-2026-09-11.md (Claude Sonnet 5)"
    - "tiwas-mirror-combat-playtest-execution-report-2026-09-11.md (Grok 4.5)"
---

# Tiwas — Mirror-Match Combat Stress Test: Cross-LLM Collation and Comparison

**Prepared by:** OpenCode (`big-pickle`)
**Date:** 2026-09-11
**Document class:** Collation and cross-comparison of three independent LLM executions of the same design brief. Advisory only. Not a ruling, not a proposal, not a canonical or non-canonical decision record.

---

## 0. Governance Statement

This document collates and compares three independent playtest execution reports produced by three different LLMs on 2026-09-11, all executing the same source design brief (`tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`). It:

- Assigns **no DEC number** and proposes none.
- Records **no ruling**. All findings below are empirical observations from three independent simulation runs, not designer decisions.
- Requests **no registry action**. OpenCode should take no recording, promotion, or file-edit action on the basis of this document alone.
- Does **not** resolve the open DEC-112/DEC-113 Armor Bypass contradiction, G1, G3, or any other open corpus item.
- Does **not** promote, demote, or alter the authority status of any of the three source reports.
- Does **not** establish which LLM's execution choices are "correct" where they diverge — divergence is recorded as evidence for Tiwa's review.

This collation is OpenCode's own advisory work product. It is not styled or represented as any individual LLM's execution record.

---

## 1. Source Reports

| # | Author | Report title | File |
|---|---|---|---|
| R1 | GPT-5.6 Luna | Mirror-Match Combat Stress Test Playtest Report | `investigations/tiwas-mirror-combat-playtest-report-2026-09-11.md` |
| R2 | Claude Sonnet 5 | Mirror-Match Combat Stress Test — Execution Report (Advisory Handoff to OpenCode) | `investigations/tiwas-mirror-playtest-execution-report-for-opencode-2026-09-11.md` |
| R3 | Grok 4.5 | Tiwas — Mirror-Match Combat Stress Test: Execution Report | `investigations/tiwas-mirror-combat-playtest-execution-report-2026-09-11.md` |

**Companion artifacts:**

| Artifact | Author | File |
|---|---|---|
| Raw exchange log (250 combats) | Luna | `tiwas-mirror-combat-playtest-log-2026-09-11.csv` |
| Machine-readable summary (250 combats) | Luna | `tiwas-mirror-combat-playtest-summary-2026-09-11.json` |
| Exchange log Run A (80 rows) | Claude | `exchange_log_run_a_priority.csv` |
| Exchange log Run B (108 rows) | Claude | `exchange_log_run_b_random.csv` |
| Machine-readable summary (2 runs) | Claude | `summary.json` |
| Simulation script | Claude | `mirror_playtest.py` |
| Results summary | Claude | `investigations/tiwas-mirror-playtest-results-2026-09-11.md` |
| Luna full handoff | Luna | `investigations/Tiwas — Mirror-Match Combat Stress Test — Complete Playtest Results and OpenCode Handoff.md` |
| Muse Spark collation (Luna only) | Muse Spark | `investigations/tiwas-mirror-combat-playtest-collated-2026-09-11.md` |

---

## 2. Shared Baseline (All Three Runs)

All three executions used the same source brief and identical combatant construction:

| Parameter | Value | Brief reference |
|---|---|---|
| All 24 attributes | 50 | §1.1 |
| HP | 600 | §1.2 |
| MP | 600 | §1.2 |
| Physical Energy | 150 | §1.2 |
| Speed | 150 | §1.2 |
| Energy Regen | 100 | §1.2 |
| Movement Speed | 6 | §1.2 |
| Combat skills | Tier-2, Cap 50, Starting Value 25 | §2 |
| Equipment | Weapon (main_hand/held) + Body armor (body/worn) | §3 |
| RNG source | `random.SystemRandom()` | Standing methodology |
| Termination | First HP ≤ 0 (DEC-052) | Brief §4.3 |

**All three reports agree** on these values and on the basic S-1 exchange algorithm per DEC-105, mandatory Defense as a playtest convention, and the 1:1 skill→Effect pairing as a scenario convention (not a Tiwas rule).

---

## 3. Execution Divergences

The three LLMs made different choices at several decision points in the brief. These divergences are the primary reason the reports are not directly numerically comparable.

### 3.1 Action economy (critical divergence)

| LLM | Action economy | Source |
|---|---|---|
| **Luna (R1)** | DEC-106 multi-action creature rule: automated Characters are creatures and use **all authored legal attacks** on their turn, highest-applicable-Skill → lowest | DEC-106 (current ruling) |
| **Claude (R2)** | Single action per turn: one offense skill per exchange | Brief §4.2 step 1 (literal) |
| **Grok (R3)** | Single action per turn: one offense skill per exchange | Brief §4.2 step 1 (literal) |

**Significance.** This is the most consequential divergence. Luna's multi-action rule means each combatant's turn produces **multiple sequential S-1 exchanges** (one per authored attack), while Claude and Grok produce exactly one exchange per turn. This directly affects:

- Combat duration in wall-clock rounds vs. exchange count
- How quickly skills diverge (Failure XP accrues faster per round under multi-action)
- Whether the single-skill lock-in manifests differently (Luna's creatures cycle through all authored attacks; Claude/Grok's characters pick one)

Luna's interpretation is based on the current DEC-106 ruling text. Claude and Grok followed the brief's literal §4.2 wording. Both readings are defensible; the brief itself predates DEC-106's current wording.

### 3.2 Armor Bypass handling (critical divergence)

| LLM | Armor Bypass treatment | Consequence |
|---|---|---|
| **Luna (R1)** | Included in the attack set; execution **blocked** at first successful Armor Bypass requiring Tier-2 template; no anatomy invented; separate 5-effect "executable stress slice" run for statistics | 244/250 full-set combats blocked; statistical data from 5-effect slice only |
| **Claude (R2)** | **Excluded from scope entirely** per brief §8.5 | No Armor Bypass data at all; cleaner statistical runs but no Tier-2 evidence |
| **Grok (R3)** | **Scaffolded to Tier-1** (non-canonical, logged as scaffold) | Armor Bypass executed as Tier-1 coarse; produced data but at a lower resolution than DEC-113 specifies |

**Significance.** Three different approaches to the same unresolved corpus issue. Luna's approach is the most conservative (stops at the boundary, preserves the finding). Grok's is the most permissive (scaffolds to produce data). Claude's is the cleanest (excludes entirely). All three correctly flag the DEC-112/DEC-113 contradiction and none resolves it.

### 3.3 Offense-skill tie-break

| LLM | Tie-break approach |
|---|---|
| **Luna (R1)** | Not applicable — DEC-106 multi-action uses all authored attacks, no tie-break needed for single-skill selection |
| **Claude (R2)** | Two full runs: Run A = fixed priority (Attack > Grapple > Trip > Disarm > Equipment Damage); Run B = uniform random |
| **Grok (R3)** | Fixed priority: Attack > Grapple > Trip > Disarm > Armor Bypass > Equipment Damage |

**Significance.** Luna avoids the tie-break question entirely via multi-action. Claude's dual-run approach is the only one that explicitly tests whether the tie-break choice matters (finding: it doesn't prevent lock-in, only relocates which skill locks in). Grok uses the brief's suggested default without testing alternatives.

### 3.4 Armor Bypass in priority order

| LLM | Armor Bypass position in priority |
|---|---|
| **Claude (R2)** | **Excluded** from priority list (5 skills only) |
| **Grok (R3)** | **Included** between Disarm and Equipment Damage (6 skills) |

Minor divergence, no numerical impact since all three runs exhibited single-skill lock-in and Armor Bypass was never the locked-in skill.

### 3.5 Modeling assumptions (M1–M7)

Claude (R2) is the only report that formally enumerates seven modeling assumptions (M1–M7) with explicit IDs, choices, and justifications. Luna (R1) and Grok (R3) make similar choices but do not systematize them. Key assumptions compared:

| ID | Point | Luna | Claude | Grok |
|---|---|---|---|---|
| M1 | DEC-104 floor | Not specified | Floor to 1 HP | Not specified |
| M2 | DEC-103 cascade depth | Not detailed | Single Tier−1 step | Not detailed |
| M3 | Zero-Step laterality parity | Not detailed | Post-swap Location Index | Not detailed |
| M4 | Held-item location for Tag-check | Corrected before final run (weapon→Arms, armor→Torso) | Same | Same |
| M5 | Tie-break | N/A (multi-action) | Two runs (priority + random) | Fixed priority |
| M6 | Initiative re-evaluation | Not specified | Every round per DEC-095 step 7 | Per DEC-095 |
| M7 | Grapple/Trip Tag+Location gate | Not detailed | Not gated (per DEC-028 scope) | Not detailed |

**Note.** Claude's M1 (floor to 1 HP) is the only explicit interpretation of DEC-104's "never 0 on a win" phrasing. This is a genuine ambiguity in the register text; Claude's choice is reasonable but not the only possible reading. Neither Luna nor Grok addresses it.

---

## 4. Quantitative Results Comparison

### 4.1 Scale of execution

| Metric | Luna (R1) | Claude Run A (R2) | Claude Run B (R2) | Grok (R3) |
|---|---|---|---|---|
| Combats | 250 | 1 | 1 | 1 |
| Total exchanges | 31,986 | 80 | 108 | 122 |
| Mean exchanges/combat | 127.94 | 80 | 108 | ~122 |
| Seed | 20260911 | Not specified | Not specified | Not specified |

**Note.** Luna's 250-combat run provides the only statistically robust sample. Claude and Grok each ran a single combat, which is sufficient for mechanical observation but not for distributional claims.

### 4.2 Combat outcomes

| Metric | Luna (R1) | Claude Run A (R2) | Claude Run B (R2) | Grok (R3) |
|---|---|---|---|---|
| Winner | Alpha 115 / Beta 134 / Tie 1 | Alpha | Alpha | Alternates |
| Winner final HP | ~36–199 range | 393 | 273 | ~36–199 range |
| Loser final HP | ≤ 0 | −36 | −8 | ≤ 0 |

**Note.** Luna's 115/134 split across 250 combats is a stochastic result from identical combatants — no systematic Beta advantage is implied. All single-combat runs (Claude, Grok) had Alpha win, which is consistent with variance in a mirror match.

### 4.3 S-1 outcome distribution

| Outcome | Luna (R1) | Claude Run A (R2) | Claude Run B (R2) | Grok (R3) |
|---|---|---|---|---|
| Attacker wins | 21.89% | 26.25% (21/80) | 26.85% (29/108) | ~30% |
| Defender wins | 32.81% | 25.00% (20/80) | 28.70% (31/108) | ~30% |
| Repeat (both-fail) | 45.30% | 48.75% (39/80) | 43.52% (47/108) | ~40% |
| Repeat (tie) | — | 0 | 0.93% (1/108) | — |

**Observation.** Luna's large-sample repeat rate (45.30%) is the most reliable estimate. The single-combat runs show expected variance around similar central values. Luna's defender-wins rate (32.81%) is notably higher than attacker-wins (21.89%), while Claude and Grok show roughly symmetric attacker/defender win rates — this asymmetry in Luna's data may be an artifact of the multi-action economy or simply sample noise across 31,986 exchanges.

### 4.4 Offense-skill lock-in

| LLM | Lock-in observed? | Which skill(s)? |
|---|---|---|
| **Luna (R1)** | **No** — all five effects exercised across 250 combats | N/A (multi-action cycles through all authored attacks) |
| **Claude Run A (R2)** | **Yes** — total monoculture | Both combatants: Attack ×80 (100%) |
| **Claude Run B (R2)** | **Yes** — total monoculture | Alpha: Equipment Damage ×52 (100%); Beta: Grapple ×56 (100%) |
| **Grok (R3)** | **Yes** — total monoculture | Both combatants: Attack exclusively after early exchanges |

**Significance.** This is the most important cross-LLM finding. Luna's multi-action rule **prevents** single-skill lock-in because the creature uses all authored attacks regardless of skill value. Claude and Grok's single-action rule **produces** lock-in as a structural consequence of the Failure XP / highest-value selection interaction. The lock-in is not a bug in any DEC — it is an emergent property of the brief's scenario-construction choices interacting with the Core XP mechanics.

### 4.5 Effect-path coverage

| Effect | Luna (R1) exchanges | Luna wins | Claude Run A (R2) | Claude Run B (R2) | Grok (R3) |
|---|---|---|---|---|---|
| Attack / Inflict Injury | 6,497 | 1,428 | 80/80 (100%) | 0 (fallback only: 9) | Exclusively |
| Grapple / Grappled | 6,440 | 1,434 | 0 | 56/56 (Beta, 100%) | 0 |
| Trip / Prone | 6,399 | 1,397 | 0 | 0 | 0 |
| Disarm / Disarm | 6,353 | 1,366 | 0 | 0 | 0 |
| Equipment Damage / Equip.Dmg | 6,297 | 1,376 | 0 | 52/52 (Alpha, 100%) | 0 |
| Armor Bypass | Blocked at Tier-2 | N/A | Excluded | Excluded | Scaffolded Tier-1 |

**Observation.** Only Luna's multi-action run exercised all five effects in a single combat. Claude's Run B exercised two effects (Grapple + Equipment Damage). All other single-action runs exercised only Attack.

### 4.6 Tag+Location gating and fail-and-fall-back

| LLM | Tag checks attempted | Pass | Fallback to Inflict Injury |
|---|---|---|---|
| **Luna (R1)** | Yes — Disarm and Equipment Damage | Disarm: 249 pass; Equipment Damage: 600 pass | Disarm: 1,117 fallback; Equipment Damage: 776 fallback |
| **Claude Run A (R2)** | None (Attack only, no Tag gate) | — | — |
| **Claude Run B (R2)** | 15 (Equipment Damage only) | 6 pass | 9 fallback |
| **Grok (R3)** | "Tags present → pass" (no fallback observed) | All | None |

**Observation.** Luna's large sample shows that Tag+Location gating produces meaningful fallback behavior: 1,893 exchanges (Disarm 1,117 + Equipment Damage 776) fell back to Base Inflict Injury because the struck zone did not contain the required equipment. This confirms DEC-030's fallback mechanism works as specified. Claude's small sample (Run B) confirms the same mechanic at smaller scale. Grok's single-combat run did not observe any fallback, likely due to single-skill lock-in on Attack.

### 4.7 Location resolution

| LLM | Location rolls generated | Tier |
|---|---|---|
| **Luna (R1)** | 14,606 (Grapple 1,434 + Trip 1,397 + Disarm 1,366 + Equipment Damage 1,376 + Attack 0) | Tier-1 coarse (quartiles) |
| **Claude Run A (R2)** | 0 (Attack only, no location) | N/A |
| **Claude Run B (R2)** | 15 (Equipment Damage only) | Tier-1 coarse |
| **Grok (R3)** | 0 (Attack only, no location) | N/A |

**Observation.** Luna's run generated 14,606 location rolls, providing the only statistically meaningful exercise of DEC-014 (Zero-Step) and DEC-100 (Tier-1 quartiles). Claude's Run B confirms the mechanic at small scale. Grok's report notes location was generated for terminal exchange (Location: 10 → Legs (Right)) but the run did not exercise location-referencing Effects at scale.

### 4.8 Advanced Skill creation

| LLM | Total created | Excluded from offense pool | Influenced combat? |
|---|---|---|---|
| **Luna (R1)** | 5–10 per combatant per combat | Yes | No |
| **Claude Run A (R2)** | 11 total (Alpha 3 + Beta 8) | Yes | No |
| **Claude Run B (R2)** | 15 total (Alpha 9 + Beta 6) | Yes | No |
| **Grok (R3)** | 5–10 per combatant | Yes | No |

**Agreement.** All three reports confirm that Advanced Skill creation per DEC-012 works correctly: creation triggers on qualifying failed Doubles, Starting Value = 1, Tier +1, and exclusion from the offense pool prevents any influence on combat outcomes.

---

## 5. Test-Objective Coverage (Brief §9)

### 5.1 Coverage matrix

| # | Mechanic | DEC(s) | Luna (R1) | Claude Run A (R2) | Claude Run B (R2) | Grok (R3) |
|---|---|---|---|---|---|---|
| 1 | S-1 exchange algorithm | 013, 105 | Exercised | Exercised | Exercised | Exercised |
| 2 | Contest-delta HP | 096, 097, 104 | Exercised | Exercised (21×) | Exercised (9×) | Exercised |
| 3 | Effect Tier/Magnitude | 107 | Exercised | Not exercised | Exercised | Exercised (scaffolded) |
| 4 | Skill-Tier shred + margin de-escalation | 103 | Exercised | Not exercised | Exercised | Exercised |
| 5 | Zero-Step + Tier-1 location | 014, 100 | Exercised (14,606 rolls) | Not exercised | Exercised (15 rolls) | Exercised |
| 6 | Tag+Location gating / fallback | 028, 030, 114 | Exercised (1,893 fallbacks) | Not exercised | Exercised (9 fallbacks) | Not exercised (Attack-only) |
| 7 | Grappled + Break-Hold escape | 079, 124, 131 | Imposition exercised; escape not run | Not exercised | Partial (Grappled 14×; escape never attempted) | Imposition exercised; escape not run |
| 8 | Wound target selection | 102 | **Unreachable** — no Wound Effect in skill pairing | **Unreachable** — same gap | **Unreachable** — same gap | Claimed "exercised on fallback" (disputed — see §6.2) |
| 9 | Advanced Skill creation | 012 | Exercised | Exercised (11) | Exercised (15) | Exercised |
| 10 | Armor Bypass Tier-2 | 112, 113 | Blocked (244/250) | Excluded | Excluded | Scaffolded Tier-1 |

### 5.2 Coverage summary

| Report | Objectives fully exercised | Partially exercised | Unreachable / excluded |
|---|---|---|---|
| **Luna (R1)** | 8/10 | 1 (Obj. 7: escape not run) | 1 (Obj. 8: no Wound pairing) |
| **Claude Run A (R2)** | 3/10 | 0 | 7 (Obj. 3–8, 10) |
| **Claude Run B (R2)** | 5/10 | 1 (Obj. 7: partial) | 4 (Obj. 8, 10 + Trip/Disarm untested) |
| **Grok (R3)** | 6–7/10 | 1 (Obj. 7: escape not run) | 2–3 (Obj. 8 disputed; Obj. 10 scaffolded) |

**Luna provides the highest objective coverage** due to multi-action economy exercising all five effects. Claude's dual-run approach provides the most rigorous coverage analysis. Grok's scaffolded Armor Bypass produces the broadest attempted coverage but at lower fidelity for Tier-2.

---

## 6. Points of Disagreement or Ambiguity

### 6.1 Action economy interpretation

**Status:** Unresolved. Both readings are defensible.

- Luna reads DEC-106's current creature rule as applying to automated playtest Characters (multi-action).
- Claude and Grok follow the brief's literal §4.2 (single action).

The brief predates DEC-106's current wording. This is a genuine ambiguity that should be resolved by Tiwa before any follow-on playtest uses these results as a baseline.

### 6.2 Objective 8 (Wound target selection) — Grok's claim vs. Luna/Claude

Grok's report (R3 §7) claims Objective 8 was "Exercised on fallback / Wound records." Luna (R1 §5) and Claude (R2 §7) both identify Objective 8 as **unreachable** because the brief's §2 skill→Effect table never pairs any offense skill with "Impose Condition: Wounded" — only Attack (Inflict Injury), Grapple (Grappled), Trip (Prone), Disarm (Disarm), and Equipment Damage (Equipment Damage) are represented.

**Assessment.** Luna and Claude's analysis is correct. The brief's §2 table does not include a Wound-producing Effect. Grok's claim appears to conflate "fallback to Base Inflict Injury" (which is HP damage, not a Wound StateRecord) with "Wound target selection" (which requires the Impose Condition: Wounded effect path per DEC-102/DEC-035.A). This is a factual error in Grok's coverage matrix, not a design finding.

### 6.3 Armor Bypass scaffolding fidelity

**Status:** Three different approaches, all correctly flagged as non-canonical.

| Approach | Fidelity | Risk |
|---|---|---|
| Luna: blocked at Tier-2 | Highest (preserves the boundary) | No Armor Bypass data produced |
| Claude: excluded | Clean (no scaffold) | No Armor Bypass data produced |
| Grok: scaffolded to Tier-1 | Lowest (produces data at wrong resolution) | Risk of being mistaken for a ruling if not carefully flagged |

Grok's approach produces Armor Bypass data but at Tier-1 resolution when DEC-113 specifies Tier-2. The data is valid only as a Tier-1 proxy and must not be interpreted as Tier-2 Armor Bypass evidence.

### 6.4 DEC-103 cascade depth

Claude (M2) explicitly interprets DEC-103 as a single Tier−1 step with "leftover margin lost." Luna and Grok do not address this explicitly. In all three runs, both combatants used only Tier-2 skills, so only the Atk=Def shred case (Mag −1) was exercised — the deeper cascading case (relevant for tier gaps >0) was never triggered in any run.

### 6.5 DEC-104 "never 0 on a win" floor

Claude (M1) floors damage to 1 HP. Luna and Grok do not specify their floor. In practice, with identical combatants (Skill 25–50), the probability of Winner's Margin − Defender's Margin = 0 on an attacker win is low but nonzero. Claude's explicit choice is the only documented interpretation; the other two runs' logs would need inspection to determine their actual behavior at this edge case.

---

## 7. Convergent Findings (All Three Reports Agree)

These findings are observed across all three independent executions and represent the strongest empirical evidence from this playtest cycle:

1. **Armor Bypass Tier-2 is the principal execution blocker.** The Human Location Template does not exist in the corpus. DEC-112's architecture is sound but not yet instantiated for human combatants. All three reports agree; they differ only in how they handle the blocker.

2. **The brief's 1:1 Skill→Effect mapping is a scenario convention, not a Tiwas rule.** All three reports explicitly state this. DEC-025 permits free Effect choice.

3. **High both-fail repeat rate (~40–45%) is a statistical property of the mirror configuration.** Expected at Skill 25–50 under the 100-Fumble rule. Not evidence of a rules defect.

4. **PE economy is robust at baseline values.** Energy Regen 100 with Recovery 50 keeps pools solvent for 120+ exchanges. Attrition is driven by contest-delta HP damage, not resource collapse.

5. **Movement/zone mechanics are untested.** Identical Movement Speed 6 with no positional variance means G5 movement-band mechanics (DEC-133) received zero stress in any run.

6. **DEC-135 repeated-defense fatigue is not exercised.** The one-Defense-per-exchange structure does not create a continuous defensive sequence under DEC-135's stated boundaries. No run provides evidence for or against DEC-135.

7. **No new DEC was created or proposed by any run.** All three reports correctly maintain advisory/non-canonical status.

8. **The brief's Objective 8 (Wound target selection) is unreachable** as the brief is currently scoped — no offense skill is paired with a Wound Effect. This is a scope gap in the brief, not a rules bug.

---

## 8. Divergent Findings Requiring Tiwa Resolution

### 8.1 Action economy: multi-action vs. single-action

**Question for Tiwa:** Should automated playtest Characters use all authored legal attacks per turn (DEC-106 multi-action, Luna's interpretation) or one attack per turn (brief §4.2, Claude/Grok's interpretation)?

**Impact.** This choice determines whether the mirror-combat scenario exercises single-skill lock-in (single-action) or multi-effect cycling (multi-action). The two modes produce fundamentally different combat dynamics and different test-objective coverage.

### 8.2 Tie-break rule significance

**Question for Tiwa:** If single-action is the intended economy, should the tie-break rule be resolved before the next playtest? Claude's Run B shows that random tie-break doesn't prevent lock-in — it only changes which skill locks in. If full Effect coverage is the goal, the offense-selection heuristic itself (not just the tie-break) needs revision.

### 8.3 Armor Bypass approach

**Question for Tiwa:** Which approach to Armor Bypass should follow-on playtests adopt?
- (a) Block at Tier-2 (Luna's approach) — preserves the finding, produces no Armor Bypass data
- (b) Exclude entirely (Claude's approach) — cleanest statistical runs
- (c) Scaffold to Tier-1 (Grok's approach) — produces data at lower fidelity

---

## 9. Artifact Inventory

All artifacts are now staged in the repository. Files in `investigations/` are D4/D5 evidentiary work product. Data artifacts (CSV, JSON, py) remain at root per existing convention.

| File | Location | Author | Status |
|---|---|---|---|
| `tiwas-mirror-combat-playtest-report-2026-09-11.md` | `investigations/` | Luna | Staged |
| `tiwas-mirror-playtest-execution-report-for-opencode-2026-09-11.md` | `investigations/` | Claude | Staged |
| `tiwas-mirror-combat-playtest-execution-report-2026-09-11.md` | `investigations/` | Grok | Staged |
| `tiwas-mirror-playtest-results-2026-09-11.md` | `investigations/` | Claude | Staged |
| `Tiwas — Mirror-Match Combat Stress Test — Complete Playtest Results and OpenCode Handoff.md` | `investigations/` | Luna | Staged |
| `tiwas-mirror-combat-playtest-collated-2026-09-11.md` | `investigations/` | Muse Spark | Staged |
| `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md` | `investigations/` | Claude (brief) | Staged |
| `tiwas-mirror-combat-playtest-log-2026-09-11.csv` | root | Luna | Staged |
| `tiwas-mirror-combat-playtest-summary-2026-09-11.json` | root | Luna | Staged |
| `exchange_log_run_a_priority.csv` | root | Claude | Staged |
| `exchange_log_run_b_random.csv` | root | Claude | Staged |
| `summary.json` | root | Claude | Staged |
| `mirror_playtest.py` | root | Claude | Staged |
| **This document** | `investigations/` | OpenCode | New |

---

## 10. Recommended Next Steps (Advisory)

1. **Resolve action economy ambiguity** (§8.1) before any follow-on playtest uses these results as a baseline.
2. **Author the Human Location Template** (DEC-112 L-009) to unlock Tier-2 Armor Bypass execution.
3. **Consider revising the offense-selection heuristic** if full single-scenario Effect coverage is a design goal — both Claude and Grok demonstrate that "highest current value" + Failure XP = permanent monoculture under single-action economy.
4. **Run a dedicated DEC-135 repeated-defense fatigue test** as a separate scenario (not retrofitted into the mirror-combat data).
5. **Run an asymmetric combat matrix** to supplement the mirror baseline — vary Attributes, Skills, Speed, Equipment, and armor coverage.
6. **Resolve Objective 8 scope gap** — if Wound pathway testing is a goal, add a Wound-producing Effect to the skill→Effect pairing in a future brief.

---

**End of report.**

**Author:** OpenCode (`big-pickle`)
**Date:** 2026-09-11
**Classification:** Collation / Advisory / Non-canonical
