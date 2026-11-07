---
document:
  title: "Tiwas — Adventure Module: Your First Adventure (Full Red Box Solo Tutorial Adaptation)"
  version: "0.2"
  status: "Advisory / Non-canonical. No DEC assigned. GM table-use and unattended-playtest scenario, not a ruling. Companion to tiwas-adventure-the-bargle-incident-2026-09-13.md. v0.2 applies Tiwa rulings D1–D7 (2026-09-14) and DEC-140."
  purpose: >
    Adapts the full 1983 Basic Rules solo tutorial ("Your First Adventure": goblin,
    rattlesnake, Aleena, ghouls, locked door, Bargle) to current Tiwas rulings, keeping
    the Bargle Incident's deliberate revision (Aleena survives) and both climax endings.
    Built for unattended multi-LLM playtest determinism with bounded scene resolution.
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
revision_note: >
  v0.2 (2026-09-14, from the R2/R3 playtest collation plus Tiwa rulings D1–D7):
  D1 — Bargle HP≤0 before the climax fork → Ending A immediately, fork skipped;
  D2 — Scene-1 Perception test is a MANDATORY module teaching beat with fixed roll 00 (=100),
  creating a named Advanced Skill (DEC-012); creature-side Advanced-Skill creation is
  universal under DEC-140; D3 — Zero-Step quoted verbatim from Canonical §14.1 (rule gap
  finding retracted; no new ruling), hazard zones corrected to DEC-100 quartiles
  (LI 30/LI 42 → Torso); D4 — exclusive one-Effect-per-winning-exchange (no sequential /
  compound path); D5 — budget-expiry withdrawal is the intended primary scene end;
  D6 — Scene-1 Perception test always resolves (mandatory); D7 — rewrite to v0.2, no
  re-run until Tiwa reviews this text. Execution reports R1–R3 remain as delivered.
  **v0.2 text ACCEPTED by Tiwa, 2026-09-14 (in-session): approved for playtest use; the
  document remains Advisory / Non-canonical — acceptance confers no promotion.**
---

# Tiwas — Your First Adventure

Loosely adapted from the 1983 Basic Set introductory solo adventure (Aleena/Bargle).
**Aleena survives** — continuity with the 2026-09-13 Bargle Incident module. Except for the
Scene-1 Perception teaching beat (which is a **fixed-roll 00 teaching beat**, D2/D6), all
numbers are worked examples for teaching/testing, not scripted outcomes: actual rolls diverge.

**Module-side corrections carried from the Bargle Incident collation (§8.7–8.8):**
Perception (mss, Mind-domain) tests charge **MP**, not PE; a Body-attribute Wound
live-recalculates HP downward (Bargle 452→449) — no Wound here is "cosmetic."

---

## Run Conventions for This Module (A1–A8)

Playtest-run conventions scoped to unattended execution. None is a rule; none alters
table play (DEC-070/074 GM discretion untouched).

| # | Convention |
|---|---|
| A1 | **Action economy (fixed):** one substantive exchange per combatant per round (single-action reading of DEC-106). DEC-106 multi- vs single-action remains OPEN (collation §7.1); this fixes it for cross-comparable unattended runs. |
| A2 | **Turn order:** Speed desc (DEC-095). Ties: higher bss, then bsp; remaining tie: reroll. |
| A3 | **Bounded scenes:** each combat has a maximum round budget (stated per scene). **Primary end = budget-expiry withdrawal beat** (D5 — the tutorial pacing leans on budget beats by design). **Secondary end = HP≤0** (forced incapacitation, DEC-052; negative HP persists, DEC-108), whichever occurs first. No mid-rule "bloodied" thresholds (none exists). |
| A4 | **Aleena-survives invariant:** Aleena never ends a scene at HP≤0. If resolved HP would cross 0, clamp at 1 and narrate collapse (module content, not a rule). |
| A5 | **Healing:** Automated Playtest Run Conventions — H1(a) restore = accumulated Margin capped at current max; H2 target 40; H3 module-designated skill (Devotion), MP cost = natural roll, HP-only restore; H4 targeted penalty; H7 locked accounting order; HC-1.1 sum magnitudes; HC-1.2 clamp; DEC-072.A. |
| A6 | **Advanced-Skill coverage — DETERMINISTIC in Sc.1, probabilistic elsewhere:** the Scene-1 Perception teaching beat is **mandatory with a fixed roll 00 (=100)** (D6/D2); it creates a **named Advanced Skill** (DEC-012). Elsewhere Advanced Skills are probabilistic — never force a failed Double outside the Sc.1 teaching beat. |
| A7 | **Terminality (H6):** HP≤0 = forced incapacitation, terminal for the run's combat. In Scene 6, **Bargle HP≤0 before the climax fork → Ending A immediately, fork SKIPPED** (D1). No revival invented. |
| A8 | **Effect rotation + exclusivity (D4):** per-round winner may declare the module-prescribed Effect — **exactly one Effect per winning exchange**; the contest identical to DEC-025 declared intent within the Effect/Condition vocabulary; **no sequential or compound multi-Effect path** from a single win. |

---

## Cast — Full 24-Attribute Stat Blocks

Compact grid, one value per attribute. Derived formulas locked (Canonical §4, DEC-004).
Skills: Tier — attributes — Cap — Start. `sig` = creature-signature full-Cap start (DEC-086/087).

### Rowan (Player Character — fresh Tier-1 start)
Body: bpp58 · bps52 · bpe47 · bpx40 · bsp61 · bss55 · bse50 · bsx38 · bep60 · bes53 · bee57 · bex44
Mind: mpp42 · mps45 · mpe50 · mpx33 · msp48 · mss55 · mse40 · msx46 · mep51 · mes43 · mee49 · mex47
Derived: **HP 615 · MP 549 · PE 170 · Speed 166 · ER 113 · MR 94 · Movement 7**
Skills: Attack T1 bpp cap58 **29** · Defense T1 bss cap55 **27** · Perception T1 mss cap55 **27**
· Stealth T1 bsp cap61 **30** · **Composure T1 mex cap47 23** (module-added, see Notes)
Gear: Shortsword (`state:held, offense:melee, damage:slashing, handling:light`); Leather
Armor (`state:worn, defense:armor`). **Tag: `reaction:vigilant`** (ally-targeted trigger, DEC-132.B).

### Aleena (Ally NPC)
Body: bpp45 · bps40 · bpe50 · bpx48 · bsp42 · bss47 · bse44 · bsx41 · bep55 · bes46 · bee58 · bex50
Mind: mpp50 · mps48 · mpe62 · mpx44 · msp46 · mss50 · mse43 · msx49 · mep60 · mes55 · mee65 · mex52
Derived: **HP 566 · MP 624 · PE 159 · Speed 133 · ER 101 · MR 115 · Movement 5**
Skills: Devotion T1 mee cap65 **32** · Smite T1 bep cap55 **27** · Defense T1 bss cap47 **23**
Gear: Mace (`state:held, offense:melee, damage:bludgeoning, handling:light`); Holy Vestments
(`state:worn` — **no** `defense:armor` Tag).

### Goblin (Creature)
Body: bpp40 · bps38 · bpe30 · bpx25 · bsp45 · bss48 · bse35 · bsx30 · bep32 · bes36 · bee34 · bex28
Mind: mpp22 · mps28 · mpe20 · mpx15 · msp25 · mss35 · mse24 · msx18 · mep20 · mes22 · mee25 · mex19
Derived: **HP 421 · MP 273 · PE 102 · Speed 128 · ER 68 · MR 42 · Movement 6**
Skills: Crude Attack T1 bpp cap40 **40 sig** · Defense T1 bss cap48 **24** · **Trip T2 bsp+bss cap46 46 sig**
Gear: Rusty Dagger (`offense:melee, damage:piercing, handling:light`). No armor tag.

### Rattlesnake (Creature — new)
Body: bpp30 · bps28 · bpe24 · bpx20 · bsp60 · bss58 · bse55 · bsx45 · bep22 · bes25 · bee24 · bex26
Mind: mpp15 · mps18 · mpe14 · mpx12 · msp30 · mss40 · mse28 · msx20 · mep16 · mes18 · mee15 · mex17
Derived: **HP 417 · MP 243 · PE 71 · Speed 173 · ER 47 · MR 34 · Movement 7**
Skills: **Venomous Bite T2 bsp+bss cap59 59 sig** · Defense T1 bss cap58 **29** · Stealth T1 bsp cap60 **30**
Gear: natural fangs. No armor tag. **Bite = Body-attribute Wound (poison-flavored; poison is
NOT a ruled Effect — representation flagged as advisory).**

### Ghoul (Creature — new)
Body: bpp42 · bps36 · bpe40 · bpx30 · bsp50 · bss52 · bse44 · bsx38 · bep40 · bes42 · bee44 · bex36
Mind: mpp20 · mps25 · mpe18 · mpx16 · msp28 · mss30 · mse22 · msx20 · mep18 · mes22 · mee20 · mex21
Derived: **HP 494 · MP 260 · PE 126 · Speed 146 · ER 82 · MR 40 · Movement 6**
Skills: **Claw T2 bpp+bps cap39 39 sig** · **Grapple T2 bsp+bpp cap46 46 sig** · Defense T1 bss cap52 **26**
· **Desecration T2 mpp+mps cap22 22 sig** (opposes turning).
Gear: natural claws. No armor tag.

### Bargle (Villain)
Body: bpp35 · bps32 · bpe30 · bpx44 · bsp40 · bss46 · bse38 · bsx42 · bep33 · bes35 · bee37 · bex40
Mind: mpp68 · mps65 · mpe60 · mpx55 · msp58 · mss52 · mse50 · msx48 · mep62 · mes57 · mee55 · mex50
Derived: **HP 452 · MP 680 · PE 105 · Speed 124 · ER 68 · MR 119 · Movement 5**
Skills: **Bolt T2 mpp+mps cap66 66 sig** · Defense T1 bss cap46 **23** · Beguile T1 mpx cap55 **27**
Gear: Gnarled Wand (`state:held, offense:ranged, damage:electric`); Traveling Robes
(`state:worn` — **no** `defense:armor` Tag).

> **Notes**
> 1. One Skill, several declared Effects (DEC-025): the Skill's label never gates the Effect;
>    Wound / Inflict Injury / (vs armored targets) Armor Bypass all ride the same roll.
> 2. **Composure (mex)** is module-added for the climax domination fork (Bargle Incident PC
>    continuity otherwise intact). Content-authoring under DEC-077.A; flagged.
> 3. **Reaction (DEC-132/132.A/132.B):** Rowan's `reaction:vigilant` grants one category of
>    out-of-turn reaction — an *ally-targeted trigger* (a tracked ally becomes the object of a
>    hostile Effect). Resolved as a full S-1 exchange (Cost, Overflow, Failure XP standard).
>    Uncapped (DEC-132.A R3); this module exercises it exactly once (Scene 6, Round 1).

---

## Scene 1 — The Goblin on the Road

Framing: Rowan, a young fighter of no renown, is warned by the village that a goblin thief
preys on the Old Road below the hills. A short walk confirms it. Speed order: **Rowan 166 →
Goblin 128**. Budget: **max 6 rounds**.

**End conditions (A3/D5 — budget-expiry withdrawal is the intended primary end):** Round 6
expiry → the Goblin **withdraws** (the 1983 source's plot beat: it flees once hurt — narrated,
**not** a morale rule; the corpus defines no morale/flee threshold). **HP≤0 is the secondary
end**: Goblin HP≤0 (incapacitated; DEC-052) → scene ends early; Rowan HP≤0 → per A7,
incapacitated-alive (Ending B pathway if this is the finale, otherwise "the village elder
finds him; the tutorial restarts per the source's teaching note").

A **Perception** test to notice the goblin's poisoned-meat bait is **mandatory** (D6) and is
this module's **fixed-roll teaching beat** (D2): the natural roll is **fixed at 00 (=100)**.
Per canon this is deterministic, not a real d100 draw. It charges **MP** (mss, Mind-domain):

1. **Roll 100** → auto-fail (DEC-001: 100 always fails). **Cost 100 MP** (549→449); no
   Overflow (549 ≥ 100).
2. **Double:** 100 always qualifies as a failed Double (D1 §2.3/§2.4).
3. **Advanced Skill created (DEC-012, §12.1):** failed Skill Tier 1 → **Tier 2**; add one
   attribute not already in the formula → **mps (Wits)**; new Cap = floor((mss 55 + mps 45)/2)
   = **50**; Start = **1** (option (i)). Named skill: **Perception (Advanced), Tier 2,
   mss+mps, Cap 50, Start 1** (Mind-domain lineage, §12.3).
4. **Failure XP 73** (100−27) → Skill Roll Pool cascade (DEC-010): Pool 73 ≥ 27 →
   Perception 28, remainder 46; Pool 46 ≥ 28 → Perception 29, remainder 18; 18 < 29 →
   **18 → General XP**. **Perception 27 → 29.**
5. **Recovery** +47 (floor(MR/2)) → **MP 496**.

> **Teach:** 100 always fails, always qualifies, and always creates an Advanced Skill on a
> qualifying failed Double — for **any** actor (Universal DEC-012, DEC-140). The named skill's
> Cap recomputes from the full attribute set; its lineage keeps the Mind/MP domain.

**Worked example (Round 1):**
| Ex | Actor→Target | Skill | Roll (Margin) | Def roll | Outcome | Effect | Result |
|---|---|---|---:|---:|---|---|---|---|
| 1 | Rowan→Goblin | Attack 29 | 22 (7) | 31 fail | Win | Inflict Injury | Injury 7−0=7. Goblin 421→414 |
| 2 | Goblin→Rowan | Trip 46 (T2) | 30 (16) | 35 fail | Win | Knock Prone | Location: Zero-Step 30→3; Legs (quartile 1–25); parity 3 odd → Left. Shred: T2>T1 → Mag 2→3; no mitigation. **Record: `Left Leg, Tier-3 Prone, -3`** |
| 3 | Rowan stands (free, DEC-082; still acts) | Attack 29 | 15 (14) | 40 fail | Win | Inflict Injury | Injury 14. Goblin 414→400 |

> **Teach:** Skill-Tier shred rewards tier gaps, not raw Skill value — Trip (46) beats Defense
> (27) by the T2-vs-T1 shred regardless of numbers. Prone = Condition record, separate from HP.

**Worked 100-Fumble (Goblin side, universal):** if the Goblin's Crude Attack rolls exactly
100, it auto-fails (DEC-001, unconditional) and, being a qualifying failed Double, creates an
**Advanced Skill for the creature too** (Universal DEC-012, DEC-140). Example: Creep Attack —
failed Crude Attack (T1 bpp) → Tier 2, add **bps**: Cap = floor((bpp 40 + bps 38)/2) = **39**,
Start = **1** (option (i)). The module does not force this roll; it is shown as the universal
symmetric branch. (The Row-side Advanced-Skill half is exercised deterministically in the
Perception teaching beat above, per DEC-140.)

**Worked Overflow:** with Goblin PE 40 and a Trip roll of 95 → Cost 95; shortfall 55 →
self-inflicted HP damage to the **roller**, win or lose: Goblin PE→0, HP 421−55=366 (DEC-007).

**Advanced Skill (elsewhere probabilistic, A6):** outside the Scene-1 Perception teaching
beat, the module never forces a failed Double. If Rowan's Attack exceeds its skill and rolls a
qualifying failed Double (33, 44, 55, 66, 77, 88, 99, or 100), create **Power Strike
T2 bpp+bps cap55** (worked example in the Bargle Incident; Start = rolled value, capped);
**or** the execution may instead resolve the module's named-skill precedent:
**Perception (Advanced) T2 mss+mps cap50 Start 1**, already created in Scene 1.

> **Zero-Step (verbatim, Canonical §14.1 — D3):** "Zero-Step derives the Location Index by
> exchanging the tens and units digits of the attacker's natural d100 roll. Interpret `00` as
> `100` under the normal d100 rule after the exchange." Canonical examples: 37→73, 10→1, 1→10,
> 100→100. The Q2/Q3 module examples conform (30→3, 22→22, 9→90); the "exact function is
> undocumented" finding is **retracted — the function is canonical (§14.1)**, and no new ruling
> is required.

---

## Scene 2 — The Rattlesnake's Chamber

A tumbled chamber under the hills holds a coiled ten-foot rattlesnake over a small wooden
footlocker. Speed order: **Snake 173 → Rowan 166** (the foe acts first — a first for the
tutorial). Budget: **max 5 rounds**. End: snake HP≤0 (killed/driven off), or Round 5 expiry →
it slithers into a crevice (source beat; it abandons the lair once hurt).

**Worked example (Snake acts first):** Venomous Bite 59 vs Defense 27 — snake roll 22 (M37),
Rowan roll 51 (fail) → snake wins. Declared Effect (A8): **Impose Condition: Wounded**
(T1 coarse, DEC-113). Location: Zero-Step 22→22; **Legs** (quartile 1–25); parity 2 even →
Right. Shred: T2>T1 → Mag 3; no mitigation. Target (DEC-102): snake is a creature → Body
attribute wound from {bsp, bss}; random → **bss (Reflexes)** 55−3=52. **Live recalc
(DEC-004):** bss is Body → HP 615→612; Defense is bss-based → Cap 55→52 (current Skill 27
stays under Cap; an above-Cap state is unruled — R1 Finding 1 — flagged). Poison is
**flavored**, not a ruled Effect — flagged.

**Treasure Search (charges MP):** Perception 29, roll 45 → fail; Cost 45 MP (496→451);
Failure XP 16 → Pool 16 < 29 → 16 → General XP. Recovery +47 → 498. One retry allowed
(default: yes). On ≤29: finds a purse of electrum (≈20 sp value; value = GM discretion) and,
**on that search only**, a lustrous white pearl. The pearl matters only in Ending B
(source fidelity — Bargle misses it).

---

## Scene 3 — Aleena (S-11 Healing)

In the next cavern, a young cleric in white-and-gold vestments (Aleena) prays amid spotty
moss-light. She joins Rowan and offers to mend him. If Rowan was unharmed at Scene 2's end,
she is declined (no test — deterministic branch). Otherwise: S-11 **Extended Test** (DEC-073),
Devotion 32, H2 target **40**, per A5.

**Locked interval accounting (H7), full transaction shown (interval 1 of 4):**
1. Roll 12 vs effective 32 → success. 2. Cost = 12 MP (624→612). 3. Overflow: none.
5. Margin 20 → total 20. 7. Recovery +57 (floor(115/2)) → 668, clamped at 624.
| Int | Roll | Outcome | Margin | Total | MP net |
|---|---:|---|---:|---:|---:|
| 1 | 12 | ✓ | 20 | 20 | −12 +57 |
| 2 | 25 | ✓ | 7 | 27 | −25 +57 |
| 3 | 41 | ✗ neutral (DEC-068) | 0 | 27 | −41 +57 |
| 4 | 8 | ✓ | 24 | **51 ≥ 40** | −8 +57 |
Restore **HP = 51, clamped at current max (H1(a), HC-1.2)** — e.g., Rowan 420→471 (or to 612
if the Scene 2 bss Wound lowered his max; the clamp uses the **current** max, post-Wound).

> **Targeted penalty (DEC-072.A):** a Wound penalizes Aleena's heal **only** if its record
> names Devotion or mee. Her mpp/mps Wound (Scene 6) does not — her heal proceeds unpenalized.

---

## Scene 4 — The Ghoul Passage

A narrow, reeking passage opens onto a wide hall where **three ghouls** stand swaying. Aleena
raises her holy symbol. **The turning** = S-1: **Devotion 32 vs Desecration 22** (single
contest; the pack is opposed by the leader ghoul's Desecration).

**Success (default expectation):** Aleena wins (e.g., roll 18, M14 vs roll 40, fail) → the
ghouls shrink back, scrabbling down the far tunnel. Party passes. **No morale rule exists** —
the withdrawal is the source plot beat narrated as the declared outcome of the contest, flagged.

**Failure (worked branch):** the ghouls lunge. **Fight budget: 3 rounds**, Speed Rowan 166 →
Ghoul 146 → Aleena 133. End: ghouls HP≤0 (incapacitated/driven) or Round 3 expiry → the pack
breaks at the tunnel mouth, letting the party slip past. Effects available on wins: Claw (T2)
and Grapple (T2, Prone); a Body Wound from Claw recalculates HP (DEC-004) — never "cosmetic."

---

## Scene 5 — The Locked Door

An iron-bound oak door, locked, blocks the way to the voices Rowan can hear beyond. Three
approaches (module default for unattended runs: **bash**). This is a **passive-gate test**:
roll d100; **success = roll ≤ effective Skill − hardiness (15)**.

| Approach | Skill | Effective | Pass on ≤ |
|---|---:|---:|---:|
| Bash (smash with your weapon) | Attack 29 | 14 | 14 |
| Pick (improvised: wedge + dagger) | raw mpp 42 | 27 | 27 |
| Find a way around | Perception 29 | 14 | 14 |

Default: **bash**, up to 3 attempts (repeat test). Worked fail: roll 40 → Cost 40 PE;
Failure XP 11 → Pool 11 < 29 → General XP; retry roll 11 → pass. After 3 fails: forced open
by exhaustion (narrated); the party proceeds weary (GM discretion: leave normal HP/PE or take
the 11-point PE deficit).

> **Teach (DEC-041):** bash is Tier-1 → the Skill-Tier ≥2 production gate does **not** fire →
> no Location Index, no Wound — exactly the gate, exactly the lesson.

---

## Scene 6 — The Black-Robed Mage (Two Endings)

The door opens on a lantern-lit chamber. A goblin crouches, being berated by a tall
black-robed man — **Bargle**. Retreat is impossible (the ghoul-hall behind refills with
shadows — narrated; the tutorial forbids retreat by beat design, not by a rule). Bargle snarls
a word and his shape flickers (invisibility: **no mechanical surprise advantage in Tiwas —
an ambush is not a mechanic — flagged**). Initiative: **Rowan 166 → Aleena 133 → Bargle 124**.

**Budget: 3 rounds + the climax fork.** Attrition can end the scene early (Bargle HP≤0 in any
round → Ending A, fork skipped — D1); otherwise **the fork, not attrition, decides the ending**.
HP pools (452 / 615 / 566) are too large for a 3-round knockout by typical margins; that is
deliberate (collation §4 pacing).

### Round 1 (worked example)
- **Triggering exchange:** Bargle Bolt (66) → Aleena Defense (23). Bargle roll 9 (M57),
  Aleena roll 88 (fail). Cost 88 MP (624→536); Overflow none; Failure XP 65 → cascade:
  Pool 65 ≥ 23 → Defense 24, Pool 42 ≥ 24 → Defense 25, Pool 18 → 18 → General XP.
  Declared Effect: **Impose Condition: Wounded** (A8). Location: Zero-Step 9→90 → Head
  (76–100); parity 0 even → **Right**. Shred: T2>T1 → Mag 3. Target (creature): Mind attribute
  from {mpp, mps} → random → **mps (Wits)** 48−3=45 → **MP max 624→621** (recalc; **HP
  unchanged — a Mind Wound correctly steps only MP**). Recovery +57 → **593**, clamped at 621.
- **Reaction (the module's single DEC-132.B exercise):** Rowan's `reaction:vigilant` /
  ally-targeted trigger fires the moment Bargle's hostile Effect lands on Aleena: S-1 Rowan
  **Attack 29** vs Bargle Defense 23 — Rowan roll 21 (M8), Bargle roll 44 (fail) → Rowan wins
  → **Inflict Injury 8** → Bargle 452→444. Cost 21 PE (170→149); full exchange (cost,
  overflow, Failure XP), out-of-turn, uncapped (DEC-132.A R3). Resolved **once**.
- **Rowan's own turn (Round 1):** Attack 29 vs Defense 23 — e.g., Margin total → Injury 10–40.
- **Aleena's turn:** Smite 27 vs Defense 23.

### Rounds 2–3
Prescribed rotation: Round 2 winner declares **Inflict Injury**; Round 3 winner declares
**Armor Bypass** — if the assaulted location carries no `defense:armor` garment (a head/legs
hit on Rowan past his Leather Armor, or any hit on Vestments/Robes), it degrades to the
DEC-030 fail-and-fall-back (the instructive case here); a torso hit on Rowan would exercise
the full DEC-136/137 path — flagged, not forced. Track HP; typical totals take **Bargle to
≈380–420**. **If Bargle reaches HP≤0 in any round → ENDING A immediately; the climax fork is
SKIPPED (D1)** — Bargle is down, the party prevails by attrition, and no Beguile/Composure
contest is resolved. Otherwise, after Round 3, proceed to the **climax fork**.

### The Climax Fork (the tutorial's "saving throw")
Bargle raises his wand — a domination hex (the 1983 charm spell; **charm is not a ruled
Effect** — represented here, flagged) locks onto Rowan. **S-1: Beguile 27 vs Composure 23.**
Ties: reroll up to 3×; a final tie → Ending A (defense holds). Determined only by this roll.

### Ending A — The Hero Shrugs It Off (Bargle defeated)
Rowan resists (e.g., Beguile roll 30 fail, M0 vs Composure roll 12, M11). Aleena, reeling but
alive, drives Bargle's wand arm wide; Rowan's next strike is the closing note: **decisive
exchange — Attack/Power Strike vs Defense 23**. On a success, Bargle is recorded at HP ≤ 0
(forced incapacitation, DEC-052); if the exchange's contest-delta does not itself reach his
remaining HP, the module's Ending-A closure beat absorbs the residual as the mage's collapse
(a module script, not a rule — flagged). Capture or kit per the table. On a failed decisive
roll, Bargle claps a hand to the gash and steps into shadow, escaping wounded — still Ending A
(cast out of the county for now; the road ambuscade of the Bargle Incident module awaits
another day). Treasure: Bargle's pouch (gems, a sealed potion, a rolled scroll — values GM
discretion; the pearl stays with Rowan). Aleena is carried out, furious but alive.

### Ending B — The Hex Bites (Bargle escapes)
The hex holds: Rowan's hand lowers the sword; laughing, Bargle directs the cowed goblin to
strip the pair — the electrum purse goes, **but the pearl winks unnoticed in the dust**
(source-fidelity beat, if it was found in Scene 2). Bargle departs into the dark, his name
louder than ever. The wake finds Rowan at the cave mouth, Aleena conscious and pale, binding
his arm. They return to the village with the truth and a grudge. **Aleena survives. Neither
dies.**

---

## Aftermath

Any ending: S-11 Devotion healing (A5) restores HP = accumulated Margin, current-max clamped.
Wound records step down one Tier per qualifying Skill Test (Effect Heal System,
DEC-035.A cl.5 / DEC-121) — healing HP and healing Wounds are **different actions** against
**different records** (Bargle Incident teaching retained).

---

## GM Coverage Checklist — What This Module Exercised

| Mechanic | DEC(s) | Where |
|---|---|---|
| Core Test, Cost=Roll, Overflow→HP | 006/007 | Sc.1 (Overflow worked), Sc.2 |
| 100-Fumble (universal, DEC-140) | 001/012/140 | Sc.1 Perception teaching beat (fixed roll 00=100, deterministic); Goblin-side worked example |
| Failure XP + Skill Roll Pool cascade | 009/010 | Sc.1 Perception beat (73 → 27→28→29), Sc.3 Aleena Defense |
| Advanced Skill — deterministic named skill | 012/140 | Sc.1 Perception (Advanced) T2 mss+mps cap50 Start 1 |
| Advanced Skill — probabilistic | 012 | Sc.1 (Power Strike, optional; never forced) |
| Recovery + clamping | 008 | Sc.1–3 |
| S-1 opposed contest / melee exchange | 013/105 | All combat scenes |
| Contest-delta Inflict Injury | 096/097/104 | Sc.1, Sc.6 |
| Skill-Tier shred + de-escalation | 103 | Sc.1 (Prone), Sc.2, Sc.6 Wound |
| Zero-Step Location Index / parity | 014/100/041 | Sc.1, Sc.2, Sc.6 |
| Skill-Tier ≥2 production gate | 041 | Sc.1 (Trip), Sc.5 (non-fire, taught) |
| Wound record + DEC-102 target selection | 035.A/102 | Sc.2 (bss), Sc.6 (mps) |
| Live attribute recalc (incl. HP step) | 004 | Sc.2 (HP 615→612), Sc.6 (MP 624→621) |
| Conditions (Prone) | 079/122–125 | Sc.1 |
| Reactions (single tagged exercise) | 132/132.A/132.B | Sc.6 R1 (reaction:vigilant) |
| Tag+Location gating / fallback | 028/114/030 | Sc.6 R3 Armor Bypass fallback |
| Morale/surprise non-mechanics (flagged) | — | Sc.1/4/6 withdrawals narrated |
| GM Fiat (bounded, declared) | 130 | Available; not required |
| S-11 Extended Test (full H7 order) | 071–074 | Sc.3 (A5 conventions) |
| Speed-based turn order | 095 | Every scene (Snake 173 acts first, Sc.2) |
| Creature signature full-Cap starts | 086/087 | All creatures |

**Not exercised (flagged, not invented):** Active Defense as a distinct genuine Core Test
(DEC-044); Fatigue from repeated defenses (DEC-135 — never 2+ active defenses in a sequence
here); full Tag-matched Armor Bypass resolution (DEC-136/137/138/139 — R3 falls back by
design); Encumbrance (DEC-078); Equipment damage/repair (DEC-118–129); a magic subsystem,
or charm, poison, and morale as ruled Effects (each represented by a flagged ruled-equivalent).
Honest-gap-flagged per the Bargle Incident precedent.

---

**End of module.**