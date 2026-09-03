---
document:
  title: "GURPS → Tiwas Creature Conversion Scratch — Beyond the Vale of Madness (Ice Troll, Blood Man)"
  version: "0.2"
  status: "Advisory scratch/editable conversion — NOT a definitive template, NOT canonical, NOT a DEC. Authored under Tiwa's explicit session clarification of DEC-077's helper boundary (2026-09-03): advisory models may propose Tiwas-format conversions of GURPS creatures as editable scratch for Tiwa to review; Tiwa retains authorship/ownership and rules on all content."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "GPT-5.6 Luna", version: "gpt-5.6-luna"}
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-03"
  last_modified_date: "2026-09-03"
---

# GURPS → Tiwas Creature Conversion Scratch (v0.2)

**Source:** `BeyondtheValeofMadnessGURPS.pdf` (19-page GURPS one-shot, v1.2, J.C. Connors), pages 4 and 8 — the only two creatures in the adventure with full GURPS stat blocks.

**Scope note:** The adventure also narratively mentions tundra wolves, yetis, ice rats, and grave ghouls with **no GURPS stats given**. Not converted here. The two pregenerated GURPS PCs (King Coppertong, Enfys Loom) are player characters, not creature-template material, and are also not converted here.

**v0.2 changelog:** Independently reviewed by a second advisory model (GPT-5.6 Luna), whose derived-statistic and Skill-Cap recalculations matched this document exactly (cross-model validation, no discrepancies found). This revision: (a) adds an explicit Attack Resource Transaction worked example and combat-pipeline diagram Luna's pass showed were needed for table clarity; (b) adds a flag for the Inflict Injury magnitude gap that v0.1 didn't surface; (c) elevates two governance-boundary questions (Fork A/B Starting Skill tension; pre-authored Advanced Skill origin) from footnotes to formal flags, since they set precedent for every future creature template, not just these two. A separate, non-compliant conversion draft (numeric DR, damage-over-time grapple mechanic, generic non-module creatures) was also produced independently this session and is **not** incorporated — see §5.

**Authority:** This document proposes conversions only. It does not rule on any open Tiwas subsystem question, does not assign a DEC number, and is not table-ready until you accept it (in whole, in part, or with changes) and OpenCode records whatever you decide against the live register.

---

## 1. Conversion Methodology (my judgment calls — flag anything you'd do differently)

### 1.1 Attribute assignment
Tiwas has no locked GURPS↔24-attribute mapping (none exists in the register). I assigned each creature a full 1–100 value per attribute using an archetype logic (predator build for the Troll, corrosive-humanoid build for the Blood Man), anchored loosely to GURPS's relative stat spread (ST vs DX vs IQ vs HT) rather than any formula. **This is a recommendation, not a derivation** — there is no Ruled conversion procedure to derive it from.

### 1.2 Combat resolution — attack cost vs. target consequence
GURPS's flat damage dice ("1d+2 cut") don't port directly — Tiwas has no separate damage roll, and the attacker's d100 result is never the target's damage. Two independent tracks apply, and they must not be merged:

**Track A — Attacker's own resource cost (DEC-006/DEC-007):**

| Symbol | Meaning |
|---|---|
| `R` | The exact d100 rolled on the attack |
| `PE_before` | Attacker's Physical Energy before the test |
| `Cost` | = `R` (always — the roll itself, not a derived value) |
| `Overflow` | = `R − PE_before`, only if `R > PE_before`; applied as direct HP damage **to the attacker** |

*Worked example (Ice Troll, PE 220):* Icy Claws rolled at 42 → Cost 42, `PE_after` = 178, Overflow = 0. If PE were instead already down to 40 and the Troll rolled 91 → Cost 91, PE floors at 0, Overflow = 91 − 40 = **51 HP damage to the Troll itself**, not the target.

**Track B — Target consequence (DEC-023/DEC-027/DEC-032):** Only if the Troll *wins* the S-1 Opposed Contest does a declared Effect (gated by Quality per DEC-031, and by Skill-Tier per DEC-041 if it's a location-referencing Effect) apply to the target. The two tracks never combine into a formula like "roll = target damage."

### 1.3 Combat pipeline (table-use reference)

```
Named attack (Skill roll)
        ↓
   S-1 Opposed Contest (attacker Cost/Overflow resolves per Track A above,
   regardless of outcome)
        ↓
   Creature wins? ──No──→ contest resolves per S-1 outcome matrix (repeat on
        │                  mutual failure, etc.) — no Effect
       Yes
        ↓
   Declare eligible Effect (DEC-023/DEC-023.A menu; Quality gates tier, DEC-031)
        ↓
   S-2 Location Index generated, if the Effect requires one (needs Skill-Tier ≥ 2
   per DEC-041 — see §1.4)
        ↓
   S-6 Active Defense — defender's own voluntary Core Test, post-hoc mitigation
   (Model B, DEC-048). Defender's own Skill, not a stat-block number.
        ↓
   S-5 Armor check, if the target has applicable coverage
        ↓
   S-4 Injury/Wound consequence recorded
        ↓
   S-7 Incapacitation/Death check if HP reaches 0
```

**GURPS Dodge/Parry values are quoted below purely as source reference and are never carried into Tiwas mechanics.** The defender's Active Defense roll always uses the defender's own Tiwas Skill (S-6), never a number assigned to the attacker's stat block.

### 1.4 Critical cross-check finding — Skill-Tier gate
**DEC-041 requires Skill-Tier ≥ 2 (Advanced) for ANY Location Index generation — which means ANY Wound-producing Effect.** A Tier-1 attack skill can only ever produce the Base-tier Inflict Injury (HP-only, Overflow) outcome; it can never Wound. If you want these creatures capable of inflicting the "Wounded" Condition (matching GURPS's threat level — trolls and blood men are meant to actually hurt PCs, not just chip HP), their signature attacks need to be built as **Tier-2 Skills** from the start. I've done this below, but flag it because it's a non-obvious consequence of a rule you already locked, and it means **every future "dangerous" NPC needs a Tier-2+ signature attack by design, or it structurally cannot Wound.** Worth deciding whether that's an intended universal constraint on monster design or something you want to revisit. (This is related to, but distinct from, the origin-story question in §4.7.)

### 1.5 GURPS traits with no current Tiwas equivalent
Several GURPS traits on these two creatures don't map onto anything Ruled. I have **not** invented mechanics for these — they're listed as open flags in §4.

---

## 2. Ice Troll

**GURPS source (verbatim, p.4):** ST 15, DX 12, IQ 7, HT 12; HP 15, Will 11, Per 12, FP 12; Speed 6.5, Move 6, SM 0, DR 2; Dodge 9, Parry – *(source reference only — not imported, see §1.3)*. Icy Claws (13): 1d+2 cut, Reach C,1. Sharktoothed Maw (13): 1d+2 cut, Reach C. Traits: Appearance (Hideous); Bad Temper; Claws (Sharp); Regeneration (Fast, 1 HP/minute, freezing only); Regrowth (freezing only); DR 2 (freezing only). Skills: Brawling-13; Camouflage-12; Stealth-10; Tracking-11.

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

*Independently recalculated and confirmed by GPT-5.6 Luna's assessment pass — no discrepancies.*

### 2.3 Skills (DEC-005 formulas, exact)

| Skill | Tier | Formula attributes | Cap | Proposed Current | Domain |
|---|---:|---|---:|---:|---|
| Icy Claws | 2 | bsp (60) + bpp (75) | floor(135/2)=67 | 67 (veteran; see note, and §4.6) | Physical Energy |
| Sharktoothed Maw | 2 | bpp (75) + bep (75) | floor(150/2)=75 | 75 | Physical Energy |
| Brawling (general) | 1 | bpp (75) | 75 | 37 | Physical Energy |
| Camouflage | 1 | mss (60) | 60 | 30 | MP |
| Stealth | 1 | bse (60) | 60 | 30 | Physical Energy |
| Tracking | 1 | mss (60) | 60 | 30 | MP |

**Note on "Current" values:** Per DEC-005, Starting Value = floor(Cap/2). I've set the two signature attack skills to full Cap on the recommendation that named/boss NPCs are pre-built as "veterans" rather than starting characters — this is a content-authoring choice, not a rule; adjust freely. General skills left at standard Starting Value. **See §4.6 — this convention has a governance-level tension worth resolving before it's applied to more creatures.**

### 2.4 Traits and Tags mapping

| GURPS trait | Tiwas mapping | Status |
|---|---|---|
| Claws (Sharp) | `damage:slashing` Tag (DEC-080 alpha vocabulary) on both attacks | Clean map |
| Appearance (Hideous) | Flavor/GM note; no current mechanical hook | Not mechanized (no fear/reaction subsystem exists — see §4.4) |
| Bad Temper | Flavor/GM note (AI behavior: fights rather than flees) | Not mechanized |
| Regeneration (Fast, freezing only) | **Flagged, not converted** | See §4.3 |
| Regrowth (freezing only) | **Flagged, not converted** | See §4.3 |
| DR 2 (freezing only) | **Flagged, not converted** | See §4.3 / §4.5 |

---

## 3. Blood Man

**GURPS source (verbatim, p.8):** ST 13, DX 12, IQ 9, HT 12; HP 15, Will 11, Per 11, FP 12; Speed 6.0, Move 6, SM 0, DR 1; Dodge 10, Parry 10 *(source reference only — not imported, see §1.3)*. Claws (14): 1d cut, Reach C. Blood Seep: grappled + wounded victims take 1d-2 corrosive/second (Large-Area Injury, average of torso DR and least-protected DR); dead victims absorbed. Traits: Appearance (Monstrous); Combat Reflexes; Injury Tolerance (Homogenous); Night Vision 6. Skills: Brawling-14; Camouflage-12; Stealth-12.

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
| Night Vision 6 | `env:darkness` interaction — no Tag currently negates the darkness penalty | **Flagged, not converted** — see §4.8 |
| Appearance (Monstrous) | Flavor/GM note | Not mechanized (see §4.4) |
| Injury Tolerance (Homogenous) | **Flagged, not converted** | See §4.3 |
| Blood Seep (corrosive grapple DoT) | **Flagged, NOT converted — direct conflict with DEC-023.A** | See §4.2 |

---

## 4. Flagged Issues Requiring Your Ruling

These are genuine gaps or conflicts surfaced by the conversion, not judgment calls I made silently. Reordered in v0.2 to put the two items with the broadest blast radius (affecting all future creatures/combat, not just these two) first.

### 4.1 No Inflict Injury magnitude formula exists (new in v0.2 — highest priority)
`Inflict Injury` is an established Base-tier Effect (DEC-023): HP-only, distinct from Wound (DEC-032), auto-applies on a win (DEC-027). **No DEC anywhere specifies how many target HP it removes.** Wound magnitude is fully specified (`−Tier`, DEC-035.A/DEC-035.B); Injury magnitude is not. This is a corpus gap, not a creature-specific one — it blocks *any* combat resolution (PC or creature) that goes through the base tier rather than the Wound pathway, which is most of them, since Wound requires the Skill-Tier ≥ 2 gate (§1.4). Until this has a rule, I'd recommend testing these creatures through the Wound pathway only (their signature attacks already qualify, §1.4) and treating base-tier Inflict Injury combat as untestable pending your ruling.

### 4.2 Blood Seep directly conflicts with the locked "no damage-over-time" content policy
GURPS's Blood Seep is fundamentally a per-second corrosive DoT applied while grappled. DEC-023.A explicitly states as locked alpha content policy: **"no damage-over-time."** I have not converted Blood Seep into any Tiwas mechanic — doing so would mean either quietly violating DEC-023.A or quietly inventing an exception to it, and both are outside my authority. Options for you to weigh:
- Represent Blood Seep as a single-application Effect on a successful Grapple win
- Rule a scoped exception to the DoT prohibition specifically for "ongoing grapple" cases.
- Cut the ability's ongoing-damage identity entirely and represent it narratively/GM-fiat only.
- Something else.

I have not picked one of these for you.

### 4.3 No Regeneration / Regrowth / Injury Tolerance vocabulary exists
Neither the DEC-079 Conditions alpha vocabulary (14 entries) nor the DEC-080 Tags alpha vocabulary (34 entries) contains anything for "heals X per time unit," "regrows lost limbs," or "immune to called-shot/dismemberment effects." All three appear on these two creatures. Options for you to consider (not a recommendation — genuinely open):
- Extend DEC-079/DEC-080's vocabularies with new entries.
- Represent as a bespoke per-creature Trait note resolved by GM Fiat (per DEC-035.A's GM Fiat universal override) rather than a formal Tag/Condition.
- Defer — leave these two creatures without the trait until the vocabulary is extended.

### 4.4 No fear/reaction subsystem exists
GURPS's "Appearance (Hideous/Monstrous)" traits normally trigger Fright Checks. This is the same missing subsystem already tracked in your roadmap ("Fear/sanity resolution equivalent — identified as a Missing Subsystem blocking the playtest adventure"). This conversion surfaces it again for both creatures, plus the adventure's own explicit Fright Check calls (§38, §58 in the source text) that Tiwas currently has no equivalent for at all.

### 4.5 Conditional/environmental Armor Tags have no precedent
Both creatures' DR is conditional ("only in freezing temperatures"). DEC-058/DEC-062 establish Armor as a Tags/Traits system but no existing DEC addresses a Tag whose applicability depends on ambient environmental state. This needs either a new Tag-qualifier convention or a GM-Fiat carve-out — I have not proposed one.

### 4.6 Fork A/B tension on creature Starting Skill values (new in v0.2)
Both creatures here use full-Cap "veteran" values for signature skills instead of the canonical Starting Value `floor(Cap/2)` (§2.3/§3.3 notes). DEC-076 (S-12 Ruling A) forks creature generation into: (A) automated/computerized systems using **full 24-attribute generation identical to PCs with the same Core Test economy**, or (B) non-automated/tabletop systems using an abbreviated stat-block with **GM-discretion** resolution. Both creatures here are built as full 24-attribute matrices — Fork A territory. But Fork A's "identical Core Test economy" language would, read literally, mean Starting Skill also follows the PC rule (`floor(Cap/2)`), not an author-assigned full-Cap value. Letting creatures start at full Cap "because it's content, not chargen" arguably borrows Fork B's GM-discretion license into a Fork A creature — an unflagged cross-fork blend. This precedent will apply to every future creature template built this way, so I'd recommend settling it now rather than after more creatures are built on the ambiguous convention.

### 4.7 Pre-authored Tier-2+ skills without a DEC-012 origin (new in v0.2)
Advanced Skills (Tier 2+) are, per DEC-012, created *only* by a qualifying failed Double during play. Both creatures here are handed ready-made Tier-2 signature attacks (Icy Claws, Sharktoothed Maw, Claws) at creature creation, with no in-fiction "failed Double" event — this is what makes them capable of Wounding at all (§1.4). This is plausibly fine as a content-authoring convention for NPCs/creatures (DEC-076 doesn't prohibit it), but it's an assumption riding on silence in the corpus, not a settled rule. Worth an explicit ruling so all future creature templates use the same convention consistently.

### 4.8 Darkness penalty negation has no Tag
The adventure imposes a -3 attack penalty in darkness (unless the PC has Night Vision-equivalent). `env:darkness` exists as a Tag (DEC-080) but nothing currently defines what negates its effect for a creature with natural dark-adapted senses.

---

## 5. Note on the parallel Perplexity conversion draft

A separate, independently-produced conversion draft (via Perplexity) covering these same two creatures plus a generic Goblin and Dragon was also generated this session. It is **not** incorporated into this document and I'd recommend not using it as-is:

- Assigns only ~6 of 24 attributes per creature (HP/MP are then uncomputable against DEC-004).
- Represents Armor as flat numeric DR, contradicting DEC-058 (Tags/Traits only, no numeric pool).
- Represents Blood Man's Blood Seep as literal per-turn HP damage, the exact DEC-023.A violation flagged in §4.2.
- Retains raw GURPS dice notation (`1d+2 cut`) as if it were the Tiwas damage value, the exact Track A/B conflation addressed in §1.2.
- Imports GURPS Dodge/Parry as static Tiwas defense numbers, contrary to §1.3.
- Goblin and Dragon templates are generic GURPS Fantasy bestiary stand-ins, not sourced from *Beyond the Vale of Madness* itself — outside DEC-077.A's stated scope (module-sourced conversion for this specific playtest), which only the Ice Troll and Blood Man satisfy.

Its open-question framing (e.g., "should DR become a Tag or Condition?") overlaps with §4 above and isn't wrong to ask — just answered wrong by default in that draft. Nothing from it needs to survive into a revised version of this document.

---

## 6. What I Did Not Touch

- Two pregenerated GURPS PCs (King Coppertong, Enfys Loom) — not converted; say if you want these as playtest pregens.
- Unstatted narrative creatures (tundra wolves, yetis, ice rats, grave ghouls) — GURPS gives no stats for these; would need original Tiwas design work, not conversion, if wanted.
- Weapon/equipment conversion (Foeflayer axe, Brynmor's broadsword, spells, etc.) — out of scope for this creature-conversion pass.

---

## Documentarian Verification (added by OpenCode, 2026-09-03)

Stored from `C:\Users\Tiwa Pene\Downloads\Tiwas-GURPS-Creature-Conversion-Scratch-2026-09-03-v0.2.md` at Tiwa's instruction. This is advisory scratch work under DEC-077.A; supersedes the earlier v0.1 scratch (which OpenCode had appended an attack-cost correction to). Its mechanical judgments and §4 flags require Tiwa's rulings. `author_llm` remains Claude Sonnet 5. OpenCode appended as `assessor_llm` and set as `last_modified_by_llm` for the storage pass. Consistency note: v0.2 already incorporates the GPT-5.6 Luna-derived corrections (attack-cost vs target-damage, no GURPS Dodge/Parry, Wound-pathway-first) that were recorded as DEC-085 and previously applied to the v0.1 stored copy; the v0.1 stored copy's appended correction is now redundant with v0.2's integral text.
