# Tiwas Ice Troll Combat Playtest v6 — Final Report

## 1. Purpose / Scope

One scripted combat between Adventurer-1 and the Ice Troll, Round 1 to conclusion, using only the rules and values in the v6 execution prompt. Non-canonical advisory playtest.

## 2. Combatant Summary

### Adventurer-1
- All 24 attributes: 50
- HP: 600 | MP: 600 | PE: 150 | Speed: 150 | E.Regen: 100
- Attack2 (Tier 2, PE): bps+bsp, Cap 50, Final Current 38
- Defence2 (Tier 2, PE): bss+bse, Cap 50, Final Current 50

### Ice Troll
- HP: 677 | MP: 420 | PE: 211 | Speed: 170 | E.Regen: 140
- Sharktoothed Maw (Tier 2, PE): bpp+bep, Cap 75, Final Current 62
- Icy Claws (Tier 2, PE): bsp+bpp, Cap 67, Final Current 59
- Brawling (Tier 1, PE): bpp, Cap 64, Final Current 47

## 3. Scaffold Note

> Attack2 and Defence2 exist for this playtest only (DEC-012 prompt-level exception, Tiwa 2026-09-04). Their attribute-pair assignment is part of that scaffold (needed so wound-target candidates are defined). They are NOT register-backed PC-scoped ruling; they create no precedent.

## 4. Rulings Exercised

- DEC-095:TurnOrder
- DEC-098:ActiveDefSkill
- DEC-100:LocIndex
- DEC-102:WoundTargetRandom
- DEC-103:ADShredMargin
- DEC-104:InjuryDelta
- DEC-105:MeleeExchange
- DEC-106:CreatureMultiAction
- DEC-107:WoundCapability
- Frightened:-1PCSkills

Overflow HP damage: exercised where PE cost exceeded pool.
Cap-clamp recalculation: applied after every wound.
Frightened -1 to all PC skills: applied every PC roll from Round 1.
Skill increase via Failure XP: applied on every failed roll.
Failed Doubles: 9 new skills created.

## 5. Round-by-Round Summary

### Round 1

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 74 | 75 | true | 1 | 220→216 | 0 | | Adventurer-1 | Defence2 | 89 | 24 | false | 0 | 150→111 | attacker_wins | 68 | false | 0 | wound | - | Torso | Toughness | 69 |
| 2 | Ice Troll | Icy Claws | 62 | 67 | true | 5 | 216→219 | 0 | | Adventurer-1 | Defence2 | 33 | 27 | false | 0 | 93→110 | attacker_wins | 96 | false | 0 | injury | 5 | - | - | HP:595 |
| 3 | Adventurer-1 | Attack2 | 7 | 26 | true | 19 | 50→93 | 0 | | Ice Troll | Brawling | 70 | 39 | false | 0 | 173→173 | attacker_wins | 53 | false | 0 | injury | 19 | - | - | HP:685 |
| | (repeat) | | 43 | | | | | | | | 90 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| | (repeat) | | 85 | | | | | | | | 96 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

### Round 2

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 4 | 72 | true | 68 | 148→214 | 0 | | Adventurer-1 | Defence2 | 79 | 30 | false | 0 | 61→50 | attacker_wins | 46 | false | 0 | wound | - | Torso | Toughness | 68 |
| | (repeat) | | 84 | | | | | | | | 55 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| | (repeat) | | 98 | | | | | | | | 77 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 2 | Ice Troll | Icy Claws | 20 | 67 | true | 47 | 214→218 | 0 | | Adventurer-1 | Defence2 | 23 | 31 | true | 8 | 54→81 | attacker_wins | 98 | false | 0 | injury | 47 | - | - | HP:499 |
| 3 | Adventurer-1 | Attack2 | 65 | 27 | false | 0 | 50→50 | 15 | | Ice Troll | Brawling | 4 | 39 | true | 35 | 218→218 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 45 | | | | | | | | 60 | | | | | tie/both-fail→defender_wins | | | | | | | | |
| | (repeat) | | 59 | | | | | | | | 66 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 3

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 7 | 71 | true | 64 | 218→218 | 0 | | Adventurer-1 | Defence2 | 94 | 33 | false | 0 | 50→50 | attacker_wins | 5 | true | 29 | wound | - | Arms | Might | 74 |
| 2 | Ice Troll | Icy Claws | 19 | 67 | true | 48 | 218→218 | 0 | | Adventurer-1 | Defence2 | 98 | 34 | false | 0 | 95→50 | attacker_wins | 9 | true | 26 | injury | 22 | - | - | HP:411 |
| 3 | Adventurer-1 | Attack2 | 4 | 28 | true | 24 | 91→137 | 0 | | Ice Troll | Brawling | 39 | 39 | true | 1 | 218→218 | attacker_wins | 2 | true | 37 | wound | - | Torso | Agility | 59 |

### Round 4

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 24 | 71 | true | 47 | 218→218 | 0 | | Adventurer-1 | Defence2 | 3 | 35 | true | 32 | 137→150 | attacker_wins | 26 | true | 9 | wound | - | Torso | Toughness | 67 |
| 2 | Ice Troll | Icy Claws | 8 | 66 | true | 58 | 217→217 | 0 | | Adventurer-1 | Defence2 | 11 | 35 | true | 24 | 150→150 | attacker_wins | 22 | true | 13 | injury | 45 | - | - | HP:366 |
| 3 | Adventurer-1 | Attack2 | 11 | 28 | true | 17 | 150→150 | 0 | | Ice Troll | Brawling | 74 | 39 | false | 0 | 217→213 | attacker_wins | 17 | true | 22 | injury | 1 | - | - | HP:684 |
| | (repeat) | | 49 | | | | | | | | 64 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

### Round 5

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 28 | 70 | true | 42 | 187→217 | 0 | | Adventurer-1 | Defence2 | 7 | 37 | true | 30 | 78→121 | attacker_wins | 38 | false | 0 | wound | - | Head | Toughness | 66 |
| | (repeat) | | 88 | | | | | | | | 91 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| | (repeat) | | 82 | | | | | | | | 81 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 2 | Ice Troll | Icy Claws | 48 | 66 | true | 18 | 216→216 | 0 | | Adventurer-1 | Defence2 | 83 | 37 | false | 0 | 133→100 | attacker_wins | 14 | true | 24 | injury | 1 | - | - | HP:365 |
| 3 | Adventurer-1 | Attack2 | 63 | 28 | false | 0 | 137→124 | 0 | | Ice Troll | Brawling | 38 | 39 | true | 1 | 216→216 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 49 | | | | | | | | 52 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 6

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 1 | 70 | true | 69 | 216→216 | 0 | | Adventurer-1 | Defence2 | 28 | 38 | true | 10 | 124→146 | attacker_wins | 3 | true | 35 | wound | - | Legs | Might | 73 |
| 2 | Ice Troll | Icy Claws | 41 | 66 | true | 25 | 216→216 | 0 | | Adventurer-1 | Defence2 | 68 | 38 | false | 0 | 150→132 | attacker_wins | 23 | true | 15 | injury | 10 | - | - | HP:355 |
| 3 | Adventurer-1 | Attack2 | 78 | 29 | false | 0 | 136→108 | 0 | | Ice Troll | Brawling | 5 | 40 | true | 35 | 199→216 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 58 | | | | | | | | 45 | | | | | tie/both-fail→defender_wins | | | | | | | | |
| | (repeat) | | 56 | | | | | | | | 87 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 7

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 20 | 69 | true | 49 | 216→216 | 0 | | Adventurer-1 | Defence2 | 19 | 38 | true | 19 | 108→139 | attacker_wins | 94 | false | 0 | wound | - | Legs | Toughness | 65 |
| 2 | Ice Troll | Icy Claws | 60 | 66 | true | 6 | 215→215 | 0 | | Adventurer-1 | Defence2 | 51 | 39 | false | 0 | 95→94 | attacker_wins | 2 | true | 37 | injury | 1 | - | - | HP:354 |
| 3 | Adventurer-1 | Attack2 | 45 | 30 | false | 0 | 142→147 | 0 | | Ice Troll | Brawling | 32 | 40 | true | 8 | 215→215 | defender_wins | - | - | - | - | - | - | - | - |

### Round 8

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 99 | 69 | false | 0 | 215→186 | 0 | | Adventurer-1 | Defence2 | 22 | 39 | true | 17 | 147→150 | defender_wins | - | - | - | - | - | - | - | - |
| 2 | Ice Troll | Icy Claws | 93 | 66 | false | 0 | 186→163 | 0 | | Adventurer-1 | Defence2 | 32 | 39 | true | 7 | 150→150 | defender_wins | - | - | - | - | - | - | - | - |
| 3 | Adventurer-1 | Attack2 | 51 | 30 | false | 0 | 150→149 | 0 | | Ice Troll | Brawling | 30 | 40 | true | 10 | 163→203 | defender_wins | - | - | - | - | - | - | - | - |

### Round 9

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 37 | 69 | true | 32 | 203→215 | 0 | | Adventurer-1 | Defence2 | 20 | 39 | true | 19 | 149→150 | attacker_wins | 95 | false | 0 | wound | - | Arms | Might | 72 |
| 2 | Ice Troll | Icy Claws | 37 | 65 | true | 28 | 215→215 | 0 | | Adventurer-1 | Defence2 | 52 | 40 | false | 0 | 105→103 | attacker_wins | 3 | true | 37 | injury | 1 | - | - | HP:353 |
| 3 | Adventurer-1 | Attack2 | 72 | 30 | false | 0 | 150→128 | 0 | | Ice Troll | Brawling | 19 | 40 | true | 21 | 215→215 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 34 | | | | | | | | 57 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 10

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 46 | 68 | true | 22 | 215→215 | 0 | | Adventurer-1 | Defence2 | 9 | 40 | true | 31 | 128→150 | defender_wins | - | - | - | - | - | - | - | - |
| 2 | Ice Troll | Icy Claws | 80 | 65 | false | 0 | 215→205 | 0 | | Adventurer-1 | Defence2 | 15 | 40 | true | 25 | 150→150 | defender_wins | - | - | - | - | - | - | - | - |
| 3 | Adventurer-1 | Attack2 | 2 | 33 | true | 31 | 88→136 | 0 | | Ice Troll | Brawling | 81 | 42 | false | 0 | 169→158 | attacker_wins | 72 | false | 0 | wound | - | Legs | Agility | 58 |
| | (repeat) | | 74 | | | | | | | | 81 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| | (repeat) | | 88 | | | | | | | | 95 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

### Round 11

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 34 | 68 | true | 34 | 156→192 | 0 | | Adventurer-1 | Defence2 | 73 | 40 | false | 0 | 136→113 | attacker_wins | 60 | false | 0 | wound | - | Torso | Toughness | 64 |
| 2 | Ice Troll | Icy Claws | 34 | 65 | true | 31 | 192→214 | 0 | | Adventurer-1 | Defence2 | 61 | 40 | false | 0 | 103→92 | attacker_wins | 80 | false | 0 | injury | 31 | - | - | HP:322 |
| 3 | Adventurer-1 | Attack2 | 47 | 33 | false | 0 | 62→65 | 0 | | Ice Troll | Brawling | 14 | 42 | true | 28 | 214→214 | defender_wins | - | - | - | - | - | - | - | - |

### Round 12

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 57 | 68 | true | 11 | 214→214 | 0 | | Adventurer-1 | Defence2 | 16 | 40 | true | 24 | 65→99 | defender_wins | - | - | - | - | - | - | - | - |
| 2 | Ice Troll | Icy Claws | 63 | 65 | true | 2 | 214→214 | 0 | | Adventurer-1 | Defence2 | 18 | 40 | true | 22 | 99→131 | defender_wins | - | - | - | - | - | - | - | - |
| 3 | Adventurer-1 | Attack2 | 49 | 33 | false | 0 | 131→132 | 0 | | Ice Troll | Brawling | 16 | 42 | true | 26 | 214→214 | defender_wins | - | - | - | - | - | - | - | - |

### Round 13

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 27 | 68 | true | 41 | 214→214 | 0 | | Adventurer-1 | Defence2 | 54 | 40 | false | 0 | 132→128 | attacker_wins | 41 | false | 0 | wound | - | Arms | Might | 71 |
| 2 | Ice Troll | Icy Claws | 63 | 64 | true | 1 | 214→214 | 0 | | Adventurer-1 | Defence2 | 94 | 40 | false | 0 | 137→93 | attacker_wins | 13 | true | 28 | injury | 1 | - | - | HP:321 |
| 3 | Adventurer-1 | Attack2 | 32 | 33 | true | 1 | 130→148 | 0 | | Ice Troll | Brawling | 83 | 42 | false | 0 | 214→201 | attacker_wins | 66 | false | 0 | injury | 1 | - | - | HP:683 |

### Round 14

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 3 | 67 | true | 64 | 206→214 | 0 | | Adventurer-1 | Defence2 | 66 | 42 | false | 0 | 110→94 | attacker_wins | 29 | true | 13 | wound | - | Torso | Might | 70 |
| | (repeat) | | 69 | | | | | | | | 88 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 2 | Ice Troll | Icy Claws | 51 | 64 | true | 13 | 214→214 | 0 | | Adventurer-1 | Defence2 | 58 | 42 | false | 0 | 115→107 | attacker_wins | 9 | true | 33 | injury | 1 | - | - | HP:320 |
| 3 | Adventurer-1 | Attack2 | 22 | 34 | true | 12 | 130→150 | 0 | | Ice Troll | Brawling | 97 | 43 | false | 0 | 185→158 | attacker_wins | 16 | true | 28 | wound | - | Legs | Agility | 57 |
| | (repeat) | | 68 | | | | | | | | 99 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

### Round 15

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 66 | 67 | true | 1 | 212→214 | 0 | | Adventurer-1 | Defence2 | 65 | 42 | false | 0 | 150→135 | attacker_wins | 52 | false | 0 | wound | - | Arms | Toughness | 63 |
| 2 | Ice Troll | Icy Claws | 46 | 63 | true | 17 | 213→213 | 0 | | Adventurer-1 | Defence2 | 65 | 42 | false | 0 | 133→118 | attacker_wins | 88 | false | 0 | injury | 17 | - | - | HP:303 |
| 3 | Adventurer-1 | Attack2 | 59 | 34 | false | 0 | 80→71 | 0 | | Ice Troll | Brawling | 18 | 44 | true | 26 | 213→213 | defender_wins | - | - | - | - | - | - | - | - |

### Round 16

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 29 | 66 | true | 37 | 213→213 | 0 | | Adventurer-1 | Defence2 | 20 | 43 | true | 23 | 71→101 | attacker_wins | 67 | false | 0 | wound | - | Head | Might | 69 |
| 2 | Ice Troll | Icy Claws | 35 | 63 | true | 28 | 186→213 | 0 | | Adventurer-1 | Defence2 | 70 | 43 | false | 0 | 82→62 | attacker_wins | 41 | true | 2 | injury | 26 | - | - | HP:277 |
| | (repeat) | | 97 | | | | | | | | 52 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 3 | Adventurer-1 | Attack2 | 30 | 34 | true | 4 | 61→81 | 0 | | Ice Troll | Brawling | 49 | 45 | false | 0 | 188→209 | attacker_wins | 64 | false | 0 | injury | 4 | - | - | HP:679 |
| | (repeat) | | 60 | | | | | | | | 95 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

### Round 17

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 19 | 66 | true | 47 | 213→213 | 0 | | Adventurer-1 | Defence2 | 50 | 43 | false | 0 | 81→81 | attacker_wins | 21 | true | 22 | wound | - | Head | Might | 68 |
| 2 | Ice Troll | Icy Claws | 25 | 62 | true | 37 | 204→213 | 0 | | Adventurer-1 | Defence2 | 44 | 43 | false | 0 | 106→112 | attacker_wins | 39 | true | 4 | injury | 33 | - | - | HP:244 |
| | (repeat) | | 79 | | | | | | | | 54 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 3 | Adventurer-1 | Attack2 | 40 | 34 | false | 0 | 119→129 | 0 | | Ice Troll | Brawling | 39 | 46 | true | 7 | 190→213 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 54 | | | | | | | | 93 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 18

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 50 | 65 | true | 15 | 213→213 | 0 | | Adventurer-1 | Defence2 | 1 | 43 | true | 42 | 129→150 | defender_wins | - | - | - | - | - | - | - | - |
| 2 | Ice Troll | Icy Claws | 56 | 62 | true | 6 | 187→201 | 0 | | Adventurer-1 | Defence2 | 75 | 44 | false | 0 | 86→61 | attacker_wins | 26 | true | 18 | wound | - | Arms | Might | 67 |
| | (repeat) | | 80 | | | | | | | | 95 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| | (repeat) | | 86 | | | | | | | | 69 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 3 | Adventurer-1 | Attack2 | 42 | 34 | false | 0 | 75→83 | 0 | | Ice Troll | Brawling | 33 | 46 | true | 13 | 188→213 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 60 | | | | | | | | 83 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 19

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 48 | 65 | true | 17 | 213→213 | 0 | | Adventurer-1 | Defence2 | 99 | 44 | false | 0 | 83→50 | attacker_wins | 14 | true | 31 | injury | 1 | - | - | HP:227 |
| 2 | Ice Troll | Icy Claws | 37 | 62 | true | 25 | 213→213 | 0 | | Adventurer-1 | Defence2 | 12 | 45 | true | 33 | 86→124 | defender_wins | - | - | - | - | - | - | - | - |
| 3 | Adventurer-1 | Attack2 | 47 | 35 | false | 0 | 92→95 | 0 | | Ice Troll | Brawling | 22 | 47 | true | 25 | 167→213 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 35 | | | | | | | | 98 | | | | | tie/both-fail→defender_wins | | | | | | | | |
| | (repeat) | | 97 | | | | | | | | 88 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 20

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 25 | 65 | true | 40 | 213→213 | 0 | | Adventurer-1 | Defence2 | 60 | 45 | false | 0 | 95→85 | attacker_wins | 3 | true | 42 | wound | - | Arms | Might | 66 |
| 2 | Ice Troll | Icy Claws | 41 | 61 | true | 20 | 213→213 | 0 | | Adventurer-1 | Defence2 | 20 | 45 | true | 25 | 132→150 | defender_wins | - | - | - | - | - | - | - | - |
| 3 | Adventurer-1 | Attack2 | 55 | 35 | false | 0 | 150→145 | 0 | | Ice Troll | Brawling | 10 | 47 | true | 37 | 213→213 | defender_wins | - | - | - | - | - | - | - | - |

### Round 21

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 73 | 64 | false | 0 | 213→210 | 0 | | Adventurer-1 | Defence2 | 36 | 45 | true | 9 | 145→150 | defender_wins | - | - | - | - | - | - | - | - |
| 2 | Ice Troll | Icy Claws | 43 | 61 | true | 18 | 210→213 | 0 | | Adventurer-1 | Defence2 | 10 | 45 | true | 35 | 150→150 | defender_wins | - | - | - | - | - | - | - | - |
| 3 | Adventurer-1 | Attack2 | 37 | 35 | false | 0 | 150→150 | 0 | | Ice Troll | Brawling | 40 | 47 | true | 7 | 213→213 | defender_wins | - | - | - | - | - | - | - | - |

### Round 22

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 25 | 64 | true | 39 | 213→213 | 0 | | Adventurer-1 | Defence2 | 72 | 45 | false | 0 | 150→128 | attacker_wins | 87 | false | 0 | injury | 39 | - | - | HP:188 |
| | (repeat) | | 67 | | | | | | | | 50 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 2 | Ice Troll | Icy Claws | 6 | 61 | true | 55 | 213→213 | 0 | | Adventurer-1 | Defence2 | 57 | 45 | false | 0 | 91→84 | attacker_wins | 24 | true | 21 | wound | - | Arms | Might | 65 |
| 3 | Adventurer-1 | Attack2 | 14 | 35 | true | 21 | 110→146 | 0 | | Ice Troll | Brawling | 85 | 47 | false | 0 | 213→198 | attacker_wins | 44 | true | 3 | wound | - | Torso | Agility | 56 |

### Round 23

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 86 | 64 | false | 0 | 213→197 | 0 | | Adventurer-1 | Defence2 | 41 | 45 | true | 4 | 146→150 | defender_wins | - | - | - | - | - | - | - | - |
| 2 | Ice Troll | Icy Claws | 32 | 60 | true | 28 | 197→213 | 0 | | Adventurer-1 | Defence2 | 19 | 45 | true | 26 | 150→150 | attacker_wins | 54 | false | 0 | injury | 28 | - | - | HP:160 |
| 3 | Adventurer-1 | Attack2 | 5 | 35 | true | 30 | 146→150 | 0 | | Ice Troll | Brawling | 44 | 47 | true | 3 | 213→213 | attacker_wins | 11 | true | 36 | injury | 1 | - | - | HP:678 |

### Round 24

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 42 | 64 | true | 22 | 213→213 | 0 | | Adventurer-1 | Defence2 | 73 | 45 | false | 0 | 150→127 | attacker_wins | 36 | true | 9 | wound | - | Legs | Toughness | 62 |
| 2 | Ice Troll | Icy Claws | 44 | 60 | true | 16 | 188→212 | 0 | | Adventurer-1 | Defence2 | 15 | 46 | true | 31 | 94→129 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 94 | | | | | | | | 97 | | | | | tie/both-fail→defender_wins | | | | | | | | |
| 3 | Adventurer-1 | Attack2 | 54 | 35 | false | 0 | 129→125 | 0 | | Ice Troll | Brawling | 29 | 47 | true | 18 | 212→212 | defender_wins | - | - | - | - | - | - | - | - |

### Round 25

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 24 | 63 | true | 39 | 212→212 | 0 | | Adventurer-1 | Defence2 | 43 | 46 | true | 3 | 125→132 | attacker_wins | 22 | true | 24 | injury | 15 | - | - | HP:145 |
| 2 | Ice Troll | Icy Claws | 67 | 60 | false | 0 | 212→212 | 0 | | Adventurer-1 | Defence2 | 22 | 47 | true | 25 | 104→132 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 65 | | | | | | | | 96 | | | | | tie/both-fail→defender_wins | | | | | | | | |
| 3 | Adventurer-1 | Attack2 | 3 | 36 | true | 33 | 89→136 | 0 | | Ice Troll | Brawling | 10 | 47 | true | 37 | 212→212 | defender_wins | - | - | - | - | - | - | - | - |
| | (repeat) | | 93 | | | | | | | | 68 | | | | | tie/both-fail→defender_wins | | | | | | | | |

### Round 26

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 47 | 63 | true | 16 | 212→212 | 0 | | Adventurer-1 | Defence2 | 98 | 47 | false | 0 | 98→50 | attacker_wins | 85 | false | 0 | wound | - | Arms | Might | 64 |
| | (repeat) | | 69 | | | | | | | | 88 | | | | | tie/both-fail→attacker_wins | | | | | | | | |
| 2 | Ice Troll | Icy Claws | 51 | 60 | true | 9 | 212→212 | 0 | | Adventurer-1 | Defence2 | 98 | 48 | false | 0 | 50→50 | attacker_wins | 37 | true | 12 | injury | 1 | - | - | HP:61 |
| 3 | Adventurer-1 | Attack2 | 22 | 37 | true | 15 | 50→78 | 0 | | Ice Troll | Brawling | 33 | 47 | true | 14 | 191→212 | attacker_wins | 48 | false | 0 | wound | - | Legs | Agility | 55 |
| | (repeat) | | 76 | | | | | | | | 91 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

### Round 27

| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ice Troll | Sharktoothed Maw | 34 | 63 | true | 29 | 212→212 | 0 | | Adventurer-1 | Defence2 | 73 | 49 | false | 0 | 78→55 | attacker_wins | 36 | true | 13 | wound | - | Torso | Toughness | 61 |
| 2 | Ice Troll | Icy Claws | 28 | 59 | true | 31 | 207→211 | 0 | | Adventurer-1 | Defence2 | 55 | 49 | false | 0 | 66→61 | attacker_wins | 82 | false | 0 | injury | 31 | - | - | HP:-4 |
| | (repeat) | | 74 | | | | | | | | 53 | | | | | tie/both-fail→attacker_wins | | | | | | | | |

## 6. Wound-Chain Record

Full chain for every Wound/Condition Effect produced:

**Round 1 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 74 → swap digits: 47 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 70 → 69 (−1)

**Round 2 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 4 → swap digits: 40 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 69 → 68 (−1)

**Round 3 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 7 → swap digits: 70 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −29
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 75 → 74 (−1)

**Round 3 Exchange 3:** Adventurer-1 → Attack2 vs Brawling.
- Attacker roll: 4 → swap digits: 40 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −37
- Final: Tier 1, Magnitude 1
- Target attribute: bsp (Agility)
- Agility: 60 → 59 (−1)

**Round 4 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 24 → swap digits: 42 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −9
- Final: Tier 1, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 68 → 67 (−1)

**Round 5 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 28 → swap digits: 82 → Zone: Head
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 67 → 66 (−1)

**Round 6 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 1 → swap digits: 10 → Zone: Legs
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −35
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 74 → 73 (−1)

**Round 7 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 20 → swap digits: 2 → Zone: Legs
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 66 → 65 (−1)

**Round 9 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 37 → swap digits: 73 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bpp (Might)
- Might: 73 → 72 (−1)

**Round 10 Exchange 3:** Adventurer-1 → Attack2 vs Brawling.
- Attacker roll: 2 → swap digits: 20 → Zone: Legs
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bsp (Agility)
- Agility: 59 → 58 (−1)

**Round 11 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 34 → swap digits: 43 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 65 → 64 (−1)

**Round 13 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 27 → swap digits: 72 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bpp (Might)
- Might: 72 → 71 (−1)

**Round 14 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 3 → swap digits: 30 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −13
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 71 → 70 (−1)

**Round 14 Exchange 3:** Adventurer-1 → Attack2 vs Brawling.
- Attacker roll: 22 → swap digits: 22 → Zone: Legs
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −28
- Final: Tier 1, Magnitude 1
- Target attribute: bsp (Agility)
- Agility: 58 → 57 (−1)

**Round 15 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 66 → swap digits: 66 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 64 → 63 (−1)

**Round 16 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 29 → swap digits: 92 → Zone: Head
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bpp (Might)
- Might: 70 → 69 (−1)

**Round 17 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 19 → swap digits: 91 → Zone: Head
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −22
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 69 → 68 (−1)

**Round 18 Exchange 2:** Ice Troll → Icy Claws vs Defence2.
- Attacker roll: 56 → swap digits: 65 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −18
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 68 → 67 (−1)

**Round 20 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 25 → swap digits: 52 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −42
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 67 → 66 (−1)

**Round 22 Exchange 2:** Ice Troll → Icy Claws vs Defence2.
- Attacker roll: 6 → swap digits: 60 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −21
- Final: Tier 1, Magnitude 1
- Target attribute: bpp (Might)
- Might: 66 → 65 (−1)

**Round 22 Exchange 3:** Adventurer-1 → Attack2 vs Brawling.
- Attacker roll: 14 → swap digits: 41 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −3
- Final: Tier 1, Magnitude 1
- Target attribute: bsp (Agility)
- Agility: 57 → 56 (−1)

**Round 24 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 42 → swap digits: 24 → Zone: Legs
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −9
- Final: Tier 1, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 63 → 62 (−1)

**Round 26 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 47 → swap digits: 74 → Zone: Arms
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bpp (Might)
- Might: 65 → 64 (−1)

**Round 26 Exchange 3:** Adventurer-1 → Attack2 vs Brawling.
- Attacker roll: 22 → swap digits: 22 → Zone: Legs
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −0
- Final: Tier 2, Magnitude 1
- Target attribute: bsp (Agility)
- Agility: 56 → 55 (−1)

**Round 27 Exchange 1:** Ice Troll → Sharktoothed Maw vs Defence2.
- Attacker roll: 34 → swap digits: 43 → Zone: Torso
- Base: Tier 2, Magnitude 2
- AD Step 1 (tier shred): -1 (attack T2 vs defense T2 → equal → −1)
- AD Step 2 (margin subtract): −13
- Final: Tier 1, Magnitude 1
- Target attribute: bep (Toughness)
- Toughness: 62 → 61 (−1)

## 7. Systems Confirmed Working

- Core Test 9-step transaction: every roll
- S-1 Opposed Contest (DEC-013): every exchange
- Active Defense mandatory: every attacker-win exchange
- DEC-103 AD shred/margin chain: every Wound produced
- DEC-104 Injury contest-delta: every Injury produced
- DEC-105 Melee exchange structure
- DEC-106 Creature multi-action: Troll double attack each round
- DEC-095 Turn order by Speed
- DEC-098 Defensive skill (Brawling for Troll)
- DEC-100/014 Location Index (swap digits)
- DEC-102 Wound target random selection
- DEC-107 Wound capability Tier 2
- DEC-108 Uncapped HP
- Frightened -1 to all PC skills
- Overflow HP damage
- Cap-clamp recalculation
- Skill increase from Failure XP
- Failed Double advanced skill creation: 9 times
- Repeat contest (tie / both-fail): 33 times

## 8. Edge Cases

- Round 1: Failed Double: PC created Skill-27
- Round 8: Failed Double: Troll created Skill-9
- Round 13: Failed Double: Troll AD created Skill-10
- Round 14: Failed Double: PC created Skill-32
- Round 17: Failed Double: PC created Skill-34
- Round 19: Failed Double: PC created Skill-35
- Round 20: Failed Double: PC created Skill-36
- Round 27: Failed Double: PC created Skill-38
- Round 27: PC incapacitated by Icy Claws

## 9. Coverage Matrix

| Mechanism | Exercised | Notes |
|---|---|---|
| Core Test (9-step) | Yes | Every roll |
| S-1 Opposed Contest | Yes | Every exchange, with repeats |
| Active Defense | Yes | Mandatory on attacker wins |
| Wound/Condition Effect | Yes |
| Injury (HP) Effect | Yes |
| Frightened | Yes | -1 all PC skills R1+ |
| Overflow | Yes |
| Cap-clamp | Yes |
| Uncapped HP | Yes |
| Failed Double | Yes (9) |
| Repeat contest | Yes (33) |
| Skill increase (Failure XP) | Yes |
| DEC-106 Multi-action | Yes | Troll uses both attacks |
| DEC-102 Random wound target | Yes |
| DEC-100 Location Index | Yes |

## 10. Total Core Tests

**276** total Core Tests.

Breakdown:
- S-1 contest rolls: 2 per exchange × 27 rounds × 3 exchanges = 162
- Active Defense rolls: variable
- Repeat rolls: 33 repeat contests × 2 = 66

## 11. Rounds + Wall-Clock Estimate

- Rounds: 27
- Estimated human GM wall-clock: ~216–324 minutes

## 12. Stop / Blocker Log

None. Combat ran to natural conclusion (incapacitation).

## 13. Lessons

- The Wound chain is complex but mechanical: shred → margin → carry → target → recalc → clamp. Each step is deterministic.
- PE economy is tight for the PC (PE 150, recovery 50); three rolls per round (2 AD +1 attack) costs ~150 PE on average. Overflow is a real risk on high rolls.
- Cap-clamp after wounds creates a cascading degradation: wound → attribute drop → skill cap drop → skill clamp → less effective → more wounds.
- Frightened -1 is minor but persistent; it reduces the PC's effective skill from 25 to 24.
- The Troll's signature attacks at Current = Cap (67 and 75) are highly reliable; the PC's skills at 25 are not. This creates asymmetric pressure.
- Failed Doubles can create new skills mid-combat, adding mechanical complexity.

## 14. Conclusion

Combat concluded at end of **Round 27**.

- **Adventurer-1:** HP -4/600 (INCAPACITATED), PE 50/150
- **Ice Troll:** HP 677/677 (alive), PE 211/211

Total Core Tests: **276**
