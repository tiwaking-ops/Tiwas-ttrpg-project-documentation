# Tiwas TTRPG — Ice Troll Combat Playtest v3: Cross-Report Synthesis

```yaml
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
  source_documents:
    - "tiwas-ice-troll-playtest-v3-FINAL-REPORT-2026-09-04.md"
    - "Tiwas TTRPG — Ice Troll Combat Playtest v3-Unedited Playtest Execution Results.md"
    - "Tiwas TTRPG — Ice Troll Combat Playtest v3.md"
    - "tiwas-ice-troll-playtest-v3-LIVE-LOG-2026-09-04.md"
    - "Tiwas TTRPG — Ice Troll Combat Playtest (v3) Execution-grok2.md"
    - "tiwas-ice-troll-playtest-v3-cross-model-synthesis-2026-09-04.md"
```

## 1. Document Purpose

This document compares, contrasts, collates, and synthesizes the available playtest execution reports for the Tiwas TTRPG Ice Troll Combat Playtest v3. Its purpose is to improve future playtests by identifying:

- Execution methodology differences between LLM implementations
- Outcome variations and their causes
- System gaps surfaced by both executions
- Recommendations for prompt refinement and rule clarification

**Authority status:** This is a playtest analysis document. It does not create new canonical rules, DEC numbers, or system decisions. All findings require human confirmation before promotion.

---

## 2. Source Document Inventory

| Document | Author | Type | Rounds | Final PC HP | Status |
|---|---|---|---:|---:|---|
| Final Report | Claude Sonnet 5 | Summary report | 18 | 0 | Complete |
| Live Combat Log | Claude Sonnet 5 | Execution log | 18 | 0 | Complete |
| Unedited Execution Results | GPT-5.6 Luna | Execution record | 20 | −29 | Complete |
| Action-Selection Decision | GPT-5.6 Luna | Finding/gap analysis | 20 | −29 | Complete |
| Execution Log + Final Report | Grok 4.5 (xAI) | Step-by-step execution + summary | 20 | 0 | Complete |

---

## 3. Execution Comparison

### 3.1 Combat Parameters

All three executions used identical:

- **Adventurer-1 stat block:** 24 attributes at 50, HP 600, PE 150, Speed 150, all Tier-1 skills at 25 (Cap 50), Attack2/Defence2 at 25 (Cap 50) via DEC-012 exception
- **Ice Troll stat block:** HP 705, PE 220, Speed 175, Icy Claws 67, Sharktoothed Maw 75, Brawling 37
- **Initiative:** Ice Troll (175) → Adventurer-1 (150)
- **Frightened condition:** Tier-1, −1 to all Skills on Adventurer-1, full duration

### 3.2 Attack Selection — Critical Divergence (Governance Failure)

| Parameter | Claude Sonnet 5 | GPT-5.6 Luna | Grok 4.5 |
|---|---|---|---|
| Round 1 Troll attack | Icy Claws | Sharktoothed Maw | Icy Claws |
| Attack selection method | Alternated between attacks | Fixed on Sharktoothed Maw | Alternated between attacks |
| Icy Claws usage | 9 of 18 Troll turns | 0 of 20 Troll turns | 10 of 20 Troll turns |
| Sharktoothed Maw usage | 9 of 18 Troll turns | 20 of 20 Troll turns | 10 of 20 Troll turns |
| Flagged as gap/scaffold? | No — alternation applied silently | **Yes — separate companion document, GM-stop, Q1–Q3 escalated** | No — alternation applied silently |

**Governance finding:** All three executing LLMs hit the identical decision point — the Ice Troll has two legal Tier-2 attacks and nothing in the corpus says which one it uses — and handled it three different ways. Two of three executions (Claude, Grok) violated the prompt's own governing instruction ("You never invent a rule to smooth over a gap... Where the corpus is silent and no rule or scaffold is pre-authorized below, you stop and flag the human monitor") without logging it as either a scaffold or a GM-stop. GPT-5.6 Luna's separate companion document is the only source document that correctly identifies this as **SC-XX, a genuine open system gap**, and the only execution that visibly paused for it.

**However:** GPT-5.6's handling was also imperfect — it correctly stopped once, obtained a one-time explicit instruction ("Sharktoothed Maw"), then silently generalized that single-round answer into a 20-round default without flagging that generalization.

This is not resolved by any existing DEC. DEC-095 (SC-04) governs *turn order*, not *action choice among multiple legal actions*.

### 3.3 Outcome Comparison

| Metric | Claude Sonnet 5 | GPT-5.6 Luna | Grok 4.5 |
|---|---|---|---|
| Total rounds | 18 | 20 | 20 |
| PC final HP | 0 | −29 | 0 (shown as "−11 → 0", clamped) |
| Troll final HP | 610/705 | 583/705 | 641/705 |
| Troll HP damage taken | 95 | 122 | 64 |
| PC HP damage taken | 600 | 629 | 600 |
| PC incapacitation round | 18 | 20 | 20 |
| Active Defense successes | Multiple (0–24 mitigation) | Multiple (varied) | Multiple (0/5/8/9/11/17 mitigation) |
| Overflow events | Yes (PE depletion) | Yes (PE depletion) | None observed |
| Advanced Skill creations | 6 (4× PC, 2× Troll) | Not detailed | None triggered |
| HP floor convention | 0 (arithmetic landed exactly on 0) | **−29 (uncapped)** | 0 (clamped, pre-clamp preserved) |

### 3.4 Round Count and Outcome Analysis

The differences across executions stem from:

1. **Attack selection:** GPT-5.6's exclusive use of Sharktoothed Maw (Skill 75) vs Claude/Grok's alternating pattern produced different damage distributions
2. **Roll variance:** Different random seeds produced different margins — Grok's rolls were generally lower-margin in Troll attacks, resulting in less total PC damage (600 vs 629 for GPT-5.6)
3. **Active Defense outcomes:** Different mitigation results affected HP trajectories — Grok observed successful Active Defense with mitigations of 5, 8, 9, 11, and 17
4. **Overflow events:** Claude observed Overflow-to-HP damage in mid-combat; Grok's full 20 rounds showed no Overflow (all Costs stayed within PE pools)
5. **Advanced Skill creation:** Claude observed 6 Advanced Skill creations via failed Doubles; Grok observed none — this is roll-variance dependent, not a rule difference
6. **HP floor convention:** GPT-5.6 recorded −29 (uncapped); Grok clamped to 0 but preserved pre-clamp value; Claude landed exactly on 0 (clamping untested)

**Key observation:** Both Claude and Grok ended with PC HP exactly 0 (incapacitated per DEC-052). GPT-5.6 overshot to −29. All three are valid outcomes under the same rules, but the HP floor convention affects comparability of final records.

**Conclusion:** All three executions are valid instances of the same rules. The variance demonstrates normal playtest variance, not rule interpretation differences.

---

## 4. Rule Validation Matrix

All three executions tested the same DEC-094–DEC-101 rulings. Validation status:

| DEC | Rule | Claude Validated | GPT-5.6 Validated | Grok Validated | Consensus |
|---|---|---|---|---|---|
| DEC-094 | Passive Frightened (scene-state) | Yes — full 18 rounds | Yes — full 20 rounds | Yes — full 20 rounds | **Confirmed** |
| DEC-095 | Combat sequencing / initiative | Yes — fixed order, no ties | Yes — fixed order, no ties | Yes — fixed order, no ties | **Confirmed** |
| DEC-096 | Inflict Injury = Winner's Margin | Yes — deterministic | Yes — deterministic | Yes — deterministic | **Confirmed** |
| DEC-097 | Active Defense = Defender's Margin | Yes — 0/2/4/10/17/24 observed | Yes — varied mitigation | Yes — 0/5/8/9/11/17 observed | **Confirmed** |
| DEC-098 | Creature default defensive skill = Brawling | Yes — 37→45 via XP | Yes — 37→? (not detailed) | Yes — 37 (no XP change observed) | **Confirmed** |
| DEC-099 | Quality ≥1 Base / ≥10 Gated | Yes — checked on every win | Yes — checked on every win | Yes — checked on every win | **Confirmed** |
| DEC-100 | Location Tier-1 quartile split | Yes — exercised once (Round 1) | Not explicitly detailed | Not exercised (Injury only) | **Partially confirmed** |
| DEC-101 | Defender-wins = no counter-Effect | Yes — consistent | Yes — consistent | Yes — consistent | **Confirmed** |

**Consensus:** 7 of 8 rulings fully confirmed by all three executions. DEC-100 (Location quartile) confirmed by Claude only; GPT-5.6 and Grok did not exercise this pathway. Grok explicitly noted "Location Index available but not required for pure HP Injury" in Round 1 and chose Inflict Injury (Base) exclusively for "baseline validation of C-01/C-02."

---

## 5. Systems Observation

### 5.1 Core Test Transaction (DEC-006)

All three executions ran the 9-step transaction without exception. Claude reported 70+ individual Core Tests across 18 rounds. GPT-5.6 reported 20 rounds of exchanges. Grok documented ~55 Core Tests across 20 rounds (including repeats and nested Defense).

**Recommendation:** Future playtests should explicitly count and report total Core Tests for auditability.

### 5.2 S-1 Opposed Contest (DEC-013)

All three executions handled:

- Failure/Failure repeats (multiple exchanges required 2–5 repeats)
- Quality ties requiring repeats
- No safety cap breaches

Grok's documentation shows the most detailed repeat handling: Round 2 PC action required 3 repeats before resolution; Round 6 required 2 repeats; Round 10 required 2 repeats. Grok also documented a unique edge case: Round 2 PC won with Margin 0 (exact Skill match), producing Quality 0 < 1 → no Effect available (DEC-031 floor ≥1).

**Finding:** The repeat mechanism is robust across implementations. Grok's detailed logging confirms that each repeat resolves its own Cost/Overflow/Recovery independently. The Margin-0 no-Effect edge case is a valid rule confirmation.

### 5.3 Resource Cost / Overflow (DEC-007, DEC-007.A)

Claude observed Overflow-to-HP damage when PE pools were depleted by high rolls (e.g., Round 6 PC Active Defense roll 95 vs 26 remaining PE → 26 Overflow HP damage). GPT-5.6 also observed Overflow events. Grok's full 20 rounds showed no Overflow — all Costs stayed within PE pools, and PE recovered to clamp each round.

**Recommendation:** Future playtests should log Overflow events with explicit PE pool states. The absence of Overflow in Grok's run is not a failure but reflects roll variance within PE capacity. Grok's PE path tracking (before → after → final) is the most transparent format.

### 5.4 Skill Progression (DEC-010, DEC-011, DEC-012)

Claude documented 6 Advanced Skill creations (4× PC Attack2/Defence2 lineage, 2× Troll Brawling lineage) via qualifying failed Doubles. GPT-5.6's documentation is less detailed on progression. Grok explicitly noted "No failed Doubles triggered Advanced Skill creation" across all 20 rounds.

**Finding:** Advanced Skill creation via failed Doubles is roll-variance dependent. Its absence in Grok's run is not a rule failure but reflects the randomness of Double rolls.

**Recommendation:** Future playtests should track all Skill changes with before/after values and explicitly note when no progression occurs.

### 5.5 Active Defense (DEC-044/046)

All three executions invoked Active Defense on every applied Effect (voluntary, per DEC-046). Mitigation varied widely:

- Claude: 0, 2, 4, 10, 17, 24 observed
- GPT-5.6: varied (not itemized)
- Grok: 0, 5, 8, 9, 11, 17 observed

Grok's documentation shows that successful Active Defense occurred when both attacker and defender succeeded (Quality comparison), with mitigation = Defender's Margin. Failed Active Defense = mitigation 0. Grok also documented the Edge case where defender succeeded but attacker won on Quality (Round 4: PC succeeded with Margin 5, but Troll won with Margin 60 → mitigation 5 applied).

**Finding:** Active Defense is a significant damage reduction mechanism. Its voluntary nature means PC survival depends heavily on PE management.

---

## 6. Gaps and Issues Identified

### 6.1 Quality → Wound Tier Numeric Mapping (Claude finding)

Claude identified a genuine gap: DEC-035.B ties wound tier to "Quality-gated Effect tier" but provides no numeric conversion table. Claude scaffolded Wound Tier = 1 (minimum) as a non-canonical default.

**Status:** Unresolved. Requires human ruling.

**Impact:** Low for this playtest (only affected Round 1 demonstration). High for future playtests involving Wound effects.

**Coverage:** Single data point only — Claude's run exercised the Wound pathway; GPT-5.6 and Grok did not.

### 6.2 Creature/NPC Action Selection — SC-XX (GPT-5.6 finding, highest priority)

GPT-5.6 identified that combat sequencing (DEC-095) determines *when* a creature acts but not *which* action it selects when multiple legal attacks exist. This is the single most important finding from comparing the three runs.

**Status:** Unresolved. GPT-5.6 correctly escalated with three mandatory human confirmation questions (Q1–Q3). Claude's synthesis restates these questions.

**Governance failure:** Two of three executing LLMs (Claude, Grok) silently invented an alternation rule instead of flagging the gap, contradicting the prompt's own explicit instruction. This is not just a divergence — it is an unflagged governance violation.

**Impact:** High. Affects all future playtests with multi-attack creatures. The prompt must either:

1. Pre-author an explicit action-selection procedure or scaffold for the test creature before execution begins, or
2. Explicitly instruct the executing LLM that action selection is a mandatory GM-stop point every time it recurs (not just the first time), or
3. Require human escalation at action-selection boundaries

### 6.3 HP Floor / Negative-HP Recording Convention (Claude finding, new)

DEC-052 states HP = 0 triggers forced incapacitation. It does not state whether HP is clamped at 0 for record-keeping or allowed to go negative to preserve the magnitude of overkill. The three runs handled this three different ways:

| Run | Final PC HP recorded | Convention |
|---|---:|---|
| GPT-5.6 Luna | **−29** | Uncapped — raw arithmetic result |
| Grok 4.5 | 0 (shown as "−11 → 0") | Clamped, but pre-clamp value preserved in log |
| Claude Sonnet 5 | 0 | Arithmetic landed exactly on 0; clamping behavior untested |

**Status:** Unresolved. Neither DEC-052 nor any other located ruling settles this.

**Impact:** Medium. Affects comparability of final records across runs. Should be settled before next playtest so all executing LLMs clamp (or don't) consistently.

### 6.4 Location/Wound Pathway Exercise Gap

Only Claude exercised the Location Tier-1 quartile split (DEC-100) in Round 1. Grok explicitly noted the Location Index was "available but not required for pure HP Injury" and chose Inflict Injury (Base) exclusively for "baseline validation of C-01/C-02." GPT-5.6's documentation does not detail this decision.

**Finding:** The Location/Wound pathway remains under-exercised across executions. 2 of 3 parallel runs never touched this pathway, so the Quality→Wound-Tier gap (OI-001) currently rests on a single execution.

**Recommendation:** Future playtests should explicitly require at least one Wound exercise per playtest to validate the full pathway, rather than leaving it to executor discretion.

### 6.5 Margin-0 No-Effect Edge Case (Grok finding)

Grok documented a unique edge case in Round 2: PC won with Margin 0 (exact Skill match = 24 vs 24), producing Quality 0 < 1 → no Effect available per DEC-031 floor ≥1. Attack succeeds but produces no selectable Effect. No HP change.

**Status:** Confirmed as valid rule behavior. Not a gap — DEC-031 floor is working as designed.

**Finding:** This edge case is worth noting for future playtests as it demonstrates the Quality floor mechanism in practice.

### 6.6 Output-Format Granularity Compliance (Claude finding, process)

The v3 prompt's "Output format" section mandates that the live log record, for every roll: raw d100, Skill tested, Cost, Overflow if any, Success/Fail, Quality if relevant, Effect selected, Location Index if rolled, Wound/Condition applied, Recovery amount.

- **Claude and Grok's logs comply** — every roll shows Skill value, Cost, Overflow, Recovery.
- **GPT-5.6 Luna's log does not comply** — it shows only the raw roll and Success/Fail per test, with net HP damage per exchange. Skill values, Cost, Overflow, Failure XP, Quality, and Recovery are not shown per-roll.

**Status:** Process/compliance finding, not a new mechanical gap. The rules functioned identically whether or not the log showed the work.

**Impact:** Low for this playtest. But it materially reduces the audit value of GPT-5.6's document relative to the other two, and should inform how tightly the next prompt specifies mandatory log format.

### 6.7 RNG Method / Reproducibility Disclosure (Claude finding, process)

Claude's log discloses `random.SystemRandom()` (OS entropy) as the roll source. Grok's and GPT-5.6 Luna's documents do not state how rolls were generated.

**Status:** Process finding, not a mechanical gap.

**Impact:** Low. Only one of three runs is independently auditable/reproducible in principle. Recommend the next prompt make RNG-method disclosure a mandatory provenance field.

---

## 7. Coverage Gaps Across the Three Runs

No single run exercised everything. Aggregate coverage:

| Pathway | GPT-5.6 Luna | Claude | Grok |
|---|:---:|:---:|:---:|
| DEC-100 Location/quartile | ✗ | ✓ | ✗ |
| Wound Effect (vs. plain Injury) | ✗ | ✓ | ✗ (declined intentionally) |
| Advanced Skill creation shown | ✗ (not visible) | ✓ (6 instances, named) | ✗ (none triggered) |
| Overflow→HP shown | ✗ (not visible) | ✓ | ✗ (none occurred) |
| Full 9-step per-roll transparency | ✗ | ✓ | ✓ |
| RNG method disclosed | ✗ | ✓ | ✗ |
| HP floor convention tested | ✓ (uncapped) | ✗ (landed on 0) | ✓ (clamped) |

**Key finding:** Only Claude's run touched the Wound/Location pathway, meaning the entire gated-tier Effect content and Quality→Wound-Tier question has exactly one data point. Only Claude's run disclosed RNG method. Only Claude and Grok provided full per-roll transparency. The HP floor convention was tested in two of three runs with different results.

---

## 8. Execution Methodology Comparison

### 8.1 Automation Approach

| Aspect | Claude Sonnet 5 | GPT-5.6 Luna | Grok 4.5 |
|---|---|---|---|
| Computation | Python-computed (OS entropy) | Not specified | Not specified |
| Roll source | `random.SystemRandom()` | Not specified | Not specified |
| Math verification | Explicit arithmetic fidelity guarantee | Not specified | Explicit step-by-step arithmetic |
| Output format | Live log + summary report | Execution record + finding document | Step-by-step Core Test tables + summary |
| PE tracking | Logged per exchange | Not detailed | Explicit PE path columns (before → after → final) |
| Engine runtime | Not specified | Not specified | ~45 minutes sequential resolution |

**Recommendation:** Future playtests should adopt Claude's approach of explicit computation method documentation and raw data output (`combat_results.json`). Grok's PE path tracking and runtime documentation are exemplary and should be standard.

### 8.2 Documentation Quality

| Aspect | Claude Sonnet 5 | GPT-5.6 Luna | Grok 4.5 |
|---|---|---|---|
| Round-by-round detail | Full exchange-level log | Condensed table | Full step-by-step (R1–10) + summary (R11–20) |
| Skill progression tracking | Explicit before/after | Not detailed | Explicitly noted "none triggered" |
| PE pool tracking | Logged per exchange | Not detailed | Explicit PE path columns |
| Overflow tracking | Explicit events logged | Not detailed | Explicitly noted "none observed" |
| Active Defense detail | Mitigation values logged | Not itemized | Mitigation values logged with edge cases |
| Scaffold flagging | Explicit scaffold log | Embedded in report | Explicit scaffold note in pre-combat |
| Governance compliance | Strong provenance notes | Strong interpretation discipline | Strong provenance notes |
| Repeat handling | Counted repeats | Counted repeats | Detailed repeat tables with resolution |
| Edge case documentation | Limited | Limited | Margin-0 no-Effect case documented |
| Final report | Separate summary | Separate finding document | Integrated with execution log |

**Finding:** Each execution has documentation strengths. Claude's summary + live log combination provides both overview and audit trail. GPT-5.6's governance discipline prevents over-interpretation. Grok's step-by-step Core Test tables with PE path tracking are the most auditable format, and the integration of execution log with final report provides the most complete single-document record. Future playtests should combine all three approaches.

---

## 9. Recommendations for Future Playtests

### 9.1 Prompt Refinement

1. **Attack selection:** Explicitly specify which attack the creature uses for each test, or require human input at action-selection boundaries
2. **Wound Tier mapping:** Provide explicit numeric conversion table or scaffold default before execution
3. **Documentation requirements:** Mandate round-by-round exchange logs with PE pool states, Skill changes, and Overflow events
4. **Raw data output:** Require JSON or structured data output for programmatic audit
5. **Location/Wound exercise:** Explicitly require at least one Wound exercise per playtest to validate the full pathway

### 9.2 Execution Standards

1. **Computation method:** Document roll source and computation approach
2. **Math verification:** Use deterministic computation (not LLM arithmetic)
3. **Provenance:** Maintain Claude/Grok's provenance note style for DEC-012 exceptions
4. **Scaffold logging:** Explicitly flag all non-canonical decisions with justification
5. **PE path tracking:** Adopt Grok's explicit PE path columns (before → after → final) as standard format
6. **Repeat detail:** Document each repeat with its own Core Test table, not just repeat counts
7. **Edge case documentation:** Explicitly document edge cases like Margin-0 no-Effect (Grok Round 2)
8. **Runtime documentation:** Record engine runtime for benchmarking (Grok: ~45 minutes for 20 rounds)

### 9.3 Post-Execution Requirements

1. **Cross-report synthesis:** Run synthesis analysis after each multi-implementation playtest
2. **Gap tracking:** Register all identified gaps (Quality→Wound Tier, Action Selection) in project tracking
3. **Human escalation:** Present all unresolved gaps to human before next playtest
4. **Progression tracking:** Explicitly note when Advanced Skill creation does or does not trigger (Grok: "none triggered")

---

## 10. Open Items Requiring Human Decision

| ID | Issue | Source | Priority |
|---|---|---|---|
| OI-001 | Quality → Wound Tier numeric conversion | Claude finding | Medium |
| OI-002 | Creature/NPC action selection procedure (SC-XX) | GPT-5.6 finding | **High** |
| OI-003 | HP floor / negative-HP recording convention | Claude finding | Medium |
| OI-004 | Location/Wound pathway under-exercise | This synthesis | Low |
| OI-005 | GPT-5.6 Q1–Q3 (attack-selection confirmation questions) | GPT-5.6 finding | **High** (restated in OI-002) |

---

## 11. Conclusion

The three available playtest executions (Claude Sonnet 5, GPT-5.6 Luna, Grok 4.5) used identical rules and stat blocks but produced different outcomes due to attack selection and roll variance. All validated DEC-094–DEC-101 as deterministic. The key findings:

1. **Attack selection (governance failure):** Claude and Grok silently invented an alternation rule; GPT-5.6 stopped and escalated but then silently generalized a single-round instruction into a 20-round default. This is the highest-priority finding — SC-XX remains open.
2. **Round count:** 18 (Claude), 20 (GPT-5.6), 20 (Grok)
3. **Final HP:** 0 (Claude), −29 (GPT-5.6), 0 (Grok) — three different HP floor conventions used
4. **Overflow variance:** Claude observed Overflow in mid-combat; Grok's full 20 rounds showed none — normal variance within PE capacity
5. **Advanced Skill creation:** Claude observed 6 creations; Grok observed none — roll-variance dependent, not a rule difference
6. **Active Defense effectiveness:** All three executions confirmed mitigation = Defender's Margin on success, 0 on failure
7. **Edge cases:** Grok documented Margin-0 no-Effect (DEC-031 floor ≥1) — valid rule confirmation
8. **Quality→Wound Tier mapping:** Single data point only (Claude Round 1) — needs triangulation
9. **Output format compliance:** GPT-5.6's log does not meet v3 prompt requirements — reduces audit value
10. **RNG disclosure:** Only Claude disclosed roll source — limits reproducibility

All three executions confirmed the same seven DEC rulings deterministically. The cross-model comparison surfaced two genuine new gaps (HP floor convention, governance failure in attack selection) and one coverage weakness (Wound pathway single data point) that a single run would not have exposed. This validates the multi-LLM playtest methodology as standing practice.

The synthesis demonstrates that cross-implementation comparison is valuable for validating rule determinism, surfacing governance failures, and identifying coverage gaps. Future playtests should adopt standardized documentation formats (combining Claude's summary approach, GPT-5.6's governance discipline, and Grok's step-by-step PE tracking) to enable automated synthesis.

---

## 12. Document Status

**Status:** Playtest analysis — not canonical  
**Authority:** Advisory — requires human confirmation for any rule changes  
**Next action:** Present OI-002 (SC-XX) and OI-003 (HP floor) to human for decision  
**Canonical rule change:** None  
**Source documents analyzed:** 6 of 6 (all complete, including Claude's cross-model synthesis)
