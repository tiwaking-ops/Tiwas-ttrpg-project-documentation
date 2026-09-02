---
document:
  title: "Perplexity — Creature Creation Development Ideas (GURPS → Tiwas Conversion Framework) for the Playtest"
  version: "1.0"
  status: "Advisory scratch/development transcript — NOT a definitive template, NOT canonical, NOT a DEC. Authored under DEC-077.A: advisory models may propose Tiwas-format conversions of GURPS creatures as editable scratch for Tiwa to review; Tiwa retains authorship/ownership and rules on all content."
provenance:
  author_llm: {name: "Perplexity", version: "unknown"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-03"
  last_modified_date: "2026-09-03"
---

# Perplexity — Creature Creation Development Ideas (GURPS → Tiwas)

**Source:** PDF transcript `perplexity - I want to create creatures for the playtest. 5.4 S.pdf` (8 pages, 2026-09-03). Transcribed/extracted to markdown by OpenCode for repository storage. GURPS source: `Beyond-the-Vale-of-Madness-GURPS.pdf` (not committed; copyrighted third-party material, gitignored).

**Authority:** Advisory scratch under DEC-077.A. Proposes conversions only; rules nothing. Not table-ready until Tiwa accepts and OpenCode records.

---

## 1. Conversion Framework (as proposed by Perplexity)

**GURPS → Tiwas attribute mapping (proposed):**
- ST → Strength (Body)
- DX → Dexterity (Body)
- HT → Health/Stamina (Body)
- IQ → Intelligence (Mind)
- HP → Hit Points (reference only)
- Will → Willpower (Mind)
- Per → Perception (Mind)
- Speed → initiative/movement reference
- Move → Movement Speed
- DR → Tags/Conditions
- SM → Size modifier (affects hit-location granularity per DEC-041)
- GURPS Skills → Tiwas Skills (tier by governing attributes)
- GURPS Advantages/Disadvantages → Tags and Conditions (DEC-079/DEC-080)
- Attacks → attack profiles with HP damage + potential Wound Effects (DEC-032–039)

---

## 2. ICE TROLL — Creature Template (Perplexity working draft)

- Threat Level: Moderate (solo playtest encounter)
- Size: SM 0
- Location Tier: promotes to Tier 1 on failed attacks (DEC-040)

| Body | Mind |
|---|---|
| Strength 75 | Intelligence 35 |
| Dexterity 60 | Willpower 55 |
| Stamina 60 | Perception 60 |

Derived: HP 15 (GURPS reference), Speed 6.5, Movement Speed 6.
Skills: Brawling 70 (DX+2 equiv, Tier 1), Intimidation 43, Tracking 60.
Attacks: Claw (Brawling 70, 1d+2 cut), Bite (Brawling 70, 1d+1 cut, Reach C), `damage:slashing` tags.
Defenses: DR 2 (Fur), Dodge 9–10.
Special Tags/Conditions: `env:cold_resistant`, `phys:enhanced_move`, `phys:sharp_claws`, `phys:sharp_teeth`, `phys:peripheral_vision`, `ment:bad_temper`, `phys:quadruped`.
Anatomical mapping (DEC-041): Tier-1 zones Torso/Head/Limbs; left/right by digit parity; Fur DR 2 uniform.

Combat tactics: rush target; Will roll to retreat at ≤0 HP; All-Out Attack when pressed; starts adjacent to bone pile.

---

## 3. BLOOD MAN — Creature Template (Perplexity working draft)

- Threat Level: Moderate–High (grappling danger)
- Size: SM 0
- Location Tier: Tier 1 on promoted failed attacks

| Body | Mind |
|---|---|
| Strength 65 | Intelligence 35 |
| Dexterity 60 | Willpower 55 |
| Stamina 60 | Perception 60 |

Derived: HP 15, Speed 6.0, Movement Speed 6.
Skills: Brawling 65–70, Grappling 65.
Attacks: Claw (Brawling 65, 1d cut, triggers Blood Seep on wound), Bite (Brawling 65, 1d+1 cut).
**Blood Seep (flagged):** Trigger = target wounded + grappled; Effect = ongoing HP damage per turn; counter = break grapple (Opposed Contest). **Directly conflicts with DEC-023.A "no damage-over-time" policy.**
Defenses: DR 0, Dodge 9.
Tags: `phys:blood_covered`, `phys:sharp_claws`, `ment:relentless`, `phys:grapple_focus`.
Tactics: wound → grapple → maintain to activate Blood Seep → focus one target.

---

## 4. GOBLIN — Creature Template (Perplexity working draft)

- Threat Level: Low–Moderate (swarm/grunt)
- Size: SM -1
- Location Tier: Tier 0 default

| Body | Mind |
|---|---|
| Strength 45–50 | Intelligence 45–50 |
| Dexterity 55–60 | Willpower 50 |
| Stamina 50–55 | Perception 55 |

Derived: HP 10, Speed 5.5–6.0, Movement Speed 6.
Skills: Stealth 60, Shortsword 58, Throwing 58.
Attacks: Shortsword 58 (1d-1 cut), Dagger Throw 58 (1d-2 imp, Range 10/20), Bite 55 (1d-2 cut).
Defenses: DR 0–1 (leather), Dodge 8–9.
Tags: `phys:night_vision`, `phys:sharp_teeth`, `ment:cowardice`, `ment:greed`, `soc:tribal`.
Tactics: ambush/stealth, numbers advantage, retreat when odds turn, may carry copper/trinkets.
Note: Goblin has**no GURPS stat block in the source PDF excerpts** — Perplexity invented a standard GURPS Fantasy template.

---

## 5. DRAGON — Template Framework (Perplexity, "if present in BToV-Madness")

- Threat Level: High (boss)
- Size: SM +2 to +4
- Location Tier: Tier 2 (fine granularity per DEC-041)

| Body | Mind |
|---|---|
| Strength 90–120 | Intelligence 50–70 |
| Dexterity 50–70 | Willpower 60–80 |
| Stamina 80–100 | Perception 60–75 |

HP 25–40+, Speed 7.0–9.0, Move Ground 6–8 / Air 12–20.
Attacks: Bite 70–80 (2d+4 cut), Claw 70–80 (2d+2 cut, ×2), Tail 65–75 (2d+3 cr), Breath Weapon (variable, recharge mechanic needed).
Defenses: DR 4–8 (scales, location-varying), Dodge 10–12, Parry 10–11.
Tags: `phys:flight`, `phys:fire_breath` (or element), `phys:thick_scales`, `phys:enhanced_move`, `ment:frightening`, `phys:wings`.
Anatomical mapping (Tier 2): Head/Neck/Torso/Wings(×2)/Legs(×2)/Tail; subdivision per DEC-042; scale DR location-based.
Note: No Dragon stat block appears in the source PDF excerpts — this is a generalized framework, not a conversion.

---

## 6. Perplexity's Open Questions (for Tiwa's ruling)

1. **GURPS Skill Levels → Tiwas Skill Values:** use flat values (as Perplexity did) or recalculate via Tiwas formula (`floor(Cap/2)`, Cap = floor(avg(Tier attributes)))?
2. **GURPS Advantages → Tags:** complete advantage-to-tag conversion table for consistency?
3. **DR in Tiwas:** should natural DR become a `phys:damage_resistance` Tag with magnitude, or a Condition?
4. **Breath Weapons / Special Attacks:** not in DEC-080 Tag list — custom S-3 Effects or new Tags in `phys:`/`magic:` namespace?
5. **Creature HP Formula:** keep GURPS HP as-is for playtest, or recalculate via Tiwas derived-stat formula (D1 §4)?

---

## 7. Documentarian Notes (OpenCode)

- Transcribed from 8-page PDF transcript; text extracted via pypdf (some character-encoding artifacts normalized: `→`, `,`, `?` where extraction was lossy).
- The original Perplexity sources cited external GURPS resources (SJGames, GURPS wiki, fandom, third-party GURPS PDFs, Scribd/Reddit links) to derive the GURPS side of the conversions.
- **GURPS stat-block source concern:** the Ice Troll and Blood Man conversions reference the BToV-Madness PDF; the Goblin (no source stat block) and Dragon (framework) are **original inventions** by Perplexity, not conversions — flagged because DEC-077.A authorizes *conversion* work, not original creature authorship, so these two may exceed the amendment's scope.
- All values remain provisional under DEC-077.A pending Tiwa's rulings; nothing is recorded against the register from this document yet.
- Perplexity's "Blood Seep ongoing DoT" conflicts with DEC-023.A's locked no-damage-over-time policy (same flag raised in Claude's conversion scratch §4.5) — needs a ruling.
