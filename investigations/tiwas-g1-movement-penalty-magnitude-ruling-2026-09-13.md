---
document:
  title: "Tiwas — G1 Movement-Penalty Magnitude: Designer Ruling Record"
  version: "1.0"
  status: "Advisory session record — Non-canonical. No DEC number assigned by this document. Pending OpenCode formal recording into the live decision register."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — G1 Movement-Penalty Magnitude: Designer Ruling Record

## 0. Purpose and Authority Boundary

This document is an **advisory session record**, not a ruling and not a canonical or
non-canonical rules document in its own right. It records a decision made by Tiwa (human
designer / ruling authority) during an in-session advisory conversation with Claude Sonnet
5, for the purpose of formal recording by OpenCode into the live decision register
(`_consolidation/decision-register.md`) and, where applicable, the Proposals/WIP and
Implementation Roadmap documents.

**No DEC number is assigned by this document.** Per standing project governance, only
OpenCode assigns DEC numbers and records rulings into the register after Tiwa's approval.
This report supplies the ruling content, rationale, and cross-references needed for that
recording step.

## 1. Item Addressed

**G1 — Movement-penalty magnitude table**, carried as an explicitly open item since its
introduction in the G2 movement-denial advisory session (2026-09-07) and reaffirmed as
open in two subsequent closure passes:

| Prior reference | Status before this ruling |
|---|---|
| DEC-133 (G5 — Movement resolution granularity) | G1 explicitly named as **not** resolved by DEC-133 |
| DEC-082.A (Time/Action economy — closure of two DEC-082 carried-open items) | R1 confirms DEC-122/DEC-125 for the *ruled* scope but explicitly states "the G1 movement-penalty magnitude table remains explicitly open" |
| DEC-133.A (G5 confirmation amendment) | Confirms G1 remains open as a separate G-series item, not touched by that amendment |

## 2. Options Presented

Three candidate approaches were presented for closing G1:

| Option | Mechanism | Summary |
|---|---|---|
| **A** | Uniform Tier-based formula (no table) | Any movement-affecting Condition not already governed by DEC-122's self-referential-Y total-lock model applies the existing `Tier-Y Condition Value Z` (`Z = −Y`) overlay to effective Movement Speed — the same mechanism already used for Encumbered (DEC-078) and Slowed (DEC-079). No new data structure. |
| B | Explicit per-Condition table | A hand-authored lookup: Condition × Tier → fixed movement-penalty value, independent of the Condition's general Skill-penalty Tier. |
| C | Hybrid | Option A as default, with DEC-130 bounded-universality GM Fiat or DEC-077.A content-authoring permitted to override on a per-creature/per-scene basis. |

### 2.1 Comparative Assessment (as presented)

- Every movement/magnitude mechanic already ruled in the corpus (DEC-079 C2 `Z = −Y`;
  DEC-122 self-referential-Y; DEC-125 `max(1, floor(MS/2))`) is a **formula**, not a table.
- No table-based magnitude mechanic has been adopted anywhere in the corpus; DEC-116 R4
  explicitly declined a comparable table/matrix mechanism for Tag counters on the same
  general grounds (unnecessary bespoke structure where a uniform rule suffices).
- Option B would be the first instance of a standalone per-Condition magnitude table in the
  ruleset, external to the unified `Type / Tier Y / Magnitude Z / [Location X]` StateRecord
  schema (DEC-115/DEC-116/DEC-117).
- Option A requires no new authored content and no new record fields; it reads directly off
  the `Tier Y` value already present on any Condition record.

## 3. Ruling

**RULED by Tiwa, 2026-09-13 (in-session, this advisory conversation): Option A adopted.**

> Movement-affecting Conditions not already governed by a self-referential-Y total-lock
> (DEC-122) apply their standard `Tier-Y Condition Value Z` record (`Z = −Y`, per DEC-079
> C1/C2) as an overlay to effective Movement Speed, using the identical mechanism already
> governing Encumbered (DEC-078) and Slowed (DEC-079). No separate movement-penalty
> magnitude table is created. Content-authored exceptions to the formula's output (e.g.,
> DEC-125's Prone floor-of-1 clamp) remain available on a per-Condition basis under
> DEC-077.A where the plain formula would produce a degenerate result (e.g., zero
> movement).

**Reason (Tiwa, verbatim):** "Simplification and compatibility with existing system."

## 4. Consequences

| Effect | Detail |
|---|---|
| G1 closed | No table is authored; no further design work is required to close this item. |
| Mechanism confirmed | The `Tier-Y Condition Value Z` (`Z = −Y`) formula is now the **universal** default for movement-penalty magnitude across all Conditions not covered by DEC-122's total-lock treatment. |
| Escape hatch preserved | Content-authored exceptions (per DEC-077.A) remain permitted where the uniform formula would produce a degenerate result, consistent with the DEC-125 precedent (Prone's floor-of-1 clamp exists precisely because the plain `−Y` overlay could otherwise zero out movement). |
| DEC-122 provisional status unaffected | DEC-122 itself remains explicitly provisional ("this decision may change in the future if a better system can be found," per Tiwa's original DEC-122 ruling). This G1 ruling extends the same formula-based approach to the remaining movement-affecting Conditions and would need re-examination alongside any future DEC-122 supersession. |
| No canonical change | This ruling touches only non-canonical material (Conditions subsystem, Time/Action economy). The Locked Canonical Core (D1) is untouched. |

## 5. Cross-References

**Preserves (unchanged by this ruling):**

- DEC-004 — Movement Speed formula (`floor((bsp+bss)/15)`), never modified by any overlay.
- DEC-078 — Encumbrance Condition mechanism (`Tier-Y Encumbered Value Z`).
- DEC-079 — Conditions subsystem format (`Tier-Y Condition Value Z`, `Z = −Y`; C2 magnitude
  scaling; C5 Movement Speed overlay-on-effective-stat principle).
- DEC-082 / DEC-082.A — Time/Action economy (Skill-side/Movement-penalty model only; no
  action-point pool); G1 was DEC-082.A's sole remaining open item alongside the general
  Time/Action subsystem scope.
- DEC-115 / DEC-116 / DEC-117 — Unified StateRecord schema; this ruling adds no new field
  and no new record type.
- DEC-122 — Self-referential-Y total-lock treatment (Stunned/Incapacitated/Restrained/
  Grappled/Prone); remains the governing mechanism for those five Conditions specifically;
  provisional status unchanged.
- DEC-125 — Prone crawl floor-of-1 clamp; cited as the precedent pattern for future
  content-authored exceptions under this ruling.
- DEC-077.A — Content-authoring path; governs any future per-Condition exception.
- DEC-133 / DEC-133.A — G5 movement-resolution granularity; G1 remains a distinct G-series
  item, not merged into or resolved by G5.

**Not touched:**

- G3 (duration/time-unit scale) — remains open, unaffected by this ruling.
- The broader Time/Action subsystem (Proposals §12, Reserved) — remains open beyond the
  items already closed by DEC-082.A and this G1 ruling.

## 6. Required OpenCode Actions

1. Assign a DEC number to this ruling (suggested placement: as an amendment/closure entry
   associated with DEC-082.A, DEC-133, or DEC-133.A, consistent with how prior G-series
   closures were recorded — e.g., the DEC-079.A / DEC-081.A / DEC-082.A amendment pattern).
2. Record the ruling text (Section 3) verbatim into the decision register
   (`_consolidation/decision-register.md`), Section B (Non-canonical designer rulings).
3. Update DEC-082.A's cell to remove G1 from its "remains open" list, replacing it with a
   pointer to the new DEC entry.
4. Update DEC-133 / DEC-133.A's cross-references to reflect that G1 is now closed
   (G3 remains the sole open G-series item from that cluster, alongside DEC-133's other
   explicitly-left-open consuming-mechanic items).
5. Update Proposals/WIP §12 (Time/Action) and §20 (Open Residual Decision Register) if and
   where those documents separately track G1's status.
6. No Canonical Rules (D1) change is required.

## 7. Reconfirmation Checklist for Tiwa

- [ ] Confirms Option A (uniform Tier-based formula; no table) as the adopted mechanism.
- [ ] Confirms the content-authoring escape hatch (Section 3, final sentence) is intended
      as stated, or should be narrowed/removed.
- [ ] Confirms no numeric ceiling or floor beyond DEC-125's existing Prone precedent is
      intended at this time.
- [ ] Confirms DEC number placement/association preference (standalone new DEC vs.
      amendment to DEC-082.A or DEC-133.A) — no preference was stated in-session; OpenCode
      may propose one per its own recording conventions, or Tiwa may specify.

---

*End of record. This document confers no authority beyond recording Tiwa's in-session
ruling for OpenCode's formal processing. It is not a Canonical or non-canonical rules
document until OpenCode records it into the live register.*
