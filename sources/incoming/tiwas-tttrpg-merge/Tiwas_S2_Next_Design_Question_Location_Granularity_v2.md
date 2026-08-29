# Tiwas — Next S-2 Design Question: Location Granularity Policy (Starter Brief v2.0)

**Use this to open a new chat.** Supersedes `Tiwas_S2_Next_Design_Question_Tier_Policy_v1.md` — same
underlying question, reframed and scoped more precisely after a second review.

---

## 1. What's already settled (don't re-litigate)

- **S-2 Tier-1 formula:** Zero-Step is the ruled, canonical Tier-1 Location Index provider. Deterministic,
  no player choice. Canonical Rules §14.1–§14.2.
- **E9 (physical-dice usability):** Passed, for the tested two-physical-d10 method specifically. Other
  input methods remain untested — §14.5.
- **Comparative derivation cost:** Units-Digit needs 0–1 extra operations across rolling modes, Zero-Step
  needs 1–2 — §14.6. Structural, not a human-usability finding.
- None of this is open for reconsideration here. Zero-Step is finished. This question treats it as a
  fixed input, not something to reopen.

## 2. The question, reframed

Not: ~~"When does a scene use Tier 0, 1, or 2?"~~

Instead: **What rule determines the required location granularity for a particular situation?**

The first framing quietly assumes the answer is "someone selects a tier." It might not be. The rule could
be automatic-by-action, automatic-by-declared-intent, scene-level, equipment-dependent, GM-adjudicated,
campaign-selected, or some combination. "Tier 0/1/2" is still the underlying vocabulary — this is about
not prematurely assuming *how* the selection happens.

## 3. Do this before generating candidate answers

**Establish design criteria first — what is each tier actually *for*, not just what it *is*:**

- **Tier 0:** not just "low-detail combat" — what information is deliberately being discarded, and why is
  that acceptable in the situations Tier 0 covers?
- **Tier 1:** the derivation mechanism is settled (Zero-Step); the open question is *what game situation
  creates a meaningful need for a location index in the first place* — ordinary attacks? called shots?
  position-dependent attacks? attacks on equipment? anything a later wound system will consume? formal
  duels? specific weapons? Treat these as candidates to test, not assumptions to build on.
- **Tier 2:** don't define it as "more granular Tier 1." It needs an articulated purpose — e.g., a
  medically/anatomically meaningful action where a generic index is insufficient. If that purpose can't be
  named, Tier 2 isn't ready to be designed yet, and that's fine — leave it reserved.

**Then ask which dimension granularity actually depends on:**

> Does location granularity represent a property of the scene, the action, the attacker, the target, the
> declared intent, or the consequence being resolved?

Three illustrative models, not an exhaustive list:

- **Scene-based** — "this combat uses Tier 1." Simple, potentially wasteful.
- **Action-based** — normal strike → Tier 0, called strike → Tier 1, surgical/precision action → Tier 2.
  Potentially elegant, risks player manipulation and added adjudication.
- **Consequence-based** — location isn't determined unless some rule actually needs it. Worth serious
  consideration: it's the model most naturally aligned with Priority 3 ("minimum resolution steps... without
  sacrificing Priority 1").

## 4. Explicit scope guards for the new investigation

- **Do not design the anatomical mapping table yet.** If a zone table (`01–10 Head, 11–30 Torso...`) gets
  designed before the granularity policy is settled, the table will start driving the architecture instead
  of the other way around. Correct order: location policy → location invocation → location provider →
  Location Index → anatomical mapping → wound/armor/effect consumers.
- **Do not touch Tier 2 mechanics, anatomical content, or downstream wound/armor/effect interaction.**
  Those are separate, later questions.
- **Do not treat this as a numerical-optimization problem the way Zero-Step vs. Units-Digit was.** There's
  no equivalent of "run 5,040 permutations" that settles this — it's a design/workflow question, not a
  statistical one.

## 5. Suggested process

1. Define the granularity-policy problem precisely, using §3–4 above.
2. Generate 3–4 concrete candidate policies (not abstract categories — actual proposed rules).
3. Walk each candidate through several concrete play scenarios.
4. Measure each against: resolution-step cost, table friction, player agency, GM burden, simulation
   granularity, exploitability, compatibility with future wounds/armor systems, and Priorities 1 and 3.
5. If one candidate clearly dominates, propose it. If not, present the remaining choice to the designer
   rather than forcing a single "winner."

## 6. Source documents

Canonical Rules & Changelog v1.3, Proposals/WIP v1.4, Implementation Roadmap v1.4. The Roadmap's
dependency-graph inconsistency (S-2/S-3 ordering) is now corrected as of v1.4; a separate, unresolved
architectural question about whether S-2 and S-3 should be modeled as sequential or parallel is flagged
there but deliberately not decided — unrelated to this brief, not blocking.
