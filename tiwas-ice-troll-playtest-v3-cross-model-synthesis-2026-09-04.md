---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest v3: Cross-Model Comparative Synthesis"
  version: "1.0"
  status: "Advisory analysis (not canonical). Compares four independent executions of the same playtest prompt. Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
source_documents:
  - "Tiwas_TTRPG___Ice_Troll_Combat_Playtest_v3-Unedited_Playtest_Execution_Results.md (GPT-5.6 Luna)"
  - "Tiwas_TTRPG___Ice_Troll_Combat_Playtest_v3.md (GPT-5.6 Luna, Action-Selection finding)"
  - "tiwas-ice-troll-playtest-v3-FINAL-REPORT-2026-09-04.md (Claude Sonnet 5)"
  - "tiwas-ice-troll-playtest-v3-LIVE-LOG-2026-09-04.md (Claude Sonnet 5)"
  - "Tiwas_TTRPG___Ice_Troll_Combat_Playtest__v3__Execution-grok2.md (Grok 4.5)"
governing_prompt: "tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md"
---

# Tiwas TTRPG — Ice Troll Combat Playtest v3: Cross-Model Comparative Synthesis

**Purpose of this document:** three LLMs (GPT-5.6 Luna, Claude Sonnet 5, Grok 4.5) independently executed the identical v3 playtest prompt as Combat Referee. This is a comparative analysis of the four resulting documents (GPT-5.6 Luna produced two). **No ruling is made here. No DEC is assigned. This report exists to give Tiwa a single consolidated view of what converged, what diverged, and what new gaps the triangulated execution surfaced** — for the specific purpose of improving the next playtest prompt/process.

---

## 1. Sources Compared

| # | Executing LLM | Document | Rounds | Role |
|---|---|---|---:|---|
| 1 | GPT-5.6 Luna | *Unedited Playtest Execution Results* | 20 | Primary combat log/report |
| 2 | GPT-5.6 Luna | *Action-Selection Decision and Execution Record* | — | Companion finding on the same run |
| 3 | Claude Sonnet 5 | *LIVE-LOG* | 18 | Primary combat log |
| 4 | Claude Sonnet 5 | *FINAL-REPORT* | 18 | Report on the same run as #3 |
| 5 | Grok 4.5 | *Execution* (combined log + report) | 20 | Primary combat log/report |

Three genuinely independent full combats exist: **GPT-5.6 Luna's run, Claude's run, Grok's run.** Each used its own RNG stream, so different round counts and HP tracks are expected stochastic variance, not evidence of a rule discrepancy — that variance is not itself analyzed further below except where it exposes a *procedural* (not numeric) divergence.

---

## 2. Cross-Run Comparison Matrix

| Metric | GPT-5.6 Luna | Claude Sonnet 5 | Grok 4.5 |
|---|---|---|---|
| Rounds to incapacitation | 20 | 18 | 20 |
| Adventurer-1 final HP | **−29** (uncapped) | 0 | 0 (reported as "−11 → 0", clamped) |
| Ice Troll final HP | 583/705 | 610/705 | 641/705 |
| Troll attack selection | **Sharktoothed Maw only, all 20 rounds** — via one-time explicit human instruction | Alternated Icy Claws / Sharktoothed Maw every round, autonomously | Alternated Icy Claws / Sharktoothed Maw every round, autonomously |
| Attack-selection procedure flagged as a gap? | **Yes — separate companion document, execution paused pending human input, Q1–Q3 escalated to Tiwa** | No — alternation applied silently, not logged as a scaffold or GM-stop | No — alternation applied silently, not logged as a scaffold or GM-stop |
| Per-roll Cost/Overflow/Recovery/Failure XP logged? | **No** — table shows only roll + S/F + net HP damage | Yes, full 9-step detail every roll | Yes, full 9-step detail every roll |
| Skill values shown per roll (verifying Frightened −1, XP growth)? | **No** | Yes | Yes |
| DEC-100 (Location quartile) / Wound pathway exercised? | Not mentioned at all | **Yes — once, Round 1 (demonstration)** | No — explicitly declined "for data purity" |
| New gap surfaced by exercising Wound pathway (Quality→Wound-Tier) | N/A (not exercised) | **Yes — flagged, scaffolded Wound Tier 1** | N/A (not exercised) |
| Advanced Skill creation (failed Doubles) logged? | Not visible in log | Yes, multiple instances, named | Not shown in truncated excerpt but referenced in summary as "none triggered" |
| RNG method disclosed? | No | Yes — `random.SystemRandom()`, Python | No |
| Frightened (DEC-094) applied and logged? | Yes, stated but not traceable in per-roll math | Yes, traceable in effective Skill values | Yes, traceable in effective Skill values |
| GM-required stop occurred mid-combat? | **Yes, at Round 1 action-selection** (resolved only because the human supplied an instruction) | No | No |

---

## 3. Convergent Findings — DEC-094–DEC-101 Confirmed Deterministic

Across the three independent runs, every ruling actually exercised resolved without invented values, and no run contradicted another's *mechanical application* of a ruling (only the never-ruled attack-selection step differed):

| DEC | Ruling | GPT-5.6 Luna | Claude | Grok | Convergent? |
|---|---|---|---|---|---|
| DEC-094 | Passive Frightened (scene-state) | Applied, Tier-1 −1 | Applied, Tier-1 −1, traceable | Applied, Tier-1 −1, traceable | Yes |
| DEC-095 | SC-04 sequencing | Troll first (Speed 175>150) | Troll first every round | Troll first every round | Yes |
| DEC-096 | C-01 Injury = Winner's Margin | Used (implicit, math checks out in §8) | Used, shown per roll | Used, shown per roll | Yes |
| DEC-097 | C-02 Defense mitigation = Defender's Margin | Used (implicit, math checks out in §8) | Used, shown per roll | Used, shown per roll | Yes |
| DEC-098 | C-06 Brawling default defense | Used | Used | Used | Yes |
| DEC-099 | C-07 Quality ≥1/≥10 | Not traceable (no Quality shown) | Applied and shown every win | Applied and shown every win | Consistent where checkable |
| DEC-100 | C-08 quartile Location | Not exercised | Exercised once, correct zone/laterality math | Not exercised | Untested by 2 of 3 runs |
| DEC-101 | C-09 defender-wins, no counter-Effect | Applied (Round 12/13/14/16 "PC wins" rows) | Applied, multiple exchanges | Applied, multiple exchanges | Yes |

**Conclusion:** the eight rulings function as intended wherever independently checkable. This triangulates the DEC-094–101 package as sound for the mechanics it actually covers.

---

## 4. New/Divergent Findings — Requires Tiwa's Attention

### 4.1 SC-XX — Creature Multi-Attack Action-Selection Procedure (highest priority)

**This is the single most important finding to come out of comparing the three runs.** All three executing LLMs hit the identical decision point — the Ice Troll has two legal Tier-2 attacks (Icy Claws 67, Sharktoothed Maw 75) and nothing in the corpus says which one it uses on a given turn — and handled it three different ways:

| LLM | Handling | Consistent with "never invent silently, stop and flag when genuinely open"? |
|---|---|---|
| GPT-5.6 Luna | **Stopped, escalated to the human, obtained one-time explicit instruction ("Sharktoothed Maw"), then reused that single instruction for all 20 rounds without re-asking** | Partially — correctly stopped once, but then silently generalized a single-round answer into a 20-round default without flagging that generalization |
| Claude Sonnet 5 | Silently alternated Icy Claws/Sharktoothed Maw every round | **No** — this is an unflagged invention; nothing in the corpus authorizes alternation as a selection rule |
| Grok 4.5 | Silently alternated Icy Claws/Sharktoothed Maw every round | **No** — same issue |

Two of three executions violated the prompt's own governing instruction ("You never invent a rule to smooth over a gap... Where the corpus is silent and no rule or scaffold is pre-authorized below, you stop and flag the human monitor") without logging it as either a scaffold or a GM-stop. GPT-5.6 Luna's *separate* companion document is the only one of the five source documents that correctly identifies this as **SC-XX, a genuine open system gap**, and it is the only execution that visibly paused for it.

**This is not resolved by any existing DEC.** DEC-095 (SC-04) governs *turn order*, not *action choice among multiple legal actions*. GPT-5.6 Luna's three confirmation questions (Q1–Q3 in its companion document) remain live and are restated here for convenience:

1. Was the Round-1 "Sharktoothed Maw" selection an intentional one-off test instruction (not a rule)?
2. When a creature has multiple legal actions and no authored selection rule exists, should the Combat Referee be required to stop and request human input, rather than picking one itself?
3. Should "creature/NPC action selection" be formally registered as an open system gap (SC-XX) pending a future designer ruling?

**Recommendation for the next playtest prompt:** either (a) pre-author an explicit action-selection procedure or scaffold for the test creature before execution begins, or (b) explicitly instruct the executing LLM that action selection is a mandatory GM-stop point every time it recurs, not just the first time.

### 4.2 Quality → Wound-Tier Numeric Conversion (new gap, only surfaced once)

Only Claude's run exercised the Location/Wound pathway (Round 1, Quality 52, gated-tier eligible). Doing so exposed a real gap: **DEC-035.B** ties Wound Tier to "the Quality-gated Effect tier," but no formula converts a Margin-based Quality integer into a Wound Tier integer. Claude's run scaffolded Wound Tier = 1 (minimum) and flagged it; this was **not** independently confirmed or contradicted by the other two runs, because neither Grok nor GPT-5.6 Luna's runs ever selected a Wound/Location Effect (Grok explicitly declined it "for data purity"; GPT-5.6 Luna's log never mentions Location/Wound at all).

**Coverage implication:** 2 of 3 parallel runs never touched this pathway, so this finding currently rests on a single execution. It should be treated as a real flag for Tiwa, but the specific scaffold value (Tier 1) should not be assumed representative until re-tested.

### 4.3 HP Floor / Negative-HP Recording Convention (new gap)

DEC-052 states HP = 0 triggers forced incapacitation. It does not state whether HP is clamped at 0 for record-keeping or allowed to go negative to preserve the magnitude of overkill. The three runs handled this three different ways:

| Run | Final PC HP recorded | Convention used |
|---|---:|---|
| GPT-5.6 Luna | **−29** | Uncapped — raw arithmetic result |
| Grok 4.5 | 0 (shown as "−11 → 0") | Clamped, but the pre-clamp value is preserved in the log |
| Claude Sonnet 5 | 0 | Arithmetic landed exactly on 0; clamping behavior untested this run |

This is a genuine, previously-unflagged open item: **should Overflow/Injury damage that would drive HP below 0 be clamped at 0 in the permanent record, or recorded as the literal negative result?** Neither DEC-052 nor any other located ruling settles this. Flagged for Tiwa.

### 4.4 Output-Format Granularity Compliance (process finding, not a rule gap)

The v3 prompt's "Output format" section mandates that the live log record, for every roll: raw d100, Skill tested, Cost, Overflow if any, Success/Fail, Quality if relevant, Effect selected, Location Index if rolled, Wound/Condition applied, Recovery amount.

- **Claude and Grok's logs comply** — every roll shows Skill value, Cost, Overflow, Recovery.
- **GPT-5.6 Luna's log does not comply** — it shows only the raw roll and Success/Fail per test, with net HP damage per exchange. Skill values, Cost, Overflow, Failure XP, Quality, and Recovery are not shown per-roll anywhere in that document. This makes it impossible to independently verify that Frightened (−1), Skill-Roll-Pool advancement, or Overflow were correctly applied in that run — the reader must take the final HP numbers on faith.

This is a **process/compliance finding**, not a new mechanical gap: the rules functioned identically whether or not the log showed the work. But it materially reduces the audit value of that one document relative to the other two, and should inform how tightly the next prompt specifies mandatory log format (e.g., reject non-conforming logs, or require a machine-checkable log schema).

### 4.5 RNG Method / Reproducibility Disclosure (process finding)

Claude's log discloses `random.SystemRandom()` (OS entropy) as the roll source. Grok's and GPT-5.6 Luna's documents do not state how rolls were generated. This doesn't affect the validity of any individual roll, but it means only one of the three runs is independently auditable/reproducible in principle. Recommend the next prompt make RNG-method disclosure a mandatory field.

---

## 5. Coverage Gaps Across the Three Runs

No single run exercised everything. Aggregate coverage:

| Pathway | GPT-5.6 Luna | Claude | Grok |
|---|:---:|:---:|:---:|
| DEC-100 Location/quartile | ✗ | ✓ | ✗ |
| Wound Effect (vs. plain Injury) | ✗ | ✓ | ✗ (declined intentionally) |
| Advanced Skill creation shown | ✗ (not visible) | ✓ (6 instances, named) | Partial (stated none in summary excerpt) |
| Overflow→HP shown | ✗ (not visible) | ✓ (Round 18, +22 HP) | ✗ (claimed none occurred) |
| Full 9-step per-roll transparency | ✗ | ✓ | ✓ |
| RNG method disclosed | ✗ | ✓ | ✗ |

Only Claude's run touched the Wound/Location pathway at all, meaning the entire gated-tier Effect content and Quality→Wound-Tier question (§4.2) has exactly one data point. **Recommend the next combat playtest explicitly require at least one run to force a Wound-tier Effect selection**, rather than leaving it to chance/executor discretion, so this pathway gets triangulated the same way the Base-tier Injury pathway did.

---

## 6. Recommendations for the Next Playtest Prompt (v4 candidate checklist)

These are process recommendations only — none of them are rulings, and none should be treated as settled without Tiwa's sign-off:

1. **Pre-author or explicitly scaffold creature action selection** (§4.1) before execution, or mandate a GM-stop on every occurrence (not just the first) until a rule exists.
2. **Mandate machine-checkable per-roll log fields** (Skill value, Cost, Overflow, Failure XP, Quality, Recovery) as a pass/fail compliance gate on the executing LLM's output, not just a formatting suggestion.
3. **Require RNG-method disclosure** as a mandatory provenance field in every combat log.
4. **Force at least one Wound/Location-tier Effect selection** per run (rather than leaving Base-tier Injury vs. gated-tier Effect selection to the executor's discretion) so the Quality→Wound-Tier gap (§4.2) gets more than one data point.
5. **Settle the HP-floor/negative-HP convention (§4.3) before the next run**, so all executing LLMs clamp (or don't) consistently and the reports remain comparable.
6. **Continue running the same prompt across multiple LLMs in parallel.** This comparison is only possible because three independent executions existed; it surfaced two genuine gaps (§4.1, §4.3) and one coverage weakness (§4.2/§5) that a single run would not have exposed. Recommend this remain standing playtest methodology, not a one-off.

---

## 7. Consolidated Flags Requiring Tiwa's Ruling

| # | Item | Status | Source |
|---|---|---|---|
| 1 | Creature multi-attack action-selection procedure (SC-XX) | **Open — highest priority**, two independent unflagged rule-inventions occurred | §4.1 |
| 2 | Quality → Wound-Tier numeric conversion | **Open**, single data point only | §4.2 |
| 3 | HP floor / negative-HP recording convention | **Open**, three different conventions used across three runs | §4.3 |
| 4 | GPT-5.6 Luna's Q1–Q3 (attack-selection confirmation questions) | **Open**, restated in §4.1, still unanswered | Companion doc §11 |

None of these four items should be resolved by this document. They are collated here so they reach Tiwa as a single list rather than being re-discovered independently in each source document.

---

## 8. Conclusion

Triangulating three independent LLM executions of the same v3 prompt confirms that **DEC-094–DEC-101 resolve deterministically wherever they were actually exercised** — the core finding the prompt was designed to validate holds up. The comparison also demonstrates the value of running the same prompt across multiple LLMs: it surfaced a real, previously-invisible governance failure (two of three executors silently invented an attack-selection rule instead of flagging it, contradicting the prompt's own explicit instruction), a genuine new numeric gap with only single-run coverage, and an unresolved record-keeping convention — none of which any single run would have exposed on its own.

No mechanics are ruled, promoted, or invented as canon by this document. No DEC number is assigned.
