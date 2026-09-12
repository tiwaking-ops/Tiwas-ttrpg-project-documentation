---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test: Playtest Design Brief"
  version: "0.1 (design brief — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa review before OpenCode handoff or script execution."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-10"
---

# Tiwas — Mirror-Match Combat Stress Test

**Purpose.** Exercise the currently-Ruled combat stack end-to-end (S-1 exchange, Active
Defense, Effect Tier/Magnitude, Location Index + Tag gating, Grapple/Trip/Disarm/Armor
Bypass/Equipment Damage, incidental Advanced Skill creation) using two mechanically
identical combatants. This is a **design brief only** — no rolls have been made, no
Python script exists yet.

---

## 1. Combatant baseline

Both combatants ("Alpha" and "Beta") are identical: all 24 attributes = **50**. Per
DEC-076 Ruling A, automated/computerized combatants use full 24-attribute generation
identical to PCs. Per DEC-102(1), **automated playtest Characters are classified as
creatures** for Wound-target-type purposes (Attribute wounds only, random tie-break —
see §6.4).

### 1.1 Attributes

All 24 attributes (bpp…mex) = 50. (Full matrix omitted — uniform value, no variance.)

### 1.2 Derived statistics

| Stat | Formula | Value |
|---|---:|---:|
| HP | Σ 12 Body attributes | 600 |
| MP | Σ 12 Mind attributes | 600 |
| Physical Energy | bep+bes+bee | 150 |
| Speed | bsp+bss+bse | 150 |
| Energy Regen | bep+bes | 100 |
| MP Regen | mep+mes | 100 |
| Movement Speed | floor((bsp+bss)/15) | 6 |

Both combatants: identical values. Tied Speed → initiative resolved by reroll (DEC-095
step 7); re-checked only if an Attribute Wound later changes Speed (DEC-095 step 6).

---

## 2. Skill loadout

All combat skills are **Tier-2** (2 attributes), per your confirmation. Because every
attribute = 50, Cap and Starting Value are identical for every Tier-2 skill regardless
of which attributes are chosen:

`Cap = floor((50+50)/2) = 50` → `Starting Value = floor(50/2) = 25`

Attribute pairs below are a **design choice** (flagged — see §8.1), chosen only to keep
Wound-target attribution (DEC-102 §4) sensible; they don't change any number.

| Skill | Attributes | Tier | Cap | Start | Resource | Paired S-3 Effect (this playtest's convention — §8.2) |
|---|---|---:|---:|---:|---|---|
| Attack | bpp + bps | 2 | 50 | 25 | PE | Inflict Injury (Base tier) |
| Defense | bss + bse | 2 | 50 | 25 | PE | (defensive roll only — no Effect) |
| Grapple | bpp + bsp | 2 | 50 | 25 | PE | Impose Condition: Grappled |
| Trip | bsp + bss | 2 | 50 | 25 | PE | Knock Prone (DEC-113 Tier 1) |
| Disarm | bss + bsx | 2 | 50 | 25 | PE | Disarm/Break Hold (DEC-028, DEC-113 Tier 1) |
| Armor Bypass | bps + bpe | 2 | 50 | 25 | PE | Armor Bypass (DEC-113 Tier 2 — only Tier-2 Effect) |
| Equipment Damage | bpp + bpe | 2 | 50 | 25 | PE | Equipment Damage (DEC-113 Tier 1) |

All Body-domain → Physical Energy resource pool throughout (DEC-012.3).

---

## 3. Equipment & Tag loadout

Disarm, Armor Bypass, and Equipment Damage are gated by target Tag presence at the
struck location (DEC-114 R2). Without matching Tags on both combatants, those three
Effects would always fail-and-fall-back (DEC-030) — so both combatants carry:

| Item | Tags | Notes |
|---|---|---|
| Weapon | `slot:main_hand`, `state:held`, `offense:melee`, `damage:slashing`, `handling:light` | satisfies Disarm's `state:held` + `slot:main_hand` trigger |
| Body armor | `slot:body`, `state:worn`, `defense:armor` | satisfies Armor Bypass's `defense:armor` trigger; also satisfies Equipment Damage's broad `state:worn` trigger |

No `env:*`, no Bypass-relational counter-Tag pairing (DEC-059) is declared on either
side — Armor Bypass is not blocked by any defined counter for this scenario.

---

## 4. Combat procedure

### 4.1 Turn structure
- Speed-based turn order, tie-break reroll (DEC-095).
- One substantive combat action per turn = one S-1 melee exchange (DEC-095/105).
- Movement is free/bundled, doesn't consume the action (both combatants have identical
  Movement Speed 6, so movement/positioning is not a meaningful variable here — flagged,
  §8.3).

### 4.2 Exchange algorithm (per DEC-105)
1. **Offense skill selection.** The acting combatant selects, among {Attack, Grapple,
   Trip, Disarm, Armor Bypass, Equipment Damage}, the skill with the **currently
   highest numeric value** (your explicit rule). Ties broken arbitrarily (flag if this
   matters — with a mirror match and shared starting values it will occur often; see
   §8.4 for a suggested tie-break).
2. **Defense skill.** The defending combatant always uses Defense (their only defensive
   skill). Defense is **mandatory** for this playtest, per DEC-105's own "playtests =
   defense MANDATORY" convention (not a guess — this is the Ruled playtest default).
3. **Roll.** Both combatants make one ordinary Core Test (DEC-006) simultaneously: the
   acting combatant on their chosen offense skill, the defender on Defense. This single
   pair of rolls **is** the S-1 opposed contest (DEC-013) **and** supplies both Margins
   used below — there is no separate third "Active Defense" roll (DEC-104 composes
   DEC-096+DEC-097 from this one contest's two Margins).
4. **Resolve outcome** per DEC-013 matrix / DEC-105 table:
   - Both fail → repeat (§13.4).
   - Exact Quality tie on double-success → repeat (§13.5).
   - Defender wins → attack fails, no counter-Effect (DEC-101).
   - Attacker wins → apply the paired Effect (§8.2 table) per branch below.
5. **HP branch (Inflict Injury only):** damage = Winner's Margin − Defender's Margin,
   never < 0 on a win (DEC-104).
6. **Effect branch (Grapple/Trip/Disarm/Armor Bypass/Equipment Damage):**
   - Effect Tier = acting Skill-Tier = **2**; Magnitude = 2 by default (`Z=−2`),
     "equal" per DEC-107 (no player/GM present to choose a lesser tier — automated run).
   - Apply DEC-103 Skill-Tier-shred + margin de-escalation (Atk Tier = Def Tier → Mag
     −1 first, then −= Defender's Margin; floor-0 → Tier−1 cascade; Tier-0 = negated).
   - If the Effect is location-referencing (Trip, Disarm, Armor Bypass, Equipment
     Damage, Wound) — all are, since Skill-Tier 2 ≥ DEC-041's gate — generate a Location
     Index via Zero-Step off the attacker's natural roll (DEC-014), then resolve per
     §5 below.
   - Tag-check the target at the resolved location (DEC-114 R2). Match → Effect applies
     as a StateRecord (DEC-115/117 schema: `Type / Tier Y / Magnitude Z / Location X`).
     Mismatch → fail-and-fall-back to Base Inflict Injury (DEC-030).
7. **Recovery** (DEC-008) applies to both combatants' spent pools, always last.
8. **Failure XP / Skill Roll Pool** (DEC-009/010) resolved for both, regardless of
   exchange outcome.
9. **Failed-Double check** (DEC-012): a qualifying failed Double on either roll creates
   an Advanced Skill — random unused attribute added, Tier = old Tier+1, **Starting
   Value = 1** (per your instruction — not the 1d100-vs-cap alternative). This skill is
   **excluded** from the offense-skill-selection pool in step 1 for the remainder of the
   test (per your "will not influence the battle" constraint).

### 4.3 Termination
Combat ends when either combatant's HP reaches 0 (forced incapacitation, DEC-052; HP is
uncapped and may go negative per DEC-108, so exchanges do not stop immediately at 0 if
you want post-incapacitation logging — but decide the log's actual stop point). **No
round cap is set here** — left to you/the eventual script. A default of "first HP ≤ 0"
is the minimal Ruled stopping condition; anything else (e.g., a fixed 50-exchange cap
for log-length control) is your call.

---

## 5. Location Index resolution (per Effect)

| Effect | DEC-113 tier assignment | Resolution |
|---|---|---|
| Trip, Disarm, Equipment Damage, Inflict-Injury-with-location | Tier 1 (coarse) | DEC-100 quartiles off the Zero-Step index: 1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head. Parity (odd/even) sets left/right (DEC-041(3)). |
| Armor Bypass | Tier 2 (the only Tier-2 Effect) | **See §8.5 — this is a live corpus contradiction you should resolve before running the test.** |

---

## 6. Wound / StateRecord format

Wound Effects (Impose Condition: Wounded, if declared): `Location X Tier-Y Wound Z
(Attribute or Skill)` (DEC-035.A). All other Effects/Conditions: `Type / Tier Y /
Magnitude Z / [Location X]` (DEC-115/117).

**Wound target selection** (DEC-102, applies since both combatants are automated =
creatures): Attribute wounds only, no player choice. Multiple-candidate attribute ties
resolve **randomly**.

---

## 7. Logging schema (per exchange, for eventual scripting)

| Field | Description |
|---|---|
| exchange_# | sequential |
| actor / defender | Alpha / Beta |
| offense_skill_chosen | value at time of roll + which skill |
| atk_roll, def_roll | natural d100 results |
| atk_margin, def_margin | Skill − Roll for each |
| outcome | repeat / defender-wins / attacker-wins |
| effect_declared | Inflict Injury / Grappled / Prone / Disarm / Armor Bypass / Equipment Damage |
| location_index, zone, laterality | if location-referencing |
| tag_check | pass / fail-and-fall-back |
| resulting_staterecord | Type/Tier/Magnitude/Location |
| hp_after (both) | post-exchange |
| pe_after (both) | post-recovery |
| failure_xp, skill_pool_change | both combatants |
| advanced_skill_created | Y/N, attribute added, excluded-from-selection flag |

---

## 8. Flagged assumptions & open corpus issues

**8.1 — Attribute-pair assignment (§2).** Chosen for Wound-target coherence only; every
number is identical regardless of choice since all attributes = 50. Change freely.

**8.2 — Skill↔Effect pairing (§2, §4.2 step 6).** DEC-025 rules that a skill's *name*
carries no mechanical weight and doesn't gate which Effect can be declared — in
principle any winning skill could declare any unlocked Effect. This brief adopts a
1:1 skill→Effect convention purely as a playtest simplification so "highest-value skill
selection" has a deterministic meaning. This is **not** a Tiwas rule, just this
scenario's convention — flag if you want free Effect choice instead.

**8.3 — Movement Speed identical (6/6).** With no positional variance seeded, the G5
movement-band mechanics (DEC-133) have nothing to differentiate — this scenario as
designed won't meaningfully stress-test movement/zones. If that's a goal, one combatant
needs an asymmetric Movement Speed or starting Zone.

**8.4 — Offense-skill tie-break (§4.2 step 1).** Your rule ("highest numeric value")
doesn't specify what happens on an exact tie among candidate skills (common here, since
all six skills start at 25 and grow via the same Failure-XP mechanism symmetrically).
No corpus rule covers this. Suggested default: alternate by a fixed priority order
(Attack > Grapple > Trip > Disarm > Armor Bypass > Equipment Damage) — but this is
invented for this brief, not derived from any DEC. Your call.

**8.5 — Armor Bypass location resolution: live corpus contradiction.** DEC-113 R2
(2026-09-06) says Armor Bypass resolves at Tier 2 "via the DEC-042 secondary roll."
DEC-112 (re-ruled 2026-09-08) explicitly **supersedes** "DEC-042 secondary-roll
mechanism for Tier 2+ location resolution" in favor of a single-source deterministic
hierarchical address model (L-003, L-011) — and that newer ruling has not been
back-propagated into DEC-113's text. Separately, **no Human Location Template exists**
yet (DEC-112 L-009 explicitly defers template content to future content-authoring), so
even the newer model can't be executed as-is for a human-shaped combatant.

Also relevant: DEC-113 R3 allows a **PC** to downgrade a Tier-2-eligible Effect to
Tier-1 coarse; R4 makes tier **mandatory** for creatures/NPCs. Since DEC-102(1)
classifies automated playtest characters as creatures, R4 (mandatory Tier-2, no
downgrade) would apply here — colliding directly with the missing-template problem.

**I have not resolved this** — per standing practice, this is exactly the kind of
designer fork that shouldn't be silently picked. Two ways forward, your call:
  - (a) Treat Alpha/Beta as PC-equivalent for this one purpose and downgrade Armor
    Bypass to Tier-1 coarse for this playtest only (scaffold, non-canonical, logged as
    such), or
  - (b) Author a minimal placeholder sub-zone template (e.g., Head/Torso/Arms/Legs ×
    Upper/Lower, per DEC-112 L-006's stated Tier-2 semantics) explicitly flagged as
    non-canonical scaffolding, pending the real Human Location Template.

Nothing below §8.5 assumes either resolution — the rest of the brief is unaffected
except Armor Bypass's location step.

---

## 9. Test objectives (what this scenario is meant to validate)

| # | Mechanic under test | DEC(s) |
|---|---|---|
| 1 | S-1 melee-exchange algorithm, mandatory-defense convention | DEC-013, 105 |
| 2 | Contest-delta HP resolution | DEC-096, 097, 104 |
| 3 | Effect Tier/Magnitude = Skill-Tier (no Quality gating) | DEC-107 |
| 4 | Skill-Tier shred + margin de-escalation on non-HP Effects | DEC-103 |
| 5 | Zero-Step + Tier-1 quartile location resolution | DEC-014, 100 |
| 6 | Tag+Location gating / fail-and-fall-back | DEC-028, 030, 114 |
| 7 | Grappled imposition + contested Break-Hold escape | DEC-079, 124, 131 |
| 8 | Wound target selection (automated/creature path) | DEC-102 |
| 9 | Incidental Advanced Skill creation, non-influencing | DEC-012 |
| 10 | Armor Bypass Tier-2 path | DEC-112/113 — **blocked pending §8.5** |

---

## 10. Status / next steps

This is a design brief, not a ruling and not an execution. Recommended path: you resolve
§8.5 (and optionally §8.1/8.3/8.4), then this converts either into a manually-narrated
worked exchange or a `random.SystemRandom()` Python script with a YAML-headered results
document, per standing playtest methodology — at your direction.
