---
document:
  title: "Wurm Online Crafting System — Comprehensive Adaptation for Tiwas TTRPG — Part 2: Expanded Item Catalog"
  version: "v0.1"
  status: "Advisory / Non-canonical. No DEC assigned. Example/candidate content pending Tiwa's review under the DEC-077.A content-authoring precedent. Companion to and continuation of Part 1 (`tiwas-wurm-online-crafting-adaptation-2026-09-14.md`) — read Part 1 first for the mapping framework, materials, and governance notice."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-14"
  research_source: "Wurmpedia (wurmpedia.com), retrieved via web search/fetch, 2026-09-14"
---

# Wurm Online Crafting System — Part 2: Expanded Item Catalog

Continuation of Part 1. All governance notices, the mapping framework (§2 of Part 1),
Open Questions OQ-1–OQ-8, and the "what was not adapted" scope boundary (§10 of Part 1)
apply identically here and are not repeated. Nothing below is a ruling.

---

## 11. Weapons — Full Category Breakdown

Wurm splits weapons by handedness and damage type, each with its own sub-skill under
Weaponsmithing (creation side) and a matching combat sub-skill (use side — combat-skill
mapping is **out of scope** for this crafting document; only the **creation** chain is
addressed).

### 11.1 One-Handed Weapons

| Wurm Item | Damage Type (reference) | Proposed Tiwas Tags | Component Chain |
|---|---|---|---|
| Short sword | Cutting + Piercing | `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light` | Metal Lump → Blade + Log → Grip |
| Long sword | Cutting + Piercing | `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light` | Metal Lump → Blade + Log → Grip |
| Small axe | Cutting | `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light` | Metal Lump → Axe Head + Shaft |
| Large axe | Cutting (fastest in class, lowest base damage per Wurm's own combat notes) | `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light` | Metal Lump → Axe Head + Shaft |
| Small maul | Mauling/blunt | `slot:main_hand`, `offense:melee`, `damage:bludgeoning`, `handling:light` | Metal Lump → Maul Head + Shaft |
| Medium maul | Mauling/blunt | `slot:main_hand`, `offense:melee`, `damage:bludgeoning`, `handling:light` | Metal Lump → Maul Head + Shaft |
| Crowbar | Blunt (dual-purpose tool/weapon — a clean example of an Item carrying both a `tool:` and a `weapon` Tag set) | `slot:main_hand`, `offense:melee`, `damage:bludgeoning`, `handling:light`, `tool:pry` | Metal Lump (single-piece forge) |
| Sickle | Cutting (also a Farming tool — another dual-purpose example) | `slot:main_hand`, `offense:melee`, `damage:slashing`, `handling:light`, `tool:harvest` | Metal Lump → Blade + Shaft |

### 11.2 Two-Handed Weapons

Two-handed weapons trade the off-hand/shield slot for materially higher damage — in
Wurm, two-handed weapon quality matters disproportionately (low-QL two-handers suffer a
much steeper damage/accuracy falloff than one-handers of equivalent QL). This is a
useful **design note** (not a rule) for any future Tiwas Effect/Magnitude scaling on
`handling:heavy` weapons: a nonlinear, not merely additive, Quality-to-output curve may
be worth flagging for Tiwa if `handling:heavy` weapon balancing is revisited.

| Wurm Item | Damage Type (reference) | Proposed Tiwas Tags | Component Chain |
|---|---|---|---|
| Two-handed sword | Cutting + Piercing | `slot:two_hand`, `offense:melee`, `damage:slashing`, `handling:heavy` | Metal Lump → Blade + Log → long Grip |
| Huge axe | Cutting | `slot:two_hand`, `offense:melee`, `damage:slashing`, `handling:heavy` | Metal Lump → Axe Head + long Shaft |
| Large maul | Mauling/blunt | `slot:two_hand`, `offense:melee`, `damage:bludgeoning`, `handling:heavy` | Metal Lump → Maul Head + long Shaft |
| Huge shod club | Mauling/blunt | `slot:two_hand`, `offense:melee`, `damage:bludgeoning`, `handling:heavy` | Log (shod = metal-banded) → Shaft + Metal Bands |

### 11.3 Polearms

Polearms are a distinct Wurm skill family; per Wurmpedia, polearms deal bonus damage
against mounted/moving targets — a situational combat-Effect note, not itself a
crafting concern, but worth flagging as a possible future `handling:reach` Tag
consumer once a Position/Mounted-combat Effect exists.

| Wurm Item | Damage Type (reference) | Proposed Tiwas Tags | Component Chain |
|---|---|---|---|
| Long spear | Piercing | `slot:two_hand`, `offense:melee`, `damage:piercing`, `handling:reach` | Metal Lump → Spearhead + long Shaft |
| Spear | Piercing (also usable one-handed per Wurm's own dual listing) | `slot:main_hand` **or** `slot:two_hand`, `offense:melee`, `damage:piercing`, `handling:reach` | Metal Lump → Spearhead + Shaft |
| Halberd | Cutting | `slot:two_hand`, `offense:melee`, `damage:slashing`, `handling:reach` | Metal Lump → Halberd Head + long Shaft |
| Staff (wooden) | Mauling/blunt | `slot:two_hand`, `offense:melee`, `damage:bludgeoning`, `handling:reach` | Log only (no metal Component — good low-Tier training example) |
| Staff (metal) | Mauling/blunt | `slot:two_hand`, `offense:melee`, `damage:bludgeoning`, `handling:reach` | Metal Lump (single-piece forge, no wood) |

### 11.4 Ranged (Bowyery / Fletching)

| Wurm Item | Component Chain | Proposed Tiwas Tags |
|---|---|---|
| Short bow / Long bow | Willow or ash-analog Log (Bowyery) → shaped Bow Stave | `slot:main_hand`, `offense:ranged`, `handling:light`/`handling:heavy` |
| Crossbow | Log → Stock + Metal Lump → Prod/Mechanism (a genuine two-Material-Type Item, same pattern as §6.3's studded jacket) | `slot:two_hand`, `offense:ranged`, `handling:heavy` |
| Arrow | Shaft (Log) + Metal Lump → Arrowhead + Feathers (from butchered fowl) | `offense:thrown`/`offense:ranged` ammunition, consumed on use (a genuinely **consumable** Item — see §13 below) |

---

## 12. Armor — Full Tier Progression

Wurm's own player community (forum consensus, cited in research) describes a widely
agreed **armor material tier ladder**, from cheapest/weakest to best/most prestigious.
This ladder is proposed as a ready-made **Item Tier progression template** for Tiwas
armor content — each step is a strictly higher Item Tier band than the last, using the
same base Armor slot set (head/chest/arms/hands/legs/feet):

```
Cloth  →  Leather  →  Studded Leather  →  Chain  →  Plate (Steel) / Drake Hide
       →  Plate (Adamantine) / Drake Scale
       →  Plate (Glimmersteel) / Plate (Seryll)
```

| Tier Band (proposed) | Armor Type | Material Chain | Notes (reference only) |
|---|---|---|---|
| 1 | Cloth | Fiber crop → Cloth squares (Cloth Tailoring) | Lowest defense, no metal required — good starter Tier |
| 1–2 | Leather | Hide → Leather (Leatherworking) | §6.3's base Item before studding |
| 2 | Studded Leather | Leather + metal Rivets (composite, §6.3) | First composite (two-Material-Type) armor tier |
| 2–3 | Chain | Metal Lump → wire/links (Armoursmithing) | Superior defense, higher mobility cost than Plate per Wurm's own data |
| 3 | Plate (base metal: Steel) | Steel Lump (alloy, §3.2) → Plate pieces (Armoursmithing) | Highest base-metal defense; heaviest |
| 3 | Drake Hide | Rare creature-sourced hide (Leatherworking, improved only with regular Leather per Wurm's own note) | Lighter than Plate at comparable defense — a `material:drake_hide` Tag candidate under OQ-2 |
| 4 | Plate (Adamantine) | Rare Adamantine Lump | Top metal tier; per §3.2's reference bonus data, adds damage-reduction and movement-speed bonuses |
| 4 | Dragon Scale | Rare creature-sourced scale | Parallel top tier to Adamantine Plate, different Material source |
| 5 | Plate (Glimmersteel / Seryll) | Rarest lumps | Wurm's community-agreed apex armor tier |

### 12.1 Armor Slot Set (per Wurmpedia's `Category:Armour` listing)

| Slot | Cloth | Leather | Chain | Plate |
|---|---|---|---|---|
| Head | Cloth hood | Leather cap | Chain coif | Great helm / Basinet helm |
| Chest | Cloth jacket/shirt | Leather jacket | Chain jacket | Breast plate |
| Arms | Cloth sleeve | Leather sleeve | Chain sleeve | Plate vambrace |
| Hands | Cloth glove | Leather glove | Chain gauntlet | Plate gauntlet |
| Legs | Cloth pants | Leather pants | Chain pants | Plate leggings |
| Feet | Cloth shoe | Leather boot | Chain boot | Plate sabatons |
| Mount (Barding) | — | Leather barding | Chain barding | — (per Wurmpedia, Barding is its own slot family, not paralleled at every tier) |

**Note (reference only, not adapted):** Wurmpedia records that mixing armor Types
within a set generally auto-defaults the **weaker/lower piece up to the stronger
adjacent piece's category** for certain interactions (e.g., a leather set with one chain
gauntlet defaults toward chain for that interaction) — an item-mixing edge case. This is
flagged only as a design note; Tiwas has no ruled per-slot armor-mixing interaction and
none is proposed here.

Each slot maps to a Tiwas `Location` value once armor is checked against a struck
sub-location (already-ruled machinery: DEC-062 armor location-bound, DEC-112/DEC-137
Human location template, DEC-114 R2 Armor Bypass tag trigger — this catalog changes
none of that, it only supplies the flesh for the `defense:armor` Tag's bound Location).

---

## 13. Consumables — A New Item Sub-Category

Ammunition (Arrows, Bolts) and certain single-use Items (e.g., a torch's fuel, a
whetstone's sharpening charges in some editions) are **consumed on use**, which is a
genuinely different lifecycle from every other Item discussed so far (all of which
persist and accumulate Tier/Magnitude/damage records indefinitely). Tiwas's Item-family
record (DEC-128 Q1) does not currently distinguish a "consumed on use" lifecycle from
a persistent one.

**This is flagged as a new open question, OQ-9**, not answered here: should a
Consumable Item simply be an ordinary Item-family record that a *using* Effect deletes
outright on a successful application (no Repair/Upgrade ever applies to it), or does it
need its own lighter-weight record shape? Wurm's answer (ammunition is just a
lower-Tier Item consumed in bulk, tracked by stack quantity per the DEC-078 A5 bulk
bookkeeping precedent already used for encumbrance-load tracking) is offered as the
simplest available precedent and is the recommended default absent a contrary ruling.

---

## 14. Tools — Full List (Cross-Skill)

Tools are the Items that gate **other** Items' creation as a `tool:`-tagged
precondition (OQ-5). Consolidated from Wurmpedia's per-skill "tools needed" guidance
across Carpentry, Blacksmithing, and Leatherworking/Tailoring:

| Tool | Required By (Skill family) | Proposed Tag |
|---|---|---|
| Hammer / Mallet | Blacksmithing, Carpentry (both families use a hammer-class tool) | `tool:strike` |
| File | Carpentry, Blacksmithing (improve actions) | `tool:refine` |
| Pelt (rough hide, untreated) | Carpentry, Blacksmithing (polishing step) | `tool:polish` |
| Carving knife | Carpentry | `tool:carve` |
| Whetstone | Blacksmithing (improve actions) | `tool:sharpen` |
| Needle | Leatherworking, Cloth Tailoring | `tool:stitch` |
| Awl | Leatherworking | `tool:pierce` |
| Scissors | Cloth Tailoring | `tool:cut_cloth` |
| Stone chisel | Blacksmithing subskills, Masonry | `tool:chisel` |
| Saw | Carpentry (plank production) | `tool:saw` |
| Hatchet / Axe | Woodcutting (gathering, not crafting proper) | `tool:fell` |
| Pickaxe | Mining (gathering) | `tool:mine` |
| Rake / Hoe | Farming (gathering, fiber crops) | `tool:till` |
| Mortar and pestle | Pottery, Alchemy-adjacent | `tool:grind` |
| Kiln (fixture, not carried) | Pottery | `tool:fire` (fixture-class; requires a `Location`-bound structure Item, not a carried tool) |
| Forge (fixture, not carried) | Blacksmithing (heating metal for all creation/improve actions) | `tool:heat` (fixture-class) |
| Loom (fixture, not carried) | Cloth Tailoring | `tool:weave` (fixture-class) |

**Fixture-class tools** (Forge, Kiln, Loom) are a distinct sub-case: they are not
carried in inventory but must be present at the crafting location. This is presented as
a `Location`-bound precondition (parallel to how armor location-binding already works,
DEC-062) rather than an inventory-Tag precondition — flagged as part of OQ-5, not
separately numbered, since it is the same underlying open question (how crafting
preconditions attach to the Extended Test) applied to a fixture instead of a carried
item.

---

## 15. Ships, Vehicles, and Structures (Large Multi-Component Items)

These categories are Wurm's most complex builds — a hull can require dozens of planks,
hundreds of nails, and multiple sub-Component types, assembled over many creation
actions rather than one. They are the clearest real-world precedent for a
**multi-stage Extended Test** (DEC-067/068/070) whose Margin-accumulation total must
cross a much larger GM-set completion threshold (DEC-070) than a simple hand tool.

| Wurm Item | Component Summary (reference only) | Proposed Tiwas Treatment |
|---|---|---|
| Small cart | Planks + wheels (Planks + Metal fittings) + Nails | Single Extended Test, moderate threshold |
| Rowboat | Planks (hull) + Nails + Rope (fiber Component, not yet detailed in Part 1 — flagged for future addition) | Single Extended Test, higher threshold |
| Sailboat | Rowboat's Components + Square of Cloth (sail) + Rope | Two-stage build: hull Item, then a sail sub-Item attached — a genuine worked example of an **Item consuming another finished Item as a Component**, not yet covered by the existing DEC-128 record shape and flagged as OQ-10 (see below) |
| House wall (stone) | Stone Bricks (Masonry) | Structure Item, `Location`-fixed, not inventory-carried — parallel to the Fixture-class tools in §14 |
| Bridge | Marble/Stone Bricks + Keystone (Marble Slab, a load-bearing single high-Tier Component) | Multi-stage Extended Test with a required high-Tier "keystone" sub-Component — a good template for any future "boss Component" gating pattern |

**OQ-10 (new):** Should the Item-family record (DEC-128 Q1) permit a finished Item to
be consumed as an **input Component** for a larger Item (a sail Item feeding into a
sailboat Item), and if so, does the smaller Item's own Tier/Magnitude propagate into the
larger Item's Tier-assignment formula (§9 OQ-8) the same way a raw Component does, or
does it cap differently (a "sub-assembly" rule)? Wurm's implicit answer is that a
finished, wearable/usable sub-item (a sail, a wheel, a lock) can absolutely be attached
to a larger build and its own quality matters to the whole — this document recommends
treating it identically to any other Component input for Tier-formula purposes unless
Tiwa rules otherwise, but explicitly does not decide this.

---

## 16. Jewelry and Locks (Low-Volume, High-QL-Sensitivity Categories)

| Category | Component Chain | Notes |
|---|---|---|
| Jewelry (ring, bracelet, amulet) | Silver/Gold/Electrum/Seryll Lump → shaped piece (Jewelry Smithing) | Small material weight per item; QL-sensitive value scaling in Wurm (not adapted — trader-price mechanic, EQ-3A territory) |
| Locks/Keys | Metal Lump → Lock body + matching Key (Locksmithing) | A Lock Item and its Key Item are **paired records** — a genuine precedent for an Item that only functions correctly against one other specific Item instance, which is new territory relative to anything in DEC-115/117's counter/removal-Tag machinery (flagged as a design curiosity, not numbered as an open question since it has no clear near-term Tiwas use case) |

---

## 17. Consolidated Skill-Family Diagram

```
                         TIWAS CRAFTING (proposed)
                                   |
        -----------------------------------------------------------
        |            |            |            |           |
   Carpentry    Blacksmithing   Masonry    Leatherworking  Pottery
        |            |                          |
  Fine Carpentry  Weaponsmithing            Cloth Tailoring
   (Advanced)     Armoursmithing              (parallel,
                   (Advanced)                 not a child
                                                of Leatherworking
                                                per Wurm's own
                                                Tailoring-parent
                                                split)

              Jewelry Smithing — parallel, metal-lump-fed,
              but its own family (per Wurmpedia's own
              skill tree, not a Blacksmithing subskill)
```

---

## 18. Summary of All Open Questions (Parts 1 + 2 combined)

| ID | One-line summary |
|---|---|
| OQ-1 | Crafting `min_skill_tier` gate: adopt or not? |
| OQ-2 | Material-type mechanical Tag clauses (oak, adamantine, etc.): adopt or not, and via what grammar? |
| OQ-3 | Multi-input fixed-ratio Component combination (alloying): adopt as a first-class recipe mode? |
| OQ-4 | Optional Rarity bonus layer: adopt or not? |
| OQ-5 | `tool:` Tag namespace as a consumed-never precondition (including fixture-class tools bound by Location rather than inventory)? |
| OQ-6 | Leather's "no Material-Tier ceiling on Repair" exception: adopt as a per-Material flag, or reject uniformity exceptions entirely? |
| OQ-7 | Does a negative StateRecord (equipment damage) need a graduated effective-Magnitude formula, or does the existing binary `state:unusable` gate fully cover it? |
| OQ-8 | Which Tier-assignment formula (Option A/B/C) does the alloying evidence favor? |
| OQ-9 | Do Consumable Items (ammunition) need a distinct lightweight record lifecycle, or are they ordinary Items deleted on use? |
| OQ-10 | Can a finished Item be consumed as a Component input to a larger Item, and does its Tier propagate normally? |

None of these are rulings. All are presented for Tiwa's review, exactly as the existing
stored crafting proposal's own open questions (1–6) remain open pending review.

---

## Appendix — Additional Source Pointers (Part 2)

- Weapon categories: `wurmpedia.com/index.php/Category:One_handed_weapon`,
  `wurmpedia.com/index.php/Category:Two_handed_weapon`,
  `wurmpedia.com/index.php/Polearms`
- Fighting/damage-type reference: `wurmpedia.fandom.com/wiki/Fighting`
- Armor categories and progression: `wurmpedia.com/index.php/Category:Armour`,
  `wurmpedia.com/index.php/Armour`, community armor-tier consensus thread
  (`steamcommunity.com/app/366220/discussions/0/490124466463724329/`)

**No content from these pages is reproduced verbatim beyond short attributive
paraphrase; all figures and category structures are restated in Claude's own words per
standing copyright discipline.**
