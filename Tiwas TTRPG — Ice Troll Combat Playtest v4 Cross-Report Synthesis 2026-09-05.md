# Tiwas TTRPG — Ice Troll Combat Playtest v4: Cross-Report Synthesis

```yaml
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  source_documents:
    - "tiwas-ice-troll-v4-combined-report.md"                 # Claude combined artifact (final report + live log + JSON)
    - "tiwas-ice-troll-combat-playtest-v4-comprehensive-report.md"  # Grok 4.5 comprehensive report
    - "Tiwas TTRPG — Ice Troll Combat Playtest v4 Comprehensive Report.md"  # GPT-5.6 Luna comprehensive report (aborted)
    - "tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md"
    - "Tiwas TTRPG — Ice Troll Combat Playtest v3 Cross-Report Synthesis 2026-09-04.md"
```

## 1. Document Purpose

This document compares, contrasts, collates, and synthesizes the three v4 playtest execution
reports for the Tiwas TTRPG Ice Troll Combat Playtest v4. v4 was the first playtest prompt
written **after** the v3 Cross-Report Synthesis (2026-09-04), and it baked several previously
open items into the prompt as pre-authorized scaffolds. The purpose of this v4 synthesis is
the same as its v3 predecessor — **to improve future playtests** by identifying:

- Execution methodology differences between LLM implementations
- Outcome variations and their causes
- System gaps surfaced by the executions
- Where the v3 gaps were successfully closed versus where they remain open
- New gaps the v4 run exposed **beyond** the v3 gap set
- Recommendations for prompt refinement and rule clarification

**Authority status:** This is a playtest analysis document. It does not create new canonical
rules, assign DEC numbers, or make system decisions. All findings require human confirmation
before promotion. Consistent with `governance/authority.md` and the repository's governance
controls in `AGENTS.md`, this synthesis is purely advisory and records no authority.

---

## 2. Source Document Inventory

| Document | Author | Type | Rounds | Final PC HP | Status |
|---|---|---|---:|---:|---|
| `tiwas-ice-troll-v4-combined-report.md` | Claude Sonnet 5 | Combined final report + live log + JSON | 99 | 0 | Complete |
| `tiwas-ice-troll-combat-playtest-v4-comprehensive-report.md` | Grok 4.5 | Comprehensive report + JSON | 16 | 0 | Complete |
| `Tiwas TTRPG — Ice Troll Combat Playtest v4 Comprehensive Report.md` | GPT-5.6 Luna | Comprehensive report + JSON | 0 (aborted R1) | 600 (unchanged) | **ABORTED / GM stop** |
| `tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md` | opencode/big-pickle | Governing executable prompt | — | — | Advisory |

**Summary of the three outcomes:** Claude completed 99 rounds; Grok completed 16 rounds;
GPT-5.6 Luna aborted in Round 1 after 2 Core Tests on a mandatory GM stop. This is the
first v-series playtest in which the three parallel runs did **not** all reach conclusion,
and the divergence between GPT-5.6's abort and the two completed runs is the central finding
of this synthesis.

---

## 3. Execution Comparison

### 3.1 Combat Parameters (identical across all three)

All three executions used the same stat blocks, same order, same conditions:

- **Adventurer-1:** 24 attributes at 50; HP 600, PE 150, Speed 150, Energy Regen 100;
  Tier-1 skills at 25 (Cap 50); Attack2/Defence2 Tier-2 at Starting Value 25 (Cap 50) via
  the DEC-012 exception; `Frightened` Tier-1 Value −1 active from Round 1 (DEC-094
  scene-state binding on the Troll's Appearance:Hideous).
- **Ice Troll:** HP 705, PE 220, Speed 175, Energy Regen 140; Icy Claws 67 (veteran),
  Sharktoothed Maw 75, Brawling 37 (DEC-098 default defensive skill).
- **Initiative:** Troll (175) → Adventurer-1 (150), every round.
- **Attack selection:** pre-authorized scaffold — Icy Claws odd rounds, Sharktoothed Maw
  even rounds, starting Round 1.
- **Four pre-authorized scaffolds:** DEC-012 exception, attack-selection alternation,
  Quality→Wound Tier table (1–9=T1, 10–19=T2, 20–29=T3, 30+=T4), and HP clamp-to-0 with
  pre-clamp preservation.

### 3.2 Headline Outcome Comparison

| Metric | Claude Sonnet 5 | Grok 4.5 | GPT-5.6 Luna |
|---|---:|---:|---:|
| Total rounds | 99 | 16 | 0 (aborted R1) |
| Complete rounds | 99 | 16 | 0 |
| Total Core Tests | 307 | 88 | 2 |
| Final PC HP | 0 (incapacitated) | 0 (incapacitated) | 600 (unchanged) |
| Final Troll HP | 674 | 645 | 705 (unchanged) |
| PC incapacitation round | 99 | 16 | never reached |
| Wound/Location exercises | 76 | 14 | 1 (then GM stop) |
| Base-tier Inflict Injury | 17 | multiple | 0 |
| Active Defense rolls | 110 | 31 | 0 (defense failed) |
| Overflow events | 31 | multiple (PC PE exhausted) | 0 |
| Advanced Skills (failed Double) | 13 (PC 8, Troll 5) | 0 | 0 |
| GM-required stops | 0 | 0 | **1 (blocking)** |
| RNG method | `random.SystemRandom()` OS entropy | `random.Random(42)` seeded | `secrets.SystemRandom()` OS entropy |
| Computation | Python (external) | Python (external) | Python-computed |
| PC defeat cause | **Self-inflicted Overflow** (604 HP) | Troll Wounds/Injury | n/a (aborted) |

### 3.3 Why the Runs Diverged So Wildly

The three runs all obeyed the same v4 prompt and all four scaffolds, yet produced 99 vs 16
vs 0 rounds. The causes are:

1. **The Wound-consequence gap (the deciding factor).** GPT-5.6 stopped because the corpus
   does not specify (a) which Attribute/Skill a Wound targets and (b) how Active Defense's
   Defender's Margin modifies a Wound Tier/magnitude. Claude and Grok both **bypassed** this
   gap by treating Wounds as records/conditions that impose **no direct HP loss** on
   application (consistent with DEC-032, and specifically flagged by Claude as a scope note
   referencing OPEN-007 "not table-ready for a full penalty-application engine"). Because
   the two completed runs did not apply Wound consequences, the primary PC-killing mechanism
   in those runs was HP loss — by Overflow (Claude) and by Troll Injury/Wound *HP magnitude*
   (Grok). GPT-5.6's stricter reading treated the Wound branch as a blocking stop. **This is
   the central, unresolved divergence in v4 and the most important finding of this synthesis.**
2. **The exchange-algorithm reconstruction diverges.** No single DEC spells out the full
   combined melee-exchange algorithm. Claude explicitly reconstructed one (its §14
   methodology note) and applied `Effects` as nested rolls; Grok's implementation also
   produced a completed combat but with far fewer rounds because its Troll Wounds carried
   HP magnitude directly. GPT-5.6 did not reach a full exchange because it could not define
   the Wound consequence. The two completed runs therefore operationalized "What does a Wound
   do?" differently, which changes lethality, round count, and outcome.
3. **Skill growth trajectory.** Claude's 99-round run allowed sustained Skill Roll Pool
   cascade (Attack2 25→49, Defence2 25→45), which in turn made more failed Doubles and more
   Overflow possible. Grok's 16-round run ended quickly because the Troll's high-margin Wounds
   carried direct HP magnitude every round. The PC's survival time is therefore not a stable
   system property — it depends entirely on the (unresolved) Wound-consequence model.
4. **RNG seed and variance.** Grok used a fixed seed (42); Claude and GPT-5.6 used OS entropy.
   Grok's 16-round conclusion, Claude's 99-round conclusion, and GPT-5.6's instant abort are
   all within the same ruleset given the differing Wound-consequence interpretation, so raw
   round count is **not** a comparability metric across these three runs.

**Conclusion:** The three runs are *not* valid instances of the same mechanical system in any
comparable sense. They are three different operationalizations of an unresolved Wound-consequence branch. Any future playtest that aims to validate end-to-end combat **must first
resolve the Wound-consequence question** (see §6 and §9).

---

## 4. What the v4 Prompt Fixed vs What Remains Open

### 4.1 v3 Gaps the v4 Prompt Addressed (pre-authorized scaffolds)

| v3 Gap / Recommendation | v4 Handling | Result across the three runs |
|---|---|---|
| **6.2 Attack selection (silent invention)** | Pre-authorized alternation scaffold + mandatory log | All three followed alternation; none silently invented. **Fixed.** |
| **6.1 Quality → Wound Tier numeric table** | Explicit scaffold table | Claude/Grok applied it; GPT-5.6 applied it (Q30→T4) then stopped on the *next* gap. **Fixed as a table; exposed the downstream gap.** |
| **6.3 HP floor convention (three conventions in v3)** | Clamp-to-0 + preserve pre-clamp | Claude/Grok applied consistently; GPT-5.6 did not reach HP loss. **Fixed.** |
| **6.4 Location/Wound under-exercise** | Mandatory ≥1 Wound exercise | All three triggered the Wound pathway (GPT-5.6 in Round 1). **Fixed.** |
| **6.6 Output format compliance** | Tighter mandatory field list | Claude/Grok fully populated; GPT-5.6 populated its 2 rolled tests. **Fixed.** |
| **6.7 RNG method disclosure** | Mandatory provenance field | All three disclosed RNG. **Fixed.** |
| **9.1.4 Core Test counting** | Mandatory total + breakdown | All three reported totals (307 / 88 / 2). **Fixed.** |

The v4 prompt's scaffolds **successfully closed every v3 gap that was purely a recording or
procedural convention gap**. The attack-selection governance problem, in particular, was
cleanly resolved: no run silently invented an alternation rule; all three logged the scaffold.

### 4.2 v3 Gaps That Remain Open (correctly, as scaffolds require human ruling)

| v3 Open Item | Status after v4 |
|---|---|
| SC-XX Creature/NPC action selection | **Still open.** Scaffold works but not canonical. |
| Quality → Wound Tier numeric mapping | **Still open** (scaffold used; needs human ruling). |
| HP floor / negative-HP recording convention | **RESOLVED via DEC-108 (2026-09-05)** — HP uncapped; negative values persist. |

All three of these match exactly the items the v4 prompt left open and scaffolded — no run
attempted to canonize them, which is correct behavior.

---

## 5. Rule Validation Summary

Because GPT-5.6 aborted early and the two completed runs applied different Wound-consequence
models, **rule validation status varies sharply by rule**.

| Ruling | Claude | Grok | GPT-5.6 | Consensus |
|---|---|---:|---:|---:|---|
| DEC-094 Passive Frightened (scene-state) | Yes (full combat) | Yes (full combat) | Yes (Round 1) | **Confirmed/Exercised** |
| DEC-095 SC-04 sequencing | Yes (99 rounds) | Yes (16 rounds) | Yes (Round 1) | **Confirmed** |
| DEC-096 Inflict Injury = Winner's Margin | Yes (17 Base) | Yes (Base pathway) | Not reached | **Confirmed in completed runs** |
| DEC-097 Active Defense = Defender's Margin | Yes (110 rolls) | Yes (31 rolls) | Branched but unresolved vs Wound | **Confirmed for Injury mitigation; gap vs Wound** |
| DEC-098 Brawling default defense | Yes (37→44) | Yes (37) | Not triggered (defense failed) | **Confirmed** |
| DEC-099 Quality ≥1 / ≥10 gating | Yes | Yes | Yes (Q30 gated) | **Confirmed** |
| DEC-100 Location quartile split | Yes (76) | Yes (14) | Yes (R1: 32→Torso) | **Confirmed** |
| DEC-101 Defender-wins = no counter-Effect | **Not triggered (0)** | Yes (defender-wins frequent) | Not reached | **Confirmed by Grok; coverage gap for Claude** |

**Key nuance for DEC-097:** All three runs invoke Active Defense on a won attacker's Effect.
But the *meaning* of that mitigation differs: Claude/Grok subtracted Defender's Margin from
the winner's raw HP magnitude. GPT-5.6's stop exposed that the corpus does not define how
Defender's Margin modifies a **Wound** consequence specifically (as opposed to an Injury).
So DEC-097 is confirmed for the Injury branch but **unresolved for the Wound branch** — a
distinction the v4 prompt did not draw.

**Coverage note:** DEC-101 (defender-wins = no counter-Effect) is the *opposite* type of
finding in Claude vs Grok: Grok observed frequent defender-wins (the PC often failing, the
Troll often failing → no counter-Effect); Claude observed **zero** natural defender-wins in 99
rounds (the skill gap made it rare) and flagged DEC-101 as a genuine coverage gap for future
playtests. This is worth noting: two runs landed on opposite ends of the DEC-101 exercise
spectrum.

---

## 6. New and Deepened Gaps Exposed by v4 (the core deliverable)

### 6.1 The Wound-Consequence / Wound-Target Gap (NEW — highest priority, blocking)

GPT-5.6's abort isolated this as the decisive open question. The v4 scaffolds successfully
carried execution through:

```
Attack → Defence → Win → Quality → gated Effect → Location → Wound Tier
```

and it stopped at:

```
Wound Tier + Location → exact mechanical consequence
```

The corpus does not specify, after a Wound Tier and anatomical zone are established:

1. **Which Attribute/Skill the Wound targets or reduces** (Gap A — Wound target selection).
2. **How Active Defense's Defender's Margin modifies a Wound Tier/magnitude** (Gap B —
   Wound vs Active Defense).

**Why this is the single most important v4 finding:** because the two runs that *completed*
(GPT-5.6 aborted) did so by **not applying Wound consequences at all**. Claude explicitly
records (its §8) that it logged 76 Wound *creation* events but did not simulate downstream
attribute/skill penalties from those Wounds, citing OPEN-007 as "not table-ready for a full
penalty-application engine within a single fast-combat run." Grok applied Wounds as direct HP
magnitude. Neither approach is validated against the corpus — each is an executor's choice to
bridge a genuine gap without a GM stop. That means:

- **The PC-killing mechanism in the two "completed" runs is an artifact of how each run
  sidestepped the Wound-consequence gap, not a stable property of the Ruled system.**
- The 99-round vs 16-round difference is substantially explained by this, not by roll variance.
- Claude's headline emergent finding (self-inflicted Overflow dominance) is real and
  mechanically literal, but its *relative* contribution (100.7% of HP loss vs Troll's 7.5%)
  is only meaningful under the assumption that Wounds impose no direct HP loss — which is
  exactly the unresolved assumption.

**Status:** Open / **blocking for end-to-end validation**.
**Consequence:** No v4 run constitutes a valid end-to-end combat that exercises the full
Wound consequence chain. GPT-5.6 explicitly flags its own run as "diagonostic success /
end-to-end validation failure."

### 6.2 The Exchange-Algorithm Reconstruction Divergence (NEW measurement of 6.1)

Claude explicitly documented that no single DEC spells out the full combined melee-exchange
algorithm and that it reconstructed one (its §14), built from DEC-013, DEC-044–050, DEC-096,
DEC-097, DEC-101, and SC-04's "nested" phrasing. This reconstruction is an interpretive step
Claude flagged for confirmation. Grok produced a compatible but not identical operational
implementation. GPT-5.6 effectively rejected the idea that the exchange could be resolved
against the Wound branch. 

**Status:** This is not a separate rule gap so much as a **measurement** of how much of the
melee procedure is left to enumeration. v3's synthesis noted GPT-5.6's insufficiently-detailed
algorithms; v4 reveals that even a "complete" exchange requires a reconstruction that shapes
the result. Worth human confirmation of the exact combined exchange algorithm as a
precondition for comparable future runs.

### 6.3 Wound-Application Scope (Claude's OPEN-007 scope note)

Claude flagged that Wound *consequences* (attribute/skill penalties applied to later tests)
were deliberately not simulated in-run, and that OPEN-007 is "not table-ready for a full
penalty-application engine within a single fast-combat run." This is the same underlying gap
as 6.1, framed as a deliberate scope decision by one executor.

**Status:** Open. Directly related to 6.1.

### 6.4 DEC-101 Coverage Asymmetry (low priority, coverage)

Claude recorded **zero** natural defender-wins in 99 rounds and recommended a rematch with
closer-matched defense skills or a forced-scenario test. Grok observed frequent defender-wins.
This is the reverse of v3, where defender-wins was a different coverage point. Not a rule gap —
a coverage gap.

**Status:** Closed 2026-09-05 via DEC-109 — coverage satisfied. Grok's run already exercised
DEC-101 frequently and in-spec ("Every defender-win produced 'attack fails, no counter-
Effect'"); the initial "gap" reading followed Claude's summary, which its own combined log
contradicts (rows labelled DEC-101/C-09 at R6, R15, R20, ...). Per Tiwa, the next playtest
will invalidate these run results anyway.

---

## 7. Systems Observation

### 7.1 Core Test Transaction (DEC-006)

All three ran the 9-step transaction on every test: Claude 307, Grok 88, GPT-5.6 2. No
transaction exception across ~400 combined Core Tests. Confirmed robust.

### 7.2 Overflow → HP (DEC-007 / DEC-007.A)

- **Claude:** 31 Overflow events, **all** landing on the roller's own HP — 604 HP to the PC,
  0 to the Troll. Emergent finding: the PC lost ~13.4× more HP to its own Overflow than to
  the Troll's Inflict Injury. Claude attributes this to `Cost = natural roll` (DEC-007) on a
  Tier-2 skill with growing value, against a 150-PE pool and Regen-70/test recovery, with a
  100-Fumble-capable d100.
- **Grok:** Overflow occurred as PC PE exhaustion from Round 6 onward, but Wounds carried the
  HP loss, so Overflow was not the dominant-kill factor.
- **GPT-5.6:** No Overflow (only 2 tests, both within PE pools).

**Finding:** Claude's Overflow-dominance observation is a real literal consequence of DEC-007
and is worth Tiwa's attention as a balance observation. However, its **quantitative dominance**
is conditional on the unresolved Wound-consequence model (see §6.1). If Wounds were to carry
direct HP magnitude (Grok's approach), the Overflow:Injury ratio would change substantially.

### 7.3 Skill Roll Pool Cascade (DEC-010) and Advanced Skills (DEC-012)

- **Claude:** sustained growth — Attack2 25→49, Defence2 25→45, Brawling 37→44; 13 failed
  Doubles created 8 PC + 5 Troll Advanced Skills (all Tier-3, starting value 1).
- **Grok:** 0 failed Doubles; no Advanced Skill creation (roll-variance).
- **GPT-5.6:** 1 failure XP cascade (Defence2 25→26) before abort.

Claude's 99-round run is the first to richly exercise DEC-010/012 growth and DEC-012 Advanced
Skill creation. Confirms those mechanics run without exception, and confirms the
"Current < Cap" stopping condition (DEC-016 Invariant 10).

### 7.4 Active Defense (DEC-044–050, DEC-097)

- Claude: 110 nested defense rolls, mitigation on success only.
- Grok: 31 defense/Active Defense rolls, including partial mitigation.
- GPT-5.6: defense failed (mitigation 0) but **the exchange blocked before Wound consequence**.

**Finding:** Active Defense is confirmed for the Injury branch. Its interaction with the Wound
branch is unresolved (§6.1 Gap B).

### 7.5 Wound / Location / Quality Gating

All three triggered the Wound pathway in Round 1 and exercised the quartile split
(Legs/Torso/Arms/Head). Claude: 76 Wounds, Tier distribution {2: 9, 3: 16, 4: 51} (Tier 4
dominant against the PC's low, Frightened-penalized Defence2). Grok: 14 Wounds. GPT-5.6: 1
(Q30→Torso→T4) then GM stop. The invocation path is confirmed; the consequence path is not.

---

## 8. Execution Methodology Comparison

| Aspect | Claude Sonnet 5 | Grok 4.5 | GPT-5.6 Luna |
|---|---|---|---|
| RNG | `random.SystemRandom()` (OS entropy), Python-computed | `random.Random(42)` fixed seed, Python-computed | `secrets.SystemRandom()`, Python-computed |
| Computation method | External Python, disclosed | External Python, disclosed | Python-computed, disclosed |
| Engine runtime | "well under one minute" | 0.000803 s (pure simulation) | Not captured (correctly not fabricated) |
| Core Test count | 307 total | 88 total | 2 total |
| Wound consequence applied | **No** (logged as records only; OPEN-007 scope note) | **Yes** as direct HP magnitude | **Blocked** (GM stop) |
| Exchange algorithm | Explicitly reconstructed & flagged for audit (§14) | Implicitly implemented | Rejected at Wound branch |
| Documentation quality | Excellent (summary + methodology note + JSON) | Excellent (full field set + JSON) | Excellent (rigorous stop + JSON) |

**Finding:** All three disclose RNG, computation, and Core Test counts — the v4 provenance
mandates were met by every executor. The decisive methodological difference is **not**
documentation but the difference in how each handled the unresolved Wound-consequence branch
(§6.1). Grok's disclosure that its engine runtime was a sub-millisecond *pure simulation*
(0.000803 s) is a useful clarification that reported runtimes are not wall-clock play time.

---

## 9. Recommendations for Future Playtests

### 9.1 Resolve the Blocker Before the Next Full Combat (highest priority)

The next intervention should **not** add another generic combat scaffold. The v4 run proves
that additional scaffolding risks masking the actual design dependency. Before another full
Ice Troll end-to-end combat is treated as valid, obtain a human ruling (or a tightly-scoped,
explicitly-flagged scaffold) for:

1. **Wound target selection** — which Attribute/Skill a given Wound Tier at a given anatomical
   zone affects and by how much.
2. **Active Defense vs Wound** — the deterministic transformation from Defender's Margin into
   a modification of Wound Tier/magnitude (or an explicit ruling that Active Defense does not
   modify Wounds).

These are the two questions GPT-5.6 escalated. Without them, completed runs differ in the
mechanism that actually ends the combat, so their conclusions are not comparable.

### 9.2 Standardize the Exchange Algorithm

Confirm (or correct) Claude's documented reconstruction of the combined melee-exchange
algorithm — attacker Core Test → defender Active Defense/S-1 roll → margin comparison →
Effect resolution (including pre-mitigation Quality for tier-gating) → Overflow independence.
Codify it so future runs apply an identical exchange procedure rather than re-reconstructing it.

### 9.3 Decide What a Wound Actually Does Before Comparing Lethality

Because the two completed runs (a) didn't apply Wound penalties (Claude) vs (b) applied Wounds
as direct HP (Grok) vs (c) aborted (GPT-5.6), **round count and HP-loss attribution are not
comparable** across v4 runs. Settle the Wound-consequence model first, then re-run for
comparable data.

### 9.4 Preserve the Good v4 Habits

Retain the four scaffolds (with mandatory logging), the mandatory output field set, RNG
disclosure, Core Test counting, PE-path tracking, per-repeat rows, edge-case logging, JSON
output, and mandatory Wound exercise. These all worked and materially improved audit quality.

### 9.5 Targeted DEC-101 Coverage — CLOSED via DEC-109 (2026-09-05)

Grok's v4 run already exercised DEC-101 in-spec (frequent defender-wins, complete,
no invention); DEC-101's 2 : 1 convergence is unchanged. Tiwa ruled OI-104 **closed as
resolved** — no forced-scenario or matched-defender test required as a prerequisite.
Claude's "gap" flag followed its own narrative summary, which its embedded log contradicts;
and per Tiwa, the next playtest will invalidate these run results anyway.

### 9.6 Note Claude's Overflow Observation (balance, not a rule change)

Flag Claude's self-inflicted-Overflow dominance to Tiwa as a balance/observation item. It is
mechanically literal under DEC-007 but is conditional on the unresolved Wound-consequence
model for its relative magnitude.

---

## 10. Open Items Requiring Human Decision

| ID | Issue | Source | Priority |
|---|---|---|---|
| ~~OI-101~~ | Wound target selection — which Attribute/Skill a Wound Tier at a zone affects | GPT-5.6 Finding F-06 (Gap A) | **RESOLVED via DEC-102 (2026-09-05)** |
| ~~OI-102~~ | Active Defense vs Wound — Defender's Margin modification of Wound Tier/magnitude | GPT-5.6 Finding F-07 (Gap B) | **RESOLVED via DEC-103/DEC-104 (2026-09-05)** |
| ~~OI-103~~ | Standardized melee-exchange algorithm (confirm/correct Claude's reconstruction) | Claude §14 methodology note | **RESOLVED via DEC-105 (2026-09-05)** |
| ~~OI-104~~ | DEC-101 coverage — need a matched or forced case to exercise defender-wins | Claude §8 coverage note | **RESOLVED via DEC-109 (2026-09-05) — closed as resolved: branch exercised frequently and in-spec by Grok 4.5's v4 run; no forced test required; next playtest supersedes these run results** |
| OI-105 | SC-XX action selection (carried over from v3) | v3 OI-002 / this synthesis | **RESOLVED via DEC-106 (2026-09-05) — Design Override of DEC-095 Step 3 for creatures/NPCs** |
| ~~OI-106~~ | Quality → Wound Tier numeric table (carried over from v3) | v3 OI-001 / this synthesis | **RESOLVED via DEC-107 (2026-09-05) — not-a-gap: Effect/Wound Tier = causing skill's Skill-Tier; no numeric Quality table; scaffold table invalidated** |
| ~~OI-107~~ | HP floor / negative-HP recording convention (carried over from v3) | v3 OI-003 / this synthesis | **RESOLVED via DEC-108 (2026-09-05) — HP uncapped, negative persists; DEC-052 trigger preserved; post-incapacitation accrual + target exclusion; revival gate = heal HP back to 0; wound-healing revival path retracted** |

**Note:** OI-101 is **RESOLVED** by Tiwa's designer ruling recorded as **DEC-102 (2026-09-05)** —
Target type (creatures/automated PCs = Attribute wounds only; players may choose Attribute or
Skill; Effect restrictions override), Attribute-wound target = the affecting Skill's Body
attribute(s) with random-vs-choice selection, Mind-only Skills cause Mind attribute wounds,
Skill-wound target = the skill sharing the most Attributes (highest value wins, random on tie),
and Attribute wounds trigger downstream base/recalcuation of Skills and HP/MP/Energy pools.
Source: `investigations/tiwas-wound-target-selection-designer-ruling-oi101-2026-09-05.md`.
OI-102 is **RESOLVED** by Tiwa's designer ruling recorded as **DEC-103/DEC-104 (2026-09-05)** —
Active Defense vs Effect resolves via the Skill-Tier comparison shred + margin de-escalation
(then carry rule; magnitude = negation buffer, survivor records natively Z = −Y, tier = triangular
negation cost; Effects only, never HP), and Inflict Injury (HP) resolves as contest-delta =
Winner's Margin − Defender's Margin.
Source: `investigations/tiwas-active-defense-effect-mitigation-designer-ruling-oi102-2026-09-05.md`.
OI-103 is **RESOLVED** by Tiwa's designer ruling recorded as **DEC-105 (2026-09-05)** —
a melee exchange is one S-1 opposed contest, both participants always roll (correcting
Claude §14's gated reconstruction); playtests = mandatory defense, live play = voluntary,
declined defense → attacker gets a normal Core Skill Test.
Source: `investigations/tiwas-melee-exchange-algorithm-designer-ruling-oi103-2026-09-05.md`.
OI-105 (SC-XX) is **RESOLVED** by Tiwa's designer ruling recorded as **DEC-106 (2026-09-05)** —
a Design Override of DEC-095 Step 3 for creatures/NPCs: base one substantive action per turn
for every combatant with GM fiat on multiple applicable skills; creature/NPC exception = GM fiat
when present, else all authored attack actions played highest→lowest Skill on the creature's own
turn back-to-back, nearest-possible-target priority (AoE = most targets possible); creatures/NPCs
may multi-attack by default unlike PCs; each attack is its own Core Test (Energy cost — a creature
may exhaust itself); automated playtest Characters are creatures (DEC-102).
Source: `investigations/tiwas-creature-npc-action-selection-designer-ruling-oi105-2026-09-05.md`.
GM Fiat universality remains pending — Tiwa: "GM Fiat should be universal but I will rule on that
once all the base systems have been designed and completed."
OI-106 is **RESOLVED** by Tiwa's designer ruling recorded as **DEC-107 (2026-09-05)** —
closed as **not-a-gap**: Effect Tier = the Skill-Tier of the skill used, Effect Magnitude =
Effect Tier, Wound Tier = Effect Tier (max, per DEC-035.A cl.2; default equal; lesser tier
only by Player choice + GM Fiat). Quality retains no numeric gating role (S-1 tie-break +
success precondition ≥1 only); the v4 scaffold table (`Q1–9=T1 … Q30+=T4`) is **invalidated
as scaffold artifact** — the 51 Tier-4 Wound records generated from the Ice Troll's
Skill-Tier-2 attacks were **not possible under this rule** (scaffold-invalid, annotated
2026-09-05). Future playtest statblocks must author Skill-Tiers consistent with the rule
(e.g., a Tier-4 Wound requires a Skill-Tier-4 attack or GM Fiat).
Supersedes DEC-035.B (Quality hard ceiling), DEC-099 (≥1/≥10 thresholds), and DEC-031's
Quality-gating clause; preserves DEC-035.A cl.2/cl.3, DEC-041, DEC-013, DEC-024, DEC-104
(HP channel unchanged), DEC-103.
Source: `investigations/tiwas-quality-wound-tier-skill-tier-designer-ruling-oi106-2026-09-05.md`.
OI-107 (HP floor / negative-HP recording convention) is **RESOLVED** by Tiwa's designer
ruling recorded as **DEC-108 (2026-09-05) — Option C: HP is uncapped** — raw negative
values persist (no clamp, no floor); the v4 "clamp to 0, preserve pre-clamp" test-scaffold
convention is superseded. DEC-052 (HP = 0 forced incapacitation) preserved unchanged as the
trigger. Post-incapacitation damage continues to accrue, but an incapacitated character is
no longer a "nearest possible target" for NPCs/creatures, and if all characters are
incapacitated combat ends. Revival gate: negative HP must be healed back to 0 before revival
is possible (via S-11 HP healing, DEC-071–074); the **wound-healing revival path was
RETRACTED** by Tiwa in-session — a Wound penalizes the underlying Attribute (DEC-102),
which recalcs the HP **maximum** down, so healing the Wound restores the maximum, not the
current pool, and cannot revive a negative-HP character. DEC-056 therefore remains **untouched**
(no healing/incapacitation interaction introduced).
Source: `investigations/tiwas-hp-floor-negative-hp-recording-convention-designer-ruling-oi107-2026-09-05.md`.
OI-104 (DEC-101 coverage) is **RESOLVED** by Tiwa's designer ruling recorded as **DEC-109
(2026-09-05)** — closed as **resolved (coverage satisfied)**: Grok's v4 run exercised the
defender-win branch frequently and in-spec ("Every defender-win produced 'attack fails, no
counter-Effect'"); no forced-scenario test required; DEC-101's 2 : 1 convergence unchanged.
Claude's "gap" flag is an internal-inconsistency artifact (its narrative says 0, its own
log labels R6/R15/R20 as DEC-101/C-09). Per Tiwa, the next playtest will invalidate these
run results anyway.
Source: `investigations/tiwas-dec101-defender-wins-coverage-designer-ruling-oi104-2026-09-05.md`.
Known-open (post-resolution): GM Fiat universality; DEC-108 carried-open corners (AoE
"most-targets" composition with post-incapacitation targeting exclusion; PC extension of
the exclusion).

---

## 11. Conclusion

The v4 Ice Troll Combat Playtest produced three deeply divergent outcomes from identical
stat blocks, identical scaffolds, and identical sequence: **99 rounds (Claude), 16 rounds
(Grok), and an abort in Round 1 (GPT-5.6)**. Unlike v3 — where differences were attributable
to attack selection and roll variance — the v4 divergence is structural and more important:
the three runs operationalized the **unresolved Wound-consequence branch** three different ways.

The v4 prompt succeeded at its procedural goals:

1. **Every v3 recording/convention gap was closed** and logged as a non-canonical scaffold.
2. **No run silently invented an attack-selection rule** — the biggest v3 governance failure.
3. **The Location/Wound *invocation* path was successfully reached** (all three runs).
4. **All provenance and documentation mandates were met** (RNG, computation, Core Test counts,
   PE path, JSON).

But the v4 run also proved that the playtest had **not yet reached the end of the Wound
chain**:

5. The Wound consequence — which Attribute/Skill a Wound targets (now **resolved via DEC-102**),
   and how Active Defense's Defender's Margin modifies a Wound — the second half remains
   undefined (OI-102).
6. As a direct result, the two "completed" runs ended via **invented-by-exclusion** mechanisms
   (no-Wound-penalty for Claude; direct-HP-magnitude Wounds for Grok), so neither is a valid
   end-to-end validation of the full consequence chain.
7. Claude's emergent self-inflicted-Overflow dominance is real but its *relative* contribution
   is conditional on the unresolved Wound model.
8. GPT-5.6's abort was the **correct** governance outcome: it reached farther than v3 runs,
   and rather than inventing the missing consequence, it stopped and escalated precisely.

**Net assessment:** v4 materially advanced the playtest infrastructure — closing every
procedural gap from v3 and reaching the Wound branch — and Tiwa has since ruled the Wound
*target selection* (DEC-102). The one remaining blocking design gap that prevents end-to-end
combat validation is the Wound/Active-Defense link (**OI-102**). The next step is a human
decision on OI-102 (and confirming the exchange algorithm, OI-103), after which a fresh
completed run can yield comparable data.

The synthesis confirms the multi-LLM cross-report methodology's value: a single run would not
have exposed the Wound-consequence divergence; the fact that one executor completed on
assumption A, one on assumption B, and one correctly stopped is exactly the kind of hidden
dependency cross-implementation comparison is designed to surface.

---

## 12. Document Status

**Status:** Playtest analysis — not canonical  
**Authority:** Advisory — requires human confirmation for any rule changes  
**Makes no rulings, assigns no DEC numbers, promotes nothing**  
**Next action:** Present OI-102 (Active Defense vs Wound) plus OI-103 (exchange algorithm) for
confirmation before any further full-combat playtest. OI-101 is **resolved** via DEC-102
(2026-09-05, designer ruling).  
**Canonical rule change:** None  
**Source documents analyzed:** 3 execution reports + v4 prompt + v3 synthesis template
