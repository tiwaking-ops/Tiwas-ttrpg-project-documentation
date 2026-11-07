---
document:
  title: "Tiwas — S-17 Setting Modules: Architecture Contract, Reference Setting (Fantasy), Content-Integration Pipeline, Six-Setting Stress Test"
  version: "0.1"
  status: "Advisory / Non-canonical. No DEC assigned. Committed design draft: every default below is a recommendation awaiting Tiwa's ruling. Confers no authority; promotes, demotes and supersedes nothing."
  purpose: >
    Completes the S-17 requirement (Setting architecture and content integration) as one committed draft with
    recommended defaults pre-filled: (A) architecture contract, (B) reference setting, (C) content-integration
    pipeline, (D) stress test against the six settings named in Proposals §18, (E) work plan and acceptance criteria.
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-20"
  last_modified_date: "2026-09-20"
  ruleset_pin: "Canonical Rules & Changelog (file v1.3, internal v1.4) + Decision Register through DEC-154 (register header 2026-09-20)"
  suggested_repo_path: "investigations/tiwas-s17-setting-modules-proposal-v0.1-2026-09-20.md"
---

# Tiwas — S-17 Setting Modules (Committed Draft v0.1)

# 0. Governance and Reading Guide

| Item | Statement |
|---|---|
| Authority | None. Canonical Rules govern; this draft is design exploration (Proposals §0/§21; LLM Governance Rules 1–16). |
| Promotion | Not sought. Any promotion requires the 8-step Promotion Rule (REQ-021). |
| DEC inference | None. No DEC number is assigned or implied. |
| Source precedence | Where Proposals v1.4.3 / Roadmap v1.4.3 conflict with the Decision Register, the register is treated as operative (both documents pre-date DEC-050 onward). Flagged as [GUESS-2]. |
| Evidence labels | **[DEC-n / Canonical §n]** = cited ruling or locked text. **[REC]** = recommendation of this draft. **[GUESS-n]** = assumption listed in §10. **[OPEN]** = unruled gap; not filled here (LLM Rule 6). |
| Formula changes | None proposed. See §11. |

---

# 1. Scope and Label Mapping

The label "S-17" has no corpus definition. The Roadmap S-series ends at S-12. [GUESS-1]

| Item | Corpus location | Status |
|---|---|---|
| Setting Modules design direction | Proposals §17 | Design Direction |
| Six named settings | Proposals §18 (Fantasy, Science Fiction, Modern, Horror, Historical, Cinematic) | Listing only |
| Setting Interface | Roadmap Phase 12 (§19); U-22 "Isolate setting rules" | Non-canonical implementation guidance |
| Acceptance criterion | Roadmap §19/§22: "A new setting can be implemented without modifying the Core Engine." | Non-canonical |
| Magic / special abilities | Canonical §15 (Reserved); DEC-114 R3; DEC-146 R1–R10 | Reserved; rulings non-canonical |
| Content authorship | DEC-077, DEC-077.A, DEC-084, DEC-137, DEC-149 | Non-canonical rulings |

**Deliverables**

| ID | Deliverable | Section |
|---|---|---|
| D-A | Architecture contract (layers, rule classes, manifest, rules, composition, conformance suite, lifecycle) | 4 |
| D-B | Reference setting: Fantasy manifest instance from existing corpus content | 5 |
| D-C | Content-integration pipeline (routes, stages, primitive mapping, provenance) | 6 |
| D-D | Stress test against all six §18 settings, with blocker register | 7 |
| D-E | Work plan, acceptance criteria, pre-filled defaults, guess register | 8–10 |

---

# 2. Definitions

| Term | Definition |
|---|---|
| Setting Module (SM) | A declarative package that adds vocabulary, records, parameters and guidance above Core + Universal Play. Contains **no resolution logic**. |
| Setting Content | Instances authored under an SM: creature templates, Location Templates, items, recipes, hazards, scenarios. |
| Manifest | The SM's single top-level declaration (§4.3). |
| Primitive | An existing ruled construct: Core Test, S-1 contest, StateRecord (Tag/Effect/Condition, DEC-115/117), Extended Test, Location Template, Item record (DEC-128 Q1). |
| Rule Class L / F / T / E / U | Locked / Fixed / Tunable / Extension / Unruled (§4.2). |
| World module / Overlay module | `kind: world` defines a fictional world's content; `kind: overlay` adds tone or content usable on any world (§4.5). [REC] |
| Conformance Card | Per-record checklist proving the record is expressible in existing primitives (§4.6). |
| Ruleset pin | The Canonical version and register cutoff a module was validated against. |
| Blocker | An unruled gap (Class U) that stops a requested capability from being table-ready. |

---

# 3. Binding Constraints

| ID | Constraint | Source |
|---|---|---|
| C-01 | Core invariants 1–18 bind every subsystem | Canonical §16; DEC-016 |
| C-02 | Core Test Transaction (9 steps) may not be replaced | Canonical §6; Invariant 18 |
| C-03 | No competing primary resource or progression economy | Invariant 17; DEC-117 R6 |
| C-04 | Overflow immutability | DEC-007.A |
| C-05 | Skills never require Tags; no Skill-side tag/category system | DEC-025; DEC-117 R7 |
| C-06 | Tags are vocabulary-only unless a ruling supplies numeric fields | DEC-116 R1–R2 |
| C-07 | Effects: one per win; no DoT; no Advantage/Disadvantage language; no natural-roll modification; no new pools | DEC-024; DEC-023.A |
| C-08 | Location-referencing Effects require Skill-Tier ≥ 2 promoting roll | DEC-041 (1)/(6) |
| C-09 | Time/Action expressed only as Skill-side or Movement penalty; no action-point pool | DEC-082; DEC-138 |
| C-10 | No skip-the-roll / Stakes Gate | DEC-051 |
| C-11 | GM Fiat is universal in scope but never overrides Overflow immutability, Cost = natural roll, HP = 0 incapacitation, or the no-DoT policy | DEC-130 |
| C-12 | Content authorship: Tiwa authors/accepts; advisory models draft candidates; conversions are provisional | DEC-077, DEC-077.A, DEC-137, DEC-149 |
| C-13 | Conversion method: derived stats via DEC-004/005; no source damage dice, Dodge/Parry or DR imported | DEC-085 |
| C-14 | `magic:` / `ability:` namespaces reserved with zero entries; starter vocabulary deferred | DEC-114 R3; DEC-146 R7 |
| C-15 | Duration constants, band↔hex boundaries, and similar numeric constants are content-authoring, not ruled numbers | DEC-145; DEC-133.A R1 |
| C-16 | Setting must not redefine d100, roll-under, 100-Fumble, Cost = Roll, Overflow → HP, Failure XP, Skill Roll Pool, Advanced Skill construction, Core recovery | Proposals §17; Roadmap §19 |
| C-17 | Equipment subsystem remains Reserved; wealth, loadout, ranged/ammunition, starting equipment unruled | DEC-081.A (Open 3); Proposals §13 |
| C-18 | LLMs never silently resolve open forks; never infer numbers from examples | Roadmap §24 Rules 5–6 |

---

# 4. Part A — Architecture Contract

## 4.1 Layer model

```text
CORE (Canonical §2–§13, §14.1–§14.2, §14.7; Invariants 1–18)
  ↓
CORE TEST TRANSACTION (Canonical §6)
  ↓
UNIVERSAL PLAY (S-1…S-12 rulings; Conditions; Tags; Effects; Time/Action; Equipment; Hazards)
  ↓
SETTING MODULE  (manifest: vocabulary + parameters + guidance)      ← S-17
  ↓
SETTING CONTENT (records + scenarios)
```

**Direction rule:** references flow downward only. A lower layer never edits, overrides or deletes an upper layer. [REC; Proposals §1.3/§17]

## 4.2 Rule classes (what a setting may touch)

| Class | Meaning | Members | Setting may |
|---|---|---|---|
| **L** — Locked | Canonical Rules | d100/100-Fumble/Doubles/rounding (§2); 24-attribute matrix (§3); derived stats (§4); Skill Tier/Cap/Start (§5); Test Transaction (§6); Cost/Overflow (§7); Recovery (§8); Failure XP, Skill Roll Pool, General XP (§9–§11); Advanced Skills (§12); S-1 (§13); Zero-Step (§14.1–§14.2); §14.7; Invariants 1–18 | Nothing |
| **F** — Fixed | Every ruled (non-canonical) mechanic or value that is **not** listed in Class T. Load-bearing examples: DEC-007.A, DEC-023.A prohibitions, DEC-024, DEC-025, DEC-041 gate, DEC-044/048 (Active Defense as post-hoc mitigation), DEC-051, DEC-052, DEC-063 structure, DEC-078 (capacity `floor(HP/6)`, bands, penalties), DEC-082, DEC-100 (for bipedal-humanoid), DEC-103/104, DEC-115 (`Z = −Y`), DEC-117 R6 | Nothing [REC; GUESS-3] |
| **T** — Tunable | Parameter explicitly delegated to content-authoring (§4.2.1) | Listed below | Set a value citing the delegating ruling, or leave unset |
| **E** — Extension | Additive vocabulary and records | Tags, Conditions, Effects, templates, items, recipes, hazards, scene-state Tags, reaction triggers, alias and naming catalogs | Add, subject to a Conformance Card and Tiwa's acceptance |
| **U** — Unruled | Gap with no ruling (§7.4) | B-01…B-14 | Nothing; declare in `open_gaps`; escalate |

### 4.2.1 Class T — delegated tunables

| Parameter | Delegating ruling | Value form | Behaviour if unset |
|---|---|---|---|
| Band↔hex boundaries for Engagement / Short / Medium / Far | DEC-133 (4); DEC-133.A R1 | Hex counts per band | GM discretion (DEC-130) |
| Prone crawl base fraction (clamp `max(1, …)` is ruled and fixed) | DEC-125 | Fraction of Movement Speed | Session standard `max(1, floor(MS/2))` |
| Base durations per category (combat, social, crafting, travel, healing, downtime) | DEC-145 (1)–(7) | Per-category constants | GM discretion; automated runs use the DEC-145 (9) conversion convention |
| Travel constants (band hex-count; `k` in `Duration = NaturalRoll × k`) | DEC-145 (4)(5) | Numbers | Unset |
| Extra-spend conversion rate (Option M) | DEC-145 (8) | One tunable | Unset |
| Reaction trigger menus; `reaction:*` grants per creature/class/equipment | DEC-132.A R1; DEC-132.B R3 | Trigger lists | None defined |
| ZoC posture list | DEC-152 R1 | Posture Tags/conditions | None defined |
| Regeneration / Regrowth heal value and cadence | DEC-110 | Per creature | None |
| Creature signature-skill values (full-Cap veteran) and pre-authored Tier-2 skills | DEC-086; DEC-087 | Per creature | n/a |
| Location Templates: Tier-1 split per body-plan class, Tier-2+ trees, 100-state allocation | DEC-112 L-004; DEC-137; DEC-144 | Per creature type | Body-plan default (§6.3 row 20) |
| Scene-state `env:` Tag sets per zone | DEC-088; DEC-088.A | Tag set | No `env:` Tag active |
| Hazard Intensity lookup tables | DEC-093 | Key → predefined parameters | None |
| Item mass (kg); Item Tier / Magnitude at creation | DEC-078 R1; DEC-128 Q1; DEC-129 | Numbers | n/a |
| Recipes: `min_skill_tier`, inputs, tool Tags | DEC-142; DEC-141 | Per recipe | Gate 1 |

**Not tunable although it looks like it:** difficulty-grade numeric values (DEC-063 rules named tiers with fixed additive modifiers but the corpus supplies no numbers → Class U, B-11); Encumbrance bands and penalties (ruled, Class F).

## 4.3 Setting Manifest schema

```yaml
setting_module:
  id: <slug>                       # unique across modules
  kind: world | overlay
  version: <x.y.z>
  status: "Advisory / Non-canonical — working content"   # only permitted value until REQ-021 completes
  requires: [<module id>, ...]     # overlay: a world module, or none
  provenance: {author_llm, assessor_llm[], last_modified_by_llm, created_date, last_modified_date}   # per governance/provenance.md; unknown = "not established"
  authority: {designer: "Tiwa", acceptance_refs: [<DEC or ruling record>]}
  ruleset_pin: {canonical: "v1.4", register_through: "DEC-nnn"}
  conformance: {invariants_1_18: attested, suite_results: {SC-01: pass|fail, ...}}
  vocabulary:
    tags:        [{id, namespace, scope: <module id>, meaning, numeric: none | <ruling ref>}]
    conditions:  [{id, record: StateRecord, expression: skill_side | movement_overlay, stacking: add_replace | highest_only, removal_routes: [...], card: <ref>}]
    effects:     [{id, tier_placement, gating: {tag, location, skill_tier}, fallback: DEC-030, card: <ref>}]
    aliases:     [{label, maps_to: <Tier-1 lineage | Advanced formula>, mechanical_weight: none}]
    naming_catalog: [{base_lineage, added_attribute, label}]   # descriptive only (DEC-146 R1 Option 2)
  permissions: [{lineage, grants: <descriptive text>, gate: none}]   # DEC-025; DEC-146 R2
  content: {creatures: [...], location_templates: [...], items: [...], recipes: [...], hazards: [...], scenarios: [...]}
  tunables: [{param, value | unset, delegating_ruling}]
  guidance: {difficulty_grade_usage, gm_fiat_posture, tier_promotion_patterns}   # non-binding
  open_gaps: [{gap_id, description, escalated_to: "Tiwa"}]
```

## 4.4 Setting Rules (S-R)

| ID | Rule | Basis |
|---|---|---|
| S-R1 | **Additive only.** A module adds records; it never overrides, deletes or reinterprets a Class L/F rule. | C-16; DEC-130 |
| S-R2 | **No new resolution.** Every setting mechanic is expressed as an existing Core Test, S-1 contest, StateRecord, Extended Test, Location Template or Item record. | Invariant 18; C-02 |
| S-R3 | **No new pool.** No currency-, mana-, sanity-, luck- or fate-style counter that is spent or refilled. Such concepts must map to PE/MP/HP or to StateRecords. StateRecords never modify pools. | Invariant 17; DEC-117 R6; DEC-135 precedent; DEC-146 (Corruption not adopted) |
| S-R4 | **No Skill gating.** No Skill record carries `requires_tag`; permissions are descriptive. | DEC-025; DEC-146 R2 |
| S-R5 | **Natural roll untouched.** Setting modifiers act Skill-side (DEC-063/064) or as Movement overlays (DEC-138). | Invariants 1, 6 |
| S-R6 | **Tags default vocabulary-only.** A numeric Tag requires a cited ruling. | DEC-116 |
| S-R7 | **Location-referencing content obeys the DEC-041 gate** and DEC-112/144 templates. | C-08 |
| S-R8 | **Effect additions carry a Conformance Card:** tier placement, gating, DEC-030 fallback, one-Effect-per-win, no DoT, no Advantage language. | C-07 |
| S-R9 | **Condition additions use the template:** `Tier-Y Condition Value Z` (`Z = −Y`); Skill-side or Movement-penalty expression only; stacking from {add/replace, highest-only}; removal via existing routes (Effect Heal System, rest/recovery, removal Effect). | DEC-079; DEC-082; DEC-121; DEC-135.A |
| S-R10 | **Unruled gaps are declared, not filled.** Each Class U dependency appears in `open_gaps`. | C-18 |
| S-R11 | **Setting-scoped Tag ids.** New Tags carry `scope: <module id>`; entry into the standing vocabulary requires a Tiwa ruling (DEC-080 T1 precedent: DEC-088, DEC-114 R4, DEC-132.B). | [REC; F-2] |
| S-R12 | **Provenance mandatory** on every module and record; status never "Canonical". | governance/provenance.md |

## 4.5 Composition model [REC; F-3]

| ID | Rule |
|---|---|
| CP-1 | A campaign binds Core + exactly one **world** module + zero or more **overlay** modules. |
| CP-2 | Vocabulary and content compose as an additive union. |
| CP-3 | An id collision is an error; there is no silent override. |
| CP-4 | Class T conflicts resolve only by an explicit, logged `override` in the later module, and only for Class T parameters. Any other conflict is an error. |
| CP-5 | An overlay's `requires` must be satisfied at load. |
| CP-6 | Every record is self-contained: no record's meaning may depend on another module's unpublished content. |

## 4.6 Conformance suite

**Conformance Card (per record):** record id · primitives used · Class L/F untouched (Y/N + cite) · natural roll untouched · no pool created · no Skill gated · Effect fields (tier, gate, fallback) · expression (Skill-side / Movement) · provenance · authorization route.

| ID | Test | Pass condition |
|---|---|---|
| SC-01 | Core diff | Module load produces zero edits to `canonical/` and Core rules text |
| SC-02 | Invariant attestation | Each of Invariants 1–18 has a mechanical check, all pass |
| SC-03 | Phase 0 regression | Roadmap §7/§21 suite passes unchanged with the module loaded |
| SC-04 | No new pool | No manifest field is a spendable/refillable counter; no StateRecord modifies HP, Overflow or a pool |
| SC-05 | Natural roll immutability | All setting modifiers are Skill-side or Movement overlays |
| SC-06 | Tag discipline | New Tags are vocabulary-only or cite a numeric ruling; `magic:`/`ability:` entries = 0 |
| SC-07 | DEC-025 | No Skill/alias/permission record has a Tag requirement or Effect entitlement |
| SC-08 | Effect cards | Every added Effect satisfies S-R8 |
| SC-09 | Location Templates | 100 states assigned, no reserves, parity conventions per DEC-137; Tier-1 body-plan class per DEC-144 |
| SC-10 | Creature templates | Derived stats recompute (DEC-004); signature skills full-Cap only where DEC-086 applies; Brawling default defensive Skill only where none authored (DEC-098); mode per DEC-076 |
| SC-11 | Item records | `Item Tier Y = Item Magnitude Y` at creation (DEC-129); damage is record-only (DEC-118) |
| SC-12 | Provenance | Frontmatter present; status non-canonical; unknowns recorded as "not established" |
| SC-13 | Gap escalation | Every Class U dependency is in `open_gaps` with no invented value |
| SC-14 | Fixture run | The unattended harness (module + harness + Conventions 1.1 format) completes under the module's ruleset pin |

## 4.7 Lifecycle

| Stage | Actor | Gate | Output |
|---|---|---|---|
| L0 Draft | Drafter pool (multi-vendor) | — | Candidate module/records |
| L1 Verify | Adversarial Verifier (not in drafter pool) | SC-01…SC-13 | Pass/fail + contradiction report |
| L2 Merge | Synthesizer → Backbone Builder | Contradictions become the question list | Merged candidate |
| L3 Ruling (G1) | Tiwa | Accept / edit / reject; batch acceptance permitted (DEC-149 R1 precedent) | Status "Ruled (working playtest content; not yet promoted via REQ-021)" |
| L4 Fixture | Runner (SC-14) | Ruleset pin stated | Execution record (advisory) |
| L5 Register | Registrar | Advisory annotation only | Provenance + annotation |
| L6 Promotion (G2, optional) | Tiwa | REQ-021 8 steps | Canonical text |

---

# 5. Part B — Reference Setting: Fantasy v0.1

## 5.1 Why Fantasy first [REC]

| Available content | Source | Status |
|---|---|---|
| Human Location Template + 100-state allocation | DEC-137 | Ruled (Human v1) |
| Nine creature Location Templates (Ice Troll, Blood Man, Giant Spider, Hobgoblin, Kobold, Troll, Dragon, Goblin, Orc) | DEC-149 R1 | Accepted working playtest content |
| Ice Troll, Blood Man (conversions); Goblin, Dragon (Tiwa-authored new content) | DEC-077.A, DEC-085; DEC-084 | Provisional / Tiwa-authored |
| Tutorial cast: Rowan, Aleena, Goblin, Rattlesnake, Ghoul, Bargle | Your First Adventure v0.2 | Advisory, accepted for playtest use |
| Reaction vocabulary `reaction:vigilant / guardian / opportunist` | DEC-132.B R3 | Ruled |
| 14-Condition alpha vocabulary; Tags ontology | DEC-079; DEC-080/088/114/119 | Ruled |
| Regression fixture (module + harness + Conventions 1.1) | 2026-09-14 documents | Advisory |

## 5.2 Manifest instance (`fantasy-reference`)

| Field | Value |
|---|---|
| id / kind / version | `fantasy-reference` / world / 0.1.0 |
| status | Advisory / Non-canonical — working content |
| requires | none |
| ruleset_pin | Canonical v1.4; register through DEC-154 |
| vocabulary.tags | **Zero new Tags at v0.1.** The standing vocabulary must suffice; any Fantasy Tag need is surfaced through the pipeline (§6) as a candidate. [REC; tests the minimal-surface principle] |
| vocabulary.conditions / effects | None added at v0.1 |
| permissions | Descriptive text only; no `magic:` / `ability:` Tags (DEC-146 R7) |
| content.location_templates | Human v1 (DEC-137) for Rowan, Aleena, Bargle; nine DEC-149 templates for their creatures |
| tunables | All unset except the DEC-125 session-standard crawl formula |
| open_gaps | B-01, B-02, B-03, B-04, B-05, B-07, B-08, B-09, B-12, B-13 (see §7.4) |

### 5.2.1 Alias map (descriptive; mechanical weight none) [GUESS-4]

The tutorial cast uses content labels over Tier-1 lineages. The mapping below is inferred from each label's attribute code against the Canonical §3 table. No corpus record states it.

| Module label | Formula | Canonical Tier-1 lineage |
|---|---|---|
| Attack | bpp | Might |
| Defense | bss | Reflexes |
| Perception | mss | Perception |
| Stealth | bsp | Agility |
| Composure | mex | Composure |
| Devotion | mee | Resolve |
| Smite | bep | Toughness |
| Beguile | mpx | Glamour |

Tier-2 signature skills (Trip, Venomous Bite, Claw, Grapple, Desecration, Bolt) are named Advanced formulas (DEC-087 template authoring), not aliases.

## 5.3 Magic integration (DEC-146)

| Element | Treatment in `fantasy-reference` |
|---|---|
| Base architecture | Advanced-Skill-native: new "spells" are new Advanced Skills created by the Canonical §12 qualifying failed Double (DEC-146 R1, R6) |
| Naming grammar | Technique×Form is an authoring convention only (DEC-146 R1 Option 2); `naming_catalog` is **empty** at v0.1 — Verb/Domain catalogs are Tiwa-authored content (DEC-077.A) |
| Permission | Descriptive text; no mechanical gate (DEC-146 R2; DEC-025) |
| Ritual casting | Extended Test, any Skill-Tier (DEC-146 R8; DEC-067–070) |
| Body/Mind mixing | Allowed by default (DEC-146 R4); setting restrictions via GM Fiat (DEC-130) |
| Corruption / miscast track | Not adopted; contingencies R3/R9 inactive |
| Starter `magic:` vocabulary | Deferred (DEC-146 R7) |

## 5.4 Fixture refresh required before S-17 use (SC-14)

| # | Finding | Basis |
|---|---|---|
| FX-1 | The Rattlesnake resolves hit location with DEC-100 "Legs" quartiles (Scene 2). A serpent is not a bipedal-humanoid, so under DEC-144 (2026-09-18) it needs a bespoke Tier-1 split. The module (2026-09-14) predates DEC-144, so this is staleness, not a defect. | DEC-144 (1) |
| FX-2 | No L-004 template exists for the Rattlesnake, Ghoul or Bargle. The Ghoul (bipedal-humanoid) may reuse DEC-100 Tier-1, but its Tier-2+ tree has no copy permission: the advisory C1 candidate ("Tier-2+ intra-zone copy/adaptation for bipedal humanoids") is explicitly not ruled. Tier-2 only matters for Armor Bypass, which falls back in the module. | DEC-149 "Left open" |
| FX-3 | The module pins DEC-140. Movement rulings DEC-143 and DEC-150–154 and the DEC-145 duration architecture postdate it. Re-verify Grapple, Restrained and Prone handling against them. | DEC-143; DEC-150–154 |
| FX-4 | The A1 convention (single-action reading of DEC-106) remains a run convention, not a ruling. Keep it stated in every run. | Module A1 |

## 5.5 Reference-module acceptance

`fantasy-reference` v0.1 is complete when SC-01…SC-14 pass (with FX-1…FX-4 addressed) and its `open_gaps` list matches §7.4 for Fantasy.

---

# 6. Part C — Content-Integration Pipeline

## 6.1 Authorization routes

| Route | Source | Authorization in corpus | Scope limit | Default treatment |
|---|---|---|---|---|
| R-Conv | GURPS creatures from the BToV-Madness PDF | DEC-077.A | **Limited to that source for the BToV-Madness playtest; "not generalized"** | Working stat block; provisional until Tiwa affirms |
| R-New | Tiwa-authored new content | DEC-077; DEC-084 | Advisory models draft candidates; acceptance is Tiwa's ruling (DEC-137, DEC-149 precedent) [GUESS-5] | Candidate → acceptance ruling |
| R-Adapt | Adapted scenario/module | No DEC; accepted for playtest use in-session | Non-canonical | Advisory |
| R-Ext | Any other published source | **None** | — | **Blocked until Tiwa authorizes that source** [REC; F-5] |

## 6.2 Stages

| Stage | Actor | Input → Output | Checks |
|---|---|---|---|
| PS-0 Intake and route | Registrar | Source → route (§6.1) | Record source reference. IP checkpoint: convert mechanics only; no verbatim source text; no numeric import (DEC-085 (3)). This is a flag, not a legal assessment. [GUESS-13] |
| PS-1 Decompose | Drafter | Source entity → primitive inventory (attributes, skills, Tags, Traits, attacks, defenses, armor, resources, body plan, special rules) | Complete inventory |
| PS-2 Map | Drafter | Inventory → mapping (§6.3) | Every source concept maps or is logged as a gap |
| PS-3 Author | Drafter pool (≥3 vendors for divergent generation) | Mapping → candidate records | DEC-085 baseline: derived stats by DEC-004/005; attacks are S-1 contests; test the Wound pathway first |
| PS-4 Verify | Verifier (not in pool) | Candidates → Conformance Cards + SC-01…SC-13 | Mechanical pass/fail |
| PS-5 Merge | Synthesizer/Backbone Builder | Survivors → merged candidate + question list | Disagreements escalate, never averaged |
| PS-6 Ruling (G1) | Tiwa | Question list → accept / edit / reject | Status label per §4.7 |
| PS-7 Fixture | Runner | Accepted content → execution record (SC-14) | Ruleset pin stated |
| PS-8 Record | Registrar | Advisory register annotation + provenance | No DEC unless Tiwa rules |

## 6.3 Primitive mapping table

| # | Source concept (generic) | Tiwas primitive | Governing rulings | Status |
|---|---|---|---|---|
| 1 | Hit points | Derived HP (Σ Body); no source value imported | DEC-004; DEC-085 (2) | Ruled |
| 2 | Damage dice | Not imported; Inflict Injury = Winner's Margin − Defender's Margin | DEC-085 (3); DEC-096/097/104 | Ruled |
| 3 | Dodge / Parry / Block | Active Defense Skill; Brawling default only where a template authors none | DEC-044; DEC-098 | Ruled |
| 4 | Damage resistance / armor value | `defense:armor` Tag, location-bound; Bypass = Tag-pair + location | DEC-058/059/062; DEC-114 R2 | Ruled |
| 5 | Ongoing / per-second damage | Single-application Effect or narration; no DoT | DEC-023.A; DEC-083 | Ruled |
| 6 | Environment-conditional trait | Conditional-Trait Binding + `env:` Tag | DEC-088; DEC-088.A | Ruled |
| 7 | Regeneration / regrowth | Per-creature content; gated via Condition Clause | DEC-110; DEC-088 | Ruled (content) |
| 8 | Fear aura | Condition Clause + Frightened | DEC-094; DEC-079 | Ruled |
| 9 | Status effect with penalties | Condition `Tier-Y Value Z`, `Z = −Y` | DEC-079 | Ruled |
| 10 | Control effects (charm, domination, possession) | Not expressible as Skill-side/Movement penalty; S-1 contest + narrated outcome, flagged | DEC-082; DEC-023.A (4); DEC-123 | **Gap B-09** |
| 11 | Poison / disease | Poisoned / Sickened Conditions (no HP DoT) | DEC-079 C7 | Ruled |
| 12 | Spells / psionics / tech powers | Advanced Skills; no spell list; naming catalog is content | DEC-146 R1/R6; Canonical §12/§15 | Ruled architecture; vocabulary deferred (B-08) |
| 13 | Ritual / long casting | Extended Test, any Skill-Tier | DEC-146 R8; DEC-067–070 | Ruled |
| 14 | Movement rate | Movement Speed derived; distance = effective MS hexes/turn; four bands | DEC-004; DEC-133 | Ruled |
| 15 | Flight / 3D movement | Unruled | DEC-133 (dimension unstated) | **Gap B-07** |
| 16 | Weight / encumbrance | Item mass in kg; `C = floor(HP/6)`; six bands | DEC-078 | Ruled |
| 17 | Prices / wealth | Not portable | DEC-081.A Open 3 (EQ-3A) | **Gap B-01** |
| 18 | Weapon range / ammunition | Not portable | DEC-081.A Open 3 (EQ-3C) | **Gap B-02** |
| 19 | Size categories | `creature:size_small / medium / large` only; more needs a DEC-080 T1 ruling | DEC-080; DEC-149 R3 | **Gap B-04** |
| 20 | Body layout / hit locations | Location Template per creature type; bipedal-humanoid reuses DEC-100, all other body plans bespoke-by-default | DEC-112 L-004; DEC-144; DEC-137 | Ruled |
| 21 | Skill lists | Tier-1 lineages + Advanced Skills; source skills become alias labels or Advanced Skills; never gating | Canonical §3/§12; DEC-025 | Ruled + alias content |
| 22 | Advantages / disadvantages / quirks | No Advantage/Disadvantage language; express as descriptive Tags, Conditions, or content | DEC-023.A; DEC-116 | Ruled (prohibition) |
| 23 | Initiative | Speed order | DEC-095 | Ruled |
| 24 | Multi-attack creatures | All authored attacks back-to-back (automated) / GM fiat (GM present) | DEC-106 | Ruled |
| 25 | Healing rates | S-11 Extended Test; Effect Heal System | DEC-071–074; DEC-121; DEC-127; DEC-135.A | Ruled |
| 26 | Crafting / repair | Extended Test; Item Tier/Magnitude; recipes | DEC-128; DEC-129; DEC-141; DEC-142 | Ruled + partial (B-12) |
| 27 | Durations | Per-domain assignment; constants are content | DEC-145 | Ruled; constants content |

## 6.4 Record provenance fields (every converted or authored record)

`source_ref` · `route` (R-Conv / R-New / R-Adapt) · `authorization` (DEC-077.A / DEC-084 / DEC-149 / none) · `conversion_status` (converted / Tiwa-authored / candidate) · `tiwa_ruling_ref` · `ruleset_pin` · `author_llm` / `assessor_llm[]` · `status` (never Canonical).

## 6.5 Failure modes and controls

| Failure mode | Control |
|---|---|
| Contradiction drift between drafters | Spec cards + Verifier report; disagreements escalate (orchestration plan §8) |
| Silent numeric import | SC-13; DEC-085 (3) check at PS-4 |
| Coincident error | ≥3-vendor drafting; Tiwa G1 gate |
| Module blending into canon | Status field fixed; G2 required (REQ-021) |
| Stale ruleset pin | `ruleset_pin` mandatory; re-verify on any register change touching the module's records |

---

# 7. Part D — Six-Setting Stress Test

## 7.1 Method

For each §18 setting: list its capability demands, map each to primitives, classify the outcome, and record blockers. The genre demands are generic assumptions, not corpus facts. [GUESS-8]

| Code | Meaning |
|---|---|
| **V1** | Native: existing rulings suffice |
| **V2** | Additive: expressible with Class E content and Tiwa's acceptance; no new ruling |
| **V3** | Blocked pending a ruling (blocker id) |
| **V4** | Conflicts with Class L/F; reject |
| **w** | Inherits from the world module (overlay only) |

## 7.2 Matrix

| # | Capability | Fantasy | Sci-Fi | Modern | Horror | Historical | Cinematic |
|---|---|---|---|---|---|---|---|
| 1 | Melee combat and wounds | V1 | V1 | V1 | V1 | V1 | V1 |
| 2 | Ranged weapons and ammunition | V3 B-02 | V3 B-02 | V3 B-02 | w | V3 B-02 | w |
| 3 | Armor and protection | V1 | V2 (new `damage:*` Tags) | V1 | w | V1 | w |
| 4 | Powers / special abilities | V2 B-08 | V2 B-08; V3 B-06 (augmentation) | V2 B-08 | V2 B-08 | V1 (martial techniques) | w |
| 5 | Creatures / NPCs / body plans | V2 B-13 | V2 B-13 | V2 B-13 | V2 B-13 | V2 B-13 | V1 (abbreviated GM-run NPCs, DEC-076) |
| 6 | Vehicles / vessels / structures | V3 B-04 | V3 B-04 | V3 B-04 | w | V3 B-04 | w |
| 7 | Wealth and trade | V3 B-01 | V3 B-01 | V3 B-01 | w | V3 B-01 | w |
| 8 | Travel, scale, time | V2; V3 B-07 (flight) | V3 B-07 | V2 | V2 | V2 | V2 |
| 9 | Hazards and environment | V2 | V2 | V2 | V2 | V2 | V2 |
| 10 | Psychological harm | V2; V4 B-09 (control) | V2 | V2 | V2 | V2 | V1 |
| 11 | Tone control (lethality, heroism) | V1 | V1 | V1 | V1 (guidance) | V1 | V2; V4 B-10, B-14 |
| 12 | PC ancestry / culture | V3 B-05 | V3 B-05 | V2 | V2 | V2 | w |
| 13 | Healing and medicine | V1 | V2 | V2 | V1 | V1 | w |
| 14 | Crafting / maintenance | V3 B-12 | V3 B-12 | V3 B-12 | w | V3 B-12 | w |

## 7.3 Per-setting notes

### Fantasy — world module, reference (Part B)
- Native: melee, armor Tags, healing, tone, nine accepted creature templates.
- Additive: magic under DEC-146 (naming catalog empty until Tiwa authors it), bestiary, hazards via `env:` Tags plus DEC-093 lookups.
- Blocked: bows/ammunition (B-02), ships (B-04), trade (B-01), mechanical ancestry (B-05), flight (B-07), crafting item families (B-12).
- Rejected as mechanic: charm/domination as a control Condition (B-09). Represent as an S-1 contest plus a narrated, flagged outcome, as Your First Adventure Scene 6 does.

### Horror — overlay module
- Fear: Frightened via a scene-state trigger (DEC-094; `env:darkness` and similar Tags; DEC-079).
- Mental harm: Mind-attribute Wounds (DEC-102 (3)) need a Skill-Tier ≥ 2 promoting roll and a Location Index (DEC-041, DEC-033), so they suit located threats only. For non-located dread, add a setting Condition using the S-R9 template; it may be `permanent` until the Effect Heal System reduces it (DEC-117 R2; DEC-121). [GUESS-7]
- Attrition: Cost = roll with Overflow → HP is inherent (Canonical §7).
- **V4:** a Sanity pool (Invariant 17). A Corruption track was considered and not adopted (DEC-146 R1).
- Dread pacing and forced-retreat beats are scenario guidance, not rules.

### Cinematic — overlay module (guidance-heavy)
- Native: Tier-0 default already suits location-light play (DEC-040); heroic resilience is design Priority 2 (DEC-052, DEC-054); abbreviated GM-run extras (DEC-076); symmetric difficulty grades (DEC-063/066).
- **V4:** skip-the-roll for trivial or dramatic actions (DEC-051, B-10); hero/luck/fate points (Invariant 17, B-14); Fiat overriding HP = 0 incapacitation or Overflow (DEC-130).
- The module is therefore mostly non-binding guidance plus content; it cannot add mechanics.

### Historical — world module
- Native: weapons and armor Tags, healing, no magic (zero `magic:`/`ability:` use).
- Content: period item mass (DEC-078), travel constants (DEC-145 K/D), period Skill labels (alias/naming catalogs).
- Blocked: wealth/trade (B-01), ranged/ammunition (B-02), vessels and siege structures (B-04), crafting item families (B-12).

### Modern — world module
- Native: melee, armor with Bypass via `damage:*`↔`defense:armor` Tag pairing (DEC-059, DEC-114 R2), hazards (`damage:electric`, `env:hazard_*`).
- Blocked: firearms range/ammunition (B-02), vehicles (B-04), wealth (B-01), crafting families (B-12).
- Descriptive only: law, authority, communications (no mechanic needed).

### Science Fiction — world module (highest blocker load)
- Technology lineages via setting permission (Proposals §15), descriptive only; augmentation needing persistent beneficial records is blocked (B-06).
- Blocked: 3D and zero-gravity movement (B-07), vessels and scale (B-04), energy weapons range (B-02), species mechanics (B-05), wealth (B-01).
- Additive: new `damage:*` Tags via DEC-080 T1, band↔hex constants at interplanetary scale (Class T).

## 7.4 Blocker register

| ID | Blocked capability | Settings | Why unruled | Recommended interim default [REC] | Ruling needed from Tiwa |
|---|---|---|---|---|---|
| B-01 | Wealth, currency, trade | F, SF, M, Hi | EQ-3A; Equipment Reserved; Invariant 17-sensitive | Modules contain no prices or currency; acquisition narrated or GM Fiat; items list mass and Tags only | Wealth model that creates no competing economy |
| B-02 | Ranged range assignment and ammunition | F, SF, M, Hi | EQ-3C | `offense:ranged` Tag only; weapon range left unset; no ammunition counter | Range-band assignment and ammunition tracking |
| B-03 | Loadout swap cost; starting equipment | All | EQ-3B / EQ-3D | Scenario-authored starting gear; no swap-cost rule | Loadout and starting-equipment rules |
| B-04 | Vehicles, vessels, structures as targets/combatants; size Tags beyond `size_large` | F, SF, M, Hi | Object-as-combatant unruled; DEC-080 T1 ruling needed for new size Tags | Vessels appear as scenery or Item records (DEC-128 Q1); no vehicle combat at v0.1 | Object-combatant model; size vocabulary |
| B-05 | PC ancestry / species mechanics | F, SF | Canonical §3 fixes attribute generation; nothing rules ancestry | Descriptive-only ancestry Tags (DEC-116; mirrors DEC-146 R2) | Whether any mechanical ancestry exists and where it may attach |
| B-06 | Persistent beneficial StateRecords (blessings, augmentations) | SF, F | DEC-115 fixes `Z = −Y`; beneficial-record sign convention is not stated | Modules exclude persistent beneficial records; instant beneficial Effects unaffected | Sign and format for beneficial records |
| B-07 | Flight, vertical/3D movement, low/zero gravity | SF, F | DEC-133 gives no dimensionality | 2D bands only; flying creatures resolve in 2D; dimension declared unset | Dimensionality of the distance model |
| B-08 | Magic / ability vocabulary; naming catalogs | F, SF, M, H | DEC-146 R7 deferral; DEC-077.A content | Zero `magic:`/`ability:` Tags; catalog empty | Vocabulary authorization (when the system matures) |
| B-09 | Control effects (charm, domination, possession) | F, H | DEC-082 and DEC-023.A (4) allow only Skill-side/Movement expression | S-1 contest plus narrated, flagged outcome; no control Condition | Whether any control-type Condition may exist |
| B-10 | Skip-roll / auto-success | C | Rejected, DEC-051 | **Reject** (V4) | None; already ruled |
| B-11 | Difficulty-grade numeric values | All | DEC-063 rules named tiers, corpus supplies no numbers | Reference grades by name only | Numeric values (Universal Play, not a setting matter) |
| B-12 | Crafting: Material/Component record typing; tool/fixture Tag preconditions | F, SF, M, Hi | Crafting proposal's record extension unruled; DEC-141/142 rule arithmetic and gate only | Item Creation limited to DEC-128/141/142; no Material/Component typing | Item-family record; tool-precondition rule |
| B-13 | Body plans beyond DEC-144's four classes (serpentine, avian, aquatic) | All | DEC-144 (1): non-listed classes are bespoke-by-default | Author a bespoke Tier-1 per creature (content work, not a ruling gap) | None required; optional new pre-ruled classes |
| B-14 | Meta-currency (hero/luck/fate points) | C | Invariant 17 | **Reject** (V4) | None; already bound |

---

# 8. Work Plan and Acceptance

## 8.1 Work packages

| WP | Work | Depends on | Owner role | Done when |
|---|---|---|---|---|
| WP-1 | Freeze ruleset pin and constraint table (§3) | — | Backbone Builder | Pin recorded; C-01…C-18 verified against the register |
| WP-2 | Manifest schema + Conformance Card templates | WP-1 | Backbone Builder | Tiwa approves templates (G1) |
| WP-3 | Conformance suite SC-01…SC-14 spec + harness hooks | WP-2 | Backbone Builder | Each test has an executable definition |
| WP-4 | `fantasy-reference` manifest + fixture refresh (FX-1…FX-4) | WP-2, WP-3 | Drafter pool → Verifier | SC-01…SC-14 pass |
| WP-5 | Pipeline runbook + provenance record template | WP-2 | Registrar | Route R-New exercised end to end on one creature |
| WP-6 | Independent verification of the stress test; blocker escalation packet | WP-4 | Verifier | Packet delivered to Tiwa |
| WP-7 | Overlay skeletons: Horror, then Cinematic | WP-4, WP-6 | Drafter pool | Skeleton manifests pass SC-01…SC-13 |
| WP-8 | World skeletons: Historical, Modern, Sci-Fi (gap declarations plus non-blocked content) | WP-6 | Drafter pool | Each lists `open_gaps` matching §7.4 |
| WP-9 | Documentation sync (Roadmap §25): Phase 12 status; Proposals §17 pointer | WP-6 | Registrar | Advisory annotations only |

**Delivery order [REC; F-9]:** Fantasy → Horror → Cinematic → Historical → Modern → Sci-Fi. Rationale: ascending blocker load from the §7.2 matrix; overlays before dependent worlds.

## 8.2 Acceptance criteria

| ID | Criterion | Source |
|---|---|---|
| AC-1 | A new setting module loads with zero edits to Canonical Rules or Core (SC-01) | Roadmap §19/§22 |
| AC-2 | Phase 0 regression passes unchanged with each module loaded (SC-03) | Roadmap §7 |
| AC-3 | Every Class U dependency is declared, none filled (SC-13) | C-18 |
| AC-4 | `fantasy-reference` passes SC-01…SC-14, including the fixture run | §5.5 |
| AC-5 | All six settings have matrix rows and the blocker packet has reached Tiwa | §7 |
| AC-6 | Every record carries provenance and authority; none is marked Canonical | S-R12 |
| AC-7 | No new invariant is added; any proposed one is escalated instead | Governance Rule 6 |

---

# 9. Pre-filled Defaults Awaiting Tiwa

| ID | Decision | Default (pre-filled) | Alternative considered | Reason for default |
|---|---|---|---|---|
| F-1 | May settings amend Class F rulings? | **No.** Settings extend and tune only. | Allow settings to amend selected Class F rulings | DEC-130 already places several Fixed items beyond Fiat; amendment would let a setting redefine Core-equivalent behaviour (C-16) |
| F-2 | Tag scoping | Setting-scoped ids (`scope: <module id>`); entry into the standing vocabulary needs a Tiwa ruling | One global vocabulary | Keeps DEC-080 T1's ruling-per-extension precedent without polluting the standing vocabulary |
| F-3 | Composition | World + overlay, additive, explicit Class T override only | Single monolithic module per setting; free inheritance | Horror and Cinematic are tone layers, not worlds (§18 lists them as peers) [GUESS-6] |
| F-4 | Setting Conditions/Effects | Allowed as candidates with a Conformance Card; in force only after Tiwa accepts (batch acceptance permitted) | Free addition by authors | C-12; DEC-149 R1 precedent |
| F-5 | Content sources beyond the BToV PDF | Blocked until Tiwa authorizes each source | Extend DEC-077.A generally | DEC-077.A is explicitly "not generalized" |
| F-6 | Module status | "Ruled (working playtest content; not yet promoted via REQ-021)" after G1 | Canonical on acceptance | DEC-137/149 precedent; REQ-021 |
| F-7 | Skill label handling | Descriptive alias table, mechanical weight none | Rename Tier-1 skills per setting | DEC-025; Canonical §3 names are locked |
| F-8 | Unset tunables | Allowed; GM discretion at the table; DEC-145 (9) convention in automated runs | Require all tunables set | Numbers are content-authoring (C-15); avoids LLM-invented constants |
| F-9 | Delivery order | Fantasy → Horror → Cinematic → Historical → Modern → Sci-Fi | Alphabetical or Proposals §18 order | Blocker load (§7.2) |

---

# 10. Guess and Assumption Register

| ID | Guess | Effect if wrong |
|---|---|---|
| GUESS-1 | "S-17" means Proposals §17/§18 + Roadmap Phase 12 + U-22 | Scope mismatch; re-map §1 |
| GUESS-2 | Register overrides Proposals/Roadmap v1.4.3 where they conflict (both documents pre-date most rulings) | Some Class F entries would need re-checking |
| GUESS-3 | Class F = all ruled mechanics except delegated tunables; the F/T boundary is my reading of DEC-077.A/DEC-145 delegation language | Some Class F items may be tunable, or vice versa |
| GUESS-4 | The alias map (§5.2.1) is inferred from attribute codes; no corpus record states it | Alias table needs Tiwa's confirmation |
| GUESS-5 | Advisory candidate drafting is acceptable despite DEC-077's original wording, based on DEC-137/DEC-149 practice | Pipeline stage PS-3 would need Tiwa-only authoring |
| GUESS-6 | World/overlay split fits Horror and Cinematic as tone layers | Six peer modules (Proposals §18 reading) would replace F-3 |
| GUESS-7 | Non-located mental harm is expressed as a setting Condition using the DEC-079 template and existing removal routes | Horror may need a ruling on a dedicated record |
| GUESS-8 | Per-setting demands are generic genre assumptions, not corpus facts | Matrix cells change with Tiwa's intended scope per setting |
| GUESS-9 | Genre demands were tested only against records I could see; unstated register entries after DEC-154 are unknown to me | New rulings may close blockers |
| GUESS-10 | DEC-144's four-class taxonomy is open-ended (non-listed → bespoke) | If closed, B-13 becomes a ruling gap |
| GUESS-11 | Suggested repo path `investigations/…` and filename convention | Cosmetic |
| GUESS-12 | Length and table density chosen to match repo convention | Cosmetic |
| GUESS-13 | IP/licensing handling in PS-0 is a process flag only; I cannot assess legal status of source material or of the tutorial adaptation | Needs Tiwa's own judgment or counsel |

---

# 11. Conflict Check Statement

| Check | Result |
|---|---|
| Formula changes proposed | None |
| Class L rules touched | None |
| Class F rulings altered | None (F-1 default forbids it) |
| New pools, currencies or resolution methods proposed | None; B-01/B-14 explicitly rejected or deferred |
| Register annotations or DECs created | None; register annotation only after Tiwa rules (§4.7 L5) |
| Contradictions between corpus documents noted | Proposals/Roadmap v1.4.3 predate the register (GUESS-2); tutorial fixture predates DEC-144 (FX-1) |

**End of document.**
