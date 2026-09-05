---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest Cross-Reference Report"
  version: "1.0"
  status: "Advisory working document (not canonical). Collation and comparative analysis of three independent playtest lineages. Makes no rulings, assigns no DEC numbers, promotes nothing."
provenance:
  author_llm: {name: "Grok", version: "4.5"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
source_reports:
  - "tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md (Grok 4.5)"
  - "tiwas-ice-troll-playtest-execution-handoff-claude-2026-09-04.md (Claude Sonnet 5)"
  - "tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md (GPT-5.6 Luna)"
governing_prompt: "claude-playtest-prompt-version2.md (v2.1)"
---

# Tiwas TTRPG — Ice Troll Combat Playtest Cross-Reference Report

**Document Type:** Formal Project Documentation / Comparative Playtest Analysis  
**Status:** Advisory — Non-Canonical  
**Date:** 2026-09-04  
**Authority Level:** Collation and evidence only. No new mechanics established. No DEC numbers assigned. No scaffolds promoted.

---

## 1. Purpose and Scope

### 1.1 Objective

Collate, compare, and cross-reference the three independent Ice Troll combat playtest executions performed against `claude-playtest-prompt-version2.md` (v2.1). Produce a single evidence base that identifies:

- Systems that functioned end-to-end under live resolution.
- Systems that required scaffolds or interpretive choices.
- Systems that remain unresolved or absent.
- Priority gaps that must be closed before a full adventure-scale playtest of *Beyond the Vale of Madness* (or any equivalent combat-heavy scenario) can be treated as mechanically complete.

### 1.2 Source Lineages (Must Not Be Conflated)

| Lineage ID | Executing LLM | Duration | Terminal State | Relationship |
|---|---|---|---|---|
| **L1 — Grok Full** | Grok 4.5 | 22 rounds | PC HP = 0 (incapacitated); Troll HP = 412 | Independent full run |
| **L2 — Claude Abort** | Claude Sonnet 5 | 2 rounds / 4 exchanges | Explicit abort; PC HP = 585; Troll HP = 698 | Independent short run |
| **L3 — Luna Continuation** | GPT-5.6 Luna | Continuation of L2 to termination | PC HP = 0 (incapacitated); Troll HP = 569 | Direct continuation of L2 state |

**Critical governance note:** L1 and L2+L3 are distinct empirical records. Outcomes must be compared by lineage, never averaged or treated as a single continuous combat.

### 1.3 Shared Constraints Across All Lineages

- Ice Troll v0.2 / DEC-077.A block used verbatim (or inlined copy).
- Regeneration / Regrowth / freezing DR 2 treated inactive.
- Adventurer-1 pre-authored Tier-2 Attack1 / Defence1 skills are **prompt-level scaffolds only** (DEC-012 exception; non-register-backed; no precedent).
- Scaffold values for missing numeric magnitudes authorized only under prompt rules; never promoted.
- No creative GM rulings permitted; genuine gaps produce GM-stops or conservative interpretations.

---

## 2. Comparative Outcome Summary

| Metric | L1 (Grok Full) | L2 (Claude Abort) | L3 (Luna Continuation) |
|---|---|---|---|
| Rounds / Exchanges | 22 rounds | 2 rounds / 4 exchanges | Continuation of L2 to R11 (approx.) |
| Final PC HP | 0 | 585 | 0 |
| Final Troll HP | 412 | 698 | 569 |
| Winner | Ice Troll | N/A (aborted) | Ice Troll |
| Advanced Skills created | 0 (no qualifying failed Doubles) | 1 (Exchange 3, 100-Fumble) | ≥1 additional (failed 99) |
| Frightened applied | Not selected | Yes (Tier-2, −2) | Carried forward from L2 |
| Wound applied | Not selected | Yes (Torso, Tier-2) | Carried forward / further |
| GM-stops triggered | 0 | 1 (passive Frightened trigger) | 0 additional (used existing) |
| Designer Override used | None | None | “Round 1, Exchange 1 — PC attacks” (playtest-only) |

**Observation:** Both complete lineages (L1, L3) reach the same terminal condition (PC HP = 0 under DEC-052). Net attrition rates differ because scaffolds for Inflict Injury and Active Defense mitigation differed between lineages.

---

## 3. Systems Exercised and Status Classification

Classification key:

| Label | Definition |
|---|---|
| **Exercised — Functional** | Pathway executed end-to-end under existing Ruled/Locked text; no scaffold required. |
| **Exercised — Scaffolded** | Pathway executed, but required a non-canonical numeric or substitution value. |
| **Exercised — Interpretive** | Pathway reached; corpus silent; conservative interpretation applied (no new numeric invented). |
| **Idle / Unexercised** | Available in corpus but not selected or triggered in these runs. |
| **Absent / Gap** | No Ruled procedure or content exists; would force GM-stop or further design. |

### 3.1 Core Resolution Layer (DEC-001–DEC-012)

| System | L1 | L2 | L3 | Consensus Status |
|---|---|---|---|---|
| d100 roll-under, 100-Fumble, Doubles | Functional | Functional | Functional | **Exercised — Functional** |
| Floor rounding (DEC-002) | Functional | Functional | Functional | **Exercised — Functional** |
| Derived statistics live (DEC-004) | Functional | Functional | Functional | **Exercised — Functional** |
| Skill Cap / Starting Value (DEC-005) | Functional | Functional | Functional | **Exercised — Functional** |
| 9-step Core Test Transaction (DEC-006) | Functional | Functional | Functional | **Exercised — Functional** |
| Cost = natural roll; Overflow → HP (DEC-007 / 007.A) | Functional | Functional | Functional | **Exercised — Functional** |
| Recovery floor(Regen/2) clamped (DEC-008) | Functional | Functional | Functional | **Exercised — Functional** |
| Failure XP → Skill Roll Pool cascade (DEC-009 / 010) | Functional | Functional | Functional | **Exercised — Functional** |
| Advanced Skill creation via failed Double (DEC-012) | Idle (no Double) | Functional (1 created) | Functional (≥1 created) | **Exercised — Functional** |

**Finding:** Core transaction layer is mature and reliable under combat load. Resource pressure, Overflow immutability, and Failure XP cascade all behaved as specified.

### 3.2 Opposed Contests and Combat Loop (S-1, S-3, S-6, S-7)

| System | L1 | L2 | L3 | Consensus Status |
|---|---|---|---|---|
| S-1 Universal Opposed Contest (DEC-013) | Functional | Functional | Functional | **Exercised — Functional** |
| Quality comparison (Margin / Blackjack / Hybrid) | Blackjack scaffolded | Used | Used | **Exercised — Scaffolded** (mode selection) |
| Base-tier Inflict Injury (DEC-023) | Scaffolded (flat 25 HP) | Scaffolded (winner Margin) | Scaffolded (winner Margin) | **Exercised — Scaffolded** |
| Active Defense post-hoc mitigation (DEC-044–050) | Scaffolded (−20 HP or full cancel) | Scaffolded (defender Margin / 0) | Scaffolded (defender Margin / 0) | **Exercised — Scaffolded** |
| Effect auto-apply + sequential Track A/B (DEC-027 / 034) | Functional | Functional | Functional | **Exercised — Functional** |
| HP = 0 forced incapacitation (DEC-052) | Functional | Not reached | Functional | **Exercised — Functional** |
| Quality ≥ 1 Base-tier floor (DEC-031) | Functional | Functional | Functional | **Exercised — Functional** |
| Gated-tier Quality unlock threshold | Not exercised | Scaffolded (≥10) | Scaffolded (≥10) | **Exercised — Scaffolded** |
| Defender-wins opposed attack Effect rights | Not reached | Interpretive (no counter-Effect) | Interpretive (no counter-Effect) | **Exercised — Interpretive** |

**Finding:** The opposed-contest primitive and Track A/B sequencing work. The combat *payload* (how much damage, how much mitigation, when gated Effects unlock) remains scaffold-dependent.

### 3.3 Location, Wounds, Conditions

| System | L1 | L2 | L3 | Consensus Status |
|---|---|---|---|---|
| Zero-Step Location Index (DEC-014) | Idle | Exercised | Exercised | **Exercised — Functional** (provider) |
| Anatomical zone ranges (DEC-041) | Idle | Scaffolded (quartiles) | Scaffolded (quartiles) | **Exercised — Scaffolded** |
| Wound creation (DEC-035.A/.B) | Idle | Functional | Functional | **Exercised — Functional** (architecture) |
| Wound consequences (OPEN-007) | Idle | Not fully exercised | Not fully exercised | **Idle / Gap** (consequences) |
| Frightened Condition (DEC-079) | Idle | Functional (via won Effect) | Carried | **Exercised — Functional** (application) |
| Passive / aura Frightened trigger | Deliberately avoided | GM-stop | Not re-triggered | **Absent / Gap** |

### 3.4 Creature / NPC Layer (S-12)

| System | Status Across Lineages |
|---|---|
| Ice Troll attribute / skill / derived values | Used as supplied; no re-derivation |
| Dedicated defensive skill on creature block | Absent → Brawling substituted (scaffold) |
| Regeneration / Regrowth / freezing DR | Inactive by disposition; never tested |
| Creature Trait framework beyond listed skills | Absent |

**Finding:** S-12 content authoring is a hard prerequisite for any non-scaffold combat. The v0.2 block is usable as a provisional template but incomplete (no dedicated defence skill; gated Traits inactive).

### 3.5 Action Economy / Sequencing

| System | Status |
|---|---|
| Initiative / turn order / round structure | **Absent / Gap** (all lineages required scaffold or Designer Override) |
| Number of actions per actor per exchange | Scaffolded (one attack each) |
| Timing of Active Defense relative to Effect | Functional under sequential Track A/B |
| Simultaneous declaration / ties | Unresolved |

**Finding:** DEC-082 expresses Time/Action economy constraints (Skill-side / Movement-penalty) but does not supply a sequencing procedure. This is the most frequently cited structural gap across all three lineages.

---

## 4. Scaffold Inventory (Cross-Lineage)

All values below are non-canonical. They must not be promoted.

| Gap | L1 Scaffold | L2/L3 Scaffold | Notes |
|---|---|---|---|
| Inflict Injury magnitude (Base-tier) | Flat 25 HP | Winner’s Margin | Different numerical philosophies; both produce playable attrition |
| Active Defense mitigation | −20 HP (or full cancel) | Defender’s Margin (0 on failure) | L1 produces slower net attrition; L2/L3 faster |
| Quality mode | Blackjack | Implicit Margin-style | DEC-013 permits choice; no locked default |
| Quality gated-tier unlock | Not used | ≥ 1 Base / ≥ 10 gated | DEC-031 silent on numeric threshold |
| Location-Tier-1 zones | Not used | 1–25 Legs / 26–50 Torso / 51–75 Arms / 76–100 Head | DEC-041 leaves ranges directional |
| Creature defensive skill | Brawling (Tier-1 ≈ 37) | Brawling (Tier-1) | Substitution only |
| Initiative / first actor | Higher Speed acts first | Designer Override (“PC attacks”) | Playtest-only; not general rule |
| Frightened magnitude | −10 (prepared, unused) | −2 (Tier-2 applied) | Different scales |

**Convergence:** All three lineages independently identified the same magnitude gaps (Inflict Injury, Active Defense mitigation, Quality threshold, location ranges, defensive-skill substitution). This is strong multi-model evidence that these are real corpus lacunae, not execution artefacts.

---

## 5. Unresolved Mechanics Register (Consolidated)

| ID | Subject | Evidence Sources | Classification | Blocking Impact for Full Playtest |
|---|---|---|---|---|
| U-01 | Inflict Injury (Base-tier) numeric magnitude | All three | Scaffold dependency | **Critical** — combat cannot be deterministic |
| U-02 | Active Defense mitigation numeric amount | All three | Scaffold dependency | **Critical** — defence loop incomplete |
| U-03 | Quality → gated-tier unlock threshold | L2, L3 | Scaffold dependency | **High** — Condition / Position / Equipment Effects gated |
| U-04 | Location-Tier-1 coarse-zone numeric ranges | L2, L3 | Scaffold dependency | **Medium–High** (if location-referencing Effects used) |
| U-05 | General combat action sequencing / initiative | All three | Absent procedure | **Critical** — every combat requires ad-hoc order |
| U-06 | Passive / aura Frightened trigger | L2 (GM-stop), L1 avoided | Absent subsystem | **High** for Ice Troll / Blood Man fidelity |
| U-07 | Defender-wins opposed attack → Effect rights | L2, L3 | Interpretive gap | **Medium** — frequency depends on roll outcomes |
| U-08 | Creature dedicated defensive skill | All three | Content gap in v0.2 block | **Medium** — substitution works but is not design |
| U-09 | Wound consequences catalogue (OPEN-007) | All (idle or partial) | Not table-ready | **Medium** — “wounded” state incomplete |
| U-10 | Regeneration / Regrowth activation & magnitude | All (inactive) | Trait + magnitude missing | **Medium** for Ice Troll fidelity |
| U-11 | S-3 gated-tier Effect content enumeration | Structural only | Design-stage | **Critical** for grapple, darkness, ongoing damage, etc. |

---

## 6. Systems Confirmed Ready for Broader Playtest Use

The following can be treated as operational under current Ruled/Locked text for any subsequent combat or exploration playtest that stays within their scope:

1. Full 9-step Core Test Transaction (including Cost, Overflow immutability, Recovery).
2. Failure XP → Skill Roll Pool cascade and Cap-limited advancement.
3. Advanced Skill creation on failed Double (DEC-012).
4. S-1 Opposed Contest outcome matrix (including Fail/Fail repeat).
5. Track A (attacker Cost/Overflow) / Track B (won Effect) sequential application.
6. HP = 0 forced incapacitation (DEC-052).
7. Zero-Step Location Index numeric provider (DEC-014).
8. Frightened Condition application when produced as a won S-1 Effect (DEC-079).
9. Wound creation architecture (DEC-035) once a magnitude source exists.

These form a stable resolution kernel. They are not the complete combat system.

---

## 7. Priority Development Sequence for Full Adventure Playtest Readiness

Ranked by impact on the ability to run the Ice Troll and Blood Man encounters (and by extension any comparable combat set-piece) without scaffolds or GM-stops.

| Priority | Work Item | Rationale | Minimum Deliverable |
|---|---|---|---|
| **P0** | Combat action sequencing procedure | Every lineage required an ad-hoc order rule before Round 1 could begin | Explicit initiative / exchange construction rule (or formal Designer Override scope) |
| **P0** | Inflict Injury magnitude formula (Base-tier) | Core attack payload undefined | Locked formula or Quality-scaled table |
| **P0** | Active Defense mitigation formula | Defence loop undefined | Locked formula or table |
| **P1** | S-3 gated-tier Effect content (minimum set) | Grapple, ongoing damage, darkness, fear, position required by adventure | Enumerated Effects for Grapple/Break Hold, Condition (Frightened, Darkness, Wounded), ongoing damage delivery |
| **P1** | Quality gated-tier unlock threshold | DEC-031 silent | Single numeric threshold or table |
| **P1** | Passive Condition triggers (Frightened aura) | Adventure and Ice Troll Appearance demand it | Trigger rule or explicit “won-Effect only” confirmation |
| **P2** | Location-Tier-1 zone ranges | Required if any location-referencing Effect is used | Locked quartile or weighted table |
| **P2** | Creature defensive-skill convention | v0.2 block incomplete | Template rule or mandatory Defence skill field |
| **P2** | Wound consequences (OPEN-007) | “Wounded” state currently label-only | Penalty / healing-cost catalogue |
| **P3** | Regeneration / environmental Trait activation | Ice Troll fidelity | Timing + magnitude + environmental Tag interaction |
| **P3** | Equipment / weapon attack payloads | Adventure assumes weapons | Minimal Tag + Effect payload model |
| **P3** | Environmental hazard magnitude (falls, cold) | Adventure survival layer | Hazard → Effect / HP procedure |

Magic remains optional for a non-spellcaster diagnostic run but is required if the Enfys pregen is retained.

---

## 8. Cross-Lineage Consistency Observations

1. **Core engine robustness:** All three lineages confirm that the d100 Core Test, resource accounting, Overflow, Failure XP, and Advanced Skill generation survive multi-exchange combat pressure without contradiction.
2. **Magnitude divergence:** L1 (flat 25 / −20) produces slower attrition than L2/L3 (Margin-based). Both are internally consistent; neither is canonical. A locked formula is required before results can be compared quantitatively across future playtests.
3. **Scaffold convergence:** The same five numeric gaps (Injury, Mitigation, Quality threshold, Location zones, defensive-skill substitution) appear in independent executions. This is strong evidence of genuine design incompleteness rather than model-specific invention.
4. **Initiative gap universality:** Every lineage required either a scaffold or a Designer Override to begin. DEC-082 does not close this.
5. **Passive trigger gap confirmed live:** L2 produced an explicit GM-stop on the Frightened aura; L1 deliberately avoided the trigger. The gap is real.
6. **DEC-012 exception discipline:** All three reports correctly isolate the pre-authored Tier-2 PC skills as playtest-only scaffolds and refuse to treat them as precedent.

---

## 9. Governance Compliance Summary

| Constraint | Observed Compliance |
|---|---|
| No scaffold promoted to canonical | All three reports explicit |
| Designer Override scoped to playtest only | L3 correctly limited |
| No automatic DEC assignment | All three reports explicit |
| DEC-012 exception provenance preserved | All three reports carry the note |
| Lineages kept distinct | Documentarian notes already separate L1 from L2→L3 |
| GM-stops recorded rather than papered over | L2 recorded passive Frightened stop |

No lineage violated the standing “reconfirmation-before-recording” rule.

---

## 10. Recommendations for Next Project Actions

1. **Do not** treat any scaffold value from these reports as a candidate for automatic promotion.
2. **Present** U-01 through U-11 (or the prior CANDIDATE-01…09 set) to Tiwa as individual ruling items.
3. **Author** a minimal combat sequencing rule (or formal temporary override protocol) before any further multi-round combat playtest.
4. **Lock** Base-tier Inflict Injury and Active Defense mitigation formulas as the highest-leverage single design actions.
5. **Enumerate** the minimum S-3 Condition and Grapple Effects required by the Blood Man set-piece before claiming adventure readiness.
6. **Update** the Ice Troll (and Blood Man) conversion blocks with an explicit defensive skill field once the convention is ruled.
7. **Retain** the three lineages as separate empirical records in the investigation archive; cross-reference by lineage ID only.

---

## 11. Conclusion

The three Ice Troll combat playtests collectively demonstrate that the Tiwas Core Test and S-1 opposed-contest architecture are stable under sustained combat load. They also demonstrate, with multi-model convergence, that the combat *payload* layer (damage magnitude, defence mitigation, gated Effect thresholds, action sequencing, passive Condition triggers) remains incomplete.

A full mechanical playtest of *Beyond the Vale of Madness* (or any equivalent combat-and-hazard module) is blocked primarily by:

- absence of a combat sequencing procedure,
- absence of locked numeric magnitudes for Injury and Active Defense,
- incomplete S-3 gated-tier Effect contents,
- missing passive Condition triggers,
- incomplete creature template fields.

Until those items receive designer rulings and are recorded under the project’s formal promotion process, any further combat execution must continue to carry explicit scaffold and interpretive-gap declarations.

**This report establishes no new canonical mechanics.**

---

## 12. Source Register

| Document | Role |
|---|---|
| `tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md` | L1 empirical record (Grok 4.5) |
| `tiwas-ice-troll-playtest-execution-handoff-claude-2026-09-04.md` | L2 empirical record + candidate list (Claude Sonnet 5) |
| `tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md` | L3 continuation record (GPT-5.6 Luna) |
| `claude-playtest-prompt-version2.md` (v2.1) | Shared execution specification |
| `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` | Authority baseline for Ruled/Locked status |
| `AGENTS.md` | Agent operating constraints (authority, promotion, no silent invention) |

---

**End of report.**
