---
document:
  title: "Tiwas — Alpha-Playtest Corpus (One-Off, GM Table-Ready)"
  version: "1.0"
  status: "One-off, dated, scoped exception (see Standing-Prohibition Overrule below). NOT canonical. NOT a standing merge artifact. Does not rule, promote, or lock anything."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-01"
  last_modified_date: "2026-09-01"
---

# Tiwas — Alpha-Playtest Corpus (One-Off, GM Table-Ready)

## Standing-prohibition overrule — required log entry (inserted verbatim, dated)

Tiwa has explicitly and consciously overridden the standing "do not create another
single merged file" prohibition, for this one alpha-playtest corpus only. This file
is a dated, one-off, scoped exception for GM table use during alpha playtesting.
It is NOT a reinstatement of any standing merge artifact, is NOT to be periodically
regenerated, and future agents must NOT assume this prohibition is generally lifted.
Scoped per Tiwa's direct instruction as human designer/ruling authority, **2026-09-01**.

---

## How to use this file

- **What this file is.** A single-file, table-ready assembly of every system currently
  Ruled or Locked in the live repository, compiled 2026-09-01 from the live register
  (`_consolidation/decision-register.md`, last modified 2026-09-01), the canonical
  ruleset (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`, v1.3), and the
  cited handoff records in `investigations/`. No rule in this file has been reconstructed
  from memory or from any cached snapshot; the live register is authoritative over any
  earlier wording.
- **What this file is NOT.** It is not a ruling. It does not resolve, merge, or clean up
  any open fork. It does not promote or demote anything — Locked / Ruled-non-canonical /
  Draft-pending-reconfirmation / Open distinctions are preserved exactly as they appear
  in the live register. Compilation confers no authority.
- **Compilation boundary.** Only material tagged `Canonical / Locked` or `Non-canonical
  designer ruling` and currently Current/Ruled in the live register appears as table-ready
  mechanics (Parts A–B). Explicitly unsettled material is listed without mechanics in
  Part C. Play observations should be logged against Part D.
- **Provenance of the underlying material.** The canonical ruleset (D1) is
  Canonical / Locked. Every DEC cited in Part B is a real designer ruling recorded in
  the live register as `Non-canonical designer ruling` — none has completed the 8-step
  Promotion Rule (REQ-021 / Proposals/WIP §21), and none of this file's assembly changes
  that.

### Status vocabulary used throughout (per `governance/status-model.md`)

| Label in this file | Meaning |
|---|---|
| **Canonical / Locked** | Authoritative, current, must not be contradicted (D1 self-declared). |
| **Non-canonical designer ruling** | Real human/designer decision about candidate/non-canonical material. Not Canonical. |
| **Draft pending Tiwa reconfirmation** | The cited handoff file is a draft; the live DEC entry is the operative register content. |
| **Open** | No settled decision exists. Not table-ready. |
| **Confirmed-closed** | Resolved via the named DEC/ruling; listed in Part C so it is neither re-opened nor omitted. |

---

# Part A — Core Locked Rules (D1): DEC-001–DEC-016

Source: `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` (D1, v1.3), transcribed
without compression. All formulas, the 9-step Core Test Transaction, and all 18 Invariants
are given in full below.

## A.1 d100 and Resolution (DEC-001) — Canonical / Locked

- A Tiwas d100 produces an integer from **1–100**.
- Physical percentile dice displaying `00` represent **100**, never zero.
- Roll-under: a skill test succeeds when `Roll <= Skill`, unless the 100-Fumble rule applies.
- **100-Fumble:** a roll of **100 always fails**, regardless of Skill value. A roll of 100
  is also always treated as a qualifying Double. Therefore no Skill value produces literal
  100% test reliability.
- **Doubles:** canonical Double values are `11, 22, 33, 44, 55, 66, 77, 88, 99, 100`. A
  Double produces its special Advanced Skill effect only when the roll is also a Failure.
  The nine digit-doubles qualify when the Double exceeds the tested Skill. 100 always
  qualifies because 100 is always a Failure.

## A.2 Rounding (DEC-002) — Canonical / Locked

All fractional calculations use **floor** rounding. There are no general exceptions.

## A.3 The 24-Attribute Matrix (DEC-003) — Canonical / Locked

Characters possess 24 independently generated attributes, each generated as `1d100`,
divided into twelve Body and twelve Mind attributes.

| Code | Animal | Category | Tier-1 Skill |
|---|---|---|---|
| bpp | Bear | Body / Power / Power | Might |
| bps | Tiger | Body / Power / Speed | Impact |
| bpe | Elephant | Body / Power / Endurance | Brawn |
| bpx | Dragon | Body / Power / Social | Presence |
| bsp | Hawk | Body / Speed / Power | Agility |
| bss | Rat | Body / Speed / Speed | Reflexes |
| bse | Horse | Body / Speed / Endurance | Quickness |
| bsx | Monkey | Body / Speed / Social | Grace |
| bep | Badger | Body / Endurance / Power | Toughness |
| bes | Wolf | Body / Endurance / Speed | Stamina |
| bee | Ox | Body / Endurance / Endurance | Vitality |
| bex | Dog | Body / Endurance / Social | Poise |
| mpp | Stag | Mind / Power / Power | Cunning |
| mps | Snake | Mind / Power / Speed | Wits |
| mpe | Rooster | Mind / Power / Endurance | Willpower |
| mpx | Fox | Mind / Power / Social | Glamour |
| msp | Bat | Mind / Speed / Power | Acuity |
| mss | Cat | Mind / Speed / Speed | Perception |
| mse | Rabbit | Mind / Speed / Endurance | Alacrity |
| msx | Otter | Mind / Speed / Social | Charm |
| mep | Crane | Mind / Endurance / Power | Focus |
| mes | Goat | Mind / Endurance / Speed | Discipline |
| mee | Owl | Mind / Endurance / Endurance | Resolve |
| mex | Pig | Mind / Endurance / Social | Composure |

An attribute belongs permanently to either Body or Mind.

## A.4 Derived Statistics (DEC-004) — Canonical / Locked

Derived statistics are **live calculations** — changing an attribute immediately changes
every derived statistic and Skill Cap that depends on it.

| Statistic | Formula |
|---|---|
| Health Points (HP) | Sum of all 12 Body attributes |
| Mental Points (MP) | Sum of all 12 Mind attributes |
| Physical Energy | bep + bes + bee |
| Speed | bsp + bss + bse |
| Energy Regen | bep + bes |
| MP Regen | mep + mes |
| Movement Speed | floor((bsp + bss) / 15) |

MP is simultaneously the Mind resource pool and the total derived from the twelve Mind
attributes. This identity is intentional.

## A.5 Skills: Tier / Cap / Starting Value (DEC-005) — Canonical / Locked

- **Skill Tier** is the number of **distinct attributes** used in its Cap formula. A
  Tier-1 Skill uses one attribute; a Tier-T Skill uses T attributes. No attribute may
  appear more than once within a Skill formula. The theoretical maximum Tier is 24.
- **Skill Cap:** `Cap = floor((A1 + A2 + ... + AT) / T)` — the floored average of the
  underlying attributes. Increasing Tier does not inherently increase expected Cap; it
  averages additional attributes and reduces variance.
- **Starting Skill:** `Starting Value = floor(Cap / 2)`. A Skill may therefore
  legitimately begin at 0.

## A.6 Canonical Test Transaction (DEC-006) — Canonical / Locked

Every Skill test follows this order:

1. Roll 1d100.
2. Determine the Skill's resource domain.
3. Determine Success or Failure.
4. Pay Cost equal to the natural roll.
5. Apply Overflow if the resource pool cannot pay the full cost.
6. Resolve Failure XP.
7. Resolve qualifying failed Double / Advanced Skill effects.
8. Recover the appropriate resource.
9. End the test.

No Universal Play subsystem may replace this transaction with an alternative resolution
engine.

## A.7 Resource Cost and Overflow (DEC-007 + DEC-007.A) — Canonical / Locked

Every test costs the exact number rolled.

- **Body Skill:** Cost is paid from Physical Energy.
- **Mind Skill:** Cost is paid from MP.
- If the available resource is insufficient: `Overflow = Cost - Remaining Resource`. The
  resource pool falls to zero and the Overflow becomes direct HP damage. Overflow does
  not create a second resource pool.

**DEC-007.A — Overflow-immutability clause (designer-approved wording amendment, 2026-09-01):**

> "Overflow (the HP damage resulting from insufficient resource to cover a test's
> natural-roll Cost) is a pure function of the natural roll and the resource pool at time
> of test. No Tag, Trait, Effect, Condition, or subsystem may reduce, redirect, absorb,
> or otherwise modify Overflow's magnitude or application to HP."

Placement: recorded as an amendment to DEC-007 per designer ruling — not a new Invariant.
Assessed as a gap-closer making explicit what DEC-007/Invariant 7 already imply, not a
change to Locked material (checked against Invariants 6/7 for contradiction — none found).
**Corollary:** consequence of this + DEC-058 (S5-A) = Armor Tags never modify Overflow
(Item B corollary; no separate DEC).

## A.8 Recovery (DEC-008) — Canonical / Locked

Recovery occurs **after every test** and is always the final stage. The recovered amount
is `floor(Regen / 2)`. Recovery applies to the resource pool just spent and is clamped at
that pool's maximum. Recovery occurs regardless of success, failure, Overflow, failed
Double, or Advanced Skill creation. A full Rest action remains Reserved and is not defined
by the Core.

## A.9 Failure XP (DEC-009) — Canonical / Locked

Failure XP is `max(0, Roll - Skill)`. The clamp prevents negative XP when the 100-Fumble
forces a failure against Skill 100 or higher.

## A.10 Skill Roll Pool (DEC-010) — Canonical / Locked

Failure XP first enters a temporary Skill Roll Pool. The pool exists only for the current
failed test; it does not persist between tests. Within the failed test:

```text
while Pool >= Current Skill
and Current Skill < Cap:

    Pool -= Current Skill
    Skill += 1
```

The process stops when the remaining pool cannot afford another increase, or the Skill
reaches its Cap. Any remaining pool becomes General XP.

**Skill at 0:** If a Skill is 0, the cost of increasing it to 1 is zero. A failed test
with nonzero Failure XP therefore raises a Skill-0 to at least 1 immediately. This is
intentional.

## A.11 General XP (DEC-011) — Canonical / Locked

General XP receives: Skill Roll Pool remainder; GM/quest/adventure awards. General XP may
increase Attributes and Skills. The cost of increasing a value by 1 is its current value.
General XP must cover the entire cost of an increase; partial advancement is not permitted.

- **Above-Cap advancement:** General XP may raise a Skill above its current Cap. Skill Roll
  Pool advancement may not.
- **Advancement ceiling:** the initial 1–100 range applies to attribute generation;
  advancement has no fixed upper bound. Skills above 100 remain subject to the mandatory
  100-Fumble.

## A.12 Advanced Skills (DEC-012) — Canonical / Locked

A qualifying failed Double immediately creates an Advanced Skill.

**Creation:**
1. New Skill Tier = failed Skill Tier + 1.
2. Add one attribute not already present in the failed Skill formula.
3. Recalculate the new Cap from the complete attribute set.
4. Choose either: starting value 1; or roll 1d100 and use `min(Roll, New Cap)`.

**Duplicate restrictions:** an attribute cannot appear twice within a single Skill formula.
The same Advanced Skill — defined by the same base Skill and added attribute — cannot be
created twice.

**Resource domain:** an Advanced Skill retains the resource domain of its original Tier-1
lineage. A Body-rooted lineage remains Physical Energy based even if later attributes
include Mind attributes; a Mind-rooted lineage remains MP based even if later attributes
include Body attributes.

**Advancement depth:** Advanced Skills may themselves generate further Advanced Skills.
There is no arbitrary Tier ceiling beyond the natural 24-attribute limit.

## A.13 Universal Opposed Contest — S-1 (DEC-013) — Canonical / Locked

S-1 is the universal opposed-contest primitive. Each participant performs an ordinary Core
Test independently. The contest layer does not alter the underlying test.

**Outcome matrix:**

| Participant A | Participant B | Result |
|---|---|---|
| Success | Failure | A wins |
| Failure | Success | B wins |
| Success | Success | Compare Quality |
| Failure | Failure | Repeat contest |

Each participant pays their own natural roll cost and resolves their own Failure XP, Double
eligibility and Recovery.

**Quality measures** (selected by contest type):

| Mode | Formula | Primary identity |
|---|---|---|
| Margin | `Skill - Roll` | Efficiency / precision |
| Blackjack | `Roll` | Commitment / force |
| Hybrid Committed | `Roll + max(0, Skill - 99)` | Commitment with continued high-Skill scaling |

Quality only compares already-rolled successful tests. It never modifies: the historical
roll; Cost; Failure XP; Double eligibility; Recovery.

**Quality selection** — current guidance:

| Situation | Default |
|---|---|
| Precision / efficiency | Margin |
| Force / commitment | Blackjack |
| Mixed / uncertain | Hybrid |

Blackjack and Hybrid's distinctive identity becomes meaningful primarily once relevant
Skills are sufficiently high. At low Skill, the success/failure gate dominates. The GM may
override situational guidance where the fiction demands another Quality measure.

**Failure/Failure:** both participants repeat the contest. Both tests have already incurred
all normal Core consequences before the repeat occurs.

**Exact Quality tie:** an exact Quality tie causes the contest to repeat; the repeat is a
fresh contest round.

**S-1 validation:** S-1 has been validated through simulation across Skill 10–250 and Skill
gaps up to 151. The empirical validation and designer rulings are retained as historical
design evidence rather than treated as mathematical rules themselves.

## A.14 S-2 — Tier-1 Location Index Provider: Zero-Step (DEC-014) — Canonical / Locked, limited S-2 decision

This section locks only the Tier-1 Location Index provider. It does not complete the
broader hit-location subsystem.

**Zero-Step:** when a rule calls for a Tier-1 Location Index, use **Zero-Step**. Zero-Step
derives the Location Index by exchanging the tens and units digits of the attacker's
natural d100 roll. Interpret `00` as `100` under the normal d100 rule after the exchange.

| Natural d100 roll | Zero-Step Location Index |
|---:|---:|
| 37 | 73 |
| 10 | 1 |
| 1 | 10 |
| 100 (`00`) | 100 (`00`) |

For physical percentile dice, exchange the displayed tens and units digits. For another
rolling method, express the natural roll as its two percentile digits before exchanging
them.

**Determinism and player choice:** Zero-Step is deterministic. The attacker does not choose
between the natural roll and the transformed result. The natural roll remains authoritative
for every Core Test consequence, including outcome, Cost, Overflow, Failure XP, failed-Double
eligibility, Advanced Skill effects and Recovery. The transformed result is used only as the
Tier-1 Location Index.

**Scope retained for later S-2 work** (not established by this ruling): whether and when a
scene uses Tier 0, Tier 1 or Tier 2 location granularity; Tier-0 and Tier-2 procedures;
anatomical mapping from a Location Index to a zone; wound, armour, defence and Outcome
Effect interaction; whether any later rule may select, modify or consume a Location Index.
These remain non-canonical until separately resolved through governance.

**Future optional-rule observations:** playtest participants suggested choosing between the
natural and swapped values. That suggestion is not part of the basic rule and creates no
player choice in current Tiwas. The designer may later consider, in an optional-rule
appendix only: an attacker choice granted by an explicit special ability; and a defender
choice. Neither observation is a current rule, a permission, or a design commitment.

**E9 human usability playtest record** (evidence class: empirical finding — passed for the
tested physical two-d10 method only): the E9 playtest used two physical d10s with 50
participants (25 new to RPGs, 25 RPG players new to Tiwas). Participants reported no
difficulty rolling the dice or exchanging the digits for hit location; feedback was
positive. Other input methods (single d100, digital roller, verbally announced result)
were not tested and are not covered by this finding.

**Comparative derivation-cost residual** (separate from E9): Units-Digit requires 0–1
additional derivation operations across the examined rolling modes; Zero-Step requires 1–2.
This is a comparative structural observation about derivation steps, not a human-usability
finding and not an additional E9 status.

## A.15 Reserved Systems (DEC-015) — Canonical / Locked (scope statement)

The following remain outside the locked Core unless separately incorporated through formal
governance: hit-location rules (except the Tier-1 Zero-Step provider, §A.14); wound
activation/severity; Outcome Effects; armor; active/passive defense; incapacitation; death;
healing; Rest; equipment; encumbrance; conditions; environmental hazards; difficulty
grades; task/stakes adjudication; Extended Tests; NPC construction; magic/special-ability
implementation; GM procedure; campaign procedures; setting-specific content.

Where a separate Universal Play subsystem has already been locked, such as S-1, its current
rules supersede the older "Reserved" classification.

## A.16 Core Architectural Invariants (DEC-016) — Canonical / Locked

Every future Tiwas subsystem must preserve:

1. d100 produces 1–100.
2. 100 always fails.
3. 100 is a qualifying failed Double.
4. All fractions floor.
5. Success is roll-under.
6. Cost equals the natural roll.
7. Overflow becomes HP damage.
8. Failure XP uses `max(0, Roll - Skill)`.
9. Skill Roll Pool is temporary.
10. Skill Roll Pool advancement cannot exceed Cap.
11. General XP can exceed Cap.
12. Failed Doubles can create Advanced Skills.
13. Advanced Skill Caps are recalculated from the full attribute set.
14. Advanced Skill resource domain follows lineage.
15. Derived statistics are live.
16. Recovery occurs last.
17. No Universal Play subsystem may introduce a competing primary resource or progression
    economy.
18. Universal Play modules must build on the Core Test Transaction rather than replace it.

---

# Part B — Ruled non-canonical subsystems (table-ready, fully detailed)

Each block below is tagged **Non-canonical designer ruling** and cited by DEC number and
source path, per the live register (`_consolidation/decision-register.md`). DEC entries are
transcribed verbatim from the register's Decision column; where the register is the
operative content, the handoff file is cited as the source pointer. Where a DEC is also
a Locked item reproduced in Part A, the block points to Part A rather than duplicating (the
full Locked text remains available — nothing has been compressed).

## B.1 S-1 Opposed Contest — Quality tie-breaker addendum

- **DEC-013 (S-1 core):** **Canonical / Locked** — full text in **Part A §A.13**.
- **DEC-031 (Quality's Role in Single-Effect Outcome Resolution, Q-S3-6):**
  **RULED — Option B: Quality gates eligible Effects.** Quality (already computed at S-1
  for tie-breaking) determines which Effect tier is selectable by the winner of a
  successful opposed contest. Higher Quality unlocks access to more severe/narratively
  significant Effects; every winning Quality value (≥ 1) guarantees at least one
  baseline-tier Effect (floor rule). No Effect scaling by Quality; no additional Effect
  granted. Single deterministic threshold lookup post-winner; preserves "one roll → one
  Effect" and minimum resolution steps.
- Evidence: Designer ruling, 2026-08-30; supported by 8-model LLM blind survey (5/8 B,
  3/8 C, 0/8 A) per `investigations/llm-quality-s3-reports-2026-08-30.md`, meta-analysis
  per `investigations/tiwas-s3-documentarian-handoff-report-dec028-2026-08-30.md` and
  `investigations/gemini-S-3-collate-table2-2026-08-30.md`. (Survey transcripts: pointer
  only — see `investigations/`.)
- Authority / Status: **Non-canonical designer ruling** — Ruled.

**Table-play with this block:** every winning Quality value ≥ 1 guarantees at least one
baseline-tier Effect; Quality also breaks S-1 ties via §13.5 (exact tie → repeat) and
selects the Effect tier the winner may draw from at B.3.

## B.2 S-2 Zero-Step Location Index subsystem (attack + non-attack provenance)

- **DEC-014 (Zero-Step core):** **Canonical / Locked** — full text in **Part A §A.14**.
- **DEC-037 (S-2 / S-4 Non-Attack Location Index Generation):**
  **RULED — (1) Primary Provenance Rule:** When a character fails a governing Core Test
  against an environmental hazard, obstacle, or physical risk (e.g. Jump, Climb, Evasion,
  Spot Trap), that same failed d100 roll supplies the digits for Zero-Step Tier-1 Location
  Index generation (exchanging tens/units digits per Canonical §14.1–14.2).
  **(2) Hazard "Win":** A failed test constitutes a "win" for the hazard; if failure
  margin/severity qualifies for an S-3 Effect, the applicable Effect (Inflict Injury or
  Impose Condition: Wounded) is applied to the location indicated by the character's failed
  roll. **(3) Systemic Exempt:** Global/systemic threats (Drowning, Suffocation, Extreme
  Temperature, Poison) apply direct HP/Conditions without a Location Index. **(4) Passive
  Fallback:** If a physical impact occurs with no roll of any kind, the system outputs a
  numeric stub Location Index (e.g. `00` or `50`) routed through Zero-Step, deferring
  anatomical naming until OPEN-003 locks.
- Evidence: Designer ruling, 2026-08-30; agreed text per
  `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md` §3.5, §5; refined
  passive-fallback (numeric stub) supersedes earlier "Center Mass/Torso" wording;
  stress-test reopening step satisfied by literal re-run in
  `investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md` (all 14 scenarios
  handled; non-blocking flags: H0 Rider B, S-8 dependency).
- Authority / Status: **Non-canonical designer ruling** — Ruled.
- **DEC-039 (OPEN-001B — Extended Test governing roll for Location Index):**
  **RULED — Final roll governs.** When an Extended Test (S-9/S-10) produces a physical
  consequence across a multi-roll sequence, the **final roll in the sequence** is the
  governing test for Location Index generation. No earlier roll in the chain is stored or
  referenced for this purpose (rationale: less record-keeping). Answers only "which roll
  feeds Zero-Step" — orthogonal to S-9/S-10's progress-method and failure-behavior forks.
  Closes the "H0 Rider B tie-break for Extended Tests" residual flag recorded under
  DEC-037.
- Evidence: Designer ruling, 2026-08-31 (in-session chat); residual flag per
  `investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md`.
- Authority / Status: **Non-canonical designer ruling** — Ruled.

**Scope notes for the table.** DEC-037 point (4) references "deferring anatomical naming
until OPEN-003 locks" — OPEN-003 is now closed/confirmed via DEC-041 (see B.4), which
supplies the anatomical mapping; the DEC-037 wording is preserved verbatim. Related
confirmed-closed items (OPEN-001 → DEC-038, OPEN-002 → DEC-040) are listed in Part C and
are not table-ready material.

## B.3 S-3 Effect menu and gating (DEC-023–DEC-030)

**Status tag:** **Non-canonical designer ruling** — all eight rulings Ruled
(recorded in `_consolidation/decision-register.md` §D; menu structure via
`investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`). The S-3
effect-identity/multi-effect-opposition thread is Closed.

> **Caveat — gated-tier Contents are not fully enumerated.** The menu *structure* below is
> Ruled (DEC-023). The *contents* inside the gated tiers (specifically the specific Effects
> populating the Position, Condition, Equipment, Defense, and Location tiers) are **not
> fully enumerated** — that enumeration remains an open tracking item and is NOT table-ready.
> See Part C.

- **DEC-023 (Q-S3-1) — Effect menu structure.** **RULED — Tiered Effect menu**: base tier =
  Inflict Injury (HP-only) + Open Retreat/Compel Yield; five gated tiers (Position →
  Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6; Location →
  S-2 invocation promotion). **Disarm/Break Hold** placed via Q-S3-3's combined
  Tag+Location gating. Status: Ruled; Disarm/Break Hold placement finalised via DEC-028.
- **DEC-024 (Q-S3-2) — Effect purchasing / multiplicity.** **RULED — Flat one-Effect-per-win.**
  No Quality-based scaling, no purchasing of additional Effects off a single win. A
  second/additional Effect requires a **separate opposed roll** — mechanism not yet
  designed; deferred. Status: Ruled; mechanism deferred to new thread.
- **DEC-025 (Q-S3-2a) — Effect naming/identity gating.** **RULED — Pure declared intent
  (no Skill-side gating).** Effects are granted solely by the declared outcome of a
  successful S-1 contest (subject to the other gates already ruled: gear/ability Tag +
  Location Index where required, DEC-028). The Skill name carries no mechanical weight and
  does not entitle or gate any Effect; a formal tag/category system on Advanced Skills is
  **rejected** (designer rationale: formal tags are exploitable and would push players to
  limit Skill choices to degenerate mechanical Effects). Reinforces Canonical §12.3; no
  Skill-side tag data introduced; REQ-017 satisfied. Status: Ruled.
- **DEC-026 (Q-S3-2b) — Second-Effect opposed-roll mechanism.** **RULED — Different
  Advanced Skill; defensive roll deferred.** The separate opposed roll for any Effect
  beyond the single free one (DEC-024) uses a **different Advanced Skill** domain-appropriate
  to the declared second Effect; the actor accepts the risk of the additional roll. The
  full 9-step Core Test Transaction applies (REQ-018). The target receives **no defensive
  roll until S-6 locks**; any provisional resistance used in the interim is non-canonical
  scaffolding to be discarded when S-6 locks. Same-Skill and flat-check options rejected.
  No residual Advantage/Margin/state carries from the first contest. Status: Ruled.
- **DEC-027 (Q-S3-5) — Effect application, auto vs contested.** **RULED — Auto-apply.**
  Winning S-1 with a declared Effect applies it directly; no secondary application contest
  is required. Gate checks (Tag + Location Index where required, DEC-028; fail-and-fall-back
  per DEC-030) remain in force and are evaluated once, post-win. Contested application is
  **rejected as the S-3 default**; S-6 (Defense) may later introduce Tags/equipment that
  counter or prevent specific Effects after auto-apply (e.g., locked gauntlets prevent
  Disarm), and any contested-application mechanic is deferred to S-6 as an optional
  modifier, not an S-3 default. Status: Ruled.
- **DEC-028 (Q-S3-3) — State-3 Effect triggering.** **RULED — Combined Location + Tag
  gating** for the three in-scope S-3 Effects (**Disarm/Break Hold, Equipment Damage,
  Armor Bypass**): trigger requires both a matching gear/ability Tag **and** a supporting
  Zero-Step Location Index (Tier 1+). **Function Impairment and Incapacitation deferred OUT
  of S-3 scope** (Flagged: Incapacitation → S-7; Function Impairment → S-4/Condition).
  Dependencies: Tags subsystem starter vocabulary (§11); anatomical mapping table
  (canonical §14.3, unbuilt); S-2 invocation policy (§2.1A) unaffected. **NARROWED by
  DEC-041 (2026-08-31):** the supporting Location Index must now come from a **Skill-Tier
  ≥ 2 (Advanced) promoting roll** per DEC-041 — the three Effects previously had no
  Skill-Tier qualifier. Recorded as a refinement, not a silent contradiction. Status: Ruled;
  2 concepts deferred out of S-3 (narrowed by DEC-041).
- **DEC-029 (Q-S3-4) — S-3/S-4 boundary.** **RULED — confirmed prototype-only; no S-3/S-4
  interface work needed yet** (base-tier Injury is HP-only, no wound produced). Roadmap §10
  boundary holds, dormant until a wound-producing Effect is proposed. S-4 *direction*
  (location-based injury from repeated hits; no Location Index → no Injury, full stop;
  per-location hit-history by GM adjudication; healing open) recorded as a **steer for a
  future S-4 investigation, not an S-3 ruling, not Canonical**. Status: Ruled; S-4 direction
  non-binding.
- **DEC-030 (Q-S3-3a) — Partial Tag/Location match.** **RULED — Fail-and-fall-back
  (Option A).** On a partial Tag/Location match for any Tag+Location-gated Effect
  (Disarm/Break Hold, Equipment Damage, Armor Bypass), the declared Effect fails entirely;
  the successful S-1 contest instead applies the Base-tier Effect Inflict Injury (HP-only
  form). No residual Advantage, magnitude, duration, or secondary state is generated from
  the partial match. Designer clarification: any further Effect beyond the single free
  Effect from a win requires a **separate opposed roll using an appropriate Advanced
  Skill** — the actor accepts the risk of that additional roll (consistent with, and not
  expanding, DEC-024). Status: Ruled.

**Table-play with this block.** Winner of a successful S-1 contest declares one Effect
(subject to DEC-031's Quality tier gate and DEC-023's menu tiers). Base-tier Effects
(Inflict Injury HP-only; Open Retreat/Compel Yield) are usable now. Gated-tier Effects
unlock with their listed dependency. Effect applies auto (DEC-027), evaluated once,
post-win. Tag+Location-gated Effects additionally need a matching Tag and a supporting
Skill-Tier ≥ 2 Zero-Step Location Index; partial match → full fallback to Base Inflict
Injury (DEC-030). Effects beyond the single free one require a separate opposed roll with
a different domain-appropriate Advanced Skill (DEC-026).

## B.4 S-4 Wound/Injury (DEC-032–DEC-036, DEC-041, DEC-042; DEC-037 → B.2)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md`;
`investigations/tiwas-s4-dec035-original-wording-and-correction-2026-08-30.md`;
`investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md`.

- **DEC-032 — Terminology: Injury vs. Wound.** **RULED — Injury = HP Damage; Wound =
  Localized, Lasting Numerical State.** Wounds are distinct from HP and tracked numerically;
  each individual Wound is functionally equivalent at base. Status: Ruled.
- **DEC-033 — Wound Trigger & Location Scope.** **RULED — Wounds are exclusively triggered
  as a selectable Effect from a successful S-1 contest.** Wound is realized as the
  **"Wounded" Condition**, selected via S-3 Effect #2 (Impose Condition) — not a standalone
  11th menu entry. **Both *Inflict Injury* (Effect #1) and *Impose Condition: Wounded*
  require a Location Index when selected as Effects.** Overflow→HP damage is exempt
  (automatic; no Effect selection). Overflow never causes Wounds. **NARROWED by DEC-041
  (2026-08-31):** the Location Index requirement now also carries a **Skill-Tier ≥ 2
  (Advanced) gate** per DEC-041 — a Location Index (and therefore a Wound) can only be
  produced by a Skill-Tier 2+ promoting roll. Recorded as a refinement, not a silent
  contradiction. Status: Ruled (narrowed by DEC-041).
- **DEC-034 — Track A/B Interaction.** **RULED — Both Track A (Overflow→HP) and Track B
  (Wound Effects) can apply from one hit, sequentially.** Overflow resolves first, then on
  success an Effect is chosen. Status: Ruled.
- **DEC-035 — Wound Severity Definition.** **RULED (CORRECTED — replaces earlier recorded
  "severity = accumulated count").** Wound severity/quality comes from the **S-3 gated
  Effect** that inflicts the wound — a "Serious wound" is a distinct S-3 Effect (e.g.
  Greater Wound such as Serious Frost/Fire/Shock) which **by definition** makes the
  character seriously wounded. It does **not** derive from an accumulated count of wounds.
  A character's ability to *withstand* a wound (adult vs child) is a matter of that
  character's capacity to endure mechanical negatives, not what makes the wound "serious."
  Wounds are tracked individually, each with its own numerical magnitude (e.g. "3 wounds
  −1, 4 wounds −5"; magnitudes may differ per wound, −1/−5/−30/−80/−100). Prior "severity
  = accumulated numerical count" recording was an LLM misreading of the designer's phrase
  "more wounds = more severe" and is superseded. Status: Ruled.
- **DEC-036 — DEC-020 Reopening.** **RULED — DEC-020 (S-2 non-attack deferral) is
  reopened.** Non-attack physical resolutions can produce Wounds via an Effect, provided a
  Location Index can be generated for such scenarios (new mechanism for LI generation
  required — supplied by DEC-037, B.2). Status: Ruled.
- **DEC-041 — Anatomical mapping: Skill-Tier-gated granularity (universal, corrected).**
  **RULED (CORRECTED in-session — supersedes "Wound-only" drafting).** Six-part rule:
  **(1) Gate:** A Location Index is generated only when (a) the roll is promoted to
  Location-Tier 1/2+ per DEC-040/Item 3, **AND** (b) the promoting roll comes from a
  **Skill-Tier 2+ (Advanced) skill**. Base/untrained skills are **Skill-Tier 1** (per
  Canonical §5.1/§5.3) and can **never** trigger a location roll for any
  location-referencing Effect, under any circumstances. **(2) Location-Tier 1 → coarse
  zones** (Head/Torso/Arms/Legs) via **anatomically-weighted numeric ranges**
  (small/awkward zones narrower, large/central wider); "very difficult" = numerically
  harder, not a separate difficulty modifier; granularity does not further vary by
  Skill-Tier at this tier. **(3) Left/right laterality:** Zero-Step output digit-parity =
  odd/left, even/right (interpretive layer; does not alter DEC-014). **(4) Location-Tier 2
  → granularity scales with acting Skill-Tier** (upper/lower then hands/feet then
  fingers/toes); exact tier-to-granularity assignments directional, not locked.
  **(5) Creature coverage:** individual templates per creature type (not a shared scheme);
  content dependency on S-12 (open). **(6) Scope — universal:** the Skill-Tier 2+ gate
  applies uniformly to **all** location-referencing Effects (Wound, Trip, Disarm/Break
  Hold, Equipment Damage, Armor Bypass). **Narrows DEC-033** (adds Skill-Tier ≥ 2 gate atop
  "a Location Index exists") **and DEC-028** (adds Skill-Tier ≥ 2 gate to the three
  Tag+Location-gated Effects, which previously had no Skill-Tier qualifier). 'Wound-only'
  scope restriction and its external-element rationale are struck/superseded. Status: Ruled.
- **DEC-042 — Tier-2+ location subdivision procedure and cost.** **RULED — Option B:
  secondary roll, no resource cost.** Tier-2+ subdivision is resolved by a **dedicated
  secondary roll** (e.g. d10/d6), separate from the original Zero-Step-derived number, with
  **no resource cost** (no Energy/MP spend). It is **explicitly not a second Core Test** —
  no independent Cost, Failure XP, or Double-eligibility (scoping required to stay clear of
  Invariant 18, D1 §16/DEC-016; to be stated explicitly in formal rule text). The acting
  skill's Tier still sets the reachable sub-zone menu (per DEC-041); the secondary roll
  resolves within that menu. Left/right laterality via Zero-Step odd/even digit parity
  carries over unchanged. **Location-mismatch** (secondary roll yields a zone the declared
  Effect can't use) is resolved by existing precedent **DEC-030** (fail-and-fall-back to
  Base Inflict Injury, HP-only); no GM-intervention mechanism introduced. Option A (derive
  subdivision from the same original roll, incl. a player-choice/skill-modifier mechanic)
  was explored, found to conflict with DEC-014 §14.2 ("no player choice"), and **explicitly
  revoked this session** — recorded for design history, superseded. Status: Ruled.

**Table-play with this block.** On a successful S-1 contest where the win reader is a
Skill-Tier 2+ promoting roll, selectable location-referencing Effects may draw a Location
Index (Zero-Step, B.2/DEC-037 for non-attack). Tier 1 → coarse zones. Tier 2+ → further
subdivision by a secondary d10/d6, no resource cost, not a Core Test; mismatch → fall back
to Base Inflict Injury (HP-only). Wounds are the "Wounded" Condition via Impose Condition;
Overflow never inflicts a Wound; Track A and Track B resolve sequentially from one hit.
Greater Wound Effects (e.g. Serious Frost/Fire/Shock) are distinct, gated-by-Quality
Effects (DEC-031). Wound *consequences* (individual attribute penalties, healing-cost
scaling) are OPEN-007 material — listed in Part C, **not** table-ready.

## B.5 S-5 Armor (DEC-058–DEC-062)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` (recorded as
DEC-058–DEC-062 in the live register).

- **DEC-058 (S5-A) — Armor architecture: Tags/Traits only.** **RULED — Armor is a
  Tags/Traits system only.** No numeric durability/soak pool. Structurally identical in
  kind to item Tags generally, applied to defensive gear. Never interacts with Overflow.
  Confirms the existing Recommendation-level "Traits/Tags" note as the actual ruling. Does
  not invoke the Invariant 17 exception (no new resource economy created). **Corollary
  cross-reference:** as a consequence of S5-A + DEC-007 amendment (Overflow immutability),
  Armor Tags never modify Overflow under any circumstance (Item B corollary; no separate
  DEC needed). Status: Ruled.
- **DEC-059 (S5-B) — Bypass definition (consolidated with post-hoc amendment).**
  **RULED — Bypass = a relational property between specific Tag pairs.** An Armor Tag's
  rule text may specify it does not trigger against Effects carrying a designated other
  Tag. Requires **both** a Tag-pairing match **and** a location match (amended after
  S5-E). Stateless; neither Tag is altered. **Inapplicable at Location Tier 0** (no tracked
  location context exists to satisfy the location-match condition). Status: Ruled.
- **DEC-060 (S5-C) — Sunder Effect (addition model).** **RULED — Sunder: (C1) exists;
  (C2) Addition model** — an Impose Condition Effect adding a "Sundered" Tag to the armor
  item (does not remove/delete any existing Tag); (C3) **permanent** — persists until
  deliberately addressed, no automatic reversion; (C4) resolved via the **ordinary Core
  Test Transaction** (DEC-006, 9-step) — Sunder is the outcome/payload of a qualifying
  skill roll, not a new resolution mechanism. Additionally: Sunder is a **selectable**
  Effect (actor chooses it from among available options on a qualifying roll). **Menu
  placement:** Condition tier of the S-3 Effect menu (open to additions, per Dizzy
  precedent), gated on Conditions subsystem (§10) lock — confirmed against live S-3 record,
  no conflict found. Status: Ruled.
- **DEC-061 (S5-D) — Armor resolution sequence vs. Active Defense (consolidated with
  amendment/supersession).** **RULED — Armor resolves before Active Defense.** Sequence:
  Effect auto-applies (DEC-027) → checked against Armor Tags (including Bypass relational
  matching) → surviving Effect magnitude/state then subject to Active Defense mitigation
  (Model B, DEC-048) as a separate pass, consistent with DEC-049 (separate mitigation per
  Effect). **Final operative rule per S5-E supersession:** the intermediate amendment
  ("Tier-0 location hits can never bypass") is fully superseded by the Zero-Step clause
  under S5-E — an Armor check is location-bound but uses the single-purpose Zero-Step read
  at Tier 0, so Tier promotion is never forced by Armor's presence alone, and Tier 0
  remains reachable. Status: Ruled.
- **DEC-062 (S5-E) — Armor coverage location-bound + Zero-Step clause (consolidated with
  amendment).** **RULED — (E1) Armor coverage is location-bound** — a given Armor Tag
  protects only specified location(s), not the whole target uniformly. (E2) Armor uses the
  **same fine-grained individual-creature-template anatomy** as DEC-041 — full reuse, no
  separate coarser coverage-zone system. **Amendment (Zero-Step Armor-location clause):**
  when an attack roll against an Armor-wearing target is resolved at Location Tier 0, the
  struck location for **Armor-coverage-check purposes only** is derived via the existing
  DEC-014 Zero-Step digit-exchange procedure — read-only, off the natural roll already
  made, no new roll, no player choice, does not promote Tier, does not persist, discarded
  immediately after the Armor check resolves. Preserves DEC-040's Tier-0-as-default intact;
  Armor's presence never forces Tier promotion. Bypass remains inapplicable under this path
  (its location-match condition requires tracked Tier 1/2 context). Status: Ruled.

> **S5-C Sunder menu-placement caveat — verbatim from the source handoff
> (`investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md`, §4 Item C):**
>
> "**Item C — S-3 Effect menu placement for Sunder (see S5-C row above).** Requires
> OpenCode's live-repository confirmation before Sunder's menu placement is treated as
> finalized. This is the single open item blocking full closure of S5-C."
>
> **Compiler's cross-reference (not a ruling):** this caveat was *pending confirmation at
> the time of the S-5 handoff*. Per the live register, DEC-060 now records the placement as
> **confirmed by OpenCode against live record DEC-023 /**
> `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`, and the S-6/S-12
> handoff (`investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` §4) records the
> "pending" status as stale. The caveat is preserved verbatim above for the record; the
> operative menu placement is the DEC-060 record.

**Table-play with this block.** An auto-applied Effect is first checked against Armor Tags
(Tag-pair match + location match for Bypass); the surviving magnitude/state then faces
Active Defense mitigation (B.6). Armor coverage is location-bound per the DEC-041 anatomy.
At Tier 0, struck location for the Armor check comes from the single-purpose Zero-Step read.
Bypass cannot trigger at Tier 0. Sunder adds a permanent "Sundered" Tag to the armor item
via a qualifying Core Test, no Tag removal.

## B.6 S-6 Defense (DEC-044–DEC-050)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-s6-defense-opening-brief-2026-08-31.md` §1a (recorded as
DEC-044–DEC-050 in the live register); OPEN-009 resolution via DEC-050 amendment recorded
per `investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` §3.1.

- **DEC-044 (Fork 3) — Defense architecture.** **RULED — Active Defense.** The defender
  makes a genuine Core Test in response to the incoming Effect: full PE/MP cost, full Core
  Test consequences (DEC-006/007). Passive Defense, contest-participant, and
  resource-costed-reaction are no longer live candidates. Status: Ruled.
- **DEC-045 (Fork 4) — Who makes the Defense roll.** **RULED — The defender rolls.** The
  Active Defense roll is made by the defender (gives defensive agency; avoids a second
  attacker roll). Status: Ruled.
- **DEC-046 (Fork 5) — Voluntary decline of Defense.** **RULED — Yes.** The defender may
  choose not to defend and accept the incoming Effect as applied. Confirms the candidate
  previously labeled S-6.2. Status: Ruled.
- **DEC-047 (Fork 7) — Defense roll ceiling.** **RULED — Uncapped.** No per-action limit on
  Defender Defense rolls. Follow-up (deferred, unscoped): whether repeated Defense rolls
  within a scene/encounter should trigger fatigue/exhaustion consequences — no such system
  exists anywhere in the game, so cannot be scoped until/unless one is designed.
  Non-blocking. Status: Ruled. (The follow-up was later closed by DEC-075 — see Part C.)
- **DEC-048 (Fork 2) — Defense timing vs. DEC-027 auto-apply.** **RULED — Model B
  (preserve DEC-027 literally).** The Effect auto-applies exactly as DEC-027 rules; the
  Active Defense roll acts as **post-hoc mitigation on the already-applied Effect**, not
  as a gate preventing application. DEC-027 is not contradicted or reinterpreted (Effect
  genuinely auto-applies in every case; Defense only affects its aftermath/magnitude).
  Model A/hybrid alternatives no longer live. Status: Ruled.
- **DEC-049 (Fork 6) — DEC-026 deferred defensive position.** **RULED — Separate mitigation
  per Effect.** Each Effect (the primary Effect and any DEC-026 second Effect) receives its
  own **independent Active Defense mitigation roll**, rather than one Defense roll covering
  the combined outcome. Consistent with Model B (DEC-048); each auto-applied Effect is
  independently mitigable. A single exchange producing two Effects can generate two Defense
  rolls. Status: Ruled.
- **DEC-050 (Fork 1) — Defensible-Effect scope (AMENDED 2026-09-01 — resolves OPEN-009
  follow-up).** **RULED — Universal eligibility.** Any Effect that successfully auto-applies
  is eligible for Active Defense mitigation — **no enumerated/gated list of "defensible"
  Effects** is maintained. Reasons: (1) player agency; (2) S-3 Effect menu is currently
  undefined, so an enumerated list is not buildable; (3) the Effect menu includes positive
  Effects, not only negative ones. **AMENDMENT (2026-09-01, closes the OPEN-009
  follow-up):** Active Defense may target **any and all** auto-applied Effects, **including
  positive/beneficial Effects** — no coherence/desirability carve-out exists for positive
  Effects. Invocation remains a **voluntary player choice**, never automatic, never
  mandatory. Recorded as an amendment extending/confirming DEC-050's scope (per the
  DEC-007.A amendment precedent), not an independent mechanic. The still-unenumerated S-3
  gated-tier Effect *content* (Position/Condition/Equipment/Defense/Location) remains a
  separate tracking item and is not resolved by this amendment. Status: Ruled (amended,
  resolves OPEN-009).

**Table-play with this block.** Any auto-applied Effect (positive or negative) may be
mitigated by the defender via a voluntary, uncapped Active Defense roll — a genuine Core
Test (full Cost/Overflow/Failure XP/Double/Recovery consequences). Defense is post-hoc
mitigation; it never gates application. Each Effect gets its own Defense roll. The
Defender may decline.

## B.7 S-7 Incapacitation/Death (DEC-052–DEC-057)

> **PAY ATTENTION — Source-handoff status:** source handoff is **DRAFT pending Tiwa
> reconfirmation** (`investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md`);
> **DEC entries are the operative register content**
> (`_consolidation/decision-register.md`). The register records these as Ruled
> (non-canonical); the handoff is a draft working record and must not be read as more
> settled than the register.

**Status tag:** **Non-canonical designer ruling** — Ruled (recorded in the live register,
2026-09-01; confirmed by Tiwa to OpenCode).

- **DEC-052 (Fork 1) — HP = 0 forced incapacitation.** **RULED — HP = 0 triggers forced
  incapacitation.** No roll, no save/check. This replaces the prior directional "HP = 0
  should not automatically mean death" (Proposals/WIP §7) with a specific mechanic: HP = 0
  = incapacitated (not dead, but forced down). Status: Ruled.
- **DEC-053 (Fork 2) — Wound/Incapacitation independence.** **RULED — Incapacitation is
  HP-driven only.** Wound severity (DEC-035) does not feed into incapacitation.
  Incapacitation and Wounds are fully independent systems. The prior Proposals/WIP §7 line
  "serious localized injury may matter where locations are active" is superseded by this
  ruling. Status: Ruled.
- **DEC-054 (Fork 3) — Permanent character loss (death).** **RULED — Two-branch
  permanent-loss condition.** Permanent character loss (death) occurs when EITHER:
  (a) character is incapacitated AND all attempts to revive via skill tests have failed
  (unlimited attempts; no cap), OR (b) player voluntarily chooses permanent loss while
  incapacitated. Status: Ruled.
- **DEC-055 (Fork 4) — Stabilization procedure.** **RULED — GM discretion, no formal
  procedure.** The stabilization procedure around skill-test-based revival attempts is left
  to GM discretion (which skill, how many attempts, pacing). GM discretion governs the
  mechanics of the skill-test attempts, NOT whether skill tests are used at all — that is
  fixed by DEC-054 (Fork 3). Status: Ruled.
- **DEC-056 (Fork 5) — S-11 boundary.** **RULED — No interaction with S-11 (Rest/Healing).**
  Incapacitation is HP-driven; it does not affect healing/recovery mechanics. S-11 remains
  independent. Status: Ruled.
- **DEC-057 (Fork 6) — S-2 non-attack reopening trigger closure.** **RULED (session-level
  assessment) — S-2 non-attack deferral reopening trigger assessed as removed.** The
  original flag arose from Proposals/WIP §7's "serious localized injury may matter where
  locations are active." Under the Fork 2 ruling (DEC-053, HP-only incapacitation),
  incapacitation has a single trigger (HP = 0) with no Wound/location dependency, so the
  original §7 line is superseded and the reopening pathway no longer exists. This is a
  session-level assessment, not a formal re-verification of DEC-037. Status: Ruled
  (session-level assessment).

**Table-play with this block.** HP = 0 → forced incapacitation, no roll. Incapacitation is
HP-driven only (Wounds independent). Permanent loss only by: all revival skill-tests
failed (unlimited attempts, no cap), or voluntary player choice. Stabilization procedure,
which skill, attempt count and pacing are all GM discretion. No interaction with S-11.

## B.8 S-8 Difficulty and third-party adjudication (DEC-043, DEC-051-rejected, DEC-063–DEC-066)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary sources:
`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` §3.1
(DEC-063–DEC-066); `investigations/tiwas-s8-third-party-adjudication-mutual-failure-candidate-v1.md`
(DEC-043); `investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md` (DEC-051).
The S-8 Stakes Gate proposal (Proposals/WIP §8) is **rejected** — see DEC-051 below.

- **DEC-043 — Third-Party Adjudication of Mutual-Failure Opposed Contests (Q1–Q5).**
  **RULED — all five sub-questions closed.** **Q1** Default adjudication skill = the
  **same skill** used by the two contestants in the original opposed contest; fallback if
  the adjudicator lacks it = GM/table discretion choosing a domain-appropriate substitute
  (consistent with DEC-026 precedent). **Adjudication-roll mechanics (precondition):** a
  **full, ordinary Core Test** — normal Cost (natural roll), Overflow→HP, Failure XP on
  failure, standard Recovery, full Double-eligibility, no exemptions. **Q2** Outcome is
  **binary** — adjudicator success/failure alone decides; Quality plays no role. **Q3**
  **Inverted comparison** — on adjudicator success the contestant with the **lower** Failure
  Margin (`Roll − Skill`) wins; on adjudicator **failure** this inverts and the **higher
  (worse)** Failure Margin wins. **Q4** A failed Double on the adjudicator's own roll **does**
  unlock Advanced Skill creation, as a direct corollary of the full-ordinary-Core-Test
  ruling (no exemption stated; answer by consequence, not separately negotiated).
  **Q5** **Generalized to all mutual-failure opposed contests**, not scoped to crafting
  (crafting was the illustrative example only). Reuses existing primitives (Margin, d100
  roll-under, full Core Test); no new roll type. Status: Ruled.
- **DEC-051 — S-8 Stakes Gate rejection.** **RULED — Rejected.** No pre-Core-Test "skip the
  roll" filter will exist for stakes-based reasons. Rationale: rolls are intended to be
  meaningful and to carry risk/reward; a Stakes Gate reduces roll frequency at the cost of
  player opportunities the system is designed to preserve. Proposals/WIP §8 Stakes Gate
  entry superseded. Roadmap Phase 6 scope narrowed (Stakes Gate struck). The S-2 non-attack
  deferral reopening trigger previously flagged on S-8/Stakes Gate (DEC-037 non-blocking
  flag) is removed by this rejection. Difficulty grades and Skill-side modification remain
  open S-8 work — **since ruled by DEC-063–DEC-066 below**. Status: Ruled (rejected).
- **DEC-063 (S8-A) — Difficulty grade structure.** **RULED — Named tiers with fixed additive
  Skill-side modifiers.** Difficulty grade structure = named tiers (e.g.,
  Trivial/Easy/Standard/Hard/Extreme) with fixed additive modifiers to effective Skill.
  Modifiers act on the Skill side of a comparison only — never on the natural die roll
  (Invariant 6/Invariant 1 preserved). Status: Ruled.
- **DEC-064 (S8-B) — Difficulty-modified Skill usage scope.** **RULED — Effective Skill used
  for all three Skill-side values.** The difficulty-modified (effective) Skill is used for:
  (1) the success/fail check, (2) Failure XP calculation, AND (3) as the comparison value
  entering the Skill Roll Pool cascade. Supports advancement past Skill 100;
  high-risk/high-reward design intent. **Interacts with DEC-065 (S8-C) — must be recorded
  together to preserve Invariant 10.** Status: Ruled.
- **DEC-065 (S8-C) — Skill Roll Pool cascade cap (supersedes revoked C1 selection).**
  **RULED — Effective Skill CLAMPED at permanent Cap for cascade stopping condition.** The
  cascade cannot push a character's permanent Skill above their normal Cap, regardless of
  difficulty bonus. Any Pool XP beyond what the cascade can spend before hitting Cap spills
  into General XP (DEC-011) as normal. **Preserves Invariant 10 exactly as currently
  worded; no Invariant-level amendment required for S-8.** An earlier C1 selection was made
  and explicitly revoked by Tiwa mid-session after a clarifying discussion; only C2 is
  operative. Status: Ruled.
- **DEC-066 (S8-D) — Difficulty grade symmetry.** **RULED — Symmetric grades.** Difficulty
  grades apply symmetrically — both bonuses (easier tests) and penalties (harder tests) —
  rather than penalty-only. Status: Ruled.

**Table-play with this block.** Apply the named difficulty tier's fixed additive modifier
to the **effective Skill** (Skill side only — never the die). Effective Skill drives the
success/fail check, Failure XP, and the Skill Roll Pool cascade entry; the cascade clamp is
the permanent Cap, remainder spilling to General XP. Grades are symmetric. Mutual-failure
opposed contests adjudicate per DEC-043. No Stakes Gate exists (DEC-051).

## B.9 S-9/S-10 Extended Tests (DEC-067–DEC-070)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` §3.2. (DEC-039,
Final-roll-governs for Location Index provenance in Extended Tests, is at **B.2**.)

- **DEC-067 (S9-A) — Extended Test progress method.** **RULED — Margin-accumulation.**
  Interval progress toward completing an Extended Test accumulates via Margin-accumulation:
  each successful interval's Margin (Skill − Roll) adds to a running total; failures
  contribute nothing. Monotonically increasing; never decreases. Status: Ruled.
- **DEC-068 (S9-B) — Extended Test failure behavior.** **RULED — Neutral.** A failed
  interval is neutral with respect to progress — it costs resources and generates ordinary
  Failure XP per DEC-006/007/009, but does not reduce or reset the accumulated progress
  total. Combined with DEC-067 (A2): monotonically-increasing, never-decreasing Margin
  total. Status: Ruled.
- **DEC-069 (S9-C) — Extended Test Invariant-17 coherence assessment.** **ASSESSED — No
  Invariant-17 violation.** The DEC-067 + DEC-068 combination (a monotonically-increasing,
  never-decreasing Margin total) has no income/expenditure ("spending") dynamic and cannot
  be mistaken for a competing resource pool. No explicit Invariant-17 non-violation note
  required. Assessment covers A2+B1 combination only; does not generalize to other B-fork
  choices. Authority: **Architectural constraint (assessment)** — not itself a numeric
  mechanic. Status: Ruled.
- **DEC-070 (S-9/S-10) — Extended Test completion target.** **RULED — GM discretion, no
  formula.** The numeric target a Margin-accumulation total must reach to complete an
  Extended Test is set entirely at GM discretion, per-instance, with no formula and no
  fixed default. Precedent: DEC-055 (same "GM discretion, no formal procedure" pattern).
  Status: Ruled.

**Table-play with this block.** Each interval is an ordinary Core Test (Cost = Roll,
Overflow→HP, Failure XP, Double eligibility, Recovery). Successful intervals add Margin
(Skill − Roll) to a running total; failures add nothing and never reduce/reset the total.
No Progress currency is created (Invariant 17). Completion target: GM discretion,
per-instance.

## B.10 S-11 Rest/Healing (DEC-071–DEC-074)

> **PAY ATTENTION — Source-handoff status:** source handoff is **DRAFT pending Tiwa
> reconfirmation** (`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md`);
> **DEC entries are the operative register content**
> (`_consolidation/decision-register.md`). The register records these as Ruled
> (non-canonical); the handoff is a draft working record and must not be read as more
> settled than the register.

**Status tag:** **Non-canonical designer ruling** — Ruled (recorded in the live register,
2026-09-01; confirmed by Tiwa to OpenCode).

- **DEC-071 (S11-A) — Rest/Healing resolution method.** **RULED — Explicit Skill Test
  required.** Healing during a Rest period requires an explicit Skill Test (a full,
  ordinary 9-step Core Test per DEC-006) — not a passive/automatic HP restoration.
  Status: Ruled.
- **DEC-072 (S11-B) — Wound magnitude healing penalty.** **RULED — Penalty on healer's
  effective Skill.** Wound magnitude penalizes the healer's EFFECTIVE Skill for the healing
  test — the same mechanism pattern as DEC-064 (S8-B) difficulty-on-Skill-side approach —
  rather than altering the natural roll, the resource Cost, or the HP amount restored
  directly. Cross-subsystem consistency with S-8. Status: Ruled.
- **DEC-073 (S11-C) — S-11 as literal Extended Test instance.** **RULED — S-11 healing IS
  an Extended Test instance.** S-11 Rest/Healing is treated as a literal instance of the
  S-9/S-10 Extended Test subsystem: one Rest period = one Extended Test interval; each
  interval is an ordinary Core Test with DEC-072's wound-magnitude Skill penalty applied;
  progress accumulates via DEC-067's Margin-accumulation (A2); failures are neutral per
  DEC-068 (B1); and the completion target follows the same general GM-discretion rule as
  DEC-070, with no S-11-specific override. Tiwa's own proposal, adopted after two prior
  framings were rejected as unclear. Status: Ruled.
- **DEC-074 — S-11 healing completion target.** **RULED — GM discretion, generally — no
  HP-deficit lock.** For healing specifically, the completion target remains general GM
  discretion — same as the base DEC-070 rule — and is NOT locked to "HP deficit" as a
  required or default target, even though HP deficit is an obvious candidate a GM might
  reach for. Status: Ruled.

**Table-play with this block.** A Rest period's healing is resolved as an Extended Test:
each interval is an ordinary Core Test; wound magnitude penalizes the healer's effective
Skill; progress accumulates Margin (Skill − Roll), failures neutral; completion target at
GM discretion (no HP-deficit lock).

---

# Part C — Explicitly NOT table-ready

This section lists, in full, the material that is **not** table-ready. No mechanics for
these items are included by design — listing them here ensures nothing Open is silently
included as if settled, and nothing confirmed-closed is re-opened or omitted.

## C.1 S-12 — Creature/Campaign content — **Open** (not table-ready)

- Creature/npc content is a content-authoring track, not a settled mechanic.
- Ruled and recorded in the live register (both **Non-canonical designer ruling**):
  - **DEC-076 (S-12 Ruling A) — dual-mode fork:** computerized/automated systems use full
    24-attribute generation identical to player characters with the same Core Test economy;
    non-automated (tabletop/GM-run) systems use an abbreviated/simplified stat-block method
    with resolution **defaulting to GM decision on system** (no system-authored alternate
    mechanism; the superseded draft phrase "GM-facing shortcut layer" must not appear).
  - **DEC-077 (S-12 Ruling B) — content authoring path:** actual creature/campaign template
    instances (e.g. Goblin, Dragon), using DEC-041's individual-template method, are
    developed by Tiwa via playtesting; not drafted by any advisory model.
- These DECs are recorded for pointer purposes only. No stat blocks, templates, or
  creature mechanics are provided here. (Sources:
  `investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` §3.3; `decision-register.md`.)

## C.2 OPEN-005, OPEN-009, OPEN-010 — not table-ready

- **OPEN-005** (S-5…S-12 umbrella): listed here because it was carried in the compilation
  brief as "the only reason still open: S-12". **Compiler's read-only observation:** the
  live register (last modified 2026-09-01) records OPEN-005 as **CLOSED via DEC-076 /
  DEC-077** (S-12's sole mechanical dependency satisfied; remainder is ordinary content
  authoring), with Tiwa's confirmations documented in
  `investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` §7. No fork-level open item
  remains under OPEN-005. This file neither re-opens nor re-closes it; it records the live
  register status. No mechanics included.
- **OPEN-009** (S-6 positive-Effect Active Defense mitigation): listed here so it is not
  mistaken for table-ready. Live register status: **CLOSED via the DEC-050 amendment
  (2026-09-01)** — Active Defense may target any and all auto-applied Effects including
  positive ones; invocation remains voluntary. No mechanics included here (see DEC-050 in
  Part B.6 for the operative text).
- **OPEN-010** (S-6 repeated-Defense fatigue/exhaustion): listed here so it is not mistaken
  for table-ready. Live register status: **CLOSED via DEC-075 (2026-09-01)** — repeated
  Active Defense rolls carry no fatigue/exhaustion penalty beyond the existing Cost/Overflow
  economy (DEC-006/007); no separate fatigue system is created. Designer note: future
  fatigue, if ever implemented, would be a selectable Condition-tier Effect (per the
  DEC-060 Sunder addition-model precedent), not a subsystem. No mechanics included here.

## C.3 S-3 gated-tier Effect *contents* beyond menu structure — not table-ready

- The S-3 menu **structure** is Ruled (DEC-023, Part B.3). The **contents within the gated
  tiers** — the specific Effects populating the Position, Condition, Equipment, Defense, and
  Location tiers — are **not fully enumerated** and remain a separate open tracking item.
  They are referenced (not resolved) by DEC-050's amendment note (B.6) and DEC-075's
  fatigue note. No mechanics for the unenumerated gated-tier contents are included here.

## C.4 §3.9 "confirmed-closed" items (from the task-scoped snapshot of 2026-09-01)

These resolve questions that must not be treated as open. They are listed here so they are
neither re-opened nor omitted. No mechanics for these items are reproduced in this section
(where a resolving DEC is table-ready material within Part B, the pointer is given):

| Item | Resolved by | The table-ready material, if any, lives at |
|---|---|---|
| OPEN-001 (H0 Rider B causal attribution) | DEC-038 — single causal-attribution principle: the governing Core Test for Location Index generation is whichever Core Test is causally responsible for the physical consequence | (not a Part B block; pointer: `decision-register.md` DEC-038) |
| OPEN-002 (scene/campaign Location Tier selection) | DEC-040 — Tier 0 universal default; promotion per-roll only | (not a Part B block; referenced by DEC-041/DEC-062 verbatim text; pointer: `decision-register.md` DEC-040) |
| OPEN-003 (anatomical mapping) | DEC-041 — Skill-Tier-gated granularity, universal | Part B.4 (DEC-041) |
| OPEN-004 (Tier-2 procedure/cost) | DEC-042 — Option B secondary roll, no cost | Part B.4 (DEC-042) |
| OPEN-006 (wound-severity "thresholds") | DEC-035 (corrected) — severity from the S-3 gated Effect, not an accumulated count | Part B.4 (DEC-035) |
| OPEN-007 (wound consequences) | Ruled (2026-08-30) — individual mechanical attribute penalties; magnitudes may differ (e.g. −1, −5, −30, −80, −100); more/severe wounds → more negatives; too many → "game overed" (faster for weaker characters); healing cost scales with magnitude | **Not table-ready** — pointer: `decision-register.md` §C OPEN-007 |
| OPEN-008 (non-attack Location Index generation) | DEC-037 — governing failed-roll provenance + passive-stub fallback | Part B.2 (DEC-037) |

---

# Part D — Playtest Report Template

**How to use.** Copy the capture table per alpha session. For each subsystem row mark
whether the system was exercised in that session, whether it worked as intended, add any
table-level observations, and record a recommendation. The recommendation is a data marker
(Keep as-is / Needs Tiwa review / Flag for reopening) — filling it out does **not** rule on
anything; assessment happens during/after play and any actual reopening decision is Tiwa's
via the established governance path.

**Example entry (illustrative only — not a real log):**

| System | Exercised in session? (Y/N) | Worked as intended (Y/N/Partial) | Notes | Recommend |
|---|---|---|---|---|
| S-1 Opposed Contest | Y | Partial | Margin/Blackjack both rolled; Hybrid not needed this session | Needs Tiwa review |

**Capture table — session date:** ____________

| System | Exercised in session? (Y/N) | Worked as intended (Y/N/Partial) | Notes | Recommend: Keep as-is / Needs Tiwa review / Flag for reopening |
|---|---|---|---|---|
| S-1 Opposed Contest (DEC-013 + DEC-031 Quality tie-breaker) | | | | |
| S-2 Zero-Step Location Index subsystem (DEC-014, DEC-037, DEC-039) | | | | |
| S-3 Effect menu / gating (DEC-023–DEC-030) | | | | |
| S-4 Wound/Injury (DEC-032–DEC-037, DEC-041, DEC-042) | | | | |
| S-5 Armor (DEC-058–DEC-062) | | | | |
| S-6 Defense (DEC-044–DEC-050) | | | | |
| S-7 Incapacitation/Death (DEC-052–DEC-057) | | | | |
| S-8 Difficulty & 3rd-party adjudication (DEC-063–DEC-066, DEC-043, DEC-051-rejected) | | | | |
| S-9/S-10 Extended Tests (DEC-067–DEC-070) | | | | |
| S-11 Rest/Healing (DEC-071–DEC-074) | | | | |

---

# Appendix — Source pointers (pointer-reference only)

This corpus is compiled from the live repository at 2026-09-01. Authoritative sources,
from which every rule above is drawn verbatim (no raw merge trail, survey transcripts, or
hash-indexed evidence items are included inline):

- `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` — D1, Core Locked Rules
  (Part A: DEC-001–DEC-016).
- `_consolidation/decision-register.md` — the live decision register (Sections A–D).
- `_consolidation/requirement-register.md` — REQ-001–REQ-025 (incl. REQ-021 Promotion Rule).
- `governance/authority.md`, `governance/status-model.md`, `governance/provenance.md`.
- `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` — DEC-023–DEC-030.
- `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md` — DEC-032–DEC-037.
- `investigations/tiwas-s4-dec035-original-wording-and-correction-2026-08-30.md` — DEC-035.
- `investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md` — DEC-037 verification.
- `investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` — DEC-058–DEC-062,
  DEC-007.A wording, S5-C caveat.
- `investigations/tiwas-s6-defense-opening-brief-2026-08-31.md` — DEC-044–DEC-050.
- `investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` — DEC-050 amendment,
  DEC-075–DEC-077, OPEN-005/009/010 closure confirmations.
- `investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md` — DRAFT source for
  DEC-051–DEC-057 (DEC entries operative).
- `investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` — DRAFT source
  for DEC-063–DEC-074 (DEC entries operative).
- `investigations/tiwas-s8-third-party-adjudication-mutual-failure-candidate-v1.md` — DEC-043.
- `Tiwas-Task-Scoped-Snapshot-for-Claude-2026-09-01-v2.md` — §3.9 confirmed-closed list;
  compilation-brief reference only (the live register supersedes its wording).

**One-off notice (as required by the standing-prohibition overrule):** this file is a
dated, one-off, scoped exception for GM table use during alpha playtesting only
(2026-09-01). It is NOT to be periodically regenerated, and it does not lift the standing
"no single merged file" prohibition for any future task.