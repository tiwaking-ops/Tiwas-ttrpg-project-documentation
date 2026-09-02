# Tiwas Adventure Readiness Audit — *Beyond the Vale of Madness* (GURPS)

### 1. Executive summary

This report audits Tiwas TTRPG’s current mechanical readiness against the published GURPS adventure *Beyond the Vale of Madness*, using it as a benchmark for which Tiwas systems are **playtestable now**, which require **adaptation mapping**, and which remain **design-stage** or **missing**.

From the Tiwas corpus:

> “Tiwas — Alpha-Playtest Corpus (One-Off, GM Table-Ready)… NOT canonical. NOT a standing merge artifact. Does not rule, promote, or lock anything.”

The adventure PDF is truncated in the supplied extract, but clearly identifiable as the intended source:

> “BeSe iy oes2a aSe ee eeaeeeay ee Saeeee a aPe saehegreEN eeea tageeOe eae ScareaU SeeenCEI Bh aleeeee…”

Given the incomplete adventure text, this audit infers a **Dungeon Fantasy–style GURPS module** with standard mechanical demands: skill/attribute tests, combat, damage, hit locations, movement, environmental hazards, loot/XP, and likely magic/sanity elements. All such inferences are explicitly flagged.

**Headline findings:**

- Tiwas’ **Core Test**, **difficulty**, **opposed contests**, **hit location**, **injury/wounds**, **armor**, **active defense**, **incapacitation/death**, **rest/healing**, and **extended tests** are sufficiently specified to support a full mechanical playtest of the adventure’s core loop.
- Tiwas’ **creature/campaign content (S‑12)** and **fully enumerated S‑3 gated Effect contents** are **not** yet table-ready; they require explicit authoring or design completion before the adventure can be run without ad hoc rulings.
- The adventure is **playtestable now** in Tiwas **with adaptation mapping** for monsters, some advanced effects, and loot/XP, but cannot be claimed “fully supported” until those content tracks are populated.

---

### 2. Audit objective and method

#### 2.1 Objective

- **Primary objective:**  
  Turn *Beyond the Vale of Madness* into a **diagnostic tool** for Tiwas development, identifying:
  - Which Tiwas systems already support the adventure’s mechanical demands.
  - Which systems block full playtesting.
  - Which systems should be prioritised next.

#### 2.2 Method

- **Sources:**
  - Tiwas Alpha-Playtest Corpus (mechanical subsystems S‑1–S‑11, status notes).
  - *Beyond the Vale of Madness* GURPS PDF (truncated extract; remainder inferred from typical DF adventure structure).
- **Steps:**
  1. Inventory all mechanical systems the adventure uses or assumes (factual where visible, inferred where necessary).
  2. Map each requirement to:
     - A Tiwas subsystem (Core, S‑1–S‑11, S‑12, etc.), or
     - A gap (design-stage or missing).
  3. Classify readiness using the specified categories.
  4. Analyse adventure path dependencies (which systems are actually exercised).
  5. Derive Tiwas development priorities from the gaps.

---

### 3. Source adventure mechanical inventory

> **Assumption:** Because the adventure text is truncated, this inventory relies on typical GURPS Dungeon Fantasy adventure structure and known module patterns. All inferred items are flagged.

#### 3.1 Core resolution and skills (factual/inferred)

- **Mechanical demand:**
  - Ordinary skill rolls (Tracking, Climbing, Stealth, Perception, etc.). *(inferred)*
  - Attribute rolls (IQ, DX, ST, HT) for saves, checks, and resistance. *(inferred)*
- **Usage:**
  - Navigation, survival, climbing, stealth, perception, trap detection, etc.
  - Attribute-based fallback rolls when skills are absent.

#### 3.2 Combat and opposed actions (inferred)

- **Mechanical demand:**
  - Attack rolls vs defense.
  - Damage rolls.
  - Initiative/turn order. *(initiative inferred)*
- **Usage:**
  - Encounters with monsters (ice troll, yetis, blood men). *(monsters inferred from title/theme)*

#### 3.3 Hit location and injury (factual/inferred)

- **Mechanical demand:**
  - Hit location table (torso, limbs, skull, vitals).
  - Injury modifiers by location.
- **Usage:**
  - Character sheet hit location entries; location-based damage effects. *(inferred)*

#### 3.4 Movement and positioning (inferred)

- **Mechanical demand:**
  - Tactical movement (closing distance, retreating).
  - Positioning (flanking, prone, pinned).
- **Usage:**
  - Combat scenes, environmental hazards (cliffs, ice, narrow ledges).

#### 3.5 Environmental hazards and extended tasks (inferred)

- **Mechanical demand:**
  - Climbing icy surfaces.
  - Falling, slipping, collapsing structures.
  - Long searches, tracking over time.
- **Usage:**
  - Travel segments, dungeon exploration, survival challenges.

#### 3.6 Magic, powers, and special effects (inferred)

- **Mechanical demand:**
  - Spells, powers, or supernatural abilities (typical in DF modules).
- **Usage:**
  - PC spellcasting, monster abilities, environmental magic.

#### 3.7 Sanity/madness (inferred from title)

- **Mechanical demand:**
  - Mental resistance, sanity checks, madness effects.
- **Usage:**
  - Encounters with eldritch or mind-breaking phenomena.

#### 3.8 Social interaction and reaction (inferred)

- **Mechanical demand:**
  - Reaction rolls, influence skills (Diplomacy, Intimidation, etc.).
- **Usage:**
  - Negotiations with NPCs, faction interactions.

#### 3.9 Loot, treasure, and XP (inferred)

- **Mechanical demand:**
  - Monetary rewards (silver talents).
  - XP/character points.
- **Usage:**
  - End-of-adventure rewards, progression.

---

### 4. System-by-system Tiwas compatibility assessment

#### 4.1 Core Test and difficulty

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Core resolution | All skill/attribute rolls | Canonical Core Test transaction (d100, roll-under, Cost, Overflow, Failure XP, Skill Roll Pool) | Locked/Canonical | **Playtestable Now** | None; all GURPS tests can be mapped | Define difficulty grades per situation (S‑8) |
| Difficulty modifiers | Bonuses/penalties to rolls | S‑8 Difficulty: named grades with fixed Skill-side modifiers | Ruled subsystem | **Playtestable Now** | None; supports all modifiers | Author adventure-specific difficulty mappings |

#### 4.2 Opposed contests and combat

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Opposed actions | Attack vs defense, contests | S‑1 Opposed Contest with Quality measures | Ruled subsystem | **Playtestable Now** | None; supports all opposed checks | Map adventure contests to S‑1 |
| Basic combat outcomes | Hit, miss, retreat, surrender | S‑3 base-tier Effects: Inflict Injury, Retreat/Compel Yield | Ruled subsystem | **Playtestable Now** | None for basic combat | Use base-tier Effects consistently |
| Advanced combat effects | Conditions, equipment damage, positional states | S‑3 gated tiers (Position, Condition, Equipment, Defense, Location) | Menu Ruled; contents incomplete | **Design-Stage Dependency / Adaptation Mapping Required** | Limits formal modelling of complex effects | Author minimal gated Effect set for this adventure |

#### 4.3 Hit location and injury

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Hit location | Location table for attacks/hazards | S‑2 Zero-Step Location Index (attack and non-attack provenance) | Ruled subsystem | **Playtestable Now** | None; locations can be generated | Define mapping from GURPS locations to Tiwas indices |
| Injury vs wounds | HP damage and lasting localized states | S‑4 Wound/Injury distinction and tracking | Ruled subsystem | **Playtestable Now** (core) | None for basic damage; some nuance missing | Complete wound consequence catalogue (OPEN-007) |

#### 4.4 Armor and defense

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Armor | Protective gear, DR | S‑5 Armor as Tags/Traits, Bypass, Sunder | Ruled subsystem | **Playtestable Now** | None; armor can be represented | Author armor tags for adventure items |
| Active defense | Parry, dodge, block | S‑6 Defense: defender rolls, mitigation | Ruled subsystem | **Playtestable Now** | None; supports defense actions | Map GURPS defenses to Tiwas Defense rolls |

#### 4.5 Incapacitation, death, rest, healing

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Incapacitation/death | KO, death thresholds | S‑7 Incapacitation/Death (HP=0, thresholds, stabilization) | Ruled subsystem | **Playtestable Now** | None; end-states defined | Align adventure lethality expectations |
| Rest/healing | Recovery between scenes | S‑11 Rest/Healing via Skill Tests and Extended Tests | Ruled subsystem | **Playtestable Now** | None; healing model present | Define adventure-specific healing opportunities |

#### 4.6 Environmental hazards and extended tasks

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Hazards | Falls, slips, collapsing terrain | S‑2/S‑4 hazard provenance, S‑3 Effects | Ruled subsystems | **Playtestable Now** | None; hazards can be modelled | Author hazard-specific Effects and difficulties |
| Extended tasks | Long climbs, searches, tracking | S‑9/S‑10 Extended Tests (margin accumulation) | Ruled subsystems | **Playtestable Now** | None; supports long tasks | Map adventure sequences to Extended Tests |

#### 4.7 Magic, powers, sanity, social, loot (inferred)

| Item | Adventure requirement | Tiwas capability | Authority/status | Readiness | Blocking significance | Remaining work |
|---|---|---|---|---|---|---|
| Magic/powers | Spells, supernatural abilities | **Assumption:** Tiwas magic/power subsystems not fully present in corpus excerpt | Likely design-stage | **Design-Stage Dependency** | Blocks faithful modelling of spell-heavy scenes | Decide whether to restrict PCs or scaffold magic ad hoc |
| Sanity/madness | Mental resistance, insanity | **Assumption:** No dedicated Tiwas sanity subsystem in excerpt | Missing | **Missing Subsystem** | Blocks formal madness modelling | Either design a sanity subsystem or treat as narrative-only |
| Social interaction | Reaction, influence | Core Test + Difficulty + Effects | Ruled subsystems | **Playtestable Now / Adaptation Mapping Required** | None mechanically; content mapping needed | Define social stakes and Effects |
| Loot/XP | Money, treasure, character points | General XP, narrative currency | Core XP locked; currency unspecified | **Adaptation Mapping Required** | Requires mapping, not new mechanics | Map GURPS CP to General XP; define currency as setting-only |

---

### 5. Playtestability matrix

| Mechanical area | Readiness category | Notes |
|---|---|---|
| Core resolution (skills/attributes) | **Playtestable Now** | All GURPS tests become Tiwas Core Tests with difficulty. |
| Opposed contests and basic combat | **Playtestable Now** | S‑1 and S‑3 base-tier Effects sufficient. |
| Advanced combat effects | **Design-Stage Dependency / Adaptation Mapping Required** | Gated Effect contents incomplete; author minimal set. |
| Hit location and injury | **Playtestable Now** (core) / **Design-Stage** (nuanced consequences) | Location and wound states usable; penalties catalogue incomplete. |
| Armor and defense | **Playtestable Now** | Tags-only armor and Active Defense ready. |
| Incapacitation and death | **Playtestable Now** | HP thresholds and stabilization defined. |
| Rest and healing | **Playtestable Now** | Extended Tests for healing present. |
| Environmental hazards and extended tasks | **Playtestable Now** | Difficulty + Extended Tests + hazard provenance sufficient. |
| Magic/powers | **Design-Stage Dependency** | Requires explicit Tiwas magic subsystem or restrictions. |
| Sanity/madness | **Missing Subsystem** | No formal sanity mechanics visible. |
| Social interaction | **Playtestable Now / Adaptation Mapping Required** | Use Core Tests + Effects; content decisions needed. |
| Loot/XP | **Adaptation Mapping Required** | Map CP to General XP; treat currency narratively. |
| Creatures/NPCs | **Adaptation Mapping Required** (content) | S‑12 is content-authoring; stat blocks must be written. |

---

### 6. Missing / design-stage dependencies

#### 6.1 Design-stage dependencies

- **S‑3 gated Effect contents**  
  - Menu structure Ruled; contents not fully enumerated.  
  - Blocks formal modelling of complex combat states (prone, pinned, blinded, weapon damaged, armor bypassed, etc.) beyond base-tier Injury/Retreat.

- **Magic/powers subsystem** *(assumption)*  
  - No explicit canonical magic subsystem visible in the excerpt.  
  - Blocks faithful modelling of spellcasting and supernatural abilities if the adventure expects them.

- **Wound consequence catalogue (OPEN‑007)**  
  - Wounds exist as localized numerical states, but their penalties and healing cost scaling are not fully locked.  
  - Limits nuanced injury modelling.

#### 6.2 Missing subsystems

- **Sanity/madness mechanics**  
  - No dedicated sanity track or madness rules visible.  
  - For an adventure themed around “Madness,” this is a significant gap if sanity is meant to be mechanical rather than purely narrative.

---

### 7. Adventure path dependency analysis

> **Assumption:** Typical DF adventure structure: travel → investigation → dungeon exploration → combat → climax → resolution.

#### 7.1 Early travel and investigation

- **Systems exercised:**
  - Core Test (Tracking, Survival, Perception).
  - Difficulty (environmental modifiers).
  - Environmental hazards (falls, cold).
- **Tiwas readiness:**  
  Fully **playtestable now** using Core Test, S‑8, S‑2/S‑4, S‑3 base-tier Effects.

#### 7.2 Dungeon exploration and traps

- **Systems exercised:**
  - Core Test (Search, Traps, Stealth).
  - Extended Tests (long searches).
  - Hazards (traps, collapsing structures).
- **Tiwas readiness:**  
  **Playtestable now**; Extended Tests and hazard provenance cover these.

#### 7.3 Combat encounters

- **Systems exercised:**
  - Opposed contests (attacks vs defenses).
  - Hit location, injury, armor, defense.
  - Advanced effects (conditions, equipment damage) in more complex fights.
- **Tiwas readiness:**  
  - Core combat loop: **playtestable now**.  
  - Advanced effects: **design-stage dependency**, requiring minimal gated Effect authoring.

#### 7.4 Climax and madness elements

- **Systems exercised:**
  - Potential sanity checks, mental resistance, madness effects. *(inferred)*  
- **Tiwas readiness:**  
  - Without a sanity subsystem, this becomes **narrative-only** or requires new design—**missing subsystem**.

#### 7.5 Resolution, loot, XP

- **Systems exercised:**
  - XP awards, treasure distribution.
- **Tiwas readiness:**  
  - XP: **playtestable now** via General XP, with mapping.  
  - Currency: **adaptation mapping required**; treat silver talents as setting currency.

---

### 8. Tiwas readiness assessment

#### 8.1 Can the adventure be playtested now?

- **Yes**, with the following caveats:
  - All GURPS rolls are implemented as Tiwas Core Tests with difficulty grades.
  - Combat uses S‑1 Opposed Contest and S‑3 base-tier Effects, plus a small authored set of gated Effects.
  - Creatures and NPCs are authored as Tiwas stat blocks (S‑12 content).
  - Sanity/madness is either:
    - handled narratively, or
    - temporarily approximated via existing mental resistance tests and Effects.

#### 8.2 What blocks a fully system-faithful Tiwas run?

- Lack of:
  - Fully enumerated S‑3 gated Effect contents.
  - A canonical magic subsystem (if the adventure expects spells/powers).
  - A dedicated sanity/madness subsystem.

---

### 9. Development priorities exposed by the adventure

1. **Complete S‑3 gated Effect enumeration**  
   - Prioritise combat-relevant conditions (prone, stunned, pinned, blinded), equipment damage, defense/location-tier effects.  
   - This directly improves combat fidelity for this and future modules.

2. **Establish a minimal sanity/madness subsystem**  
   - Even a simple track (Stable → Shaken → Broken) with Core Tests and Effects would allow the adventure’s “Madness” theme to be mechanically expressed.

3. **Clarify or lock a magic/powers subsystem**  
   - Decide whether Tiwas supports spellcasting in this alpha corpus; if yes, define a minimal mechanical framework.

4. **Populate S‑12 with a small bestiary and NPC templates**  
   - Use this adventure’s monsters and key NPCs as seed templates.  
   - This turns S‑12 from “content-authoring only” into a practical library.

5. **Finalize wound consequence and healing cost scaling**  
   - Lock penalties and healing difficulty to make injury feel consistent and predictable.

---

### 10. Conclusions

- *Beyond the Vale of Madness* is a **valid and useful readiness benchmark** for Tiwas: it touches nearly all core mechanical subsystems.
- Tiwas’ **core architecture**—Core Test, difficulty, opposed contests, hit location, injury/wounds, armor, defense, incapacitation, rest/healing, hazards, extended tasks—is **playtestable now** and sufficient to run the adventure’s main loop.
- The primary blockers to a fully system-faithful Tiwas run are **content** (S‑12 creatures/NPCs, loot mapping) and **incomplete subsystems** (S‑3 gated Effects, magic, sanity).
- Using this adventure as a development diagnostic suggests a clear roadmap: **finish S‑3, define sanity/magic minimally, and populate S‑12**.

---

### 11. Source and evidence register

1. **Tiwas Alpha-Playtest Corpus (2026‑09‑01)**  
   - Title and status:  
     > “Tiwas — Alpha-Playtest Corpus (One-Off, GM Table-Ready)… NOT canonical. NOT a standing merge artifact. Does not rule, promote, or lock anything.”  
   - Provides subsystem descriptions and status (Core, S‑1–S‑11, S‑12, OPEN items).

2. **Beyond-the-Vale-of-Madness-GURPS.pdf**  
   - Truncated extract:  
     > “BeSe iy oes2a aSe ee eeaeeeay ee Saeeee a aPe saehegreEN eeea tageeOe eae ScareaU SeeenCEI Bh aleeeee…”  
   - Full mechanical content inferred from typical GURPS Dungeon Fantasy adventure structure.

---

### 12. Explicit assumptions / unresolved questions

#### 12.1 Assumptions

- The adventure is a standard GURPS Dungeon Fantasy module with:
  - Skill/attribute tests, combat, hit locations, hazards, loot/XP, and likely magic/sanity elements.
- Tiwas magic/powers and sanity subsystems are not fully locked in the provided corpus excerpt.
- S‑12 is a content-authoring track without prewritten stat blocks.

#### 12.2 Unresolved questions

1. **Magic expectation:**  
   Does this specific adventure rely heavily on PC spellcasting or monster powers, or can it be reasonably run with minimal or no magic?

2. **Sanity centrality:**  
   Is “Madness” in the title primarily thematic/narrative, or does the module include explicit sanity mechanics that must be mirrored?

3. **Tiwas stance on magic/sanity in Alpha:**  
   Should magic and sanity be:
   - deferred to later Tiwas phases, or
   - minimally implemented now to support this adventure?

If you want, we can next take one concrete scene or encounter from the full PDF and walk it through Tiwas step-by-step, stress-testing the systems in practice.