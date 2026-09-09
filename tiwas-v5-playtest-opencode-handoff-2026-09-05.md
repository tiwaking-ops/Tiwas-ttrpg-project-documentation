```yaml
document:
  title: "Tiwas TTRPG — v5 Ice Troll Combat Playtest: Session Decision Handoff for OpenCode"
  version: "1.0"
  status: "Advisory session record. NOT canonical. NOT a ruling. Assigns no DEC numbers."
provenance:
  author_llm: {name: "Claude", version: "Claude Sonnet 5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude", version: "Claude Sonnet 5"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
session_source:
  - "tiwas-ice-troll-combat-playtest-prompt-v5-2026-09-05.md (executed prompt)"
  - "tiwas-ice-troll-playtest-v5-report-2026-09-05.md (final report, this session)"
  - "tiwas-ice-troll-playtest-v5-result-2026-09-05.json (structured combat log, this session)"
recipient: "OpenCode (big-pickle) — for confirmation routing to Tiwa; no register action without Tiwa sign-off"
```

# Tiwas TTRPG — v5 Ice Troll Combat Playtest: Session Decision Handoff

## 0. Governance Statement (read first)

This document records **interpretive choices and gaps** encountered while executing the v5 Ice
Troll combat playtest prompt as Combat Referee/Simulation Engine. It contains:

- **Zero rulings.** Claude has no ruling authority over Tiwas mechanics.
- **Zero DEC numbers.** DEC numbers are assigned only by OpenCode against the live register, and
  only after Tiwa's explicit sign-off.
- **Four flagged items** requiring Tiwa's decision before any of them may be treated as settled,
  recorded as scaffold-for-reuse, or promoted toward a DEC candidate.

Per standing project practice, **OpenCode must not record any of the items below as a ruling,
scaffold precedent, or register entry until Tiwa has answered the corresponding question in
Section 2.** This document's role is to present the options and the precise question — not to
pre-select an answer on Tiwa's behalf.

---

## 1. Session Summary

**Task executed:** `tiwas-ice-troll-combat-playtest-prompt-v5-2026-09-05.md`, run in full by Claude
Sonnet 5 acting as Combat Referee/Simulation Engine, per the prompt's own role assignment.

**Outcome:** Combat resolved in 10 rounds. Adventurer-1 incapacitated at HP −5 (DEC-052/DEC-108).
Ice Troll ended at 671/705 HP. 78 Core Tests logged; 19 Wound applications; 11 both-fail repeats;
0 exact-Quality-tie repeats; 0 full Effect negations via DEC-103's carry rule.

**Rulings applied literally, without incident:** DEC-094 through DEC-110 as specified in the
prompt — turn order (DEC-095/106), the standardized exchange (DEC-105), Inflict Injury delta
(DEC-104), Active Defense shred (DEC-103), Wound Tier = Skill-Tier (DEC-107), Wound targeting
(DEC-102), Location quartiles (DEC-100), uncapped/negative HP (DEC-108), Brawling default defense
(DEC-098), and the passive Frightened Condition Clause (DEC-094) all executed deterministically and
required no rule invention.

**Four items could not be executed, or could only be executed by way of an unauthorized or
under-specified choice.** These are detailed below. All four are candidate discussion items only —
none is proposed as a ruling by this document.

---

## 2. Flagged Items — Questions for Tiwa

**Instruction to OpenCode: pose each numbered question below to Tiwa verbatim, in order, and
record only Tiwa's verbatim answer against each item. Do not summarize, do not infer an answer
from silence, and do not assign a DEC number until Tiwa has answered and explicitly authorized
recording.**

### OI-108 — Missing attribute formulas for Attack2 / Defence2 / Icy Claws / Sharktoothed Maw / Brawling

**What was found:** The v5 prompt specifies Skill Tier and Cap for these five skills but does
**not** state which specific attributes compose each Tier-2 (or Tier-1, for Brawling) formula.
DEC-102 (Wound target selection) requires that formula to determine which Body attribute a Wound
Effect penalizes. Without it, the Wound-consequence chain — which the prompt marks as **mandatory
to exercise at least once** — could not run at all.

**What Claude did (unauthorized scaffold, flagged, NOT proposed as a ruling):** Assigned attribute
pairs whose sums matched the prompt's stated Cap values exactly (so no other stat was altered):

| Skill | Assigned formula (scaffold only) |
|---|---|
| Attack2 | bpp (Might) + bps (Impact) |
| Defence2 | bep (Toughness) + bee (Vitality) |
| Icy Claws | bpx (Presence) + bee (Vitality) |
| Sharktoothed Maw | bpp (Might) + bep (Toughness) |
| Brawling (Tier 1) | bpp (Might) |

**Question for Tiwa:**

> "For the v5 Ice Troll playtest character build (Adventurer-1's Attack2/Defence2, and the Ice
> Troll's Icy Claws/Sharktoothed Maw/Brawling): should these skills' attribute formulas be
> (a) formally authored now, as content, so future playtests of this exact build are reproducible;
> (b) treated as a one-off scaffold specific to this single session, discarded afterward; or
> (c) something else? If (a), please specify or confirm the attribute pairs to use — the ones
> Claude guessed for this session (above) are placeholders only and were never authorized."

### OI-109 — DEC-104's "never 0 on a win" has no stated floor for an exact-margin tie

**What was found:** DEC-104 states Inflict Injury HP damage = Winner's Margin − Defender's Margin,
"never 0 on a win." In Round 5, Exchange 2 of this session, a decided attacker win (success/success,
attacker's margin higher than defender's on the S-1 comparison) nonetheless produced a raw
contest-delta of exactly 0, because the specific numbers happened to make Winner's Margin equal to
Defender's Margin at the HP-delta arithmetic step even though the attacker's margin was higher at
the win-determination step. [Note: this is possible because "who wins" is decided by comparing
Quality/Margin between two successes, while the HP delta is a separate subtraction — the two
comparisons can, in edge cases, disagree on whether the result is nonzero.] DEC-104 gives no
explicit floor or fallback for this case.

**What Claude did (unauthorized fallback, flagged, NOT proposed as a ruling):** Floored the result
to the attacker's own raw Margin (i.e., treated Defender's Margin as 0 for this single computation)
so the "never 0" clause held. This is Claude's own invented fallback, applied only to keep the
simulation running, and is explicitly not endorsed as the correct answer.

**Question for Tiwa:**

> "DEC-104 requires Inflict Injury damage to 'never be 0 on a win.' When the literal formula
> (Winner's Margin − Defender's Margin) computes to exactly 0 on a decided win, what is the correct
> floor or fallback value? Options observed during this session's execution: (a) floor to 1 HP;
> (b) floor to the attacker's own raw Margin (what Claude used, unauthorized); (c) floor to some
> other fixed minimum; (d) treat this as evidence that the underlying formula is mis-specified and
> needs revision, rather than patched with a floor. Please rule, or indicate this needs further
> investigation before a DEC candidate is drafted."

### OI-110 — Does an attacker win always produce HP damage (DEC-104) AND a Wound/Condition Effect (DEC-103) simultaneously, or are they mutually exclusive under DEC-024's "one Effect per win"?

**What was found:** The v5 prompt's "Ruled procedures summary table" lists "Attacker win → HP" and
"Attacker win → Effect" as two separate rows, without stating whether both resolve on every
attacker win (HP as an automatic combat-resolution channel, decoupled from the DEC-023/DEC-024
Effect-selection system) or whether they are alternatives — i.e., the winner picks **either**
Inflict Injury (HP) **or** a Wound/Condition Effect as their single DEC-024 Effect, not both.

**What Claude did (interpretive reading, flagged, NOT proposed as a ruling):** Read DEC-104's own
wording — "HP channel is fully separate from the DEC-103 negation table" — as support for the
concurrent reading, and applied **both** HP damage and a Wound/Condition Effect on every one of the
19 qualifying attacker wins this session. This reading was not confirmed by any single explicit
sentence in the supplied corpus; it is Claude's best-effort resolution of an apparent tension
between DEC-104's wording and DEC-024's older "flat one-Effect-per-win" rule.

**This is the single most consequential open item from this session** — it materially changes
every HP-damage number in the playtest report if the answer is "mutually exclusive" rather than
"concurrent."

**Question for Tiwa:**

> "Under the v5 ruling set (DEC-102 through DEC-110), when a combatant wins an opposed attack
> exchange, does the win always produce BOTH (a) Inflict Injury HP damage per DEC-104's
> contest-delta formula, AND (b) a separate Wound/Condition Effect per DEC-103's shred procedure —
> as two concurrent, independent consequences of the same win? Or does DEC-024's 'one Effect per
> win' still apply, meaning the winner must choose EITHER Inflict Injury (HP) OR a Wound/Condition
> Effect, not both? Claude assumed 'concurrent' for this session's playtest, based on DEC-104's
> 'HP channel is fully separate from the DEC-103 negation table' wording, but this was never
> explicitly ruled and should be confirmed or corrected."

### OI-111 — DEC-012's Advanced Skill starting-value sub-choice, for automated/creature Doubles

**What was found:** DEC-012 §1 item 4 offers two options for a newly created Advanced Skill's
starting value: (i) a fixed value of 1, or (ii) roll 1d100 and use `min(roll, New Cap)`. This is
framed in the corpus as a designer/player choice at the moment of creation. During this automated
playtest, both Adventurer-1 and the Ice Troll each triggered several qualifying failed Doubles
(6 total, none used as active combat actions this session), and an automated executor has no
player to make this choice on the spot.

**What Claude did (unauthorized default, flagged, NOT proposed as a ruling):** Defaulted to option
(i), starting value = 1, for every Advanced Skill created during this session, purely to keep
execution deterministic without a human present to choose.

**Question for Tiwa:**

> "For automated/unattended playtest execution (no human player present to make the DEC-012 §1
> item 4 starting-value choice at the moment an Advanced Skill is created via a qualifying failed
> Double), should the executor default to (a) starting value 1, (b) roll-and-take-min(roll,cap), or
> (c) something else — e.g., GM/Tiwa pre-declares a standing default for all future automated runs?
> This only affects automated/creature-side Advanced Skill creation; it does not touch PC-side
> Advanced Skill creation in live human play, where the player still makes the choice."

---

## 3. Items Explicitly NOT Flagged as Open (for completeness — confirmed working, no decision needed)

The following systems executed exactly as specified in the v5 prompt with no ambiguity encountered,
and require no action from Tiwa or OpenCode:

- DEC-095/DEC-106 turn order and creature multi-attack ordering
- DEC-105 standardized exchange (including both-fail and exact-tie repeat branches — both-fail was
  exercised 11 times; exact-tie was not exercised this session)
- DEC-100 Zero-Step quartile location resolution
- DEC-102's non-formula logic (random-selection-among-candidates mechanism itself, as opposed to
  which attributes are candidates — see OI-108)
- DEC-107 Effect/Wound Tier = Skill-Tier
- DEC-108 uncapped/negative HP recording
- DEC-098 Brawling default defensive skill
- DEC-094 Frightened application (the termination branch was not exercised, since the Ice Troll was
  never incapacitated this session — this is a coverage gap in the *test*, not a rule gap, and
  needs no decision, only a future playtest where the Troll loses)

---

## 4. Recommended Next Action (advisory only)

Once Tiwa has answered OI-108 through OI-111 above, OpenCode may draft DEC candidates for whichever
answers Tiwa authorizes recording, following the standard 8-step Promotion Rule / decision-register
process. Claude makes no recommendation as to outcome on any of the four items, consistent with its
advisory-only, no-ruling-authority role on this project.

**End of handoff.**
