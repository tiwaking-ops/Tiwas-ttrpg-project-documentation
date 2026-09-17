---
document:
  title: "Tiwas — Adventure Module: Mentzer D&D Red Box Solo Adaptation (2026-09-17)"
  version: "1.1"
  status: "NON-CANONICAL — advisory playtest scenario only. Makes no rulings, assigns no DEC, promotes nothing. Every adventure beat is a reconstruction from general knowledge, never quoted source text."
provenance:
  author_llm: {name: "opencode", version: "unknown / not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "Muse Spark", version: "unknown / not established"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
revision_note: >
  v1.1 (Muse Spark, 2026-09-17): trims v1.0 to the 250–350-line module band;
  adds explicit per-beat dependency classifications, DEC-077.A scope-extension
  flag (workflow is GURPS-BToV-scoped; D&D reuse is analogical), and coverage
  checklist. Author record preserved per governance/provenance.md. Uses
  "tsr01011b - CoreRules - D&D - Basic Rules Boxed Set v2.md" and
  "DnD - Basic Rules Boxed Set Adventure.md" as research sources only.
---

# Tiwas — Mentzer D&D Red Box Solo Adaptation

**NON-CANONICAL advisory module.** Loosely adapted from general knowledge of the
1983 Basic Set introductory solo (character-creation walkthrough, road encounters,
Aleena/Bargle finale). **Aleena survives** — continuity with the 2026-09-13 Bargle
Incident module. Except the Scene-1 Perception teaching beat (**fixed roll 00=100**),
all numbers are worked examples, not scripted outcomes: live rolls diverge.

**Module-side corrections carried (Bargle Incident collation):** Perception (mss,
Mind-domain) charges **MP**, not PE; a Body-attribute Wound live-recalculates HP
downward; healing follows A5/H1(a)–H7.

**Divergence note (required):** shares characters (Aleena, Bargle) — not content —
with `tiwas-tutorial-adventure-aleena-bargle-2026-09-13.md`,
`tiwas-adventure-the-bargle-incident-2026-09-13.md`, and
`tiwas-adventure-your-first-adventure-2026-09-14.md`. No stat block is imported
from them; all blocks below are fresh DEC-077.A-analogous constructions.

---

## Run Conventions (A1–A8, advisory; none alters table play)

| # | Convention |
|---|---|
| A1 | **Action economy (fixed):** one substantive exchange per combatant per round (single-action reading of DEC-106, still OPEN). |
| A2 | **Turn order:** Speed desc (DEC-095). Ties: higher bss, then bsp; remainder reroll. |
| A3 | **Bounded scenes:** per-scene round budget. **Primary end = budget-expiry withdrawal beat; secondary end = HP<=0** (DEC-052; negatives persist, DEC-108). |
| A4 | **Aleena-survives invariant:** Aleena never ends a scene at HP<=0; clamp at 1, narrate collapse (module content, not a rule). |
| A5 | **Healing:** H1(a) restore = accumulated Margin capped at current max; H2 target 40; H3 Devotion-only, MP cost = natural roll, HP-only; H4 targeted penalty; H7 locked order; HC-1.1/1.2; DEC-072.A. |
| A6 | **Advanced-Skill coverage:** Scene-1 Perception teaching beat is **mandatory, fixed 00=100** (DEC-012 named skill). Elsewhere probabilistic — never force a failed Double. |
| A7 | **Terminality (H6):** HP<=0 ends the run's combat; no revival. Scene 6: **Bargle HP<=0 before the fork → Ending A, fork SKIPPED.** |
| A8 | **Effect exclusivity:** winner declares the prescribed Effect — **exactly one Effect per winning exchange** (DEC-024/025); no compound path. |

---

## Cast — DEC-077.A-analogous advisory conversions

NPC construction is **Reserved** (Canonical §15). Method: DEC-077.A workflow used
**analogically** — DEC-077.A is ruled for GURPS-BToV conversions only; applying it
to D&D Red Box beats is an unruled extension, flagged advisory (see Guesses G1).
Tiwa rules on each conversion; all blocks stay provisional. **All Defense values
are advisory fiat** (no ruled NPC-defense construction method; cf. DEC-098 default
only where no skill is authored — here Defense IS authored, value still fiat).

### Rowan (PC, fresh Tier-1; locked derivation Canonical §4/DEC-004)
Body bpp58 bps52 bpe47 bpx40 bsp61 bss55 bse47 bsx38 bep60 bes53 bee57 bex44;
Mind mpp42 mps45 mpe50 mpx33 msp48 mss55 mse40 msx46 mep51 mes43 mee49 mex47.
**HP 615 · MP 549 · PE 170 · Speed 166 · ER 113 · MR 94 · Movement 7.**
Attack T1 bpp 29 · Defense T1 bss 27 · Perception T1 mss 27 · Stealth T1 bsp 30 ·
Composure T1 mex 23 (module-added for the climax fork; content-authoring, flagged).
Gear: Shortsword (held, melee, slashing, light); Leather Armor (worn, defense:armor).
Tag: `reaction:vigilant` (ally-targeted trigger, DEC-132.B; exercised once, Sc.6).

### Aleena (ally NPC)
Body 45/40/50/48/42/47/44/41/55/46/58/50; Mind 50/48/62/44/46/50/43/49/60/55/65/52.
**HP 566 · MP 624 · PE 159 · Speed 133 · ER 101 · MR 115 · Movement 5.**
Devotion T1 mee 32 · Smite T1 bep 27 · Defense T1 bss 23 (**fiat**). Mace (bludgeoning,
light); Holy Vestments (worn, **no** defense:armor tag).

### Goblin (creature; signature skills at full Cap per DEC-086/087)
Body 40/38/30/25/45/48/35/30/32/36/34/28; Mind 22/28/20/15/25/35/24/18/20/22/25/19.
**HP 421 · MP 273 · PE 102 · Speed 128 · Movement 6.** Crude Attack T1 bpp 40 sig ·
Defense T1 bss 24 (**fiat**) · Trip T2 bsp+bss 46 sig. Rusty dagger; no armor tag.

### Rattlesnake (creature)
Body 30/28/24/20/60/58/55/45/22/25/24/26; Mind 15/18/14/12/30/40/28/20/16/18/15/17.
**HP 417 · MP 243 · PE 71 · Speed 173 · Movement 7.** Venomous Bite T2 bsp+bss 59 sig ·
Defense T1 bss 29 (**fiat**) · Stealth T1 bsp 30. Bite = Body-attribute Wound,
poison-flavored — **poison is NOT a ruled Effect (advisory, flagged).**

### Ghoul pack (creature; opposed via leader)
Body 42/36/40/30/50/52/44/38/40/42/44/36; Mind 20/25/18/16/28/30/22/20/18/22/20/21.
**HP 494 · MP 260 · PE 126 · Speed 146 · Movement 6.** Claw T2 bpp+bps 39 sig ·
Grapple T2 bsp+bpp 46 sig · Defense T1 bss 26 (**fiat**) · Desecration T2 mpp+mps
22 sig (opposes turning). No armor tag.

### Bargle (villain)
Body 35/32/30/44/40/46/38/42/33/35/37/40; Mind 68/65/60/55/58/52/50/48/62/57/55/50.
**HP 452 · MP 680 · PE 105 · Speed 124 · MR 119 · Movement 5.** Bolt T2 mpp+mps
66 sig · Defense T1 bss 23 (**fiat**) · Beguile T1 mpx 27. Wand (ranged, electric);
Robes (worn, **no** defense:armor tag).

---

## Scene 1 — Goblin on the Road [reconstruction]

Beat: warned village → Old Road ambush. Speed: Rowan 166 → Goblin 128. Budget 6.
End: Round-6 expiry → goblin withdraws (**plot beat narrated, no morale rule —
advisory**); HP<=0 ends early (DEC-052/108).

- **Perception teaching beat — mandatory, fixed 00=100** (locked DEC-001: 100 always
  fails; ruled DEC-012/DEC-140: failed Double creates Advanced Skill; locked
  DEC-006/007/008/010 for cost/overflow/recovery/cascade). Cost 100 MP (549→449),
  no overflow; Failure XP 73 → Perception 27→29; **Perception (Advanced) T2
  mss+mps Cap 50 Start 1** created; Recovery +47 → MP 496.
- **Combat exchanges** (locked+ruled: DEC-013/105 matrix; DEC-104 contest-delta
  injury; DEC-103 shred where T2 fires; DEC-007 overflow; DEC-008 recovery).
  Prescribed effects: Attack wins → Inflict Injury; Trip wins → Prone Condition
  (Zero-Step + quartile/parity per Canonical §14.1 + DEC-100, **locked**).
- **100-fumble symmetric branch** (ruled DEC-140): a goblin roll of exactly 100
  would create a creature Advanced Skill (e.g., Creep Attack T2 bpp+bps Cap 39
  Start 1). Shown, never forced.
- **Worked overflow (locked DEC-007):** Trip roll 95 vs Goblin PE 40 → cost 95,
  shortfall 55 → roller takes 55 HP (PE→0, HP 421→366), win or lose.

## Scene 2 — Rattlesnake Chamber [reconstruction]

Beat: coiled snake over a footlocker. Snake 173 acts first. Budget 5. End: HP<=0
or Round-5 expiry → retreats into a crevice (**plot beat, advisory**).

- **Venomous Bite (T2) wins → Wound** (ruled DEC-035.A record, DEC-102 target,
  DEC-004 live recalc, DEC-041 ≥T2 gate, DEC-103 shred). Poison flavor advisory.
- **Treasure Search** (locked Core Test, Mind→MP): Perception 29; fail → Failure XP
  → General XP; one retry. Success finds electrum + (that search only) a white
  pearl — pearl matters only in Ending B (source-fidelity beat, advisory).

## Scene 3 — Aleena Joins: S-11 Healing [reconstruction]

Beat: cleric in white-and-gold joins; mends Rowan iff harmed (else declined, no
test). Extended Test DEC-073 + A5/H7 (ruled/convention). Devotion 32, target 40.
Worked: rolls 12/25/41/8 → margins 20+7+0+24 = **51 ≥ 40** → restore **51 HP,
current-max clamped** (H1(a)/HC-1.2). DEC-072.A: only Devotion/mee-targeted wounds
penalize — her later mpp/mps wound does not. Interval ledger (MP; Recovery
floor(MR/2) = 57, clamped at 624): 612/602/618/593/642→624 across the four
intervals; failures still cost (DEC-068) but add no Margin (DEC-067).

## Scene 4 — Ghoul Passage / Turning [reconstruction]

Beat: three ghouls; Aleena raises her symbol. **Turning = S-1 Devotion 32 vs
leader Desecration 22** (ruled DEC-013/105). Success → pack withdraws (**plot beat;
no morale rule — advisory**). Failure branch: 3-round budget fight, Claw/Grapple
(T2) with Body-wound recalc (never "cosmetic").

## Scene 5 — Locked Door [reconstruction]

Beat: iron-bound door; voices beyond. **Passive-gate test** (advisory mapping):
success = roll ≤ Skill − hardiness 15. Bash Attack 29→14 / improvise mpp 42→27 /
find-around Perception 29→14. Default **bash**, ≤3 attempts. After 3 fails: forced
by exhaustion (narrated, advisory). Teach (ruled DEC-041): Tier-1 bash → ≥T2
production gate does NOT fire → no Location Index, no Wound.

## Scene 6 — Bargle: Two Endings [reconstruction]

Beat: lantern chamber; black-robed mage berating a goblin; retreat blocked
(**beat design, not a rule — advisory**). Invisibility grants **no surprise
advantage (no ambush mechanic — advisory)**. Order Rowan 166 → Aleena 133 →
Bargle 124 (module runs Bargle-first Round 1 as narrative override, flagged).
Budget 3 rounds + climax fork. **Attrition can pre-empt the fork** (Bargle HP<=0
any round → Ending A, fork skipped).

- **Bolt (T2) wins → Wound** (same ruled chain as Sc.2). Worked: Bolt→Aleena Head,
  Mag 3, mps −3 → MP max recalc, HP unchanged (Mind wound — locked DEC-004).
- **Reaction (DEC-132.B, ruled framework + authored content):** Rowan's
  `reaction:vigilant` fires once when Bargle's hostile Effect lands on Aleena:
  full S-1 out-of-turn, standard cost/overflow/XP, uncapped (DEC-132.A R3).
- **Rounds 2–3 rotation:** Inflict Injury → Armor Bypass (degrades per DEC-030
  against untagged locations; full DEC-136/137 path flagged, not forced).
- **Climax fork — S-1 Beguile 27 vs Composure 23** (charm NOT a ruled Effect —
  **advisory representation, flagged**). Tie → reroll ≤3×, final tie → Ending A.
- **Ending A** (resist / Bargle down): decisive exchange; residual absorbed as
  scripted collapse (module script, flagged). **Ending B** (hex holds): stripped,
  pearl winks unnoticed (if found); both walk out. **Neither dies.**

## Aftermath [reconstruction]

Any ending: S-11 Devotion healing (A5) restores accumulated Margin, clamped.
Wound records step down one Tier per qualifying test (DEC-035.A cl.5 / DEC-121) —
**healing HP and healing Wounds are different actions against different records.**

---

## Dependency Classification (verify vs live decision register)

| Dependency | Basis |
|---|---|
| d100 roll-under, 100 always fails; Cost = natural roll; Overflow→HP; Recovery | **locked** (Canonical §§2/7/8; DEC-001/006/007/008) |
| S-1 opposed contest matrix; both roll; defender-win = no counter | **ruled** (DEC-013/105/101) |
| Contest-delta injury; wound record + Body/Mind target + live recalc | **ruled** (DEC-104; DEC-035.A/102; DEC-004) |
| Tier shred + margin de-escalation; tier=gating ≥2 | **ruled** (DEC-103; DEC-041/107) |
| Zero-Step + quartiles + parity laterality | **locked** (Canonical §14.1; DEC-100/112) |
| Advanced-Skill failed-Double origin, universal incl. creatures | **ruled** (DEC-012/140; template pre-auth DEC-087) |
| Failure XP + Roll-Pool cascade; Extended/S-11 healing + H1(a)–H7 | **ruled + convention** (DEC-009/010/067/068/071/073; H-block) |
| Targeted healing penalty; Speed order; single-action; incapacitation/neg-HP | **ruled** (DEC-072.A; DEC-095/106; DEC-052/108) |
| Reaction ally-trigger; one Effect per win | **ruled** (DEC-132/132.A/132.B; DEC-024/025) |
| All NPC Defense values; DEC-077.A D&D reuse; morale/withdrawal; invisibility edge; charm/poison; pearl/electrum values; door hardiness 15; pearl-miss beat | **advisory-flagged** (Reserved §15 / no rule / scope extension — one-line reasons) |

---

## Guesses Disclosed

1. **DEC-077.A reuse (medium):** workflow is ruled for GURPS-BToV conversions; D&D
   Red Box reuse is analogical. Blocks stay provisional pending Tiwa.
2. **Beat order/content (medium):** goblin → snake → Aleena → ghouls → door →
   Bargle/two endings reconstructed from general knowledge + repo research sources;
   no verbatim source used.
3. **Budgets 6/5/3 + withdrawal ends (medium):** pacing beats; withdrawal is plot,
   never a morale rule (none exists).
4. **Door hardiness 15; pearl/electrum (low):** deterministic advisory tokens.
5. **Bargle-first Round 1 (medium):** narrative override of DEC-095; flagged.
6. **Single-seed discipline (high):** seed 20260917, single life, no distributional claims.

## Coverage Checklist

Core Test · Overflow · Recovery · Failure XP/cascade · S-1 matrix · defender-wins ·
contest-delta injury · T2 gate · shred/de-escalation · Zero-Step/quartiles/parity ·
wound record/target/recalc · Advanced-Skill + universal · S-11 + H-block + targeted
penalty · Speed · single-action · incapacitation/neg-HP · reaction · one-Effect rule
· signature full-Cap starts — **all exercised or exercisable.** NOT covered by design:
Active Defense (DEC-044), full Armor Bypass, equipment damage/repair, encumbrance,
magic subsystem, charm/poison/morale as ruled Effects.

## Fidelity Limits

Could not verify against the 1983 text: exact room/beast order; Perception-test
mechanics; healing procedure; location method; gate/saving-throw mechanics;
surprise rules; climax outcomes (Aleena-survives is a Bargle-Incident revision);
NPC numbers; treasure values. Research sources used only to confirm the public
beat skeleton (solo walkthrough → road encounters → Aleena/Bargle finale), never
as quotation sources. All beats are reconstructions.

## Authority Boundary + Human Question

No ruling made; nothing promoted. Evidence: DEC-077.A text limits the conversion
workflow to GURPS-BToV creatures. Ambiguity: whether its workflow generalizes to
D&D-sourced beats. Consequence: this module's NPC blocks cannot claim DEC-077.A
coverage without extension. **Human question for Tiwa: does the DEC-077.A
conversion workflow extend to non-GURPS (e.g., D&D) source material, or is a
separate authoring path needed?** — stopping here per escalation workflow.

*End of NON-CANONICAL advisory module (v1.1).*
