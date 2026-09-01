# Tiwas-TTRPG — Task-Scoped Consolidated Snapshot for Claude (Advisory Session)

---
document:
  title: "Task-Scoped Consolidated Snapshot — Claude Advisory Session"
  version: "4.0"
  status: "Dated task-scoped working snapshot (NOT the authoritative corpus; NOT a standing merge artifact)"
  scope: "Single decision-making session. Consumed cold by Claude (advisory design assistant, no repo access). Curated per task; superseded by the live repository at all times."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-01"
  last_modified_date: "2026-09-01"
---

## Standing-prohibition overrule (one-line log entry)

Tiwa has **explicitly and consciously** overridden the earlier standing "do not create another single merged file" prohibition, **for this one working session only.** This snapshot is a **dated, task-scoped exception** — it is NOT a reinstatement of `TTTRPG-merge-v2.md` as a standing artifact, and future agents must NOT assume the prohibition applies generally. This overrule is scoped to the single file below and to this session's curation, per Tiwa's direct instruction as human designer/ruling authority.

---

# 1. Purpose of This Snapshot

You (Claude) are reading this **cold** at the start of a decision-making work session, with no prior memory and no repository access. Tiwa is moving away from giving you broad/standing corpus access (GitHub Project integration, periodically-regenerated full merge file) because both produced stale, bloated, or unverifiable context, and because standing access let contamination from other LLMs' unrelated-game assumptions go unchallenged. **Tiwa will relay to you, separately, the specific open design decisions to advise on; you will give advisory opinions; Tiwa will verify them with OpenCode (live repo access) before anything is recorded.**

This snapshot gives you:
1. Every **currently Open** decision in the register, each with its full **upstream Ruled/Locked dependency chain**.
2. The **governance framework** you need to interpret status vocabulary, authority, and provenance correctly.
3. The **current formal-reporting/provenance standard** for any document you produce this session — sourced **verbatim**, not reconstructed.

**This file is NOT the authoritative corpus.** It is a curated, dated snapshot. Anything downstream must treat the live repository as ground truth. Flag any discrepancy you cannot resolve from this file rather than guessing.

### Session-closure addendum (2026-09-01, after the advisory session)

The open items in §3 of this snapshot were **ruled and recorded in the live register** on 2026-09-01, superseding their status as stated below:
- **OPEN-009** → resolved via **amendment to DEC-050** (Active Defense targets any/all auto-applied Effects, incl. positive, voluntary) — closed.
- **OPEN-010** → resolved via **DEC-075** (no fatigue penalty beyond Cost/Overflow; future fatigue = Condition-tier Effect) — closed.
- **S-12** → ruled via **DEC-076** (stat-generation mode fork) and **DEC-077** (content deferred to Tiwa's playtesting).
- **OPEN-005** → **closed** (S-12's sole mechanical dependency DEC-041 §5 satisfied; remainder is content authoring).

**No fork-level Open item remains** in the register's OPEN-005/009/010 set. The only remaining non-fork tracking item is the S-3 gated-tier Effect *content* enumeration (structure locked DEC-023; contents unwritten). Source record: `investigations/tiwas-s6-s12-session-handoff-2026-09-01.md`. For ground truth consult the live `_consolidation/decision-register.md`.

---

# 2. Authority Hierarchy & Status Vocabulary (verbatim, core)

## 2.1 Authority hierarchy (from `governance/authority.md`)

The repository is organized as:

1. **`canonical/` (D1) — Canonical Rules & Changelog.** The sole source of locked game mechanics. Per its own §0.1 the (2) Proposals and (3) Roadmap "cannot override" this document. A mechanic reopens only through formal governance, never through implementation convenience, LLM preference, or repetition.
2. **`roadmap/` (D2) — Implementation Roadmap & Project Governance.** Explicitly disclaims rule authority ("Rule Authority: None — this document does not create game mechanics"). Governs sequencing, dependencies, simulation gates, regression requirements, LLM/documentation process rules. Never a source of game mechanics.
3. **`proposals/` (D3) — Proposals, WIP & Design Direction.** Explicitly "Non-Canonical Design Repository... Design exploration only." Contains real designer rulings (see register §B) but those rule *candidate, non-canonical* material, not the Canonical ruleset, until the 8-step Promotion Rule is completed.
4. **`investigations/` (D4, D5) — design investigations feeding Proposals/WIP.** Evidentiary and analytical work product. Never self-executing — require designer/human ruling before anything they contain affects even the non-canonical Proposals/WIP layer, and never claim any effect on Canonical Rules.

## 2.2 Status vocabulary (from `governance/status-model.md`, D1's own header)

- **Canonical / Locked** — authoritative, current, must not be contradicted by downstream design/implementation.
- **Reserved** — a known required subsystem with no settled implementation yet.
- **Historical / Superseded** — retained for understanding, no longer current.

### Expanded vocabulary used in Proposals/WIP (D3 §0)

| Status | Meaning |
|---|---|
| Proposed | A candidate rule under active consideration |
| WIP | Currently being developed or reviewed |
| Experimental | Tested/invented for exploration but explicitly excluded from the ruleset |
| Design Direction | An architectural or philosophical preference, not necessarily a mechanic |
| Reserved | Known required subsystem with no settled implementation |
| Superseded | Historical material retained for understanding but no longer current |

**None of Proposed / WIP / Experimental / Design Direction / Reserved / an "observation" is a locked rule (D3 §0 explicit instruction).**

## 2.3 Status lifecycle (D2 §23.1)

```
Idea → Proposal → WIP → Independent Review → Simulation/Analysis → Designer Ruling → Accepted → Locked/Canonical
```

An item may return to WIP if evidence exposes a substantive problem.

## 2.4 The Promotion Rule (D3 §21) — the ONLY path from non-canonical to canonical

1. The design question is explicitly identified.
2. Competing alternatives have been considered where appropriate.
3. Relevant simulation/analysis has been completed.
4. The human designer has accepted the ruling.
5. The mechanic is documented as a formal rule.
6. The Canonical Rules & Changelog document is updated.
7. The former proposal is marked Superseded or Locked in its source document.
8. Implementation documentation is updated.

**No item currently in `proposals/` or `investigations/` has completed this process.** A detailed proposal, however fully described, is not a rule merely because it is detailed (D3 §21). None of the rulings referenced in §3 below are Canonical — they are all **Non-canonical designer rulings** (or Locked Canonical mechanics where explicitly noted).

---

# 3. Open Decisions in the Register — with their full upstream Ruled/Locked chains

The live decision register is `_consolidation/decision-register.md`. This section restates every **currently Open** item, and each one's upstream dependencies, so you can reason about any open fork without guessing.

## 3.0 Canonical / Locked foundation you must treat as fixed (and may not contradict)

From `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`. These are **Canonical / Locked** (register Section A, DEC-001…DEC-016). Any advisory opinion you give on an open S-item must preserve these:

| # | Mechanic | Locked statement (verbatim/close) |
|---|---|---|
| DEC-001 | d100 resolution | Roll-under on 1–100; `00`=100; 100 always fails and always qualifies as a failed Double (D1 §2.1–§2.4) |
| DEC-002 | Rounding | All fractions floor, no exceptions (D1 §2.5) |
| DEC-003 | Attributes | 24 independently generated (12 Body / 12 Mind), each 1d100 (D1 §3) |
| DEC-004 | Derived stats | HP=ΣBody; MP=ΣMind; PE=bep+bes+bee; Speed=bsp+bss+bse; EnergyRegen=bep+bes; MPRegen=mep+mes; MoveSpeed=floor((bsp+bss)/15); live-recalc (D1 §4) |
| DEC-005 | Skill Tier/Cap/Value | Tier=#distinct attrs in formula; Cap=floor(avg); Start=floor(Cap/2), may be 0 (D1 §5) |
| DEC-006 | Core Test Transaction | Fixed 9-step: roll→outcome→cost→overflow→failure XP→doubles→recovery; no subsystem may replace it (D1 §6) |
| DEC-007 | Resource cost & Overflow | Cost=natural roll; insufficient→Overflow→direct HP damage; no second pool (D1 §7) |
| DEC-007.A | Overflow-immutability clause | **Amendment (designer-approved, 2026-09-01):** "Overflow (the HP damage resulting from insufficient resource to cover a test's natural-roll Cost) is a pure function of the natural roll and the resource pool at time of test. No Tag, Trait, Effect, Condition, or subsystem may reduce, redirect, absorb, or otherwise modify Overflow's magnitude or application to HP." Placed as amendment to DEC-007 (not a new Invariant). Gap-closer making explicit what DEC-007/Invariant 7 already imply — checked against Invariants 6/7 for contradiction: none found. **Corollary:** Armor Tags never modify Overflow (Item B; no separate DEC needed). |
| DEC-008 | Recovery | floor(Regen/2), clamped, always final step, unconditional (D1 §8) |
| DEC-009 | Failure XP | max(0, Roll − Skill) (D1 §9) |
| DEC-010 | Skill Roll Pool | Temporary, single-test-scoped; cascading while affordable; capped at Cap; remainder→General XP (D1 §10) |
| DEC-011 | General XP | May exceed Cap; +1 cost = current value; no partial advancement (D1 §11) |
| DEC-012 | Advanced Skills | Only on qualifying failed Double; Tier+1; full-formula Cap recompute; lineage resource domain (D1 §12) |
| DEC-013 | S-1 Opposed Contest | Universal primitive; outcome matrix; Margin/Blackjack/Hybrid Quality; Failure/Failure repeat; exact-tie repeat (D1 §13) |
| DEC-014 | S-2 Tier-1 Location Index (Zero-Step) | Deterministic tens/units digit exchange on natural roll; no player choice; read-only post-process; does not alter Core consequences (D1 §14.1–§14.2). **Limited scope only** (D1 §14) |
| DEC-015 | Reserved Systems | Everything not locked (hit-location beyond Tier-1, wounds, Effects, armor, defense, incapacitation, death, healing, Rest, equipment, etc.) outside locked Core (D1 §15) |
| DEC-016 | Architectural Invariants | 18 invariants binding all future subsystem work (D1 §16) |

### The 18 Core Architectural Invariants (D1 §16) — binding on every open subsystem

1. d100 produces 1–100.
2. 100 always fails.
3. 100 is a qualifying failed Double.
4. All fractions floor.
5. Success is roll-under.
6. Cost equals the natural roll.
7. Overflow becomes HP damage.
8. Failure XP uses `max(0, Roll − Skill)`.
9. Skill Roll Pool is temporary.
10. Skill Roll Pool advancement cannot exceed Cap.
11. General XP can exceed Cap.
12. Failed Doubles can create Advanced Skills.
13. Advanced Skill Caps are recalculated from the full attribute set.
14. Advanced Skill resource domain follows lineage.
15. Derived statistics are live.
16. Recovery occurs last.
17. No Universal Play subsystem may introduce a competing primary resource or progression economy.
18. Universal Play modules must build on the Core Test Transaction rather than replace it.

## 3.1 OPEN-005 — S-5 to S-12 subsystem content (the umbrella open item)

**Open.** All S-5…S-12 were originally Open/Reserved/Proposed — no locked mechanic for any of them. **Current state of the umbrella (updated from prior snapshot):**

- **S-5** Armor is **Ruled** (DEC-058…DEC-062) — all five forks resolved.
- **S-6** Defense is **Ruled** (DEC-044…DEC-050) — Active Defense, all seven forks resolved.
- **S-7** Incapacitation/Death is **Ruled** (DEC-052…DEC-057) — all six forks resolved.
- **S-8** Difficulty/Skill-modification is **Ruled** (DEC-063…DEC-066); S-8 Stakes Gate rejected (DEC-051).
- **S-9/S-10** Extended Tests is **Ruled** (DEC-067…DEC-070).
- **S-11** Rest/Healing is **Ruled** (DEC-071…DEC-074).
- **S-12** Creature/Campaign content — **still Open.** Content dependency on S-4/S-41 anatomical mapping (DEC-041 §5 — individual creature templates per creature type).

**OPEN-005 remains open only because S-12 has no settled mechanic.**

### Per-subsystem current state

| Subsystem | Subject | Upstream deps | Status | Existing concrete material |
|---|---|---|---|---|
| **S-5** | Armor | S-3, S-4 | **Ruled (non-canonical)** | DEC-058…DEC-062 (see §3.2 below) |
| **S-6** | Defense | S-1 | **Ruled (non-canonical)** | DEC-044…DEC-050: Active Defense (defender rolls genuine Core Test); voluntary decline allowed; uncapped; Model B (post-hoc mitigation on already-applied Effect, DEC-027 preserved); separate mitigation per Effect; universal defensible-Effect eligibility. |
| **S-7** | Incapacitation/Death | S-4 | **Ruled (non-canonical)** | DEC-052…DEC-057 (see §3.3 below) |
| **S-8** | Difficulty/task/stakes | Core | **Ruled (non-canonical)** | DEC-063…DEC-066 (see §3.4 below); DEC-043 (3rd-party adjudication) ruled; DEC-051 Stakes Gate rejected. |
| **S-9/S-10** | Extended Tests | — | **Ruled (non-canonical)** | DEC-067…DEC-070 (see §3.5 below). DEC-039 ruled Final-roll-governs for Location Index provenance in Extended Tests. |
| **S-11** | Rest/Healing | S-4, S-7 | **Ruled (non-canonical)** | DEC-071…DEC-074 (see §3.6 below). S-11 healing is a literal instance of S-9/S-10 Extended Tests. |
| **S-12** | Creature/Campaign content | S-4 (DEC-041 anatomical mapping) | **Open** | Creature coverage: individual templates per creature type (DEC-041 §5); content dependency. No further concrete material. |

## 3.2 S-5 Armor — ruled 2026-09-01 (DEC-058…DEC-062, all non-canonical)

**Upstream dependencies:** DEC-013 (S-1 Opposed Contest), DEC-032…DEC-037 (S-4 Wound/Injury), DEC-023…DEC-030 (S-3 Effect menu and gating), DEC-028/030 (Tag+Location-gated Effects), DEC-006/007 (Core Test/Cost/Overflow).

| DEC | Fork | Ruling |
|---|---|---|
| DEC-058 | S5-A — Armor architecture | **Tags/Traits system only.** No numeric durability/soak pool. Structurally identical in kind to item Tags generally, applied to defensive gear. Never interacts with Overflow. **Corollary:** Armor Tags never modify Overflow under any circumstance (consequence of S5-A + DEC-007 amendment). |
| DEC-059 | S5-B — Bypass definition (consolidated with post-hoc amendment) | **Relational property between specific Tag pairs.** An Armor Tag's rule text may specify it does not trigger against Effects carrying a designated other Tag. Requires **both** a Tag-pairing match **and** a location match (amended after S5-E). Stateless; neither Tag is altered. **Inapplicable at Location Tier 0.** |
| DEC-060 | S5-C — Sunder Effect (addition model) | **Exists; Addition model** — an Impose Condition Effect adding a "Sundered" Tag to the armor item (does not remove/delete any existing Tag); **permanent** — persists until deliberately addressed, no automatic reversion; resolved via the **ordinary Core Test Transaction** (DEC-006, 9-step). Sunder is a **selectable** Effect (actor chooses it from among available options on a qualifying roll). **Menu placement:** Condition tier of the S-3 Effect menu (open to additions, per Dizzy precedent), gated on Conditions subsystem lock. |
| DEC-061 | S5-D — Armor resolution sequence vs. Active Defense (consolidated with amendment/supersession) | **Armor resolves before Active Defense.** Sequence: Effect auto-applies (DEC-027) → checked against Armor Tags (including Bypass relational matching) → surviving Effect magnitude/state then subject to Active Defense mitigation (Model B, DEC-048) as a separate pass, consistent with DEC-049. **Final operative rule per S5-E supersession:** intermediate amendment ("Tier-0 location hits can never bypass") fully superseded by Zero-Step clause under S5-E — Armor check is location-bound but uses single-purpose Zero-Step read at Tier 0, so Tier promotion is never forced by Armor's presence alone. |
| DEC-062 | S5-E — Armor coverage location-bound + Zero-Step clause (consolidated with amendment) | **(E1)** Armor coverage is **location-bound** — a given Armor Tag protects only specified location(s), not the whole target uniformly. **(E2)** Armor uses the **same fine-grained individual-creature-template anatomy** as DEC-041 — full reuse, no separate coarser coverage-zone system. **Amendment (Zero-Step Armor-location clause):** when an attack roll against an Armor-wearing target is resolved at Location Tier 0, the struck location for **Armor-coverage-check purposes only** is derived via the existing DEC-014 Zero-Step digit-exchange procedure — read-only, off the natural roll already made, no new roll, no player choice, does not promote Tier, does not persist, discarded immediately after the Armor check resolves. Preserves DEC-040's Tier-0-as-default intact; Armor's presence never forces Tier promotion. Bypass remains inapplicable under this path (its location-match condition requires tracked Tier 1/2 context). |

### S-5 Remaining open item

- **S5-C S-3 Effect menu placement for Sunder** — pending OpenCode's live-repository confirmation before the menu placement is finalized. If S-3's menu structure is closed/fixed-cardinality or has an incompatible selection-gating rule, this needs to come back to Tiwa. (Source: `investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` §4 Item C.)

## 3.3 S-7 Incapacitation/Death — ruled 2026-09-01 (DEC-052…DEC-057, all non-canonical)

**Status:** These rulings have been **recorded in the live register** (DEC-051–057) and committed. The source handoff report (`investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md`) is a **DRAFT** pending Tiwa's explicit reconfirmation of each fork before it carries any documentary weight beyond that handoff. **Treat the DEC entries as the operative source; the handoff is a draft working record, not the register.**

**Upstream dependencies:** DEC-035 (Wound severity), DEC-032 (Injury/Wound terminology), DEC-006/007/008 (HP/Cost/Overflow/Recovery). **Design philosophy the rules embody:** heroic resilience; HP=0 ≠ death; incapacitation distinct from ordinary resource depletion; permanent loss comparatively uncommon.

| DEC | Fork | Ruling |
|---|---|---|
| DEC-052 | 1 — HP=0 state | **HP = 0 triggers forced incapacitation.** No roll, no save/check. Replaces prior directional "HP = 0 should not automatically mean death". |
| DEC-053 | 2 — Wound/Incapacitation relationship | **Independent.** Incapacitation is HP-driven ONLY; Wound severity (DEC-035) does not feed into it. Supersedes the old §7 line "serious localized injury may matter where locations are active". |
| DEC-054 | 3 — Permanent loss (death) | Occurs when EITHER: (a) incapacitated AND **all attempts to revive via skill tests have failed** (unlimited attempts; no cap), OR (b) **player voluntarily chooses** permanent loss while incapacitated. |
| DEC-055 | 4 — Stabilization procedure | **GM discretion, no formal procedure.** GM decides which skill, how many attempts, pacing — but NOT whether skill tests are used at all (that is fixed by DEC-054). |
| DEC-056 | 5 — S-11 interaction | **No interaction.** Incapacitation is HP-driven; does not affect S-11 healing/recovery. |
| DEC-057 | 6 — S-2 reopening-trigger closure | **Session-level assessment:** S-2 non-attack deferral reopening pathway assessed as removed (single HP=0 trigger, no Wound/location dependency). Advisory only — NOT a formal re-verification of DEC-037. |

## 3.4 S-8 Difficulty Grades & Skill-Side Modification — ruled 2026-09-01 (DEC-063…DEC-066, all non-canonical)

**Upstream dependencies:** DEC-016 (Architectural Invariants, esp. #6/#10), DEC-010 (Skill Roll Pool), DEC-006/007/009 (Core Test/Cost/Failure XP). **Key design constraint:** Difficulty modifiers act on the Skill side only — never on the natural die roll (Invariant 6 preserved). DEC-065 B1+C2 together require **no amendment to any Core Invariant** (Invariant 10 preserved exactly as currently worded).

| DEC | Fork | Ruling |
|---|---|---|
| DEC-063 | S8-A — Difficulty grade structure | **Named tiers with fixed additive Skill-side modifiers.** Named tiers (e.g., Trivial/Easy/Standard/Hard/Extreme) with fixed additive modifiers to effective Skill. Modifiers act on the Skill side only — never on the natural die roll. |
| DEC-064 | S8-B — Difficulty-modified Skill usage scope | **Effective Skill used for all three Skill-side values.** The difficulty-modified (effective) Skill is used for: (1) the success/fail check, (2) Failure XP calculation, AND (3) as the comparison value entering the Skill Roll Pool cascade. Supports advancement past Skill 100; high-risk/high-reward design intent. **Must be recorded with DEC-065 to preserve Invariant 10.** |
| DEC-065 | S8-C — Skill Roll Pool cascade cap (**supersedes revoked C1**) | **Effective Skill CLAMPED at permanent Cap for cascade stopping condition.** The cascade cannot push a character's permanent Skill above their normal Cap, regardless of difficulty bonus. Any Pool XP beyond what the cascade can spend before hitting Cap spills into General XP (DEC-011). **Preserves Invariant 10 exactly.** An earlier C1 selection was revoked by Tiwa mid-session; only C2 is operative. |
| DEC-066 | S8-D — Difficulty grade symmetry | **Symmetric grades.** Difficulty grades apply symmetrically — both bonuses (easier tests) and penalties (harder tests) — rather than penalty-only. |

## 3.5 S-9/S-10 Extended Tests — ruled 2026-09-01 (DEC-067…DEC-070, all non-canonical)

**Upstream dependencies:** DEC-006/007/009 (Core Test/Cost/Failure XP), DEC-016 Invariant #17. **Key design constraint:** monotonically-increasing Margin total has no spending dynamic, so Invariant-17 is not at risk (DEC-069 coherence assessment).

| DEC | Fork | Ruling |
|---|---|---|
| DEC-067 | S9-A — Progress method | **Margin-accumulation.** Each successful interval's Margin (Skill − Roll) adds to a running total; failures contribute nothing. Monotonically increasing; never decreases. |
| DEC-068 | S9-B — Failure behavior | **Neutral.** A failed interval costs resources and generates ordinary Failure XP per DEC-006/007/009, but does not reduce or reset the accumulated progress total. |
| DEC-069 | S9-C — Invariant-17 coherence assessment | **No Invariant-17 violation.** The A2+B1 combination has no income/expenditure ("spending") dynamic and cannot be mistaken for a competing resource pool. Assessment covers this combination only; does not generalize to other B-fork choices. |
| DEC-070 | Completion target | **GM discretion, no formula.** The numeric target a Margin-accumulation total must reach is set entirely at GM discretion, per-instance, with no formula and no fixed default. Precedent: DEC-055. |

## 3.6 S-11 Rest/Healing — ruled 2026-09-01 (DEC-071…DEC-074, all non-canonical)

**Upstream dependencies:** DEC-006/007/009 (Core Test/Cost/Failure XP), DEC-067/068/070 (S-9/S-10 Extended Tests), DEC-056 (S-7 independence from S-11). **Key design decision:** S-11 healing IS a literal instance of the S-9/S-10 Extended Test subsystem (Tiwa's own proposal, not Claude's recommendation).

| DEC | Fork | Ruling |
|---|---|---|
| DEC-071 | S11-A — Resolution method | **Explicit Skill Test required.** Healing during a Rest period requires a full, ordinary 9-step Core Test per DEC-006 — not passive/automatic HP restoration. |
| DEC-072 | S11-B — Wound magnitude penalty | **Penalty on healer's effective Skill.** Wound magnitude penalizes the healer's effective Skill for the healing test — same mechanism pattern as DEC-064 (S8-B) — rather than altering the natural roll, resource Cost, or HP amount restored directly. |
| DEC-073 | S11-C — S-11 as literal Extended Test instance | **S-11 healing IS an Extended Test instance.** One Rest period = one Extended Test interval; each interval is an ordinary Core Test with DEC-072's wound-magnitude Skill penalty applied; progress accumulates via DEC-067 (Margin-accumulation); failures are neutral per DEC-068; completion target follows DEC-070 (GM discretion, no S-11-specific override). Tiwa's own proposal. |
| DEC-074 | S-11 healing completion target | **GM discretion, generally — no HP-deficit lock.** The completion target remains general GM discretion — same as DEC-070 — and is NOT locked to "HP deficit" as a required or default target. |

## 3.7 OPEN-009 — S-6 positive-Effect Active Defense mitigation

**Open — deferred.** Raised by DEC-050's universal-eligibility ruling: since any auto-applied Effect is eligible for Active Defense mitigation and the S-3 Effect menu includes positive Effects, whether "mitigating" a positive Effect (e.g., an opponent's successful advantageous Effect) is coherent — and whether it is desired — is unresolved. **Cannot be scoped until the S-3 Effect menu's gated-tier contents are enumerated (the menu *structure* is locked via DEC-023, and the S-3 design-investigation thread on effect identity/auto-apply/second-effect/partial-match is closed, but the specific Effects within each gated tier — Position, Condition, Equipment, Defense, Location — are not yet fully enumerated).** Not blocking.
- Upstream: DEC-050 (universal eligibility), DEC-048 (Model B), DEC-049 (separate mitigation per Effect), DEC-027 (auto-apply), DEC-023 (menu structure locked).

## 3.8 OPEN-010 — S-6 repeated-Defense fatigue/exhaustion

**Open — deferred.** Follow-up from DEC-047 (uncapped Defense rolls): whether repeated Defense rolls within a scene/encounter should trigger additional negative effects from fatigue/exhaustion. **Explicitly unscoped — no fatigue/exhaustion system currently exists anywhere in the game**, so it cannot be scoped until/unless such a system is designed. Non-blocking.

## 3.9 Confirmed-closed items (so you do not re-open them silently)

These resolve questions you might otherwise treat as open. **Do not silently re-open; if reopening is warranted, flag it for Tiwa via the human-escalation workflow:**
- OPEN-001 → DEC-038 (H0 Rider B causal attribution)
- OPEN-002 → DEC-040 (Location Tier default 0; per-roll promotion)
- OPEN-003 → DEC-041 (anatomical mapping; Skill-Tier ≥ 2 gate)
- OPEN-004 → DEC-042 (Tier-2 secondary roll, no cost)
- OPEN-006 → DEC-035 (Wound severity mis-frame corrected)
- OPEN-007 → Ruled (Wound consequences)
- OPEN-008 → DEC-037 (non-attack Location Index generation)

---

# 4. LLM Governance Rules (D2 §24) — binding on any LLM working here

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
4. Never promote a proposal because it appears repeatedly in documentation.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. Never silently resolve an open designer fork.
7. Identify contradictions between current and historical documents.
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
14. When a subsystem is locked, update the Canonical document and its changelog.
15. When a proposal is superseded, retain its historical significance but mark it Superseded.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

## Human escalation workflow (from AGENTS.md)

```
INSPECT → ANALYSE → IDENTIFY AMBIGUITY → EXPLAIN EVIDENCE
→ IDENTIFY CONSEQUENCE → PRESENT HUMAN QUESTION → STOP
→ HUMAN RULING → IMPLEMENT IF AUTHORISED
```

When an authority question is unresolved, present: (1) Evidence, (2) Established governance, (3) Ambiguity, (4) Consequence, (5) Human question — then **stop**. Do not silently select one interpretation.

---

# 5. Evidence Classes (D2 §23.2 / D3) — use these labels precisely

- **Mechanical fact** — directly follows from existing locked rules.
- **Empirical finding** — supported by simulation, playtesting, or other explicit evidence (e.g., E9 usability playtest, Named-Outcome 21/21 trial).
- **Designer ruling** — a deliberate choice not mathematically forced by the system.
- **Recommendation** — a proposed preference not yet accepted.
- **Architectural constraint** — governs how systems interact, not what a mechanic numerically does.

An empirical finding does not itself establish a designer ruling. An architectural constraint does not establish a numerical mechanic. **Preserve this labeling discipline in any document you produce.**

---

# 6. The Formal Reporting / Provenance Standard (verbatim) — REQUIRED for any document you produce this session

The repository's provenance rules are in `governance/provenance.md`. Any document an LLM creates (a draft ruling report, handoff record, investigation, etc.) **must** conform to this. Follow it on the **first attempt** — do not reconstruct or guess it.

## 6.1 Mandatory metadata block (from `governance/provenance.md`)

> Every document created by an LLM in this repository must open with a metadata block identifying `author_llm`, `assessor_llm`, and `last_modified_by_llm` (each with `name` and `version`), plus `created_date` and `last_modified_date`. Use `unknown` or `not established` rather than inventing a value. `assessor_llm` may be a **list** when more than one assessment pass has been performed (e.g., an original authoring-session assessment followed by an independent second-model assessment appended later); each entry represents one assessment, earliest first.

The exact YAML front-matter shape (from `governance/provenance.md` and the real example reported in §6.4):

```yaml
---
document:
  title: "<title>"
  version: "<version>"
  status: "<status>"
provenance:
  author_llm: {name: "<model>", version: "<version>"}
  assessor_llm:
    - {name: "<model>", version: "<version>"}
  last_modified_by_llm: {name: "<model>", version: "<version>"}
  created_date: "<YYYY-MM-DD>"
  last_modified_date: "<YYYY-MM-DD>"
---
```

## 6.2 Role distinction (from `governance/provenance.md`)

- **author_llm** — the original creator. **Never overwritten by later editors**, even if they substantially rewrite the document.
- **assessor_llm** — reviews for factual/documentary consistency, canonical-status accuracy, provenance, or structure. An assessment is **not** a human decision and does **not** confer authority. Where an additional independent assessment is later performed, the independent assessor is **appended** as another entry — the original assessor record is preserved, not overwritten.
- **last_modified_by_llm** — the most recent substantive editor. Updated on material changes; formatting-only changes may be handled per future project policy (not yet defined).

**Critical: do not overwrite original authorship.** If you produce a document and OpenCode later records/edits it, OpenCode becomes `last_modified_by_llm`, but `author_llm` stays as the original creator (per §6.4-adjacent discipline). Do not fabricate provenance — record unknown provenance as `not established`.

## 6.3 ID / versioning discipline for you as the session author

In the consolidated repo, your model identification must be the full `name` + `version`. For you, that is `{name: "Claude Sonnet 5", version: "claude-sonnet-5"}` (matching how prior Claude-authored reports are recorded). If you are unsure of the exact model string, record it honestly and flag the version for OpenCode to confirm rather than inventing one.

## 6.4 Real example report — flag the standard in context

The repository's own documentarian handoff reports are the closest model for what you will produce. **Do not copy their content** — those are hash-indexed evidence/pointer-referenced items. You need the **form**, which is:

- Title line: `# Tiwas — <Subsystem> ... — Documentarian Handoff Report`
- A **Document Version** and **Document Status** line.
- A **Rule Authority** line explicitly declaring whether the document creates game mechanics (typically: "None — this document creates no game mechanics. It records what was discussed, what the designer ruled, and what remains open.")
- A **Prepared By** line naming the model and role.
- **Session Participants** list (role + ruling authority designation).
- Sections: Session Chronology; Terminology Lock (if any); Ruled/Confirmed positions (each with Status + Notes for OpenCode); any audit findings; Remaining Open Items; Recommended Action Items; Governance Notes.

Example to reference for form (pointer, not inline): `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md` — see its §1 (Session Chronology), §3 (Ruled positions with Status/Notes-for-OpenCode columns), §6 (Remaining Open Items), §7 (Recommended Action Items), §8 (Governance Notes with the non-canonical reminder).

## 6.5 Decision-register column structure (verbatim)

The live register's row schema is: **`ID | Subject | Decision/State | Evidence (source) | Authority | Status`**.

- **ID** — `DEC-###` for decisions, `OPEN-###` for open items.
- **Subject** — short name.
- **Decision/State** — the actual ruling/statement.
- **Evidence (source)** — pointer(s) to the source document(s) and the in-session/designer provenance.
- **Authority** — e.g., `Canonical / Locked`, `Non-canonical designer ruling`.
- **Status** — e.g., `Ruled`, `Current`, `Open`, `Closed via DEC-###`, `Inert / dormant`.

You do **not** assign DEC numbers yourself unless explicitly instructed — numbering is left to OpenCode against the live register's actual next-available sequence (per the governing practice stated in the prior session's handoff). OpenCode currently records next-available IDs from the live register.

---

# 7. What Is EXCLUDED from this snapshot (by design, per Tiwa)

- **`sources/incoming/tiwas-tttrpg-merge/` draft trail** and all other raw/incoming LLM-merge artifacts.
- **Closed/superseded investigation threads** for already-Ruled subsystems — only their closure record/characterization is included (their DEC entries), not the process drafts.
- **Raw multi-model survey transcripts** (e.g., the 8-model blind survey raw outputs) whose conclusions are already captured in the register (e.g., DEC-031). Those are pointer-referenced, not reproduced.
- **Hash-indexed evidence items** — e.g., the dec025–028 handoff reports — are **pointer-referenced by path + one-line status**, NOT copied inline, per the standing evidence-preservation rule.

## Pointer references to audit-trail/evidence items (do not reproduce inline)

| Item | Status | Location |
|---|---|---|
| S-3 designer rulings & handoff (DEC-023…DEC-030) | Ruled (non-canonical) | `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` |
| S-4 documentarian handoff report | Record source for DEC-032…DEC-037 | `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md` |
| S-4 DEC-035 original wording & correction | Verbatim designer quote | `investigations/tiwas-s4-dec035-original-wording-and-correction-2026-08-30.md` |
| DEC-037 stress-test rerun | 14-scenario literal re-run | `investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md` |
| S-5 armor advisory session handoff (DEC-058…DEC-062 source) | Ruled (non-canonical) | `investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` |
| S-6 defense opening brief (DEC-044…DEC-050 source) | Ruled (non-canonical) | `investigations/tiwas-s6-defense-opening-brief-2026-08-31.md` |
| S-7/S-8 advisory session handoff (DEC-051…DEC-057 source) | DRAFT (pending reconfirmation) | `investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md` |
| S-8/S-9-S-10/S-11 advisory session handoff (DEC-063…DEC-074 source) | DRAFT (pending reconfirmation) | `investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` |
| S-8 third-party adjudication candidate (DEC-043 source) | Ruled | `investigations/tiwas-s8-third-party-adjudication-mutual-failure-candidate-v1.md` |
| S-3 Effect identity & multi-effect opposition investigation | Closed (all items ruled: DEC-025, DEC-026, DEC-027, DEC-030 — effect naming, second-effect mechanism, auto-apply, partial-match fallback). Menu *structure* locked (DEC-023). Gated-tier *contents* not fully enumerated. | `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` |
| DEC-038/039/040/041/042 designer rulings session (2026-08-31) | Ruled (non-canonical) | `tiwas-designer-rulings-session-2026-08-31-v2.md` (path as reported in register; verify against live repo) |
| S-4 third-party adjudication mutual-failure candidate | Ruled (via DEC-043) | `investigations/tiwas-s8-third-party-adjudication-mutual-failure-candidate-v1.md` |

---

# 8. Session Instructions

You are **Claude Sonnet 5 (`claude-sonnet-5`)**, in the **Lead Systems Architect / Design Assistant** (advisory, conflict-checker, cross-model auditor) role. Tiwa is the **human designer and sole ruling authority.** OpenCode is the **documentarian** with live repo access.

- Give **advisory opinions** on the open design decisions Tiwa raises. You do **not** rule, promote, lock, or record — Tiwa decides, and OpenCode records against the live register.
- Never silently resolve an open fork (Rule 6). Present options, evidence, consequences, and a recommendation; flag what only Tiwa can decide.
- Preserve the Locked/Ruled/Open distinctions exactly. Do not let a non-canonical ruling read as Canonical, and do not treat a proposal as a rule.
- Any formal document you produce must follow the reporting/provenance standard in §6 (correct YAML block, evidence-class labels, register-column alignment), on first attempt.
- Flag — do not silently resolve — any ambiguity, contradiction, or contamination risk you detect.

*End of snapshot. Dated 2026-09-01, v4.0. Task-scoped; not authoritative beyond this session.*
