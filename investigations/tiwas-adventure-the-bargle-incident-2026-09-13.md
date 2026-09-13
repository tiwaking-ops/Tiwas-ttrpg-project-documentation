---
document:
  title: "Tiwas — Adventure Module: The Bargle Incident (System-Completeness Playtest)"
  version: "0.1"
  status: "Advisory / Non-canonical. No DEC assigned. GM table-use playtest scenario, not a ruling."
  purpose: >
    Built to exercise as much of the currently-Ruled Tiwas mechanical stack as reasonably
    fits in a few scenes, using full 24-attribute NPC builds and at least two pre-authored
    Tier-2 signature skills (per DEC-086/087) so Location-referencing Effects and the
    DEC-136/137 Armor Bypass resolution path can actually fire.
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
---

# Tiwas — The Bargle Incident

Loosely adapted from the 1983 Basic Set solo introductory adventure (the Aleena/Bargle
encounter). In this version, **Aleena survives** — she takes real, mechanically-resolved
harm but does not die, and fights alongside the player character in the final scene. All
numbers below are worked examples for teaching/testing purposes, not scripted outcomes —
any GM running this at the table should let actual rolls diverge from the samples shown.

---

## Cast — Full 24-Attribute Stat Blocks

All four characters use full attribute-matrix builds (24 attributes, 12 Body / 12 Mind).
Derived statistics use the locked Canonical formulas (§4) throughout.

### Rowan (Player Character — fresh Tier-1 start)

| Body | Val | Mind | Val |
|---|---:|---|---:|
| bpp (Might) | 58 | mpp (Cunning) | 42 |
| bps (Impact) | 52 | mps (Wits) | 45 |
| bpe (Brawn) | 47 | mpe (Willpower) | 50 |
| bpx (Presence) | 40 | mpx (Glamour) | 33 |
| bsp (Agility) | 61 | msp (Acuity) | 48 |
| bss (Reflexes) | 55 | mss (Perception) | 55 |
| bse (Quickness) | 50 | mse (Alacrity) | 40 |
| bsx (Grace) | 38 | msx (Charm) | 46 |
| bep (Toughness) | 60 | mep (Focus) | 51 |
| bes (Stamina) | 53 | mes (Discipline) | 43 |
| bee (Vitality) | 57 | mee (Resolve) | 49 |
| bex (Poise) | 44 | mex (Composure) | 47 |

| Derived | Formula | Value |
|---|---|---:|
| HP | Σ Body | 615 |
| MP | Σ Mind | 549 |
| Physical Energy | bep+bes+bee | 170 |
| Speed | bsp+bss+bse | 166 |
| Energy Regen | bep+bes | 113 |
| MP Regen | mep+mes | 94 |
| Movement Speed | floor((bsp+bss)/15) | 7 |

| Skill | Tier | Attributes | Cap | Start |
|---|---:|---|---:|---:|
| Attack | 1 | bpp | 58 | 29 |
| Defense | 1 | bss | 55 | 27 |
| Perception | 1 | mss | 55 | 27 |
| Stealth | 1 | bsp | 61 | 30 |

**Gear:** Shortsword (`slot:main_hand`, `state:held`, `offense:melee`, `damage:slashing`,
`handling:light`); Leather Armor (`slot:body`, `state:worn`, `defense:armor`).

---

### Aleena (Ally NPC)

| Body | Val | Mind | Val |
|---|---:|---|---:|
| bpp | 45 | mpp | 50 |
| bps | 40 | mps | 48 |
| bpe | 50 | mpe | 62 |
| bpx | 48 | mpx | 44 |
| bsp | 42 | msp | 46 |
| bss | 47 | mss | 50 |
| bse | 44 | mse | 43 |
| bsx | 41 | msx | 49 |
| bep | 55 | mep | 60 |
| bes | 46 | mes | 55 |
| bee | 58 | mee | 65 |
| bex | 50 | mex | 52 |

| Derived | Value |
|---|---:|
| HP | 566 |
| MP | 624 |
| Physical Energy | 159 |
| Speed | 133 |
| Energy Regen | 101 |
| MP Regen | 115 |
| Movement Speed | 5 |

| Skill | Tier | Attributes | Cap | Start |
|---|---:|---|---:|---:|
| Devotion | 1 | mee | 65 | 32 |
| Smite (Attack) | 1 | bep | 55 | 27 |
| Defense | 1 | bss | 47 | 23 |

**Gear:** Mace (`slot:main_hand`, `state:held`, `offense:melee`, `damage:bludgeoning`,
`handling:light`); Holy Vestments (`slot:body`, `state:worn` — **no** `defense:armor` Tag;
cloth only, deliberately so this stat block can demonstrate an Armor Bypass no-match case
later).

---

### Goblin (Creature)

| Body | Val | Mind | Val |
|---|---:|---|---:|
| bpp | 40 | mpp | 22 |
| bps | 38 | mps | 28 |
| bpe | 30 | mpe | 20 |
| bpx | 25 | mpx | 15 |
| bsp | 45 | msp | 25 |
| bss | 48 | mss | 35 |
| bse | 35 | mse | 24 |
| bsx | 30 | msx | 18 |
| bep | 32 | mep | 20 |
| bes | 36 | mes | 22 |
| bee | 34 | mee | 25 |
| bex | 28 | mex | 19 |

| Derived | Value |
|---|---:|
| HP | 421 |
| MP | 273 |
| Physical Energy | 102 |
| Speed | 128 |
| Energy Regen | 68 |
| MP Regen | 42 |
| Movement Speed | 6 |

| Skill | Tier | Attributes | Cap | Start | Note |
|---|---:|---|---:|---:|---|
| Crude Attack (signature) | 1 | bpp | 40 | **40** | Full-Cap veteran start, DEC-086 |
| Defense (non-signature) | 1 | bss | 48 | 24 | floor(Cap/2), standard |
| Trip (signature) | 2 | bsp+bss | 46 | **46** | Pre-authored Tier-2, DEC-086/087 |

**Gear:** Rusty Dagger (`slot:main_hand`, `state:held`, `offense:melee`, `damage:piercing`,
`handling:light`). No worn armor.

---

### Bargle (Villain)

| Body | Val | Mind | Val |
|---|---:|---|---:|
| bpp | 35 | mpp | 68 |
| bps | 32 | mps | 65 |
| bpe | 30 | mpe | 60 |
| bpx | 44 | mpx | 55 |
| bsp | 40 | msp | 58 |
| bss | 46 | mss | 52 |
| bse | 38 | mse | 50 |
| bsx | 42 | msx | 48 |
| bep | 33 | mep | 62 |
| bes | 35 | mes | 57 |
| bee | 37 | mee | 55 |
| bex | 40 | mex | 50 |

| Derived | Value |
|---|---:|
| HP | 452 |
| MP | 680 |
| Physical Energy | 105 |
| Speed | 124 |
| Energy Regen | 68 |
| MP Regen | 119 |
| Movement Speed | 5 |

| Skill | Tier | Attributes | Cap | Start | Note |
|---|---:|---|---:|---:|---|
| Bolt (signature) | 2 | mpp+mps | 66 | **66** | Pre-authored Tier-2, DEC-086/087 |
| Defense (non-signature) | 1 | bss | 46 | 23 | floor(Cap/2) |
| Beguile | 1 | mpx | 55 | 27 | Roleplay/social, unused mechanically below |

**Gear:** Gnarled Wand (`slot:main_hand`, `state:held`, `offense:ranged`, `damage:electric`);
Traveling Robes (`slot:body`, `state:worn` — **no** `defense:armor` Tag).

> **GM Note — one Skill, several declared Effects.** Per DEC-025 (pure declared intent),
> neither Bolt's name nor its formula gates which Effect Bargle may declare on a win — Wound,
> plain Inflict Injury, or (against an armored target) Armor Bypass are all available from
> the same roll. What actually resolves is a function of what the *player/GM declares*, the
> Skill-Tier gate (DEC-041), and Tag/Location matching (DEC-114) — never the Skill's label.

---

## Scene 1 — The Road to Alderbrook

Rowan meets Aleena on the road; she's travelling the same way and offers to join him after
some conversation. Before they reach the treeline, have Rowan roll **Perception** to notice
a goblin scout's tracks.

**Worked example:** Rowan rolls **45** against Perception (Skill 27) → **fails** (45 > 27).

| Step | Value |
|---|---:|
| Cost (= Roll) | 45 PE |
| PE after cost | 170 − 45 = 125 |
| Failure XP = max(0, 45−27) | 18 |
| Skill Roll Pool cascade | Pool(18) < Skill(27) → no increase; 18 → General XP |
| Recovery = floor(113/2) | 56 |
| PE after recovery | 125 + 56 = 181, **clamped to max 170** |

> **GM Tutorial Note — an ambush isn't a separate mechanic.** Even though Rowan failed to
> notice the scout, the goblin does **not** get an automatic free hit. Tiwas has no surprise
> round; the coming fight still resolves entirely through Speed-based turn order (DEC-095).
> The failed check only justifies *why* the goblin gets to choose the engagement terrain,
> narratively — not any mechanical advantage.

---

## Scene 2 — Ambush! The Goblin's Trap

**Turn order (DEC-095, Speed-based):** Rowan (166) → Aleena (133) → Goblin (128).

| Exch. | Actor→Target | Skill (Tier) | Atk Roll | Def Roll | Outcome | Effect | Location / Tag | Result |
|---|---|---|---:|---:|---|---|---|---|
| 1 | Rowan→Goblin | Attack (T1) vs Defense | 22 (Margin 7) | 31 (fail) | Rowan wins | Inflict Injury | — | Injury = 7−0 = 7. Goblin HP 421→414 |
| 2 | Goblin→Rowan | Trip (T2) vs Defense | 30 (Margin 16) | 35 (fail) | Goblin wins | Knock Prone | LI=3 (Legs, Left) | See breakdown below |
| 3 | Rowan (stand, free) →Goblin | Attack (T1) vs Defense | 15 (Margin 14) | 40 (fail) | Rowan wins | Inflict Injury | — | Injury = 14−0 = 14. Goblin HP 414→400 |

**Exchange 2 breakdown — Location Index & Skill-Tier shred:**

- Zero-Step on Goblin's roll 30: tens=3, units=0 → swap → **3**. DEC-100 quartile 1–25 =
  **Legs**. Parity = units digit of the output (3) → odd → **Left**.
- DEC-041 gate check: Trip is Tier-2, satisfies the Skill-Tier ≥ 2 production requirement —
  a Location Index is generated.
- Base Effect: `Tier Y = Magnitude Y = Goblin's Skill-Tier (2)`.
- DEC-103 shred: Attacker Tier (2) > Defender Tier (Rowan's Defense is Tier-1) → **Mag +1**
  → Magnitude 3.
- De-escalation: Rowan's Defense failed → mitigation 0. No further reduction.
- **Final record:** `Location: Left Leg, Tier-3 Prone, Magnitude -3` (DEC-115/117 schema).

Rowan is now Prone: −3 to attack rolls (his effective Attack becomes 26) until he spends
movement to stand or the Effect is removed (DEC-079). Since movement is free/bundled and
doesn't consume the substantive action (DEC-082), Rowan **stands and still attacks** on
Exchange 3.

> **GM Tutorial Note — Skill-Tier shred rewards training gaps, not raw Skill value.** The
> Goblin's Trip Skill (46) isn't even close to Rowan's Defense (27) in raw numbers, but the
> shred step only cares about **Skill *Tier***, not Skill value — a Tier-2 skill beats a
> Tier-1 defense by the shred rule regardless of who has the bigger number.

**Later, unlogged exchanges (GM-narrated):** run several more rounds using the identical
procedure. Two specific events worth calling out if/when they occur:

> **Worked 100-Fumble example.** Suppose the Goblin's Crude Attack roll comes up exactly
> **100**. Despite a Skill of only 40, the roll **still auto-fails** (100-Fumble is
> unconditional) and **still qualifies as a failed Double**. Per DEC-012/DEC-087, Advanced
> Skill creation from a failed Double is a **player-character** advancement rule — it does
> **not** apply to creature templates, so the Goblin gains nothing from this roll beyond the
> guaranteed failure. Flag this PC/creature asymmetry explicitly for a new player.

> **Worked Overflow example.** Suppose, several rounds in, the Goblin's Physical Energy has
> dropped to 40 and it rolls a costly **95** on a Trip attempt. Cost = 95, but only 40 PE
> remains: `Overflow = 95 − 40 = 55`. The Goblin's own pool falls to 0 and it takes **55
> direct HP damage** from its own overexertion — Overflow always applies to the *roller*,
> win or lose.

**Rowan's Advanced Skill (worked example, PC-side):** on a later exchange, Rowan rolls **88**
on Attack (Skill 29) — a failure (88 > 29) that is also a qualifying Double.

| Step | Value |
|---|---:|
| Failure XP = max(0, 88−29) | 59 |
| Skill Roll Pool cascade | 59≥29 → Skill 30, Pool 30 → 30≥30 → Skill 31, Pool 0 → stop |
| New Attack Skill | 31 |
| Advanced Skill created | Tier 2, adds bps (52) to bpp (58); Cap = floor(110/2) = 55 |
| Starting Value chosen | Player rolls 1d100 → 63 → `min(63, 55)` = **55** |
| New Skill | **Power Strike** (bpp+bps, Tier 2, Cap 55, Start 55), PE-domain (lineage) |

Rowan now has a homegrown Tier-2 skill for Scene 3.

**Ending the fight:** no morale/flee threshold exists anywhere in the ruled corpus — that is
a genuine open item, not something to silently invent. Either narrate enough further
exchanges to bring the Goblin to HP ≤ 0 (DEC-052 forced incapacitation, no roll), or have it
break and flee at GM discretion.

---

## Interlude — Aleena's Aid (S-11 Healing)

Rowan is battered from the fight. Aleena offers to mend him with Devotion. This is an
**Extended Test** (DEC-073: S-11 healing *is* a literal Extended Test instance), each
interval an ordinary Core Test, progress by Margin-accumulation (DEC-067), failures neutral
(DEC-068), completion target set by GM discretion (DEC-070/074) — say the GM sets the target
at **40 accumulated Margin**.

| Interval | Roll | Skill 32 | Outcome | Margin | Running Total | Cost (MP) |
|---|---:|---:|---|---:|---:|---:|
| 1 | 12 | 32 | success | 20 | 20 | 12 |
| 2 | 25 | 32 | success | 7 | 27 | 25 |
| 3 | 41 | 32 | **fail** | — (neutral, DEC-068) | 27 (unchanged) | 41 |
| 4 | 8 | 32 | success | 24 | **51 ≥ 40 → complete** | 8 |

Total Cost across intervals: 12+25+41+8 = 86 MP (Recovery applies after each interval;
detail omitted for brevity — apply `floor(115/2)=57` per interval, clamped at 624).
On completion, the GM restores an amount of Rowan's HP proportionate to the finished
threshold — Tiwas locks no fixed Margin-to-HP healing conversion (DEC-074 explicitly
rejects a fixed "HP-deficit lock"), so this is a GM-discretion call, not an invented formula.

> **GM Tutorial Note — Wound magnitude would have penalized this roll, if present.** DEC-072
> says a Wound's magnitude penalizes the *healer's* effective Skill for a healing test. Rowan
> only picked up a Condition (Prone) in Scene 2, not a Wound, so no penalty applied here —
> contrast this with Scene 3, where an actual Wound record changes this math.

---

## Scene 3 — Bargle's Ambuscade

**Turn order:** Rowan (166) → Aleena (133) → Bargle (124).

### Round 1, Exchange 1 — Rowan's Power Strike (Wound on Bargle)

Rowan attacks with the new Power Strike (Tier-2, Skill 55) vs Bargle's Defense (23).
Roll 18 (Margin 37) vs Bargle's Defense roll 60 (fail).

- Zero-Step on 18: tens=1, units=8 → swap → **81**. Quartile 76–100 = **Head**. Parity:
  units digit of 81 = 1, odd → **Left**.
- Rowan (a Player) declares **Impose Condition: Wounded** rather than plain Injury (DEC-025:
  declared intent, not Skill-gated).
- Base Effect Tier = Magnitude = 2 (Power Strike's Skill-Tier). Shred: Atk Tier(2) >
  Bargle's Defense Tier(1) → Mag +1 → 3. De-escalation: Bargle's Defense failed → 0.
- **Wound record:** `Location: Head (Left), Tier-3 Wound, Magnitude -3`.
- DEC-102 target selection: Rowan is a **Player**, so he **chooses** the wounded attribute
  from Power Strike's own candidate attributes {bpp, bps}. He picks **bps** (Bargle's
  Impact): `32 − 3 = 29`, live-recalculated (DEC-004) — no currently-relevant Skill draws on
  Bargle's bps this session, so the mechanical consequence is cosmetic for now (a fair,
  non-inflated outcome — not every Wound is crippling).

### Round 1, Exchange 2 — Aleena's Smite

Aleena (Smite, Skill 27) vs Bargle Defense (23). Roll 11 (Margin 16) vs Bargle roll 71
(fail). Injury = 16 − 0 = 16. **Bargle HP: 452 → 436.**

### Round 1, Exchange 3 — Bargle's Bolt (Wound on Aleena)

Bargle (Bolt, Skill 66) targets Aleena. Roll 9 (Margin 57) vs Aleena's Defense (23),
Aleena rolls **88** — a **failure that is also a qualifying Double**.

Full sequencing, in order:

1. **Cost paid** on Aleena's Defense roll: 88 MP. Pool: 624 − 88 = 536.
2. **Overflow check:** 536 ≥ 0, no shortfall — no Overflow this step.
3. **Failure XP** = max(0, 88−23) = 65.
4. **Failed Double → Advanced Skill.** GM Fiat (DEC-130, bounded universality — this doesn't
   override any locked invariant) rules that Aleena, a named ally, advances like a
   player-adjacent character here. New skill **Iron Faith** (bss+bee), Tier 2,
   Cap = floor((47+58)/2) = 52. GM chooses the **safe default**: Starting Value = **1** (the
   other official option, contrasting with Rowan's rolled 55 above). This does **not**
   retroactively change the Defense roll that already failed.
5. **Bargle's declared Effect** (winning side, Tag/Location check first): Bargle could
   attempt Armor Bypass (Bolt is Tier-2) — but Aleena's Vestments carry **no** `defense:armor`
   Tag anywhere. Per DEC-114 R2, Armor Bypass has no valid match → automatic
   **fail-and-fall-back (DEC-030)** if declared. Bargle instead declares **Impose Condition:
   Wounded** (Tier-1 coarse per DEC-113 R2).
6. **Location Index:** Zero-Step on Bargle's roll 9: tens=0, units=9 → swap → **90**.
   Quartile 76–100 = **Head**. Parity: units digit of 90 = 0, even → **Right**.
7. **Effect Tier/Magnitude:** base 2 (Bolt's Skill-Tier). Shred: Atk(2) > Aleena's Defense
   Tier(1) → Mag +1 → 3. De-escalation: Aleena's Defense failed → 0.
8. **DEC-102 target selection:** Bargle is a creature → **Attribute wound only**. Bolt's
   formula (mpp+mps) is Mind-only → Mind attribute wound (DEC-102(3)). Two candidates
   {mpp, mps}; creature picks **randomly** → **mps** (Wits). `48 − 3 = 45`.
9. **Live recalculation (DEC-004):** Aleena's MP (sum of Mind attributes) drops by exactly
   the attribute change: 624 → **621**.
10. **Recovery** (last, always): floor(115/2) = 57. Pool: 536 + 57 = 593, clamped at the
    *new* max 621 → no clamping needed, final MP = **593**.

**Final Wound record:** `Location: Head (Right), Tier-3 Wound, Magnitude -3 (mps)`.

> **GM Tutorial Note — a Wound is not automatically HP loss.** This entire exchange produced
> zero direct HP damage to Aleena — only a resource cost, a Failure-XP cascade, a new
> Advanced Skill, and a lasting Wound record. She is meaningfully hurt (and now weaker in
> Wits specifically) but **not** bleeding out. This is exactly the distinction the Two-Track
> Harm Model exists to make: Injury (Track A, HP) and Wounds (Track B, lasting attribute
> penalties) are independent consequences that can arise from the very same winning roll.

### Round 2 — Aleena takes real Injury

Aleena attacks again (Smite 27) vs Bargle Defense (23): roll 11 (Margin 16) vs Bargle roll
58 (fail). Injury = 16. **Bargle HP: 436 → 420.**

Bargle's turn: he declares plain **Inflict Injury** this time. Bolt roll 14 (Margin 52) vs
Aleena's Defense — she uses her original Defense (23; her new Iron Faith sits at Starting
Value 1, clearly the worse choice this early) and rolls 45 (fail). Injury = 52 − 0 = **52**.
**Aleena HP: 566 → 514.**

> **GM Tutorial Note — full-attribute NPCs have large HP pools relative to Margin damage.**
> At this build scale (HP in the 400–600 range against typical Margin hits in the 10s–50s),
> expect a genuine fight to run many rounds — the same scale relationship observed in the
> corpus's own Mirror-Match stress test (100 exchanges, neither combatant reduced below half
> HP). For pacing at the table, narrate **4–6 more Bargle-vs-Aleena exchanges** off-page using
> the identical roll → Margin → contest-delta procedure until her HP is wherever you want it
> for the scene's tension — Tiwas defines no "bloodied"/"critical" threshold below HP = 0;
> only HP = 0 itself triggers forced incapacitation (DEC-052), with no intermediate tier.
> **Do not invent one** — this is an honest gap in the ruled corpus, not a place to improvise
> a new rule.

### Closing Exchange — Rowan finishes it

After further rounds (GM-narrated, same procedure), Rowan's Power Strike lands a decisive
hit that brings Bargle's HP to 0 or below. **HP = 0 triggers forced incapacitation with no
roll** (DEC-052); HP may continue negative and persists (DEC-108). Bargle is down, not
necessarily dead — permanent death requires either exhausted revival attempts or a
voluntary choice while incapacitated (DEC-054). Whether Rowan turns him over to the
authorities or something else happens is entirely up to the table.

Aleena survives the encounter at reduced HP, carrying a Tier-3 Head Wound and a fledgling
Advanced Skill she can grow into later.

---

## Aftermath

Both Rowan and Aleena can pursue further S-11 healing afterward (same Extended-Test
procedure as the Interlude) to recover HP and, separately, to step down the Wound record's
Tier via the Effect Heal System (a qualifying Skill Test at Tier ≥ the Wound's current Tier
reduces it one step; DEC-035.A cl.5 / DEC-121). Healing HP and healing a Wound are two
different actions against two different records — another distinction worth calling out
explicitly to a new table.

---

## GM Coverage Checklist — What This Module Exercised

| Mechanic | DEC(s) | Where |
|---|---|---|
| Core Test Transaction, Cost=Roll, Overflow→HP | DEC-006/007 | Scene 1, Goblin fight |
| 100-Fumble | DEC-001 | Goblin fight (worked example) |
| Failure XP, Skill Roll Pool cascade | DEC-009/010 | Scene 1, Rowan's Double |
| Advanced Skill creation (both Start-Value options) | DEC-012 | Rowan (rolled), Aleena (flat 1) |
| Recovery + clamping | DEC-008 | Scene 1, Interlude |
| S-1 opposed contest / melee exchange | DEC-013, DEC-105 | All combat exchanges |
| Contest-delta Inflict Injury | DEC-096/097/104 | Multiple exchanges |
| Skill-Tier shred + margin de-escalation | DEC-103 | Trip, both Wounds |
| Zero-Step Location Index | DEC-014 | Trip, both Wounds |
| Tier-1 quartiles + parity laterality | DEC-100, DEC-041(3) | Trip, both Wounds |
| Skill-Tier ≥ 2 production gate | DEC-041(1) | Trip, Power Strike, Bolt |
| DEC-107 Effect Tier = Skill-Tier | DEC-107 | Trip, both Wounds |
| Wound record format + target selection | DEC-035.A, DEC-102 | Both Wounds |
| Live attribute recalculation | DEC-004 | Aleena's mps Wound |
| Conditions (Prone) | DEC-079, DEC-122/125 | Goblin's Trip |
| Tag+Location gating / fallback | DEC-028, DEC-114, DEC-030 | Armor Bypass no-match (Aleena) |
| GM Fiat (bounded universality) | DEC-130 | Aleena's Advanced Skill |
| S-11 Rest/Healing as Extended Test | DEC-071–074 | Interlude |
| Forced incapacitation at HP=0, negative HP | DEC-052, DEC-108 | Aftermath |
| Speed-based turn order | DEC-095 | Scene 2, Scene 3 |
| Creature signature-skill full-Cap start | DEC-086/087 | Goblin, Bargle |

**Not exercised (flagged, not invented):** Active Defense as a separate genuine Core Test
(DEC-044, distinct from the direct S-1 melee model used here per DEC-105); Reactions
(DEC-132); Equipment damage/repair (DEC-118–129); Encumbrance (DEC-078); full Armor Bypass
resolution against a Tag-matched target (the module deliberately shows the *no-match*
fallback path only — a follow-up scene against an armored foe would be needed to exercise
DEC-136/137's deterministic address resolution end-to-end).
