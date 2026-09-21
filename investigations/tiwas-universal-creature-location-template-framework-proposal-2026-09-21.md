---
document:
  title: "Tiwas — Universal Creature Location Template Framework (Frame / Module / Profile / Overlay)"
  version: "v0.1"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-21"
  last_modified_date: "2026-09-21"
  request_scope: "Structure for creature Location Templates (no location numbers); spec + blank skeletons + check against the ten stored templates; readers = Tiwa + LLM drafters; designer granted total creative freedom."
  evidence_limits: "Register annotations and the supplied corpus were read; the ten template files themselves were NOT available to this session. Rulebooks (GURPS, WFRP, RuneQuest/Mythras, Harn) were reached only through wikis and forum threads, not primary texts."
  stored_from: "tiwas-universal-creature-location-template-framework-proposal-v0.1-2026-09-21.md (repo-root copy, 2026-09-21)"
---

## Purpose and Origin

Framework proposal authored by **Claude Sonnet 5** (`claude-sonnet-5`), 2026-09-21:
a reusable Frame / Module / Profile / Overlay structure for creature Location
Templates, proposing no location numbers, with blank body-plan skeletons and a
check against the ten stored templates. Stored 2026-09-21 by OpenCode /
muse-spark-1.3-contributor-free under the analyze-assess-record-store workflow
as **advisory-only, non-canonical material** — assessed against the live
decision register (through DEC-156) and governance model, recorded on DEC-149,
no DEC assigned or inferred, nothing promoted or reclassified. Original body
preserved verbatim below; the file-level frontmatter above replaces the root
copy's header (original author preserved; assessor/last-modified record this
storage pass; request_scope/evidence_limits carried over).

---

# Tiwas — Universal Creature Location Template Framework

## 0. Governance and reading rules

| Item | Statement |
|---|---|
| Authority | None. Advisory proposal. Nothing here is Canonical, Ruled, or promoted (REQ-021 not run). |
| Creative freedom | Granted by Tiwa for this proposal. It permits proposing amendments, not making them. Each is tagged **AMEND-n** (§12) with default recommendation. |
| Numbers | This document proposes **no location numbers** for any creature. Numeric intervals stay content-authoring under DEC-077/077.A. The only numbers are (a) integer test vectors for the apportionment procedure (§8.3), explicitly illustrative, and (b) already-ruled figures quoted from the register. |
| External systems | Other RPGs, games and literature appear **only as research inputs** (§3). No external rule is adopted. |
| Drafter obligations | Advisory drafters submit candidates only; acceptance is Tiwa's (DEC-077/077.A; DEC-149 binding condition 4). |

## 1. Purpose, scope, variables

**Purpose.** Give creature-template authors (Tiwa, LLM drafters) one reusable structure so that any creature's Location Template can be built by choosing and composing parts, then attaching numbers later.

| In scope | Out of scope |
|---|---|
| Topology (tree), symmetry modes, function roles, coverage registration, composition operators, allocation-profile interface, validators, authoring workflow, body-plan skeletons, coverage test, check against stored templates | Numeric 100-state intervals for any creature; creature stat blocks; Effect rules that would consume roles; changing Zero-Step; promotion |

**Variables (defined before use).**

| Symbol | Meaning |
|---|---|
| LI | Location Index: integer 1–100 produced by Zero-Step (DEC-014). The 100 values are "states". |
| Node | One element of a template tree. Root = whole creature. |
| Interval [lo, hi] | Contiguous LI range owned by a node; width w = hi − lo + 1. |
| Leaf / Container | Node without / with children. |
| Address depth (AD) | Edges from root (root = 0; Tier-1 coarse zones = 1). Non-mechanical label (DEC-137/139); avoids collision with Skill-Tier. |
| Frame | Topology skeleton for one body plan (no widths). |
| Module | Reusable subtree kit attached to a frame slot. |
| Slot | Named attachment point on a frame or module, with accepted module kinds and cardinality. |
| Profile | The allocation layer: width classes/pins per sibling group → concrete intervals. The only layer that carries numbers. |
| Overlay | Metadata-only modifier (roles, registrations, tags). May not add/remove nodes or change widths. |
| Role | Descriptive function label on a node (§5.3). |
| Registration | Coverage assertion (e.g. `defense:armor`) bound to a node, separate from geometry. |
| Pin | A width fixed by an existing ruling (e.g. DEC-100 quartile) that apportionment must respect. |

## 2. Interface baseline (what any framework must interoperate with)

| # | Fixed point | Source | Framework stance |
|---|---|---|---|
| I-1 | LI = Zero-Step output, 1–100 | DEC-014 / Canonical §14.1 | Kept — the 100-state space is the coordinate system |
| I-2 | Laterality = units digit of Zero-Step output; odd = Left, even = Right | DEC-041(3), DEC-137 fork 6 | Kept for bilateral; **extended** to serial/radial/none (AMEND-3) |
| I-3 | Hierarchical address; single-source deterministic; no secondary roll | DEC-112 L-003/L-011, DEC-136 R1 | Kept |
| I-4 | Location Tier unbounded; resolution saturates at deepest authored node; qualifying Tier-2 Effect resolves to full authored leaf | DEC-136 R2, DEC-137 fork 1, DEC-139 | Kept |
| I-5 | Skill-Tier ≥ 2 gate for any location-referencing Effect | DEC-041(1)/(6) | Kept, untouched |
| I-6 | Tier-1 coarse Effects (Wound, Trip, Disarm/Break Hold, Equipment Damage) vs Tier-2-eligible (Armor Bypass) | DEC-113 R2 | Kept — frames must expose Tier-1 zones and leaf addresses |
| I-7 | Parent covers children; parent fallback on mismatch | DEC-112 L-007/L-012/L-014 | Kept; formalised as nesting invariant V-02 + Registration layer |
| I-8 | Wound record stores full address | DEC-112 L-013 | Kept |
| I-9 | Tier-1 zones: DEC-100 quartiles for bipedal-humanoid; bespoke otherwise | DEC-100, DEC-144 | Kept via **pins**; class table extended (AMEND-1) |
| I-10 | Individual templates per creature type, not a shared scheme | DEC-041(5) | **Tension** (AMEND-2) — shared skeletons, individual profiles |
| I-11 | Tags vocabulary-only; Skills never require Tags | DEC-116, DEC-117 R7, DEC-025 | Kept; roles are descriptive metadata |
| I-12 | Effect triggers read `state:held` / `state:worn` / `defense:armor` / `defense:shield` at struck zone | DEC-114 R2 | Kept; framework supplies `manipulation` nodes and registration structure |
| I-13 | Human v1 allocation frozen; content is Tiwa-authored/accepted | DEC-137 | Kept; Human v1 = reference profile of F-BIP |
| I-14 | No reserved states; single-state paired leaf fixes side | DEC-137 fork 7 + conventions | Kept; lint waiver W-137 |
| I-15 | Human-comparative statements in proposals are non-normative until re-derived | DEC-149 condition 1 | Kept; validator V-19 |
| I-16 | Parent→variant derivation acceptable; sibling interpolation needs sign-off per family | DEC-149 R7 | Kept; operators DERIVE / INTERPOLATE labelled accordingly |

## 3. Research synthesis

### 3.1 Sources and what they show

| ID | Domain | Source (§15) | Finding | Lesson taken |
|---|---|---|---|---|
| R-01 | TTRPG | GURPS hit locations | Penalty and location vary by target shape; missing anatomy (e.g. no head) is a modifier on the table | Presence/absence of parts must be a first-class structural fact |
| R-02 | TTRPG | AD&D 2e humanoid vs monster/animal d10 chart | Two shapes only; foreleg and wing share a row; tail is a location with its own consequences | Small closed tables force merges; tails/wings deserve real nodes |
| R-03 | TTRPG | WFRP reversed-d100 hit location | The attack roll's digits, reversed, give the location (37→73) | Independent confirmation of the Zero-Step idea; a forum post says non-humanoid body types are handled by separate RuneQuest tables, i.e. outside the core method |
| R-04 | TTRPG | HarnMaster-style and forum d100 tables | Finer d100 tables allocate percentages to skull, face, neck, shoulder, etc.; odd=left/even=right is a widespread folk convention | Allocation is a design choice; parity laterality is familiar |
| R-05 | TTRPG | D&D/Pathfinder creature types | Types classify origin/nature; the "Beast" group alone spans crab, bat, octopus, scorpion, spider, snake, shark | Frame must be chosen by **anatomy**, not creature type |
| R-06 | Video game | RimWorld body defs | Parts have parent, coverage relative to parent, external/internal, mirrored flag, apparel coverage groups; loader warns when child coverage swallows the parent | Separate geometry from coverage; ship a validator |
| R-07 | Video game | Dwarf Fortress raws | Body structure, body-detail plans (materials, positions, relative sizes) and creature variations (templated deltas) are separate object types | Topology / proportions / variation as separate layers |
| R-08 | Video game | Monster Hunter parts | Named parts are breakable/severable; consequences track function (wings→flight, tail→reach/poison, head→special attack) | Attach consequences to function roles |
| R-09 | Game research | Spore animation (Hecker et al. 2008) | Motion authored in a morphology-independent form using semantic information, retargeted to any body | Rules written once against roles work on any body |
| R-10 | Academic | Sims 1994 evolved creatures | Morphology as a directed graph that reuses instructions for repeated/recursive parts, with recursion limits and a terminal-only flag | Modules + instance counts + depth limits |
| R-11 | Biology | Body-plan definition; bilateral vs radial symmetry; cephalization; metamerism; tagmata | Body plan = integrated morphological/developmental traits; segments group into functional tagmata (head/thorax/abdomen; prosoma/opisthosoma) | Frames per plan; serial and radial symmetry as modes; tagma-style Tier-1 zones |
| R-12 | Biology | Limb modules (stylopod/zeugopod/autopod) | Tetrapod limbs share a three-part proximal→distal pattern through serial homology | One generic limb module reused for arm/leg/foreleg/hindleg |
| R-13 | Academic | Uberon (Mungall et al. 2012) | Species-neutral anatomy with part-of relations so that a query on a structure also covers its substructures | Partonomy tree; parent covers children |
| R-14 | Academic | Schlosser & Wagner 2004 modularity | Modules match adaptive functions; colonial individuals can themselves be modules | Modules by function; swarms are a distinct case |
| R-15 | Biomechanics | Segment-mass models (Dempster, Zatsiorsky) | Segment fractions differ noticeably between methods and segment definitions differ | No single "true" proportion — declare allocation basis |
| R-16 | Mathematics | Apportionment (Hamilton / largest remainder) | Integer allocation that sums to the total; known paradox when the total changes | Deterministic width apportionment with pins and diff-check |

### 3.2 Convergent lessons

| ID | Lesson | Becomes |
|---|---|---|
| L1 | Topology and proportions are different objects | Frame vs Profile (§4) |
| L2 | Anatomy is a part-of tree with inference | Nesting invariant, parent coverage |
| L3 | Repeated parts are instances of one module | Modules, `serial`/`radial` modes |
| L4 | Rules should key on function, not part names | Role vocabulary (§5.3) |
| L5 | Paired/mirrored is a property, not extra nodes | Symmetry modes (§5.2) |
| L6 | Real authoring errors are catchable by validators | V-01…V-20 (§9) |
| L7 | Variants are templated deltas | DERIVE (§6) |
| L8 | Coverage is a layer over geometry | Registration layer (§5.4) |
| L9 | Proportion sources disagree | Declared allocation basis + Profile IDs |
| L10 | Closed 2–3-shape tables do not scale | Frame catalogue (§7) |
| L11 | Creature type ≠ body plan | Classifier by anatomy (§7.1) |
| L12 | Integer partition needs a deterministic method | AP-1 (§8.3) |

## 4. Architecture: Frame + Module + Profile + Overlay

```text
CREATURE TEMPLATE (instance) = Frame ⊕ Module attachments ⊕ Profile ⊕ Overlays ⊕ Registrations

Frame      topology skeleton for one body plan        (no numbers)   → §7, App. B
Module     reusable subtree kit for a slot            (no numbers)   → §5.5
Profile    width classes / pins → intervals           (ONLY numbers) → §8
Overlay    roles, tags, registrations                 (no geometry)  → §5.6
Null frame "locations: none" for swarms/incorporeal                   → F-NULL
```

**Design rules**

| Rule | Text |
|---|---|
| A-1 | Geometry (nodes) and coverage (registrations) are separate; armour never creates nodes. |
| A-2 | Overlays cannot change geometry. Anything that adds/removes a node is a DERIVE. |
| A-3 | Widths exist only in Profiles. Frames and Modules are number-free. |
| A-4 | Every creature template is an *individual instance* (own Profile, own ID) even when it reuses a Frame (preserves DEC-041(5) in letter; AMEND-2 records the residual tension). |
| A-5 | Roles are descriptive-only in this proposal; any Effect consuming a role needs its own ruling. |
| A-6 | Depth is a budget, not a rule: a shallow template is fully legal (DEC-137 fork 1 saturation). |

## 5. Schema

### 5.1 Node record

| Field | Type | Req | Meaning | Validator |
|---|---|---|---|---|
| `id` | dotted path string | Y | Unique, e.g. `torso.chest.heart` | V-12 |
| `label` | text | Y | Display name | — |
| `parent` | id | Y (root: null) | Part-of link | V-02 |
| `order` | int | Y | Canonical sibling position (§5.7) | V-06 |
| `sym` | enum §5.2 | Y | Laterality/ordinal mode | V-07–V-10 |
| `roles` | set §5.3 | Y | Function labels (or `none`) | V-11 |
| `count` | int ≥ 1 | if serial/radial | Instances n | V-10 |
| `pin` | int | opt | Ruled fixed width | V-15 |
| `width_class` | enum §8.1 | Profile only | Ordinal proportion | V-16 |
| `interval` | [lo, hi] | Profile output | Concrete states | V-01–V-03 |
| `notes` | text | opt | — | — |

### 5.2 Symmetry modes

| `sym` | Meaning | Side/ordinal source | Notes |
|---|---|---|---|
| `midline` | Single structure on the axis | Parity computed then **discarded** (DEC-137 convention) | Heart, spine, skull |
| `paired` | Node stands for both sides; inherited by descendants | Parity of Zero-Step output (odd L, even R) | Arms, legs, wings, eyes |
| `serial` | Ordered repeats along the body axis | Each repeat owns its own interval; **no parity** | Body segments, tail segments, leg pairs along a thorax |
| `radial` | n repeats around a central axis | Each ray owns its own interval; **no parity** | Starfish rays, octopus arms, eyestalks |
| `none` | No laterality identity | Parity ignored | Amorphous zones (as ruled for Blood Man pseudopods, DEC-149 R5) |

Descendants of a `paired` node inherit `paired` unless declared `midline`, `serial`, `radial` or `none`.

### 5.3 Role vocabulary (descriptive only)

| Role | Meaning | Possible future consumer (NOT proposed) |
|---|---|---|
| `structural` | Frame/limb support | Break/Sunder-type outcomes |
| `vital-core` | Organ/system the plan treats as life-critical (heart, brain, power core, nucleus) | Critical Location (DEC-023.A). Does **not** drive incapacitation (DEC-053). |
| `sensory:sight` / `:hearing` / `:smell` / `:other` | Sense organ | Blinded/Deafened-type Effects |
| `feeding` | Mouth, jaw, beak, mandible, proboscis | — |
| `respiration` | Lungs, gills, tracheae | — |
| `locomotion:ground` / `:air` / `:water` / `:climb` / `:burrow` | Movement organ | Trip, Cripple Limb, Prone/Slowed targeting |
| `manipulation` | Can hold/grip items | Disarm/Break Hold, Equipment Damage (DEC-114 R2 `state:held`) |
| `natural-weapon` | Claw, fang, horn, stinger, tail club, breath origin | — |
| `balance` | Tail, fins, counterweights | Trip resistance content |
| `sessile-anchor` | Root, holdfast | — |
| `special:<id>` | Content-authored (e.g. `special:ice-gland`) | Content only |
| `none` | Explicitly none | — |

Rationale (R-08, R-09): consequences follow function; roles let one future rule serve every body.

### 5.4 Registration layer (coverage over geometry)

```yaml
registrations:
  - node: torso            # covers descendants (L-007/L-012)
    tag: defense:armor
    source: innate         # innate | worn
    cond: null             # e.g. "env:freezing" per DEC-088
```

Rules: register on the set of covered nodes (**positive registration**, DEC-149 R4(a)); no "except" grammar; unlisted nodes are uncovered; a child registration adds to, never removes, parent coverage.

### 5.5 Modules and slots

**Slot record:** `{slot_id, accepts:[module_kind], count:(min,max)|n, sym, attach_to:node_id, promote: default|tier1|nest}`.

**Module catalogue (names only; variants in brackets).**

| Module | Kind | Inner structure | Default sym | Default roles |
|---|---|---|---|---|
| M-HEAD | head | Cranium/Skull; Face{Eyes, Ears (optional/foldable), Nose/Snout, Jaw/Mouth [jaw+teeth \| beak \| mandibles \| proboscis \| oral tentacles]} | midline (eyes/ears paired) | sensory:*, feeding |
| M-NECK | neck | Throat; Nape | midline | structural |
| M-CORE-VERT | core | Chest{wall, Heart, Lungs}; Abdomen{wall, Stomach, Liver, Intestines, Kidneys}; Pelvis; Spine | midline (Lungs, Kidneys paired) | vital-core, respiration |
| M-CORE-ARTH | core | Ganglia; Dorsal vessel; Gut; Respiratory organs | midline | vital-core |
| M-CORE-CEPH | core | Mantle wall; Hearts; Gills; Ink sac; Brain | midline | vital-core, respiration |
| M-CORE-CONSTRUCT | core | Chassis; Power core; Joints | midline | vital-core (core only) |
| M-CORE-AMO | core | Nucleus/vacuole; Membrane | none | vital-core |
| M-LIMB-TETRA | limb | Proximal seg; Joint; Middle seg; Joint; Distal{Palm/Sole; Digits n [claws]} [arm \| foreleg \| hindleg \| digitigrade leg] | paired | manipulation *or* locomotion:ground |
| M-LIMB-ARTH | limb | Basal joint; Proximal; Middle; Distal/Tarsus; Claw | paired or serial-of-pairs | locomotion:ground/climb |
| M-WING-VERT | appendage | Shoulder; Proximal arm; Forearm/Manus; Flight surface [feather \| membrane] | paired | locomotion:air |
| M-WING-INS | appendage | Wing root; Wing/elytron | paired | locomotion:air |
| M-TAIL | appendage | Base; Mid (serial k optional); Tip [plain \| club \| stinger \| fan \| spikes] | midline | balance, natural-weapon (tip variants) |
| M-CEPH-ARM | appendage | Base; Shaft; Tip | radial | manipulation, locomotion:water |
| M-PSEUDOPOD | appendage | Base; Shaft; Grasping tip | none | manipulation |
| M-FIN | appendage | Base; Ray/membrane | paired or midline | locomotion:water, balance |
| M-CHELA | appendage | Palm/carpus; Fixed finger; Movable finger | paired | manipulation, natural-weapon |
| M-STALK | appendage | Base; Shaft; Terminal organ [eye \| mouth] | radial or serial | sensory or feeding |
| M-SEG-SERIES | series | k regions (anterior/mid/posterior…), each {plates; optional limb-pair} | serial | locomotion |
| M-CROWN / M-TRUNK / M-ROOT-SYS | plant | Foliage, fruiting bodies, branch stubs / outer layer, core / taproot, laterals, holdfast | none/radial | sessile-anchor |

### 5.6 Overlays

| Overlay | Effect | Constraint |
|---|---|---|
| O-NONVITAL | Replace `vital-core` with `none` on all nodes (skeletal, zombie-type) | Descriptive only; DEC-052/053 unchanged |
| O-CORE-SWAP | Substitute the core module kind (construct, ooze) | Substitution keeps interval budget of the core container |
| O-INNATE-ARMOR | Adds registrations (§5.4) with optional DEC-088 condition | Positive registration only |
| O-TISSUE | Retags materials (bark, chitin, scale) as metadata | No geometry |
| O-SIZE | Sets a DEC-080 size Tag | Descriptive; new size Tags need a DEC-080 T1 ruling |

### 5.7 Canonical sibling ordering (default for new templates)

1. Tier-1 zones ordered inferior→superior (upright) or posterior→anterior (horizontal) — Human v1 does this at Tier 1 (Legs, Torso, Arms, Head).
2. Within an appendage: proximal→distal, internal/self leaf last (Human v1 limbs comply).
3. Within an axial zone: caudal→cranial or as authored, with `order_reason` if it deviates. Human v1's Torso (Chest, Neck, Abdomen, Pelvis, Groin, Spine) is an accepted exception.

Purpose: nearby LI values map to nearby anatomy and drafters produce comparable trees.

## 6. Composition operators

| Op | Signature | Effect | Preconditions / postconditions |
|---|---|---|---|
| INSTANTIATE | `(frame) → template` | Creates tree, no widths | Frame valid |
| ATTACH | `(module, slot, count?, variant?, sym?)` | Grafts subtree | V-12; `count` respects slot cardinality |
| MULTIPLY | `(module, n, mode)` | n ordinal instances (`serial`/`radial`) | Each instance owns an interval; per-instance state (severed head) is a Wound/Effect matter, not template |
| PROMOTE / NEST | `(module_instance)` | Module becomes a Tier-1 zone or nests under nearest zone | Default rule R-PROMOTE: promote if it carries a primary `locomotion:*` or `natural-weapon` role **and** (the designer flags it **or** its Profile class is ≥ `Broad`); otherwise nest under the zone that holds its slot. Designer sign-off per creature (the stored Dragon's Wings zone is the precedent) |
| DERIVE | `(template, deltas[])` | Variant creature | Deltas ∈ {add-node, remove-node, retag, re-class, swap-variant, add/remove-registration}. Only the affected sibling group is re-apportioned; every unaffected interval is preserved bit-for-bit |
| MERGE | `(frameA.part, frameB.part, junction)` | Hybrid (centaur, naga) | One root, one head; Tier-1 set = union; widths rebased with REBASE |
| REBASE | `(node, new_width)` | Rescales a subtree | AP-1 with old widths as weights |
| COLLAPSE | `(node)` | Node becomes leaf | Depth budget for minions |
| INTERPOLATE | `(profileA, profileB, t)` | Ordinal blend of two profiles of the **same frame** | Profile-level only; DEC-149 R7 requires Tiwa sign-off per sibling family |

**Depth budget (advisory):** minions D1 (Tier-1 only); standard creatures D2–D3; featured creatures to leaf depth. Human v1 reaches address depth 4.

## 7. Frame catalogue and skeletons

### 7.1 Classifier (apply top to bottom)

| # | Test | → Frame |
|---|---|---|
| 1 | Location meaningless (swarm, gas, incorporeal)? | F-NULL |
| 2 | Single fluid mass, no persistent limbs? | F-AMO |
| 3 | Sessile, rooted? | F-SESS |
| 4 | ≥ 3 rays around a central axis, no forward end? | F-RAD (F-CEPH if a mantle-head with arms) |
| 5 | Serial repeated segments dominate; 0 or ≥ 6 legs? | F-MYR, F-HEX, F-ARA, F-CRU by tagma pattern; F-SER if limbless axial |
| 6 | Finned aquatic vertebrate? | F-PISC |
| 7 | Two locomotor limb pairs, one pair are upright manipulators? | F-BIP |
| 8 | Two locomotor limb pairs, forelimbs wings? | F-AVI |
| 9 | Two locomotor limb pairs, otherwise? | F-QUAD |

Rule: classify by **persistent limb function**, not fiction (an owlbear is F-QUAD unless its forelimbs are treated as upright manipulators). Hybrids use MERGE.

### 7.2 Frame table

| Frame | Nearest DEC-144 class | Default Tier-1 preset (names only) | Key slots | Sym at Tier-1 | Exemplars |
|---|---|---|---|---|---|
| F-BIP | bipedal-humanoid | Legs, Torso, Arms, Head (DEC-100 pins) | head, arm×2, leg×2, opt. tail, opt. wing | paired limbs | human, goblin, orc, troll, giant, skeleton, golem |
| F-QUAD | quadrupedal | Head, Torso, Forelimbs, Hindlimbs (+Tail/Neck/Wings if promoted) | head, neck, tail, fore×2, hind×2, opt. wing | paired limbs | wolf, bear, horse, dragon |
| F-AVI | quadrupedal (nearest; flagged AMEND-1) | Head, Torso, Wings, Legs (+Tail) | head, wing×2, leg×2, tail | paired | eagle, bat, wyvern |
| F-HEX | multi-limbed/segmented | Head, Thorax, Abdomen | head, leg×3 pairs, opt. wings | serial pairs | beetle, ant, wasp, mantis |
| F-ARA | multi-limbed/segmented | Prosoma, Opisthosoma, Legs (order per template) | prosoma appendages, leg×4 pairs | serial pairs | giant spider |
| F-CRU | multi-limbed/segmented | Cephalothorax, Chelae, Abdomen/Tail, Legs | chela×2, leg pairs, tail (stinger opt.) | paired | scorpion, crab |
| F-MYR | multi-limbed/segmented | Head, Body (serial regions), Terminal | seg-series, head | serial | centipede, worm |
| F-SER | multi-limbed/segmented (nearest; AMEND-1) | Head, Body (serial regions), Tail | head, seg-series, tail | serial/none | snake, eel, naga lower |
| F-PISC | multi-limbed/segmented (nearest; AMEND-1) | Head, Trunk, Fins, Tail | fin pairs + midline fins | paired | shark, whale |
| F-CEPH | multi-limbed/segmented | Head-Mantle, Arms, Tentacles | arm×8 radial, tentacle×0–2 | radial | octopus, squid, kraken |
| F-RAD | (new; AMEND-1) | Central Body, Rays | ray×n radial, stalks | radial | starfish, jellyfish, beholder |
| F-AMO | amorphous | Core, Pseudopod field, Surface/Head-analog | pseudopod (none) | none | ooze, Blood Man |
| F-SESS | (new; AMEND-1) | Crown, Trunk/Stem, Limbs/Vines, Roots | crown, trunk, root system | radial/none | carnivorous plant, giant fungus |
| F-NULL | — | none (`locations: none`) | — | — | swarm, ghost, gas |

F-NULL: any location-referencing Effect against it falls back per DEC-030; Tier 0 stays the default (DEC-040).

### 7.3 Skeleton notation (Appendix B)

`node [sym] {roles}`; `P`=paired, `M`=midline, `S×n`=serial, `R×n`=radial, `N`=none. Names only; no widths.

## 8. Allocation Profiles (the numbers-later interface)

### 8.1 Width classes and bases (no numeric values proposed)

| Item | Definition |
|---|---|
| Width classes | Ordinal: `Sliver` < `Narrow` < `Standard` < `Broad` < `Dominant` |
| `weight_map` | Profile parameter mapping classes to weights. **Left unset by this proposal.** |
| Allocation basis (per sibling group, one primary + rationale) | `exposure` (surface/silhouette), `mass`, `targetability` (called-shot difficulty), `vitality-emphasis` (deliberate gameplay weighting), `narrative`, `equal`, `other:<text>` |
| Pins | `pin: n` freezes a width that an existing ruling fixes (e.g. DEC-100 quartiles, all Human v1 numbers) |

Why a declared basis (R-15): published human segment fractions differ by method and segment definition, so no single "true" proportion exists; every profile must say what its numbers represent.

### 8.2 Profile record

```yaml
profile:
  id: PROF-<creature>-<n>
  frame: F-...
  status: candidate            # candidate | accepted (accepted only by Tiwa)
  weight_map: null             # filled at authoring time
  apportion: AP-1
  groups:
    - parent: root
      basis: {primary: vitality-emphasis, rationale: "..."}
      children: [{id: legs, class: Standard}, {id: torso, class: Standard}]
      pins: {}                 # e.g. DEC-100 quartiles for F-BIP
```

### 8.3 AP-1 apportionment (deterministic)

1. Inputs: parent width W, ordered children with weights `weight_map[class]` or pins.
2. Allocate pins; R = W − Σpins; require R ≥ number of unpinned children.
3. Any unpinned child whose quota `R·w/Σw` < 1 receives 1; remove it; repeat.
4. Quota `q_i = R·w_i/Σw` for the remainder; floor each; distribute leftover states to largest remainders; ties → larger weight, then earlier `order`.
5. Emit intervals in canonical order; verify V-01–V-03, V-15, V-17.

**Test vectors (illustrative weights, verified by script):**

| W | Inputs (order) | Output |
|---|---|---|
| 25 | weights 5, 3, 1, 1 | 13, 8, 2, 2 (sum 25) |
| 10 | weights 20, 1, 1 | 8, 1, 1 (sum 10) |
| 25 | pin 10; weights 1, 1, 1 | 10, 5, 5, 5 (sum 25) |

Known limitation (R-16): largest-remainder can shrink one sibling when the parent width grows (Alabama paradox). V-17 therefore emits a **width-diff report** on every re-profile so authors see any such shrink.

## 9. Validation suite (machine-checkable)

| ID | Sev | Check |
|---|---|---|
| V-01 | ERR | Leaf intervals are disjoint and their union is exactly [1, 100] |
| V-02 | ERR | Container interval = union of children; children contiguous in `order`, non-overlapping |
| V-03 | ERR | Every node width ≥ 1 |
| V-04 | INFO | Containers with no self/surface leaf are listed (pattern P-SELF: Human v1 chest wall, "internal" leaves) |
| V-05 | ERR | No leaf at AD 0; Tier-1 zone set non-empty (except F-NULL) |
| V-06 | WARN | Sibling order follows §5.7 or carries `order_reason` |
| V-07 | ERR | Child `sym` is inherited or one of midline/serial/radial/none |
| V-08 | WARN (INFO at Tier-1 zones) | Paired leaf has even width (parity-balanced); single-state paired leaf flagged, waivable by W-137 |
| V-09 | ERR | Midline nodes never emit L/R in formatted addresses |
| V-10 | ERR | serial/radial: n ≥ 2, each repeat own interval, n ≤ container width |
| V-11 | WARN | Every leaf has a role or explicit `none`; frame declares a locomotion role or `sessile` |
| V-12 | ERR | Ids unique; modules attach only to accepting slots within cardinality |
| V-13 | ERR | Every registration references an existing node |
| V-14 | WARN | Tier-1 zone count within 3–6 (derived from stored templates: 4, 4, 4, 4, 4, 4, 4, 3, 6, 3) |
| V-15 | ERR | Pins preserved; Σpins ≤ parent width − (# unpinned siblings) |
| V-16 | ERR | Every container group has classes or pins and a declared basis |
| V-17 | ERR | Regenerating intervals from the Profile reproduces stored intervals; width-diff report attached |
| V-18 | ERR | F-NULL template contains no nodes |
| V-19 | WARN | Any comparison to a reference creature cites a Profile ID (DEC-149 condition 1) |
| V-20 | ERR | A derived template's delta list applied to its parent reproduces it |

**Lint report format**

```text
TEMPLATE <id>  FRAME <F-..>  PROFILE <PROF-..>
V-01 PASS  V-02 PASS  V-03 PASS
V-08 WARN  forearm[61-65] odd width (3 odd / 2 even)
V-08 WARN  waived W-137: ankle[13] single-state paired (side fixed: Left)
RESULT: PASS-WITH-WARNINGS (0 ERR, 2 WARN)
```

## 10. Coverage test

### 10.1 By D&D-style creature type

| Type | Typical frame(s) | Overlays | Note |
|---|---|---|---|
| Aberration | F-RAD, F-AMO, F-CEPH, F-BIP + head variant | O-TISSUE | Anatomy varies by individual |
| Beast | F-QUAD, F-AVI, F-HEX, F-ARA, F-CRU, F-MYR, F-SER, F-PISC, F-CEPH | — | Widest spread (R-05) |
| Celestial / Fiend | F-BIP (+ wings/horns), F-QUAD | O-INNATE-ARMOR | Fiction type, ordinary anatomy |
| Construct | any | O-CORE-SWAP | Core module replaced |
| Dragon | F-QUAD + wings/tail/neck; wyvern F-AVI | O-INNATE-ARMOR | Stored dragon proposal |
| Elemental | F-AMO or F-BIP | O-CORE-SWAP | Judgement call |
| Fey / Giant / Humanoid | F-BIP | O-SIZE | — |
| Monstrosity | MERGE hybrids | varies | Catch-all type |
| Ooze | F-AMO | O-CORE-SWAP | — |
| Plant | F-SESS, or F-BIP + O-TISSUE if mobile | — | — |
| Undead | any | O-NONVITAL; incorporeal → F-NULL | — |

### 10.2 By iconic creature

| Creature | Frame + modules | Overlay |
|---|---|---|
| Wolf, bear, horse, lion | F-QUAD, M-TAIL(short) | — |
| Owlbear | F-QUAD, M-HEAD(beak) | — |
| Centaur | MERGE(F-BIP upper, F-QUAD lower) | — |
| Griffin | MERGE(F-AVI fore, F-QUAD hind), M-WING-VERT | — |
| Harpy | F-BIP + M-WING-VERT (arm-replacing variant) | — |
| Gargoyle | F-BIP + M-WING-VERT | O-INNATE-ARMOR |
| Minotaur | F-BIP, M-HEAD(horned) | — |
| Skeleton / zombie | F-BIP | O-NONVITAL |
| Golem | F-BIP | O-CORE-SWAP(construct) |
| Giant spider | F-ARA, M-LIMB-ARTH ×4 pairs | O-INNATE-ARMOR |
| Giant scorpion | F-CRU, M-CHELA, M-TAIL(stinger) | — |
| Giant beetle / wasp | F-HEX, M-WING-INS | — |
| Giant centipede | F-MYR, M-SEG-SERIES | — |
| Constrictor snake, eel | F-SER | — |
| Naga | MERGE(F-BIP upper, F-SER lower) | — |
| Shark, orca | F-PISC, M-FIN | — |
| Merfolk | MERGE(F-BIP upper, F-PISC tail) | — |
| Giant octopus, kraken | F-CEPH, M-CEPH-ARM ×8 | — |
| Mind flayer | F-BIP, M-HEAD(oral tentacles: M-CEPH-ARM ×4 radial) | — |
| Starfish, jellyfish | F-RAD | — |
| Beholder | F-RAD, M-STALK ×10 radial + central eye | — |
| Ooze, gelatinous cube, Blood Man | F-AMO, M-PSEUDOPOD (optional) | O-CORE-SWAP |
| Treant | F-BIP | O-TISSUE |
| Carnivorous plant | F-SESS | — |
| Hydra | F-SER or F-QUAD + MULTIPLY(M-HEAD+M-NECK, n) | — |
| Cerberus | F-QUAD + MULTIPLY(M-HEAD, 3) | — |
| Swarm, ghost | F-NULL | — |

### 10.3 Gaps (not covered by design)

| ID | Gap | Handling |
|---|---|---|
| G-1 | Shapeshifters | One template per form; no morph operator |
| G-2 | Riders/mounts, symbiotes | Separate creatures |
| G-3 | Mid-fight anatomy changes (regrown heads, detached parts) | Template is static; change is Wound/Effect state |
| G-4 | Colonial creatures with distributed organs | F-NULL or per-unit templates |
| G-5 | Extreme scale differences | Size Tag only; template unchanged |

## 11. Check against the ten stored templates

**Basis and limits.** Human v1 was re-verified from DEC-137 register text; the nine proposals (Ice Troll, Blood Man, Giant Spider, Hobgoblin, Kobold, Troll, Dragon, Goblin, Orc) are assessed only from register annotations. Zone names, per-state values and Appendix tables were not visible. Findings marked (data) were computed; marked (annot.) rest on annotations.

### 11.1 Conformance matrix

| Template | Frame | Tier-1 as recorded | Expressible with no new mechanic? | Notes |
|---|---|---|---|---|
| Human v1 (DEC-137) | F-BIP | 4 zones, DEC-100 quartiles | Yes (data) | Partition of [1,100] passes V-01/V-02 from register text |
| Ice Troll | F-BIP | 4 zones, DEC-100 | Yes (annot.) | Registration at Torso+Arms+Legs, DEC-088 condition; Ice Gland = `special:` node; ears folded |
| Troll | F-BIP | 4 zones, DEC-100 | Yes (annot.) | = DERIVE(Ice Troll, remove Ice Gland, remove conditional registration); DEC-149 R7 policy |
| Goblin | F-BIP | 4 zones, DEC-100 | Yes (annot.) | Profile differences (wider Ears node, dropped Kidney) = profile/remove-node deltas |
| Orc | F-BIP | 4 zones, DEC-100 | Yes (annot.) | 16/9 chest split = profile; no Ears node = remove-node |
| Hobgoblin | F-BIP | 4 zones, DEC-100 | Yes (annot.) | Sibling interpolation = INTERPOLATE (sign-off case-by-case) |
| Kobold | F-BIP | 4 zones, DEC-100 | Yes (annot.) | No innate registration (KB-Q2) |
| Giant Spider | F-ARA | 3 zones, bespoke (45+20+35) | Yes (annot.) | 8 legs = 4 pairs, structural branch × parity; six registrations (Eyes/Spinnerets carved) |
| Dragon | F-QUAD + wing/tail/neck | 6 zones, bespoke | Yes (annot.) | Fore/hind × L/R via parity; wings promoted; positive registration for exceptions |
| Blood Man | F-AMO | 3 zones, bespoke (60/30/10) | Yes (annot.) | Pseudopod `sym: none`; no registrations |

### 11.2 Findings

| ID | Finding | Evidence | Consequence |
|---|---|---|---|
| F-1 | **Stored family is bipedal-heavy:** 7 of 10 are F-BIP; F-QUAD, F-ARA, F-AMO have one each; **10 of 14 frames have no exemplar** | Table 11.1 | Skeletons in Appendix B are desk-checked only; pilot before adopting (Q-6) |
| F-2 | **Odd-width paired zones cannot be parity-balanced.** DEC-100 quartiles have width 25 (13 odd / 12 even), so paired Legs and Arms give Left ≈52% / Right ≈48% at Tier 1 | Computed (data) | Inherent to DEC-100 + DEC-041(3); lint INFO at Tier 1 |
| F-3 | Four Human v1 leaves have odd width: Thigh [1–5] (3 odd/2 even), Lower Leg [8–12] (2/3), Forearm [61–65] (3/2), Femoral/internal [23–25] (2/1) — assuming these are paired leaves | Computed (data) | V-08 WARN; small; cancels partly across a limb |
| F-4 | **Nine single-state paired leaves** in Human v1: Ankle 13 (L); Toes 16–19 (R,L,R,L); Fingers 70–73 (R,L,R,L). Each reaches one side only, as DEC-137 states | Computed (data) | Waiver W-137; the other side needs a qualifier layer or GM Fiat |
| F-5 | Tier-1 zone counts across the family are 3–6 (4×7 bipeds, 3, 6, 3) | Annotations | Supports V-14 range as a *descriptive* norm, not a cognitive-limit claim |
| F-6 | Existing decisions already realise the Frame/Profile split: DEC-137 (Human profile), DEC-144 (per-class Tier-1), DEC-149 R7 (derive vs interpolate) | Register | Framework formalises, does not overturn |
| F-7 | Armour carve-outs (Dragon, Giant Spider) are cleanly expressed as positive registrations over unchanged geometry | Register (DEC-149 R4) | Confirms A-1 |
| F-8 | Human-comparative statements in the proposals predate the adopted DEC-137 allocation | DEC-149 condition 1 | V-19 forces Profile-ID citations |

## 12. Amendment candidates and tensions

| ID | Proposal | Touches | Default recommendation | If rejected |
|---|---|---|---|---|
| AMEND-1 | Extend the DEC-144 class table: add `sessile`, `radial`; split `limbless-axial`; treat frames as pre-ruled defaults | DEC-144 | Adopt as **authoring aid** now; make normative only after a pilot (F-1) | Keep DEC-144 as is; frames stay non-normative |
| AMEND-2 | Shared frame/module library with individual profiles | DEC-041(5) ("individual templates, not a shared scheme") | Treat as compatible (each creature keeps its own instance and profile); ask Tiwa to confirm reading | Frames become documentation only; each creature authored from scratch |
| AMEND-3 | Add `serial`/`radial`/`none` symmetry modes (interval-based ordinal identity) | DEC-041(3), DEC-137 fork 6 | Adopt (extends, does not alter parity) | n-fold limbs must use parity buckets only |
| AMEND-4 | Optional parity-balance fix (parity relative to zone start) | DEC-137 fork 6 | **Do not adopt**; keep lint INFO/WARN (F-2) | — |
| AMEND-5 | Role vocabulary as template-local metadata | DEC-080 T1, DEC-116 | Adopt as local metadata; do not add Tags yet | If wanted as Tags, needs a DEC-080 T1 ruling |
| AMEND-6 | Explicit Null Frame (`locations: none`) | DEC-040, DEC-030 | Adopt (already implied) | Swarms stay undocumented |
| AMEND-7 | AP-1 width apportionment as optional authoring convention | DEC-137 fork 7 (no reserves preserved) | Adopt as optional; pins protect ruled numbers | Authors allocate manually |
| AMEND-8 | R-PROMOTE default for module→Tier-1 | DEC-113 R2 (untouched) | Adopt as default heuristic with per-creature sign-off | Promotion stays ad hoc |
| AMEND-9 | Use "Address Depth" in documentation | DEC-112/137 terminology | Adopt (terminology only) | Keep "Location Tier" |

**Deliberately compatible:** Zero-Step, single-source resolution, full-depth reading, Skill-Tier gate, DEC-113 classes, DEC-100 quartiles, Human v1, parent coverage/fallback, Wound address records.

## 13. Open questions for Tiwa

| ID | Question | Proposed default |
|---|---|---|
| Q-1 | Are frames normative defaults or authoring aids? | Aids until a pilot passes (F-1) |
| Q-2 | Roles as local metadata or `role:`-style Tags? | Local metadata |
| Q-3 | Extend laterality beyond parity to serial/radial? | Yes |
| Q-4 | Keep the parity-balance lint (V-08)? | Yes, WARN/INFO, waivable |
| Q-5 | Standardise AP-1 or leave allocation to authors? | Standardise as optional, with pins |
| Q-6 | Which frames to pilot first? | F-SER (constrictor snake), F-CRU (giant scorpion), F-CEPH (giant octopus) — all appear in a published beast list (R-05) and none is stored |

## 14. Authoring workflow for LLM drafters

| Step | Action | Output |
|---|---|---|
| 1 | Classify by §7.1 (anatomy, not type) | Frame ID (+ MERGE plan if hybrid) |
| 2 | Choose Tier-1 preset; note pins if F-BIP | Zone list |
| 3 | ATTACH modules; set variants, counts, sym; apply R-PROMOTE | Tree |
| 4 | Apply overlays (roles, registrations) | Metadata |
| 5 | Set depth budget | D1–D4 |
| 6 | Build Profile: width class per sibling group, basis, pins | Profile record |
| 7 | Run AP-1 | Intervals |
| 8 | Run V-01…V-20; attach lint report and width-diff | Lint report |
| 9 | State open questions and any comparison with Profile IDs (V-19) | Notes |
| 10 | Emit YAML + provenance header; **do not rule, promote or edit any DEC** | Candidate template |

Hard bans: no new DEC; no changes to ruled numbers; no unstated pins; no Effect rules consuming roles.

## 15. References

| ID | Reference | URL |
|---|---|---|
| R-01 | GURPS Wiki, Hit Location | https://gurps.fandom.com/wiki/Hit_Location |
| R-01 | BRP forum, creature hit-location tables per body shape | https://basicroleplaying.org/topic/951-hit-locations/ |
| R-02 | AD&D 2e hit location chart (humanoid vs monster/animal) | https://discmaster.textfiles.com/file/30444/AD&D Core Rules 2.0 Expansion.iso/webhelp/sm/dd03611.htm?html=true |
| R-03 | BRP forum, WFRP reversed-digit locations | https://basicroleplaying.org/topic/380-hit-location-dice/ |
| R-03 | GiantITP thread on WFRP hit locations | https://forums.giantitp.com/archive/index.php/t-589922.html |
| R-04 | BRP forum d100 table (Harn-derived) | https://basicroleplaying.org/topic/520-do-you-plan-on-using-hit-locations/page/2/ |
| R-04 | ENWorld, second-digit d100 hit locations | https://www.enworld.org/threads/hit-location-options-question.41685/latest |
| R-05 | Roll20 compendium, monsters by creature type | https://roll20.net/compendium/dnd5e/Rules:Monsters%20by%20Creature%20Type |
| R-06 | RimWorld Wiki, Body parts / Body part | https://rimworldwiki.com/wiki/Body_parts |
| R-06 | RimWorld Wiki, Armor layers | https://mail.rimworldwiki.com/wiki/Armor |
| R-06 | Steam thread quoting the BodyDef coverage warning | https://steamcommunity.com/workshop/filedetails/discussion/1106719215/1473095331504795559 |
| R-07 | Dwarf Fortress Wiki, Raw / Body detail plan token | https://dwarffortresswiki.org/index.php/Raw |
| R-08 | Steam Monster Hunter: World, effects of breaking parts | https://steamcommunity.com/app/582010/discussions/0/3007808519559550578 |
| R-09 | Hecker et al., Real-time motion retargeting to highly varied user-created morphologies (SIGGRAPH 2008) | https://chrishecker.com/Real-time_Motion_Retargeting_to_Highly_Varied_User-Created_Morphologies |
| R-10 | Sims, Evolving Virtual Creatures (SIGGRAPH 1994) | https://course.ccs.neu.edu/cs5100f12/resources/reading/sims_creatures.pdf |
| R-11 | Wikipedia, Tagma (biology) | https://en.wikipedia.org/wiki/Tagma_(biology) |
| R-12 | Limb modularity and serial homology (PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC2840520 |
| R-13 | Mungall et al., Uberon (Genome Biol. 2012) | https://pmc.ncbi.nlm.nih.gov/articles/3334586 |
| R-14 | Schlosser & Wagner (eds.), Modularity in Development and Evolution (2004) | https://press.uchicago.edu/ucp/books/book/chicago/M/bo3636976.html |
| R-15 | Segment-parameter model comparison (BMClab notebook) | https://nbviewer.jupyter.org/format/script/github/BMClab/bmc/blob/master/notebooks/BodySegmentParameters.ipynb |
| R-16 | Apportionment / largest remainder and paradox | https://jdawiseman.com/papers/electsys/apportionment.html |

**Evidence caveats.** GURPS, WFRP, RuneQuest/Mythras and Harn material was read through wikis and community threads, not primary rulebooks. One forum claim (a hit-location chart "derived from ATF data") is unverified and not relied on. Wiki-sourced game data (RimWorld, Dwarf Fortress, Monster Hunter) is community documentation.

---

# Appendix A — Example (structure only): Gargoyle = F-BIP + M-WING-VERT + O-INNATE-ARMOR

```yaml
template:
  id: TPL-gargoyle-0
  frame: F-BIP
  modules:
    - {module: M-WING-VERT, slot: wing, attach_to: torso, count: 2, sym: paired, variant: membrane, promote: nest}
  overlays:
    - O-INNATE-ARMOR: [{node: torso, tag: defense:armor, source: innate},
                       {node: arms,  tag: defense:armor, source: innate},
                       {node: legs,  tag: defense:armor, source: innate}]
    - O-SIZE: creature:size_medium
  profile:
    id: PROF-gargoyle-0
    status: candidate
    weight_map: null
    groups:
      - parent: root
        pins: {legs: PIN_FROM_DEC-100, torso: PIN_FROM_DEC-100, arms: PIN_FROM_DEC-100, head: PIN_FROM_DEC-100}
        basis: {primary: equal, rationale: "F-BIP default per DEC-144"}
      - parent: torso
        children: [{id: wing, class: Standard}]   # nested under the slot's zone, not promoted; class only, no number
```

# Appendix B — Blank skeletons (names only, no widths)

```text
F-BIP   [ref. instance: Human v1, DEC-137]
 Legs[P]{loco:ground}: Thigh, Knee, LowerLeg, Ankle, Foot{Toes, Midfoot/Heel[M]}, Internal
 Torso[M]: Chest{wall, Heart, Lungs[P]}, Neck, Abdomen{wall, Stomach, Liver, Intestines, Kidneys[P]}, Pelvis, Groin, Spine
 Arms[P]{manip}: Shoulder, UpperArm, Elbow, Forearm, Wrist, Hand{Digits, Palm/Back}
 Head[M]: Skull, Face{Eyes[P], Ears[P], Nose, Jaw/Teeth}

F-QUAD
 Hindlimbs[P]{loco:ground}: Hip/Thigh, Knee/Hock, Shank, Foot/Paw|Hoof
 Torso[M]: Abdomen, Chest (vital-core), Spine
 Forelimbs[P]{loco:ground|manip}: Shoulder, Upper, Elbow, Lower, Paw|Hoof|Claw
 Neck[M] (nest or promote)   Head[M]: Skull, Face, Jaw
 Tail[M]{balance} (optional)   Wings[P]{loco:air} (optional, R-PROMOTE)

F-AVI
 Legs[P]{loco:ground}: Thigh, Tarsus, Foot{Talons}
 Torso[M]: Breast, Abdomen, Spine (vital-core)
 Wings[P]{loco:air}: Shoulder, Arm, Manus, Flight surface
 Head[M]: Skull, Face{Eyes[P]}, Beak{feeding}   Tail[M]{balance}

F-HEX
 Abdomen[M]: Segments (S×k), Respiratory
 Thorax[M]: Leg pairs (S×3){loco:ground}, Wing pairs (opt.){loco:air}, Core
 Head[M]: Capsule, Eyes, Antennae[P], Mandibles[P]{feeding}

F-ARA
 Opisthosoma[M]: Abdomen wall, Vessel, Respiratory, Spinnerets
 Prosoma[M]: Carapace, Brain/ganglia (vital-core), Eyes, Chelicerae[P]{feeding, natural-weapon}, Pedipalps[P]
 Legs[S×4 pairs, P]{loco:ground|climb}: Proximal, Middle, Tarsus, Claw

F-CRU
 Tail/Abdomen[M]: Segments (S×k), Telson|Stinger{natural-weapon}
 Cephalothorax[M]: Carapace, Core (vital-core), Eyes, Mouthparts{feeding}
 Chelae[P]{manip, natural-weapon}: Carpus, Fixed finger, Movable finger
 Legs[S×n pairs, P]{loco:ground}

F-MYR
 Terminal[M]: Tail segments|Stinger
 Body[S×k regions]: {plate, limb-pair (opt.){loco}}
 Head[M]: Capsule, Sensors, Mouth{feeding}

F-SER
 Tail[M]{balance}: Base, Tip
 Body[S×k regions]{loco:ground|water}
 Head[M]: Skull, Eyes[P], Jaw{feeding}

F-PISC
 Tail[M]{loco:water}: Peduncle, Caudal fin
 Trunk[M]: Flank, Belly, Core (vital-core)
 Fins[P & M]{loco:water|balance}: Pectoral, Pelvic, Dorsal, Anal
 Head[M]: Skull, Eyes[P], Gills[P], Jaw{feeding}

F-CEPH
 Tentacles[R×0–2]{manip}: Base, Shaft, Club
 Arms[R×8]{manip, loco:water}: Base, Shaft, Tip
 Head-Mantle[M]: Mantle wall, Core (vital-core), Eyes[P], Beak{feeding}, Siphon

F-RAD
 Rays[R×n]: Base, Shaft, Tip {loco|manip}
 Central body[N]: Disc, Core (vital-core), Oral surface{feeding}, Sensors

F-AMO
 Surface/Head-analog[N]: Membrane, Sense cluster|Head-clot
 Pseudopod field[N]{manip}: Base, Shaft, Grasping tip
 Core[N]: Nucleus (vital-core), Bulk

F-SESS
 Roots[R]{sessile-anchor}: Taproot, Laterals, Holdfast
 Trunk/Stem[N]: Outer layer, Core
 Limbs/Vines[R|S]{manip (opt.)}: Base, Shaft, Tip
 Crown[N]: Foliage, Fruit/spore bodies

F-NULL
 locations: none   (Tier 0 default; DEC-030 fallback for location-referencing Effects)
```

# Appendix C — Change log for this document

| Version | Date | Note |
|---|---|---|
| v0.1 | 2026-09-21 | First proposal draft. No DEC assigned. |

**End of document.**
