---
document:
  title: "Tiwas — Session Report v2: Expanded Wurm Online Crafting Adaptation & Formal Rule Recommendations"
  version: "v2.0"
  status: "Advisory / Non-canonical. Session report only. No DEC assigned or inferred. Extends and partially supersedes the v1 session report's item catalog (§6) and tension notes (§7); v1's framework mapping (§§2-5) is unchanged and referenced, not repeated."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
supersedes: "tiwas-wurm-online-crafting-adaptation-session-report-2026-09-17.md — §6 (ten items) is extended to twenty-six; §7 (flagged tensions) is elevated into two formal candidate recommendations (§§4-5 below). §§0-5 of v1 are otherwise unchanged and not restated here."
---

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-17
**Classification:** Advisory / Non-canonical session report for OpenCode. No DEC assigned; two formal candidate recommendations proposed for Tiwa's ruling (§§4-5), neither adopted.

---

# Tiwas — Session Report v2: Expanded Wurm Crafting Adaptation

## 0. Governance Statement

- Assigns **no DEC number**. §§4-5 below are **candidate amendment requests**, formally written so Tiwa can rule on them directly — they are not adopted anywhere in this document's own item catalog (§6), which continues to follow the Ruled DEC-128 Q2/Q3 behavior unmodified.
- This document extends, and for §6/§7 supersedes, the v1 session report. v1's §§0-5 (governance, deliverables overview, research log, findings summary, mapping table, time/action resolution) remain valid and are not repeated.

---

## 1. What Changed From v1

| v1 element | Status in v2 |
|---|---|
| §6 — Ten items | Extended to twenty-six (§6 below); the original ten are unchanged, renumbered 1–10 for continuity |
| §7 — Two flagged tensions | Elevated into formal, mechanically-specified candidate recommendations (§§4-5 below), each addressed to a named DEC |
| §§0-5 (framework, research log, findings, mapping, time/action resolution) | Unchanged — see v1 |

---

## 2. Additional Research Process

| Step | Query | What it established |
|---|---|---|
| 5 | Wurm Online blacksmithing/weapon-smithing crafting steps | Confirmed the Smithing skill family's structure (Weapon, Armour, Chain Armour, Plate Armour, Shield, Blacksmithing, Locksmithing, Metallurgy, Jewelry Smithing as named sub-skills); confirmed a forge (not just an anvil) is required for melting ore and higher-tier work; confirmed tool heads (e.g. small axe heads) are crafted separately and then assembled onto a shaft |
| 6 | Wurm Online leatherworking/tailoring crafting steps | Confirmed the tanning chain (hide + lye → leather); confirmed the studded-leather conversion (leather item + iron rivets via needle); and — directly relevant to §4 below — confirmed explicitly that **a failed studded-leather creation attempt damages the item being worked and consumes part of the rivets**, a concrete real example of failure having a partial, non-binary cost |
| 7 | Wurm Online masonry/pottery crafting steps | Confirmed stone bricks are chiseled from stone shards with a stone chisel, output quality capped by the shard's own quality (further Option-A validation, §4 of v1); confirmed pottery bricks require firing in a campfire/kiln/forge (reinforcing the `fire_starting_kit`/`kindling` dependency already in the primitive catalog); confirmed mortar is a masonry binder that itself decays over real time if not used or stored — a decay/spoilage mechanic not previously surfaced in this research |

---

## 3. Additional Wurm Findings Summary

| Finding | Detail |
|---|---|
| Smithing sub-skill structure | Weapon, Armour, Chain Armour, Plate Armour, Shield, Blacksmithing, Locksmithing, Metallurgy, and Jewelry Smithing are distinct named sub-skills under one Smithing family |
| Tool-head-then-assembly pattern | Metal tools follow the same two-stage pattern as the primitive catalog's wood tools: a head/blade is forged separately, then assembled onto a separately-made shaft |
| Failure with partial cost | Studded leather creation: on failure, the jacket takes damage **and** 0.05 kg of rivets is consumed — failure is not always a clean binary of "nothing happens" vs. "item exists" |
| Improvement asymmetry | Leatherworking's improve step is explicitly **not** capped by the quality of the raw leather used to improve it — an exception to the general material-caps-output rule found elsewhere, worth noting rather than assuming universal |
| Material decay/spoilage | Clay and mortar both lose usability over real time if left unstored — a mechanic distinct from both QL and from combat damage, not previously surfaced |

---

## 4. Recommendation A — Partial-Failure Byproduct Rule

**Addressed to:** DEC-128 Q2 ("failed Creation produces no item").

**Wurm grounding:** A failed woodworking attempt can yield a byproduct (woodscrap) instead of nothing; a failed studded-leather attempt damages the work-in-progress and consumes part of the rivets rather than destroying nothing or everything.

**Candidate mechanic (PROPOSED, not adopted):**

1. **Material commitment timing.** Materials/Components listed in a Recipe (§9 of the parent proposal) are consumed **once, at the start of the Extended Test**, not per interval and not only on final success — this matches Wurm's "retry on the same log" behavior and needs its own explicit ruling, since the parent proposal did not specify this.
2. **On a failed final (threshold-clearing) interval:** instead of DEC-128 Q2's flat "no item," the committed inputs partially convert into a **byproduct record** — a Material/Component of the same `type` family, one Tier lower than the intended output (or a fixed `scrap` subtype where no lower Tier exists), at `quantity` reduced proportionally to how close the Extended Test's accumulated Margin came to the completion threshold. A near-miss yields more byproduct than an early failure.
3. **Formula candidate:** `Byproduct Quantity = floor(Input Quantity × (Accumulated Margin / Completion Threshold))`, clamped to a minimum of 0.

**Why this is a recommendation and not an amendment:** it directly changes the outcome of a Ruled decision (DEC-128 Q2). It is written up here in full mechanical detail specifically so it can be taken to Tiwa as a standalone ruling request, per the Promotion Rule discipline — it is not exercised anywhere in §6's item table below.

---

## 5. Recommendation B — Diminishing-Returns Upgrade Ceiling

**Addressed to:** a proposed refinement layered on top of, not replacing, DEC-128 Q3 ("failed Upgrade → Tier+1, Magnitude+0").

**Wurm grounding:** the imp mechanic's success chance and quality gain both diminish as an item's QL approaches a skill-based asymptotic ceiling — the closer you push to your own skill's limit, the harder each further gain becomes.

**Candidate mechanic (PROPOSED, not adopted):**

1. DEC-128 Q3's outcome table is **preserved exactly as Ruled** — success is still Tier+1/Magnitude+1, failure is still Tier+1/Magnitude+0. This recommendation only proposes adjusting the **difficulty of the Upgrade roll itself**, using the already-Ruled Skill-side-penalty idiom (DEC-063/064), not a new outcome shape.
2. **Formula candidate:** when attempting to Upgrade a record whose current Item Tier is already within `c` of the crafter's Skill-Tier, apply a Skill-side penalty to the Upgrade roll: `Penalty = k × max(0, Item Tier − (Skill-Tier − c))`, with `k` and `c` as GM/content-authored constants (DEC-077.A precedent). Upgrades well below the crafter's Skill-Tier ceiling are unaffected; only the last few steps toward that ceiling get harder, mirroring Wurm's asymptote without inventing a new roll type.
3. This does **not** touch Cost, Overflow, Failure XP, or the natural roll (Invariants 6/7/8 preserved) — it only modifies effective Skill for this one roll type, exactly as DEC-063/064 already do for difficulty grades generally.

**Why this is a recommendation and not an amendment:** DEC-128 Q3's outcome table is untouched, but the roll-difficulty layer this proposes has never itself been Ruled for Upgrade attempts specifically, so it needs its own sign-off before use.

---

## 6. Expanded Item Catalog (26 items)

Items 1–10 are unchanged from v1, recapped compactly; items 11–26 are new this session.

| # | Wurm item | Wurm crafting step (paraphrased) | Tiwas `type` | Inputs | Tool required | Crafting Skill |
|---|---|---|---:|---|---|---|
| 1 | Crude Knife | Rock shard + iron-bearing rock, by hand | Item | Material `rock_shard` + Material `iron_rock` | none | Improvisation/Survival |
| 2 | Shaft | Carving knife on a log | Component | Material `log` | `crude_knife` | Woodcutting/Carpentry |
| 3 | Plank | Saw on a log | Component | Material `log` | Saw *(external, unlisted)* | Carpentry |
| 4 | Mallet | Carving knife shapes a shaft into a head, combined with a second shaft | Item | Component `shaft` ×2 | `crude_knife` | Carpentry |
| 5 | Small Anvil | Hot iron lumps combined, shaped with a mallet | Item | Material `iron_lump` ×2 | `mallet` + fire (`kindling`) | Blacksmithing |
| 6 | Small Nail | Iron lump worked on an anvil | Component | Material `iron_lump` | `small_anvil` | Blacksmithing |
| 7 | Large Nail | Iron lump worked on an anvil, more material | Component | Material `iron_lump` ×2 | `small_anvil` | Blacksmithing |
| 8 | Rope Tool | Shaft/plank shaped by hand | Item | Component `shaft` or `plank` | `crude_knife` | Carpentry |
| 9 | Rope | Rope tool on plant fiber; output QL capped at fiber's QL | Item | Material `plant_fiber` | `rope_tool` | Ropemaking |
| 10 | Kindling | Crude knife on woodscrap | Component | Material `woodscrap` | `crude_knife` | Woodcutting/Survival |
| 11 | Small Axe Head | Iron lump forged on anvil, in Weapon/Heads Smithing | Component | Material `iron_lump` | `small_anvil` + fire | Weapon Smithing |
| 12 | Small Axe | Axe head assembled onto a shaft | Item | Component `small_axe_head` + Component `shaft` | none extra | Weapon Smithing |
| 13 | Knife Blade | Iron lump forged into a blade | Component | Material `iron_lump` | `small_anvil` + fire | Blade Smithing |
| 14 | Carving Knife | Blade assembled onto a shaft — the iron-tier successor to the Crude Knife | Item | Component `knife_blade` + Component `shaft` | none extra | Blade Smithing/Carpentry |
| 15 | Stone Chisel | Iron blade + shaft handle, blacksmithed *(construction detail not researched this session — flagged, not invented)* | Item | Material `iron_lump` + Component `shaft` | `small_anvil` + fire | Blacksmithing |
| 16 | Stone Brick | Stone chisel used on a stone shard; brick QL capped by shard QL | Component | Material `stone_shard` | `stone_chisel` | Masonry/Stone Cutting |
| 17 | Mortar | Sand + lime, mixed with water by hand; **decays over time if unstored** (§3) | Component | Material `sand` + Material `lime` + Material `water` | none | Masonry |
| 18 | Pottery Brick | Clay brick, then fired in a campfire/kiln/forge | Item | Material `clay` | `fire_starting_kit` (or forge) | Pottery |
| 19 | Clay Bowl | Clay shaped directly by hand — simplest pottery item, no tool | Item | Material `clay` | none | Pottery |
| 20 | Lye | Ash + water, mixed by hand — the tanning agent | Component | Material `ash` + Material `water` | none | Leatherworking |
| 21 | Leather | Animal hide tanned with lye | Component | Material `hide_rawhide` + Component `lye` | none extra | Leatherworking (Tanning) |
| 22 | Leather Glove | Leather sewn with a needle/awl | Item | Component `leather` | `bone_awl` | Leatherworking |
| 23 | Rivets | Iron lump forged small, used to stud leather armor | Component | Material `iron_lump` | `small_anvil` + fire | Blacksmithing |
| 24 | Studded Leather Jacket | Leather jacket studded with rivets; **failure damages the jacket and consumes rivets** — real grounding for §4 | Item | Component `leather` ×N + Component `rivets` | `bone_awl` (needle-equivalent) | Leatherworking |
| 25 | String of Cloth | Cotton spun on a wooden spindle | Component | Material `cotton_boll` | Wooden spindle *(external, unlisted)* | Cloth Tailoring |
| 26 | Cloth Glove | String of cloth woven on a floor loom into a square, then sewn — the deliberate **cotton ceiling** item from the original brief, now shown as a full worked chain | Item | Component `string_of_cloth` ×N | Floor loom *(external, unlisted)* + `bone_awl` | Cloth Tailoring |

**Continuity notes:** items 10 and 18 both terminate in the same fire dependency already established by the primitive catalog's `fire_starting_kit`; item 20 reuses the primitive catalog's `ash` Material subtype directly; item 9's `plant_fiber` and item 25's `cotton_boll` are the same two Materials the original brief used to bound the "no more complicated than cotton" ceiling — item 26 is that ceiling's full worked example.

---

## 7. Updated Dependency Chain

```
crude_knife (bootstrap; no tool) ──┬─▶ shaft ──┬─▶ mallet ──▶ small_anvil ──┬─▶ small_nail
                                    │           │  (+ fire, via kindling)   ├─▶ large_nail
                                    │           └─▶ rope_tool ──▶ rope      ├─▶ small_axe_head ──▶ small_axe (+ shaft)
                                    ├─▶ kindling ──▶ fire ──▶ pottery_brick ├─▶ knife_blade ──▶ carving_knife (+ shaft)
                                    │                                       ├─▶ stone_chisel (+ shaft) ──▶ stone_brick
                                    └─▶ (plank via Saw, external)           └─▶ rivets

hide_rawhide ──▶ leather (+ lye [ash+water]) ──┬─▶ leather_glove
                                                 └─▶ studded_leather_jacket (+ rivets)

cotton_boll ──▶ string_of_cloth (+ spindle, external) ──▶ cloth_glove (+ loom, external)

clay ──▶ clay_bowl (no tool)
sand + lime + water ──▶ mortar
```

Every branch still traces back to either the `crude_knife`/`hammerstone` bootstrap pair or a directly-gathered Material, preserving the self-bootstrapping property required by the original brief.

---

## 8. Consolidated Open Questions (all four documents)

Carried forward from v1 §9, plus new items from this session:

1–8. *(unchanged from v1 — Tier formula confirmation, threshold/tool-discount formula, material-acquisition/EQ-3A dependency, recipe-authorship confirmation, tool/facility requirements, Component-as-standalone default, `self_bow`/fired-pottery Tier placement.)*
9. **New:** Recommendation A (§4) and Recommendation B (§5) — both need an explicit ruling before either is usable; neither is assumed anywhere in §6's table.
10. **New:** whether material/component **decay over time** (mortar, clay — §3) should become its own Tiwas mechanic at all, given Tiwas has no real-time clock; flagged as a possible third recommendation candidate but **not drafted** this session — noted only so it isn't silently dropped.
11. **New:** leatherworking's improve-not-capped-by-raw-material-QL exception (§3) — worth confirming whether the parent proposal's Tier formula (§5 of the base proposal) should carry a per-Skill exception list, or whether this is Wurm-specific idiosyncrasy not worth porting.

---

## 9. Complete Session Deliverables — Updated Recap

| Document | Status |
|---|---|
| `tiwas-crafting-system-proposal-v0.1-2026-09-12.md` | Non-canonical proposal, pending review |
| `tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md` | Advisory example content, pending authorship review |
| `tiwas-wurm-online-crafting-adaptation-session-report-2026-09-17.md` (v1) | Advisory session report; §6/§7 superseded by this document |
| **This document (v2)** | Advisory session report; adds 16 items and two formal candidate recommendations |

---

## 10. Required OpenCode Actions

1. File this document alongside v1 under `investigations/`, marked as v1's successor for §6/§7 specifically (not a full replacement — v1's §§0-5 remain the reference copy).
2. Route Recommendation A (§4) and Recommendation B (§5) to Tiwa as explicit, separately-rulable items — do not bundle either into a general "crafting proposal accepted" decision if one is ever made.
3. Assign no DEC to anything in this document.

---

## 11. Sources (this session's additions)

- https://www.wurmpedia.com/index.php/Blades_smithing
- https://www.wurmpedia.com/index.php/Weapon_smithing
- https://www.wurmpedia.com/index.php/Blacksmithing
- https://www.wurmpedia.com/index.php/Smithing
- https://www.wurmpedia.com/index.php/Guides:Smithing_Skill_Tips
- https://www.wurmpedia.com/index.php/Guides:Blacksmithing_and_subskills_guide_for_the_resource_conscious
- https://www.wurmpedia.com/index.php/Studded_leather_jacket
- https://www.wurmpedia.com/index.php/Tailoring
- https://www.wurmpedia.com/index.php/Leatherworking
- https://wurm.wiki.gg/wiki/Leatherworking_skill
- https://www.wurmpedia.com/index.php/Leatherworking_Skill_Tips
- https://www.wurmpedia.com/index.php/Guides:Tips_for_Skills
- https://wurmpedia.fandom.com/wiki/Clay
- https://www.wurmpedia.com/index.php/Pottery_brick_wall
- https://www.wurmpedia.com/index.php/Stone_brick
- https://www.wurmpedia.com/index.php/Masonry
- https://www.wurmpedia.com/index.php/Mortar
- https://www.wurmpedia.com/index.php/Pottery_brick

(v1's source list, §11 of that document, remains valid for items 1–10.)

---

## 12. Reconfirmation Checklist for Tiwa

- [ ] Recommendation A (Partial-Failure Byproduct Rule, §4) — accept, reject, or request revision
- [ ] Recommendation B (Diminishing-Returns Upgrade Ceiling, §5) — accept, reject, or request revision
- [ ] Material commitment timing (§4 item 1) — this is a genuine gap in the base proposal regardless of whether Recommendation A itself is accepted, and needs its own answer either way
- [ ] Items 11–26 (§6) reviewed for authorship/content-blessing per DEC-077.A
- [ ] Decay/spoilage-over-time question (§8 item 10) — confirm out of scope, or request a drafted recommendation
- [ ] All v1 checklist items (still open — see v1 §12)

---

**End of session report v2.**

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-17
