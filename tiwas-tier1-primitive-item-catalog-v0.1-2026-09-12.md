---
document:
  title: "Tiwas — Tier-1 Primitive Item Catalog (Materials, Components, Items)"
  version: "v0.1"
  status: "Non-canonical example content. Advisory catalog under the DEC-077.A content-authoring precedent — illustrative, not authored/blessed by Tiwa yet. No DEC assigned."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
depends_on: >
  Builds directly on `tiwas-crafting-system-proposal-v0.1-2026-09-12.md` — uses
  its Item-family record schema (§2), mandatory Material→Component→Item pipeline
  (§3), and Recipe record shape (§9). None of that proposal is Ruled either;
  this document is illustrative content built on top of an unruled framework and
  is doubly provisional.
---

# Tiwas — Tier-1 Primitive Item Catalog v0.1

## 0. Purpose

A worked example set of hand-made, non-metal, Tier-1 items — the earliest rung of the crafting proposal's Tier ladder — so future item authoring (any Tier, any material tech) has a concrete pattern to extend from. Every entry follows the requirement that **if making an item requires a tool, that tool must itself appear in this catalog as something buildable**, so the whole set is self-bootstrapping from bare hands.

## 1. Research Basis

Real-world grounding: primitive-technology/survival-skills practice (flintknapping, natural cordage-making, rawhide/hide processing, bow-drill fire, pit-fired pottery) and the standard tool-progression those sources teach in — cordage first (lowest tool requirement), then percussion-knapped stone edges, then hafting/sewing once a cutting edge and cordage both exist.

TTRPG/video-game cross-reference (paraphrased, structural only — no rules text reproduced): tiered "tech level" equipment categorization comparable to GURPS Low-Tech's TL0 (Stone Age) chapter, which groups gear by dominant material (stone/wood/rawhide) before bronze or iron appear; and primitive-crafting-mod/survival-game tech trees (e.g., primitive-tools-style Minecraft mods, survival-crafting games) that gate metal-tier tools behind an explicit knap→haft→bind sequence rather than letting players skip straight to finished tools. This catalog's dependency order (§5) follows the same shape.

## 2. Materials (Tier 1 — raw, gathered directly)

| Subtype | Real-world source | Acquisition | Tier | Magnitude |
|---|---|---|---:|---:|
| `stone_rock` | streambed, ground | hand-gathered, no test | 1 | 1 |
| `flint` | outcrops, streambeds | hand-gathered or Survival test to locate a good source | 1 | 1 |
| `wood_branch` | trees, deadfall | hand-gathered/broken | 1 | 1 |
| `plant_fiber` | grass, nettle, yucca, bark | hand-stripped | 1 | 1 |
| `leaf` | broad-leaf plants | hand-gathered | 1 | 1 |
| `hide_rawhide` | hunted/scavenged animal | Survival test (hunt/butcher) | 1 | 1 |
| `sinew` | animal tendon | by-product of `hide_rawhide` acquisition | 1 | 1 |
| `bone` | animal skeleton | by-product of `hide_rawhide` acquisition | 1 | 1 |
| `clay` | riverbank | hand-gathered | 1 | 1 |
| `water` | stream/spring | gathered (needs a container to carry) | 1 | 1 |
| `resin_pitch` | coniferous tree sap | hand-gathered/tapped | 1 | 1 |
| `ash` | burned wood | by-product of using `fire_starting_kit` | 1 | 1 |
| `cotton_boll` | cotton plant | hand-picked | 1 | 1 |

`cotton_boll` is this catalog's deliberate material-complexity ceiling, per your instruction — nothing here is more processed than raw cotton fiber.

## 3. Components (Tier 1 — one processing step from Materials)

| Subtype | Made from | Tool required | Crafting Skill |
|---|---|---|---|
| `cordage` | `plant_fiber` ×N | **none** — hand-twisted/plied | Fiber Craft |
| `woven_fiber_cloth` | `plant_fiber` or `cotton_boll` ×N | none — hand-plaited | Fiber Craft |
| `stone_flake_blade` | `flint` | `hammerstone` | Flintknapping |
| `stone_scraper` | `flint` | `hammerstone` | Flintknapping |
| `fire_hardened_point` | `wood_branch` | `fire_starting_kit` | Woodcraft |
| `wood_haft` | `wood_branch` | `stone_flake_blade` | Woodcraft |
| `rawhide_strip` | `hide_rawhide` | `stone_scraper` | Hideworking |
| `pitch_glue` | `resin_pitch` + `ash` | `fire_starting_kit` | Hideworking/Woodcraft |
| `bone_awl` | `bone` | `stone_flake_blade` | Boneworking |

`cordage` requires no tool at all — this is why it is the true root of the tree (matches the real-world practice of teaching cordage before knapping).

## 4. Tools (the "equipment must itself be built" chain)

| Subtype | Built from | Tool required to build it | Unlocks |
|---|---|---|---|
| `hammerstone` | `stone_rock` (selected, unmodified) | **none** — a suitable rock used directly | `stone_flake_blade`, `stone_scraper` |
| `stone_flake_blade` | see §3 | `hammerstone` | `wood_haft`, `bone_awl`, `fire_starting_kit`, cutting `rawhide_strip` |
| `fire_starting_kit` | `wood_branch` ×2 (spindle + fireboard) + `cordage` + `plant_fiber` (tinder) | `stone_flake_blade` (to notch the wood) | `fire_hardened_point`, `pitch_glue`, sealed `waterskin`, cooked food |
| `bone_awl` | see §3 | `stone_flake_blade` | any sewn item: `rawhide_vest`, `simple_tunic`, `quilted_cotton_armor` |

`hammerstone` is the one entry with no build step — real-world flintknapping starts by selecting, not making, a percussion stone. Everything else in this catalog traces back to it or to `cordage`.

## 5. Bootstrapping Order

```
TIER 0 (bare hands, no tool)
  gather all Materials (§2)
  make: cordage, woven_fiber_cloth, leaf_hat, club
  select: hammerstone

  ↓ (using hammerstone)
  make: stone_flake_blade, stone_scraper

  ↓ (using stone_flake_blade)
  make: wood_haft, fire_starting_kit, bone_awl, rawhide_strip (with stone_scraper), arrow shafts

  ↓ (using fire_starting_kit)
  make: fire_hardened_point, pitch_glue, waterskin (sealed), digging_stick/fire_hardened_spear

  ↓ (using bone_awl + sinew or cordage as thread)
  make: rawhide_vest, simple_tunic, quilted_cotton_armor

  ↓ (combining blade + haft + cordage/rawhide_strip)
  make: flint_knife, hafted_hand_axe, sling, self_bow + arrow, shields
```

## 6. Items — Weapons (non-metal)

| Subtype | Inputs | Tool required | Crafting Skill | Reference |
|---|---|---|---|---|
| `club` | `wood_branch` ×1 | none | Woodcraft | universal beginner weapon; Tier-1, straight from Material, no Component |
| `digging_stick` / `fire_hardened_spear` | `wood_branch` + self-applied `fire_starting_kit` step | `fire_starting_kit` | Woodcraft | oldest known hunting-spear technology (fire-hardened wood points); "sharpened stick" is a near-universal starter weapon |
| `flint_knife` | `stone_flake_blade` + `wood_haft` + `cordage` | `hammerstone` (upstream) | Flintknapping + Woodcraft | matches the stone-knife entry point common to Stone-Age equipment catalogs |
| `stone_hand_axe` (unhafted) | `stone_flake_blade` (larger flake) | `hammerstone` | Flintknapping | earliest tool tradition — biface with no haft |
| `hafted_hand_axe` | `stone_flake_blade` + `wood_haft` + `cordage` or `rawhide_strip` | `hammerstone` (upstream) | Flintknapping + Woodcraft | later refinement of the hand axe, per real-world hafted-axe progression |
| `sling` | `woven_fiber_cloth` (pouch) + `cordage` ×2 | none | Fiber Craft | one of the oldest ranged weapons; near-universal starter ranged option |
| `self_bow` | `wood_branch` (stave) + `cordage` (string) | `stone_flake_blade` | Woodcraft | **flagged as a stretch item** — real tillering is more involved than the rest of this list; keep at Tier 1 for accessibility, or push to Tier 2 if you want bow-making gated harder |
| `arrow` (batch) | `stone_flake_blade` or `fire_hardened_point` (small) + `wood_branch` (shaft) + `cordage` (fletch lashing) | `hammerstone` (upstream) | Woodcraft + Flintknapping | consumable ammunition — crafted and tracked by `quantity`, not as single records |

## 7. Items — Armor (non-metal)

| Subtype | Inputs | Tool required | Crafting Skill | Reference |
|---|---|---|---|---|
| `rawhide_vest` | `rawhide_strip` ×N + `sinew` (thread) | `bone_awl` | Hideworking | matches the rawhide/leather category of Stone-Age armor catalogs |
| `woven_bark_shield` | `wood_haft` (frame) + `woven_fiber_cloth` + `cordage` | `stone_flake_blade` | Woodcraft | light shield archetype |
| `wooden_buckler` | `wood_branch` (shaped plank) + `rawhide_strip` (facing/handle) | `stone_flake_blade` | Woodcraft | — |
| `quilted_cotton_armor` | `cotton_boll` (carded/quilted) + `cordage` (stitching) | `bone_awl` | Fiber Craft | the deliberate **material ceiling** of this catalog — a hand-quilted gambeson-equivalent, still built with no metal tools |

## 8. Items — Clothing & Gear

| Subtype | Inputs | Tool required | Crafting Skill | Reference |
|---|---|---|---|---|
| `leaf_hat` | `leaf` ×N (woven/layered) | none | Fiber Craft | simplest possible Tier-1 item — Material straight to Item, no Component |
| `sandals` | `woven_fiber_cloth` or `rawhide_strip` (sole) + `cordage` (straps) | none | Fiber Craft / Hideworking | matches documented plant-fiber sandal traditions |
| `simple_tunic` | `woven_fiber_cloth` or `rawhide_strip` + `cordage` (ties) | `bone_awl` if sewn | Fiber Craft / Hideworking | — |
| `fiber_pouch` | `woven_fiber_cloth` + `cordage` (drawstring) | none | Fiber Craft | — |
| `waterskin` | `hide_rawhide` + `pitch_glue` (seal) + `cordage` (neck tie) | `fire_starting_kit` (renders pitch) | Hideworking | — |
| `unfired_clay_pot` | `clay` + `water` | none — sun/air-dried | Pottery | note: a *fired* pot needs a kiln/pit fire; flag as a Tier-2 stretch item if firing should be gated behind a built fire pit |
| `torch` | `wood_branch` + `woven_fiber_cloth` or `plant_fiber` (wrap) + `resin_pitch` (fuel) | `fire_starting_kit` | Woodcraft | — |

## 9. Worked Recipe Records

Using the crafting proposal's Recipe schema (§9 of `tiwas-crafting-system-proposal-v0.1-2026-09-12.md`), fully worked out for three representative items:

```
Recipe: flint_knife
  output_subtype   : flint_knife
  output_type      : Item
  output_tier      : 1
  inputs            :
    - {subtype: stone_flake_blade, quantity: 1, type: Component}
    - {subtype: wood_haft,         quantity: 1, type: Component}
    - {subtype: cordage,           quantity: 1, type: Component}
  crafting_skill   : Flintknapping+Woodcraft (combined/adjacent skills, GM Fiat on which governs)
  min_skill_tier   : 1
  tool_required    : hammerstone (upstream, not consumed directly by this recipe)
```

```
Recipe: rawhide_vest
  output_subtype   : rawhide_vest
  output_type      : Item
  output_tier      : 1
  inputs            :
    - {subtype: rawhide_strip, quantity: 4, type: Component}
    - {subtype: sinew,         quantity: 2, type: Material}
  crafting_skill   : Hideworking
  min_skill_tier   : 1
  tool_required    : bone_awl
```

```
Recipe: hafted_hand_axe
  output_subtype   : hafted_hand_axe
  output_type      : Item
  output_tier      : 1
  inputs            :
    - {subtype: stone_flake_blade, quantity: 1, type: Component}
    - {subtype: wood_haft,         quantity: 1, type: Component}
    - {subtype: rawhide_strip,     quantity: 1, type: Component}
  crafting_skill   : Flintknapping+Woodcraft
  min_skill_tier   : 1
  tool_required    : hammerstone (upstream)
```

All three satisfy `Result Tier = min(Skill-Tier, max(input Tiers)) = min(1, 1) = 1` under the crafting proposal's default Option A formula (§5 of that document) — consistent with every entry in this catalog being genuine Tier 1.

## 10. Open Items Carried From the Parent Proposal

Nothing here resolves the parent document's Open Questions (its §11) — it only exercises the framework against concrete content. In particular still unresolved: whether `flint`/`hide_rawhide` acquisition requires its own Skill Test (flagged inline in §2 as "Survival test"), and whether `unfired_clay_pot`→fired pottery should be pushed to Tier 2 behind a built fire pit (flagged in §8). Both are recommendations embedded in this catalog, not rulings.
