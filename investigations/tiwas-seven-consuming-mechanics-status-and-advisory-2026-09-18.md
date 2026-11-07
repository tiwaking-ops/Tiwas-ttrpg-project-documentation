---
document:
  title: "Tiwas — Seven Consuming Mechanics (G5 Carry-Open): Status Confirmation and Advisory Resolution Brief"
  version: "1.0"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
---

## Purpose and Origin

Advisory material produced by Claude Sonnet 5 (`claude-sonnet-5`) in a chat session on 2026-09-18 and handed over for intake. Stored via the analyze-assess-record-store workflow (assessed and stored by OpenCode / big-pickle): advisory-only, non-canonical, no DEC inferred — storage and assessment confer no authority. Source file as received: `tiwas-seven-consuming-mechanics-status-and-advisory-2026-09-18.md` (repo root). Body preserved verbatim below; only this frontmatter block and this opener were normalised at storage time (original author preserved as `author_llm`). Assessment note: Part A's status confirmation (DEC-133 §(5) / DEC-133.A R3 seven items remain open; DEC-143's explicit scope exclusion) was cross-checked against the live register and is accurate; Part B's advisory design brief cites verified DEC precedents (DEC-013, 023.A, 024/024.A, 026, 037, 043, 063, 068, 070, 073, 082, 091, 095, 103, 107, 115/117, 122/079, 124/131, 130, 132/132.B, 133, 143) and makes no authority claims — its four flagged designer forks (§3.5) remain genuinely open pending Tiwa's ruling.

# Tiwas — Seven Consuming Mechanics: Status Confirmation and Advisory Resolution Brief

## 0. Governance Statement

This document:

- Assigns **no DEC number** and proposes none.
- Records an **advisory design brief** only — a set of options and recommendations for a future designer ruling, not a ruling itself.
- Confers **no authority** on any option, formula, or sequencing proposal it contains. Per Governance Rule 6 (`tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` §24), no open designer fork is silently resolved by this document.
- Is scoped entirely to one open item: the "seven consuming mechanics" left open by DEC-133 §(5) (2026-09-08) and explicitly reconfirmed, not resolved, by DEC-133.A R3 (2026-09-10).
- Was produced in a single, un-reviewed pass by one LLM instance (see §6, Provenance Discipline). No independent second-model assessment has been performed.

---

## 1. Purpose and Scope

This report consolidates the complete output of a single chat session into a form suitable for OpenCode's project documentation and decision-tracking workflow. The session had two parts:

1. **Status inquiry** — confirming whether the seven items listed under DEC-133 §(5) / DEC-133.A R3 have been decided in any subsequent register entry (through DEC-143, 2026-09-17).
2. **Advisory request** — producing design recommendations for resolving that open item, for Tiwa's future review.

No file in the project repository was modified by this session. No DEC was inferred, assigned, or applied to the register.

---

## 2. Part A — Status Confirmation

### 2.1 Finding

**The item remains open.** As of the decision register's state through DEC-143 (last_modified_date 2026-09-17), no subsequent ruling addresses any of the seven named mechanics.

### 2.2 Item-by-Item Status

| Item | Status | Governing citation |
|---|---|---|
| Disengage | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |
| Zone of Control | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |
| Chase | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |
| Generic movement contests | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |
| Forced Movement magnitude | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |
| Pin/Hold Position resolution | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |
| Seize/Deny Ground resolution | Open | DEC-133 §(5); reconfirmed DEC-133.A R3 |

### 2.3 Confirmation Trail

- **DEC-133** (2026-09-08, adopting the Hybrid abstract-band spatial model) originally listed all seven under "Explicitly left open (consumed by the consuming mechanics, not preempted here)," citing DEC-023.A's placement of Forced Movement, Seize/Deny Ground, and Pin/Hold Position within the S-3 Position-tier Effect menu as the reason resolution is deferred to those future Effects rather than settled by the spatial-model ruling itself.
- **DEC-133.A** (2026-09-10) — the amendment that closed DEC-133's *other* carried-open items (band↔hex conversion boundaries; contested-movement-consumption generally) — explicitly reconfirms rather than resolves R3: "Seven consuming mechanics... all remain open as Position-tier Effects under DEC-023.A — not preempted by this amendment."
- No subsequent register entry through **DEC-143** (2026-09-17) names or resolves any of the seven. The nearest adjacent ruling, **DEC-143** (non-escape Grappled/drag movement), explicitly excludes this item from its own scope: "DEC-133/DEC-133.A (general contested-movement-consumption R2/R3 remain open; only this holder-drag cost is ruled)."

### 2.4 Practical Consequence

These seven remain unbuilt Position-tier Effect content. DEC-023.A locked "Force Movement / Seize / Deny Ground" and "Pin / Hold Position" as **named entries** in the S-3 alpha Effect menu (Position tier), but their resolution mechanics, magnitudes, and procedures are not yet ruled. They sit in the same category as any other not-yet-authored gated-tier Effect content — listed, not built.

---

## 3. Part B — Advisory Design Brief

### 3.1 Binding Constraints

Any resolution proposal for these seven items must satisfy the following locked/ruled invariants without exception:

| Constraint | Source | Implication |
|---|---|---|
| No action-point pool; Time/Action = Skill-side/Movement-penalty only | DEC-082 | Mechanics must be a Condition overlay or opposed-roll gate, never a spendable resource |
| One substantive combat action per turn (PC); movement is free/bundled | DEC-095 | Cannot consume a second action; must resolve inside the existing action or as a Reaction |
| Canonical spatial model = four abstract bands (Engagement/Short/Medium/Far); Movement Distance/turn = effective Movement Speed | DEC-133 | Chase, Disengage, ZoC must be defined in band-transition terms, not grid distance |
| No new resource/progression economy | Invariant 17 | No stamina pools, no per-round usage counters |
| Unified StateRecord schema (`Type` / `Tier-Y` / `Magnitude-Z` / optional `Location-X`) | DEC-115 / DEC-117 | Any lasting state (Pinned, Zone-locked) should be authored as a StateRecord, not a bespoke flag |
| One Effect per win; additional Effects require a separate opposed roll using a different Advanced Skill | DEC-024 / DEC-026 | Movement-control Effects compete for the single free Effect slot exactly as Disarm or Trip do |
| GM Fiat is bounded — cannot override Cost=roll, Overflow immutability, HP=0 incapacitation, or the no-DoT policy | DEC-130 | Any GM-discretion escape hatch must stay within this bound |

### 3.2 Recommended Umbrella Principle (Proposed, Unruled)

> **Proposed reference label: OQ-MOVE-1.** Any Position-tier Effect that manipulates a target's location, band, or ability to move is resolved as an S-1 opposed contest (DEC-013) between the acting Skill and a Movement-appropriate resisting Skill (default: the target's Reflexes/Quickness/Grace or an authored equivalent). Effect magnitude and duration follow DEC-103 (Skill-Tier shred + margin de-escalation) exactly as Wound/Condition Effects already do.

Adopting this single principle would collapse "what die mechanic do these seven use" into one already-fully-specified primitive, consistent with Governance Rule 11 (never create a parallel resolution engine). This is presented as a candidate for Tiwa's ruling, not as an adopted rule.

### 3.3 Per-Mechanic Recommendations

#### 3.3.1 Disengage

| Aspect | Proposal | Precedent reused |
|---|---|---|
| Trigger | Declared instead of an attack; consumes the single substantive action | DEC-095 |
| Resolution | S-1 contest: actor's Grace/Agility vs. each adjacent threat's Reflexes/relevant Skill | OQ-MOVE-1 |
| Win | Actor moves one band away without provoking a Reaction from that threat | DEC-133 |
| Loss | Actor still moves (movement is free/bundled); losing contest grants the threat a movement-trigger Reaction opportunity if it holds a qualifying Tag | DEC-132.B |
| Multiple threats | Resolve vs. the single highest-Skill threat, not N separate contests | DEC-043 adjudication-skill-default precedent |

**Open sub-question flagged for Tiwa:** whether Disengage costs the actor's only action, or is free when no threat is adjacent.

#### 3.3.2 Zone of Control

**Recommendation: no standalone mechanic.** Fold entirely into Disengage (§3.3.1) plus the existing Reaction framework (DEC-132), rather than inventing a new zone-tracking primitive or an "opportunity attack" trigger type outside DEC-132.B's taxonomy. This avoids Invariant-18 risk (a second engagement-resolution engine).

#### 3.3.3 Chase

| Aspect | Proposal | Precedent reused |
|---|---|---|
| Structure | Extended Test (one round = one interval) | DEC-073 |
| Progress | Accumulate band-gap delta each round from relative effective Movement Speed | DEC-004 / DEC-133 |
| Failure behavior | Neutral — costs resources normally, does not reset chase progress | DEC-068 |
| Completion | GM discretion (gap 0 = catch; gap exceeds Far = escape) | DEC-070 |
| Terrain | Ordinary difficulty grade on the Movement-based test | DEC-063 / DEC-091 |

This drops onto the existing S-9/S-10/S-11 Extended Test chassis with no new invariant risk.

#### 3.3.4 Generic Movement Contests

**Recommendation:** retire as a distinct line item once OQ-MOVE-1 is ruled. This item has no content beyond being the general form that Disengage, Chase, and Seize/Deny Ground already instantiate.

#### 3.3.5 Forced Movement Magnitude

| Aspect | Proposal | Precedent reused |
|---|---|---|
| Magnitude source | `Bands moved = min(Effect Tier, distance to nearest band boundary/obstacle)`, where Effect Tier = acting Skill-Tier | DEC-107 (Tier = Magnitude idiom, already locked for Wounds/Conditions) |
| Collision | Remaining unresolved "bands" convert to an Impose-Condition or Inflict-Injury Effect via the existing non-attack hazard pipeline | DEC-037 |

This is the lowest-risk item — a direct reapplication of the already-ruled DEC-107 Tier=Magnitude idiom onto a spatial rather than HP/Condition axis.

#### 3.3.6 Pin / Hold Position

| Aspect | Proposal | Precedent reused |
|---|---|---|
| Mechanism | StateRecord `Tier-Y Pinned Value Z` (`Z = −Y`), zeroing effective Movement Speed via the self-referential-Y pattern | DEC-122 / DEC-079 |
| Escape | Contested Break-Free check per the "Pure Break" model (fail = no relocation, persists; success = stepwise Tier reduction) | DEC-124 / DEC-131 |
| Distinction from Grappled | Denies the target's own movement without requiring an ongoing grip Effect on a specific limb | — |

Recommended framing for Tiwa: "Pinned reuses the Grappled mechanism verbatim, substituting the pin source for a grappling limb."

#### 3.3.7 Seize / Deny Ground

| Aspect | Proposal | Precedent reused |
|---|---|---|
| Mechanism | S-1 opposed contest for control of a specific band/position | DEC-013 / OQ-MOVE-1 |
| Duration | StateRecord with `duration: scene`, removable by a subsequent contested win | DEC-117 R2 / DEC-060 addition-model precedent |
| Ties | Resolved per S-1's exact-tie repeat rule | DEC-013 §13.5 |

### 3.4 Recommended Ruling Sequence

| Order | Item | Rationale |
|---:|---|---|
| 1 | OQ-MOVE-1 (umbrella contest rule) | All six remaining items are instances of it |
| 2 | Forced Movement magnitude | Direct copy of the locked DEC-107 idiom; minimal new design surface |
| 3 | Pin/Hold Position | Direct reskin of DEC-122/DEC-131 Grappled machinery |
| 4 | Disengage | Depends only on OQ-MOVE-1 |
| 5 | Zone of Control | Recommend closing as "no standalone mechanic" |
| 6 | Seize/Deny Ground | Depends on OQ-MOVE-1 + DEC-117 duration typing |
| 7 | Chase | Independent path via the Extended Test pattern |
| — | Generic movement contests | Recommend retiring as a distinct line item once OQ-MOVE-1 is ruled |

### 3.5 Items Requiring Tiwa's Explicit Ruling

Per Governance Rule 6, none of §3 is adopted by this document. The following are the genuine designer forks requiring a decision, not settled by precedent:

1. Whether OQ-MOVE-1 itself is correct — i.e., whether Position-tier movement Effects use S-1 opposed contests at all, versus an unopposed Skill-vs-difficulty-grade model (DEC-063 style).
2. Forced Movement's exact band-count formula (flat 1/win vs. Tier-scaled vs. Margin-scaled).
3. Whether Zone of Control receives any standalone content or is fully absorbed into Disengage + Reactions (recommended: fully absorbed).
4. Chase's completion-target default — GM-discretion-only (DEC-070 default) versus a stated default band-gap threshold (mirroring the DEC-073/H2 fixed-40-Margin precedent for automated play).

---

## 4. Summary of Deliverables from This Session

| Deliverable | Type | Disposition |
|---|---|---|
| Status confirmation table (§2.2) | Research finding | For OpenCode's tracking use; no register change |
| Confirmation trail (§2.3) | Citation audit | Verifies DEC-133 / DEC-133.A / DEC-143 do not resolve the item |
| Binding constraints table (§3.1) | Design-constraint restatement | Restates existing invariants; no new constraint created |
| OQ-MOVE-1 umbrella principle (§3.2) | Advisory proposal | Unruled — requires Tiwa's decision |
| Seven per-mechanic proposals (§3.3) | Advisory proposals | Unruled — require Tiwa's decision |
| Recommended ruling sequence (§3.4) | Advisory sequencing | Unruled — a suggestion only |
| Four flagged open forks (§3.5) | Escalation list | For Tiwa's explicit review |

---

## 5. Hard Boundaries Observed

- No DEC number was inferred, assigned, or applied.
- No canonical or non-canonical document was edited.
- No prior ruling (DEC-133, DEC-133.A, DEC-143, or any other) was reinterpreted, reworded, or silently resolved.
- All proposed mechanics were checked against Invariants 6, 7, 17, and 18 and against DEC-082, DEC-095, DEC-115/117, DEC-130; no conflict was identified in the proposals as framed.
- All recommendations are explicitly labeled advisory and require Tiwa's review before any promotion toward a ruling, consistent with the 8-step Promotion Rule (Proposals/WIP §21) for anything that might later be proposed for Canonical status.

---

## 6. Provenance Discipline

This document was authored, and its own content assessed, by a single LLM instance in one session (see frontmatter `provenance` block). No independent second-model review has been performed. Per the project's established provenance convention (`governance/authority.md`; prior single-model-authorship notices in the decision register, e.g. DEC-080's Automated Playtest Run Conventions precedent), this is recorded honestly as a single-pass, single-model output and confers no additional authority beyond that of any other advisory document in the `investigations/` tree.

---

**End of document.**
