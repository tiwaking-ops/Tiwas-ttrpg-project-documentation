---
document:
  title: "Tiwas — G5 Seven Consuming Mechanics: Fusion-Draft Review, Items 1–5 (Advisory Recommendations Report)"
  version: "v0.1"
  status: "Advisory / Non-canonical. No DEC assigned. Not a ruling, not a register action. Rule Authority: None."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  related_records:
    - "investigations/tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md (NOT supplied in this chat — see §2)"
    - "investigations/verifier-report-tiwas-g5-fusion-synthesis-2026-09-19.md (NOT supplied in this chat — see §2)"
    - "investigations/tiwas-g5-seven-consuming-mechanics-verification-chat-report-2026-09-19.md (NOT supplied in this chat — see §2)"
    - "investigations/tiwas-g5-seven-consuming-mechanics-independent-assessment-2026-09-19.md (NOT supplied in this chat — see §2)"
    - "_consolidation/decision-register.md (supplied; verification basis)"
  storage_note: "Moved from repo root to investigations/ on 2026-09-19 by opencode / muse-spark-1.3-contributor-free per the analyze-assess-record-store workflow. Body unaltered; frontmatter updated to record intake assessment. Assessment: advisory/non-canonical, no DEC — consistent; second-hand limitation honestly stated (§2); spot-verified (DEC-023.A alpha list; DEC-079/124/131 Break-Free gap = U-9 confirmed; Open/Close Lane single register match = U-6 confirmed as unaddressed; DEC-143 present); one flagged labeling inconsistency (report cites Canonical Rules v1.4; the repository canonical rules file is v1.3); §11 cross-reference rows beyond the spot-checks recorded as the author's. Tiwa's accompanying rulings on Items 1–5 are not recorded by this intake; register recording proposed separately. Storage & assessment confer no authority."
---

# Tiwas — G5 Seven Consuming Mechanics: Fusion-Draft Review, Items 1–5

**Document Version:** v0.1
**Document Status:** Advisory / Non-canonical. No DEC assigned.
**Rule Authority:** None — this document does not create, amend, promote, or supersede any game mechanic or register entry.
**Author:** Claude Sonnet 5 — LLM name: `Claude Sonnet 5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-19
**Document class:** Project documentation report (advisory recommendations record) for OpenCode storage.
**Important:** Recommendations below are advisory. Candidate wording is candidate text for Tiwa to accept, edit, or reject; it is not rule text.

---

## 0. Governance Statement

This report:

- Assigns **no DEC number** and infers none.
- Records **recommendations**, not designer rulings. Every "Tiwa rules…" item below is a **pending question**, not a decision.
- Promotes, demotes, and supersedes **nothing**. No Canonical Rules (v1.4) content is touched.
- Leaves all seven DEC-133.A R3 consuming mechanics (Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position resolution, Seize/Deny Ground resolution) **open**, exactly as the register records them.
- Follows the project's status vocabulary (Canonical / Locked; Non-canonical designer ruling; Recommendation; Open) and evidence-class labelling (mechanical fact; empirical finding; designer ruling; recommendation; architectural constraint).
- Follows LLM Governance Rules 4, 6, 10, 15 and 16 (D2 §24): no silent resolution of an open designer fork; state clearly when an answer depends on a proposal rather than a Canonical rule.

**Provenance note (per `governance/provenance.md`):** this report was authored by a single model in a single pass. `assessor_llm` is recorded as `not established`. A single-model authorship carries no authority and is a weaker form of review than an independent second pass.

---

## 1. Purpose and Scope

The human user relayed five findings from the multi-model review of the 2026-09-19 Fusion synthesis of the seven G5 consuming mechanics and asked for advice and recommendations on each. This report records, for OpenCode storage:

1. The five items as presented.
2. The verification performed against the supplied decision register.
3. The recommendation given for each item, with reasoning.
4. The unresolved questions that remain for Tiwa.
5. The recommended order of work.

Out of scope: drafting or ruling any of the seven mechanics themselves; authoring register text; editing the Fusion draft.

---

## 2. Source Basis and Limitations

| Source | Supplied in this chat? | Use |
|---|---|---|
| `decision-register.md` (through DEC-146) | **Yes** | Primary verification basis for every DEC citation |
| Canonical Rules v1.4, Proposals/WIP v1.4.3, Roadmap v1.4.3, governance files (via static base), Alpha Playtest Corpus, Your First Adventure module, Claude Runner Packet, GDD Orchestration Plan | Yes | Governance, invariant, and convention reference |
| Fusion synthesis draft (§0.1, §2 Z-A, §6 P-A, §10 etc.) | **No** | Not viewed; content taken from the user's quotations and line references |
| Verifier / big-pickle / Nemotron review reports (findings C1–C4, RC-1–RC-4, SA-1–SA-6, etc.) | **No** | Not viewed; finding labels taken from the user's message |
| Draft questions Q2 (ZoC shape) and Q10 (ZoC↔Seize/Deny) | **No** | Referenced only as the user described them |

**Limitation (flagged, not fixed):** every statement about what the Fusion draft says is second-hand. Recommendations should be re-checked against the draft text before Tiwa rules. Every statement about what the register says was checked against the supplied register text.

---

## 3. Summary of Recommendations

| # | Item (finding label) | Recommendation | Who acts | Weight |
|---|---|---|---|---|
| 1 | Z-A per-hex movement multiplier (C1) | **(c) Leave open as a fork**; fix drafting now; put one binary question to Tiwa after Q2 and Q10 settle | Drafter, then Tiwa | High |
| 2 | Lock Movement-Distance ephemerality (SA-4) | **(a) Lock it**, narrowly scoped, as a DEC-133-family ruling | Tiwa | High (highest leverage) |
| 3 | DEC-023.A enumeration gap (Nemotron) | **(a) Clarification only**, reworded so R3 means "consuming mechanics operating on the Position-tier substrate" | Tiwa | Medium |
| 4 | P-A Grappled branch (RC-3) | **(a) Require the drafter to describe Grappled's real mechanism**; fall back to (b) only if Pin/Hold cannot be distinguished from Grappled | Drafter | High (genuine error) |
| 5 | P-0 citation direction (C2/RC-2) | **(c) Both** — cite DEC-079 and DEC-082.A R2 (labelled inference), with "must" softened | Drafter | Low |

---

## 4. Item 1 — Z-A Multiplier Status (C1)

### 4.1 Item as presented

Fusion §2 Z-A: entering, crossing, or exiting controlled hexes costs 2 Movement Distance per 1 hex traversed, framed as "position accounting, not a second Cost channel." Question: rule it Invariant-safe (a), reject it for Tier-Y-overlay consistency (b), or leave open (c). Interacts with Q2 (ZoC shape) and Q10 (ZoC↔Seize/Deny).

### 4.2 Terms

- **A** = per-turn Movement Distance allowance = effective Movement Speed (DEC-133(3)).
- **c** = allowance consumed per hex. Z-A sets c = 2 in controlled hexes, c = 1 elsewhere.

### 4.3 Verification against the register

| Test | Result | Basis |
|---|---|---|
| Violates DEC-138? | **No.** | DEC-138 adopts the uniform `Tier-Y Condition Value Z` overlay as the default for movement-penalty magnitude across **Conditions**; non-Conditions are outside its literal scope. |
| Does "ZoC is a declarative flag, not a Condition" resolve the tension? | **Weakly.** | DEC-117 R1 makes Tags, Effects and Conditions one mechanical record shape; the three names are fiction-level classification only. The distinction carries no mechanical weight. |
| Invariant 6 (Cost = natural roll, PE/MP) | Safe | No PE/MP charged, no roll. |
| Invariant 17 (no competing pool) | Safe **if stated correctly** | A is refreshed per turn, no carry-over, no income/expenditure dynamic (cf. DEC-069 reasoning; DEC-069 itself states it does not generalize). |
| DEC-082 (Skill-side / Movement-penalty only) | Consistent in kind | A rate change on movement is a Movement penalty. |
| DEC-091 / DEC-088.A(5) pattern | **Tension** | `env:terrain_*` Tags are descriptive-only; zone Tags impose no automatic damage/penalty. A ZoC flag that auto-doubles cost departs from that pattern. |
| DEC-125 (Prone guarantees ≥ 1 movement) | **Collision** | With A = 1 and c = 2, a mover can never enter a controlled hex. |
| Overlap with Reactions | Possible redundancy | DEC-132.B's movement-trigger category (`reaction:vigilant`) already penalises movement past an opponent. |
| ZoC itself | Open | DEC-133.A R3 carries ZoC open, so nothing is violated whichever option is chosen. |

### 4.4 Why option (b) is weakest

| Mechanism | Scope | Evaluated |
|---|---|---|
| Tier-Y overlay (DEC-138; DEC-143 precedent) | Whole turn's allowance | At query time |
| Z-A multiplier | Individual hexes | Per hex, position-dependent |

A start-of-turn overlay would not tax a mover who enters a controlled hex mid-move, so ZoC would lose its "cannot run past" function. A per-hex re-query would work, but that is the multiplier under another name. The real underlying question is whether ZoC is a **character state** or a **spatial property** — Q2's territory.

### 4.5 Recommendation

**(c) Leave Z-A open as a fork** (not a soft flag). Rank order: (c) > (a) > (b). Option (a) is acceptable only if Tiwa wants a ruling now.

**Drafting fixes (needed under (a) or (c)):**

| # | Fix | Reason |
|---|---|---|
| 1 | Delete "second Cost channel"; state Invariant 6 and Invariant 17 separately | The phrasing conflates the two (upstage precision note, as relayed) |
| 2 | Add a floor clause: a mover with unspent A ≥ 1 may always enter at least one hex | Preserves the DEC-125 guarantee. **Candidate clause for Tiwa, not a rule** |
| 3 | State order of operations: DEC-122/DEC-138 overlays fix effective MS first, then Z-A applies c | Avoids double-counting with Slowed/Encumbered |
| 4 | State that ZoC is a StateRecord (DEC-117) consumed by the movement rule | Removes the false flag-vs-Condition distinction |

**Candidate wording (not a rule):**

> Movement Distance is a per-turn allowance derived from effective Movement Speed (DEC-133). It is not a Cost (Invariant 6: Cost = natural roll, paid from PE/MP) and not a pool (Invariant 17: refreshed each turn, no carry-over). A controlled hex changes only how much allowance a hex consumes; no PE, MP or roll is involved.

### 4.6 Pending question for Tiwa (after Q2 and Q10)

> Should controlled space alter movement cost per hex (an accounting rule on a zone-scoped record), or apply a Tier-Y overlay (DEC-138 style) to the mover?

**Observation (not a prediction):** recent register precedent (DEC-136, DEC-138, DEC-141–DEC-143, DEC-145) shows a repeated preference for reusing existing machinery with the stated reason "Simplification." That favours the overlay unless per-hex granularity is shown to be necessary.

### 4.7 Interactions to check

| Item | Check |
|---|---|
| Q2 (ZoC shape) | Spatial property (supports the multiplier) vs character state (supports the overlay); duplication of the movement-trigger Reaction |
| Q10 (ZoC↔Seize/Deny) | If Seize/Deny Ground creates controlled hexes, define the multiplier once on that Effect's record, not as a second source |
| Disengage | "Exiting costs 2" is effectively a disengage tax; confirm Z-A and Disengage do not both charge for the same movement |

---

## 5. Item 2 — Lock Movement-Distance Ephemerality (SA-4)

### 5.1 Item as presented

Fusion §0.1 (ln 37) and §10 (ln 318) treat the allowance as "ephemeral per-turn" — the foundation of the draft's Invariant-17 case. Question: lock it (a), leave as intended-but-unlocked (b), or defer (c).

### 5.2 Verification against the register

| Point | Finding |
|---|---|
| Already locked (non-canonical rulings) | Size of A: DEC-133(3). No action cost: DEC-095 and DEC-133(5). |
| Not locked | That A is never stored, banked, carried over, or tracked per scene. No DEC states this. |
| Near-derivation | A is defined as a function of a live statistic; DEC-122 already treats such reads as query-time-live; no register text defines a stored balance. Close to derivable, but not a ruling. |
| Invariant 17 case | Rests entirely on this point. DEC-069 cannot be borrowed (its assessment expressly does not generalize). |
| DEC-145(4) consistency | Travel Time-per-Band = band-hex-count ÷ effective MS uses MS as a rate; consistent with ephemerality and needs no stored balance. |

### 5.3 Recommendation

**(a) Lock it, narrowly scoped**, as a small DEC-133-family ruling. Rationale: one ruling removes a whole class of silent assumptions across all seven mechanics.

Two scoping points keep the lock from over-reaching:

1. **Separate the allowance from position.** Chase, ZoC and Seize/Deny Ground may need persistent scene state (a lead, a controlled hex). That is position, not allowance. The ruling must say so, or Chase is wrongly blocked.
2. **Settle the mid-turn-change edge case in the same ruling.** If a Condition alters MS mid-turn, is remaining allowance `effective MS at query − hexes already spent this turn`, floored at 0? That is per-turn bookkeeping, not a stored pool, but it should be explicit. **Put to Tiwa as a sub-question, not an assumption.**

**Candidate wording (not a rule):**

> Movement Distance is a derived per-turn quantity (effective Movement Speed, DEC-133(3)), recomputed each turn from the live statistic. It is not stored, banked, carried between turns, or tracked per scene. Positions and distance bands are scene state; the allowance is not.

Preserves DEC-004, DEC-082, DEC-095, DEC-133 and Invariants 6, 17, 18. Does not bar a later Effect or Condition from changing effective MS through an overlay.

---

## 6. Item 3 — DEC-023.A Enumeration Gap

### 6.1 Item as presented

The draft assumes Disengage, ZoC, Chase and generic movement contests are Position-tier Effects under DEC-023.A. DEC-023.A's locked alpha Position tier names only Forced Movement, Knock Prone, Seize/Deny Ground, Pin/Hold Position, Open/Close Lane. DEC-133.A R3 says all seven "remain open as Position-tier Effects under DEC-023.A" without naming the missing four. Options: (a) confirm R3 placement suffices (clarification); (b) amend the alpha list to name all seven; (c) leave open.

### 6.2 Verification against the register

| Mechanic (DEC-133.A R3) | In DEC-023.A alpha list? | Is it an Effect at all? |
|---|---|---|
| Seize/Deny Ground | Yes | Yes |
| Pin/Hold Position | Yes | Yes |
| Forced Movement (magnitude) | Yes (as Forced Movement) | Effect exists; R3 open only on magnitude |
| Disengage | No | Unclear; may map to Base-tier Open Retreat / Compel Yield |
| Zone of Control | No | Probably not — a standing declarative flag is not a one-Effect-per-win payload (DEC-024, DEC-027) |
| Chase | No | Probably not — a multi-turn procedure |
| Generic movement contests | No | No — a contest is S-1 usage (DEC-013), not an Effect |

Further observations:

- DEC-023.A's Position tier also lists **Open/Close Lane**, which is not among the seven and has no resolution found in the register. Check whether it is a silent eighth item.
- Forcing all seven into "Position-tier Effects" carries a cost: DEC-024 gives a winner exactly one Effect per win.

### 6.3 Recommendation

**(a) Clarification only, reworded.** Record R3 as meaning "consuming mechanics operating on the Position-tier substrate," **not** "added to the DEC-023.A list." Each mechanic's Effect / non-Effect status is then decided by its own ruling. **Reject (b) for now:** amending a ruled DEC before knowing which mechanics are Effects would force a second amendment. Reopen (b) only if one of the four proves to be a true Effect.

---

## 7. Item 4 — P-A Grappled Branch (RC-3)

### 7.1 Item as presented

Fusion §6 P-A (ln 222–226): Pin/Hold routes to "Restrained or Grappled," which "already zeros or penalises Effective Movement Speed per the locked rules." Options: (a) require P-A to describe Grappled's real mechanism; (b) limit P-A to Restrained; (c) leave to the drafter with a flag.

### 7.2 Verification against the register

The draft's sentence fits **Restrained** (DEC-122 uniform self-referential-Y zero, provisional; DEC-123 guaranteed-fail declared tests). It does **not** fit **Grappled**, which has three distinct paths:

| Path | Governing ruling | Mechanism |
|---|---|---|
| Victim moves away from holder | DEC-124, resolved by DEC-131 | Contested Break Hold / Break Free check. Fail: Grapple persists, mover locked, **no relocation** ("relocate both" dropped). Success: stepwise Heal-Effect-System Tier reduction, gated on breaker's Skill-Tier ≥ record's current Tier; `Y = 0` removes the record |
| Holder moves and carries the victim | DEC-143 (2026-09-17) | Holder's effective MS reduced by Y = the Grapple record's current Tier (read live); victim moves along at no separate cost. Option A fallback authorised; per-drag contested check (Option C) rejected as framework rule |
| Any other Grappled movement | DEC-122 (provisional) | Residual uniform zero, preserved by DEC-124/DEC-131 |

Additional finding: DEC-079 says Restrained ends by "Break Free, ally intervention, or GM Fiat," but **no ruling defines the Break Free mechanism** for Restrained. Worth flagging.

### 7.3 Recommendation

**(a) Require the real mechanism.** P-A should carry the per-branch table above. Also require the drafter to state **how Pin/Hold Position differs from the existing Grappled Effect** — DEC-023.A lists both, and a Pin that routes into Grappled would create two Effect names for one state. If the drafter cannot show a difference, fall back to **(b)**: limit P-A to Restrained and leave Grappled as its own Effect. Either way, the current sentence must be removed. This is the one finding assessed as a genuine accuracy error rather than drafting hygiene.

---

## 8. Item 5 — P-0 Citation Direction (C2/RC-2)

### 8.1 Item as presented

Fusion §0.1 (ln 41) and §6(b) (ln 234): "DEC-082.A R2: Pin/Hold must reuse existing Condition stack (DEC-122/123/124/126/131)." Options: (a) cite DEC-079; (b) recast as "designer ruling (DEC-082.A R2) + inference to Pin/Hold"; (c) both. Flagged unanimously by all three reviewers (as relayed).

### 8.2 Verification against the register

| Draft cite | Register check |
|---|---|
| DEC-082.A R2 | Confirms movement-denial × Movement Speed is closed via DEC-122/123/131. Never names Pin/Hold. States co-occurring denial Conditions are not separately ruled. |
| DEC-124 | Partly superseded by DEC-131 (deferred sentence resolved). Not cited by R2 |
| DEC-126 | Terminology only ("Helpless" is non-mechanical); not a mechanism to reuse |
| Actual Condition vocabulary | DEC-079 alpha list (Restrained, Grappled, etc.) |
| "Must reuse" | Overstated. R2 rules that no *further* interaction mechanics are ruled; it does not mandate reuse for Pin/Hold |

### 8.3 Recommendation

**(c) Both**, with "must" softened:

1. Cite **DEC-079** as the Condition-vocabulary source.
2. Cite **DEC-082.A R2** as a ruled constraint, labelled "inference to Pin/Hold."
3. Drop DEC-126 (or cite it only for the "Helpless is non-mechanical" point).
4. Replace "must reuse" with: R2 rules no further movement-denial interaction mechanics; any new Pin/Hold denial rule would therefore be a new ruling.

This is the lowest-weight item — a drafting direction only.

---

## 9. Consolidated Unresolved Issues (for Tiwa)

None of the following is decided by this report.

| ID (report-local) | Question | Depends on | Status |
|---|---|---|---|
| U-1 | Z-A: per-hex accounting rule on a zone-scoped record vs Tier-Y overlay on the mover | Q2 (ZoC shape), Q10 (ZoC↔Seize/Deny) | Open fork |
| U-2 | Z-A floor clause preserving the DEC-125 guarantee (mover with A ≥ 1 may always enter one hex) | U-1 | Candidate clause only |
| U-3 | Lock Movement-Distance ephemerality (candidate wording in §5.3) | — | Awaiting Tiwa |
| U-4 | Mid-turn MS change: remaining allowance = effective MS at query − hexes spent, floored at 0? | U-3 | Sub-question |
| U-5 | Record DEC-133.A R3 as "consuming mechanics on the Position-tier substrate" (clarification, not list amendment) | — | Awaiting Tiwa |
| U-6 | Whether Open/Close Lane is a silent eighth consuming mechanic | U-5 | Unchecked |
| U-7 | Whether Disengage is a distinct Effect or maps to Open Retreat / Compel Yield | U-5 | Open |
| U-8 | How Pin/Hold Position differs from Grappled (drafter to show, or Pin/Hold limited to Restrained) | Item 4 | Drafter |
| U-9 | Definition of Restrained's "Break Free" mechanism (DEC-079 names it; no ruling defines it) | — | Unruled gap |
| U-10 | Relationship between ZoC and the `reaction:vigilant` movement-trigger Reaction (redundancy) | Q2 | Open |
| U-11 | Whether Z-A and Disengage double-charge the same movement | Z-A, Disengage | Open |

---

## 10. Recommended Order of Work

| Step | Action | Needs Tiwa? |
|---|---|---|
| 1 | Drafter fixes: Item 4 (Grappled branch table; Pin/Hold vs Grappled), Item 5 (citation direction), and the Item 1 drafting fixes (§4.5 table) | No |
| 2 | Tiwa rules Item 2 (with its mid-turn sub-question U-4) and Item 3 (clarification wording) together as small confirmations | Yes |
| 3 | Tiwa resolves Item 1 after Q2 and Q10 are answered | Yes |

---

## 11. Register Cross-Reference (verification record)

| DEC / Source | Content relied on | Status label |
|---|---|---|
| DEC-004 | Movement Speed = floor((bsp+bss)/15); untouched | Canonical-adjacent derived stat (Canonical §4) |
| DEC-023.A | Position-tier alpha list; one Effect per win | Non-canonical designer ruling |
| DEC-024 / DEC-027 | One Effect per win; auto-apply | Non-canonical designer ruling |
| DEC-069 | Invariant-17 assessment covers A2+B1 only; does not generalize | Architectural constraint (assessment) |
| DEC-079 | Alpha Condition vocabulary (Restrained, Grappled, Slowed, Encumbered…) | Non-canonical designer ruling |
| DEC-082 / DEC-082.A | Skill-side/Movement-penalty only; R2 confirms DEC-122/123/131 as the movement-denial answer | Non-canonical designer ruling |
| DEC-088.A(5) | Zone Tags impose no automatic damage or penalty | Non-canonical designer ruling |
| DEC-091 | `env:terrain_*` descriptive-only | Non-canonical designer ruling |
| DEC-095 | Movement is a free/bundled side-activity | Non-canonical designer ruling |
| DEC-117 R1 | Tags/Effects/Conditions are one record shape | Non-canonical designer ruling |
| DEC-122 / DEC-123 / DEC-125 / DEC-126 | Self-referential-Y zero (provisional); "never total"; Prone crawl floor-of-1; "Helpless" non-mechanical | Non-canonical designer rulings |
| DEC-124 / DEC-131 | Contested Break Hold; fail = no relocation; success = stepwise Tier reduction | Non-canonical designer rulings |
| DEC-132.B | `reaction:vigilant` movement-trigger Reaction; Reactions fire on any S-1 contest | Non-canonical designer ruling |
| DEC-133 / DEC-133.A | Movement Distance = effective MS per combat turn; seven consuming mechanics carried open | Non-canonical designer rulings |
| DEC-138 | Uniform `Tier-Y Condition Value Z` overlay is the default for Conditions' movement-penalty magnitude | Non-canonical designer ruling |
| DEC-143 | Non-escape Grappled movement: holder's effective MS − record Tier | Non-canonical designer ruling |
| DEC-145 | Per-domain duration; travel Time-per-Band = band-hex-count ÷ effective MS | Non-canonical designer ruling |
| Invariants 6, 17, 18 | Cost = natural roll; no competing pool; build on Core Test Transaction | Canonical / Locked (Canonical §16) |

No entry above was found to contradict Canonical Rules v1.4. No contradiction between the supplied register and the user's characterisation of it was found, except the points recorded as flags in §6.2 (Open/Close Lane) and §7.2 (Restrained "Break Free" undefined).

---

## 12. OpenCode Action Boundary

1. Store this document as an **advisory / non-canonical investigation artifact** (suggested path: `investigations/tiwas-g5-fusion-review-items-1-5-advisory-report-2026-09-19.md`).
2. Do **not** infer, assign, or request a DEC.
3. Do **not** promote, demote, supersede, or resolve anything on the basis of this report.
4. Do **not** edit the Fusion draft, the register, or any ruled text from this report. Item 1–5 fixes are drafter actions; Item 2 and Item 3 rulings and the Item 1 fork are Tiwa's.
5. Any register annotation, if Tiwa directs one, should follow the existing advisory-storage-record precedent (an annotation on the DEC-133.A entry) and confer no authority.
6. Before any use, re-check the second-hand statements about the Fusion draft against the draft text (§2 limitation).

---

**End of document.**

**Author:** Claude Sonnet 5 — LLM name: `Claude Sonnet 5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-19
**Classification:** Advisory recommendations report — Non-canonical, No DEC assigned
