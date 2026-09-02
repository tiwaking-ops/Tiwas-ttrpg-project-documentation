### Tailored prompt for this task

**Role:**  
You are a systems analyst and TTRPG design partner evaluating Tiwas TTRPG’s current mechanical readiness against a specific published adventure.

**Context:**  
You are adapting the GURPS adventure *Beyond the Vale of Madness* to Tiwas TTRPG. You want to analyse every game-mechanical system the adventure uses or assumes, then map those requirements onto the current Tiwas Alpha-Playtest Corpus. The goal is to measure how ready Tiwas is for playtesting by seeing which required systems are already developed and usable, and which still need design work. Any GURPS skill roll is treated as a standard Tiwas Skill Test mechanically.

**Audience:**  
Primary: you (Tiwa) as designer and governance authority.  
Secondary: any future collaborator or GM using Tiwas for alpha playtests and needing a clear readiness picture.

**Format and length:**  
- Output as a **comprehensive formal project report in markdown**.  
- Include:  
  - Executive summary  
  - Methodology and assumptions  
  - System requirement mapping (GURPS adventure → Tiwas subsystems)  
  - Readiness assessment table(s)  
  - Detailed findings per subsystem (compatible vs design-stage vs missing)  
  - Gap analysis and concrete recommendations for Tiwas development roadmap  
  - Brief conclusion and suggested next playtest actions  
- Length: detailed but focused—enough to be table-usable and governance-usable, without narrative padding.

**Success criteria (what makes this great):**  
1. Clear, explicit mapping from *Beyond the Vale of Madness*’s mechanical demands to Tiwas subsystems, with no silent assumptions.  
2. A precise, actionable list of which Tiwas systems are **playtestable now** for this module and which are **not yet reliable**, including why.  
3. A concise decision statement on **whether the adventure can be run in Tiwas now**, and if not, exactly which subsystems must be completed or scaffolded first.

**Constraints:**  
- Treat the **current canonical Tiwas rules + accepted designer rulings + explicitly accepted non-canonical Ruled subsystems** in the Alpha-Playtest Corpus as the available baseline; everything else is “not yet available.”   
- Assess compatibility **mechanically**, not by preserving GURPS procedures: any GURPS skill roll is a Tiwas Core Test; focus on what the adventure needs the rules to accomplish.  
- Use the readiness categories primarily as:  
  - **Playtestable now** (Tiwas has sufficient rules to run it as written, with only mechanical translation).  
  - **Needs development** (design-stage or missing subsystem; not reliable enough for alpha play without explicit scaffolding).  
- Follow a formal project-report tone and structure; avoid fiction, flavour text, or GM advice beyond what’s needed for readiness assessment.

**Examples / references:**  
- Tiwas Alpha-Playtest Corpus (Core Test Transaction, S-1–S-11 subsystems, and Part C “Explicitly NOT table-ready”).   
- *Beyond the Vale of Madness* adventure text and its embedded GURPS character sheet, skill checks (Tracking, Climbing, IQ/DX/ST rolls), combat assumptions, hit location, and equipment/loot structures.   

---

## Project report: Tiwas readiness for *Beyond the Vale of Madness* adaptation

### 1. Executive summary

This report evaluates whether *Beyond the Vale of Madness* (a GURPS Dungeon Fantasy adventure) can be run using Tiwas TTRPG in its current alpha state, and which Tiwas subsystems are ready for playtesting versus still in design or missing.

The adventure relies on:  
> “Make a Tracking roll at +3, or an IQ-2 if you do not have the skill.”   

and similar checks (Climbing, attribute-based rolls, combat, hit locations, equipment, monsters, loot, and XP). It also embeds a standard GURPS character sheet with attributes, active defenses, encumbrance, hit location, and spells.   

Tiwas currently provides a locked Core Test Transaction and a suite of Ruled subsystems (S-1–S-11) that are explicitly table-ready for alpha play, while Part C lists systems and content that are **not** table-ready.   

**High-level verdict:**  
- The **core task resolution**, **difficulty**, **opposed contests**, **hit location index**, **wounds/injury**, **armor**, **active defense**, **incapacitation/death**, **extended tests**, and **rest/healing** are all present at a Ruled or Locked level and can be used to run the mechanical backbone of the adventure.   
- **Creature/campaign content (S-12)** and **full S-3 gated Effect contents** remain open/not table-ready, meaning monsters, detailed special effects, and some condition/equipment/defense/location-tier effects must be authored or scaffolded manually.   

The adventure is **playtestable now in Tiwas** with mechanical translation and explicit GM scaffolding for:  
- NPC/monster stat blocks and templates  
- Some advanced Effect menu contents (conditions, equipment damage, defense/location-tier effects)  
- Setting-specific content and treasure valuation

This report details exactly which systems are compatible, which are usable but fragile, and which still need design work.

---

### 2. Methodology and assumptions

#### 2.1 Mechanical reading of the adventure

**Assumption (explicit):**  
- Every place the adventure calls for a GURPS roll (e.g., “Tracking roll at +3”, “Climbing roll at -3”, “IQ-2 if you do not have the skill”) is treated as a Tiwas **Core Skill Test** using the 9-step Canonical Test Transaction.   

> “Every Skill test follows this order: 1. Roll 1d100… 9. End the test.”   

#### 2.2 Tiwas baseline

**Baseline definition:**  
- Only material tagged **Canonical / Locked** or **Non-canonical designer ruling** and listed as table-ready in Parts A–B of the Alpha-Playtest Corpus is treated as available mechanics.   
- Part C items (“Explicitly NOT table-ready”) are treated as **needs development** or **content-authoring only**, not usable rules.   

#### 2.3 Readiness categories (operationalised)

For this report:

- **Playtestable now:**  
  Tiwas has sufficient rules to run the adventure’s mechanical requirement with only translation (no new subsystem design).

- **Needs development:**  
  The adventure assumes a system that Tiwas either:  
  - has only in open/draft form, or  
  - has not yet enumerated contents (e.g., S-3 gated Effect lists, S-12 creature templates).

Anywhere I had to guess (flagged later), I chose the least invasive assumption consistent with your governance model.

---

### 3. System requirement mapping (GURPS → Tiwas)

#### 3.1 Core task resolution and skills

**Adventure requirements (GURPS):**

- Attribute and skill checks: Tracking, Climbing, IQ, DX, ST, etc.  
  > “Make a Tracking roll at +3, or an IQ-2 if you do not have the skill.”   
- Success/failure branches in the paragraph structure (go to X on success, Y on failure).

**Tiwas subsystems:**

- **Core Test Transaction (DEC-006)** — locked.   
- **Difficulty grades (S-8, DEC-063–066)** — Ruled, named tiers with fixed Skill-side modifiers.   
- **Failure XP, Skill Roll Pool, General XP (DEC-009–011)** — locked progression economy.   

**Compatibility:**  
- **Playtestable now.** All GURPS skill/attribute rolls can be mapped to Tiwas Skill Tests with appropriate difficulty grades and Skill values.

#### 3.2 Combat, opposed contests, and quality

**Adventure requirements:**

- Implied combat with monsters (ice troll, yetis, blood men, etc.).  
- Attack vs defense, success/failure, and narrative consequences (injury, escape, etc.).

**Tiwas subsystems:**

- **S-1 Opposed Contest (DEC-013 + DEC-031)** — universal opposed-contest primitive with Quality measures and Effect-tier gating.   
- **S-3 Effect menu structure (DEC-023–030)** — Ruled menu structure, with base-tier Inflict Injury and Retreat/Compel Yield; gated tiers for Position, Condition, Equipment, Defense, Location.   

> “Base tier = Inflict Injury (HP-only) + Open Retreat/Compel Yield; five gated tiers…”   

**Compatibility:**  
- **Playtestable now** for basic combat: opposed contests, base-tier Inflict Injury, and retreat/yield are fully usable.  
- **Needs development** for some advanced combat effects (e.g., detailed condition/equipment/defense/location-tier effects), because gated-tier contents are not fully enumerated.   

#### 3.3 Hit location and injury

**Adventure requirements:**

- GURPS hit location table (torso, arms, legs, skull, vitals, etc.) on the character sheet.   
- Damage and injury consequences from attacks and hazards.

**Tiwas subsystems:**

- **S-2 Zero-Step Location Index (DEC-014, DEC-037, DEC-039)** — Tier-1 location index provider, including non-attack provenance and Extended Test governing roll.   
- **S-4 Wound/Injury (DEC-032–036, DEC-041–042)** — Ruled distinction between Injury (HP damage) and Wound (localized lasting numerical state), anatomical mapping, Tier-2 subdivision, and interaction with Effects.   

> “Injury = HP Damage; Wound = Localized, Lasting Numerical State. Wounds are distinct from HP and tracked numerically…”   

**Compatibility:**  
- **Playtestable now** for:  
  - Generating hit locations via Zero-Step.  
  - Applying HP damage and Wounds via S-3/S-4 Effects.  
- **Needs development** for:  
  - Full wound consequence catalogue (OPEN-007: penalties, healing cost scaling) which is explicitly not table-ready.   

#### 3.4 Armor and defense

**Adventure requirements:**

- Armor and protective gear implied by GURPS equipment and active defense entries.   

**Tiwas subsystems:**

- **S-5 Armor (DEC-058–062)** — Tags/Traits-only armor, Bypass definition, Sunder Effect placement, resolution order vs Active Defense.   
- **S-6 Defense (DEC-044–050)** — Active Defense architecture, defender rolls, voluntary decline, mitigation model.   

> “Armor is a Tags/Traits system only. No numeric durability/soak pool… Armor Tags never modify Overflow under any circumstance.”   

**Compatibility:**  
- **Playtestable now** for:  
  - Armor as tags, interacting with Effects and Active Defense.  
  - Active Defense rolls by defenders, including mitigation of auto-applied Effects.  
- **Needs development** only where specific armor tags and Sunder/Bypass content must be authored for particular items in the adventure.

#### 3.5 Incapacitation, death, rest, and healing

**Adventure requirements:**

- Characters can be injured, potentially incapacitated or killed; they may rest and recover between scenes.  
- The adventure’s conclusion awards XP and assumes future adventures.

**Tiwas subsystems:**

- **S-7 Incapacitation/Death (DEC-052–057)** — HP=0 forced incapacitation, death thresholds, stabilization.   
- **S-11 Rest/Healing (DEC-071–074)** — healing via explicit Skill Tests and Extended Tests, wound magnitude penalties, progress via Margin accumulation.   

> “Healing during a Rest period requires an explicit Skill Test… A Rest period’s healing is resolved as an Extended Test…”   

**Compatibility:**  
- **Playtestable now.** The adventure’s injury, incapacitation, and rest can be resolved using S-7 and S-11, with Extended Tests (S-9/S-10) for longer healing processes.

#### 3.6 Difficulty, environmental hazards, and extended tasks

**Adventure requirements:**

- Climbing icy walls at penalties, navigating labyrinths, tracking in difficult terrain, etc.  
- Environmental hazards (ice, cold, crumbling floors, etc.) that can injure or impede characters.   

**Tiwas subsystems:**

- **S-8 Difficulty (DEC-063–066)** — named difficulty grades with fixed Skill-side modifiers, symmetric bonuses/penalties.   
- **S-2/S-4 non-attack Location Index (DEC-037)** — hazards using failed rolls to generate location indices and apply injury/wounds.   
- **S-9/S-10 Extended Tests (DEC-067–070)** — margin-accumulation progress, neutral failure behaviour.   

**Compatibility:**  
- **Playtestable now.** All environmental challenges and extended tasks (e.g., long climbs, searches, healing) can be modelled with difficulty grades, Extended Tests, and hazard rules.

#### 3.7 Creatures, NPCs, and campaign content

**Adventure requirements:**

- Specific monsters (ice troll, yetis, blood men), NPCs (injured hunter Jrak Kul, Martyrs of War), and setting-specific factions and rewards.   

**Tiwas subsystems:**

- **S-12 Creature/Campaign content (DEC-076–077)** — Ruled as a content-authoring track, not a settled mechanic; templates are to be developed by Tiwa via playtesting.   

> “Creature/npc content is a content-authoring track, not a settled mechanic… actual creature/campaign template instances… are developed by Tiwa via playtesting; not drafted by any advisory model.”   

**Compatibility:**  
- **Needs development.** The adventure’s monsters and NPCs require explicit Tiwas stat blocks and templates authored by you; the system does not yet provide them.

---

### 4. Readiness assessment table

#### 4.1 Summary table by subsystem

| Adventure requirement area | Tiwas subsystem(s) | Readiness | Notes |
|---|---|---|---|
| Core skill/attribute checks, success/failure branches | Core Test Transaction (DEC-006), Difficulty (S-8), XP (DEC-009–011) | **Playtestable now** | Direct mechanical translation of all GURPS rolls to Tiwas Skill Tests.  |
| Opposed contests, basic combat outcomes | S-1 Opposed Contest, S-3 base-tier Effects | **Playtestable now** | Inflict Injury and Retreat/Compel Yield fully usable; Quality gating in place.  |
| Advanced combat effects (conditions, equipment damage, defense/location-tier effects) | S-3 gated tiers (Position, Condition, Equipment, Defense, Location) | **Needs development** | Menu structure Ruled; contents not fully enumerated (Part C.3).  |
| Hit location and injury | S-2 Zero-Step, S-4 Wound/Injury | **Playtestable now** (core) / **Needs development** (consequences) | Location indices and wound states usable; detailed consequence catalogue OPEN-007 not table-ready.  |
| Armor and defense | S-5 Armor, S-6 Defense | **Playtestable now** | Tags-only armor, Bypass/Sunder, and Active Defense sequence Ruled and table-ready.  |
| Incapacitation and death | S-7 Incapacitation/Death | **Playtestable now** | HP=0 incapacitation and death thresholds Ruled.  |
| Rest and healing | S-11 Rest/Healing, S-9/S-10 Extended Tests | **Playtestable now** | Healing via Skill Tests and Extended Tests; wound magnitude penalties defined.  |
| Environmental hazards and extended challenges | S-2/S-4 hazard provenance, S-8 Difficulty, S-9/S-10 Extended Tests | **Playtestable now** | Hazards can use failed rolls for location and injury; difficulty grades and extended progress defined.  |
| Creatures, NPCs, factions, treasure templates | S-12 Creature/Campaign content | **Needs development** | Explicitly content-authoring only; no stat blocks or templates provided.  |
| Setting-specific flavour and narrative | Adventure text itself | **Adventure-specific content** | Outside Tiwas system readiness; used as-is.  |

---

### 5. Detailed findings and gaps

#### 5.1 Systems fully playtestable now

**Core resolution and difficulty (DEC-001–016, S-8):**  
- The d100 roll-under, 100-fumble, Cost=Roll, Overflow, Failure XP, Skill Roll Pool, and General XP are all locked and invariant.   
- Difficulty grades provide a clean way to represent GURPS modifiers (e.g., Tracking +3, Climbing -3) as Skill-side adjustments without touching the die.   

**Opposed contests and base combat effects (S-1, S-3 base tier):**  
- S-1 gives a robust opposed-contest engine with Quality measures and tie-breaking.   
- S-3’s base-tier Inflict Injury and Retreat/Compel Yield are sufficient to model most of the adventure’s combat outcomes (damage, forcing retreat, surrender).   

**Hit location and injury (S-2, S-4):**  
- Zero-Step and its non-attack provenance rules allow both attacks and hazards to generate hit locations mechanically.   
- Wounds vs Injury distinction supports lasting localized states beyond HP damage, which fits the adventure’s more serious injuries.   

**Armor and defense (S-5, S-6):**  
- Armor as tags, Bypass, and Sunder integrate cleanly with Effects and Active Defense.   
- Active Defense gives defenders agency and a clear mitigation path for incoming Effects.   

**Incapacitation, death, rest, healing (S-7, S-11, S-9/S-10):**  
- HP=0 incapacitation and death thresholds provide clear end-states for severe injury.   
- Rest/Healing via Extended Tests allows modelling recovery over time, which suits a campaign that continues beyond this adventure.   

**Environmental hazards and extended tasks (S-2/S-4, S-8, S-9/S-10):**  
- Hazards like icy walls, crumbling floors, and labyrinths can be represented with difficulty grades, Extended Tests, and hazard provenance rules.   

#### 5.2 Systems needing development or scaffolding

**S-3 gated Effect contents (Part C.3):**  
- While the menu structure is Ruled, the specific Effects populating Position, Condition, Equipment, Defense, and Location tiers are **not fully enumerated** and explicitly listed as not table-ready.   
- For this adventure, you will need to either:  
  - Author a minimal subset of gated Effects (e.g., “Knocked Prone”, “Weapon Damaged”, “Armor Bypassed”, “Pinned”, “Blinded”) as Tiwas Effects, or  
  - Run combat primarily with base-tier Inflict Injury and narrative rulings, deferring formal gated Effects to later design.

**S-12 creature/campaign content (Part C.1):**  
- Creature and NPC templates are explicitly a content-authoring track, not provided by the system.   
- To run *Beyond the Vale of Madness*, you must author Tiwas stat blocks for:  
  - Ice troll  
  - Yetis  
  - Blood men  
  - Injured hunter Jrak Kul  
  - Martyrs of War members  
- This is design work, but it does not require new mechanics—only application of existing Tiwas character creation principles.

**Treasure, economy, and XP mapping (guess flagged):**  
- The adventure awards silver talents and character points (GURPS XP).   
- Tiwas General XP and any in-world currency system must be mapped manually:  
  - **Guess:** treat adventure XP awards as General XP, and silver talents as setting-specific currency with no mechanical impact beyond GM adjudication.

---

### 6. Recommendations and next steps

#### 6.1 Immediate steps to make the module playtestable

1. **Author minimal S-3 gated Effect contents**  
   - Define a small, adventure-relevant set of Condition, Equipment, Defense, and Location-tier Effects (e.g., Prone, Stunned, Weapon Damaged, Armor Bypassed, Pinned).  
   - Keep them tightly scoped to this module; later expand for general Tiwas.

2. **Create Tiwas stat blocks for key creatures and NPCs (S-12 content authoring)**  
   - Ice troll, yetis, blood men, Jrak Kul, Martyrs of War.  
   - Use the dual-mode S-12 ruling: abbreviated GM-facing stat blocks for tabletop play.   

3. **Define a simple loot and XP mapping**  
   - Map GURPS character points to Tiwas General XP.  
   - Treat silver talents as narrative currency; only introduce mechanical effects if needed.

4. **Draft a short GM conversion note for this adventure**  
   - State that all GURPS rolls are Tiwas Core Tests with difficulty grades.  
   - Clarify how hit location, armor, defense, and wounds are handled in Tiwas terms.  
   - Note any temporary scaffolding (e.g., limited Effect list).

#### 6.2 Medium-term Tiwas development priorities (informed by this module)

- **Complete S-3 gated Effect enumeration**  
  This adventure touches most of the core combat and hazard space; finishing the Effect catalogue will unlock richer play.

- **Build a small S-12 creature library**  
  Use monsters from this module as seed templates for a broader Tiwas bestiary.

- **Refine wound consequence and healing cost (OPEN-007)**  
  The module’s harsh environment and injuries make it a good testbed for wound penalties and healing difficulty.

---

### 7. Conclusion

**Decision statement:**  
- *Beyond the Vale of Madness* is **mechanically playtestable now in Tiwas** for alpha purposes, provided you:  
  - Translate all GURPS rolls into Tiwas Core Tests with difficulty grades,  
  - Author creature/NPC stat blocks and a minimal gated Effect list, and  
  - Accept that some advanced effects and wound consequences are still in design and will be handled with explicit GM rulings.

This adventure is a strong metric for Tiwas readiness: it exercises Core Tests, difficulty, opposed contests, hit location, wounds, armor, defense, incapacitation, rest/healing, hazards, and extended tasks—all of which are present at a Ruled or Locked level. The main gaps are **content** (S-12) and **enumeration** (S-3 gated Effects), not fundamental mechanics.

---

### 8. Guesses (explicitly flagged)

- **XP and currency mapping:** I inferred that GURPS character points should map to Tiwas General XP, and silver talents to narrative currency, since Tiwas does not yet define a specific economic subsystem in the corpus excerpt.  
- **Scope of gated Effects needed:** I assumed a minimal subset tailored to this adventure is sufficient for alpha play, rather than requiring full S-3 enumeration before running the module.