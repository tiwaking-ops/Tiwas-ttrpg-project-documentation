---
document:
  title: "Wurm Online Crafting System — Comprehensive Adaptation for Tiwas TTRPG"
  version: "v0.1"
  status: "Advisory / Non-canonical. No DEC assigned. Example/candidate content pending Tiwa's review under the DEC-077.A content-authoring precedent. Does not rule, promote, or lock anything."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-14"
  research_source: "Wurmpedia (wurmpedia.com), retrieved via web search/fetch, 2026-09-14"
---

# Wurm Online Crafting System — Comprehensive Adaptation for Tiwas TTRPG

## 0. Document Status and Governance Notice

**This is advisory design content, not a ruling.** Per standing Tiwas governance
(`governance/status-model.md`, `governance/authority.md`), Claude presents options and
drafts content; only Tiwa rules, and only OpenCode records a ruling as a numbered DEC.
Nothing in this document is Canonical. No DEC is assigned or implied by any table,
formula, or item entry below.

This document **builds on, and must be read alongside**, the existing non-canonical
Tiwas crafting groundwork already on record:

- **DEC-081 / DEC-081.A** — Equipment state model (Conditions + Tags represent negative
  item state; no independent state-tracker for *damage*).
- **DEC-128 (Q1)** — Items carry an independent **Item Tier / Item Magnitude** record
  (`Item Tier Y`, `Item Magnitude Y`, base-equal at creation, `Z = Y` — **not** the
  `Z = −Y` unified StateRecord schema of DEC-115/117). Item Creation is ruled to be an
  **Extended Test** (DEC-067/068/070 margin-accumulation machinery). Failed Upgrade →
  `Item Tier Y, Magnitude Y−1` (imbalanced; needs Repair).
- **DEC-129** — Item Magnitude is repairable up to (never above) Item Tier via a Repair
  Skill Roll.
- **DEC-118/119/120/121** — Damage does not ablate Item Magnitude; damage is a separate
  negative StateRecord (`state:unusable`, `state:sundered`); Repair reduces that record's
  Tier via the Heal Effect System (DEC-121/DEC-127).
- **DEC-080/DEC-114** — Tags ontology (`slot:`, `damage:`, `handling:`, `state:`, etc.).
- The stored advisory documents `tiwas-crafting-system-proposal-v0.1-2026-09-12.md` (a
  Materials → Components → Items pipeline sketch) and
  `tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md` (a worked Tier-1 example
  catalog). **This document supersedes neither** — it is a parallel, much larger worked
  example set specifically sourced from Wurm Online, built on the same unruled
  foundations. Every unruled dependency those documents carry (the Tier-determination
  formula options A/B/C, the Item-family record's exact placement, tool/facility
  requirements, material acquisition/economy) is **inherited here unresolved**, not
  re-decided.
- **EQ-3A (wealth/economy)** remains open (see `tiwas-equipment-subsystem-dec081a-open3-options-brief-2026-09-10.md`). Any priced/traded-goods framing below is flavor only.

**No construction/action-time values are adapted.** Tiwas has no ruled Time/Action
duration system (G3 remains open per DEC-133/DEC-138). Where Wurm's source material
specifies real-world action timers (e.g., "10-20 minutes to heat a forge"), this
document notes the figure for historical/flavor reference only and explicitly does
**not** convert it into any Tiwas mechanic, duration, or Extended-Test interval count.

---

## 1. Executive Summary

Wurm Online is a crafting-first sandbox MMO whose entire economy rests on three ideas
that map unusually cleanly onto Tiwas's already-ruled architecture:

1. **Quality Level (QL)** — a single 1–100 number describing how good a raw material,
   component, or finished item is. This maps directly onto Tiwas's existing
   **Item Tier / Item Magnitude** record (DEC-128 Q1) and, for non-item materials, onto a
   parallel **Material Tier / Material Magnitude** record using the identical shape.
2. **Skill-gated creation and improvement** — your skill determines what you can
   attempt and how high you can push an item's quality; success is a probability
   function of skill vs. material/tool quality vs. difficulty. This maps onto Tiwas's
   already-ruled Core Test Transaction (DEC-006), Extended Test Item Creation
   (DEC-128 Q2), and Repair-to-Tier (DEC-129) — **no new resolution engine is needed.**
3. **A strict material → component → item hierarchy**, where raw resources (ore, logs,
   shards, hides, fiber) are refined into intermediate components (lumps, planks,
   leather, cloth squares, blades, shafts), which are then combined into finished items.
   This is **exactly** the Materials → Components → Items pipeline already sketched in
   the stored (unruled) Tiwas crafting proposal — this document is that pipeline filled
   in with Wurm's real, extensively-tested content.

Wurm additionally contributes three mechanics **not yet present anywhere in the Tiwas
corpus**, flagged in §9 as new open questions requiring Tiwa's ruling before they can be
used at the table:

- **Material-type modifiers** (a weapon's wood or metal type grants small mechanical
  bonuses/penalties, e.g., oak tools take less use-damage; adamantine deals more damage).
- **The Rarity system** (Rare / Supreme / Fantastic items, an independent quality axis
  layered on top of QL).
- **Alloying** (combining two base materials in a fixed ratio to produce a superior
  derived material — Tiwas has no ruled multi-input Component-combination formula yet).

Everything else below is directly expressible using **already-ruled** Tiwas mechanics
and requires no new rule, only new **content** (which is exactly what DEC-077.A
authorizes advisory models to draft).

---

## 2. Mapping Framework — Wurm Mechanic → Tiwas Mechanic

| Wurm Online concept | Tiwas equivalent | Ruling(s) reused |
|---|---|---|
| Quality Level (QL), 1–100 | **Item/Material Tier** (coarse) + **Item/Material Magnitude** (fine), `Magnitude ≤ Tier` | DEC-128 Q1, DEC-129 |
| Damage (item wear, 0–100%) | **Negative StateRecord** (`state:unusable`, equipment-damage record) — does **not** touch Magnitude | DEC-118, DEC-119 |
| Effective QL = QL × (100−damage)/100 | Effective Item Magnitude while a negative StateRecord Tier is active — **exact interaction not yet ruled**; see Open Question OQ-7 | — (open) |
| Creating an item | **Extended Test** (Margin-accumulation, DEC-067; neutral failure, DEC-068; GM-set completion target, DEC-070; per DEC-128 Q2) | DEC-067/068/070/128 |
| Failed creation | No item produced (ordinary Core Test consequences still apply: Cost, Overflow, Failure XP) | DEC-128 Q2 |
| Improving an item ("imping") | **Upgrade** (raises Item Tier, requires Skill-Tier ≥ current Item Tier) or **Repair** (restores Magnitude toward Tier / reduces a negative StateRecord's Tier) | DEC-128 Q3, DEC-129, DEC-121/127 |
| Failed Improve/Upgrade | Item Tier +1, Magnitude **unchanged** → `Tier Y, Magnitude Y−1` (imbalanced; item is "damaged" and needs Repair before further Upgrade) | DEC-128 Q3 |
| "Sweet spot" improving (imping above your skill for bonus skill gain) | **Out of scope** — Tiwas has no player-facing skill-gain-rate tuning mechanic; this is a Wurm meta-game convention, not adapted | flagged, not adapted |
| Creation/improve success chance (skill vs. material/tool QL vs. difficulty) | Ordinary **Core Test** roll-under (DEC-001/006); "difficulty" = Skill-side modifier grade (DEC-063) | DEC-001, DEC-006, DEC-063 |
| Skill "hard limits" (cannot attempt above a skill threshold regardless of tools) | **Skill-Tier gate** — an item's **minimum Skill-Tier to attempt** (mirrors DEC-041's Skill-Tier ≥ 2 gate pattern for location-referencing Effects, generalized to crafting) | pattern reuse of DEC-041; new application, flagged OQ-1 |
| Tools (hammer, chisel, needle, awl, file, whetstone…) | Tagged Items (`slot:` / new `tool:` namespace) required as a Component-consuming-test precondition — consumed *never*, only required present | DEC-080 T1 (extensible namespace) |
| Material type bonuses (oak, adamantine, etc.) | **Not yet ruled** — proposed as optional per-Material Tag with a declared mechanical clause (Conditional-Trait-Binding-style, DEC-088 pattern) | flagged OQ-2 |
| Alloying (2 materials → 1 superior material, fixed ratio) | **Not yet ruled** — proposed as a Component-combination recipe: `Input A (qty) + Input B (qty) → Output (qty)`, output Tier bounded by the lesser input per the crafting proposal's unruled Tier-formula Options A/B/C | flagged OQ-3 |
| Rarity (Rare/Supreme/Fantastic) | **Not yet ruled** — proposed as an optional bonus StateRecord layered on an Item/Material record | flagged OQ-4 |
| Real-world action timers | **Not adapted.** No Tiwas Time/Action duration system exists (G3 open, DEC-133/138). | not adapted, by instruction |

---

## 3. Tier-0 Raw Materials

Raw materials are gathered (not crafted) via a gathering Skill Test (Woodcutting →
Carpentry lineage; Mining → Blacksmithing/Masonry lineage; Butchering → Leatherworking
lineage; Farming/Foraging → Cloth Tailoring lineage). Per the unruled crafting
proposal's convention, a raw material's **Item Tier/Magnitude is set at the moment of
gathering**, bounded by the gathering Skill's Skill-Tier and the quality of the
gathering tool (mirrors Wurm's "your skill and your tool's QL bound the resource's QL"
rule, and is directly expressible via the already-ruled `min(Skill-Tier, ...)` pattern
family from DEC-107/DEC-128).

### 3.1 Wood

Source (Wurmpedia): logs are produced by felling and chopping trees; the wood **type**
of the last wooden component attached to a carpentry item determines the finished
item's wood type; type grants small passive mechanical bonuses.

| Wood Type | Source Tree | Wurm's Passive Property (reference only) | Proposed Tiwas Tag (advisory, unruled — OQ-2) |
|---|---|---|---|
| Oak | Oak tree (slow-growing, rare, kills nearby trees) | Tools take 20% less use-damage; arrows take less damage; +25% bash resilience | `material:oak` — reduced equipment-damage-record accrual rate |
| Pine | Pine tree (abundant, fast-growing) | No special property; baseline wood | `material:pine` — baseline, no clause |
| Fir | Fir tree | No known special property | `material:fir` — baseline |
| Birch | Birch tree (fast-growing, abundant) | Burns well; good for structures | `material:birch` — baseline (structure-flavor only) |
| Cedar | Cedar tree | Containers decay slower; arrows easier to improve, reduced shot difficulty | `material:cedar` — slower decay-record accrual for Component `Type=Container` |
| Maple | Maple tree | Arrows take less damage; usable for arrows | `material:maple` — baseline (ranged-ammo flavor) |
| Walnut | Walnut tree | Charcoal from walnut gives +10% quality to items it fuels | `material:walnut` — +1 step to a downstream Component's Tier at GM Fiat (rare) |
| Willow | Willow tree (rare, kills nearby trees) | Best for all bow types and fishing rods | `material:willow` — baseline (bow/rod flavor) |
| Apple / Cherry / Lemon / Orange / Olive | Fruit trees | Smaller log yield only; no combat property noted | `material:fruitwood` — baseline, cosmetic |
| Linden, Chestnut | Lumber trees | No known special property | baseline |

**Component derived from Wood:** *Log* (raw, gathered) → *Plank* (Carpentry Component,
via saw/hatchet processing) → *Shaft* (Fine Carpentry Component, for hafted
tools/weapons) → *finished wooden Item* (furniture, tool handles, ship parts, structural
components, bows).

### 3.2 Metal

Source (Wurmpedia — Metal lumps, Metallurgy): ore is mined, then smelted into a *lump*
of the base metal. Certain lumps can be **alloyed** — combined in a fixed ratio with a
second material — to produce a superior derived lump.

| Base Metal | Notes (reference only) |
|---|---|
| Iron | Baseline metal; no modifier (all other metals are described relative to Iron) |
| Copper | Bonus/penalty profile (weapon poison-wound property per Wurm's live data) |
| Silver | Used in Electrum alloy; jewelry-tier metal |
| Gold | Used in Electrum alloy; jewelry-tier metal |
| Tin | Alloying input for Bronze |
| Zinc | Alloying input for Brass |
| Lead | Soft, heavy; distinct bonus/penalty profile |
| Adamantine | Top-tier rare metal: bonus damage, bonus damage-reduction, bonus movement speed, high shatter/decay resistance (per live Wurm data) |
| Glimmersteel | Top-tier rare metal, parallel to Adamantine |
| Seryll | Rare jewelry-tier metal |

**Ruled Wurm alloy recipes** (reference only — see §9 OQ-3 for the Tiwas Component-
combination question these raise):

| Alloy | Recipe (Wurm, by weight) |
|---|---|
| Steel | 0.20 kg Iron lump + 0.20 kg Charcoal → 0.40 kg Steel lump |
| Brass | 1.00 kg Zinc lump + 0.15 kg Copper lump → 0.10 kg Brass lump |
| Bronze | 0.50 kg Tin lump + 0.15 kg Copper lump → 0.10 kg Bronze lump |
| Electrum | 0.10 kg Silver lump + 0.10 kg Gold lump → 0.10 kg Electrum lump |

Wurm's own documentation notes: *"Max quality is substantially affected by the quality
of the second component of each alloy"* — i.e., the **lesser/secondary input tends to
cap the output's achievable quality**, not a simple average. This is directly relevant
to the unruled Tier-determination fork already on record in the stored crafting
proposal (Options A/B/C) and is cited there as external precedent for **Option A**
(`min(Crafting Skill-Tier, max(input Tiers))`-style capping) over a floored-average
approach — but this document does not resolve that fork; it only notes the parallel.

**Component chain:** Ore (raw) → Lump (smelted Component) → **Alloy Lump** (optional,
combined Component) → **shaped part** (blade, head, fitting — Component) → finished
metal **Item** (weapon, armor piece, tool head, fastener, fixture).

### 3.3 Stone

Source (Wurmpedia — Mining, Shards, Slabs): mining/tunneling and quarrying yield
*shards* of a stone type; shards are combined into *bricks* (wall/paving material) or
*slabs* (flooring/decorative, higher grade).

| Stone Type | Primary Use (reference only) |
|---|---|
| Rock (generic stone) | Bricks for walls, crude tools; most abundant |
| Slate | Walls, roofs, paved floors/roads |
| Marble | Bricks, slabs, bridge keystones, decorative masonry |
| Sandstone | Bricks, slabs, walls, paving |
| Rock salt | Shard-yielding vein, same shard mechanics as rock |

**Component chain:** Vein (gathering site, not itself a material) → *Shards* (raw
Material, gathered) → *Brick* or *Slab* (Masonry/Stone-cutting Component) → finished
stone **Item** (wall, tower, statue, fountain, furniture, paving).

### 3.4 Leather, Hide, and Cloth

Source (Wurmpedia — Leatherworking, Cloth tailoring, Tailoring):

- **Hide** is obtained by butchering an animal. Hide is chemically treated with **lye**
  (0.10 kg lye per 3.00 kg hide) to produce **Leather**, the actual working Material.
  Leather is notable in Wurm for being **improvable without a Material-Tier ceiling from
  the leather itself** — i.e., improving a leather item is bounded by the crafter's
  skill and tool, not by the leather's own QL. This is a genuine mechanical asymmetry
  worth flagging (OQ-6) since Tiwas's ruled Repair-to-Tier model (DEC-129) generally
  assumes the *item's own* Tier is the ceiling.
- **Cloth** is produced from a fiber crop (cotton in Wurm) spun into thread ("string of
  cloth") on a spindle, then woven into a square of cloth on a loom.
- **Drake Hide** is a rare high-tier leather analog with superior armor properties,
  obtainable only from specific creatures — a natural Tiwas parallel to a
  creature-sourced premium Material (DEC-077.A creature-content precedent).

**Component chain (Leather):** Hide (raw, from Butchering) → Leather (Leatherworking
Component, via lye treatment) → cut/shaped **Leather Piece** → finished leather **Item**
(armor piece, belt, bag, saddle/tack).

**Component chain (Cloth):** Fiber crop (raw, from Farming) → String of Cloth
(Component, spun) → Square of Cloth (Component, woven) → finished cloth **Item**
(clothing, sails, padding/backing layers for other armor).

**Studding (composite items):** Wurm's leather armor can be reinforced with metal
**rivets**, consuming a metal Component *and* a leather Component in a single finishing
step to produce a higher-tier composite item ("studded leather"). This is a clean,
already-ruled-compatible example of a **two-Component-Type combination at the Item
stage** (a Metal Component consumed into a Leather-base Item) and is used as the worked
example in §6.3 below.

### 3.5 Clay and Fired Goods (Pottery)

Source (Wurmpedia, general knowledge): Clay is dug from clay tiles/deposits, shaped on
a pottery wheel into unfired vessels, then **fired** in a kiln to become a finished,
durable pottery Item. Firing is the pottery-specific analog of a metal item's
heat-and-hammer creation step — a **required intermediate processing stage**, not
optional, mirroring the mandatory Component stage already ruled for Tiwas crafting
generally (stored crafting proposal, "Component stage mandatory for Tier 1+").

**Component chain:** Clay (raw, dug) → Unfired vessel (Component, shaped) → **Fired
vessel** (finished pottery **Item**, via kiln).

---

## 4. Tier-1/2 Components (Intermediate, Cross-Category)

These Components are consumed by multiple downstream Item categories and are the
connective tissue of the whole tree — directly analogous to the "Tool" tier already
present in the stored Tier-1 primitive-item catalog (e.g., `hammerstone`).

| Component | Made From | Consumed By (examples) |
|---|---|---|
| Plank | Log (Carpentry) | Furniture, structures, ships, containers |
| Shaft | Log/Plank (Fine Carpentry) | Hafted tools, spears, arrows, hammers |
| Metal Lump | Ore (Blacksmithing, via smelting) | Every metal Item category |
| Nail / Large Nail | Metal Lump | Structures, furniture, ship hulls |
| Rivet | Metal Lump | Studded leather armor, reinforced containers |
| Blade (weapon-head form) | Metal Lump (Weaponsmithing) | Swords, axes, knives, polearm heads |
| Butchering Knife Blade | Metal Lump (Blacksmithing) | Butchering Knife (a very low-cost training/utility Item) |
| Stone Brick | Stone Shards (Masonry) | Walls, towers, bridges |
| Stone Slab | Stone Shards (Stone-cutting) | Flooring, high-grade paving, tables |
| Leather (treated) | Hide + Lye (Leatherworking) | All leather Items |
| String of Cloth | Fiber crop (Cloth Tailoring) | Cloth squares, sails, thread-consuming repairs |
| Square of Cloth | String of Cloth (Cloth Tailoring) | Clothing, sails, backing layers |
| Fired Clay Vessel | Clay, via kiln (Pottery) | Storage jars, cookware, decorative pottery |
| Whetstone | Stone (Stone-cutting) | Required **tool** for Blacksmithing improve actions |
| Needle / Awl | Metal Lump (Blacksmithing → tool) | Required **tools** for Leatherworking/Tailoring |
| File | Metal Lump | Required **tool** for Carpentry/Blacksmithing improve actions |
| Mallet / Hammer | Shaft + Metal Head, or all-wood | Required **tool** for most creation/improve actions across categories |
| Pelt | Hide (raw, untreated) | Required **tool-analog** for Carpentry/Blacksmithing polishing steps |

**Tooling note.** In Wurm, tools are not consumed by ordinary creation actions — they
are a **quality-and-success-chance precondition** that must be present and undamaged.
This maps cleanly onto the Tiwas Tag system: a tool Item carries a `tool:` Tag (new
namespace entry, non-numeric per DEC-116 unless a specific ruling grades it), and a
Crafting Extended Test **requires** the matching `tool:` Tag present in the actor's
possession as a precondition, exactly parallel to how `state:held`/`slot:main_hand`
gate Disarm and Equipment Damage today (DEC-114 R2). **This is new territory for the
Tags ontology and is flagged as OQ-5.**

---

## 5. Item Categories (Finished Goods)

Organized by consuming Skill family, mirroring Wurm's own skill tree. Each category
below is a **Type slot** in the unruled Item-family record (DEC-128 Q1), not an
exhaustive enumeration — Wurm alone lists over 1,500 distinct finished items on
Wurmpedia's item index, so this section defines the **category schema** plus a small
number of fully worked examples per category (§6), leaving the remainder to be
authored on the same template as needed (§7).

| Category | Source Skill Family | Representative Wurm Items |
|---|---|---|
| Edged/Blunt Weapons | Weaponsmithing (Blacksmithing subskill) | Sword, axe, mace, spear, dagger |
| Ranged Weapons | Bowyery (Carpentry subskill), Fletching | Bow, crossbow, arrow, bolt |
| Armor — Metal | Armoursmithing (Blacksmithing subskill) | Plate, chain, helm, gauntlet |
| Armor — Leather | Leatherworking | Leather cap, jacket, studded leather set |
| Armor — Cloth | Cloth tailoring | Padded coat, cloth glove |
| Hand Tools | Blacksmithing / Carpentry | Pickaxe, hatchet, saw, shovel, hammer |
| Containers | Carpentry / Pottery / Tailoring | Barrel, crate, chest, basket, jar, backpack |
| Furniture | Fine Carpentry | Table, chair, bed, shelf |
| Structures (static) | Masonry / Carpentry | Wall, door, bridge, tower, house frame |
| Jewelry | Jewelry Smithing | Ring, bracelet, amulet, brooch |
| Ships/Vehicles | Ship Building / Carpentry | Rowboat, sailboat, cart, wagon |
| Locks/Security | Locksmithing | Lock, key, padlock |
| Musical/Toys | Toymaking | Yoyo, instrument (flavor content) |

---

## 6. Worked Examples (Fully Specified Crafting Chains)

Each example gives: source Materials/Components, the finished Item's proposed
Type/Skill/Tag record, and how it plugs into the already-ruled Item Tier/Magnitude and
Extended-Test-Creation machinery. **All numeric Tiers below are illustrative content,
not rulings** — the underlying Tier-assignment formula is still one of the open,
unruled Options A/B/C from the stored crafting proposal (see §9 OQ-8).

### 6.1 Butchering Knife (low-Tier training item, mirrors Wurm's own "first weapon to skill on")

| Stage | Type | Inputs | Output |
|---|---|---|---|
| 1 | Material | Iron Ore (mined) | Iron Lump |
| 2 | Component | Iron Lump (Blacksmithing) | Butchering Knife Blade |
| 3 | Component | Log (Carpentry) | Wooden Handle |
| 4 | Item | Butchering Knife Blade + Wooden Handle (Weaponsmithing) | **Butchering Knife** — `Item Tier = min(Skill-Tier, max(input Tiers))`; Tags: `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light` |

Consistent with Wurm's own design intent (a resource-cheap early item used to bootstrap
the Weaponsmithing skill), this is proposed as the **canonical Tiwas onboarding weapon
recipe** alongside the existing `hammerstone` tool-less root from the Tier-1 primitive
catalog.

### 6.2 Steel Longsword (mid-Tier alloy weapon)

| Stage | Type | Inputs | Output |
|---|---|---|---|
| 1 | Material | Iron Ore (mined) | Iron Lump |
| 2 | Material | Wood (any; charcoal-burned) | Charcoal |
| 3 | Component (**alloy combination**, OQ-3) | Iron Lump + Charcoal | Steel Lump |
| 4 | Component | Steel Lump (Weaponsmithing) | Sword Blade |
| 5 | Component | Log (Fine Carpentry) | Sword Hilt/Grip |
| 6 | Item | Sword Blade + Hilt (Weaponsmithing) | **Steel Longsword** — Tags: `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light`; the `material:steel` Tag (OQ-2) optionally grants a minor mechanical clause once OQ-2 is ruled |

### 6.3 Studded Leather Jacket (composite two-Material-Type item)

| Stage | Type | Inputs | Output |
|---|---|---|---|
| 1 | Material | Butchered Hide | Leather (via lye) |
| 2 | Component | Leather (Leatherworking) | Leather Jacket (base Item) |
| 3 | Material | Iron Lump | Rivets (Component) |
| 4 | Item (finishing/combination step) | Leather Jacket + Rivets (Leatherworking) | **Studded Leather Jacket** — Item Tier steps up one increment from the base Jacket per the studding convention; Tags gain `defense:armor` at increased Magnitude ceiling |

This is the primary worked example for **multi-Material-Type Item combination** (a
Metal Component consumed into a Leather-base Item), directly answering one of the
crafting proposal's open questions about whether Components must share a single
Material Type — Wurm's own precedent says **no**, composite items freely mix Component
Types, and the record shape (DEC-128 Q1) does not forbid it.

### 6.4 Fired Clay Storage Jar (Pottery, required-firing-stage example)

| Stage | Type | Inputs | Output |
|---|---|---|---|
| 1 | Material | Dug Clay | Clay (Component-ready) |
| 2 | Component | Clay (Pottery, shaped) | Unfired Jar |
| 3 | Item (mandatory processing step, kiln) | Unfired Jar (Pottery) | **Fired Clay Jar** — Tags: `slot:none` (freestanding container), `state:worn`/`state:held` not applicable; functions as a Location/Item container record |

---

## 7. Expandability Template (for authoring future entries)

To keep this catalog open-ended without requiring a new rule each time, every future
Material, Component, or Item entry should be authored using this fixed field set —
identical in spirit to the unified StateRecord schema's discipline (DEC-115/117) but
scoped to the **separate, DEC-128-Q1 Item-family record** (outside that schema, per
DEC-128's own placement ruling):

| Field | Description |
|---|---|
| `name` | Display name |
| `record_type` | `Material` \| `Component` \| `Item` |
| `source_skill` | The Tiwas Crafting Skill (see §8) that creates/gathers it |
| `min_skill_tier` | Minimum Skill-Tier required to attempt (mirrors DEC-041's gate pattern; OQ-1) |
| `inputs` | List of `{name, record_type, quantity}` consumed |
| `item_tier_formula` | One of the three unruled candidate formulas (Option A/B/C, §9 OQ-8) — record which one was used for this entry so it can be bulk-revised once Tiwa rules |
| `tags` | List of DEC-080-namespace Tags this record carries |
| `material_type_clause` | Optional — a Wurm-style material-type bonus/penalty, only active once OQ-2 is ruled |
| `notes` | Flavor / Wurm source citation |

A worked-example entry using this template:

```yaml
name: "Steel Longsword"
record_type: Item
source_skill: "Weaponsmithing"
min_skill_tier: 2
inputs:
  - {name: "Steel Lump", record_type: Component, quantity: 1}
  - {name: "Sword Hilt", record_type: Component, quantity: 1}
item_tier_formula: "Option A: min(Skill-Tier, max(input Tiers))"
tags: ["slot:main_hand", "offense:melee", "damage:slashing", "handling:light"]
material_type_clause: "material:steel — pending OQ-2 ruling"
notes: "Wurm Online source: Weaponsmithing subskill of Blacksmithing; Steel alloy per Metallurgy page (0.20kg Iron + 0.20kg Charcoal)."
```

---

## 8. Proposed Tiwas Crafting Skill Family (content-authoring candidate)

Wurm's skill tree suggests a clean Tier-1/Tier-2 Crafting Skill lineage for Tiwas,
**not yet assigned to any Attribute pair** — this is new content requiring Tiwa's
attribute-pairing decision (consistent with how the mirror-combat playtest brief
flagged its own skill↔attribute assignments as a non-binding design choice, §8.1 of
that brief):

| Proposed Tiwas Skill | Wurm Source Skill | Suggested Domain |
|---|---|---|
| Carpentry | Carpentry | Body |
| Fine Carpentry | Fine carpentry (Carpentry subskill) | Body (Advanced Skill off Carpentry) |
| Blacksmithing | Blacksmithing | Body |
| Weaponsmithing | Weaponsmithing (Blacksmithing subskill) | Body (Advanced Skill off Blacksmithing) |
| Armoursmithing | Armour smithing (Blacksmithing subskill) | Body (Advanced Skill off Blacksmithing) |
| Masonry | Masonry / Stone cutting | Body |
| Leatherworking | Leatherworking (Tailoring subskill) | Body |
| Cloth Tailoring | Cloth tailoring (Tailoring subskill) | Body |
| Pottery | Pottery | Body |
| Jewelry Smithing | Jewelry smithing | Body |

All ten are proposed as **Body-domain** skills (Physical Energy resource), consistent
with DEC-012.3's lineage-follows-root-Tier-1-domain rule and with every crafting skill
in Wurm being a physical trade. **No attribute pairs are proposed** — that choice is
reserved for Tiwa, exactly as the mirror-combat brief reserved its own skill↔attribute
choices.

---

## 9. Open Questions Requiring Tiwa's Ruling

These are **new** forks surfaced by this research, in addition to the crafting
proposal's already-open items (Tier-formula Option A/B/C; tool/facility requirements;
Component-as-standalone default; material acquisition/EQ-3A economy).

| ID | Question | Wurm's Answer (reference only) |
|---|---|---|
| OQ-1 | Should crafting Items carry a `min_skill_tier` gate analogous to DEC-041's location-Effect gate, or should any Skill-Tier attempt any Item (with only success-chance varying)? | Wurm uses hard skill-level gates ("hard limits") that no tool/material quality can bypass. |
| OQ-2 | Should raw-Material **type** (wood species, metal species) carry an optional mechanical clause Tag, and if so, via what grammar (DEC-088 Conditional-Trait-Binding-style, or a simpler flat modifier)? | Wurm: yes, extensively (oak −20% tool use-damage, adamantine +10% weapon damage, etc.). |
| OQ-3 | Should Components support a **multi-input combination recipe** (fixed-ratio alloying) as a first-class Component-creation mode, distinct from the single-chain Material→Component step already sketched? | Wurm: yes — Steel, Brass, Bronze, Electrum are all two-input fixed-ratio alloys. |
| OQ-4 | Should an optional **Rarity** bonus layer (three or four discrete steps above normal) be adopted for Items/Materials, independent of Tier/Magnitude? | Wurm: yes (Rare/Supreme/Fantastic), with small stacking bonuses to the item's own function and a cosmetic glow. |
| OQ-5 | Should Tags gain a dedicated `tool:` namespace, consumed as a **precondition-only** (never expended) requirement on Crafting Extended Tests? | Wurm: yes — tools gate success chance/quality but are never consumed by ordinary creation. |
| OQ-6 | Should any Material be allowed to **not** cap the Item's achievable Magnitude on Repair (Wurm's leather exception), or should DEC-129's "Magnitude repairs up to Item Tier" always apply uniformly? | Wurm: leather is a documented exception; most other materials are not. |
| OQ-7 | How does a negative StateRecord (equipment damage) interact numerically with Item Magnitude for *purposes of use*, if at all — does Tiwas need a Wurm-style "effective Magnitude = Magnitude × (favorable/unfavorable factor from the damage record's Tier)" formula, or does the existing DEC-118/119 "damage never touches Magnitude; `state:unusable` is a hard on/off gate" fully cover this with no graduated effect? | Wurm: continuous effective-QL degradation curve, not a binary gate. |
| OQ-8 | Which of the crafting proposal's three candidate Tier-assignment formulas (Option A/B/C) should be adopted, given the alloying evidence in §3.2 that the **lesser input tends to cap** the output rather than being averaged? | Wurm: capping/lesser-input behavior, favoring Option A over Option B. |

---

## 10. What Was Deliberately Not Adapted

- **All real-world action-timer values** (forge heat-up minutes, action queue seconds,
  etc.) — noted where encountered in research, never converted to a Tiwas duration,
  per this task's explicit instruction and the standing absence of a ruled Time/Action
  duration system (G3 open).
- **"Sweet spot" skill-gain optimization** — a Wurm player-skill-training meta-strategy,
  not a crafting-output mechanic; out of scope for an item/material adaptation.
- **The full 1,500+ item Wurmpedia catalog** — infeasible and unnecessary to enumerate
  exhaustively; §7's template plus §6's worked examples are intended to let any future
  session (Claude, OpenCode, or Tiwa directly) extend the catalog incrementally without
  new rules, exactly mirroring how the existing Tier-1 primitive-item catalog was built.
- **Wurm's currency/trader-price system** — out of scope pending the EQ-3A wealth/economy
  fork, which this document does not touch or presume to close.

---

## Appendix — Source Pointers (Wurmpedia, retrieved 2026-09-14)

- Crafting (main mechanics): `wurmpedia.com/index.php/Crafting`
- Quality level: `wurmpedia.com/index.php/Quality_level`
- Improving Guide (sweet-spot formula, reference only): `wurmpedia.com/index.php/Improving_Guide`
- The Curve (skill-vs-QL formula, reference only): `wurmpedia.com/index.php/The_Curve`
- Rarity system: `wurmpedia.com/index.php/Rarity_system`
- Metal lumps / Metallurgy (alloy recipes): `wurmpedia.com/index.php/Metal_lumps`, `wurmpedia.com/index.php/Metallurgy`
- Metal properties (bonus/penalty table): `wurm.fandom.com/wiki/Metal_properties`
- Wood / Tree / Woodcutting (wood-type properties): `wurmpedia.com/index.php/Wood`, `wurmpedia.com/index.php/Tree`, `wurmpedia.com/index.php/Woodcutting`
- Stone shards / slabs / Mining: `wurmpedia.com/index.php/Stone_shards`, `wurmpedia.com/index.php/Slab`, `wurmpedia.com/index.php/Mine`
- Leather / Leatherworking / Tailoring / Cloth tailoring: `wurmpedia.com/index.php/Leather`, `wurmpedia.com/index.php/Leatherworking`, `wurmpedia.com/index.php/Tailoring`, `wurmpedia.com/index.php/Cloth_tailoring`
- Skill list / Guide to Crafting Skill Limits: `wurmpedia.com/index.php/List:skills`, `wurmpedia.com/index.php/Guides:Guide_to_Crafting_Skill_Limits`

**No content from these pages is reproduced verbatim beyond short attributive
paraphrase; all figures and recipe ratios are restated in Claude's own words per
standing copyright discipline.**
