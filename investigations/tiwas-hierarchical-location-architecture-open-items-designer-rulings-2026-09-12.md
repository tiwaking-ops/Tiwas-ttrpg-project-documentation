---
document:
  title: "Hierarchical Location Architecture — Open-Item Designer Rulings (2026-09-12)"
  version: "1.0"
  status: "Designer-ruling source record — Non-canonical designer ruling, ruled in-session by Tiwa 2026-09-12; recorded by OpenCode per standing governance. Not Canonical; promotion requires the 8-step Promotion Rule (REQ-021)."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
---

# Hierarchical Location Architecture — Open-Item Designer Rulings

## 0. Governance Notice

This document is the **source record** of two in-session designer rulings made by
**Tiwa** on **2026-09-12**. OpenCode (big-pickle) recorded the rulings after Tiwa's
explicit sign-off, per the standing role separation: **Tiwa rules; OpenCode records**.
Recording here does **not** make anything Canonical — these remain non-canonical
designer rulings; entry into Canonical rules still requires the 8-step Promotion Rule
(REQ-021 / `governance/status-model.md`).

Options were presented in:
`investigations/tiwas-hierarchical-location-architecture-open-items-designer-options-brief-2026-09-12.md` (advisory; no DEC inferred).

Register effect (recorded separately in `_consolidation/decision-register.md`): new
**DEC-136** plus in-cell amendment annotations on **DEC-042, DEC-112, DEC-113, DEC-114**
(and the in-place fork note inside DEC-105), preserving original cell text.

---

## 1. Ruling Q1 — DEC-042 secondary roll (Option A: removed for all Effects)

> **Selected option:** Option A — Pure single-source (strict DEC-112).
>
> **Tiwa's reason (verbatim):**
> “The proposal was given after a decision to remove all secondary rolls had already
> been made.”

### Operative content

- The **DEC-042 secondary location roll is removed for every Effect, including
  Armor Bypass.** DEC-112 **L-011** ("Secondary roll: removed") governs
  unconditionally together with **L-003** (single-source deterministic resolution).
- Tier-2 **Armor Bypass** resolves via the deterministic Location Index → Location
  Template address path (DEC-112 L-003/L-004) when the L-010 100-state allocation and
  L-009 Human template exist. Until that content is authored, Tier-2 Armor Bypass is
  **anchored but not yet resolvable** (State-2 classification in the DEC-019 / Canonical
  §14.7 sense) and resolves at **Tier 1 coarse**.
- Register reconciliation performed under this ruling:
  - DEC-113 **R2** — the Armor Bypass clause "resolved via the DEC-042 secondary roll"
    is superseded; Armor Bypass remains the **only Tier-2-eligible Effect**, now resolved
    via the single-source deterministic address path.
  - DEC-113 **Consequence note** ("the DEC-042 secondary roll is used only by promoted
    Armor Bypass resolutions") is **vacated** — the secondary roll is used by **no**
    Effect.
  - DEC-113 **R3** (PC-only one-step coarser downgrade) **remains operative**; its
    rationale is restated: the downgrade drops the deeper sub-zone address depth
    (accepting the coarser Tier-1 outcome), not "a roll".
  - DEC-114 **R2** — "location match evaluated at DEC-112 sub-zone level via the
    DEC-042 secondary roll" is superseded; the location match is evaluated via the
    single-source deterministic address path.
  - DEC-105's embedded fork note (the stored playtest-brief annotation flagging
    "DEC-113 R2's Armor Bypass reference to the DEC-042 secondary roll is superseded by
    DEC-112 L-011 … fork still open") is **closed**.
  - DEC-042 remains recorded for design history; the "Option A … explicitly revoked
    this session" note now extends to **all** uses of the roll.

### Constraints preserved

Invariant 18 (no parallel resolution engine), DEC-030 / DEC-112 L-014 (mismatch
fallback remaining under the deterministic model), Invariant 17, DEC-062 (armor
location-bound), DEC-041 (Skill-Tier ≥ 2 gate), DEC-107 (severity tier orthogonal to
Location Tier).

---

## 2. Ruling Q2 — Location Tier ceiling (Option B: unbounded)

> **Selected option:** Option B — Unbounded (literal "no cap").
>
> **Tiwa's reason (verbatim):**
> “Simplification of Skill Tier to Location Tier. Although Location Tier technically
> ends at Tier 12 it would easily be possible to extend it beyond Tier 12. The chance
> of a character having a Skill Tier greater than 12 is extremely low though.”

### Operative content

- DEC-112 **L-005** ("no cap") is confirmed **literally**: **Skill-Tier maps directly
  to Location Tier with no architectural ceiling.** A Location Tier beyond 12 is
  architecturally possible (canonical rules v1.3 §5.1: theoretical maximum Skill-Tier
  = **24**).
- The proposal's 12-tier ladder (LOC-I15) is adopted as **content/authoring guidance,
  not a rule**: templates are expected to author meaningful depth up to ≈Tier 12;
  nothing forbids deeper authored depth if a creature genuinely needs it.
- Effective resolution per target remains bounded by **authored template depth**
  (`L_actual = min(S, D)`); depth is a content property, not a rule ceiling.

---

## 3. What Did Not Change

- The hierarchical Location Address architecture (DEC-112 L-001–L-014) is unchanged
  except for the reconciliations in §1 (all preserving L-011 as adopted).
- DEC-100 Tier-1 quartiles (1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head) are
  **not reopened** by either ruling. The proposal's separate recommendation to
  re-investigate those quartiles remains an **unperformed, lower-priority item**.
- DEC-041/042/100/113 register reopening-proposal brackets are resolved only to the
  extent the rulings above address them; the L-009/L-010 **content** deferrals stand.
- No Canonical text is created or changed.

## 4. Non-Decisions

This record does not: author the L-009 Human Template; author the L-010 100-state
allocation; establish Tier-1–12 semantics as canonical; reopen DEC-100, DEC-062,
DEC-030, DEC-014, or DEC-107; or promote anything.

## 5. Follow-Up

Per Tiwa's instruction, a **100-state allocation / information-capacity investigation
brief** is produced in the same session:
`investigations/tiwas-location-100-state-allocation-information-capacity-investigation-2026-09-12.md`.