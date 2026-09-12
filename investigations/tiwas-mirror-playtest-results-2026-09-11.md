---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test: Execution Results"
  version: "1.0 (executed run — not a ruling)"
  status: "Advisory / Non-canonical. No DEC assigned. Results, not a decision. Pending Tiwa review before any OpenCode recording action."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-11"
  source_brief: "tiwas-playtest-mirror-combat-design-brief-2026-09-10.md (v0.2)"
---

# Tiwas — Mirror-Match Combat Stress Test: Execution Results

**This document reports what a simulation did, not what Tiwas should do.** No DEC
number is implied by anything below. All numeric outputs are scaffold/playtest-only
per standing methodology. Nothing here resolves G1/G3, the DEC-112/DEC-113 Armor
Bypass contradiction, or any other open corpus item.

Full per-roll logs: `exchange_log_run_a_priority.csv` (80 rows) and
`exchange_log_run_b_random.csv` (108 rows). Dice via `random.SystemRandom()`.

---

## 1. What was run

Two variants of the brief's scenario, differing only in the offense-skill tie-break
(brief §8.4, explicitly flagged as *"invented for this brief, not derived from any
DEC"*):

| Run | Tie-break rule | Rationale |
|---|---|---|
| **A** | Fixed priority: Attack > Grapple > Trip > Disarm > Equipment Damage | The brief's own suggested default |
| **B** | Uniform-random among tied candidates | Alternate, to check whether Run A's outcome was an artifact of the specific tie-break choice |

Everything else follows the brief exactly: identical Alpha/Beta (all attributes 50,
HP 600, PE 150, all six skills Tier‑2/Cap‑50/Start‑25), Armor Bypass out of scope,
DEC‑105 melee-exchange algorithm, DEC‑104 contest-delta HP, DEC‑103 Skill-Tier
shred + margin de-escalation, DEC‑100 quartile zones, DEC‑114 R2 tag triggers,
DEC‑030 fail-and-fall-back, mandatory Defense, termination at first HP ≤ 0.

---

## 2. Headline finding (both runs)

**Once a skill is tested, it grows; untested skills never do — so whichever skill
"wins" the very first tie-break permanently locks in as that combatant's only
action for the rest of the fight.** This happens regardless of which tie-break rule
is used:

| Run | Alpha's skill choices | Beta's skill choices |
|---|---|---|
| A (priority) | **Attack** ×80 (100%) | **Attack** ×80 (100%) |
| B (random) | **Equipment Damage** ×52 (100% of Alpha's turns) | **Grapple** ×56 (100% of Beta's turns) |

In Run A, Attack wins the opening tie under the fixed-priority rule, then its value
climbs above the other four skills (still parked at Starting Value 25) on the very
first failed roll — after which Attack is *never* tied again, so the tie-break
clause is never re-consulted for the rest of the match. Grapple, Trip, Disarm, and
Equipment Damage are **never once selected** by either combatant in Run A.

In Run B, the random tie-break just relocates *which* single skill locks in
(Equipment Damage for Alpha, Grapple for Beta) — it does not prevent monoculture,
because the underlying cause isn't the tie-break rule at all: it's that **skill
value only increases via Failure XP on the skill actually rolled** (§4/Skill Roll
Pool mechanics), so a first-mover advantage of even +1 is self-reinforcing and
irreversible within a single combat. This is a structural interaction between
the offense-selection rule ("currently highest numeric value," brief §4.2 step 1)
and the Failure XP/Skill Roll Pool mechanic — not a bug in the brief's tie-break
choice specifically.

**Consequence for the brief's own test objectives (§9):** Run A silently fails to
exercise objectives 3–8 (Effect Tier/Magnitude, Skill-Tier shred, Zero-Step
location resolution, Tag+Location gating, Grappled/Break-Hold, Wound-target
selection) because only Inflict Injury (Attack) ever fires. Run B exercises more
of the mechanic stack (Grapple and Equipment Damage both fired) but *also*
locks each combatant to a single skill, so Trip, Disarm, and — on each
individual combatant — three of the five offense skills still never fire.

This is an emergent finding from running the brief as written; it is not a
proposed fix. Two directions this could go (not recommending either): (a) accept
that a mirror-match with this selection rule will always degenerate to
single-skill combat, which may itself be useful information about the "currently
highest value" heuristic outside playtest contexts too; or (b) if full mechanic
coverage in one scenario is the goal, a future brief would need either a forced
skill-rotation convention or several separate single-skill-pairing scenarios.

---

## 3. Run A — Fixed-priority tie-break

| Metric | Value |
|---|---|
| Termination | HP ≤ 0 (DEC-052) |
| Winner | **Alpha** |
| Rounds | 21 |
| Logged exchanges (incl. repeats) | 80 |
| Alpha final HP / PE | 393 / 77 |
| Beta final HP / PE | **−36** / 63 |
| Outcome distribution | repeat-bothfail 39, attacker-wins 21, defender-wins 20 |
| Effects fired | Inflict Injury ×21 (100%) |
| Tag checks | none attempted (Attack carries no location/tag gate) |
| Alpha Advanced Skills created | 3 (all off Defense, Tier‑3, Starting Value 1) |
| Beta Advanced Skills created | 8 (4 off Defense, 4 off Attack) |
| Alpha total Failure XP / General XP | 1,601 / 757 |
| Beta total Failure XP / General XP | 1,950 / 828 |
| Conditions ever applied | **0** (Grapple/Trip/Disarm/Equipment Damage never selected) |

Alpha's final Attack value 38 vs. Beta's 42, Defense 39 vs. 42 — Beta's skills grew
slightly higher on Failure XP, but Alpha won on variance (favorable roll sequence),
consistent with a pure d100 contest between near-identical combatants.

---

## 4. Run B — Uniform-random tie-break

| Metric | Value |
|---|---|
| Termination | HP ≤ 0 (DEC-052) |
| Winner | **Alpha** |
| Rounds | 30 |
| Logged exchanges (incl. repeats) | 108 |
| Alpha final HP / PE | 273 / 72 |
| Beta final HP / PE | **−8** / 66 |
| Outcome distribution | repeat-bothfail 47, attacker-wins 29, defender-wins 31, repeat-tie 1 |
| Effects fired | Impose Condition: Grappled ×14, Equipment Damage ×6, Equipment Damage→**fail-and-fall-back**→Inflict Injury ×9 |
| Tag-check results | pass 6, fail-and-fall-back 9, n/a (Grapple, ungated) 14 |
| Alpha Advanced Skills created | 9 (5 off Equipment Damage, 4 off Defense) |
| Beta Advanced Skills created | 6 (5 off Grapple, 1 off Defense) |
| Alpha total Failure XP / General XP | 2,169 / 962 |
| Beta total Failure XP / General XP | 2,552 / 1,345 |
| Conditions ever applied | Alpha caused 7 on Beta (Equipment Damage); Beta caused 13 on Alpha (Grapple + 1 stray) |

Notably, **Equipment Damage's Tag+Location gate (DEC-114 R2) actually mattered
here**: 9 of Alpha's 15 Equipment Damage wins landed on a struck zone (Legs or
Head) with no equipped item present, correctly falling back to Base Inflict
Injury per DEC-030. Only the 6 that landed on Arms (weapon) or Torso (armor)
produced a real Equipment Damage StateRecord. This is the run's only exercise of
the fail-and-fall-back path and the DEC-100/DEC-114 zone-tag interaction.

Grapple (ungated, per DEC-028's scope excluding it) applied a StateRecord on
every one of Beta's 14 wins with no fallback branch, confirming Grapple's
un-gated behavior as specified.

---

## 5. Test-objective coverage (brief §9)

| # | Mechanic under test | DEC(s) | Run A | Run B |
|---|---|---|---|---|
| 1 | S-1 melee-exchange algorithm, mandatory defense | 013, 105 | ✅ Exercised | ✅ Exercised |
| 2 | Contest-delta HP resolution | 096, 097, 104 | ✅ Exercised (21×) | ✅ Exercised (via fallback, 9×) |
| 3 | Effect Tier/Magnitude = Skill-Tier | 107 | ❌ Never fired | ✅ Exercised (Grapple, Equip. Damage) |
| 4 | Skill-Tier shred + margin de-escalation | 103 | ❌ Never fired | ✅ Exercised |
| 5 | Zero-Step + Tier-1 quartile location resolution | 014, 100 | ❌ Never fired | ✅ Exercised (15 location-referencing rolls) |
| 6 | Tag+Location gating / fail-and-fall-back | 028, 030, 114 | ❌ Never fired | ✅ Exercised (6 pass / 9 fallback) |
| 7 | Grappled imposition + contested Break-Hold escape | 079, 124, 131 | ❌ Never fired | ⚠️ Partial — Grappled applied 14×; **Break-Hold escape never attempted** (Grapple isn't an offense-pool "escape" action in this brief; no combatant ever tried to break free) |
| 8 | Wound target selection (automated/creature path) | 102 | ❌ N/A — no Wound Effect in scope (only Inflict Injury/Grapple/Trip/Disarm/Equip.Damage; "Impose Condition: Wounded" was never part of the §2 skill↔Effect pairing) | ❌ Same — not in scope either run |
| 9 | Incidental Advanced Skill creation, non-influencing | 012 | ✅ Exercised (11 total) | ✅ Exercised (15 total) |
| 10 | Armor Bypass | — | Out of scope (§8.5) | Out of scope (§8.5) |

Objective 8 (Wound target selection, DEC-102) was **never actually reachable by
either run** — not because of the tie-break issue, but because the brief's own
§2 skill→Effect table (Attack→Inflict Injury, Grapple→Grappled, Trip→Knock
Prone, Disarm→Disarm/Break Hold, Equipment Damage→Equipment Damage) never pairs
any offense skill with "Impose Condition: Wounded." This is a **gap in the
design brief itself**, separate from the tie-break finding, worth flagging back
to the brief if Wound-pathway testing (DEC-035.A record format, DEC-102 target
selection) is still a goal of this scenario family.

---

## 6. Modeling decisions made to execute the brief (flagged, non-canonical)

The brief left several points underspecified for actual execution; the following
choices were made to produce a runnable script. None of these are rulings —
they're implementation notes, listed so anyone reviewing the logs knows what a
given number means.

| # | Point | Choice made | Why |
|---|---|---|---|
| M1 | DEC-104 "never 0 on a win" | Interpreted as: if `Winner's Margin − Defender's Margin ≤ 0`, floor the result to **1** HP damage rather than 0 or negative. | The register states the delta is "never 0 on a win" without giving the floor value; 1 is the minimal reading that satisfies "never 0" without inventing a larger number. |
| M2 | DEC-103 cascade depth when the negation buffer goes very negative | Implemented as a **single** Tier‑decrement step (Tier −1, buffer reset to the new Tier value), not a repeated cascade proportional to how negative the buffer went. | DEC-103's text describes one Tier−1/Mag=new‑Tier transition and says "leftover margin lost" — read as capping the effect of a single large mitigation roll at one Tier step, not multiple. Since both combatants only ever use Tier‑2 skills in this scenario, the shred step is always the "Atk=Def" case (Mag −1), so this assumption is exercised, but the deeper cascading case (would matter for tier gaps >0) is not. |
| M3 | Zero-Step laterality parity (DEC-041(3)) | Applied **odd/even parity to the Location Index value itself** (post-swap), not to the pre-swap natural roll. | The rule text ("Zero-Step output digit-parity") reads most naturally as the post-swap output; this is the more literal reading but the alternative (pre-swap) is not ruled out by the cited text. |
| M4 | Held-item location for Tag-check purposes | Weapon (`state:held`, `slot:main_hand`) fixed at **Arms**; body armor (`state:worn`) fixed at **Torso**. | DEC-081 says held items take the Location of the holding limb; a held one-handed weapon is modeled as Arms, worn body armor as Torso, consistent with DEC-100's own zone names. No corpus text pins this down more precisely for the abstract Tier‑1 zone system. |
| M5 | Offense-skill tie-break (§8.4) | Two full runs, one per candidate convention (priority vs. random) — see §2. | The brief explicitly flags this as unresolved and invites either. |
| M6 | Initiative tie (identical Speed both combatants) | Re-rolled a fresh d100 comparison **every round** (not just once at combat start), per DEC-095 step 7's literal wording. | Speed never changed in either run (no Attribute Wound occurred), so this only affected turn order, not any numeric outcome. |
| M7 | Grapple/Trip Tag+Location gating | Modeled as **DEC-028 does not apply to Grapple or Trip** (that ruling's Tag+Location gate is explicitly scoped to Disarm/Break Hold, Equipment Damage, and Armor Bypass only) — so Grappled and Prone apply unconditionally on a win, no fallback branch. | Direct reading of DEC-028/DEC-114 R2's enumerated scope. |

---

## 7. Files produced

| File | Contents |
|---|---|
| `exchange_log_run_a_priority.csv` | Full 80-row per-roll log, Run A |
| `exchange_log_run_b_random.csv` | Full 108-row per-roll log, Run B |
| `mirror_playtest.py` | The executed simulation script (both runs, same code path, `tie_break` parameter only difference) |
| `summary.json` | Machine-readable summary for both runs |

---

## 8. Recommended next steps (advisory only)

- **If the goal is full single-scenario mechanic coverage:** the brief's offense
  selection rule needs a forced-rotation or weighted convention, not just a
  tie-break fix — Run B shows random tie-break alone doesn't prevent
  monoculture, it only changes which one skill monoculture forms around.
- **Wound pathway (Objective 8) is unreachable as the brief is currently
  scoped** — no offense skill in §2 is paired with Impose Condition: Wounded.
  A future variant would need to add that pairing (e.g., swap Attack's pairing,
  or add a seventh skill) if DEC-102 target-selection coverage is wanted.
- **Break-Hold escape (part of Objective 7) never triggers** because no
  combatant in this brief ever attempts to move away/escape a Grapple — the
  brief has no "escape" action in the offense pool. Worth flagging if DEC-124/
  DEC-131's contested Break-Hold machinery specifically needs exercise.
- The DEC-112/DEC-113 Armor Bypass contradiction remains untouched and open,
  exactly as the brief scoped it (§8.5) — not addressed by this run.

Everything above is advisory. No DEC is assigned, nothing is recorded to the
Decision Register, and no ruling is implied.
