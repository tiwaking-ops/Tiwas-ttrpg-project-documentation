---
document:
  title: "Tiwas — Ice Troll Combat Playtest (v6 executor prompt)"
  version: "6.0"
  status: "Advisory (not canonical). Self-contained execution prompt. Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
supersedes:
  - "tiwas-ice-troll-combat-playtest-prompt-v5-2026-09-05.md"
---

# Tiwas Ice Troll Combat Playtest — v6 Execution Prompt

## 1. Your task

Run one scripted combat between **Adventurer-1** and the **Ice Troll**, from Round 1 to
conclusion, mechanically and literally, using **only the rules and values in THIS document**.
You have everything you need. **Begin immediately.** Do not ask for permission. Do not ask for
more files. Do not wait for any decision. Do not request a rules corpus. All operational
parameters are fixed in Section 6.

## 2. Combatants (use these values exactly; do not re-derive)

### 2.1 Adventurer-1 (automated playtest PC)

- All 24 attributes fixed at **50** (do not randomize).
- Derived: HP **600**; MP **600**; Physical Energy **150**; Speed **150**; Energy Regen **100**;
  MP Regen **100**; Movement **6**.
- All 24 Tier-1 skills present: Cap 50, Current 25 each. (12 Body-rooted, PE domain; 12
  Mind-rooted, MP domain.)
- **Attack2** (Tier 2): formula `bps (Impact 50) + bsp (Agility 50)`; Cap 50; Current 25;
  PE domain.
- **Defence2** (Tier 2): formula `bss (Reflexes 50) + bse (Quickness 50)`; Cap 50; Current 25;
  PE domain.
- Any Advanced Skill created mid-combat via a qualifying failed Double: Tier+1, starting value 1,
  named `Skill-(n)` (n = the character's total skill count after creation).

> **Scaffold note (non-canonical, must be logged as scaffold):** Attack2 and Defence2 exist for
> this playtest only (DEC-012 prompt-level exception, Tiwa 2026-09-04). Their attribute-pair
> assignment is part of that scaffold (needed so wound-target candidates are defined). They are
> NOT register-backed PC-scoped ruling; they create no precedent.

### 2.2 Ice Troll

**GURPS source (reference only — never imported):** ST 15, DX 12, IQ 7, HT 12; HP 15; Icy Claws
(13) 1d+2 cut; Sharktoothed Maw (13) 1d+2 cut. No GURPS damage dice, Dodge/Parry, or DR imported.

**Attributes (all 24):**

| Code | Attr | Val | Code | Attr | Val |
|---|---|---|---:|---|---|---:|
| bpp | Might | 75 | mpp | Cunning | 45 |
| bps | Impact | 65 | mps | Wits | 30 |
| bpe | Brawn | 70 | mpe | Willpower | 55 |
| bpx | Presence | 55 | mpx | Glamour | 10 |
| bsp | Agility | 60 | msp | Acuity | 40 |
| bss | Reflexes | 55 | mss | Perception | 60 |
| bse | Quickness | 60 | mse | Alacrity | 35 |
| bsx | Grace | 20 | msx | Charm | 5 |
| bep | Toughness | 75 | mep | Focus | 45 |
| bes | Stamina | 65 | mes | Discipline | 30 |
| bee | Vitality | 80 | mee | Resolve | 50 |
| bex | Poise | 25 | mex | Composure | 15 |

**Derived:** HP **705**; MP **420**; Physical Energy **220**; Speed **175**; Energy Regen **140**;
MP Regen **75**; Movement **7**.

**Skills (Cap = floored average of the listed formula attributes; Current as given):**

| Skill | Tier | Formula attributes | Cap | Current | Domain |
|---|---|---|---:|---:|---:|---:|
| Icy Claws | 2 | bsp (60) + bpp (75) | 67 | 67 | Physical Energy |
| Sharktoothed Maw | 2 | bpp (75) + bep (75) | 75 | 75 | Physical Energy |
| Brawling | 1 | bpp (75) | 75 | 37 | Physical Energy |
| Camouflage | 1 | mss (60) | 60 | 30 | MP |
| Stealth | 1 | bse (60) | 60 | 30 | Physical Energy |
| Tracking | 1 | mss (60) | 60 | 30 | MP |

**Defensive skill (DEC-098):** the Troll has no dedicated authored defensive skill. Active Defense
uses **Brawling (37)**.

**Traits (fixed for this run):** `damage:slashing` on both attacks. Appearance (Hideous) is an
active fear source (see Frightened, Section 5). Regeneration / Regrowth / DR are **inactive**
(no `env:freezing` scene state) — do not apply them.

**Wound capability (DEC-107):** both signature attacks are Skill-Tier 2, so any Wound/Condition
Effect they produce is **Tier 2 / Magnitude −2**. They cannot natively produce higher tiers.

## 3. Rules (complete — use ONLY these)

### 3.1 Core Test (9-step transaction)

1. Roll 1d100 (1–100; `00` = 100).
2. Determine domain: Body-rooted skill → Physical Energy; Mind-rooted skill → MP.
3. Outcome: **Success if Roll ≤ Skill; 100 always fails.**
4. Pay **Cost = Roll** from the pool.
5. **Overflow:** if Cost > remaining pool, pool → 0 and `Overflow = Cost − remaining` becomes
   **direct HP damage to the roller** (the attacker pays it; it never hits the target).
6. **Failure XP** = `max(0, Roll − Skill)` → temporary Skill Roll Pool: while `Pool ≥ Skill` and
   `Skill < Cap`, `Pool −= Skill; Skill += 1`. Remainder → General XP (may exceed Cap).
7. **Failed Double** (11, 22, 33, 44, 55, 66, 77, 88, 99, 100) on a failure → create an Advanced
   Skill: Tier+1, add one attribute not already in the formula, recalc Cap, starting value 1.
8. **Recovery** = `floor(Regen/2)`, clamped to the pool's max, always the final step.
9. Derived statistics are **live**: an attribute change immediately recalcs every dependent skill,
   Cap, HP/MP/PE maximum.

### 3.2 S-1 Opposed Contest (DEC-013)

Two participants each roll their own skill (full 9-step transaction each). Combat uses the
**Margin** Quality measure: `Quality = Skill − Roll` on a success (minimum 1).

| Attacker | Defender | Result |
|---|---|---|
| Success | Failure | Attacker wins |
| Failure | Success | Defender wins → **attack fails; no counter-Effect** (DEC-101) |
| Success | Success | Higher Quality wins; **exact tie → repeat** as a fresh contest |
| Failure | Failure | **Repeat** as a fresh contest |

### 3.3 Melee exchange (DEC-105)

- One exchange = **one S-1 opposed contest; both participants always roll.**
- **Attacker wins** → award one Effect (Section 3.4).
- **Defender wins** → nothing happens.
- **Active Defense is MANDATORY in this playtest.** Whenever the attacker wins, the defender makes
  its own Active Defense Core Test using its defending skill (Adventurer-1: Defence2; Troll:
  Brawling) before the Effect is applied.
- **Turn order (DEC-095):** highest Speed first. Ice Troll (Speed 175) acts before Adventurer-1
  (Speed 150) every round. Ties: both reroll (not needed here).
- **Creature multi-action (DEC-106):** the Troll uses BOTH authored attacks on its own turn,
  back-to-back, highest-Skill first: **Sharktoothed Maw (75), then Icy Claws (67)** — each is its
  own separate exchange with its own mandatory Active Defense and its own Core Test cost. The PC
  has ONE attack action per turn. No AoE (single target).

### 3.4 Awarding an Effect

On each attacker-win, the attacker selects one Effect of the following two (policy in Section 5):

**(a) Inflict Injury (HP).** Damage = `Winner's Margin − Defender's Margin` (contest-delta,
DEC-104). Defender's Margin counts **only if the defender's Active Defense succeeded** (failed AD →
0). A won attack always deals at least 1 HP. HP is **uncapped** — record the raw value including
negative numbers (DEC-108).

**(b) Wound/Condition Effect.** Requires a **Location Index** — only possible when the causing
skill is Skill-Tier ≥ 2 (DEC-041). Tier-1 skills cannot produce this Effect.

1. **Location Index (DEC-014, DEC-100):** swap the tens/units digits of the **attacker's natural
   d100 roll** (`00` = 100 after swap). Then map: **1–25 Legs; 26–50 Torso; 51–75 Arms; 76–100
   Head.**
2. **Base Effect:** `Tier Y = the causing skill's Skill-Tier; Magnitude Y` (DEC-107 → Tier 2,
   Magnitude 2 for all Tier-2 attacks here).
3. **Active Defense modifies the Effect before it is recorded (DEC-103):**
   - Step 1 — Skill-Tier shred: compare the **attack** skill-tier to the **defense** skill-tier:
     equal → magnitude −1; defense higher → `−(DefTier − AtkTier)` (cascading); attack higher →
     magnitude +1.
   - Step 2 — Margin: subtract the defender's Margin on a **successful** Active Defense.
   - Carry: if magnitude would drop below 1 at 0 → reduce Tier by 1 and set magnitude to the new
     Tier; if Tier would reach 0 → **Effect is negated** (only if the AD succeeded).
   - Survivor record: `Location <zone> Tier-Y <Effect>`, magnitude = −Y. **Effects affect
     Attributes/Skills, never HP directly.**
4. **Wound target (DEC-102):** the affected Attribute is a **Body attribute of the causing
   skill**. Candidate sets:
   - Icy Claws → {bsp Agility, bpp Might}
   - Sharktoothed Maw → {bpp Might, bep Toughness}
   - Attack2 (PC) → {bps Impact, bsp Agility}
   Automated playtest characters are creatures for this purpose → **select randomly among the
   candidates**; log the selection. Reduce that attribute by the **final post-shred magnitude** (the
   magnitude remaining after AD Steps 1–2 and the Carry step above), then recalc every dependent
   skill, Cap, and HP/MP/PE maximum immediately (live statistics). (Mind-only causing skills would
   wound Mind attributes; none of these skills is Mind-only.)

   **Recalculation default (operational, scaffold, NOT a rule or ruling):** if any dependent
   skill's recalculated Cap drops below that skill's Current value, the Current value **clamps down
   to the new Cap** (excess absorbed with no compensation); log any clamp. This is the only coherent
   behavior given skill gains require `Skill < Cap`, and it is fixed for this run.

**One Effect per win only (DEC-024).**

### 3.5 Frightened condition (DEC-094)

The Troll's Hideous presence is a declared fear source, active while perceivable: **−1 to ALL of
Adventurer-1's skills** from Round 1 onward. Apply before every PC roll. The Troll is unaffected.
Ends only if the Troll becomes unperceivable (incapacitated).

### 3.6 Incapacitation and end (DEC-052, DEC-108)

- HP = 0 → forced incapacitation (no save). HP continues to record **negative** afterward (uncapped).
- An incapacitated combatant is no longer a valid target for "nearest possible target" purposes.
- If all combatants are incapacitated, combat ends. Resume nothing; produce the report.

## 4. Round structure (repeat until the combat ends)

1. **Troll turn:** Exchange 1 — Sharktoothed Maw vs PC (PC mandatory AD). Exchange 2 — Icy Claws
   vs PC (PC mandatory AD).
2. **PC turn:** one Attack2 exchange vs Troll (Troll mandatory AD).
3. Start the next round.

**Effect-selection policy (deterministic, guarantees mandatory coverage):**
- Troll: on its **first** Effect-producing win, choose **Wound/Condition** (mandatory exercise of
  the Wound chain). Thereafter alternate: Wound, Injury, Wound, Injury, …
- PC: alternate starting with **Injury**: Injury, Wound, Injury, Wound, …

If no Effect-producing win has occurred by the end of Round 5, note it in the log; if none by the
end of Round 10, stop and report the stall (this is the only case where you report without completing).

## 5. Output

### 5.1 Pre-combat declaration
State: RNG source, computation method, and the fixed operational parameters below.

### 5.2 Live combat log
Round-by-round, **every Core Test** (attack, defense, active defense, repeat), each with its own row,
containing: Round; Turn; Exchange#; Step; Actor; Skill used (with current effective value including
Frightened/wound recalcs); d100; Success?; Margin; Quality; Cost; PE before → after Cost → Overflow
→ after Recovery → final (clamped); HP Overflow damage; Effect selected; Location Index/Zone;
Wound/Effect Tier & magnitude; Wound target attribute + recalcs; AD roll/skill/result; AD Step-1
shred; AD Step-2 margin; Net HP change (raw, may be negative); Conditions applied. Also: running
Core Test count; each repeat as its own row; edge cases noted; GM-stop/verbatim only if triggered.

### 5.3 Final report (markdown)
1. Purpose/Scope. 2. Combatant summary. 3. Scaffold note (verbatim Section-2.1 block). 4. Rulings
exercised (DEC-095/096/097/098/100/102/103/104/105/106/107/108 and Frightened/over-flow/death as they
occurred). 5. Round-by-round summary table. 6. Wound-chain record (full chain at least once). 7.
Systems confirmed working. 8. Edge cases. 9. Coverage matrix. 10. Total Core Tests (count +
breakdown). 11. Rounds + wall-clock estimate. 12. Stop/blocker log. 13. Lessons. 14. Conclusion.
**No mechanic may be ruled, promoted, or invented** anywhere in the report.

### 5.4 Structured JSON
Pre-combat state; per-round/per-exchange array (all rolls, margins, costs, overflows, recoveries,
HP, PE, effects, wound recalcs); post-combat state; totals; scaffold flags; edge-case array.

## 6. Fixed operational parameters (do NOT ask, do NOT change)

- Wound ceiling: **Tier 2** (Ice Troll Tier-2 attacks → Tier-2 Wounds). No higher-tier attack, no
  GM-Fiat override.
- Regeneration / Regrowth / DR: **inactive** (no `env:freezing` scene state).
- Armor / equipment: **none** on either side. No encumbrance.
- Range: melee (both attacks Reach C,1).
- No area-of-effect.
- Active Defense: mandatory.
- Adventurer-1 is an automated PC treated as a creature (random wound-target selection).
- Wound attribute-reduction magnitude = the **final post-shred magnitude**; any dependent skill
  whose recalculated Cap falls below its Current value **clamps down to the new Cap** (log it).

## 7. Stopping rule (bounded)

**Continue to the end.** Stop early and report ONLY in these cases:
1. A situation arises with no applicable rule in Section 3 AND no fixed parameter in Section 6.
2. No Effect-producing win by the end of Round 10 (stall report).
You may modify no rule, scaffold nothing new, and request no additional material.

## 8. Document status

Advisory playtest execution prompt — **non-canonical**. Makes no rulings, assigns no DEC numbers,
promotes/locks nothing. Supersedes the v5 playtest prompt (v5 left operational defaults as
open decision gates and omitted the per-skill attribute formulas, causing executor stalling;
v6 fixes both).