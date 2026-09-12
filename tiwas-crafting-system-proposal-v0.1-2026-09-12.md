---
document:
  title: "Tiwas — Crafting System: Materials, Components & Items"
  version: "v0.1"
  status: "Non-canonical proposal. Design exploration only. No DEC assigned. Pending Tiwa's review before any promotion, OpenCode handoff, or playtest."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
scope_note: >
  This document proposes new, previously-unruled mechanics (materials/components,
  a Tier-determination formula for crafted results, recipes, tool requirements).
  It also reuses several already-Ruled mechanics (Item Tier/Magnitude, Extended
  Tests, Repair) by direct citation. Sections are labelled REUSED (cites an
  existing DEC, unmodified) or PROPOSED (new, requires a ruling) throughout.
  Nothing in this document is Canonical, Ruled, or binding until Tiwa acts on it.
---

# Tiwas — Crafting System Proposal v0.1

## 0. Decisions Already Made (by Tiwa, this session)

| # | Question | Tiwa's answer |
|---|---|---|
| 1 | Record relationship | Materials, Components, and finished Items **all use the same Item Tier/Magnitude record** (DEC-128 Q1 / DEC-129 pattern) — distinguished only by a `Type` field, not by separate record shapes. |
| 2 | Quantity tracking | Crafting tracks **exact consumed quantities** of Materials/Components per craft/upgrade/repair. |
| 3 | Component stage | **Mandatory** for anything above base tier — an Item cannot be built directly from raw Materials except at Tier 1 ("simple item," per your original framing that a simple item's maximum Tier is fixed). |

Everything below is built on these three decisions. Where this document goes further than they strictly require, it is flagged **PROPOSED** and listed again in §11 (Open Questions).

---

## 1. Integration Map — What This Touches

| Existing Ruled mechanic | DEC(s) | How this proposal touches it |
|---|---|---|
| Item Tier/Magnitude record, base-equal at creation | DEC-128 Q1 | **REUSED — extended.** Same record now hosts `Type: Material \| Component \| Item`. |
| Magnitude repairable up to Tier via Repair Skill Roll | DEC-129 | **REUSED unmodified.** Applies identically to Materials/Components/Items. |
| Damage does not ablate Item Magnitude; tracked as a separate negative record | DEC-118, DEC-119 | **REUSED unmodified.** A crafted item's *quality* (Tier/Magnitude) and its *damage state* (Equipment Damage/Sunder Condition-type record, `Z = −Y` family) remain two separate records, exactly as DEC-118 established. |
| Item Creation is an Extended Test; failed Creation = no item | DEC-128 Q2 | **REUSED — extended to Components.** See §6. |
| Failed Upgrade → Tier+1, Magnitude+0 (imbalanced) | DEC-128 Q3 | **REUSED unmodified.** Applies to upgrading Materials, Components, and Items alike. |
| Extended Test machinery (Margin-accumulation, neutral failure, GM-set threshold) | DEC-067, DEC-068, DEC-070 | **REUSED unmodified.** Governs every crafting/refining/upgrading roll sequence. |
| Numeric tracking that is not a competing resource pool (precedent) | DEC-078 (Encumbrance) | **CITED as precedent** for why quantity-tracking does not violate Invariant 17. See §7. |
| Skill-Tier as a ceiling on produced severity/Tier | DEC-107, DEC-041 | **PATTERN REUSED.** The Tier-determination formula (§5) mirrors this idiom; it is not itself Ruled. |
| Tags ontology, extensible | DEC-080, DEC-114 | **REUSED unmodified.** Crafted items carry ordinary Tags (`damage:slashing`, `slot:main_hand`, etc.). |
| Equipment subsystem, Open 3 (wealth/economy, EQ-3A) | DEC-081.A | **NOT resolved by this document.** Material *acquisition cost* (buy/forage/mine) is out of scope here — flagged in §11. |
| Invariant 17 (no competing primary resource/progression economy) | Core Invariants | **Reconciled explicitly**, not silently assumed. See §7. |

---

## 2. Unified Record Schema — PROPOSED extension of DEC-128 Q1

```
Item-Family StateRecord:
  id                : unique identifier
  type              : Material | Component | Item        (fiction-level label only)
  subtype           : string                              (e.g. "iron_ore", "steel_ingot", "longsword")
  item_tier         : Y   (integer ≥ 1)
  item_magnitude    : Z   (integer, 0 ≤ Z ≤ Y; Z = Y at creation, per DEC-129)
  quantity          : integer ≥ 1                          (stack count of identical records)
  tags              : list<Tag>                            (DEC-080 ontology; optional, absent-by-default per DEC-116)
  source_record_ids : list<{id, quantity_consumed}>        (recipe provenance trace; not mechanically load-bearing, audit-only)
  negative_records  : list<id>                              (pointers to Equipment Damage / Sunder records, DEC-118/119 — separate Z=−Y family, unchanged)
```

This record family remains **outside** the DEC-115/117 unified Effect/Condition/Tag schema, exactly as DEC-128 Q1 placed the base Item record outside it (this family uses `Z = Y`; the Effect/Condition schema uses `Z = −Y` — the two are incompatible and DEC-128 Q1 already ruled this separation for Items. This document extends that same separation to Materials and Components rather than reopening it.)

`Type` carries no independent mechanics — it is a fiction-level classifier, identical in spirit to how DEC-115/117 use `Type` to distinguish Effect/Condition/Tag on the *other* schema. All Tier/Magnitude/Repair/Upgrade math is type-agnostic.

---

## 3. The Mandatory Pipeline

```
Material  ──(Component Crafting Test)──▶  Component  ──(Item Crafting Test)──▶  Item
   │                                                                                ▲
   └──────────────────(Simple-Item Crafting Test, Tier-1 cap only)──────────────────┘
```

| Path | Permitted? | Tier ceiling |
|---|---|---|
| Material → Component | Yes (this is how Components are made) | Per §5 formula |
| Component → Item | Yes (this is how non-trivial Items are made) | Per §5 formula |
| Material → Item directly | **Only at Item Tier 1** ("simple item") | Fixed at 1 |
| Material → Item directly, Tier ≥ 2 | **Forbidden** (per Tiwa's ruling, §0.3) | — |
| Component used standalone as a finished Item | **Permitted** — a Component is an Item-family record like any other; nothing prevents a Player from using a Steel Ingot, a fletched arrow shaft, etc. as-is if it's mechanically functional in that form. This resolves your own stated uncertainty: the Component stage is *skippable for consumption* (a Component need not ever be folded into something bigger) but **not skippable for production** (an above-Tier-1 Item must still pass through a Component on the way to existing). | N/A |

---

## 4. Materials

| Property | Rule |
|---|---|
| Record shape | Item-family record, `type: Material` |
| Tier meaning | Purity / grade / rarity of the raw substance (e.g., Iron Ore Tier 1 = bog ore; Tier 3 = high-grade vein ore) |
| Magnitude | `Z = Y` at acquisition, identical to DEC-129's base-equality rule |
| Acquisition | **PROPOSED, unresolved.** Whether acquiring a Material requires a Skill Test (mining, foraging, smithing prospecting) or is purchased/GM-narrated is tied to the still-open EQ-3A wealth/economy fork (DEC-081.A Open 3). This document does not resolve it — see §11 item 3. |
| Refining a Material upward | A Material may itself receive an **Upgrade roll** (§8) before being consumed — e.g., smelting raw ore into higher-purity ore. This is not a new mechanic; it is the ordinary DEC-128 Q3 Upgrade procedure applied to a `type: Material` record. |

---

## 5. Tier-Determination Formula for Crafted Results — PROPOSED, unresolved

This is genuinely new ground; no existing DEC specifies how a crafted Component/Item's Tier derives from its inputs and the crafting Skill's Tier. Three candidates, in order of recommendation:

| Option | Formula | Rationale | Risk |
|---|---|---|---|
| **A (recommended)** | `Result Tier = min(Crafting Skill-Tier, max(input Tiers))` | Directly mirrors the DEC-107 idiom (Skill-Tier as the hard ceiling on produced severity) and DEC-041's Skill-Tier gate discipline. Simple, one comparison. | A single high-Tier input with a low-Tier Skill wastes the input's Tier — this may or may not be desired realism. |
| B | `Result Tier = min(Crafting Skill-Tier, floor(average(input Tiers)))` | Mirrors DEC-005's Cap formula (floored average) — thematically consistent with the Core's own Tier math. | Punishes mixing a high-Tier input with low-Tier filler; may discourage using premium materials in bulk crafts. |
| C | GM Fiat, guided by `max(input Tiers)` as a floor | Matches the DEC-035.A cl.6 universal-Fiat-override precedent already used for Wound Tier assignment. | Least mechanically determinate; heaviest GM burden for a "simulation-grade" system. |

**This document defaults to Option A for all worked examples below, but this is a candidate, not a ruling.**

---

## 6. Crafting as an Extended Test — REUSED, extended to Components

Per DEC-128 Q2 ("Item Creation is an Extended Test"), this proposal extends the same treatment to Component creation, Material refining, and Item creation alike — they are all instances of the same Extended Test shape:

| Step | Rule | Source |
|---|---|---|
| Interval | Each crafting attempt (one Core Test on the relevant Crafting Skill) is one Extended Test interval | DEC-067 |
| Progress | Successful intervals accumulate Margin (`Skill − Roll`) toward a completion threshold | DEC-067 |
| Failure | A failed interval costs resources and generates ordinary Failure XP but does **not** reset progress | DEC-068 |
| Completion threshold | GM discretion, no fixed formula | DEC-070. **PROPOSED refinement:** scale the threshold with the target Tier (e.g., `threshold = Tier × k`, `k` content-authored per DEC-077.A) — flagged in §11, not itself Ruled. |
| Failure on the final (threshold-clearing) roll | For first-time Creation of a Component/Item: **no item produced** (DEC-128 Q2) | DEC-128 Q2 |
| Failure on an Upgrade attempt | Tier+1, Magnitude+0 (imbalanced record; needs Repair) | DEC-128 Q3 |
| Repair | Skill Roll restores Magnitude up to Tier; separate from negative-record Tier-mutation | DEC-129, DEC-121 |

---

## 7. Quantity Tracking vs. Invariant 17 — Reconciliation

**Invariant 17:** *"No Universal Play subsystem may introduce a competing primary resource or progression economy."*

Quantity is **not** a resource pool:

| Property of a resource pool (PE/MP/HP) | Property of Material/Component quantity |
|---|---|
| Spent via Cost = natural roll (DEC-007) | Never spent via a roll — decremented only as a fixed recipe cost when a crafting attempt succeeds |
| Regenerates via Recovery (DEC-008) | Does not regenerate; only increases via acquisition or another crafting output |
| Drives Overflow → HP (DEC-007) | Has no Overflow interaction whatsoever |
| Is a single scalar per character | Is an arbitrary number of independent stacked records, each with its own Tier |

**Direct precedent:** DEC-078 (Encumbrance) already tracks a numeric quantity (carried load in kg) outside the Cost/Overflow/Recovery economy, and DEC-078 A5 explicitly confirms this is Invariant-17-safe ("static thresholds + Skill-side penalty only; no secondary capacity/weight pool"). Material/Component quantity is the same category of bookkeeping: an inventory count, not a second resource economy.

Recipe cost is therefore expressed as: *"Crafting subtype X at Tier Y consumes `N` units of Material/Component subtype Z (by quantity, decremented on success)."* This consumption is in addition to, and independent of, the crafting Skill Test's own ordinary PE/MP Cost = Roll (DEC-007) — two separate and non-competing deductions.

---

## 8. Upgrade Mechanic — REUSED unmodified (DEC-128 Q3)

Materials, Components, and Items all Upgrade identically:

- Requires a Skill-Tier at the acting Skill **equal to or greater than the record's current Tier**.
- **Success:** Tier +1, Magnitude +1 (stays base-equal, `Z = Y`).
- **Failure:** Tier +1, Magnitude +0 → `Item Tier Y, Magnitude Y−1` (imbalanced; requires Repair per DEC-129 before further Upgrade is practical, per Tiwa's original DEC-128 rationale).

No new Upgrade mechanic is proposed; this section exists only to confirm the reuse is type-agnostic across Material/Component/Item.

---

## 9. Recipes — PROPOSED, content-authoring only

A **recipe** defines, per crafted `subtype` at a given target Tier: the required input `subtype`s and `quantity`s (Materials and/or Components), and optionally a required tool/facility (see §11 item 6).

Per the DEC-077.A precedent (creature/content authoring is the designer's own work, not system-authored), **recipes are not derivable from a universal formula** — they are authored content, per item, at Tiwa's discretion. This proposal supplies the *record shape* recipes populate, not the recipes themselves:

```
Recipe:
  output_subtype   : string
  output_type      : Component | Item
  output_tier      : Y
  inputs           : list<{subtype, quantity, type: Material|Component}>
  crafting_skill   : string
  min_skill_tier   : integer   (gate, mirrors DEC-041 discipline)
  tool_required    : optional  (§11 item 6 — not resolved)
```

---

## 10. Worked Example (Option A Tier formula)

**Goal:** Craft a Tier-3 Longsword. Crafting Skill: *Blacksmithing*, Skill-Tier 3, current value 45/Cap 60.

| Step | Action | Record before | Result |
|---|---|---|---|
| 1 | Start with Iron Ore | `type: Material, subtype: iron_ore, Tier 1, Mag 1, qty 3` | — |
| 2 | Upgrade one Iron Ore stack (success) | Iron Ore Tier 1 | → `Tier 2, Mag 2, qty 3` |
| 3 | Craft Component "Steel Ingot" from 3× Iron Ore (Extended Test, threshold cleared) | consumes 3× Iron Ore (Tier 2) | New record: `type: Component, subtype: steel_ingot, Tier = min(3, 2) = 2, Mag 2, qty 1` |
| 4 | Upgrade the Steel Ingot (success; gate: Skill-Tier 3 ≥ current Tier 2, satisfied) | Steel Ingot Tier 2 | → `Tier 3, Mag 3, qty 1` |
| 5 | Craft Item "Longsword" from 2× Steel Ingot (Tier 3) via Extended Test | consumes 2× Steel Ingot (Tier 3) | New record: `type: Item, subtype: longsword, Tier = min(3, 3) = 3, Mag 3, qty 1` |
| 6 | Apply Tags | — | `slot:main_hand, damage:slashing, offense:melee, handling:light, state:held` (DEC-080) |

The finished Longsword is a normal Item-family record from this point forward: it takes damage via the ordinary Equipment Damage/Sunder Condition-type record (DEC-118/119), independent of its own Tier 3/Magnitude 3.

---

## 11. Open Questions for Tiwa's Ruling

1. **Tier-determination formula (§5):** Option A, B, or C — or a different formula entirely.
2. **Completion-threshold scaling (§6):** whether to lock a formula (`threshold = Tier × k`) or leave it pure GM discretion as DEC-070 already allows.
3. **Material acquisition:** does gathering/buying a Material require a Skill Test of its own, and does its cost interface with the still-open EQ-3A wealth/economy fork (DEC-081.A Open 3)? Not resolved here.
4. **Recipe authorship cadence:** confirm recipes are pure content-authoring (DEC-077.A) with no universal input-count formula, as assumed in §9.
5. **Tool/facility requirements:** whether crafting above a certain Tier requires a specific location/tool (forge, workbench) is untouched by any existing DEC and fully open.
6. **Component-as-standalone-Item default (§3):** this document defaults to "permitted" — confirm or override.

---

## 12. Required OpenCode Actions (if and when Tiwa rules on this)

1. Assign DEC number(s) to whichever formula/threshold options are selected from §11.
2. Record the ruling(s) in the Decision Register under a new Equipment-subsystem heading, cross-referenced to DEC-081.A (Open 3) and DEC-128/129.
3. Update Proposals/WIP §13 (Equipment, currently Reserved) to reflect the new Crafting sub-scope.
4. Do **not** mark any part of this document Canonical — none of it has passed the 8-step Promotion Rule.

---

## 13. Reconfirmation Checklist for Tiwa

- [ ] Tier-determination formula selected (§5, item 1 above)
- [ ] Completion-threshold policy selected (§11 item 2)
- [ ] Material acquisition scope decided or explicitly deferred (§11 item 3)
- [ ] Recipe-authorship assumption confirmed (§11 item 4)
- [ ] Tool/facility requirement scoped or explicitly deferred (§11 item 5)
- [ ] Component-as-standalone default confirmed or overridden (§11 item 6)
