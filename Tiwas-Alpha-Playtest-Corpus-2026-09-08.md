---
document:
  title: "Tiwas — Alpha-Playtest Corpus (One-Off, GM Table-Ready)"
  version: "1.0"
  status: "One-off, dated, scoped exception (see Standing-Prohibition Overrule below). NOT canonical. NOT a standing merge artifact. Does not rule, promote, or lock anything."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-08"
  last_modified_date: "2026-09-08"
---

# Tiwas — Alpha-Playtest Corpus (One-Off, GM Table-Ready)

## Standing-prohibition overrule — required log entry (inserted verbatim, dated)

Tiwa has explicitly and consciously overridden the standing "do not create another
single merged file" prohibition, for this one alpha-playtest corpus only. This file
is a dated, one-off, scoped exception for GM table use during alpha playtesting.
It is NOT a reinstatement of any standing merge artifact, is NOT to be periodically
regenerated, and future agents must NOT assume this prohibition is generally lifted.
Scoped per Tiwa's direct instruction as human designer/ruling authority, **2026-09-08**.

---

## How to use this file

- **What this file is.** A single-file, table-ready assembly of every system currently
  Ruled or Locked in the live repository, compiled 2026-09-08 from the live register
  (`_consolidation/decision-register.md`, through DEC-133), the canonical
  ruleset (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`, internally
  **v1.4**, last modified 2026-09-05), and the cited records in `investigations/`.
  No rule in this file has been reconstructed from memory or from any cached snapshot;
  the live register is authoritative over any earlier wording.
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
- **Register date note.** The register's front matter records `last_modified_date:
  "2026-09-07"`, while DEC-133 (ruled 2026-09-08) is recorded in the register body.
  Both dates are preserved: this corpus is compiled from the register body as read on
  2026-09-08.

### Status vocabulary used throughout (per `governance/status-model.md`)

| Label in this file | Meaning |
|---|---|
| **Canonical / Locked** | Authoritative, current, must not be contradicted (D1 self-declared). |
| **Non-canonical designer ruling** | Real human/designer decision about candidate/non-canonical material. Not Canonical. |
| **Draft pending Tiwa reconfirmation** | The cited handoff file is a draft; the live DEC entry is the operative register content. |
| **Open** | No settled decision exists. Not table-ready. |
| **Confirmed-closed** | Resolved via the named DEC/ruling; listed in Part C so it is neither re-opened nor omitted. |

---

# Part A — Core Locked Rules (D1): DEC-001–DEC-017

Source: `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` (D1, internally
**v1.4** — version bump 2026-09-05 adds §14.7 via DEC-017), transcribed without
compression. All formulas, the 9-step Core Test Transaction, and all 18 Invariants
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
change to Locked material.
**Corollary:** consequence of this + DEC-058 (S5-A) = Armor Tags never modify Overflow.
Tag/Condition architecture (DEC-079/DEC-080) is constrained to never touch Overflow.

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

**Invocation layer — PART A.** §14.7 (DEC-017, 2026-09-05) governs *when* a Location Index
is warranted on the attack side. See **A.17** below. §14.7 is an invocation layer around the
Zero-Step transformation; it does not modify Zero-Step itself.

**E9 human usability playtest record** (evidence class: empirical finding — passed for the
tested physical two-d10 method only): the E9 playtest used two physical d10s with 50
participants (25 new to RPGs, 25 RPG players new to Tiwas). Participants reported no
difficulty rolling the dice or exchanging the digits for hit location; feedback was
positive. Other input methods (single d100, digital roller, verbally announced result)
were not tested and are not covered by this finding.

## A.15 Reserved Systems (DEC-015) — Canonical / Locked (scope statement)

The following remain outside the locked Core unless separately incorporated through formal
governance: hit-location rules (except the Tier-1 Zero-Step provider, §14.1–14.2, and the
attack-side invocation/warrant policy, §14.7); wound activation/severity; Outcome Effects;
armor; active/passive defense; incapacitation; death; healing; Rest; equipment; encumbrance;
conditions; environmental hazards; difficulty grades; task/stakes adjudication; Extended
Tests; NPC construction; magic/special-ability implementation; GM procedure; campaign
procedures; setting-specific content.

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

## A.17 Attack-side invocation — when a Location Index is warranted (DEC-017, §14.7) — Canonical / Locked

**Status: Canonical / Locked — attack-side invocation policy. Established 2026-09-05 by
DEC-017 through the 8-step Promotion Rule.**

For an attack-side resolution, a Tier-1 Location Index is generated **only when all three
gates are satisfied** for one declared attack objective:

| Gate | Requirement |
|---|---|
| W1 — Explicit Objective | The actor explicitly states a distinct consequence beyond ordinary damage |
| W2 — Established Location-Dependence | Current Tiwas design establishes that the stated consequence is delivered through location (not merely plausible or anticipated) |
| W3 — Current Resolvability | Current Tiwas rules provide a mechanism that can act on the resulting Location Index |

`Generate(LocationIndex) = W1 ∧ W2 ∧ W3`. If any gate is false, no Location Index is
generated. The Zero-Step transformation itself remains governed exclusively by §14.1–§14.2
(DEC-014); §14.7 is an invocation layer around that transformation, not a modification of it.

> **GM-facing operational test.** Generate a Location Index only when the actor has
> explicitly stated a distinct outcome beyond ordinary damage, that outcome's
> location-dependence is already established under current Tiwas design (not merely
> plausible or anticipated), and current rules can actually resolve it.

**Warrant test (Named-Outcome Test).** A declared objective is definite — and therefore
Warrant-eligible — if and only if the actor explicitly names a distinct consequence, other
than ordinary damage, whose resolution depends on the specified location. Purpose or
motivation language does not by itself create definiteness; conditional phrasing does not
defeat definiteness; only the presence of a named distinct outcome matters.

**Explicit-only boundary.** The GM does not infer an unstated distinct objective from
location, attack description, fictional context, or cinematic framing alone. Only stated
objectives are Warrant-eligible.

**Procedural riders.**
1. Compound objectives are evaluated disjunctively: if any named branch of a multi-part
   declaration satisfies the Named-Outcome Test, Warrant is established for that branch.
2. Stale objectives void the match: a Warrant is invalid if the fictional state on record
   no longer supports the rationale for the named outcome.
3. S-1 winner-only: in an opposed contest, only the winning participant's natural roll is
   eligible for Location Index generation (per §13.2; Quality never alters either
   participant's historical roll).
4. Lazy evaluation: because Zero-Step is a read-only post-process of an already-recorded
   roll (§14.2), Warrant/resolvability evaluation may be deferred to the point a downstream
   stage first requires the answer.

**Classification architecture.** For documentation and cache maintenance, concepts are
classified: State 1 = Established & Resolvable (generate); State 2 = Established, Not Yet
Resolvable (do not generate; record as pending); State 3 = Outcome Plausible,
Location-Dependence Unresolved (do not generate); State 4 = No Distinct Consequence (do not
generate). This four-state scheme is an internal/documentation architecture used for
cache-content bookkeeping; a GM applying the operational test above need not separately
track it. Cache contents are revisable by later subsystem locks without reopening this
policy.

**Non-attack boundary.** These gates govern attack-side invocation only. Non-attack
Location Index generation is governed separately (DEC-037 chain; the former non-attack
deferral record DEC-020 was formally closed 2026-09-05).

---

# Part B — Ruled non-canonical subsystems (table-ready, fully detailed)

Each block below is tagged **Non-canonical designer ruling** and cited by DEC number and
source path, per the live register (`_consolidation/decision-register.md`). DEC entries are
transcribed from the register's Decision column; where the register is the operative
content, the handoff file is cited as the source pointer. Where a DEC is also a Locked item
reproduced in Part A, the block points to Part A rather than duplicating. Where a ruling
supersedes an earlier ruling, the supersession is recorded verbatim; the later ruling is the
operative content.

## B.1 S-1 Opposed Contest — Quality and the melee-exchange algorithm

- **DEC-013 (S-1 core):** **Canonical / Locked** — full text in **Part A §A.13**.
- **DEC-031 (Quality's Role in Single-Effect Outcome Resolution, Q-S3-6):**
  **RULED — Option B: Quality gates eligible Effects.** Quality (already computed at S-1
  for tie-breaking) determines which Effect tier is selectable. Every winning Quality value
  (≥ 1) guarantees at least one baseline-tier Effect (floor rule). No Effect scaling by
  Quality; no additional Effect granted. **NOTE — DEC-107 (2026-09-05) supersedes the
  numeric-gating role of Quality** for Effect severity: Quality keeps the ≥ 1 floor (as the
  success precondition), the S-1 tie-break, and the guarantee of a baseline Effect; the
  *severe/gated* role Quality previously played is now determined by the causing Skill's
  Tier (see B.4). Source:
  `investigations/llm-quality-s3-reports-2026-08-30.md`. Status: Ruled (altered by DEC-107).
- **DEC-096 (C-01 — Inflict Injury magnitude):** **RULED — Winner's Margin.** `Inflict
  Injury` (Base-tier S-3 Effect) removes target HP equal to the winner's Margin
  `(winner's Skill − natural d100 roll)` from the successful S-1 opposed contest. Preserves
  DEC-023 / DEC-002 / DEC-001 / DEC-007 (Overflow→HP is attacker-side and immutable).
  Status: Ruled.
- **DEC-097 (C-02 — Active Defense mitigation amount):** **RULED — Defender's Margin.**
  A successful Active Defense (DEC-044) reduces the incoming Effect's magnitude by the
  defender's Margin `(defender's Skill − natural d100 roll)` on their Active-Defense Core
  Test; on a failed Defense, mitigation is 0. Status: Ruled.
- **DEC-104 (C-01/C-02 — Inflict Injury contest-delta refinement):** **RULED — Inflict
  Injury (HP) resolution = Winner's Margin − Defender's Margin (contest-delta).** DEC-096
  composed with DEC-097: the winning attacker's Margin minus the (successful) defender's
  Margin is the HP damage; **never 0 on a win**. HP channel fully separate from the DEC-103
  negation table. Status: Ruled.
- **DEC-101 (C-09 — Defender-wins opposed attack):** **RULED — on a defender win in an
  opposed attack contest, the attack simply fails; the defender gains NO counter-Effect.**
  DEC-013's matrix clarified: neither side declares a counter-Effect off that result.
  Status: Ruled. (Coverage verified empirically — DEC-109, B.7.)
- **DEC-105 (Standardized melee-exchange algorithm, resolves OI-103):** **RULED — a melee
  exchange is one S-1 opposed contest (DEC-013); both participants always roll.** Matrix:
  Atk Succ/Def Fail → attacker wins, full Quality, mitigation 0; Atk Fail/Def Succ →
  defender wins, attack fails, no counter-Effect; Both Succ → compare Quality/Margin, higher
  wins, exact tie → repeat (§13.5); Both Fail → repeat (§13.4). Attacker-win channel split:
  Inflict Injury (HP) = contest-delta (DEC-104); Wound/Condition Effects = DEC-103 machinery
  (Skill-Tier shred + margin de-escalation; survivors record natively `Z = −Y`). Effect-tier
  eligibility (DEC-099's Quality ≥1 base / ≥10 gated, as retained by DEC-107) judged on the
  winner's raw, pre-mitigation Quality. Overflow (DEC-007) independent. **Additional
  (second/third/…) Effects:** each is its own separate opposed roll (DEC-024/DEC-026,
  different Advanced Skill) with its own independent AD roll, and only if the Defender
  selects an AD (DEC-050 voluntary). **Voluntary vs mandatory defense:** playtests = defense
  MANDATORY; live play = voluntary, refusal rare but legitimate; **declined defense →
  attacker gets a normal Core Skill Test** (no contest, no comparison, no mitigation;
  unopposed attack does not auto-succeed). Status: Ruled (resolves OI-103).

**Table-play with this block.** One opposed contest per melee exchange; both sides roll.
Higher Quality wins ties; exact tie or double-failure → repeat. HP damage on a win =
`WinnerMargin − DefenderMargin`, never 0. Non-HP Effects go through the DEC-103 mitigation
table (B.4/B.6). Defender wins → attack fails, nothing else. Defense is voluntary in live
play; refused → plain Core Test against the attacker.

## B.2 S-2 Zero-Step Location Index subsystem (attack + non-attack provenance; tier policy)

- **DEC-014 (Zero-Step core):** **Canonical / Locked** — **Part A §A.14**.
- **DEC-017 (§14.7 attack-side invocation; DEC-018/DEC-019 folded in):**
  **Canonical / Locked** — **Part A §A.17**.
- **DEC-037 (S-2 / S-4 Non-Attack Location Index Generation):**
  **RULED — (1) Primary Provenance Rule:** on a failed governing Core Test against an
  environmental hazard/obstacle/physical risk, that failed d100 supplies the digits for
  Zero-Step Tier-1 Location Index generation. **(2) Hazard "Win":** a failed test is a
  "win" for the hazard; if severity qualifies for an S-3 Effect, the applicable Effect
  (Inflict Injury or Impose Condition: Wounded) lands at the location indicated by the
  failed roll. **(3) Systemic Exempt:** Drowning/Suffocation/Extreme Temperature/Poison
  apply direct HP/Conditions without a Location Index. **(4) Passive Fallback:** physical
  impact with no roll → numeric stub Location Index (e.g. `00`/`50`) routed through
  Zero-Step. Status: Ruled.
- **DEC-039 (OPEN-001B — Extended Test governing roll):** **RULED — the final roll in the
  sequence** governs Location Index generation for an Extended Test's physical consequence.
  Status: Ruled.
- **DEC-040 (OPEN-002 — scene/campaign Location-Tier selection):** **RULED — Tier 0 is the
  universal default; promotion is per-roll only.** No scene-level "stays elevated" state.
  Per-Effect Tier-1-vs-Tier-2 assignment resolved 2026-09-06 via DEC-113 (B.4). Status:
  Ruled.
- **DEC-042 (Tier-2+ location subdivision procedure and cost):** **RULED — Option B:
  secondary roll, no resource cost.** Tier-2+ subdivision resolved by a dedicated secondary
  roll (d10/d6), separate from the Zero-Step-derived number, no Energy/MP spend; **explicitly
  not a second Core Test**. Acting skill's Tier sets the reachable sub-zone menu (B.4/DEC-112);
  left/right via Zero-Step odd/even digit parity. Location-mismatch → DEC-030 fail-and-fall-back.
  Status: Ruled.

**Table-play with this block.** Hit locations default OFF (Tier 0). A specific action that
needs location promotes one roll to Tier 1/2 (attack side: only if §14.7's three gates hold).
Tier 1 = coarse zones; Tier 2+ = secondary d10/d6 sub-zone roll, no cost, not a Core Test.

## B.3 S-3 Effect menu, enumeration and gating (DEC-023–DEC-030, DEC-023.A)

**Status tag:** **Non-canonical designer ruling** — all rulings Ruled.

- **DEC-023 (Q-S3-1) — Effect menu structure.** **RULED — Tiered Effect menu**: base tier =
  Inflict Injury (HP-only) + Open Retreat/Compel Yield; five gated tiers (Position →
  Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6; Location →
  S-2 invocation promotion). Disarm/Break Hold via combined Tag+Location gating (DEC-028).
- **DEC-024 (Q-S3-2) — Flat one-Effect-per-win.** A second/additional Effect requires a
  **separate opposed roll** (mechanism — DEC-026).
- **DEC-025 (Q-S3-2a) — Pure declared intent (no Skill-side gating).** Effects granted
  solely by the declared outcome of a successful S-1 contest (subject to the other gates:
  gear/ability Tag + Location Index where required). No formal tag/category system on
  Advanced Skills (**rejected**). Reinforces Canonical §12.3. **(Reopen-check 2026-09-06:
  not reopened by the unified-record-schema rulings — see B.19.)**
- **DEC-026 (Q-S3-2b) — Second-Effect roll uses a different Advanced Skill;** defensive roll
  deferred (now S-6 via DEC-049/DEC-105; each Effect gets its own AD roll).
- **DEC-027 (Q-S3-5) — Auto-apply.** Winning S-1 with a declared Effect applies it directly;
  no secondary application contest. Gate checks evaluated once, post-win.
- **DEC-028 (Q-S3-3) — Combined Location + Tag gating** for Disarm/Break Hold, Equipment
  Damage, Armor Bypass; **NARROWED by DEC-041** (Location Index must come from Skill-Tier ≥ 2
  promoting roll) and **specified 2026-09-06 via DEC-114** (trigger table — B.14).
- **DEC-029 (Q-S3-4) — S-3/S-4 boundary:** prototype-only; base-tier Injury is HP-only.
- **DEC-030 (Q-S3-3a) — Fail-and-fall-back:** on a partial Tag/Location match the declared
  Effect fails entirely; the successful S-1 contest instead applies Base Inflict Injury
  (HP-only). No residual state from the partial match.
- **DEC-023.A (locked alpha enumeration, 2026-09-02):** **RULED — Package 1 Option A: Full
  alpha enumeration.** Policy rulings: (1) candidate lists accepted as first-pass alpha
  content; (2) **ongoing / damage-over-time Effects prohibited** — all HP loss remains
  Base-tier Inflict Injury only; (3) Prone/Grappled/Restrained are **distinct mechanical
  identities**; (4) action-economy Effects resolve as Skill-side or Movement penalty,
  magnitude scaled by Effect Quality; (5) **beneficial Effects in scope** (positive or
  negative). **Locked alpha content by tier:** *Base Tier:* Inflict Injury (HP-only);
  Open Retreat / Compel Yield. *Position Tier:* Forced Movement; Knock Prone; Seize / Deny
  Ground; Pin / Hold Position; Open / Close Lane. *Condition Tier:* Encumbered (DEC-078);
  Grappled; Restrained; Prone; Blinded; Deafened; Frightened; Slowed; Stunned / Incapacitated;
  Fatigued (DEC-075); Sunder — Condition form (DEC-060); Poisoned / Sickened. *Equipment Tier*
  (Tag + Location + Skill-Tier = 2 gating where applicable): Disarm; Break / Sunder Item;
  Armor Bypass; Disable Device / Weapon; Steal / Take Item. *Defense Tier:* Lower Defense;
  Deny Defense; Force Defense; Expose. *Location Tier:* Impose Wound; Critical Location;
  Cripple Limb. **Prohibitions locked:** no DoT/persistent damage; no
  Disarm, Break/Sunder Item, Armor Bypass, Disable Device/Weapon, Steal/Take Item;
  *Defense:* Lower Defense, Deny Defense, Force Defense, Expose; *Location:* Impose Wound,
  Critical Location, Cripple Limb. **Prohibitions locked:** no DoT/persistent damage; no
  Advantage/Disadvantage language; no modification of natural d100 (Invariant 6); no new
  resource pools (Invariant 17); one Effect per win (DEC-024). **Dependency:** Condition-tier
  Effects route through the Conditions subsystem (B.13) — resolved 2026-09-02 via DEC-079.

**Table-play with this block.** Winner of a successful S-1 contest declares one Effect.
Base-tier Effects usable now; gated tiers unlock with their dependency (Tags/Conditions). GM
should read DEC-023.A's full enumeration against the table; the Conditions subsystem (B.13)
currently supplies all Condition-tier entries. Source:
`investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`;
`investigations/tiwas-tag-effect-condition-unification-*` (2026-09-06 series).

## B.4 S-4 Wound/Injury, wound target, and Location granularity

**Status tag:** **Non-canonical designer ruling** — Ruled.

- **DEC-032 — Injury = HP Damage; Wound = Localized, Lasting Numerical State.** Wounds are
  distinct from HP, tracked numerically, functionally equivalent at base.
- **DEC-033 — Wounds exclusively triggered as the selectable "Wounded" Condition** (S-3
  Effect #2). Both Inflict Injury and Impose Condition: Wounded need a Location Index when
  selected as Effects; **Overflow→HP is exempt** (automatic; never causes Wounds).
  **NARROWED by DEC-041** (Skill-Tier ≥ 2 gate).
- **DEC-034 — Track A (Overflow→HP) and Track B (Wound Effects) both apply from one hit,
  sequentially;** Overflow first, then on success an Effect.
- **DEC-035 (severity) — CORRECTED:** severity from the S-3 gated Effect, not an accumulated
  count. **SUPERSEDED for magnitude by DEC-035.A** (below); DEC-035's severity-from-Effect
  principle stands.
- **DEC-035.A (structured wound record; magnitude = tier):** **RULED — format
  `Location X Tier-Y Wound Z (Attribute or Skill)`.** `X` from DEC-037 provenance, Tier-1+
  per DEC-033/DEC-040. Tier `Y` ≤ causing Skill's Skill-Tier, OR **GM Fiat** (independent
  override). **Magnitude Z = −Y** (Tier fixes magnitude; no budget lookup). **Stacking:**
  same-tier + same-location + same-Attribute/Skill wounds stack (values add) but never raise
  the Wound Tier; different tiers at the same location do not stack. **Healing gate:** a
  wound can be healed by a skill with Tier ≥ Wound Tier. **GM Fiat universal** — may override
  the healing gate, the magnitude/tier fixedness, and any tier requirement. Status: Ruled
  (amended by DEC-035.B, superseded in ceiling-part by DEC-107).
- **DEC-035.B (Quality vs Skill-Tier ceiling):** **RULED — Quality was the hard ceiling;
  superseded by DEC-107 (2026-09-05): Quality is no longer a hard ceiling on Wound Tier;
  Skill-Tier (causing skill) is the ceiling. Original text preserved.**
- **DEC-041 (anatomical mapping — Skill-Tier-gated granularity, universal):** six-part ruled
  gate: (1) Location Index only when roll promoted to a Location Tier AND the promoting roll
  is a **Skill-Tier 2+ (Advanced) skill** — Tier-1 base skills can never trigger a location
  roll for any location-referencing Effect; (2) Tier 1 = coarse zones Head/Torso/Arms/Legs,
  anatomically-weighted numeric ranges; (3) left/right via Zero-Step digit parity
  (odd/left, even/right); (4) Tier 2 granularity scales with Skill-Tier (upper/lower → hands/
  feet → fingers/toes) — **resolved into the exact ladder by DEC-112** (below); (5) creature
  coverage = individual templates per creature type; (6) the Skill-Tier 2+ gate is universal
  across all location-referencing Effects (Wound, Trip, Disarm/Break Hold, Equipment Damage,
  Armor Bypass).
- **DEC-100 (C-08 — Location Tier-1 coarse-zone ranges):** **RULED — Quartile split:**
  **1–25 Legs; 26–50 Torso; 51–75 Arms; 76–100 Head.** Supplies DEC-041's numeric ranges.
- **DEC-102 (S-4 Wound target selection — which Attribute or Skill a Wound affects,
  resolves OI-101):** **RULED — (1) Creatures cause Attribute wounds only; Players may cause
  Attribute or Skill wounds (choice). Automated playtest Characters = creatures. Effect-side
  restrictions override. (2) Attribute-wound target = the Body attribute associated with the
  Skill that caused the wound; multiple candidates → creatures/automated pick randomly,
  Player chooses. (3) Mind-only affecting Skills cause Mind attribute wounds. (4) Skill-wound
  target: the skill sharing the most of the same Attributes; from the valid list the **skill
  with the highest numerical value** is affected; on a tie → random (creatures) or Player
  choice. (5) Attribute wounds reduce the base Attribute and **recalculate all derived Skill
  values and HP/MP/Energy Pools** (live recalculation, DEC-004).** Status: Ruled (resolves
  OI-101).
- **DEC-107 (OI-106 — Quality → Wound Tier: Skill-Tier basis; Design Override of
  DEC-035.B/DEC-099/DEC-031 gating):** **RULED — Effect Tier = Skill-Tier of the skill used;
  Effect Magnitude = Effect Tier; Wound Tier = Effect Tier** (max; "equal to or less than"
  per DEC-035.A cl.2). **GM Fiat remains universal. Quality retains no numeric gating role
  for severity** — its functions: S-1 tie-break (DEC-013), success precondition / ≥ 1 floor.
  Default Wound Tier = causing Skill's Skill-Tier ("equal"); a lesser tier requires Player
  choice + GM Fiat. Supersedes DEC-035.B (Quality no longer hard ceiling), DEC-099's
  thresholds, DEC-031's Quality-gating clause (Quality keeps tie-break + success
  precondition + ≥ 1 floor). Preserves DEC-035.A cl.2/3, DEC-041 gate, one-Effect-per-win,
  DEC-104. Future playtest statblocks must author Skill-Tiers consistent with the rule.
  Status: Ruled (Design Override).
- **DEC-112 (Location-Tier 2 granularity — exact assignments, resolves DEC-041 (4)):
  RULED — (R1) Granularity ladder (acting Skill-Tier → Level):** Skill-Tier 2 → Level 2
  (upper/lower split of every coarse zone); Skill-Tier 3 → Level 3 (limbs gain Hand/Foot;
  Head gains Eyes/Ears/Nose-Mouth; Torso gains Pelvis/Groin); Skill-Tier 4 → Level 4 (limbs
  gain individual digits; Head gains individual facial features; Torso gains an
  internal-organ level); Skill-Tier 5+ → Level 5 (joint/phalanx segments; the cap). No
  granularity above Level 5. **(R2) Per-zone sub-zone menus** (cumulative; listed in full in
  the register — Head L2 {Skull, Face}…L4 {…Jaw, Teeth}; Torso L4 {…Heart, Lungs, Liver,
  Stomach, Intestines}; Arms L4 {…Thumb, Index, Middle, Ring, Little}; Legs L4 {…Hallux,
  Second…Fifth}; Level 5 digit = {Proximal, Intermediate, Distal phalanx}, Thumb {Proximal,
  Distal} only). **(R3) Secondary-roll die faces:** menus of 2–3 → d6; 4–10 → d10; single
  secondary roll always resolves (flat menus capped at 10; finer granularity = more specific
  membership, never extra rolls). **(R4)** Tier-1 quartiles unchanged (DEC-100); DEC-030
  fail-fall-back unchanged; Level 4–5 content lists are alpha content-authoring, extensible.
  Status: Ruled (resolves DEC-041 (4)).
- **DEC-113 (Tier-1 vs Tier-2 promotion — per-Effect tier assignment, resolves DEC-040's
  deferred sentence):** **RULED — (R1) per-Effect fixed tiers, no choice at promotion.
  (R2) Tier-2-eligible: Armor Bypass — the only Tier-2 Effect.** Tier 1 (coarse): Wound,
  Trip, Disarm/Break Hold, Equipment Damage. **(R3) PC-only one-step downgrade** — a PC may
  resolve a Tier-2-eligible promoted roll at Tier 1, dropping the secondary roll; Tier 0 is
  never a downgrade option. **(R4) Creatures/NPCs: mandatory tier** (no downgrade).**
  Status: Ruled (resolves DEC-040 deferred sentence; closure via DEC-113).

**Table-play with this block.** Wounds need a Skill-Tier 2+ promoting roll and a promoted
Location Index. Zone from quartiles (1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head); Tier
2+ sub-zone from a secondary d10/d6; mismatch → fall back to Base Inflict Injury HP-only.
Wound record: `Location X Tier-Y Wound Z (Attribute or Skill)`, Z = −Y, Tier = causing
Skill's Skill-Tier. Target Attribute = the Body attribute of the causing Skill; on multiple
candidates creatures pick randomly, Players choose. Attribute wounds recalculate derived
values live. Armor Bypass alone resolves at Tier 2 (creatures always; PCs may downgrade one
step).

## B.5 S-5 Armor (DEC-058–DEC-062)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md`.

- **DEC-058 (S5-A) — Armor is a Tags/Traits system only.** No numeric durability/soak pool.
  Never interacts with Overflow (with DEC-007.A: Armor Tags never modify Overflow).
- **DEC-059 (S5-B) — Bypass = relational property between specific Tag pairs.** An Armor
  Tag may specify non-triggering against Effects carrying a designated other Tag; requires
  Tag-pairing match + location match; stateless; **inapplicable at Location Tier 0**.
- **DEC-060 (S5-C) — Sunder Effect (addition model).** C1 exists; C2 addition model (adds
  "Sundered" Tag, no deletion); C3 permanent until deliberately addressed; C4 resolved via
  ordinary Core Test Transaction. Selectable Effect; **Condition tier** of the S-3 menu
  (confirmed against live record, no conflict). **Expanded 2026-09-02 (DEC-079 C8):
  Condition + Tag model (`state:sundered`).**
- **DEC-061 (S5-D) — Armor resolves before Active Defense.** Effect auto-applies → Armor Tags
  check (incl. Bypass) → surviving magnitude subject to AD mitigation (Model B, DEC-048),
  separate pass. Tier-0 bypass protected by the Zero-Step clause (DEC-062).
- **DEC-062 (S5-E) — Armor coverage is location-bound** (per the DEC-041 fine-grained
  individual-creature-template anatomy). **Zero-Step Armor-location clause:** an armor check
  at Tier 0 derives the struck location via the Zero-Step digit-exchange — read-only, off the
  already-rolled natural roll, no new roll, no player choice, no Tier promotion, discarded
  after the armor check. Armor's presence never forces Tier promotion.

**Table-play with this block.** Auto-applied Effect → armor Tag check (Bypass needs Tag-pair
+ location) → surviving magnitude faces AD mitigation. Armor is location-bound. Tier 0 armor
checks use the one-shot Zero-Step read. Bypass cannot trigger at Tier 0. Sunder adds a
permanent `state:sundered` Tag (Condition + Tag model) via a qualifying Core Test.

## B.6 S-6 Defense — Active Defense (DEC-044–DEC-050, DEC-097, DEC-103)

**Status tag:** **Non-canonical designer ruling** — Ruled.

- **DEC-044 (Fork 3) — Defense architecture: Active Defense.** Defender makes a genuine Core
  Test (full PE/MP cost, full Core consequences). Passive/contest-participant/
  resource-costed-reaction no longer live candidates.
- **DEC-045 (Fork 4) — The defender rolls.**
- **DEC-046 (Fork 5) — Voluntary decline: yes.**
- **DEC-047 (Fork 7) — Defense roll ceiling: uncapped.** (Repeated-defense fatigue closed by
  DEC-075 — no such system; see Part C/confirmed-closed.)
- **DEC-048 (Fork 2) — Model B (preserve DEC-027 literally).** Effect auto-applies exactly;
  AD is **post-hoc mitigation on the already-applied Effect**, never a gate.
- **DEC-049 (Fork 6) — Separate mitigation per Effect.** Each Effect (primary and any
  DEC-026 second Effect) gets its own independent AD mitigation roll. One exchange producing
  two Effects can generate two Defense rolls.
- **DEC-050 (Fork 1) — Defensible-Effect scope, universal.** Any auto-applied Effect is
  eligible — no enumerated list. **AMENDMENT (2026-09-01, resolves OPEN-009):** AD may target
  **any and all** auto-applied Effects, **including positive/beneficial** ones. Invocation
  voluntary, never automatic/mandatory.
- **DEC-097 (C-02) — mitigation amount = Defender's Margin; failed Defense → 0 (B.1).**
- **DEC-103 (S-4/S-6 Active Defense Effect mitigation — Skill-Tier shred + margin
  de-escalation, resolves OI-102):** **RULED — Base Effect is `(Location X) Effect Tier Y
  Magnitude Y`, Y = Attack Skill Tier.** On application the opponent may make a voluntary AD
  roll; failed AD → mitigation 0. **Step 1 Skill-Tier shred:** Atk = Def → Mag −1; Def > Atk →
  Mag − (DefTier − AtkTier), cascading, advantage pays from +2; Atk > Def → Mag +1.
  **Step 2 margin de-escalation:** Mag −= Defender's Margin; leftover margin lost.
  **Unified carry rule:** Mag floor 0 → Tier −1 → Mag = new Tier; Tier floor 0 → Effect
  negated; instant negation only when defender succeeded. Magnitude = negation buffer only;
  surviving Effect records natively (`Location X Tier-Y <Effect> Z`, Z = −Y). **Applies to
  Effects only, never HP** (HP = DEC-104 contest-delta). Tier = difficulty to remove an
  Effect, negation cost triangular `Y(Y+1)/2`. Status: Ruled (resolves OI-102).

**Table-play with this block.** Every auto-applied Effect (positive or negative) may be
mitigated by the defender's voluntary, uncapped AD roll (genuine Core Test). Effects (not
HP): Skill-Tier shred first, then margin de-escalation; floor 0 = removed. HP: Winner −
Defender Margin. Each Effect gets its own AD roll. Defense may be declined.

## B.7 S-7 Incapacitation/Death and HP recording (DEC-052–057, DEC-108, DEC-109, DEC-111)

**Status tag:** **Non-canonical designer ruling** — Ruled. Source
`investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md` (draft; DEC entries
operative), plus 2026-09-05 rulings.

- **DEC-052 — HP = 0 triggers forced incapacitation.** No roll, no save/check.
- **DEC-053 — Incapacitation is HP-driven only**; Wounds fully independent.
- **DEC-054 — Two-branch permanent loss:** (a) incapacitated AND all revival skill tests
  failed (unlimited, no cap), or (b) voluntary player choice.
- **DEC-055 — Stabilization procedure: GM discretion** (which skill, attempts, pacing);
  whether skill tests are used at all is fixed by DEC-054.
- **DEC-056 — No interaction with S-11** (healing/recovery independent).
- **DEC-057 — S-2 non-attack reopening trigger assessed as removed** (session-level
  assessment).
- **DEC-108 (OI-107 — HP floor / negative-HP convention, Option C: uncapped HP):**
  **RULED — HP is UNCAPped; HP may go negative and persists** (no clamp, no floor). DEC-052
  unchanged: forced incapacitation triggers at HP = 0; record continues negative. Further
  damage while incapacitated deepens the negative record; an incapacitated character is no
  longer a "nearest possible target" for NPCs/creatures (See B.21 — DEC-111 refines to
  "not a valid target" for automated attackers). Reviving requires **healing HP back to 0**
  via the S-11 pipeline — negative HP is a counter/extra difficulty modifier on revival.
  *"Healing Wounds revives" does not operate* (a Wound lowers the HP *maximum* via the
  penalized Attribute; healing a Wound restores the maximum, not the current pool).
  Status: Ruled (corner-closures 2026-09-06 via DEC-111).
- **DEC-109 (OI-104 — DEC-101 coverage):** **CLOSED as RESOLVED — DEC-101's defender-win
  branch was exercised frequently and in-spec.** No forced-scenario test required. v4 run
  results superseded by the next playtest (which runs under DEC-103–109). Status: Ruled.
- **DEC-111 (AoE targeting & post-incapacitation targeting — AMENDMENT to DEC-106 §3;
  closes DEC-108 carried-open corners, also flagged in DEC-109):** **RULED — (1) AoE
  target-selection criterion (AMENDMENT to DEC-106 §3): "most targets possible" → "most
  valid actively dangerous targets possible."** An incapacitated character does not count
  toward maximisation. Unruled nuance (recorded, not assumed): whether an AoE whose blast
  physically covers an incapacitated body still affects it — left open. **(2) Unified
  target-selection rule base:** valid = in-range/reachable; an incapacitated character is
  not a valid target. **A Player-Controlled Character may choose to attack an incapacitated
  enemy; an Automated Character may NOT** (automated = creatures, DEC-102). GM-run
  creature/NPC choice remains GM fiat. Status: Ruled.

**Table-play with this block.** HP = 0 → incapacitated; HP may run negative; revive needs HP
healed to 0. Incapacitated characters aren't valid NPC/automated targets (PCs may still
choose them). AoE maximises valid actively-dangerous targets. Permanent loss only via
exhausted revival attempts or player choice; stabilization is GM discretion.

## B.8 S-8 Difficulty and third-party adjudication (DEC-043, DEC-051, DEC-063–DEC-066)

**Status tag:** **Non-canonical designer ruling** — Ruled.

- **DEC-043 — Third-Party Adjudication of Mutual-Failure Opposed Contests (all five
  sub-questions closed).** Q1 default adjudication skill = the contestants' skill; fallback =
  GM/table domain-appropriate substitute. Adjudication roll = full ordinary Core Test. Q2
  outcome binary (Quality no role). Q3 inverted comparison (adjudicator success → lower
  Failure Margin wins; adjudicator failure → higher/worse wins). Q4 failed Double on
  adjudicator roll does unlock Advanced Skill creation. Q5 generalized to all mutual-failure
  contests.
- **DEC-051 — S-8 Stakes Gate rejected.** No pre-Core-Test "skip the roll" filter.
- **DEC-063 (S8-A) — Named tiers with fixed additive Skill-side modifiers**
  (Trivial/Easy/Standard/Hard/Extreme); never on the natural die.
- **DEC-064 (S8-B) — Effective (difficulty-modified) Skill used for** the success/fail check,
  Failure XP, and the Skill Roll Pool cascade entry.
- **DEC-065 (S8-C) — Cascade clamped at permanent Cap;** remainder → General XP. Preserves
  Invariant 10.
- **DEC-066 (S8-D) — Grades symmetric** (bonuses and penalties).

**Table-play with this block.** Apply the named grade's fixed additive modifier to effective
Skill (never the die); effective Skill drives check, XP, cascade; cascade clamps at Cap.
Mutual-failure contests → DEC-043 adjudication. No Stakes Gate.

## B.9 S-9/S-10 Extended Tests (DEC-067–DEC-070)

**Status tag:** **Non-canonical designer ruling** — Ruled. Source
`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` §3.2.

- **DEC-067 (S9-A) — Margin-accumulation:** each successful interval's Margin (Skill − Roll)
  adds to a running total; failures add nothing. Monotonically increasing, never decreases.
- **DEC-068 (S9-B) — Neutral failure:** a failed interval costs resources and generates
  ordinary Failure XP but does not reduce/reset progress.
- **DEC-069 (S9-C) — No Invariant-17 violation** (no income/expenditure dynamic).
- **DEC-070 (S-9/S-10) — Completion target at GM discretion, no formula.**
- **DEC-039** (final roll governs Location Index generation in Extended Tests) — **B.2**.

**Table-play with this block.** Each interval is an ordinary Core Test; successes add Margin
to a running total; failures neutral; completion target = GM discretion.

## B.10 S-11 Rest/Healing (DEC-071–DEC-074, DEC-110, DEC-121)

**Status tag:** **Non-canonical designer ruling** — Ruled. Source
`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` (draft; DEC
entries operative).

- **DEC-071 (S11-A) — Healing during Rest requires an explicit Skill Test** (full ordinary
  9-step Core Test), not passive/automatic HP restoration.
- **DEC-072 (S11-B) — Wound magnitude penalizes the healer's effective Skill** (same pattern
  as DEC-064), not the roll, Cost, or HP amount.
- **DEC-073 (S11-C) — S-11 healing IS an Extended Test instance**: one Rest period = one
  interval; DEC-072 penalty applied; DEC-067 accumulation; DEC-068 neutral failures; DEC-070
  GM-discretion target.
- **DEC-074 — Healing completion target = GM discretion, no HP-deficit lock.**
- **DEC-110 (C-05 — Regeneration/Regrowth healing-magnitude vocabulary):** **CLOSED as a
  content-classification, NOT established as a rule.** No new heal-amount/cadence mechanic.
  The heal value + cadence + any Regrowth/Wound-tier effect is **authored content per
  creature** under DEC-077.A (provisional; Tiwa rules on each). DEC-088's Condition Clause
  decides *whether* a tick applies, not the magnitude. GURPS source value is reference, not
  import. Status: Ruled (content-classification).
- **DEC-121 (StateRecord Tier-mutation via qualifying Skill Test — Flag-3):** a qualifying
  Skill Test (per an explicitly-defined repair/restoration mechanism) may mutate an existing
  StateRecord's **Tier Y downward one step**, Magnitude Z recalculating automatically
  (`Z = −Y`). Distinct from whole-record `removal_tags`; Tier-matching re-evaluated at each
  step; full clearance `Y = 0` removes the record. Mirrors the Wound healing gate
  (DEC-035.A cl.5). Status: Ruled (companion clause to DEC-117 R5).

**Table-play with this block.** Rest healing = Extended Test: each interval an ordinary Core
Test; wound magnitude penalizes healer's effective Skill; Margin accumulation; GM-set target.
Negative HP must be healed to 0 before revival (B.7). Condition/Effect records heal by
Tier-mutation (a Skill Test reduces Tier one step toward 0) — the "Effect Heal System"
(DEC-127 naming).

## B.11 §5.5 Encumbrance (DEC-078, closed carried-open values 2026-09-06)

**Status tag:** **Non-canonical designer ruling** — Ruled; carried-open values CLOSED
2026-09-06 by Tiwa (capacity, thresholds, penalties).

- **DEC-078 (P3 — Encumbrance Model) — Option A: Load Thresholds/Penalties (Numeric
  Mechanic), five sub-rulings:** (A1) Capacity from a Body attribute (originally bpe/bee
  Endurance-coded); **(superseded 2026-09-06 by R1 below — capacity is now HP-derived)**;
  (A2) penalty = Skill-side modifier only (never the d100); (A3) Movement Speed formula
  untouched (DEC-004); (A4) exceeding a threshold imposes the Condition **Encumbered**;
  (A5) static thresholds + Skill-side penalty only; no secondary capacity/weight pool
  (Invariant 17). **ENC-F01 (ratified by Tiwa 2026-09-06): clothing counts toward load.**

**2026-09-06 closure rulings (recorded in the DEC-078 cell; operative values):**
- **(R1) Capacity:** `C = floor(HP / 6)` kg, where **HP = sum of all 12 Body attributes**.
  This supersedes the bpe/bee-averaging direction and the investigation candidate
  `C = floor((bpe+bee)/2)`. Calibration: all-20 attributes → HP 240 → C 40 kg; all-50
  playtest PC (v6 scaffold) → HP 600 → C 100 kg.
- **(R2) Thresholds — six relative-`E` bands** at cut-points **0.30 / 0.60 / 0.90 / 1.20 /
  1.50** (E = load/capacity): Unencumbered `E < 0.30`; Light `0.30 ≤ E < 0.60`; Moderate
  `0.60 ≤ E < 0.90`; Heavy `0.90 ≤ E < 1.20`; Overburdened `1.20 ≤ E < 1.50`; Extreme
  `E ≥ 1.50`.
- **(R3) Penalty ladder per band:** Band 0 = none; Bands 1–5 = **−1 / −2 / −3 / −4 / −5**,
  expressed as the Encumbered Condition `Tier-Y Encumbered Value Z`, `Z = −Y` (Band 1 →
  Tier-1 Value −1 … Band 5 → Tier-5 Value −5). Applied as a Skill-side modifier to all Body
  Skills, plus the −Y Movement-Speed overlay (overlay only; formula untouched). Same-tier
  values add, higher replaces; **Slowed + Encumbered: apply the worse penalty** (DEC-079).

**Table-play with this block.** Load (kg, incl. clothing) ÷ (`floor(HP/6)` kg) = E. Bands at
0.30/0.60/0.90/1.20/1.50. Exceeding a threshold applies the Encumbered Condition
`Tier-Y Encumbered Value Z` (Z = −Y): −Y to all Body Skills, −Y overlay to Movement Speed.
Source: `investigations/tiwas-grok-advisory-session-decision-report-s3-content-encumbrance-wound-precedence-2026-09-02.md`
§2.1 (DEC-078); `investigations/tiwas-encumbrance-system-investigation-*2026-09-06.md`
series (stored; ENC-F01 ratified 2026-09-06).

---

## B.12 §5.5 Conditions subsystem (DEC-079; G2 movement-denial closures DEC-122–DEC-127)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-grok-advisory-session-reserved-systems-5-5-conditions-tags-equipment-timeaction-2026-09-02.md`
§5; unification 2026-09-06 (DEC-115/116 — B.19); G2 clarifications 2026-09-07.

- **DEC-079 — eight sub-rulings (C1–C8):**
  - **(C1) Format:** `Tier-Y Condition Value Z` (global) or `Location X Tier-Y Condition
    Value Z` (localized), parallel to DEC-035.A Wound format.
  - **(C2) Magnitude:** Value Z = −Y, identical to Wound magnitude.
  - **(C3) Tier production:** Generating Effect Quality (hard ceiling per DEC-035.B) +
    Skill-Tier ≥ 2 production gate (DEC-041). **(NOTE — DEC-107 now makes Skill-Tier of the
    causing skill the operative ceiling; see B.4.)**
  - **(C4) Scope:** all Skills that use a Body Attribute.
  - **(C5) Movement Speed penalty:** −Y overlay on the effective stat; DEC-004 formula
    untouched.
  - **(C6) Stunned vs Incapacitated:** distinct Conditions (Incapacitated strictly stronger).
  - **(C7) Poisoned vs Sickened:** distinct; both Skill-side penalty only; no HP DoT
    (DEC-023.A preserved).
  - **(C8) Sundered:** Condition + Tag model (`state:sundered`), expanding DEC-060.
  - **Alpha vocabulary — 14 Conditions** (register-verbatim essentials; decimals of
    stacking/removal follow DEC-035.A / DEC-079): **Encumbered** (global; −Y Movement Speed +
    all Body Skills when load exceeded; same-tier add, higher replaces; ends when load falls
    below threshold or by recovery action); **Grappled** (Location or global; cannot move
    away from grappler; −Y to attacks not directed at grappler; limb unusable; highest tier
    only; ends by contested Break Hold — **see DEC-124/DEC-131**, grappler incapacity, or
    forced separation; distinct from Restrained); **Restrained** (global or Location; cannot
    move; −Y to all attacks + all Body Skills; same-tier add / higher replaces; ends by Break
    Free, ally intervention, or GM Fiat; strictly stronger than Grappled); **Prone** (global;
    −Y attack rolls; movement = crawl or spend to stand; highest tier only; ends by spending
    movement or Effect; combines with movement-denial Conditions); **Blinded** (global; auto-
    fail pure sight tests; −Y Perception + attack rolls; ends by removal Effect, time, or
    sight restoration); **Deafened** (auto-fail hearing tests; −Y Perception-involving-sound);
    **Frightened** (−Y all Skills while source perceivable; source-dependent);
    **Slowed** (−Y Movement Speed + Body Skills [Speed-coded]; **does not stack with
    Encumbered — apply the worse penalty**); **Stunned** (cannot declare actions/movement,
    auto-fail active Body/Speed resistance; highest tier; action denial); **Incapacitated**
    (cannot declare actions/movement, auto-fail all active resistance; highest tier; stronger
    than Stunned); **Fatigued** (DEC-075; −Y all Body Skills; ends by rest/recovery);
    **Sundered** (Item or Location; applies `state:sundered` Tag; permanent until repaired;
    cumulative at same tier); **Poisoned / Sickened** (no DoT; Skill-side penalties).
    **Carried open:** numeric tier values per instance, precise Movement Speed reduction
    mechanics beyond −Y, Stunned-vs-action-denial interaction.
- **DEC-122 (G2 Item 1 + Item 5 — self-referential-Y uniform treatment for movement-denial
  Conditions):** **RULED — `Y` = the target stat's own current value at time of query;
  `Z = −Y`; `Effective Stat = Stat + Z = 0`** for Stunned/Incapacitated/Restrained/Grappled/
  Prone Movement Speed interactions. DEC-004's formula never touched. No new field/record —
  fits the DEC-115 schema. **Item 5 — third Y-source pattern named "target-stat-value"**
  (alongside causing-Skill-Tier, DEC-107, and load-band non-Tier, DEC-078). **Query-time-live**
  (Y re-read at query time, not fixed at application). Adoption **provisional** per Tiwa —
  open to future supersession. **NOTE — DEC-124 removes Grappled's away-from-grappler
  movement from this overlay for the escape direction** (contested Break Hold instead; DEC-131
  closes the fail-vs-relocate outcome).
- **DEC-123 (G2 Item 2 — "never total"; Design Override of DEC-079's Stunned/Incapacitated/
  Restrained wording):** **RULED — these Conditions no longer categorically prohibit
  declaring an action.** A Stunned/Incapacitated/Restrained character may declare any test
  and roll it — guaranteed to fail (Effective Skill 0 via DEC-122), but the attempt proceeds
  through the full Core Test Transaction (Cost/Overflow/Failure XP/failed-Double eligibility).
  Whether the roll is permitted at all is **GM fiat**. Override confined to DEC-079's own
  wording; no cascade — DEC-052/DEC-053 untouched.
  **Reason (Tiwa):** "If the player wants to make a roll which is guaranteed to fail then
  that is GM fiat to allow it or to stop it. The system should not specifically prevent the
  attempt."
- **DEC-126 ("Helpless" is not a mechanical term):** **RULED — "Helpless" carries no
  mechanical meaning/trigger/effect/game-state.** Appearances in source text are descriptive
  prose only. Resolves the DEC-123 pending item; no interaction with DEC-054/055.
- **DEC-124 (G2 Item 3 — Grappled movement restriction; contested Break-Hold model):**
  **RULED — moving away from a Grapple requires a successful contested Skill Check
  (Break Hold / Break Free);** attempt failure either fails or relocates both — outcome
  **"To be decided" (deferred)**. Supersedes Grappled's away-direction denial under DEC-122's
  uniform zero for that direction only. **RESOLVED 2026-09-07 via DEC-131.**
- **DEC-131 (G2 Item 3 deferred outcome — Option A "Pure Break"):** **RULED — fail path**
  (mover loses the contest): Grapple persists, mover locked, **no relocation** (failed
  contest still a full Core Test). **Success path:** the Grapple Effect ends via **stepwise
  Heal-Effect-System reduction** (DEC-121 shape): each success reduces `Tier Y` one step, Z
  recalcs (`Z = −Y`), gate = breaker's Break Hold Skill-Tier ≥ record's current Tier;
  `Y = 0` removes the record and the mover is free. **"Relocate both" branch DROPPED.**
  Closed fully. **Remains open (content):** non-escape Grappled movement (not away-from-
  grappler; holder dragging the victim).
- **DEC-125 (G2 Item 4 — Prone crawl-speed fraction; floor-of-1):** **RULED — Prone
  guarantees nonzero movement at all Movement Speeds.** Operative session-standard form:
  **`crawl = max(1, floor(Movement Speed / 2))`** — the `max(1, …)` clamp is the ruled
  guarantee; the base fraction (half vs third) is ordinary content-authoring (DEC-077.A).
  Closes G2 Item 4.

**Table-play with this block.** Conditions are records `Tier-Y Condition Value Z`,
`Z = −Y`, Skill-side only, no DoT, never touch Overflow or the d100. Movement-denial: the
four total-lock Conditions zero the relevant stat via self-referential-Y (live query),
but declared tests still run (guaranteed failure) unless GM stops them. Break Hold is a
contested Skill Check; each win steps the Grapple Tier down; `Y = 0` breaks free. Prone
crawl = `max(1, floor(Speed/2))`.

## B.13 §5.5 Tags ontology (DEC-080; DEC-088; DEC-091; DEC-114)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-grok-advisory-session-reserved-systems-5-5-conditions-tags-equipment-timeaction-2026-09-02.md`
§6; closure 2026-09-06 via DEC-114.

- **DEC-080 — (T1) Ontology model:** open extensible, namespace-based
  (`slot:`, `damage:`, `offense:`, `handling:`, `defense:`, `state:`, `env:`, `creature:`),
  extensible without altering the base model. **(T2) Alpha closed list — 34 Tags:**
  Equipment (22): `slot:main_hand`, `slot:off_hand`, `slot:two_hand`, `slot:body`,
  `slot:head`, `slot:shield`, `damage:bludgeoning`, `damage:slashing`, `damage:piercing`,
  `offense:melee`, `offense:ranged`, `offense:thrown`, `handling:light`, `handling:heavy`,
  `handling:reach`, `handling:finesse`, `defense:armor`, `defense:shield`,
  `state:held`, `state:worn`, `state:sheathed`, `state:stowed`. Environment (6):
  `env:hazard_physical`, `env:hazard_systemic`, `env:terrain_difficult`,
  `env:terrain_hazardous`, `env:darkness`, `env:weather_obscuring`. Creature (6):
  `creature:type_humanoid`, `creature:type_beast`, `creature:type_undead`,
  `creature:size_small`, `creature:size_medium`, `creature:size_large`. Resolves the
  "starter vocabulary" dependency of DEC-028. Carried-open items closed 2026-09-06 via
  DEC-114.
- **DEC-088 (env:freezing + Conditional-Trait Binding grammar):** **RULED — new scene-state
  Tag `env:freezing`** (7th Environment tag; presence/absence, GM-declared per scene, no
  numeric grade). **Conditional-Trait Binding:** a Trait or Tag-granted Effect may declare a
  Condition Clause `Active only while [env:X] is present`, referencing exactly one `env:`
  Tag; while absent, the bound Trait/Effect is **not present** for all mechanical purposes
  (no DR, no Regeneration tick, no Regrowth). Read-only, stateless. Invariant-safe.
  Worked example: Ice Troll freezing-gated Traits. **Carried open:** graded temperature;
  scene-state tracking mechanism (full Hazards subsystem unbuilt — B.15). Also supplies the
  *whether*-gate for creature Regeneration/Regrowth (magnitude = content, DEC-110).
- **DEC-091 (terrain hazards; `env:terrain_*` descriptive-only):** **RULED — terrain hazards
  resolve through the existing failed-Core-Test → DEC-037 → S-3 pipeline; no separate
  terrain-hazard engine.** `env:terrain_difficult`/`env:terrain_hazardous` are
  **descriptive/flavour markers only, no independent mechanical trigger.** Difficulty comes
  from the GM choosing a difficulty grade (DEC-063). Modal distinction preserved:
  `env:terrain_*` descriptive vs `env:freezing` activation Tag.
- **DEC-114 (closure of DEC-080 carried-open items; four sub-rulings):**
  **(R1) Hazard routing:** `env:hazard_physical` → DEC-037 (1) route (failed roll supplies
  the Location Index; Effect lands there); `env:hazard_systemic` → systemic-exempt direct
  HP/Condition. Neither tag initiates a roll or new engine; the failure still triggers per
  DEC-037. **(R2) Location-tier Effect tag triggers:** *Armor Bypass* (Tier-2): target has
  `defense:armor` bound to the struck sub-location, or `defense:shield` at that sub-location;
  match at DEC-112 sub-zone level. *Disarm/Break Hold* (Tier 1): target has a `state:held`
  item carrying `slot:main_hand` or `slot:two_hand`; Break Hold treats any `state:held` item
  as the gripped object; match at DEC-100 coarse zones. *Equipment Damage* (Tier 1): target
  has `state:held` or `state:worn` gear at the struck coarse zone; **broad rule — no
  `damage:*` type match required.** Tag presence read/consulted only (stateless);
  mismatch → DEC-030 fallback. **(R3) `magic:` and `ability:` namespace prefixes reserved**
  with zero entries (labeling reservation only; requires authorization with the Magic
  subsystem). **(R4) Equipment damage/handling extension — 5 new tags (34 → 39):**
  `damage:fire`, `damage:cold`, `damage:corrosion`, `damage:electric`, `handling:versatile`.

**Table-play with this block.** Tags are stateless labels in namespaces; read-only, never
touch Overflow. `env:freezing` activates gated Traits via a Condition Clause. Tag-driven
Effect triggers: Armor Bypass needs a bound `defense:armor`/`defense:shield` Tag at the
sub-location; Disarm/Break Hold needs a `state:held` main-hand item; Equipment Damage needs
any held/worn gear at the zone. Terrain tags are descriptive — difficulty is a grade.

## B.14 §5.5 Equipment state and Item records (DEC-081; DEC-118–121; DEC-128–129)

**Status tag:** **Non-canonical designer ruling** — Ruled (2026-09-02 DEC-081; 2026-09-07
EQ-1/EQ-2 series). Primary sources:
`investigations/tiwas-grok-advisory-session-reserved-systems-5-5-conditions-tags-equipment-timeaction-2026-09-02.md`
§5.5; `investigations/tiwas-eq1-eq2-item-creation-upgrade-repair-draft-2026-09-07.md`;
`investigations/tiwas-equipment-tier-sunder-advisory-handoff-2026-09-07.md`.

- **DEC-081 (§5.5 Equipment state model):** **RULED — Equipment state is fully expressed
  through Conditions + Tags** — no independent state-tracker. **Held items automatically
  receive the Location of the holding limb.** Consistent with DEC-062. **AMENDED by DEC-128
  Q1:** items gain an independent base **Item Tier / Item Magnitude record** (see below).
- **DEC-118 (EquipDamage/Repair track — record-only; resolves the sync-track fork; supersedes
  "Item Magnitude = Item HP"):** **RULED — damage does NOT ablate Item Magnitude.** The
  Equipment Damage / Sunder record is the sole representation of accumulated harm; Item
  Magnitude is a **creation-quality stat only**, never read by damage application or by
  Repair. Repair reduces the negative record's Tier exclusively. **Supersedes** the earlier
  "Item Magnitude = Item HP; `state:unusable` at HP ≤ 0" model. DEC-058 reinforced (no
  numeric durability/soak pool). **Reason (Tiwa):** "Items can have a lot of Effects stacked
  on them, but the base Item should remain."
- **DEC-119 (state:unusable trigger — Option B):** **RULED — `state:unusable` gates on the
  negative record's presence/Tier, NOT on Item Magnitude.** Trigger (Tiwa, verbatim):
  "state:unusable occurs when the Item suffers an Effect which causes state:unusable or the
  impacts of an Effect or Effects cause the Item to become too heavily damaged / affected to
  be effectively used." Clearing the record via Repair lifts it directly. **Coexists with
  `state:sundered`**; `state:unusable` is a **new Tag entry** extending the `state:`
  namespace. Invalid-target rule: Unusable items are excluded from valid targets of
  **Negative** Skill Effects only (buffing remains valid); sole-candidate → DEC-030
  fail-and-fall-back; armor Tags absent for DEC-062 coverage while Unusable.
- **DEC-120 (Repair on already-Unusable items):** **RULED — Yes.** Repair may be attempted on
  an already-Unusable item; the Unusable state never mechanically forecloses the attempt
  (difficulty may rise via Tags/GM fiat).
- **DEC-121 (StateRecord Tier-mutation)** — see **B.10** (mechanism) — the Heal Effect
  System's stepwise reduction; Repair uses this shape.
- **DEC-128 (EQ-1/EQ-2: DEC-081 amendment + failed Creation/Upgrade + Repair sub-questions,
  seven sub-rulings):** **(Q1) DEC-081 amended:** items get an independent base **Item Tier /
  Item Magnitude** record (established at creation, modified by Upgrade), separate from and
  not superseded by the Condition/Tag system (which still represents negative state).
  Placed **outside** the DEC-115/117 unified StateRecord schema (uses `Z = Y`, conflicting
  with DEC-115 R2's `Z = −Y`). DEC-081's held-item Location clause and negative-state
  framework preserved. **(Q2) Failed Creation produces no item; Item Creation is an Extended
  Test** (DEC-067/068 margin-accumulation; change to the draft's default). **(Q3) Failed
  Upgrade: Reading B adopted — item Tier +1 with NO Magnitude gain** → `Item Tier Y,
  Magnitude Y−1` (imbalanced; further upgrade may now require a higher Skill Tier or GM
  Fiat). Reason (Tiwa): "To increase Item Tier requires a Skill Tier of the same level or
  higher… the Item is now Damaged… Need to be repaired." **(Q-R1) Repair uses the Heal Effect
  System; max Repair = Original Tier (set at creation); if Original Tier unknown, treat all
  Repair rolls as Upgrade Rolls. (Q-R2) GM-set completion threshold scales with the record's
  current Tier. (Q-R3) Multiple negative records on one item are independent. (Q-R4) Item
  Creation/Upgrade/Repair Skills all usable to Upgrade/Repair; GM Fiat governs which.
  (Q-R5) Mid-combat vs downtime unrestricted (ordinary Core Test; combat attempt = player
  choice).**
- **DEC-129 (Item Magnitude repair to Tier — AMENDMENT to DEC-118):** **RULED — Item
  Magnitude is repairable, capped at the Item Tier.** (1) Base equality: `Item Tier Y = Item
  Magnitude Y` at creation (confirms DEC-128 Q1 / `Z = Y`). (2) Repair target: Magnitude
  repairs **up to** Tier; never exceeds Tier. (3) An item with Magnitude < Tier may have a
  Repair Skill Roll restore Magnitude to equality with Tier — **AMENDING DEC-118's** clause
  to "referenced by Repair for restore-to-Tier only", never as ablative HP. A `Item Tier Y,
  Magnitude Y−1` imbalance repairs via a Repair Skill Roll to `Y`. Q-R1/Q-R2 machinery
  governs. DEC-058 preserved (Magnitude = creation-quality ceiling, not soak pool).

**Table-play with this block.** Items have `Item Tier Y / Item Magnitude Y` (base-equal at
creation). Damage → negative records (Sunder/Equipment Damage) only; Magnitude never ablates.
Failed Creation: no item (Creation is an Extended Test). Failed Upgrade: Tier +1, Magnitude
stays → `Item Tier Y, Magnitude Y−1`, needs repair. Repair: Skill Test steps the negative
record toward 0 (Heal Effect System); a separate Repair Skill Roll restores Magnitude up to
Tier. Unusable items: only negative Effects excluded.

## B.15 §5.5 Time/Action and Hazards (DEC-082; DEC-089–093)

**Status tag:** **Non-canonical designer ruling** — Ruled. Primary source:
`investigations/tiwas-grok-advisory-session-reserved-systems-5-5-conditions-tags-equipment-timeaction-2026-09-02.md`
§5; hazards source `investigations/tiwas-hazards-*` (2026-09-03 chain).

- **DEC-082 (§5.5 Time/Action economy):** **RULED — Skill-side / Movement-penalty model only;
  no discrete action budget or action points.** Time/Action expressed entirely through
  Skill-side and Movement penalties applied by Conditions and Effects — no action-point pool,
  no discrete action budget, no "spend an action" mechanic. Consistent with Invariant 17.
  **Carried open (partially resolved):** exact movement-penalty values per Condition (G1,
  still open), movement-denial/movement-Speed interaction (resolved via DEC-122–127 in B.12),
  full subsystem definition (Reserved).
- **DEC-089 (H1-A — Systemic Hazard resolution cadence):** **RULED — a systemic hazard
  represents an ongoing process of progress toward surviving it**, resolved via the existing
  Core Test + resource machinery; no new resource economy, no parallel engine.
- **DEC-090 (H2-A — Scope to S-3 Effect interface):** **RULED — the systemic-hazard decision
  is scoped to the S-3 systemic-hazard Effect interface**; the Core Test, Skill difficulty,
  Location Index, Cost, Overflow, Failure XP, XP cascade, Recovery, and environmental state
  stay outside S-3's ownership.
- **DEC-091 (H3-A — terrain hazards; `env:terrain_*` descriptive-only)** — **B.13**.
- **DEC-092 (H4-A — Hazard difficulty as Skill-side penalty):** **RULED — hazard difficulty
  uses DEC-063's fixed additive Skill-side penalty architecture; never the d100, Cost,
  Overflow, XP, Recovery, or pools.**
- **DEC-093 (H5-B — Graded Intensity as lookup key only):** **RULED — Intensity may be
  graded but is a LOOKUP KEY ONLY** into predefined hazard parameters; it never rolls,
  consumes resources, modifies Overflow, generates XP, creates an Effect, or creates a second
  transaction. Resolution: Intensity → lookup key → parameters → existing Tiwas mechanics.

**Table-play with this block.** No action points — conditions/effects just impose penalties.
Hazards resolve as progress toward surviving (Core Tests); difficulty = a Skill-side grade
modifier; Intensity is only a key into pre-set parameters.

## B.16 §5.5 Unified StateRecord schema (DEC-115; DEC-116; DEC-117; DEC-127 naming)

**Status tag:** **Non-canonical designer ruling** — Ruled (2026-09-06 unification series).

- **DEC-115 (Effect/Condition record schema merge):** **RULED — one record schema for Effect
  and Condition records: `Type` / `Tier Y` / `Magnitude Z` / optional `Location X`.**
  `Type` distinguishes Effect records (Wounds per DEC-035.A; Effect payloads per the
  DEC-023–030/DEC-107 chain) from Condition records (DEC-079 C1/C2). **R2:** `Z = −Y`,
  ceiling/production gate unchanged (DEC-107 / DEC-041). **R3:** format-only unification —
  stacking, duration/removal, healing gates preserved. **R4:** DEC-025 NOT reopened — no
  `skill:` namespace, no Skill-side Tags, no Tag-entitled Effect. **R5 (Tiwa):** "All six
  reports agree this is close to free — DEC-035.A and DEC-079 are already the same shape."
- **DEC-116 (Tag record schema — optional Tier/Magnitude, absent-by-default):** **RULED — a
  Tag record defaults to vocabulary-only** (identity/presence, no numeric grade); numeric
  fields only where a ruling supplies them (`state:sundered` precedent). **Absence ≠ zero.**
  ~33 of 34 alpha Tags default to vocabulary-only. No counter engine adopted at this point
  (superseded by DEC-117 R3).
- **DEC-117 (Unified StateRecord — Tags join the schema; counters; removal; type defaults;
  eight sub-rulings):** **(R1) Tags, Effects, and Conditions are the same mechanical record —
  one state record shape** (`Type` / `Tier Y` / `Magnitude Z` / optional `Location X` /
  `id` / `source` / `duration` / `removal_tags` / `counters`); the three names remain as
  fiction-level classification. **(R2) Type defaults:** Tag = `duration: permanent`,
  `removal_tags` usually empty; Effect = `duration: instant` or `scene`, S-1-contest
  payloads; Condition = varying, typically negative fiction. Overridable per record.
  **(R3) Counter rule (declarative):** optional `counters: list<text>`; "if a target has a
  StateRecord whose `id` is in another record's `counters` list, the countered record's
  effects do not apply." Pure filter — no rolls, no pools, no second engine. Explicit-only
  (no implicit counter relationships). **(R4) Magnitude tiebreak:** same `id` mutual
  counters → higher Magnitude wins; equal → neither counters. **(R5) Removal rule:**
  optional `removal_tags: list<text>`; "an Effect can remove a [matching] record when the
  removing Effect has a removal Tag present" — one removal per Effect per application; only
  same-Tier records. **(R6) DEC-117 advisory drafts comparison** (six sources) adopted with
  all designer confirmations. **(R7) Skills explicitly forbidden from requiring Tags**
  (preserves DEC-025). **(R8) Tag-as-StateRecord tension** with DEC-058/079/080's
  "read-only stateless metadata" framing is recorded and mitigated (read-only-re-pools
  constraint, meta-rule-over-engine). **Supersedes DEC-116 R4** (counters now explicitly
  adopted as a declarative filter). Full schema and meta-rules in the register / source
  `investigations/tiwas-tag-condition-effect-unification-draft-execution-report-perplexity-2026-09-06.md`.
- **DEC-127 (terminology — "Effect Tier Magnitude System" and "Effect Heal System"):**
  **RULED — naming adoption only.** **(1) "Effect Tier Magnitude System"** = the unified
  Effect/Condition/State record architecture (`Type / Tier Y / Magnitude Z / [Location X]`,
  DEC-115) with governing mechanics (Tier = Skill-Roll Tier, DEC-107; Z = −Y; Location
  optional; lesser tier = Player choice + GM Fiat). **(2) "Effect Heal System"** = healing
  gated by Skill-Tier ≥ Effect's Tier (DEC-035.A cl.5) reducing the record stepwise toward
  zero (DEC-121 Tier-mutation). No new mechanics; naming only.

**Table-play with this block.** One record shape for every state on characters/items/scenes:
`Type` / `Tier Y` / `Magnitude Z` / `[Location X]` / `id` / `source` / `duration` /
`removal_tags` / `counters`. Z = −Y. Records are removed by matching removal Effects (one per
application, same-Tier) or healed stepwise (Skill-Tier ≥ record Tier). Counters are explicit
filters. Skills never require Tags.

## B.17 Combat sequencing, reactions, movement, and GM Fiat (DEC-095; DEC-106; DEC-132; DEC-133; DEC-130)

**Status tag:** **Non-canonical designer ruling** — Ruled (2026-09-04 through 2026-09-08).

- **DEC-095 (SC-04 — Combat sequencing / initiative):** **RULED — Speed-based turn order;
  alternating turns; one substantive combat action per turn (one S-1 combat exchange);
  lower-Speed combatants may be interrupted or eliminated before acting.** Turn order:
  (1) determine each combatant's current Speed; (2) highest Speed acts first; (3) one combat
  turn per round; (4) a combat turn permits one substantive combat action/test; (5) after all
  act, round ends; (6) Speed recalculated if its attributes change; (7) ties by natural d100
  comparison (reroll until tie broken); (8) initiative is not a Core Test, no resource cost.
  "One substantive action" = **one S-1 combat exchange**; the defender's Active-Defense Core
  Test (DEC-044) is nested and does not count against the actor's one action. Movement is a
  free/bundled side-activity (DEC-082) and does not consume the substantive action.
- **DEC-106 (SC-XX / OI-105 — Creature/NPC action selection; Design Override of DEC-095
  Step 3 for creatures/NPCs):** **RULED — (1) Base economy:** one substantive combat
  action/test per turn; multiple applicable skills → GM fiat. **(2) Creature/NPC exception:**
  GM present → GM fiat; no GM (automated/delegated) → creatures with multiple legal combat
  actions use **all of them**, each authored attack in **highest-applicable-Skill →
  lowest** order, **all on the creature's own turn back-to-back**, each its own S-1 exchange.
  **(3) Targeting:** each attack targets the **nearest possible target**; AoE instead hits
  **most targets possible** (**AMENDED by DEC-111**: "most valid actively dangerous
  targets"). **(4) Energy Pool:** each attack is its own Core Test with its own Energy cost;
  an NPC/creature may exhaust itself via its own multi-attacks (self-Overflow, DEC-007).
  **(5) PCs do NOT gain multi-attack.** **(6) Automated playtest Characters are creatures.**
  **Design Override:** DEC-095 Step 3 stays for base economy and PCs; overridden for
  creatures/NPCs. **Reason (Tiwa):** "Combat system overhaul due to results of playtests."
- **DEC-132 (G4 — Reactions beyond Active Defense):** **RULED — Option C (structured
  tag-triggered reactions).** (1) Active Defense remains the primary/default out-of-turn
  defense. (2) Reactions permitted when: (a) a defined trigger occurs during another
  combatant's turn; (b) the character possesses a specific reaction-granting Tag (e.g.
  `combat:vigilant` or equivalent content-authored Tag); (c) the reaction resolves as a
  **full S-1 combat exchange** (Core Test, Cost, Overflow, Failure XP). (3) No new action
  economy — no extra turns, no bypass of the speed order, no consumption of the reactor's own
  turn. (4) Trigger definitions + matching Tags are **content-authoring (DEC-077.A)**.
  (5) Equal eligibility for PCs and automated characters. **Carried open:** trigger menu
  content, exact Tag vocabulary for grants, whether a reaction replaces or stacks with Active
  Defense on the same incoming Effect, per-scene/frequency limits. Closes the G4 blank.
- **DEC-133 (G5 — Movement resolution granularity):** **RULED — Option C (Hybrid).**
  (1) One canonical distance model, two spatial representations, explicit authority
  hierarchy: **Abstract distance bands (canonical) → Hex/grid conversion (derivative
  presentation)**. (2) Four abstract zones: **Engagement / Short / Medium / Far**.
  (3) **Movement Distance per combat turn = effective Movement Speed**;
  **1 Movement Speed = 1 hex per combat turn**, where hex = canonical distance unit;
  `Movement Distance per turn = effective Movement Speed` (Movement Speed = DEC-004 derived
  statistic; effective = after applicable penalties). (4) **Band↔hex conversion boundaries
  are content-authoring (DEC-077.A)** — qualitative at rules level. (5) Movement measured per
  combat turn under DEC-095; G5 references DEC-095, does not define real-world duration (kept
  out of G3). **Explicitly left open:** Disengage; Zone of Control; Chase; generic movement
  contests; Forced Movement magnitude; Pin/Hold Position resolution; Seize/Deny Ground
  resolution (existing Position-tier Effects in DEC-023.A). **G1 (movement-penalty magnitude
  table) and G3 (duration/time-unit scale) remain open.** Status: Ruled (spatial substrate;
  boundaries + contested-movement consumption deferred).
- **DEC-130 (GM Fiat universality — meaning and scope):** **RULED — GM Fiat is universal in
  scope but bounded in authority ("bounded universality").** (1) Scope: available **at every
  decision point across all designed subsystems** — tiers, thresholds, gates, edge cases,
  targets, adjudication gaps (consolidating DEC-035.A cl.6, DEC-107, DEC-106 §2, DEC-123,
  DEC-129). (2) **Bound: does NOT override the Locked Canonical Core** — Overflow immutability
  (DEC-007.A), Cost = natural roll (DEC-007/Invariant 6), forced HP triggers / incapacitation
  at HP = 0 (DEC-052), no-damage-over-time policy (DEC-023.A). (3) Not a mechanic substitute:
  Fiat enhances drama, does not replace normal resolution. Closes the pending markers on
  DEC-106/108/109/111.

**Table-play with this block.** Combat: Speed order, one S-1 exchange per turn (AD nested,
movement free). Creatures/NPCs: GM-fiat when GM present; otherwise all multi-attacks back-to-
back, nearest-target (AoE = most valid dangerous targets). Reactions: tag-gated full S-1
exchanges out-of-turn, trigger content authored per creature. Movement: zones Engagement/
Short/Medium/Far; 1 Speed = 1 hex per turn; hex↔band boundaries are content. GM Fiat applies
at every decision point but never overrides Overflow immutability, Cost = natural roll, HP=0
incapacitation, or the no-DoT policy.

## B.18 S-12 Creature/NPC content (DEC-076; DEC-077; DEC-077.A; DEC-083–087; DEC-098; DEC-110)

**Status tag:** **Non-canonical designer ruling** — Ruled (2026-09-01, 2026-09-02,
2026-09-04, 2026-09-05).

- **DEC-076 (S-12 Ruling A — stat-generation/resolution mode fork):** **RULED — dual-mode
  fork.** Computerized/automated: full 24-attribute generation identical to PCs, same Core
  Test economy. Non-automated (tabletop/GM-run): abbreviated/simplified stat-block method;
  resolution **defaults to GM decision on system** — no system-authored alternate mechanism
  (the phrase "GM-facing shortcut layer" is rejected/superseded). Consistent with
  DEC-041 §5, Invariant 17/18, GM-discretion precedent (DEC-055/DEC-070).
- **DEC-077 (S-12 Ruling B — content authoring path):** **RULED — content deferred to the
  designer's own playtesting.** Actual creature/campaign templates (e.g. Goblin, Dragon) via
  DEC-041's individual-template method are developed by **Tiwa via playtesting**, not drafted
  by any advisory model. **AMENDED by DEC-077.A.**
- **DEC-077.A (AMENDMENT — GURPS-to-Tiwas conversion workflow for BToV-Madness):**
  **RULED — advisory models may convert GURPS source creatures to Tiwas-format working stat
  blocks for the Beyond-the-Vale-of-Madness playtest; Tiwa rules on each conversion;
  conversions remain provisional playtest material unless expressly affirmed.** Rationale:
  Tiwa does not know GURPS and cannot author the source-to-Tiwas conversion from scratch.
  Scope: (1) GURPS creatures from `Beyond-the-Vale-of-Madness-GURPS.pdf` for the BToV-Madness
  playtest only; (2) uses DEC-076 Ruling A's abbreviated method + DEC-041's individual-
  template method; (3) Tiwa retains final authorship/ownership; (4) nothing produced is
  Canonical or promoted.
- **DEC-083 (Blood Man Blood Seep — vs no-DoT policy):** **RULED — single-application Effect
  on a grapple win; NO ongoing damage-over-time.** GURPS per-second corrosive DoT does not
  convert as ongoing damage; represented as a one-shot Impose-Condition/Inflict-Injury Effect
  on the win or narrated/GM-fiat. Preserves DEC-023.A and DEC-024.
- **DEC-084 (Perplexity Goblin/Dragon — scope of DEC-077.A):** **RULED — kept as
  Tiwa-authored NEW-Content creatures, NOT GURPS conversions** (no GURPS stat block in the
  source PDF); outside the conversion workflow but may be developed as original Tiwas
  creatures. Provenance: must not be mislabelled as conversions.
- **DEC-085 (Playtest creature working baseline & combat-pipeline method):** **RULED — adopt
  the rule-faithful baseline (GPT-5.6 Luna) for BToV working stat blocks.** Derived stats use
  DEC-004/DEC-005 exactly (no GURPS values verbatim); no GURPS damage dice/Dodge/Parry/DR
  numbers imported (attacks = S-1 contests; defense = S-6; armor = Tags/Traits); Tier-2
  signature attacks for Wound-capable creatures (content per creature, not universal); attack
  roll = attacker resource cost, ≠ target damage; test via Wound pathway first.
- **DEC-086 (Creature signature-skill Starting Value):** **RULED — creature/NPC signature
  (signature-attack) skills are pre-built at FULL CAP as "veteran" content, NOT at canonical
  `floor(Cap/2)`.** Named/boss creature signature attacks start at Cap by design; general
  (non-signature) skills still use `floor(Cap/2)` or an author-assigned GM value.
- **DEC-087 (Pre-authored Tier-2 creature skills):** **RULED — creature/NPC templates may
  pre-author ready-made Tier-2 (Advanced) skills at creation** as a content-authoring
  convention; DEC-012's failed-Double origin rule applies to PC advancement, not creature
  template authoring. Preserves DEC-041's Skill-Tier ≥ 2 gate.
- **DEC-098 (C-06 — creature defensive-skill basis):** **RULED — CONDITIONAL ACCEPTANCE:
  Brawling is the DEFAULT defensive Skill for creature templates lacking an explicitly
  authored defensive Skill — NOT a universal Tiwas principle.** Any template may author a
  dedicated defensive Skill. Applies under DEC-077.A and to templates per DEC-087.
- **DEC-110 (C-05 — Regeneration/Regrowth magnitude vocabulary):** **RULED — content-
  authoring per creature** (B.10).
- **DEC-094 (C-04/G-04 + C-10 — passive/aura Frightened trigger):** **RULED — Option C:
  scene-state / Condition-Clause trigger via the DEC-088 grammar** ("Active only while
  [env:X] is present" + scene-state Tags); no probabilistic hidden special roll. **C-10
  Frightened magnitude folded into the DEC-079 Condition architecture** (`Tier-Y Frightened
  Value Z`, Z = −Y; Effect-Quality hard ceiling per DEC-035.B; Skill-Tier ≥ 2 gate).
  Frightened remains governed by DEC-079. Trigger is declarative; which creature declares a
  fear-source binding is content-authoring (DEC-077.A/DEC-085).

**Table-play with this block.** Automated characters = full PCs under the hood; tabletop
creatures = abbreviated stat blocks resolved at GM discretion. Conversions (BToV): advisory
drafts, Tiwa-ruled, provisional. Creature signature attacks start at full Cap and may be
pre-authored Tier-2; Brawling is the default defensive skill only where none is authored.
Blood Seep is single-shot, no DoT. Frightened binds via an `env:` scene tag. Name-brand
content (Goblin/Dragon/…): authored by Tiwa via playtesting.

---

# Part C — Explicitly NOT table-ready

This section lists, in full, the material that is **not** table-ready. No mechanics for
these items are included by design — listing them here ensures nothing Open is silently
included as if settled, and nothing confirmed-closed is re-opened or omitted.

## C.1 Content-authoring / deferred tracks (not table-ready; pointer-only)

- **Creature/campaign template instances** (Goblin, Dragon, other named content): content
  authored by Tiwa via playtesting (DEC-077); advisory conversions provisional until Tiwa
  rules (DEC-077.A, DEC-084). No stat blocks or templates are provided in this corpus.
- **Reaction trigger menus and the exact reaction-granting Tag vocabulary** (DEC-132 §4
  carried open): content-authoring per creature/class/equipment.
- **Crawl-speed base fraction** (half vs third) underlying DEC-125's `max(1, floor(Speed/2))`
  clamp: ordinary content-authoring (DEC-077.A).
- **Level 4–5 Location content lists** (organ selection, phalanx segmentation): alpha
  content-authoring, extensible under standing content policies (DEC-112 R4).
- **Band↔hex conversion boundaries** for DEC-133's four distance zones: content-authoring
  (DEC-077.A).
- **Non-escape Grappled movement interactions** (movement not away-from-grappler; holder
  initiating movement / dragging the victim): open content scope (DEC-131 carry).
- **Graded temperature** (cold vs freezing vs arctic) and the **scene-state tracking
  mechanism** (full Hazards/environment subsystem): open — DEC-088 scoped to binary
  `env:freezing` presence/absence only.

## C.2 Open gaps retained by the 2026-09-07/08 rulings

- **G1 — Movement-penalty magnitude table.** The empty cell in the G2 gap table. Whether
  Conditions beyond the fixed −Y overlay carry a magnitude *table* (vs a flat −Y) remains
  open. DEC-133 explicitly does not resolve it. Not table-ready.
- **G3 — Duration/time-unit scale.** No design decision on real-world duration per combat
  turn / scene / round / Extended-Test interval; DEC-133 keeps out of it and DEC-082 does not
  define it. Not table-ready.
- **Disengage; Zone of Control; Chase; generic movement contests; Forced Movement magnitude;
  Pin/Hold Position resolution; Seize/Deny Ground resolution.** Consciously left open by
  DEC-133 for the consuming mechanics (Position-tier Effects in DEC-023.A will act on the
  four-zone substrate once their resolution is ruled). Not table-ready.
- **Whether a reaction replaces or stacks with Active Defense on the same incoming Effect;
  per-scene/frequency limits on reactions** (DEC-132 carry). Not table-ready.
- **Numeric tier values for Conditions** (which Tier a given Condition instance receives),
  **precise Movement Speed reduction mechanics beyond −Y**, and **interaction resolution
  between Stunned and other action-denial Conditions** (DEC-079 carry). Not table-ready.
- **The unruled AoE nuance** from DEC-111: whether an AoE whose blast physically covers an
  incapacitated body still affects that body incidentally (selection-only vs
  coverage-exclusion semantics). Recorded, not assumed.

## C.3 Confirmed-closed items (resolved — listed so they are neither re-opened nor omitted)

| Item | Resolved by | Pointer |
|---|---|---|
| OPEN-003 (anatomical mapping) | DEC-041 + DEC-100 + DEC-112 + DEC-113 | Part B.4 |
| OPEN-004 (Tier-2 procedure/cost) | DEC-042 | Part B.2 |
| OPEN-005 (S-5…S-12 umbrella) | DEC-076/DEC-077 (closed 2026-09-01) | Part B.18 |
| OPEN-006 (wound-severity "thresholds") | DEC-035 (corrected) | Part B.4 |
| OPEN-007 (wound consequences) | Ruled (2026-08-30); magnitude architecture closed by DEC-035.A/B, DEC-107 | Part B.4 |
| OPEN-008 (non-attack Location Index generation) | DEC-037 | Part B.2 |
| OPEN-009 (S-6 positive-Effect mitigation) | DEC-050 amendment | Part B.6 |
| OPEN-010 (repeated-Defense fatigue) | DEC-075 (no fatigue system; future fatigue would be a selectable Condition-tier Effect) | Part B.6 / B.12 |
| C-01 (Inflict Injury magnitude) | DEC-096 + DEC-104 (contest-delta) | Part B.1 |
| C-02 (Active Defense mitigation amount) | DEC-097 + DEC-103 | Part B.1/B.6 |
| C-04 / C-10 (passive Frightened + magnitude) | DEC-094 | Part B.18 |
| C-05 (Regeneration/Regrowth vocabulary) | DEC-110 (content-classification) | Part B.10 |
| C-06 (creature defensive-skill basis) | DEC-098 | Part B.18 |
| C-07 (Quality-gated tier threshold) | DEC-099, then Design-Overridden by DEC-107 (Skill-Tier basis) | Part B.4 |
| C-08 (Location Tier-1 coarse-zone ranges) | DEC-100 | Part B.4 |
| C-09 (defender-wins consequence) | DEC-101 (+ DEC-109 coverage) | Part B.1 |
| DEC-080 carried-open items (hazards/tags/magic/extension) | DEC-114 | Part B.13 |
| DEC-085 carried-open Injury magnitude / conditional DR / Regen-with-Fright vocab | DEC-096/104; DEC-088; DEC-110 / DEC-094 | Parts B.1/B.10/B.13/B.18 |
| DEC-085 Item 4 (crawl fraction) | DEC-125 | Part B.12 |
| DEC-088 carried-open graded temperature & scene-state tracking | OPEN (not closed) | C.1 |
| DEC-108 carried-open corners (AoE composition; PC extension of exclusion) | DEC-111 | Part B.7 |
| G2 Items 1–5 and Item 3 deferred outcome | DEC-122, DEC-123, DEC-124, DEC-125, DEC-126, DEC-131 | Part B.12 |
| G4 (reactions blank) | DEC-132 (framework; trigger content deferred) | Part B.17 |
| G5 (movement granularity) | DEC-133 (spatial substrate; boundaries + contested movement deferred) | Part B.17 |
| GM Fiat universality pending markers (DEC-106/108/109/111) | DEC-130 (bounded universality) | Part B.17 |

## C.4 Standing-open tracking items (unchanged from the governance model)

- **Magic/special-abilities subsystem:** Reserved (Canonical §15; DEC-015 — Design Direction
  only). `magic:`/`ability:` namespace reserved with zero entries (DEC-114 R3); any list
  requires authorization with the Magic subsystem. Not table-ready.
- **G1 / G3** — see C.2 (explicitly open; do not treat as closed).

---

# Part D — Playtest Report Template

**How to use.** Copy the capture table per alpha session. For each subsystem row mark
whether the system was exercised, whether it worked as intended, add table-level
observations, and record a recommendation. The recommendation is a data marker
(Keep as-is / Needs Tiwa review / Flag for reopening) — filling it out does **not** rule on
anything; assessment happens during/after play and any actual reopening decision is Tiwa's
via the established governance path.

**Example entry (illustrative only — not a real log):**

| System | Exercised in session? (Y/N) | Worked as intended (Y/N/Partial) | Notes | Recommend |
|---|---|---|---|---|
| S-1 Opposed Contest / melee exchange | Y | Partial | Contest-delta HP and DEC-103 Effect mitigation both exercised | Needs Tiwa review |

**Capture table — session date:** ____________

| System | Exercised in session? (Y/N) | Worked as intended (Y/N/Partial) | Notes | Recommend: Keep as-is / Needs Tiwa review / Flag for reopening |
|---|---|---|---|---|
| S-1 Opposed Contest / melee-exchange algorithm (DEC-013, DEC-105) | | | | |
| Inflict Injury contest-delta HP (DEC-096, DEC-104) | | | | |
| Active Defense mitigation (DEC-097, DEC-103; DEC-044–050) | | | | |
| S-2 Zero-Step + §14.7 attack-side invocation (DEC-014, DEC-017, DEC-037, DEC-039) | | | | |
| S-3 Effect menu / enumeration / gating (DEC-023–030, DEC-023.A) | | | | |
| S-4 Wound/Injury + target selection + granularity (DEC-032–042, DEC-100, DEC-102, DEC-107, DEC-112, DEC-113) | | | | |
| S-5 Armor (DEC-058–062) | | | | |
| S-6 Defense (DEC-044–050, DEC-050 amendment) | | | | |
| S-7 Incapacitation/Death, uncapped HP (DEC-052–057, DEC-108) | | | | |
| S-8 Difficulty & 3rd-party adjudication (DEC-063–066, DEC-043, DEC-051-rejected) | | | | |
| S-9/S-10 Extended Tests (DEC-067–070) | | | | |
| S-11 Rest/Healing + Effect Heal System (DEC-071–074, DEC-121) | | | | |
| Encumbrance (DEC-078 + closed capacity/bands/penalties) | | | | |
| Conditions subsystem (DEC-079; G2 DEC-122–127, DEC-131) | | | | |
| Tags ontology + `env:freezing` + terrain (DEC-080, DEC-088, DEC-091, DEC-114) | | | | |
| Equipment state / Item records / Repair (DEC-081, DEC-118–121, DEC-128–129) | | | | |
| Time/Action economy & hazards (DEC-082, DEC-089–093) | | | | |
| Unified StateRecord schema (DEC-115–117) | | | | |
| Combat sequencing / initiative / creature multi-attack (DEC-095, DEC-106, DEC-111) | | | | |
| Reactions (DEC-132) | | | | |
| Movement granularity (DEC-133) | | | | |
| GM Fiat bounded universality (DEC-130) | | | | |
| Creature/NPC content — BToV conversions & stat blocks (DEC-076/077/077.A, DEC-083–087, DEC-098, DEC-110) | | | | |

---

# Appendix — Source pointers (pointer-reference only)

This corpus is compiled from the live repository at 2026-09-08 (register body read date;
register front matter last-modified 2026-09-07). Authoritative sources, from which every
rule above is drawn (no raw merge trail, survey transcripts, or hash-indexed evidence items
are included inline):

- `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` — D1, Core Locked Rules,
  internally **v1.4** (Part A: DEC-001–DEC-017, incl. §14.7).
- `_consolidation/decision-register.md` — the live decision register (Sections A–D,
  DEC-001–DEC-133 + amendment rows).
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
- `investigations/tiwas-grok-advisory-session-decision-report-s3-content-encumbrance-wound-precedence-2026-09-02.md`
  — DEC-078 (S-3 content, encumbrance, wound precedence).
- `investigations/tiwas-grok-advisory-session-reserved-systems-5-5-conditions-tags-equipment-timeaction-2026-09-02.md`
  — DEC-079, DEC-080, DEC-081, DEC-082 (§5.5 reserved systems).
- `investigations/tiwas-encumbrance-system-investigation-gpt5.6-luna-2026-09-06.md` and the
  Grok-4 / full-queue (ENC-I01–I10, v1 + v2) series — stored; ENC-F01 ratified by Tiwa.
- `investigations/tiwas-tag-condition-effect-unification-*` and `tiwas-unified-state-record-*`
  and `tiwas-tag-effect-condition-unification-*` (2026-09-06 series) — DEC-114–DEC-117
  advisory drafts and six-source comparison.
- `investigations/tiwas-g2-movement-denial-condition-advisory-session-2026-09-07.md` —
  G2/G3/G4/G5 gap table; DEC-122–127, DEC-131, DEC-132, DEC-133.
- `investigations/tiwas-eq1-eq2-item-creation-upgrade-repair-draft-2026-09-07.md`,
  `investigations/tiwas-equipment-tier-sunder-advisory-handoff-2026-09-07.md`,
  `investigations/tiwas-sunder-item-staterecord-proposal-2026-09-07.md` — DEC-118–121,
  DEC-128, DEC-129.
- 2026-09-04/05 playtest-collation ruling sources (Ice Troll v5/v6 prompts and reports;
  `tiwas-*designer-ruling-*2026-09-05.md` series) — DEC-094–113 (initiative, margins,
  quartiles, tier basis, HP floor, wound target selection, melee exchange, creature action
  selection, AD mitigation, no-DoT Blood Seep).

## DEC quick index (where each decision appears in this corpus)

| DEC(s) | Subject | Location |
|---|---|---|
| 001–017 | Core Locked Rules incl. §14.7 | Part A (A.1–A.17) |
| 007.A | Overflow-immutability | A.7 |
| 013, 031 | S-1; Quality/Skill-Tier entry gate (see DEC-107) | B.1 |
| 096, 104 | Inflict Injury = Winner's Margin; contest-delta never 0 | B.1 |
| 097, 105, 101 | AD mitigation = Defender's Margin; standardized melee exchange; defender-wins no counter-Effect | B.1 |
| 014, 037, 039, 040, 042 | S-2 Zero-Step; non-attack provenance; Extended-Test final roll; Tier-0 default/per-roll promotion; Tier-2+ secondary roll | B.2 |
| 023–030, 023.A | S-3 Effect menu, enumeration, gating | B.3 |
| 032–036, 035.A, 035.B, 041, 099, 100, 102, 107, 112, 113 | S-4 Wound/Injury; target selection; Skill-Tier basis; quartiles; granularity | B.4 |
| 058–062 | S-5 Armor | B.5 |
| 044–050, 075, 103 | S-6 Defense; no fatigue; Skill-Tier shred | B.6 |
| 052–057, 108, 109, 111 | S-7 Incapacitation; uncapped HP; AoE targeting | B.7 |
| 043, 051, 063–066 | S-8 Difficulty; rejected alternative | B.8 |
| 067–070 | S-9/S-10 Extended Tests | B.9 |
| 071–074, 110, 121 | S-11 Rest/Healing; Effect Heal System | B.10 |
| 078 | Encumbrance model (closed values 2026-09-06) | B.11 |
| 079, 122–127, 131 | Conditions subsystem; G2 movement-denial closures | B.12 |
| 080, 088, 091, 114 | Tags ontology; `env:freezing`; terrain; closure | B.13 |
| 081, 118–121, 128, 129 | Equipment state; Item records; Repair; EQ-1/EQ-2 | B.14 |
| 082, 089–093 | Time/Action; Hazards | B.15 |
| 115, 116, 117, 127 | Unified StateRecord schema; Tag record; counters/removal; naming | B.16 |
| 095, 106, 111, 132, 133, 130 | Combat sequencing; creature multi-attack; Reactions; Movement; GM Fiat | B.17 |
| 076, 077, 077.A, 083–087, 094, 098, 110 | S-12 creature/NPC content; BToV conversions; Frightened | B.18 |
| 018, 019 | Explicit-only objectives; structural weak points (re-affirmed closed) | C.3 (closed) |
| 020, 021, 022 | Non-attack deferral chain (closed / rejected / inert-dormant) | C.3 + pointer A.13–A.14 |
| 051 | Rejected alternative (mutual-failure stakes) | C.3 + B.8 |
| G1, G3, DEC-111 nuance, DEC-128 Q-carry, DEC-132 carry, etc. | Open — NOT table-ready | Part C |

**One-off notice (as required by the standing-prohibition overrule):** this file is a
dated, one-off, scoped exception for GM table use during alpha playtesting only
(2026-09-08). It is NOT to be periodically regenerated, and it does not lift the standing
"no single merged file" prohibition for any future task.