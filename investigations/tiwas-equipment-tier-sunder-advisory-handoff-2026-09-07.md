---
document:
  title: "Equipment-Tier Effect Interaction & Sunder Redesign — Advisory Handoff"
  version: "v1.0"
  status: "Advisory session record — Non-Canonical. Not a ruling."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-07"
  last_modified_date: "2026-09-07"
session_role: "Claude acted in its standing advisory capacity only. No ruling was made or implied at any point in this session. All items below require Tiwa's explicit ruling before OpenCode may record any DEC number against the live register."
---

# Equipment-Tier Effect Interaction & Sunder Redesign — Advisory Handoff

## 0. Purpose and Scope

This document records the complete advisory output of a single chat session (2026-09-07) covering two related investigations:

1. How the S-3 Equipment-tier Effect menu currently populates and applies, per the live Decision Register, including gaps surfaced by cross-referencing existing DECs against one another.
2. A design-options analysis for improving the Sunder mechanic, at Tiwa's request, incorporating a cross-system research pass on item-damage/destruction models in comparable TTRPGs.

**Authority statement:** Nothing in this document is Canonical. Nothing in this document is a designer ruling. All analysis is advisory, per the standing governance model (`governance/authority.md`, `governance/status-model.md`). Where this document identifies a conflict with an existing non-canonical designer ruling (§2.5, DEC-058), that conflict is flagged for Tiwa's resolution, not resolved by this document. OpenCode must not record any DEC number, status change, or register update from this document's contents without Tiwa's explicit sign-off on each numbered item in §4 (Open Questions Register).

---

## 1. Equipment-Tier Effect: Current State as Ruled

### 1.1 Menu placement

Per DEC-023.A, the Equipment tier of the S-3 Effect menu contains five named entries:

| Effect | Trigger mechanism ruled? |
|---|---|
| Disarm | Yes — DEC-028 / DEC-114 |
| Break / Sunder Item | Ambiguous — see §1.5 |
| Armor Bypass | Yes — DEC-028 / DEC-114 |
| Disable Device / Weapon | **No ruling exists** |
| Steal / Take Item | **No ruling exists** |

Only three of the five entries (Disarm/Break Hold, Equipment Damage, Armor Bypass) are the set DEC-028 actually names as Tag+Location-gated. "Disable Device/Weapon" and "Steal/Take Item" appear on the DEC-023.A content list with no trigger, tag, or gating mechanism anywhere in the register.

### 1.2 Trigger gate (DEC-028, narrowed by DEC-041)

For the three in-scope Effects, triggering requires **both**:

- a matching gear/ability Tag, **and**
- a supporting Location Index at Tier 1+ (DEC-028), producible only by a **Skill-Tier ≥ 2** promoting roll (DEC-041 item 1).

### 1.3 Tag-match table (DEC-114, R2)

DEC-114 closed DEC-028's "matching gear/ability Tag" ambiguity with a per-Effect table:

| Effect | Tier (DEC-113) | Tag condition | Location match granularity |
|---|---|---|---|
| Armor Bypass | Tier 2 | Target has `defense:armor` bound to the struck sub-location, or `defense:shield` if the shield occupies that sub-location | DEC-112 sub-zone (via DEC-042 secondary roll) |
| Disarm / Break Hold | Tier 1 | Target has a `state:held` item carrying `slot:main_hand` or `slot:two_hand` | DEC-100 coarse zone |
| Equipment Damage | Tier 1 | Target has **any** `state:held` or `state:worn` gear at the struck coarse zone — no `damage:*` type match required | DEC-100 coarse zone |

### 1.4 Fallback on partial match

DEC-030 applies identically to all three: a partial match (Tag without location, or location without Tag) causes the declared Effect to **fail entirely**, and the successful S-1 contest applies Base-tier Inflict Injury (HP-only) instead. No graded/partial outcome exists under current rulings.

### 1.5 Naming ambiguity: "Break/Sunder Item" vs. "Equipment Damage"

DEC-023.A's menu lists **"Break / Sunder Item"** as an Effect name. DEC-028/DEC-114's trigger table governs an Effect referred to as **"Equipment Damage."** No ruling states whether these are the same Effect under two names, or two distinct Effects (e.g., a lesser "damage" state short of full Sunder).

- If identical: DEC-114's trigger table is implicitly Sunder's trigger table, and this is a documentation inconsistency only.
- If distinct: Equipment Damage has a trigger mechanism (DEC-114) but no defined payload, since DEC-060/DEC-079 define only Sunder's payload.

This is flagged as **Open Item OI-EQ-01** (§4) and is not resolved by this document.

### 1.6 Payload — Sunder (DEC-060)

The only ruled payload for a successful Equipment-tier hit is DEC-060's Sunder: an Impose Condition Effect adding a `state:sundered` Tag (DEC-079 C8) to the item. It is:

- **Additive** — does not delete existing Tags on the item.
- **Permanent** — persists until deliberately addressed; no automatic reversion.
- Resolved via the ordinary Core Test Transaction (DEC-006) — not a new resolution engine.

### 1.7 Item location (DEC-081)

Equipment has no independent state tracker; its mechanical state lives entirely in the Condition/Tag system. Held items automatically inherit the Location of the holding limb — no separate Location-assignment step is required, which is what allows DEC-114's "gear at the struck coarse zone" check to function without a parallel item-location subsystem.

### 1.8 Record shape under the current unified schema (DEC-115/116/117)

A successful Equipment-tier hit producing Sunder currently generates:

```
Type: Condition (Sunder is Impose-Condition-typed per DEC-060)
Tag: state:sundered  (Type: Tag; duration: permanent per DEC-117 R2 default)
Location X: [struck coarse zone / item slot]
Tier Y / Magnitude Z: not populated — DEC-116 confirms Tags are
    Tier/Magnitude-optional and absent-by-default; state:sundered
    has never been ruled to carry a number.
```

Removal (repair) would require a `removal_tags` entry naming `state:sundered` on a repairing Effect per DEC-117 R5 — no such repairing Effect has been authored.

---

## 2. Additional Gaps Identified (Cross-Referenced, Not Independently Ruled)

The following three items were surfaced during this session by cross-referencing existing DECs against one another. They are new observations, not new rulings, and are added to the tracking list at Tiwa's discretion.

### 2.1 Sunder has no numeric or functional effect defined (OI-EQ-02)

DEC-060 defines Sunder's payload only as "reduced effectiveness" — never operationalized into a mechanic. This is sharpest for armor specifically: does a Sundered Armor Tag stop functioning entirely (no longer contributes per DEC-058, no longer eligible for Bypass matching per DEC-059), or function at a reduced but defined capacity? As written, "reduced effectiveness" is unenforceable for any item type.

### 2.2 No item-selection rule when multiple items share a struck zone (OI-EQ-03)

DEC-114 R2 triggers Equipment Damage against "any equipped gear at the struck coarse zone," but a single coarse zone can hold multiple `state:held`/`state:worn` items simultaneously. No rule specifies which item receives the Sunder Tag when more than one candidate exists. DEC-102 already solved an analogous problem for Wound-attribute/skill targeting (random for creatures/automated characters, player choice for PCs); no equivalent ruling exists for Equipment Damage item selection.

### 2.3 Terminology collision: two unrelated mechanics both named "Bypass" (OI-EQ-04)

- **DEC-059 "Bypass"** (S-5 Armor): a stateless relational property declared on an Armor Tag's own rule text — the Armor Tag simply does not trigger against Effects carrying a specified countering Tag. Evaluated automatically; no attacker action or Effect selection involved.
- **DEC-023.A / DEC-028 / DEC-114 "Armor Bypass"**: a selectable S-3 Effect the attacker declares on a contest win, gated by Tag+Location.

No ruling states how these interact if both could apply to the same exchange (e.g., an attacker declares the Armor Bypass Effect against armor whose own DEC-059 Bypass clause names a different countering Tag). This reads as an unintentional naming collision, not a deliberate two-layer design, but that assessment is not itself a ruling.

---

## 3. Sunder Redesign: Options Analysis (Advisory)

### 3.1 The governing conflict: DEC-058

DEC-058 (S5-A, Armor architecture) rules: **"No numeric durability/soak pool"** for Armor — armor is Tags/Traits only, "structurally identical in kind to item Tags **generally**." The word "generally" extends this reasoning beyond armor to equipment as a category.

Tiwa's stated design goal — Sunder should damage an item, with an accumulation threshold past which the item becomes unusable (destruction status immaterial) — is, mechanically, a request for an item health/durability track. Any implementation using an accumulating numeric pool and a numeric threshold **conflicts with DEC-058 as currently worded** and requires either an amendment to DEC-058 or a ruling narrowing its scope to armor specifically. This document does not resolve that conflict; see Open Item OI-EQ-05.

### 3.2 Cross-system research summary (paraphrased; general design patterns, not verbatim rules text)

| System | Item-damage model | Threshold behavior |
|---|---|---|
| Pathfinder 1e / D&D 3.5 | Objects have Hardness (a form of damage reduction) plus a fixed Hit Point pool scaled by size/material; a Sunder maneuver applies weapon damage minus Hardness to that pool | Destroyed at 0 HP; a "broken" condition at roughly half HP imposes a penalty before destruction |
| D&D 5e | Objects have Armor Class and Hit Points by material/size; damage reduces HP directly | 0 HP = destroyed; no intermediate broken state in core rules |
| GURPS | Objects have Hit Points (derived from size/material) and Damage Resistance; damage resolves as ordinary combat damage | 0 HP = broken/destroyed; some variants add a "crippled" threshold at a fraction of maximum HP |
| Shadowrun | Gear has a Structure/Armor rating; sustained damage reduces the effective rating | Rating reaching 0 renders the item nonfunctional; destruction is not mechanically load-bearing |

**Observation:** every surveyed system uses some numeric pool (however labeled) that depletes to a threshold. None achieve item-unusability through a pure Tag/flag system with no numeric tracking — that constraint is specific to Tiwas' architecture (DEC-058), not an external design norm. No precedent exists that satisfies both Tiwa's stated goal and DEC-058 as currently worded without some compromise.

### 3.3 Design Option A — Staged Tag degradation (no numeric pool)

A tiered Tag replacement using the existing Tag/Condition architecture, with no Magnitude field populated:

| Stage | Tag | Meaning |
|---|---|---|
| 0 | *(no tag)* | Fully functional |
| 1 | `state:damaged` | Reduced effectiveness (content-authored penalty, DEC-060 addition-model precedent) |
| 2 | `state:sundered` | Unusable |

Each successful Equipment-tier hit replaces the item's current stage Tag with the next stage (an Impose Condition Effect, DEC-060's addition model, applied as stage-advancement). No Magnitude is populated — consistent with DEC-116's default that Tags are Tier/Magnitude-optional and absent-by-default.

- **Compatibility:** Requires no amendment to DEC-058.
- **Limitation:** Only a two-step staircase; cannot express fine-grained accumulation without adding more stages, which does not add genuine numeric tracking.

### 3.4 Design Option B — Item Wound record (reuses the existing Wound schema)

Gives items a record shaped identically to a character Wound (DEC-035.A format, folded into the DEC-115 unified schema):

```
Type: Effect (Sunder-Wound)
Location X: [struck coarse zone / item slot]
Tier Y: accumulates per hit (same-tier stacking, DEC-035.A cl.4)
Magnitude Z: = -Y
```

At a GM-set Tier threshold (GM-discretion pattern consistent with DEC-070/DEC-074), the item becomes unusable — satisfying the stated design goal directly, since only the threshold itself would need defining, with no separate destruction state required.

- **Compatibility:** This is functionally a numeric durability pool and directly conflicts with DEC-058's wording. Requires DEC-058 to be amended or narrowed to armor-only.
- **Advantage:** Reuses an already-ruled schema; delivers real accumulation granularity.

### 3.5 Design Option C — Hybrid: plain hit-counter, binary output

Tracks hits as a bare counter (not a Tier/Magnitude construct) with no per-point mechanical effect until a GM-set count is reached, at which point the existing flat `state:sundered` Tag (DEC-060) is applied as-is.

- **Compatibility:** Still a tracked number per item outside the Tag-only architecture, though smaller in footprint than Option B; still tensions with DEC-058.
- **Advantage:** Provides accumulation without per-tier combat penalties automatically attaching the way Wound Tiers do.

### 3.6 Advisory recommendation

- If DEC-058 is to remain unamended and interpreted broadly (covering all equipment, not just armor): **Option A** is the only compatible choice; a third stage may be added if finer granularity than a binary Sundered flag is desired.
- If DEC-058 is narrowed to defensive Armor DR specifically (a plausible reading, since its original rationale targeted avoiding a second Overflow-adjacent combat economy — a rationale that does not obviously extend to non-combat items like rope or a torch): **Option B** most directly satisfies the stated design goal at low additional design cost.

This is a recommendation for Tiwa's consideration, not a ruling. No option has been adopted.

### 3.7 Repair / removal (applies under any of the three options)

Under DEC-117's schema, repair is an Effect whose `id` appears in the degraded record's `removal_tags` field — a repair skill test that, on success, removes the current-stage Tag (Option A) or decrements the Tier/counter within DEC-117 R5's same-Tier restriction (Options B/C). This is unaffected by which option is chosen. EQ-2 (repair procedures) remains open in all cases and requires its own ruling on skill, cost, and repair magnitude per action.

---

## 4. Open Questions Register (This Session)

None of the following have been ruled. Each requires Tiwa's explicit decision before OpenCode records anything against the live register.

| ID | Question | Depends on |
|---|---|---|
| OI-EQ-01 | Is "Break/Sunder Item" (DEC-023.A) the same Effect as "Equipment Damage" (DEC-028/DEC-114), or two distinct Effects? | — |
| OI-EQ-02 | What does Sunder's "reduced effectiveness" (DEC-060) concretely do, especially for Armor Tags? | OI-EQ-05 |
| OI-EQ-03 | When multiple items occupy the same struck coarse zone, which item receives Equipment Damage/Sunder? | — |
| OI-EQ-04 | How do DEC-059 Bypass (relational Tag-pair property) and the DEC-028/DEC-114 "Armor Bypass" Effect interact if both could apply to the same exchange? | — |
| OI-EQ-05 | Does DEC-058's "no numeric durability/soak pool" apply to all equipment, or only to defensive Armor's combat-relevant DR? | Governs eligibility of Options B/C in §3 |
| OI-EQ-06 | Which Sunder redesign option (A / B / C, §3.3–3.5) is adopted? | OI-EQ-05 |
| OI-EQ-07 | If Option B or C is adopted, what is the GM-discretion threshold (Tier count or hit count) for "unusable"? | OI-EQ-06 |
| OI-EQ-08 | Does resolving OI-EQ-06 also resolve OI-EQ-01 (i.e., does a better-specified Sunder collapse the naming ambiguity into "same Effect")? | OI-EQ-01, OI-EQ-06 |
| EQ-2 (carried, pre-existing) | Repair procedure: what skill, what cost, what magnitude of Tag/Tier reduction per successful repair action? | OI-EQ-06 |

---

## 5. Handoff Instructions for OpenCode

1. Do not assign a DEC number to any content in §1–§3 of this document. This is an analysis and options record, not a ruling.
2. When Tiwa rules on any item in §4, ask Tiwa explicitly for each numbered item before recording — do not infer an answer to one open item from the resolution of another, even where §4 notes a dependency (e.g., OI-EQ-08 must be asked separately even after OI-EQ-01 and OI-EQ-06 are resolved).
3. If Tiwa rules on OI-EQ-05 first, flag back to Tiwa which of Options A/B/C in §3 remain eligible before asking OI-EQ-06, since B and C become unavailable if DEC-058 is confirmed to apply broadly and is not amended.
4. Cross-system research in §3.2 is paraphrased for design-pattern reference only and is not quoted rules text from any external product; it should not be treated as a citation-grade source if this document is later referenced externally.

