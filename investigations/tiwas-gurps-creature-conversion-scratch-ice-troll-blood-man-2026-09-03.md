---
document:
  title: "GURPS → Tiwas Creature Conversion Scratch — Beyond the Vale of Madness (Ice Troll, Blood Man)"
  version: "0.1"
  status: "Advisory scratch/editable conversion — NOT a definitive template, NOT canonical, NOT a DEC. Authored under Tiwa's explicit session clarification of DEC-077's helper boundary (2026-09-03): advisory models may propose Tiwas-format conversions of GURPS creatures as editable scratch for Tiwa to review; Tiwa retains authorship/ownership and rules on all content."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-03"
  last_modified_date: "2026-09-03"
---

# GURPS → Tiwas Creature Conversion Scratch

**Source:** `BeyondtheValeofMadnessGURPS.pdf` (19-page GURPS one-shot, v1.2, J.C. Connors), pages 4 and 8 — the only two creatures in the adventure with full GURPS stat blocks.

**Scope note:** The adventure also narratively mentions tundra wolves, yetis, ice rats, and grave ghouls with **no GURPS stats given**. Not converted here. The two pregenerated GURPS PCs (King Coppertong, Enfys Loom) are player characters, not creature-template material, and are also not converted here — say the word if you want those too.

**Authority:** This document proposes conversions only. It does not rule on any open Tiwas subsystem question, does not assign a DEC number, and is not table-ready until you accept it (in whole, in part, or with changes) and OpenCode records whatever you decide against the live register.

---

## 1. Conversion Methodology (my judgment calls — flag anything you'd do differently)

### 1.1 Attribute assignment
Tiwas has no locked GURPS↔24-attribute mapping (none exists in the register). I assigned each creature a full 1–100 value per attribute using an archetype logic (predator build for the Troll, corrosive-humanoid build for the Blood Man), anchored loosely to GURPS's relative stat spread (ST vs DX vs IQ vs HT) rather than any formula. **This is a recommendation, not a derivation** — there is no Ruled conversion procedure to derive it from.

### 1.2 Combat resolution
GURPS's flat damage dice ("1d+2 cut") don't port directly — Tiwas has no separate damage roll. Instead:
- Each named attack becomes a **Skill** the creature rolls in an **S-1 Opposed Contest** against the PC's active or declined defense.
- "Damage" is Cost/Overflow (DEC-007) plus whatever Effect the creature selects on a win (DEC-023/DEC-023.A menu), gated by Quality (DEC-031) and Skill-Tier (DEC-041).

**CORRECTION (added by OpenCode, 2026-09-03, per GPT-5.6 Luna F-04 and Tiwa's ruling):** the above phrasing is ambiguous and should not be read as "the d100 roll = target damage." The d100 roll is the **attacker's resource cost** (DEC-007: Cost = natural roll, paid from Physical Energy). **Overflow damages the attacker's own HP, not the target.** Target consequence is a **separate quantity** produced by the declared Effect (Inflict Injury or Wound) via the opposed-contest win, not by the roll/cost/overflow value. Attack-roll cost (attacker resource), Overflow (attacker HP), and target Effect consequence must not be conflated.

### 1.3 Critical cross-check finding — Skill-Tier gate
**DEC-041 requires Skill-Tier ≥ 2 (Advanced) for ANY Location Index generation — which means ANY Wound-producing Effect.** A Tier-1 attack skill can only ever produce the Base-tier Inflict Injury (HP-only, Overflow) outcome; it can never Wound. If you want these creatures capable of inflicting the "Wounded" Condition (matching GURPS's threat level — trolls and blood men are meant to actually hurt PCs, not just chip HP), their signature attacks need to be built as **Tier-2 Skills** from the start. I've done this below, but flag it because it's a non-obvious consequence of a rule you already locked, and it means **every future "dangerous" NPC needs a Tier-2+ signature attack by design, or it structurally cannot Wound.** Worth deciding whether that's an intended universal constraint on monster design or something you want to revisit.

### 1.4 GURPS traits with no current Tiwas equivalent
Several GURPS traits on these two creatures don't map onto anything Ruled. I have **not** invented mechanics for these — they're listed as open flags in §4.

---

## 2. Ice Troll

**GURPS source (verbatim, p.4):** ST 15, DX 12, IQ 7, HT 12; HP 15, Will 11, Per 12, FP 12; Speed 6.5, Move 6, SM 0, DR 2; Dodge 9, Parry –. Icy Claws (13): 1d+2 cut, Reach C,1. Sharktoothed Maw (13): 1d+2 cut, Reach C. Traits: Appearance (Hideous); Bad Temper; Claws (Sharp); Regeneration (Fast, 1 HP/minute, freezing only); Regrowth (freezing only); DR 2 (freezing only). Skills: Brawling-13; Camouflage-12; Stealth-10; Tracking-11.

### 2.1 Attributes (proposed)

| Code | Attribute | Value | Code | Attribute | Value |
|---|---|---:|---|---|---:|
| bpp (Might) | 75 | mpp (Cunning) | 45 |
| bps (Impact) | 65 | mps (Wits) | 30 |
| bpe (Brawn) | 70 | mpe (Willpower) | 55 |
| bpx (Presence) | 55 | mpx (Glamour) | 10 |
| bsp (Agility) | 60 | msp (Acuity) | 40 |
| bss (Reflexes) | 55 | mss (Perception) | 60 |
| bse (Quickness) | 60 | mse (Alacrity) | 35 |
| bsx (Grace) | 20 | msx (Charm) | 5 |
| bep (Toughness) | 75 | mep (Focus) | 45 |
| bes (Stamina) | 65 | mes (Discipline) | 30 |
| bee (Vitality) | 80 | mee (Resolve) | 50 |
| bex (Poise) | 25 | mex (Composure) | 15 |

Logic: high Power/Endurance Body (brute predator), moderate Speed Body (fast lunging despite bulk), near-zero Social Body (feral, Hideous). Mind attributes generally low (GURPS IQ 7 is well below human baseline), except Perception (predator senses, Per 12) and Willpower (Bad Temper's stubborn tenacity, Will 11).

### 2.2 Derived Statistics (DEC-004 formulas, exact)

| Statistic | Formula | Value |
|---|---|---:|
| HP | Σ 12 Body attributes | 705 |
| MP | Σ 12 Mind attributes | 420 |
| Physical Energy | bep + bes + bee = 75+65+80 | 220 |
| Speed | bsp + bss + bse = 60+55+60 | 175 |
| Energy Regen | bep + bes = 75+65 | 140 |
| MP Regen | mep + mes = 45+30 | 75 |
| Movement Speed | floor((bsp+bss)/15) = floor(115/15) | 7 |

### 2.3 Skills (DEC-005 formulas, exact)

| Skill | Tier | Formula attributes | Cap | Proposed Current | Domain |
|---|---:|---|---:|---:|---|
| Icy Claws | 2 | bsp (60) + bpp (75) | floor(135/2)=67 | 67 (veteran; see note) | Physical Energy |
| Sharktoothed Maw | 2 | bpp (75) + bep (75) | floor(150/2)=75 | 75 | Physical Energy |
| Brawling (general) | 1 | bpp (75) | 75 | 37 | Physical Energy |
| Camouflage | 1 | mss (60) | 60 | 30 | MP |
| Stealth | 1 | bse (60) | 60 | 30 | Physical Energy |
| Tracking | 1 | mss (60) | 60 | 30 | MP |

**Note on "Current" values:** Per-DEC-005, Starting Value = floor(Cap/2). I've set the two signature attack skills to full Cap on the recommendation that named/boss NPCs are pre-built as "veterans" rather than starting characters — this is a content-authoring choice, not a rule; adjust freely. General skills left at standard Starting Value.

### 2.4 Traits and Tags mapping

| GURPS trait | Tiwas mapping | Status |
|---|---|---|
| Claws (Sharp) | `damage:slashing` Tag (DEC-080 alpha vocabulary) on both attacks | Clean map |
| Appearance (Hideous) | Flavor/GM note; no current mechanical hook | Not mechanized (no fear/reaction subsystem exists — see §4.2) |
| Bad Temper | Flavor/GM note (AI behavior: fights rather than flees) | Not mechanized |
| Regeneration (Fast, freezing only) | **Flagged, not converted** | See §4.1 |
| Regrowth (freezing only) | **Flagged, not converted** | See §4.1 |
| DR 2 (freezing only) | **Flagged, not converted** | See §4.1 / §4.3 |

---

## 3. Blood Man

**GURPS source (verbatim, p.8):** ST 13, DX 12, IQ 9, HT 12; HP 15, Will 11, Per 11, FP 12; Speed 6.0, Move 6, SM 0, DR 1; Dodge 10, Parry 10. Claws (14): 1d cut, Reach C. Blood Seep: grappled + wounded victims take 1d-2 corrosive/second (Large-Area Injury, average of torso DR and least-protected DR); dead victims absorbed. Traits: Appearance (Monstrous); Combat Reflexes; Injury Tolerance (Homogenous); Night Vision 6. Skills: Brawling-14; Camouflage-12; Stealth-12.

### 3.1 Attributes (proposed)

| Code | Attribute | Value | Code | Attribute | Value |
|---|---|---:|---|---|---:|
| bpp (Might) | 60 | mpp (Cunning) | 55 |
| bps (Impact) | 60 | mps (Wits) | 50 |
| bpe (Brawn) | 55 | mpe (Willpower) | 55 |
| bpx (Presence) | 50 | mpx (Glamour) | 10 |
| bsp (Agility) | 70 | msp (Acuity) | 55 |
| bss (Reflexes) | 75 | mss (Perception) | 65 |
| bse (Quickness) | 55 | mse (Alacrity) | 45 |
| bsx (Grace) | 30 | msx (Charm) | 5 |
| bep (Toughness) | 55 | mep (Focus) | 50 |
| bes (Stamina) | 55 | mes (Discipline) | 40 |
| bee (Vitality) | 65 | mee (Resolve) | 55 |
| bex (Poise) | 20 | mex (Composure) | 15 |

Logic: less raw Power than the Troll but notably higher Reflexes/Agility (GURPS Combat Reflexes trait, DX 12 vs troll's implied lower coordination), higher Perception (Night Vision, ambush predator), slightly higher Mind attributes overall (IQ 9 vs troll's IQ 7 — still subhuman but sharper).

### 3.2 Derived Statistics

| Statistic | Formula | Value |
|---|---|---:|
| HP | Σ 12 Body attributes | 650 |
| MP | Σ 12 Mind attributes | 500 |
| Physical Energy | bep+bes+bee = 55+55+65 | 175 |
| Speed | bsp+bss+bse = 70+75+55 | 200 |
| Energy Regen | bep+bes = 55+55 | 110 |
| MP Regen | mep+mes = 50+40 | 90 |
| Movement Speed | floor((bsp+bss)/15) = floor(145/15) | 9 |

### 3.3 Skills

| Skill | Tier | Formula attributes | Cap | Proposed Current | Domain |
|---|---:|---|---:|---:|---|
| Claws | 2 | bsp (70) + bpp (60) | floor(130/2)=65 | 65 | Physical Energy |
| Brawling (general) | 1 | bss (75) | 75 | 37 | Physical Energy |
| Stealth | 1 | bsp (70) | 70 | 35 | Physical Energy |
| Camouflage | 1 | mss (65) | 65 | 32 | MP |

### 3.4 Traits and Tags mapping

| GURPS trait | Tiwas mapping | Status |
|---|---|---|
| Claws (implied by attack) | `damage:slashing` Tag | Clean map |
| Combat Reflexes | Reflected in high bss/bsp attribute assignment | Absorbed into attributes, no separate mechanic needed |
| Night Vision 6 | `env:darkness` interaction — no Tag currently negates the darkness penalty | **Flagged, not converted** — see §4.4 |
| Appearance (Monstrous) | Flavor/GM note | Not mechanized (see §4.2) |
| Injury Tolerance (Homogenous) | **Flagged, not converted** | See §4.1 |
| Blood Seep (corrosive grapple DoT) | **Flagged, NOT converted — direct conflict with DEC-023.A** | See §4.5 — highest-priority flag in this document |

---

## 4. Flagged Issues Requiring Your Ruling

These are genuine gaps or conflicts surfaced by the conversion, not judgment calls I made silently. Listed by priority.

### 4.1 No Regeneration / Regrowth / Injury Tolerance vocabulary exists
Neither the DEC-079 Conditions alpha vocabulary (14 entries) nor the DEC-080 Tags alpha vocabulary (34 entries) contains anything for "heals X per time unit," "regrows lost limbs," or "immune to called-shot/dismemberment effects." All three appear on these two creatures. Options for you to consider (not a recommendation — genuinely open):
- Extend DEC-079/DEC-080's vocabularies with new entries.
- Represent as a bespoke per-creature Trait note resolved by GM Fiat (per DEC-035.A's GM Fiat universal override) rather than a formal Tag/Condition.
- Defer — leave these two creatures without the trait until the vocabulary is extended.

### 4.2 No fear/reaction subsystem exists
GURPS's "Appearance (Hideous/Monstrous)" traits normally trigger Fright Checks. This is the same missing subsystem already tracked in your roadmap ("Fear/sanity resolution equivalent — identified as a Missing Subsystem blocking the playtest adventure"). This conversion surfaces it again for both creatures, plus the adventure's own explicit Fright Check calls (§38, §58 in the source text) that Tiwas currently has no equivalent for at all.

### 4.3 Conditional/environmental Armor Tags have no precedent
Both creatures' DR is conditional ("only in freezing temperatures"). DEC-058/DEC-062 establish Armor as a Tags/Traits system but no existing DEC addresses a Tag whose applicability depends on ambient environmental state. This needs either a new Tag-qualifier convention or a GM-Fiat carve-out — I have not proposed one.

### 4.4 Darkness penalty negation has no Tag
The adventure imposes a -3 attack penalty in darkness (unless the PC has Night Vision-equivalent). `env:darkness` exists as a Tag (DEC-080) but nothing currently defines what negates its effect for a creature with natural dark-adapted senses.

### 4.5 Blood Seep directly conflicts with the locked "no damage-over-time" content policy
**This is the most significant finding.** GURPS's Blood Seep is fundamentally a per-second corrosive DoT applied while grappled. DEC-023.A explicitly states as locked alpha content policy: **"no damage-over-time."** I have not converted Blood Seep into any Tiwas mechanic — doing so would mean either quietly violating DEC-023.A or quietly inventing an exception to it, and both are outside my authority. Options for you to weigh:
- Represent Blood Seep as a single-application Effect on a successful Grapple win (e.g., an Impose Condition or Inflict Injury Effect triggered once per grapple-Contest-win, not per second) — compliant with DEC-023.A's one-Effect-per-win model.
- Rule a scoped exception to the DoT prohibition specifically for "ongoing grapple" cases.
- Cut the ability's ongoing-damage identity entirely and represent it narratively/GM-fiat only.
- Something else.

I have not picked one of these for you.

---

## 5. What I Did Not Touch

- Two pregenerated GURPS PCs (King Coppertong, Enfys Loom) — not converted; say if you want these as playtest pregens.
- Unstatted narrative creatures (tundra wolves, yetis, ice rats, grave ghouls) — GURPS gives no stats for these; would need original Tiwas design work, not conversion, if wanted.
- Weapon/equipment conversion (Foeflayer axe, Brynmor's broadsword, spells, etc.) — out of scope for this creature-conversion pass.

---

## Documentarian Verification (added by OpenCode, 2026-09-03)

Stored from `C:\Users\Tiwa Pene\Downloads\Tiwas-GURPS-Creature-Conversion-Scratch-2026-09-03.md` at Tiwa's instruction. This is advisory scratch work under DEC-077.A; its mechanical judgments and §4 flags require Tiwa's rulings. `author_llm` remains Claude Sonnet 5. OpenCode appended as `assessor_llm` and set as `last_modified_by_llm` for the storage pass.
