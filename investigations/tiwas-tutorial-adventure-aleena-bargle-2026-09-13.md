---
document:
  title: "Tiwas — Tutorial Adventure: The Bandit's Trap (Aleena & Bargle)"
  version: "0.1"
  status: "Advisory / Non-canonical. No DEC assigned. GM table-use tutorial content only — not a ruling, not a rules change."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
---

# Tiwas — Tutorial Adventure: The Bandit's Trap

**Purpose.** A 1-on-1 teaching scenario that walks a new player through Tiwas's core loop —
d100 roll-under, Cost = Roll, Overflow → HP, Recovery, and the S-1 opposed-contest exchange —
using the classic "goblin ambush, then a hostile mage" beat structure. NPC stat blocks below
are **GM-abbreviated** per the ruled dual-mode fork (DEC-076 Ruling A: non-automated/tabletop
creatures use a simplified stat-block, resolution at GM discretion) — they are not full
24-attribute builds, and nothing here is Canonical or promoted.

---

## NPC Reference

| NPC | Skill (Tier / governing attribute) | Cap | Current | Resource pool | HP |
|---|---|---:|---:|---|---:|
| Goblin — Attack (bpp, Might) | 1 | 40 | 28 | Physical Energy: 35 | 22 |
| Goblin — Defense (bss, Reflexes) | 1 | 35 | 22 | (same pool) | — |
| Bargle — Bolt (mpp, Cunning) | 1 | 55 | 38 | MP: 30 | 26 |
| Aleena — Devotion (mee, Resolve) | 1 | 50 | 25 | MP: 28 | 30 |

All Skills above are Tier-1 (single governing attribute), consistent with Canonical §5.1.
Regen values for Recovery: Goblin PE Regen 12; Bargle MP Regen 10; Aleena MP Regen 11.

---

## Act I — The Ambush (Stealth and Resource Cost)

The player character is escorting Aleena, a young Devotion-skilled acolyte, along a forest
road when a Goblin springs from cover.

**Mechanic in play:** any deliberate attempt to notice or avoid the ambush is an ordinary
Core Test — one d100 roll against a Perception- or Stealth-type Skill. The roll succeeds if
`Roll ≤ Skill`. Whatever the natural roll is, that exact number is paid from the acting
character's resource pool (Physical Energy for a Body Skill, MP for a Mind Skill) — this is
**Cost = Roll**, not a flat action cost. If the pool can't cover it, the shortfall becomes
**Overflow**, applied directly as HP damage.

> **GM Tutorial Note — Stealth costs resources, and high rolls are expensive.**
> A new player will expect "spot the ambush" to be free or nearly free. In Tiwas it never is:
> rolling a 61 against a Skill of 45 costs 61 Physical Energy or MP *regardless of outcome*,
> because Cost is paid from the natural roll, not from success. If the character doesn't have
> 61 in the pool, the excess becomes Overflow → HP damage — a character can take real physical
> damage just from a costly, failed Perception check. This is the single most important early
> lesson: **every roll is an expenditure, not a free action.**

If the character fails to notice the Goblin, it attacks immediately. Resolve this as the
first S-1 opposed contest of Act III below rather than an automatic hit — Tiwas has no
"surprise round auto-damage"; ambush advantage is narrated, not mechanically free.

---

## Act II — Aleena's Aid (Recovery and Devotion)

Between the ambush and the confrontation with Bargle, give the player a quiet beat where
Aleena offers to mend a wound using her Devotion Skill (Tier-1, mee).

Aleena rolls d100 against her Devotion Skill (25). Say she rolls 19 — a success. She pays
**19 MP** as Cost (Cost = Roll, not Cap, not Skill). Her Devotion succeeding is a Core Test
success; whatever narrative healing effect you assign to it, the *mechanical* transaction
that just happened is: roll, cost, outcome, then Recovery.

**Recovery** always runs last, regardless of success, failure, or Overflow:

`Recovered = floor(Regen / 2)`

Aleena's MP Regen is 11, so she recovers `floor(11 / 2) = 5` MP this test, clamped at her
MP maximum. Her pool after the test: `28 (start) − 19 (cost) + 5 (recovery) = 14`.

> **GM Tutorial Note — Recovery is small, automatic, and always last.**
> New players often expect a "short rest" mechanic. Tiwas has none at the Core level — every
> test, win or lose, ends with the same floor(Regen/2) trickle-back, and that's it. This
> teaches the player that resource pools drain across a scene faster than they refill, which
> is exactly the tension the Core Test Transaction is built to create. Emphasize that
> Recovery is **not** optional and **not** skippable, and that it never varies with outcome.

---

## Act III — The Goblin (Margin Damage, the Opposed Contest, and 100-Fumble)

The Goblin attacks. This is a full S-1 opposed contest: both combatants roll simultaneously,
the acting side on Attack, the defending side on Defense.

1. **Player attacks.** Player rolls Attack; Goblin rolls Defense (28).
2. **Resolve the matrix:**
   - Both fail → repeat the contest.
   - Player succeeds, Goblin fails → player wins.
   - Goblin succeeds, player fails → Goblin wins, player's attack simply fails, no
     counter-Effect.
   - Both succeed → compare Margin (`Skill − Roll` for each); higher Margin wins; an exact
     tie repeats the contest.
3. **On a player win — Inflict Injury (HP damage) = Winner's Margin − Defender's Margin,
   never less than 0.**

Worked example: player's Attack Skill is 45, rolls 20 (Margin = 25). Goblin's Defense is 28,
rolls 26 (Margin = 2, a success). Both succeeded, so compare Margin: player's 25 beats the
Goblin's 2. Damage = `25 − 2 = 23` HP off the Goblin's 22 HP total — the Goblin goes down.

> **GM Tutorial Note — Damage is never a separate dice roll.**
> There is no "damage die" in Tiwas. The same roll that determined success also determines
> *how much* it mattered, via Margin. A narrow win barely scratches; a wide win (low roll
> against a high Skill) can be devastating. This is why Cost and damage are entangled: a
> player who rolls very low pays little in resources but deals enormous damage — the system
> rewards efficient, well-trained rolls on both axes at once.

If the Goblin rolls exactly 100 on its Defense or Attack roll, that's a **100-Fumble** — it
automatically fails that roll regardless of its Skill value, and the roll simultaneously
qualifies as a failed Double, which (if it were a PC) would trigger Advanced Skill creation.
Use this moment to show the player that 100 is *always* the worst possible outcome, with no
exceptions.

---

## Act IV — Bargle's Trap (Overflow and the Two-Track Harm Model)

Bargle springs his ambush on Aleena, casting Bolt (Tier-1, mpp) against her.

Bargle rolls his Bolt Skill (38) and rolls, say, 71 — a failure for Bargle personally (his
own test fails since 71 > 38), but the fiction requires his player-facing threat to land
regardless of his own success/failure per your scene design; more commonly, resolve this as
Bargle *winning* an opposed contest against Aleena's Defense the same way the Goblin fight
worked in Act III. Assume Bargle wins with a Margin of 34 against Aleena's Defense Margin of
6: Inflict Injury = `34 − 6 = 28` HP.

Aleena has 30 HP. This does **not** flatly reduce her to 0 with a scripted death — Tiwas has
no such instant-kill clause. Instead, walk the table through the **Two-Track Harm Model**:

- **Track A (Injury/HP):** the 28 HP from the contest-delta is ordinary Injury, applied
  directly to Aleena's HP pool (30 → 2).
- **Track B (Wounds):** if Bargle's player declares a location-referencing Effect (requiring
  his Bolt to be a Skill-Tier ≥ 2 roll, which a Tier-1 Bolt cannot satisfy), a **Wound**
  could additionally be recorded as a separate, lasting `Location X Tier-Y Wound Z` state.
  Since Bargle's Bolt is only Tier-1 here, no Wound can be generated this exchange — only
  Injury applies.

Aleena survives at 2 HP, not 0, because the contest-delta happened to be less than her full
pool. If Bargle's Margin had instead exceeded her remaining MP/PE reserve on a *resource
test* rather than a direct opposed Injury exchange, the excess would be **Overflow**,
converting straight to HP damage on top of any other harm — the same Cost/Overflow mechanic
from Act I, just at dramatically higher stakes.

> **GM Tutorial Note — There is no scripted "hero drops to 0 and dies."**
> Every harm event in Tiwas — a costly failed roll's Overflow, or a won opposed contest's
> Margin-delta — is computed from the same small set of formulas the player has already used
> twice by this point in the session. When Aleena goes down, walk through *exactly* which
> numbers produced it: this is what "high-consequence" means in Tiwas — not narrative
> fiat, but a player being able to trace every point of harm back to a roll they saw happen.
> HP reaching 0 (not shown reached here, but worth flagging) triggers forced incapacitation
> with no roll or save — a mechanic worth previewing even if this scene doesn't need it.

---

## Closing the Session

By the end of these four beats the player has personally executed: a costed Skill test with
Overflow risk, a Recovery cycle, a full S-1 opposed contest with Margin-based damage, a
100-Fumble, and a Two-Track harm resolution — the entire Core loop Tiwas is built around,
with no separate damage dice, save mechanics, or hidden GM math anywhere in the sequence.
