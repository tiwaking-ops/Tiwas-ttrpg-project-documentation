---
document:
  title: "Tiwas — G3 Duration / Time-Unit Scale: Designer Ruling Record"
  version: "1.0"
  status: "Advisory session record — Non-canonical. Recorded in the live decision register as DEC-145 (2026-09-18, approved by Tiwa and recorded by OpenCode)."
provenance:
  author_llm: []
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
---

# Tiwas — G3 Duration / Time-Unit Scale: Designer Ruling Record

## 0. Purpose and Authority Boundary

This document is an **advisory session record**, not a ruling and not a canonical or
non-canonical rules document in its own right. It records a decision made by Tiwa (human
designer / ruling authority) during an in-session advisory conversation with OpenCode
(big-pickle), for the purpose of formal recording by OpenCode into the live decision
register (`_consolidation/decision-register.md`).

**No DEC number is assigned by this document.** Per standing project governance, only
OpenCode assigns DEC numbers and records rulings into the register after Tiwa's approval.
This record supplies the ruling content, rationale, and cross-references needed for that
recording step (proposed placement: **DEC-145**).

**Ruling basis:** `investigations/tiwas-g3-duration-time-unit-scale-options-report-2026-09-17.md`
(Claude Sonnet 5; advisory, non-canonical, no DEC) — options catalog §4 (Options A–O),
categorization §5, cross-category comparison §6, recommended per-domain mapping §7, and
open questions §8.

## 1. Item Addressed

**G3 — Duration/time-unit scale**, carried as an explicitly open G-series item since it
was flagged in the G2 movement-denial advisory session (2026-09-07) and reaffirmed as open
in every subsequent closure pass:

| Prior reference | Status before this ruling |
|---|---|
| DEC-133 (G5 — Movement resolution granularity) | G3 explicitly named as **not** resolved by DEC-133; explicitly declines to define real-world duration per turn |
| DEC-133.A (G5 confirmation amendment) | Confirms G3 remains open as a separate G-series item |
| DEC-138 (G1 closure) | Closes G1; G3 confirmed as **the sole remaining open G-series item** from the cluster (per DEC-133.A's carried open list) |
| DEC-082 / DEC-082.A (Time/Action) | Time expressed only via Skill-side / Movement-penalty overlays; no action-point pool; no duration answer |
| DEC-067/068/070/073, DEC-089–093, DEC-117 R2 | Extended-Test interval, hazard ticks, and StateRecord `duration` field all exist but carry **no mechanical duration meaning** |

## 2. Options Presented

Fifteen candidate mechanisms (A–O) in five functional families were cataloged in the
options report (§4/§5). The decisive architectural fork (report §8 Q1) was whether to rule
a **single universal architecture** or a **per-domain assignment**. The per-domain shape
was recommended (§7) on the DEC-013 §13.3 Quality-mode precedent — G3 ruled not as "one
Option for all time," but as "different domains declare which Option(s) govern them."

The full catalog, per-option invariant checks, and extended positives/negatives are in the
source report §4; they are not duplicated here. This record records the adopted set.

## 3. Ruling

**RULED by Tiwa, 2026-09-18 (in-session, this advisory conversation): per-domain
assignment adopted.** No single universal duration architecture is ruled.

### 3.1 Adopted per-domain assignment

| Domain | Option | Mechanism (as adopted) |
|---|---|---|
| Combat exchange | **A** — fixed category lookup | Each action category (here: combat exchange) has one fixed duration drawn from a content-authored table; uniform turn length under DEC-095; table speed paramount. |
| Gather Information / low-stakes social | **A** — fixed category lookup | Explicitly avoids per-roll time overhead for high-frequency, low-stakes checks. |
| Crafting | **L + G** | Per-task **authored base durations** (Option L — a content-authored `duration` per recipe, in the DEC-142 `min_skill_tier` field pattern) **refined by a Wurm-style derived-duration formula** (Option G — effective-skill / tool-quality / exertion inputs). G is **folded into the existing crafting ruling chain** (DEC-141/142); no new DEC family is created now. G's numeric constants, tuning coefficients, BaseDurations and input sourcing are **content-authoring (DEC-077.A)** — explicitly not ruled here. |
| Travel, known/mapped route | **K** — movement-speed-derived | `Time-per-Band = Band-hex-count ÷ effective Movement Speed`, reusing DEC-133's canonical `1 Movement Speed = 1 hex per combat turn`; terrain/obstacles via the DEC-063 Skill-side penalty architecture applied to effective MS. Band↔hex counts remain content-authoring per DEC-133/DEC-133.A. |
| Travel, unknown/hostile | **D** — roll/cost-coupled | `Duration = NaturalRoll × k`; reuses the exact d100 already spent as Cost (DEC-006 step 4 / DEC-007), preserving "you don't know how long until you commit" uncertainty. `k` is a content-authored tuning constant per category. |
| Healing / Extended Tests | **J** — time-as-interval-count | The Extended-Test interval (DEC-067/DEC-073) is the atomic time unit; answers are given in interval counts; any real-world translation is optional flavor that never becomes load-bearing. |
| Dungeon/survival downtime | **I** — resource-attrition | Time is defined operationally as "however long it takes to consume one unit of a tracked consumable" (light, rations, ammunition); no independent clock. Reuses existing tracked consumables — no new resource pool (Invariant 17 clean). |
| Everywhere, as overlay | **M** — time–Energy tradeoff | A player (or creature/NPC) may deliberately overspend Energy/MP beyond normal Core Test Cost, accepting the associated Overflow risk (DEC-007), to compress whatever Duration the governing base option produced. Declared **universal, including creatures/NPCs** — mirroring DEC-140's universal-symmetry discipline. The Energy/MP→Duration conversion rate is a single content-authored tunable, not a subsystem. |

### 3.2 Adopted infrastructure (optionally first, applies to all domains)

| Piece | Ruling |
|---|---|
| **O** — reuse/extend the StateRecord `duration` field | DEC-117 R2's `duration` field (present on every Effect/Condition/Tag StateRecord) is widened with a small number of coarse content-values (e.g. `interval`, `downtime-block`) so the field carries G3's vocabulary. The widened enum is kept **unified** with DEC-117's existing narrative-pacing values, and the two meanings (narrative persistence vs mechanical action duration) coexist in one field **by documented intent**. This is plumbing; numeric/comparative meaning is supplied by the domain options above + Option F for automation. |
| **F** — automation-only conversion convention | A scoped, non-canonical conversion table (band/category/month→units → real durations) authored for **unattended automated runs only** (the Claude/GPT/Grok runner packets). Exact structural precedent: the Automated Playtest Run Conventions (H1–H8) for S-11 healing (DEC-072.A). Authoring is approved to proceed **now**. F binds no human GM and touches no table-level GM discretion (DEC-130 bounded universality preserved). |

### 3.3 Rejected / not adopted in this set

- **N** (independent duration roll) — **rejected as not a live candidate**: a second,
  independent resolution transaction sits closest to an Invariant 18 violation, and the
  corpus consistently rejects second roll types (Extended Tests deliberately reuse the
  ordinary Core Test, DEC-067/073).
- **B** (Margin-scaled), **C** (Skill-Tier-scaled) — not adopted in this per-domain set; C
  was superseded for crafting by the chosen L+G combination. These remain paper options
  only; nothing in this ruling prevents a future amendment adopting them for a domain.
- **E** (abstract time bands) — not adopted; the adopted set supplies the needed time
  vocabulary through Option O's extended `duration` field and Option J's interval unit.
- **H** (formally leave reserved) — superseded by this affirmative ruling.

### 3.4 Explicitly NOT ruled (content-authoring / implementation)

Per the options report §1.2 scope and LLM Governance Rule 5 (never infer a numerical
threshold from an example unless explicitly locked), **no numeric constants are ruled
here**: base durations, `k` tuning coefficients, G's formula parameters and input sourcing,
per-recipe authored durations, band/category↔real-time conversion numbers, and M's
conversion rate are all **content-authoring (DEC-077.A)** or implementation detail, to be
authored and validated after this architecture ruling — not inferred by any LLM.

## 4. Consequences

| Effect | Detail |
|---|---|
| G3 closed | The last open G-series item from the DEC-133/DEC-133.A cluster is closed. DEC-082's time/action scope gains a duration layer for the named domains while its no-action-point-pool architecture is fully preserved. |
| No universal formula | A single Wurm-style or Skill-Tier formula is explicitly **not** adopted across all domains; each domain carries the mechanism that fits its axis (table speed, competence, uncertainty, simplicity). |
| Crafting chain continuation | G is folded into the DEC-141/142 crafting ruling chain; the still-open P5 tool/fixture-Tag precondition and other crafting carry-overs are unaffected. |
| Automation unblocked | Option F's conversion convention (approved now) gives unattended runners a scoped, revisable number in every adopted domain without touching table play. |
| DEC-007.A preserved | Despite M's extra-Overflow incentive, DEC-007.A's Overflow immutability clause is untouched — M only changes the player's decision to accept more Overflow, never the mechanic's magnitude/calculation. |
| Invariant 17 / 18 preserved | No adopted option creates a resource pool (I reuses tracked consumables; M reuses Overflow) or a parallel resolution engine (all derive from existing values; N, the only candidate that would, is rejected). |
| StateRecord schema | DEC-117 R2's `duration` enum is widened, not replaced; no new field, record type, or system is introduced. |

## 5. Cross-References

**Preserves (unchanged by this ruling):**

- DEC-004 — Movement Speed formula, untouched; K consumes effective MS, never redefines it.
- DEC-006 / DEC-007 / DEC-007.A — Core Test Transaction; Cost = natural roll; Overflow immutability absolute.
- DEC-009 — Failure XP, unchanged.
- DEC-013 §13.3 — Quality-mode per-contest selection precedent, the architectural model for per-domain assignment.
- DEC-063 — Skill-side penalty architecture, referenced by K for terrain difficulty.
- DEC-067 / DEC-068 / DEC-070 / DEC-073 — Extended Test machinery (Margin accumulation, neutral failure, GM-set completion target); J adds a label, not a system.
- DEC-077.A — Content-authoring bar; the sole home for every numeric constant this ruling declines to set.
- DEC-082 / DEC-082.A — Time/Action economy; no action-point pool; skill-side/movement-penalty model intact.
- DEC-089–DEC-093 — Hazard machinery; duration of exposure per tick now references the domain-appropriate adopted option.
- DEC-095 — Combat turn structure; Option A rides it without redefining it.
- DEC-115 / DEC-116 / DEC-117 — Unified StateRecord schema; Option O widens the R2 `duration` enum only.
- DEC-128 Q1/Q2/Q3 / DEC-129 — Item Tier/Magnitude and creation/repair machinery; L's authored durations ride on existing per-recipe authored fields.
- DEC-130 — Bounded-universality GM Fiat; Option F is automation-scoped only and binds no human GM.
- DEC-133 / DEC-133.A — Canonical spatial model; K reuses the canonical `1 MS = 1 hex per combat turn`; band↔hex boundaries remain content-authoring.
- DEC-138 — G1 closure; G3 now closed as the cluster's final open G-series item.
- DEC-140 — Universal PC/creature symmetry precedent, applied to M.
- DEC-141 / DEC-142 — Crafting Tier-combination formula and Skill-Tier gate; unchanged; G folds into this chain.

**Not touched:**

- The broader Time/Action subsystem (Proposals §12, Reserved) — remains open beyond the
  items closed by DEC-082.A and this ruling.
- The seven consuming mechanics (DEC-133.A R3; Disengage, Zone of Control, Chase, generic
  movement contests, Forced Movement magnitude, Pin/Hold Position, Seize/Deny Ground) —
  remain open as a separate umbrella item (see the 2026-09-18 seven-consuming-mechanics
  status/advisory).
- All Locked Canonical material — no canonical change; this is a non-canonical designer
  ruling pending any future 8-step Promotion Rule run (REQ-021).

## 6. Required OpenCode Actions

1. Assign **DEC-145** and record the ruling text (Section 3) verbatim into the decision
   register (`_consolidation/decision-register.md`), Section B, after DEC-144.
2. Annotate **DEC-133.A** — G3 is closed via DEC-145 (replacing the "G3 remains open"
   carry in the G1-closure note).
3. Annotate **DEC-138** — update its "Not touched: G3 ... remains open" clause to point to
   DEC-145.
4. Update the options report's register annotation on DEC-133.A to note it is now the
   ruling basis for DEC-145 (no authority change — the report remains advisory).
5. No Canonical Rules (D1/§A) change is required.

## 7. Reconfirmation Checklist for Tiwa

Recorded as decided on 2026-09-18 (answers given to OpenCode in-session):

- [x] Per-domain assignment adopted (no single universal architecture).
- [x] Per-domain mapping adopted as recommended (§7): combat + Gather = A; crafting = L+G;
      travel-known = K; travel-unknown = D; healing/ET = J; downtime = I.
- [x] Crafting = **L + G**, folded into the crafting ruling chain (no new DEC family; G's
      constants are DEC-077.A content).
- [x] Infrastructure: **O now** and **F now**.
- [x] M adopted as **universal overlay, including creatures/NPCs**.
- [x] N rejected as not a live candidate (Invariant 18).
- [x] Numeric constants and conversion numbers explicitly not ruled (DEC-077.A content).

---

*End of record. This document confers no authority beyond recording Tiwa's in-session
ruling for OpenCode's formal processing. It is not a Canonical or non-canonical rules
document until OpenCode records it into the live register.*