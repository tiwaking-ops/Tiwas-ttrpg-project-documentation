# TIWAS — Copilot Runner Packet v0.2 (2026-09-14)

**Document class:** Compilation for upload. Advisory / Non-canonical. No DEC
assigned. No rule invented, amended, promoted, or superseded. This file
concatenates three existing repository documents verbatim (Parts 1–3) under a
runner header (Part 0). Compiler: OpenCode/big-pickle. Purpose: single-document
upload so the executing LLM treats the complete operational ruleset as an
uploaded document.

**Upload instruction for the human:** upload THIS file (and only this file is
required) to the runner's project files, then say "Run PASS 1 now."

---

## PART 0 — RUNNER PROTOCOL (normative for this run)

**Role.** You are the execution resolver. You apply the ruleset in Parts 1–3
mechanically. You generate no randomness: every d100 is supplied in the ROLL
STREAM below. This requires zero invention.

**Two passes, tables only, minimal prose.**
- PASS 1 (first reply): frontmatter + initial-state table + Scene 1 (6-round
  budget, Rowan Attack / Goblin Trip, A1/A2) + Scene 2 (5-round budget, snake
  acts first, Venomous Bite vs Defense as S-1 opposed) + Scene 3 (S-11
  healing: 4 intervals, Devotion 32, H2 target 40, H1(a) clamp, H7 order).
  End with "PASS 1 DONE, consumed through #NNN".
- PASS 2 (second reply, when asked): Scene 4 (Turning Devotion vs
  Desecration; fail → 3-round fallback combat) + Scene 5 (three Bash attempts,
  Attack−15, Tier-1, no production gate) + Scene 6 (3-round budget + D1 fork)
  + final states + coverage matrix + compliance check + findings + 3-line
  summary + flagged guesses.

**Ledger-first rule.** Emit the mapped d100 line BEFORE its outcome sentence,
every exchange (e.g. "Sc1-R1 Rowan Attack vs 29: #001=80"). Any outcome
without a preceding mapped roll is void. Consume the stream strictly in order;
cite each index. If the stream runs out, STOP at that exchange and report
rolls consumed — never continue with unlisted numbers.

**Sealed initial states (module v0.2 verbatim).**
Rowan HP 615 / PE 170 / MP 549, Speed 166, Attack 29, Defense 27, Perception
27, Composure 23. Aleena HP 566 / PE 159 / MP 624, Devotion 32. Goblin 421 /
102 / 273. Rattlesnake 417 / 71 / 243. Ghoul 494 / 126 / 260. Bargle 452 /
105 / 680.

**Fixed teaching beat (not streamed, not rolled).** Scene-1 Perception: cost
100 MP (549→449), Failure XP 73, cascade 27→28→29, +18 General XP, Recovery
+47 (→496), creates Perception (Advanced) T2. Cost 100 never exceeds MP 549:
Overflow is 0.

**Formulas (apply literally, show arithmetic).** Success iff roll ≤ skill.
Margin = skill − roll (success) / roll − skill (fail margin). Cost = natural
roll, charged to PE (Body/combat) or MP (Mind/Perception). Overflow = max(0,
Cost − paying pool) → HP. Failure XP = fail margin; every 50 XP raises the
skill by 1, remainder to General XP. Recovery = floor(ER/2) to PE or
floor(MR/2) to MP immediately post-Cost. Sealed regen values: Rowan +56 PE /
+47 MP; Aleena +50 PE / +57 MP. S-1 opposed: both roll, higher margin wins;
tie → both reroll (max 3), then defense holds. Winner declares EXACTLY ONE
Effect (D4). Scene ends at round-budget expiry (withdrawal beat, primary/D5)
or any combatant at HP≤0 (terminal; negative persists). Aleena never ends a
scene at HP≤0 — clamp to 1 and narrate collapse (A4). Bargle at HP≤0 before
the climax fork → Ending A immediately, fork SKIPPED (D1).

**Designer rulings applied (D1–D7, 2026-09-14).** D1: attrition-first Ending
A. D2/D6: Scene-1 Perception beat mandatory, fixed roll 00 (=100). D3:
Zero-Step is Canonical §14.1 verbatim. D4: exclusive one-Effect-per-win. D5:
budget-expiry withdrawal is the intended primary scene end. D7: module and
harness v0.2 reviewed and accepted (review gate closed).

**Frontmatter for the report (exact).** version 2.0; author_llm Copilot;
created_date 2026-09-14; source module v0.2; ruleset "Canonical Rules v1.4 +
Decision Register through DEC-140"; status "Execution record /
Advisory-non-canonical. No DEC assigned." Self-check line: "(a) no sentence
copied from any prior report; (b) all rolls from the stream below; (c)
version 2.0 dated 2026-09-14."

**Hard bans.** No DEC assigned or inferred. No rule invention. No module or
harness edits. No promotion, demotion, or supersession language. No narrated
morale, poison, or surprise as mechanics.

**ROLL STREAM (fresh SystemRandom entropy, generated 2026-09-14 for this run;
consume in order starting #001).**
#001–#050: 80 36 31 23 13 76 27 8 51 94 43 93 84 45 75 24 40 86 98 50 28 94 29 25 83 93 82 10 15 76 13 39 96 16 26 11 55 54 68 18 24 29 17 60 87 22 46 69 97 83
#051–#100: 96 45 23 31 11 2 21 8 4 7 5 12 70 81 59 26 94 82 74 2 67 35 54 26 22 8 7 57 55 4 22 76 23 54 45 39 62 67 66 14 46 5 80 1 48 82 98 44 10 56
#101–#150: 94 92 72 77 76 36 31 37 59 26 43 97 90 57 62 46 3 52 23 65 91 70 64 20 51 20 45 69 36 71 26 51 100 82 67 50 19 81 17 75 8 12 25 43 3 45 41 48 44 75
#151–#200: 17 97 15 42 41 72 7 52 69 41 97 46 94 45 99 33 92 14 60 45 89 44 72 36 57 53 49 65 82 28 38 15 56 99 11 87 31 38 91 45 18 42 7 43 56 40 43 50 55 48

**Stream-discipline ruling (already in effect).** Rolls #001 (80), #002 (36),
#003 (31) were consumed by the earlier partial attempt and VERIFIED against
this stream. They stay spent. This run continues consumption from #004. (If
you instead restart consumption from #001, state so explicitly and re-verify
each line against the stream above.)

---

## PART 1 — ADVENTURE MODULE v0.2 (verbatim; begins next line)
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

---

## PART 2 — HARNESS PROMPT v0.2 (verbatim; begins next line)

---
document:
  title: "Tiwas — Your First Adventure: Unattended Multi-LLM Playtest Harness Prompt (Ready-to-Fire)"
  version: "0.2"
  status: "Advisory / Non-canonical. No DEC assigned. Execution harness for automated playtest runs of tiwas-adventure-your-first-adventure-2026-09-14.md (v0.2); not a ruling, not a register action."
  purpose: >
    One copy-paste prompt that operationalizes the module (v0.2) for unattended execution by
    multiple LLMs (Claude Sonnet 5, GPT-5.6 Luna, Grok 4.5) under the Automated Playtest
    Run Conventions (H1–H8, HC-1.1–1.4, DEC-072.A) plus the module's A1–A8 conventions.
    v0.2 applies Tiwa rulings D1–D7 (2026-09-14) and DEC-140.
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  source_module: "tiwas-adventure-your-first-adventure-2026-09-14.md"
  conventions: "tiwas-automated-playtest-run-conventions-2026-09-14.md"
  precedent: "tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md"
revision_note: >
  v0.2 (2026-09-14): applies Tiwa rulings D1–D7 and DEC-140 — D1 (Bargle HP≤0 in any Scene-6
  round → Ending A immediately, climax fork SKIPPED; resolves the R2 Luna BLOCKED outcome);
  D2/D6 (Scene-1 Perception test mandatory fixed-roll 00 (=100) teaching beat creating the
  named Advanced Skill Perception (Advanced) T2 mss+mps cap50 Start 1); D3 (Zero-Step quoted
  verbatim from Canonical §14.1; zone correction LI 30/LI 42 → Torso per DEC-100 quartiles;
  no rule gap); D4 (exclusive — exactly one Effect per winning exchange); D5 (budget-expiry
  withdrawal = intended primary scene end); D7 (rewrite; no re-run until Tiwa reviews).
  Ruleset cutoff advanced DEC-139 → DEC-140.
  **v0.2 text ACCEPTED by Tiwa, 2026-09-14 (in-session): approved for playtest use; the
  document remains Advisory / Non-canonical — acceptance confers no promotion.**
---

# Tiwas — Your First Adventure: Unattended Multi-LLM Playtest Harness Prompt

**This document holds a single ready-to-fire execution prompt.** Each target LLM is an
independent provenance unit; do not merge their numerical results. Each run states its
execution settings (RNG, conventions, ruleset) in its own report.

---

## 0. Governance Statement

- Assigns **no DEC number** and proposes none.
- Runs under this prompt are **advisory / non-canonical execution records**; no report
  produced by this harness triggers a ruling, promotion, demotion, or register action.
- The harness fixes execution conventions (module A1–A8 + H-conventions) for
  cross-comparable unattended runs only. Table play and GM discretion (DEC-070/074) are
  untouched.
- Provenance: authored by OpenCode (`opencode`, `big-pickle`) in a single pass;
  single-model authorship carries no authority.

---

## 1. Target LLMs and Run Logistics

| Run | Target LLM | Expected artifact |
|---|---|---|
| R1 | Claude Sonnet 5 (`claude-sonnet-5`) | `investigations/tiwas-your-first-adventure-playtest-execution-claude-2026-09-14.md` |
| R2 | GPT-5.6 Luna | `investigations/tiwas-your-first-adventure-playtest-execution-luna-2026-09-14.md` |
| R3 | Grok 4.5 (`grok-4.5`) | `investigations/tiwas-your-first-adventure-playtest-execution-grok-2026-09-14.md` |

Each run is exercised independently with the same prompt; logs/rolls CSVs are welcomed but
must be referenced and, if desired, stored beside the report. The module, this harness, and
the conventions file are all inputs a run must not modify.

---

## 2. The Ready-to-Fire Prompt

Copy this block verbatim to each target LLM.

```text
TIWAS — UNATTENDED MULTI-LLM PLAYTEST EXECUTION
TASK: EXECUTE and CERTIFY "Tiwas — Adventure Module: Your First Adventure" (advisory v0.2) end to end.

[A] PRE-INJECTION (execute in this order)
1. Read the module (investigations/tiwas-adventure-your-first-adventure-2026-09-14.md) in full.
2. Ruleset applied — STATE exactly, in your report frontmatter: Canonical Rules v1.4 +
   Decision Register through DEC-140 (incl. DEC-132/132.A/132.B, DEC-135, DEC-136–139,
   DEC-072.A amendment) + Automated Playtest Run Conventions 1.1 (H1–H8, HC-1.1/1.2/1.4)
   + module Run Conventions A1–A8. Cross-version comparisons are valid only within the
   same stated block.
3. Initialize the full 24-attribute stat blocks with the module's derived values verbatim.
   Do not edit, "fix," or reinterpret. RNG: random.SystemRandom() (fresh entropy).
4. Adopt A1–A8. Confirm each in one bullet in your report.

[B] NARRATOR CONTRACT
5. Narrate only what mechanics have resolved; resolution precedes description; never narrate
   a free hit, a "bloodied" threshold, a morale check, charm, poison, or an invisible ambush
   into mechanical advantage. Those are module-flagged: represent them exactly as the module
   does (contested S-1 / declared Wound / narrated beat).
6. When the module gives a worked example, follow the procedure, never the numbers — EXCEPT
   the Scene-1 Perception teaching beat, whose natural roll is FIXED at 00 (=100) by module
   text (D2/D6): execute that fixed roll exactly and create the named Advanced Skill
   Perception (Advanced) T2 mss+mps cap50 Start 1.
7. Every d100 is rolled and logged (fixed-roll teaching beat logged as "fixed 00"). Every
   Outcome, Cost, Overflow, Failure-XP/cascade, and Recovery value appears in your log;
   clamping and live recalculation (DEC-004, incl. the 452→449 and 615→612 and 624→621 steps)
   are shown where triggered.
8. Timestamp the phases. Keep a running character-state line after each exchange.

[C] SAMPLER RULES (determinism contract)
9. Core Test = the 9-step DEC-006 transaction (roll, Cost=natural roll to domain pool,
   Overflow→self-HP, Outcome, Margin, Failure XP → Skill Roll Pool cascade, Recovery,
   completion, restore) in exactly that order (H7). S-1 = margin contest: Margin =
   max(0, skill − roll); higher wins; ties = reroll ≤3 then defense holds.
10. Turn order Speed-desc (DEC-095), ties bss then bsp then reroll. ONE substantive
    exchange per combatant per round (A1). Movement = free/bundled (DEC-082).
11. Effect selection follows A8 rotation and is EXCLUSIVE (D4): exactly ONE declared Effect
    per winning exchange; contest resolves that Effect's magnitude only; NO sequential or
    compound multi-Effect path from a single win. Effects resolve via DEC-103 shred
    (+1 per attacker-Tier over defender-Tier), de-escalation (defender margin), and the
    DEC-100 quartiles + parity for Tier≥2 production. Records in DEC-115/117 schema.
12. Clamp HP restores at current max (HC-1.2) — never above. Sum applicable penalty
    magnitudes (HC-1.1) and apply only per DEC-072.A targeting (named Skill or governing
    Attribute).
13. Aleena-survives invariant (A4): if her resolved HP would cross 0, record the resolved
    outcome, clamp to 1, and narrate collapse. State that you did so if it happens.
14. Scene budgets: Sc.1 ≤6 rds, Sc.2 ≤5 rds (Snake acts first), Sc.4 fallback ≤3 rds,
    Sc.6 ≤3 rds + climax fork. Budget-expiry withdrawal is the PRIMARY end (D5); HP≤0
    (DEC-052, negative persists DEC-108) is the secondary end, whichever occurs first. No
    invented intermediate thresholds.
15. Advanced-Skill forcing is limited to the Scene-1 Perception teaching beat only (D2/D6,
    fixed roll 00): resolve it deterministically. Do NOT force any other failed Double; if one
    occurs naturally on Rowan's Attack, resolve Power Strike per the module's worked example;
    otherwise record "not exercised — probabilistic."

[D] ENDING SELECTION (D1)
16. If Bargle reaches HP≤0 in ANY Scene-6 round → ENDING A immediately; the climax fork is
    SKIPPED; do NOT resolve Beguile vs Composure (Bargle is down — attrition decided the
    scene, no fork). Otherwise, after Scene 6 Round 3, resolve the climax S-1:
    Beguile 27 vs Composure 23. Win → ENDING A (then resolve the decisive exchange);
    Loss → ENDING B. A drawn fork rerolls ≤3; final tie → ENDING A. Continue narration for
    the chosen ending, including treasure and aftermath per module. If Bargle reaches HP≤0
    exactly on the decisive-exchange step of Ending A, record him incapacitated per DEC-052.

[E] GRANULAR EVALUATOR (report contract)
17. Structured report with: (i) frontmatter (document/status advisory-non-canonical;
    provenance: execution_llm, created_date, conventions/ruleset applied, RNG, any
    conventions you altered and why); (ii) initial-state confirmation table;
    (iii) per-scene exchange logs (the C-block fields); (iv) final state per combatant;
    (v) coverage matrix vs the module's GM Coverage Checklist (PASS/PARTIAL/NOT EXERCISED)
    with one-line evidence each — the 100-Fumble and Advanced-Skill rows should go PASS
    (Sc.1 fixed teaching beat); (vi) module-correction compliance check (Perception
    domains charged MP; Body-Wound HP recalcs shown; no "cosmetic" Wound claim;
    Zero-Step per Canonical §14.1 verbatim); (vii) findings (open items for Tiwa only —
    never resolved by you); (viii) artifact-class: advisory/non-canonical, no DEC assigned.
18. Hard boundaries: no DEC inference, no promotion/demotion/supersession, no invented
    rules, no rule-edit anywhere, no edits to the module file; corrections and open items
    are reported, never silently applied. Treat your run as its own provenance unit.
19. Delivery: report artifact
    investigations/tiwas-your-first-adventure-playtest-execution-<model>-2026-09-14.md
    (+ rolls/effects logs if scripts used). Do not overwrite other runs' artifacts.
    Reply with (a) the report, (b) your 3-line executive summary, (c) any flagged guesses.
```

---

## 3. Usage Notes

- **Compare only within the stated block:** healing amounts and HP trajectories are
  comparable between runs only when both state Conventions 1.1 + A1–A8 and the same ruleset
  cutoff (through DEC-140).
- **Divergence is expected** (roll variance, probabilistic A6 branch, random DEC-102 target
  selection). The harness's purpose is to make the *procedure* identical so divergence is
  attributable to rolls, not interpretation — the collation (§4) failure mode this fixes.
- **Post-run collation:** a follow-up collation comparing the three execution reports should
  mirror `tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md`
  (convergent findings, divergent findings → Tiwa escalation, factual-discrepancy list).
- **Baseline note (§10 of conventions):** if any run alters an execution-level setting, it
  must state so in frontmatter (RNG, action economy, H-convention reuse) or the result is
  not cross-comparable.

---

**End of document.**

---

## PART 3 — AUTOMATED PLAYTEST RUN CONVENTIONS (verbatim; begins next line)

---
document:
  title: "Tiwas — Automated Playtest Run Conventions"
  version: "1.1"
  status: "Advisory / Non-canonical. No DEC assigned. Records a single designer-approved conventions block (H-rule set) scoped to automated playtests only. HC-1.1/1.2/1.4 confirmed 2026-09-14; HC-1.3(b) DEC-072.A amendment applied to register 2026-09-14."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  rulings:
    - "Tiwa (human), 2026-09-14 — H1(a) HP = accumulated Margin (adopted); H2–H8 approved; H4 Option 2 (targeted penalty) ruled"
    - "Tiwa (human), 2026-09-14 — HC-1.1 (sum all applicable penalty magnitudes), HC-1.2 (clamp at current HP max), HC-1.4 (filing location) confirmed; HC-1.3(b) approved (draft DEC-072 amendment text)"
  source_module: "tiwas-adventure-the-bargle-incident-2026-09-13.md"
  collation_report: "tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md"
---

# Tiwas — Automated Playtest Run Conventions

**Prepared by (Author):** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Document class:** Advisory conventions block for unattended/automated playtest executions. Records designer-approved (H1–H8) conventions. Not a proposal, not a Decision Record, not a canonical or non-canonical rule change.

---

## 0. Governance Statement

This document records a single, consolidated block of conventions — labelled the **"Automated Playtest Run Conventions"** — adopted by Tiwa (human, sole ruling authority) on 2026-09-14, following the cross-LLM collation of three playtest executions of **The Bargle Incident** (`tiwas-adventure-the-bargle-incident-2026-09-13.md`; see `tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md`).

This document:

- Assigns **no DEC number** and proposes none.
- Is **scoped to automated/unattended playtest runs only**. It does **not** alter tabletop/GM-discretion play, DEC-070 (GM-discretion completion target), DEC-074 (no HP-deficit lock), or any other table rule.
- Promotes **nothing**; no authority change is requested or implied.
- Records **HC-1 as confirmed 2026-09-14:** HC-1.1 (sum all applicable penalty magnitudes), HC-1.2 (clamp at current HP max), and HC-1.4 (filing location) are ruled; HC-1.3(b) approved (draft the DEC-072 amendment text — register application happens only after Tiwa approves the wording).
- References but does **not** implement the **DEC-072 clarifying amendment** (blanket → targeted penalty wording), which is a separate register action requiring Tiwa's explicit direction (see §6 and §8).

**Provenance note per `governance/provenance.md`:** this document was authored, assessed, and last-modified by the same model (OpenCode `big-pickle`) in a single pass. A single-model self-assessment is a weaker form of review than an independent second pass; it is recorded honestly as such and confers no authority. The rulings recorded here are Tiwa's human decisions, not LLM decisions.

---

## 1. Purpose and Scope

Three independent playtests (R1 Claude Sonnet 5, R2 GPT-5.6 Luna, R3 Grok 4.5) operationalized the same open S-11 boundary (DEC-074 GM-discretion healing amount) in three different ways as unattended simulations. To make automated-run results deterministic and cross-comparable, this block fixes the conventions an automated run must follow. It applies **only** where no GM is present to adjudicate; it never overrides a GM-discretion decision in a human-run game.

| Convention | Applied to |
|---|---|
| H1–H8 (this block) | Automated playtest executions of Tiwas adventure modules (primary reference: The Bargle Incident) |
| Tabletop / GM-run play | Excluded — DEC-070 / DEC-074 GM discretion governs |

---

## 2. Authority Record

| ID | Ruling / approval | Authority | Date |
|---|---|---|---|
| H1(a) | Automated rest heal: **HP restored = accumulated Margin**, capped at current HP max | Tiwa (adopted) | 2026-09-14 |
| H2 | Completion target = **fixed 40 Margin** (adjustable per playtest) | Tiwa | 2026-09-14 |
| H3 | Healing skill = **module-designated only** (Devotion here); **MP-domain cost = natural roll**; **HP-only restore**; **cost ≠ restore** | Tiwa | 2026-09-14 |
| H4 | **Targeted penalty** — Wound/Effect penalizes healing only if it names the healing skill or its governing attribute; DEC-072 needs a clarifying amendment | Tiwa | 2026-09-14 |
| H5 | **Wound-record healing excluded** from automated scope initially (Wounds/Effects must be actively healed/removed) | Tiwa | 2026-09-14 |
| H6 | **Revival / negative HP: terminal** for this playtest | Tiwa | 2026-09-14 |
| H7 | **Lock the interval accounting order** (module's sequence, §7) | Tiwa | 2026-09-14 |
| H8 | **Record as a single "Automated Playtest Run Conventions" block** | Tiwa | 2026-09-14 |
| HC-1.1 | Multiple applicable Wound/Effect penalty magnitudes on a healing test | **Sum all magnitudes.** Effect Tier = difficulty of healing/removing; Magnitude = the numerical effect amount | Tiwa | 2026-09-14 |
| HC-1.2 | H1(a) restore clamp | **Clamped at current HP max** — cannot heal above a character's maximum HP | Tiwa | 2026-09-14 |
| HC-1.3 | DEC-072 amendment | **Option (b)** — amendment drafted (§12), approved by Tiwa, applied to the register as **DEC-072.A** | Tiwa | 2026-09-14 |
| HC-1.4 | Filing location | **Standalone advisory document in `investigations/`** (this file) + register advisory annotation (applied with the DEC-072.A update, after wording approval) | Tiwa | 2026-09-14 |

All entries are **non-canonical ruling/approval records**, consistent with the repository's Ruled (Non-canonical designer ruling) register convention. Nothing in this table is canonical and nothing is promoted.

---

## 3. H1(a) — Automated Healing Amount

During an automated playtest Rest/interlude (an S-11 Extended Test instance per DEC-073), when the completion target is reached:

> **HP restored = accumulated Margin (sum of successful intervals' Margin), capped at current HP max.**

- The cap uses the **current** HP max (post-Wound live recalculation per DEC-004/DEC-102).
- Restoration is **HP-only**; MP/PE recovery remains with the Recovery mechanic (DEC-008), never with healing.
- Restoration does **not** heal Wounds or Effects (see H5 — wound-record healing is out of automated scope initially).

**Note:** this is a *playtest-run convention*, adopted for unattended determinism. It is **not** a ruling that the tabletop GM must restore Margin-for-Margin; DEC-074 GM discretion is untouched at the table.

---

## 4. H2 — Completion Target

- **Default: fixed 40 accumulated Margin.**
- The value 40 is the module's own worked-example target and was demonstrated end-to-end (R1 completed at Margin 43 in 8 intervals; worked example completes at 51).
- It is **adjustable per playtest** — a convention constant, not a formula and not tied to HP deficit (respects DEC-074's no-HP-deficit-lock intent, and DEC-070's "no fixed default" applies to table play, not to this automated convention).

---

## 5. H3 — Healing Skill, Cost, and Restored Pool

| Item | Convention | Rationale / evidence |
|---|---|---|
| **Skill** | Module-designated healing skill only (here: **Devotion**, Skill 32 start). Extendable to "any skill the module explicitly designates as healing" in future modules | Deterministic skill selection for unattended runs |
| **Cost** | One ordinary Core Test per interval (DEC-071/DEC-073); **cost = the natural d100 roll, in the skill's resource domain = MP** (Devotion is `mee`-Mind-domain; DEC-003/DEC-007) | Module interlude charges MP (12+25+41+8 = 86); Perception precedent routes Mind-domain to MP |
| **Restored pool** | **HP only.** Never MP or PE | Recovery (DEC-008) handles MP/PE |

### 5.1 Confirmed: MP cost ≠ HP restored

Approved as a property of the system, not an anomaly:

- **MP cost** = natural roll per interval, paid every interval (win or lose; DEC-068 failures still cost).
- **HP restored** = accumulated **Margin** over successful intervals, paid once at completion (H1(a)).
- Margin `= effective Skill − roll` is bounded by the skill's value (~32 Devotion start), while a roll can reach 99; the transaction is **lossy by design** (resources consumed during, quality-based restore at end).

| Run | MP spent (sum of rolls) | Margin total → HP restored |
|---|---:|---:|
| Module worked example | 86 | 51 |
| R1 (Claude) | 8 intervals, large rolls | 43 |

---

## 6. H4 — Wounded-Healer Penalty (DEC-072) — Targeted Reading

**Ruling (Tiwa, 2026-09-14):** option 2 — **targeted penalty**:

> A Wound or Effect penalizes healing **only if its record names the healing skill directly or its governing attribute** (e.g., `mee`/Resolve → Devotion). Otherwise the heal is **unaffected**.

**Designer rationale (recorded verbatim):** "The previous wording was created before the creation of the Skill Tier Effect System. Unless the Wound or Effect affects the skill, then Wounds or Effects will never cause a penalty. If a Wound affects a skill, that skill will never be penalized. Wounds or Effects on underlying Attributes will cause a reduction in all related Skills."

Mechanically:

- **Skill-targeted** Wound/Effect → that Skill drops by magnitude Y; the heal uses the reduced Skill.
- **Attribute-targeted** Wound/Effect → the Attribute drops by Y (DEC-035.A/DEC-102 record target; DEC-004 live recalculation); every **related** Skill (formula uses that attribute) drops accordingly.
- **Unrelated** Wound/Effect (e.g., `mpp`/Wits wound vs a `mee`-based heal) → **no healing penalty.** R1/R2's Aleena Wounds are `mpp`-targeted; under the targeted reading they do **not** penalize her Devotion heal.

**DEC-072 clarifying amendment (applied 2026-09-14 as DEC-072.A):** DEC-072's original wording ("Wound magnitude penalizes the healer's EFFECTIVE Skill for the healing test") was blanket and predated the Skill Tier Effect System. Per HC-1.3(b) the amendment text was drafted (§12), approved by Tiwa, and applied to the decision register as **DEC-072.A** on 2026-09-14, implementing the targeted reading below.

---

## 7. H7 — Locked Interval Accounting Order

Each Rest interval is a **full, ordinary 9-step Core Test Transaction** (DEC-006; DEC-071; DEC-073), executed in this exact order:

1. **Roll** d100 against **effective** healing Skill (post-H4 penalties).
2. **Cost** = natural roll, paid from the skill's domain pool (MP).
3. **Overflow check** (DEC-007): if cost > current pool, the shortfall is **self-HP overflow** damage.
4. **Outcome:** success if roll ≤ effective Skill.
5. **On success:** Margin = effective Skill − roll; **add to accumulated total** (DEC-067).
6. **On failure:** Failure XP = max(0, roll − effective Skill) → Skill Roll Pool cascade (DEC-009/DEC-010); **no** Margin added, **no** progress loss (DEC-068).
7. **Recovery** (DEC-008): pool += `floor(Regen/2)` (= 57 for Aleena), clamped at the **current** pool max.
8. **Completion check:** accumulated Margin vs target 40 (H2).
9. **On completion:** apply H1(a) — restore HP = accumulated Margin, capped at current HP max. Intervals stop.

This is a restatement of the module's interlude worked example in full-transaction form; the module's compressed table lists only cost + recovery, which is why the sequence is written out for automation.

---

## 8. HC-1 — Confirmed Entries (2026-09-14)

All four HC-1 items are resolved by Tiwa:

| # | Item | Ruling |
|---|---|---|
| HC-1.1 | Multiple applicable Wounds/Effects on the healer — penalty accumulation | **Sum all applicable magnitudes.** Designer rationale: Effect Tier is the difficulty of healing/removing the effect; Magnitude is the numerical effect amount (magnitudes sum for the effective-Skill penalty) |
| HC-1.2 | H1(a) restore cap | **Clamped at current HP max** — cannot heal above a character's maximum HP |
| HC-1.3 | DEC-072 amendment | **Option (b)** — drafted (§12), approved by Tiwa, and **applied to the register as DEC-072.A** (2026-09-14); DEC-072's status now reads `Ruled (amended by DEC-072.A)` |
| HC-1.4 | Filing location | **Agreed: standalone advisory document in `investigations/`** (this file), cross-referenced as an advisory storage annotation in the decision register (applied with DEC-072.A once wording is approved) |

---

## 9. Adopted-but-Out-of-Scope Conventions

- **H5 — Wound-record healing:** the automated Extended Test never heals Wounds or removes Effects during this playtest. Wounds and Effects must be **actively healed or removed** as a separate, conscious action; they are out of the automated-rest scope initially.
- **H6 — Revival / negative HP:** for this playtest, a combatant at HP ≤ 0 (forced incapacitation per DEC-052; negative-HP persistence per DEC-108) is **terminal** for the automated run. No revival mechanic is exercised, invented, or assumed.

---

## 10. Notes for Future Automated Runs

- **Baseline for comparisons:** future automated runs should state their convention version ("Automated Playtest Run Conventions 1.0") and their execution-level settings (RNG, action-economy reading of DEC-106, and reuse/alteration of H1–H8). Healing amounts are comparable between runs **only** when both use H1(a).
- **Module corrections:** carry the module-side flags already raised in the storage assessment and collation (Scene 1 PE→MP domain error; Bargle "cosmetic" bps Wound; Power Strike Cap 55-vs-59; R1 `initial_state` snapshot semantics). Do not silently patch these in a stored run record.
- **Re-run baseline:** **R1** (Claude) is the current adopt-as-reference interlude execution under H1(a). Re-running the interlude with the locked conventions (H1(a)+H2+H7) is an open follow-up; not required for this document.

---

## 11. OpenCode Action Boundary

1. Store this document as an **advisory / non-canonical investigation artifact**.
2. Do **not** infer, assign, or request a DEC.
3. Do **not** promote or demote anything on the basis of this document.
4. **DONE (2026-09-14):** DEC-072.A applied to the decision register and the advisory storage annotation added per HC-1.4, after Tiwa approved the §12 wording.
5. Convention text is fully locked per the HC-1 confirmations recorded in §2 and §8.

---

## 12. DEC-072.A — Wound/Effect Healing Penalty: Targeted Reading (Amendment to DEC-072)

Drafted per HC-1.3(b) and **applied to the decision register as DEC-072.A on 2026-09-14** following Tiwa's approval. DEC-072's Status column reads `Ruled (amended by DEC-072.A)`; DEC-072's original verdict text is preserved per register amendment convention.

**Proposed register row (matches the `_consolidation/decision-register.md` column format):**

> | DEC-072.A | S11-B — Wound magnitude healing penalty: targeted attribute/skill alignment (**AMENDMENT to DEC-072**) | **RULED — Targeted penalty.** A Wound or Effect penalizes a healing Skill test **only if its record names that Skill directly or its governing Attribute**; otherwise the test is unaffected. A Skill-targeted Wound/Effect reduces that Skill by its magnitude Y. An Attribute-targeted Wound/Effect reduces the Attribute by Y (DEC-035.A/DEC-102 record target; DEC-004 live recalculation) and thereby every related Skill whose formula uses that Attribute. Where multiple applicable records bear on the same test, their magnitudes **sum** — Effect Tier is the difficulty of healing/removing the effect; Magnitude is the numerical effect amount. Supersedes DEC-072's blanket wording ("Wound magnitude penalizes the healer's EFFECTIVE Skill for the healing test"), which predates the Skill Tier Effect System and would otherwise let unrelated Wounds/Effects (records that neither name the healing Skill nor its governing Attribute) penalize the heal. Penalty touches the healer's effective Skill only — never the natural roll, the resource Cost, or the HP amount restored directly (DEC-064 S8-B pattern retained). | Designer ruling (amendment), 2026-09-14 (Tiwa, following the cross-LLM Bargle Incident playtest collation); confirmed by Tiwa to OpenCode | Non-canonical designer ruling (amendment) | Ruled |

**Optional companion note (for Tiwa's awareness, not part of the amendment):** the underlying principle — a Wound/Effect penalizes a test only when its record names that Skill or a governing Attribute — generalizes beyond healing to any Skill test. If Tiwa wants that stated as a general penalty-model rule rather than only within the healing amendment, that is a separate, larger register item to raise separately.

---

**End of document.**

**Author:** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Classification:** Advisory conventions block — Automated Playtest Run Conventions 1.1, No DEC assigned
