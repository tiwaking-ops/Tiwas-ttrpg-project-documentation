---
document:
  title: "EQ-1/EQ-2 — Item Creation, Upgrade & Repair (Decision Draft)"
  version: "v0.1"
  status: "Advisory draft — Non-Canonical. Not a ruling. Pending Tiwa review and formal 8-step Promotion Rule."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  role: "Advisory only — presents options and drafts formal text at Tiwa's direction; does not rule."
  created_date: "2026-09-07"
---

# EQ-1/EQ-2 — Item Creation, Upgrade & Repair — Decision Draft

**Status: Advisory draft.** This document formalizes mechanical decisions Tiwa has verbally
made in-session (2026-09-07) into ruling-ready text, and separately flags every remaining
gap as an explicit open question. Nothing in this document is Canonical or Ruled until
Tiwa confirms it to OpenCode and OpenCode records it against the live Decision Register.

**Scope:** Closes part of EQ-1 (item base state) and OI-SU-08/EQ-2 (Repair). Does not
resolve the full Equipment subsystem (Proposals §13, Reserved).

---

## 1. Precondition: Amendment to DEC-081

**DEC-081** (§5.5 Equipment state model) currently rules: *"Items have no independent
state-tracker; their mechanical state is represented entirely by the Condition and Tag
system."*

This draft's Item Creation/Upgrade mechanic (§2 below) gives items an independent
`Tier`/`Magnitude` pair that is **not** a Condition or Tag record. This is a direct
conflict with DEC-081's core clause, not a compatible extension.

**Proposed amendment text (pending Tiwa ruling):**

> DEC-081 is amended: items possess an independent base **Item Tier / Item Magnitude**
> record (§2, this document), established at creation and modified by Upgrade. This base
> record is separate from, and not superseded by, the Condition/Tag system, which
> continues to represent all *negative* equipment state (Sunder, Equipment Damage) per
> DEC-060/DEC-079/DEC-115 unchanged. DEC-081's "held items receive the Location of the
> holding limb" clause and equipment-state-via-Tags framework for negative state are
> otherwise preserved unchanged.

**Schema-placement note:** the Item Tier/Magnitude record is **not** placed inside the
DEC-115/117 unified StateRecord schema as a new `Type`. It uses `Z = Y` (see §2), which
would conflict with DEC-115 R2's `Z = −Y` semantics if merged into that schema. It is
recorded as a **separate, item-native record**, outside DEC-115/117's scope. This should
be stated explicitly if adopted, so it is never misread as a DEC-115 R2 violation.

**OPEN Q1 (unresolved, requires Tiwa ruling):** Confirm adoption of this amendment as
worded, or amend further.

---

## 2. Item Creation

| Field | Rule |
|---|---|
| Trigger | A character makes a Skill Roll using an Item Creation Skill (existing or new Advanced Skill lineage; no new Skill category is introduced — an ordinary Skill per §5 Core Rules) |
| Item Tier (`Y`) | = Skill Tier of the Creating Skill, at time of the successful roll |
| Item Magnitude (`Z`) | = Skill Tier of the Creating Skill (**`Z = Y`** — same numeric value; NOT Margin, NOT `−Y`) |
| Resolution | Ordinary Core Test (DEC-006, 9-step transaction) — full Cost = natural roll, full Failure XP, full Double-eligibility. No exemptions. |

**`Z = Y` note:** this is intentionally distinct from Effect/Condition's `Z = −Y`
(DEC-035.A/DEC-079). Two different record Types carry two different magnitude formulas;
this is not an inconsistency, provided it is stated explicitly in final rule text.

**OPEN Q2 (unresolved):** Failed Creation roll behavior. Default assumption (no
independent Tiwa ruling given) — no item is produced; ordinary Core Test consequences
still apply in full (Cost, Failure XP, and a qualifying failed Double still creates an
Advanced Skill per DEC-012, independent of item creation succeeding or failing). Flagged
for explicit confirmation, not assumed as final.

---

## 3. Item Upgrade

| Field | Rule |
|---|---|
| Eligible skill | The same Item Creation Skill used to make the item, OR a dedicated Item Upgrade Skill |
| Gate | Upgrading Skill's Tier **>** current Item Tier (strictly greater, not ≥) |
| On success | Item Tier **+1**; Item Magnitude **+1** |
| On failure | **Unresolved — see Q3** |
| Resolution | Ordinary Core Test (DEC-006), as per Creation |

**OPEN Q3 (unresolved, blocking):** the failure-consequence wording from the originating
session ("no effect on the Item Upgrade except its Skill Tier increases") is ambiguous
between two readings:

- **Reading A (recommended default):** "its" = the Upgrading Skill's own Tier. A failed
  Upgrade roll has no special item-side consequence beyond ordinary Core Test behavior —
  Failure XP accrues normally (DEC-009), and a qualifying failed Double still creates an
  Advanced Skill (DEC-012) exactly as it would for any other failed test. No new mechanic
  is introduced under this reading.
- **Reading B:** "its" = the **Item's** Tier. A failed Upgrade roll increases the item's
  own Tier with no Magnitude gain. This would be a novel mechanic (failure improving the
  target object's Tier) with no existing precedent elsewhere in the register, and would
  require independent justification if adopted.

This draft does not select between A and B. **Requires explicit Tiwa ruling before
formal text is finalized.**

---

## 4. Repair (Equipment Damage / Sunder recovery) — Option C, Margin-Accumulation Extended Test

**Adopted mechanism (per Tiwa's selection, this session): Option C.** Repair is modeled
as a literal Extended Test instance (S-9/S-10), structurally identical to DEC-073's
treatment of S-11 Rest/Healing as an Extended Test instance.

### 4.1 What Repair targets

Repair operates on the **Equipment Damage or Sunder record's own `Tier Y`** (DEC-060,
DEC-079 C8, unified under DEC-115 as Effect/Condition-typed StateRecords) — a track
entirely separate from the Item Tier/Magnitude established in §2–3. `Z = −Y` continues to
govern these records unchanged (DEC-079 C2); Repair reduces `Y`, and `Z` auto-updates.

### 4.2 Mechanism

For a given negative record at current Tier `Y_current`:

1. **Gate (per attempt):** Repair Skill-Tier ≥ `Y_current`. If false, no attempt is
   possible. (Matches DEC-035.A cl.5's Wound-healing gate exactly.)
2. **Each attempt = one ordinary Core Test** (DEC-006) — full Cost, full Failure XP, full
   Double-eligibility, paid from the Repair skill's own resource domain. No exemptions
   (mirrors DEC-071's "explicit Skill Test required, not passive").
3. **Progress accumulation (DEC-067 pattern):** each successful attempt's Margin
   (`Skill − Roll`) adds to a running Repair-Progress total **scoped to that specific
   record**. Monotonically increasing, never decreases.
4. **Failure is neutral (DEC-068 pattern):** costs resources, generates ordinary Failure
   XP, does not reduce or reset accumulated progress.
5. **Completion target:** GM discretion, no fixed formula (DEC-070/074 precedent). On
   reaching threshold, `Y_current` drops by 1 step; `Z` auto-updates via `Z = −Y`.
6. **Full clearance:** at `Y = 0`, the record is removed entirely.
7. **Re-gate on each step-down:** gate (step 1) re-evaluated at the new, lower Tier.

### 4.3 Worked example (validated against Tiwa's original scenario)

Shield: Equipment Damage Tier 4 (`Z=−4`); Sunder Tier 6 (`Z=−6`). Repairer: Skill-Tier 5.

- Equipment Damage: gate 5 ≥ 4 ✓ — attempts permitted; Repair-Progress accumulates via
  Margin until threshold reached, then Tier 4 → 3 (`Z` −4 → −3), re-gate 5 ≥ 3 ✓, repeat
  to clearance.
- Sunder: gate 5 ≥ 6 ✗ — **no attempt possible** until the repairer reaches Skill-Tier 6+
  (via Advanced Skill progression, DEC-012).

### 4.4 Open questions specific to Repair (unresolved)

| # | Question |
|---|---|
| Q-R1 | Does Repair-Progress reset to zero after each Tier step-down, or carry over toward the next step? |
| Q-R2 | Should the GM-set completion threshold scale with the record's current Tier, or stay flat? (Advisory only — DEC-070/074 impose no formula either way.) |
| Q-R3 | Multiple negative records on one item: confirmed independent — each has its own gate check and its own Repair-Progress counter, repaired as fully separate Extended Test tracks. Requires explicit confirmation. |
| Q-R4 | Repair skill lineage: usable via the Item Creation/Upgrade Skill, a dedicated Repair Skill, or either (symmetric to Upgrade's flexibility in §3)? |
| Q-R5 | Mid-combat vs. downtime: unrestricted ordinary Core Test (default, absent a stated exception), or restricted to a Rest period as DEC-071 does for HP/Wound healing? |

---

## 5. Consolidated Ruling Checklist

| # | Item | Status |
|---|---|---|
| Q1 | DEC-081 amendment (§1) — adopt as worded? | Open |
| Q2 | Failed-Creation consequence (§2) — confirm default? | Open |
| Q3 | Failed-Upgrade "its" ambiguity (§3) — Reading A or B? | **Open — blocking** |
| Q-R1 | Repair-Progress reset behavior across Tier steps (§4.4) | Open |
| Q-R2 | Threshold scaling guidance (§4.4) | Open (advisory only) |
| Q-R3 | Independent-tracks confirmation for multiple records (§4.4) | Open |
| Q-R4 | Repair skill lineage flexibility (§4.4) | Open |
| Q-R5 | Mid-combat/downtime restriction (§4.4) | Open |
| Flag-1 | Damage/Repair track model (§7.1) | **Ruled — Option B, this session** |
| Flag-2a | `state:unusable` gating (§7.2) | **Ruled — Option B, this session** |
| Flag-2b | Repair eligibility on Unusable items (§7.2) | **Ruled — Yes, this session** |
| Flag-3 | DEC-117 companion Tier-mutation clause (§7.3) | **Ruled — Adopted, this session** |

**Ruled/confirmed this session (§2–4, main tables):** Item Tier/Magnitude-at-creation
formula (`Y = Skill Tier`, `Z = Y`); Upgrade gate and per-success increment (`Tier > Item
Tier` → both +1); Repair mechanism selection (Option C, Margin-accumulation Extended
Test) and its core gate/progress/threshold structure.

**Ruled/confirmed this session (§7, OpenCode assessment-flag resolution):** damage/repair
track model (Option B — record-only, no Item Magnitude ablation); `state:unusable`
semantics (gates on negative-record presence/Tier, not on Item Magnitude); Repair
eligibility on already-Unusable items (permitted); DEC-117 companion Tier-mutation
clause (adopted).

---

## 7. Resolution of OpenCode Assessment Flags (2026-09-07)

OpenCode raised three joins this draft left unresolved. Tiwa ruled on all three,
same session. Recorded here for the formal handoff.

### 7.1 Flag 1 — Synced-track fork: Option B adopted

**RULED — Option B (record-only). Damage does not ablate Item Magnitude.** The
Equipment Damage / Sunder record (§4.1) is the **sole representation** of accumulated
harm to an item. Item Magnitude, set at Creation and incremented by Upgrade (§2–3), is a
**creation-quality stat only** — it is never read, written, or referenced by damage
application or by Repair. Repair (§4) reduces the negative record's Tier exclusively, as
already specified; no companion Item-Magnitude restoration step exists or is needed.

**Rationale (Tiwa):** this is intentionally the same shape as Tiwas's existing Wound/
Effect healing architecture (DEC-035.A Wound format, healing gated by Skill-Tier ≥ Wound
Tier, magnitude derived as `Z = −Y`) — one record, one Tier, one healing/repair lever.
Item Creation/Upgrade's `Z = Y` track and the Equipment Damage/Sunder `Z = −Y` track
remain two genuinely separate numbers on two separate record families, never synced.

**Consequence:** softens the DEC-058 durability-pool tension flagged previously — Item
Magnitude is confirmed as pure creation-quality content, not a disguised soak/HP pool,
so DEC-058's "no numeric durability/soak pool" for Armor is not put in tension by this
draft. §1's DEC-081 amendment (Q1, still open) is unaffected by this ruling — items
still need an independent state-tracker for their base Tier/Magnitude; that tracker
simply never interacts with damage.

### 7.2 Flag 2 — `state:unusable` semantics

**RULED — (a) Option B: `state:unusable` gates on the negative record's presence/Tier,
not on Item Magnitude.** Per Flag 1's resolution, Item Magnitude was never ablated by
damage, so there is nothing on that track to restore. `state:unusable` is instead a
Tag/state applied directly by the Equipment Damage / Sunder record's existence (exact
Tier threshold, if any, is content-authoring — not resolved by this ruling). Clearing
the record via Repair (§4.2 step 6, `Y=0`) directly lifts `state:unusable`, since the
trigger and Repair's target are the same record — no cross-track synchronization is
required.

**Rationale (Tiwa):** `state:unusable` exists to leave an item's physical fate
deliberately undetermined until someone actually attempts to assess or repair it —
whether it turns out to be salvageable or effectively destroyed is discovered through
play (a Repair attempt), not predetermined by a numeric threshold check alone.

**RULED — (b) Yes.** Repair may be attempted on an already-Unusable item. Existing Tags
on the item may make the attempt harder (via ordinary Skill-Tier gating, §4.2 step 1, or
GM-fiat difficulty per DEC-063 Skill-side modifiers), but the *option* to attempt is
never mechanically foreclosed by the Unusable state itself.

**Rationale (Tiwa):** beyond GM fiat making an attempt harder, a repairer should always
be permitted to at least try.

### 7.3 Flag 3 — Record-edit mechanism: DEC-117 companion clause adopted

**RULED — Adopted as worded.** The following is confirmed as the formal mechanism
authorizing Repair's Tier-mutation behavior, standing alongside DEC-117 R5 rather than
overloading it:

> A qualifying Skill Test result (per an explicitly-defined repair/restoration
> mechanism — this draft's Option-C Repair, §4) may **mutate an existing StateRecord's
> `Tier Y` downward by one step**, with `Magnitude Z` recalculating automatically per
> that record Type's existing formula (`Z = −Y` for Effect/Condition records). This is a
> **Tier-mutation operation**, distinct from DEC-117 R5's whole-record removal-via-
> `removal_tags`: it does not consult `removal_tags`, is not restricted to a single
> application, and requires no Tier-matching between actor and target beyond the
> existing Repair gate (Repair Skill-Tier ≥ record's current Tier, re-evaluated at each
> step, §4.2 step 1/7). Full clearance (`Y=0`) removes the record entirely, converging
> with R5's end-state via a different, incremental path.

**Rationale (Tiwa):** this mirrors the existing Wound/Effect healing system precedent
directly — the same "Skill-Tier-gated, stepwise reduction toward zero" shape already
governs Wound healing (DEC-035.A cl.5) and is simply being formally named as a
DEC-117-adjacent operation rather than left implicit.

---

## 8. Preserves / Does Not Alter

DEC-006/007 (Core Test Transaction, Cost/Overflow), DEC-009 (Failure XP), DEC-012
(Advanced Skill creation), DEC-035.A (Wound format, healing-gate precedent), DEC-058
(Armor no-durability-pool — reinforced, not just preserved, by Flag-1's ruling), DEC-060/
DEC-079 (Sunder/Condition format, `Z=−Y`), DEC-067/068/070 (Extended Test progress/
failure/completion-target precedents), DEC-071/073/074 (S-11 Extended-Test-instance
precedent), DEC-081 (Equipment state via Conditions/Tags — pending the §1 amendment for
the Item base-record addition only; negative-state representation otherwise unchanged),
DEC-115/116/117 (unified StateRecord schema for Effect/Condition/Tag — Item explicitly
kept outside this schema per §1; R5 unchanged, companion Tier-mutation clause added
alongside it per §7.3). Invariant 6 (Cost = natural roll), Invariant 17 (no new resource
pool — Repair-Progress is a per-record bookkeeping value, not a spendable pool,
consistent with DEC-069's non-violation assessment for the identical Extended Test
pattern).

**No Canonical Rules affected. Nothing in this document is promoted to Canonical or
Ruled status by virtue of being drafted.**
