---
document:
  title: "Tiwas — Human-Templated Mirror Combat Stress Test v2: Playtest Design Brief"
  version: "0.1 (design brief — executed same session per Tiwa's request)"
  status: "Advisory / Non-canonical. No DEC assigned. Scenario conventions below are playtest-scoped, not rules."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
---

# Tiwas — Human-Templated Mirror Combat Stress Test v2

**Purpose.** Exercise the current Ruled combat stack more completely than the 2026-09-10
mirror-match brief, specifically: (1) full-depth Armor Bypass resolution now that DEC-137
(Human v1 Location Address Template) closes L-009/L-010; (2) mid-combat General XP
attribute growth under a stated house convention; (3) mid-combat Advanced Skill creation
under DEC-012; (4) the "Impose Condition: Wounded" Effect and DEC-102 Wound target
selection, which the prior playtest never reached (Objective 8, unreachable by design).
Two mechanically identical, Human-templated combatants ("Alpha"/"Beta").

---

## 1. Combatant baseline

All 24 attributes = **50** for both combatants (identical to the 2026-09-10 baseline, for
direct comparability). Per DEC-076 Ruling A, automated combatants use full 24-attribute
generation. Per DEC-102(1), automated playtest Characters are **creatures** for
Wound-target-type purposes (Attribute wounds only, random tie-break).

### 1.1 Derived statistics (identical, live-recalculated per DEC-004 as attributes change)

| Stat | Formula | Initial value |
|---|---:|---:|
| HP (max) | Σ 12 Body attributes | 600 |
| MP (max) | Σ 12 Mind attributes | 600 |
| Physical Energy | bep+bes+bee | 150 |
| Speed | bsp+bss+bse | 150 |
| Energy Regen | bep+bes | 100 |
| MP Regen | mep+mes | 100 |
| Movement Speed | floor((bsp+bss)/15) | 6 |

Current HP is tracked separately from HP max; it starts equal to HP max and is reduced
only by Overflow (DEC-007) and Inflict Injury contest-delta (DEC-104). It is **uncapped
and may go negative** (DEC-108); forced incapacitation triggers at HP ≤ 0 (DEC-052).

---

## 2. Skill loadout (9 skills, all Tier-2 at start)

`Cap = floor((50+50)/2) = 50` → `Start = floor(50/2) = 25` for every starting skill
(identical since all attributes = 50). Attribute-pair choices are a **design choice**
(flagged §9.1) affecting only DEC-102 Wound-target attribution, not any number.

| Skill | Attributes | Role | Paired S-3 Effect |
|---|---|---|---|
| Attack | bpp+bps | Offense | Inflict Injury (Base, HP contest-delta) |
| Grapple | bpp+bsp | Offense | Impose Condition: Grappled |
| Trip | bsp+bss | Offense | Knock Prone (DEC-113 Tier 1) |
| Disarm | bss+bsx | Offense | Disarm/Break Hold (DEC-028, Tag+Location, Tier 1) |
| Equipment Damage | bpp+bpe | Offense | Equipment Damage (Tag+Location, Tier 1) |
| **Wound** | bps+bpe | Offense (NEW this brief) | Impose Condition: Wounded (DEC-033/035.A, Location Tier 1) |
| **Armor Bypass** | bsp+bsx | Offense (unlocked this brief) | Armor Bypass — the sole Tier-2 Effect (DEC-113 R2), resolved via the DEC-137 full address (DEC-136 R1) |
| Defense | bss+bse | Defense | Active Defense roll (no Effect) |
| Guard | bep+bee | Defense | Active Defense roll (no Effect) |

All Body-domain → Physical Energy resource pool (DEC-012.3).

**Offense-skill selection (per your instruction):** each turn the acting combatant selects
uniformly at random among its **currently unlocked** offense skills — including any
offense-type Advanced Skill created mid-combat (see §4; this is a deliberate change from
the 2026-09-10 brief's permanent exclusion of newly created skills).

**Defense-skill selection (per your instruction):** the defender always uses whichever of
its current defensive skills (Defense, Guard, or a defense-type Advanced Skill) currently
has the **highest numeric value**; ties broken alphabetically by skill name (consistent
with §3's attribute tiebreak convention).

---

## 3. General XP — mandatory immediate spend (house rule, this playtest only)

**Not a Tiwas rule** — a playtest-scoped convention per your explicit instruction:

> Whenever a combatant holds General XP (DEC-011: Skill Roll Pool remainder after the
> DEC-010 cascade), it is **immediately** spent to increase the combatant's **lowest
> current attribute(s)** by 1, repeated while affordable (cost of +1 = current value,
> DEC-011). **Tie-break: alphabetical order of the 3-letter attribute code** (e.g. `bee`
> before `bep`).

This never touches Skill Roll Pool advancement (DEC-010, which stays scoped to the
just-failed skill) — it only governs where the **remainder** goes. Every attribute
increase live-recalculates HP/MP/PE/Speed/Regen/Movement Speed and every Skill Cap that
uses that attribute (DEC-004).

---

## 4. Advanced Skill creation (mid-combat, per your instruction)

On a qualifying failed Double (DEC-012, DEC-001 doubles list, 100 always qualifies):

1. New Skill Tier = failed skill's Tier + 1.
2. **Attribute formula = all attributes already in the failed skill's formula, plus one
   additional attribute not already present, chosen randomly** (automated character,
   DEC-102-pattern for random selection) — this matches canonical DEC-012 exactly; no
   deviation.
3. New Cap recalculated from the complete attribute set (DEC-005).
4. Starting Value = **1** (playtest convention carried from the 2026-09-10 brief, not the
   1d100-vs-Cap alternative).
5. Resource domain retained from Tier-1 lineage (Body → PE, DEC-012.3).
6. **Effect/role inheritance (playtest convention, flagged):** the new skill inherits its
   parent's role (offense with the same paired Effect, or defense with no Effect) and
   **joins the corresponding random-selection pool immediately** — unlike the 2026-09-10
   brief, it is not excluded from future selection. Effect Tier for this skill going
   forward = its own (now higher) Skill-Tier, per DEC-107.

---

## 5. Equipment & Tags (identical loadout, both combatants)

| Item | Tags | Bound location (DEC-137, parent-covers-children per L-007/L-012) |
|---|---|---|
| Weapon | `slot:main_hand`, `state:held`, `offense:melee`, `damage:slashing`, `handling:light` | Arms (coarse; satisfies Disarm/Equipment Damage triggers when struck zone = Arms) |
| Body armor | `slot:body`, `state:worn`, `defense:armor` | Torso → **Chest** (DEC-137 range 26–35, covers wall/Heart/Lungs as children) |
| Helmet | `slot:head`, `state:worn`, `defense:armor` | Head → **Skull** (DEC-137 range 76–91) |

Armor deliberately does **not** cover Legs, Neck, Abdomen, Pelvis, Groin, Spine, Shoulder–
Hand, Eyes/Ears/Nose/Jaw — so Armor Bypass has both a hit and a miss condition to exercise
(DEC-030 fail-and-fall-back is reachable when the struck sub-location has no bound armor).

---

## 6. Combat procedure

### 6.1 Turn structure
Speed-based turn order (DEC-095); tie → natural-roll reroll until broken. One substantive
combat action per turn = one S-1 melee exchange. **DEC-106 automated-creature multi-attack
is deliberately NOT used this playtest** — your stated rule ("randomly select an attack
skill" — singular) overrides DEC-106(2)'s "use all legal attacks back-to-back" default for
automated combatants without a GM present. Flagged in §9.2 as an explicit scope choice,
not a silent contradiction.

### 6.2 Exchange algorithm (per DEC-105/097/103/104 — identical structure to the
2026-09-10 brief, re-verified against the register)

1. Actor rolls their randomly-selected offense skill; Defender rolls their highest-value
   defensive skill. This single pair of rolls **is** the S-1 opposed contest (DEC-013) and
   supplies both Margins for DEC-096/097/103/104 — no separate third roll.
2. **Quality mode: Margin** (`Skill − Roll`) — DEC-013 default for melee/precision use
   cases; both-fail → repeat (§13.4); exact-Quality-tie double-success → repeat (§13.5).
3. Defender wins → attack fails, no counter-Effect (DEC-101).
4. Attacker wins → resolve the paired Effect:
   - **Attack → Inflict Injury (HP):** damage = Attacker Margin − Defender Margin (0 if
     Defender's AD failed), never < 0 on a win (DEC-104).
   - **Grapple / Trip / Wound → Condition/Effect, no Tag gate:** these three are not
     among DEC-028's three Tag+Location-gated Effects — they apply once the DEC-041
     Skill-Tier≥2 gate and a generated Location Index exist, no fail-and-fall-back check.
   - **Disarm / Equipment Damage / Armor Bypass → Tag+Location gated (DEC-028/114 R2):**
     resolve Location Index first (§7), then Tag-check; mismatch → DEC-030
     fail-and-fall-back to Base Inflict Injury (HP-only).
   - All non-HP Effects: **Effect Tier = actor's Skill-Tier; Magnitude = Effect Tier**
     (`Z = −Y`, DEC-107), then DEC-103 Skill-Tier shred (Atk Tier vs Def Tier of the
     skill just rolled) + margin de-escalation (successful-AD margin only), unified carry
     rule to Tier-0 negation.
5. Recovery (DEC-008) for both, always last: `floor(Regen/2)` to the spent pool, clamped.
6. Failure XP/Skill Roll Pool (DEC-009/010) resolved for both, every exchange.
7. General XP remainder spent immediately per §3.
8. Failed-Double check (DEC-012) for both rolls; Advanced Skill creation per §4.

### 6.3 Termination
First HP ≤ 0 for either combatant (DEC-052 forced incapacitation) ends the encounter — a
1v1 fight has no remaining valid target once one side is down. A 400-exchange safety cap
is imposed for log-length control if neither reaches HP ≤ 0 (not a Ruled stopping
condition — your call if hit).

---

## 7. Location Index resolution

**Zero-Step** (DEC-014): exchange the tens/units digits of the actor's natural roll;
`00`→100.

| Effect | Depth | Table |
|---|---|---|
| Grapple, Trip, Disarm, Equipment Damage, Wound | Tier 1 (coarse) | DEC-100 quartiles: 1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head |
| Armor Bypass | Tier 2 (full address — the only Tier-2 Effect, DEC-113 R2) | DEC-137 Human v1 table (full leaf resolution; **not** truncated to Skill-Tier depth — see §9.3) |

Laterality: Zero-Step digit parity, odd=left/even=right (DEC-041(3)), recorded for flavor;
does not change which quartile/leaf is struck.

---

## 8. StateRecord / Wound format

Non-Wound Effects/Conditions: `Type / Tier Y / Magnitude Z / [Location X]` (DEC-115/117).
Wound: `Location X Tier-Y Wound Z (Attribute)` (DEC-035.A). **Wound target selection**
(DEC-102, both combatants automated = creatures): Attribute wound only; candidate
Attribute = the Body attribute(s) used by the Wound skill (bps, bpe); on tie, select
**randomly**. Wound magnitude reduces the chosen attribute directly, live-recalculating
HP max and every dependent Skill Cap (DEC-004).

---

## 9. Flagged assumptions & open corpus issues

**9.1 — Attribute-pair assignment (§2).** Playtest convenience only, not load-bearing on
any number since all attributes start equal.

**9.2 — DEC-106 multi-attack deliberately not exercised.** Your stated "randomly select an
attack skill" (singular) is a scope choice, not a silent override — DEC-106(2)/(6) would
otherwise give automated creature combatants full multi-attack (all legal offense skills,
highest-Skill→lowest, back-to-back, each its own exchange with its own self-Overflow
risk). This playtest tests the single-action DEC-095 base economy plus everything layered
on top of one exchange, not the DEC-106 creature-multi-attack override. Flagged as an
explicit coverage gap, matching the prior brief's own currency-gap note.

**9.3 — Armor Bypass depth vs. DEC-136 R2's "Skill-Tier maps to Location Tier" language.**
DEC-136 R2 states Skill-Tier maps directly to Location Tier with no cap, which could be
read as requiring the combatant's Skill-Tier (2, or higher after an Advanced Skill) to cap
how deep into DEC-137's address the resolution goes. However, DEC-113 R2 fixes Armor
Bypass as a **binary** Tier-1-vs-Tier-2 classification (it is simply "the Tier-2 Effect"),
and DEC-137's adopted table is not itself sub-labeled with per-node Tier numbers. This
brief resolves Armor Bypass to the **full DEC-137 leaf** whenever the DEC-113 Tier-2
classification and the DEC-041 Skill-Tier≥2 gate are both satisfied, without inventing a
truncation scheme. This is the more direct reading of "DEC-137 exists specifically so
Armor Bypass has a real deterministic target," but the depth-scaling question your
corpus's own DEC-136 R2 language raises is **not resolved here** — flagged per Governance
Rule 6 (never silently resolve an open designer fork), not decided by this brief.

**9.4 — Reactions (DEC-132), repeated-Defense Fatigue (DEC-135), Movement/zone mechanics
(DEC-133), and Break-Hold contested escape (DEC-124/131) are out of scope for this
playtest.** Grapple is imposed as a Condition; the contested Break-Hold escape roll and
Fatigued accumulation from repeated Active Defense are not simulated. Flagged, not
silently omitted.

**9.5 — Skill-name-to-Effect binding for Advanced Skills (§4.6) is a playtest convention,**
not a corpus rule — DEC-025 establishes Skill identity carries no mechanical Effect
entitlement, so a "real" table could let a newly Advanced offense skill declare any
unlocked Effect. Inheriting the parent's paired Effect keeps the simulation deterministic
without inventing a new corpus rule.

---

## 10. Logging schema

| Field | Description |
|---|---|
| exchange_# | sequential |
| round | Speed-order round number |
| actor / defender | Alpha / Beta |
| offense_skill, defense_skill | chosen skills + current values |
| atk_roll, def_roll | natural d100 |
| atk_margin, def_margin | Skill − Roll (defender margin 0 if AD failed) |
| outcome | repeat / defender_wins / attacker_wins |
| effect | declared Effect name |
| location_index, zone/leaf, laterality | if location-referencing |
| tag_check | pass / fail_and_fallback / n/a |
| record | resulting StateRecord or Wound string |
| hp_after (both) | post-exchange current HP |
| pe_after (both) | post-recovery PE |
| general_xp_spent | attribute(s) incremented this exchange, if any |
| advanced_skill_created | Y/N + new skill name/attrs |

---

## 11. Test objectives

| # | Mechanic under test | DEC(s) |
|---|---|---|
| 1 | S-1 melee-exchange algorithm | DEC-013, 105 |
| 2 | Contest-delta HP resolution | DEC-096, 097, 104 |
| 3 | Effect Tier/Magnitude = Skill-Tier | DEC-107 |
| 4 | Skill-Tier shred + margin de-escalation | DEC-103 |
| 5 | Zero-Step + Tier-1 quartile resolution | DEC-014, 100 |
| 6 | Tag+Location gating / fail-and-fall-back | DEC-028, 030, 114 |
| 7 | Grappled imposition (escape out of scope, §9.4) | DEC-079 |
| 8 | **Wound target selection (NEW — unreached by the prior playtest)** | DEC-102, 035.A |
| 9 | Incidental Advanced Skill creation, now non-excluded and effect-inheriting | DEC-012 |
| 10 | **Full-depth Armor Bypass resolution via DEC-137** | DEC-112, 113, 136, 137, 114 |
| 11 | **General XP mandatory-lowest-attribute spend, live recalculation** | DEC-004, 011 (house rule §3) |
| 12 | Uncapped/negative HP, forced incapacitation | DEC-052, 108 |

---

## 12. Status

Design brief executed the same session per your instruction. Python simulation
(`random.SystemRandom()`), full per-exchange CSV log, and a results summary follow.
