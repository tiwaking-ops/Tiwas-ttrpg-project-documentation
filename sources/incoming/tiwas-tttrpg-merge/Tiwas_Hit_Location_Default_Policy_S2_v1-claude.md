# Tiwas — Hit-Location Default Policy (S-2, v1 — Draft, Not Locked)

**Status:** Draft. First pass only — produced for designer review and independent cross-review by
ChatGPT before any element is treated as canonical, mirroring the process S-1 (Opposed Contest
Resolution) went through before it was locked. **Nothing in this document is settled.** Comparative
Design Direction Brief §2.2 and Synthesized Roadmap §3.1 list "Hit-location policy: Tier 0/1/2 and
situation use" as Open, ranked residual S-2, dependency S-1 (now satisfied — S-1 is locked). This pass
closes only the tier-selection question and the precise mechanics of Tier 1's location derivation.
Wound-threshold formulas (S-4), Tier 2's detailed mechanics, and the anatomical location table itself
are explicitly out of scope and are not resolved here (§H).

**Source confirmation (per house method, checked before drafting):** all three required source
documents are present in the project: the Comparative Design Direction Brief, the Synthesized Roadmap,
and `Tiwas_Opposed_Contest_Resolution_S1_v1.md` (locked). A fourth project file,
`Tiwas_RPG_Project_Documentation_v1.pdf`, was also checked directly — it is the original v1 rules
document that Core Rules v2 supersedes (its content matches the "System Instruction" text block also
pasted into this session: no 100-Fumble override, no `max(0,…)` Failure-XP clamp, same Zodiact-animal
phrasing). It contains Sections 1–5 (Core Philosophy, Attributes, Derived Stats, Skills, Experience)
only — no combat, opposed-test, or location content of any kind, and in particular **no existing
location table anywhere in the project**. This document builds on Core Rules v2 and the locked S-1
document throughout, not the v1 phrasing.

---

## A. Relationship to Core Rules v2, S-1, and the Roadmap

Hit-location derivation is a **read-only, additive post-process** attached to an already-resolved test.
It consumes the historical Roll produced by an ordinary Core Test Transaction (Core Rules v2 §5) — or,
in a contest, one participant's Roll within the Universal Opposed Contest Procedure (S-1 §A–§B) — and
produces a second, independent value, the **Location Index** (defined in §C). It does not participate
in, and cannot modify, Cost, Outcome, Failure XP, Double-eligibility, or Recovery; those remain governed
entirely and unchanged by Core Rules v2 §5 / S-1 §B.

### A.1 Terminology collision: "Tier"

Core Rules v2 §4.1 already defines **Skill Tier** — the number of distinct attributes in a skill's Cap
formula, ranging 1–24. The hit-location system's **Tier 0/1/2** (Brief §2.2) is an unrelated,
independently scoped term for location-granularity level. The two uses share no formula and no numeric
relationship; they are a namespace collision only, not an interaction. This document always means
location-granularity Tier unless explicitly marked "Skill Tier." (Precedent: S-1 §H flagged an analogous
collision between "Hybrid Committed" and the unrelated "S-1D Committed/Guarded Stance" variant.)

### A.2 Dependency note, and a Roadmap inconsistency

Synthesized Roadmap §3.1 (Ranked Residuals) lists S-2's dependency as **S-1 only**, consistent with §5
(Residual-to-Roadmap Mapping: S-2 → Phase 2, preceding S-3 → Phase 3) and §6 (Phase 2 precedes Phase 3
in the phased roadmap). This document proceeds on that basis: S-1 is locked, so S-2's dependency is
satisfied.

For the record: Roadmap §4's prose dependency-graph chain lists "S-3 Outcome Effects" *before* "S-2
Location Interface," which conflicts with §3.1/§5/§6 above. This reads as a drafting inconsistency in §4
(likely because §4 compresses many parallel items into one linear narrative sequence) rather than a
considered re-ranking — §3.1's dependency column, the most granular and explicit statement, agrees with
§5 and §6, and is what this task's own framing also assumes. Flagged in §H for a future Roadmap cleanup;
it does not block this document.

### A.3 Why the source forbids a universal default

Brief §0 (Locked Priority Ranking) ranks **"Granular physical simulation… where the situation warrants
it"** as Priority 1 — the qualifier is load-bearing. A single global Tier would apply uniform granularity
regardless of situation, which is the thing Priority 1 explicitly does not ask for. That is the direct
reason Brief §2.2 and Roadmap Phase 2 both require situational, not universal, selection, and why this
document does not name a default anywhere (§E).

---

## B. The Location Provider Procedure

Location derivation wraps the Core Test Transaction / Opposed Contest without altering either:

```
      Core Test Transaction              Opposed Contest (S-1 §B)
       (Core Rules v2 §5)                 — two Core Tests, then
   Roll → Outcome → Cost →                    outcome matrix
 Failure XP → Recovery                             │
     (unchanged by S-2)                            │
              └───────────────┬────────────────────┘
                               │
                  Did a hit occur? (trigger condition
                 belongs to future combat/Effect rules
                     — not defined by S-2; see §H)
                               │
                    no ────────┼──────── yes
                     │                     │
                (nothing              Location Tier flag
                 happens)              (§D.3), set per
                                       scene by the GM
                                             │
                    ┌────────────┬───────────┴───────────┐
                    │            │                        │
                 Tier 0       Tier 1                   Tier 2
              no location   compute Location         procedure not
                 state      Index from hitting        defined this
                            side's own natural Roll     pass (§H)
                            via §C.2 / §D.1–D.2
                                     │
                        Location Index → handed to
                     S-3 / S-4 / S-5 / Setting-table
                    systems for consumption (§H, §I)
```

The Location Tier flag and the Location Index it produces sit **entirely outside** the Core Test
Transaction's data. Switching Tier 0↔1↔2 changes only whether a post-hoc derived value is computed; it
cannot be wired back into Roll, Cost, Outcome, Failure XP, Double-eligibility, or Recovery — this is true
by construction (§G), not by convention, since nothing in §C or §D touches those fields.

**Location Index (definition):** the integer output of a Tier-1 (or Tier-2) derivation procedure,
computed once per hit from that hit's own historical Roll. It is **not** itself a body-part label.
Mapping a Location Index onto a named anatomical zone requires a location table, which does not
currently exist in any project document and is out of scope here (§H).

---

## C. Tier Definitions

### C.1 The three tiers (restated from Brief §2.2)

| Tier | Model | Resolution Cost | Simulation Fidelity | Recommended Situational Use |
|---|---|---|---|---|
| **0** | No locations; Quality maps to global HP/conditions only | Lowest | Lowest | Mass brawls, cinematic fights, social-only scenes |
| **1** | Lightweight derivation from the existing attack roll; no extra die | Near-zero extra steps | Medium-High | Standard simulation-grade play, formal duels |
| **2** | Full location/armor/surgery trees | Higher (exact cost undefined — §H) | Highest | Optional gritty module only |

Tier 0 requires no formalization: no Location Index is ever computed, and no location state exists for
the scene. Tier 2 is named and scoped by source (Brief §2.2, Roadmap Phase 2) but its internal mechanics
are not defined by either source document and are not invented here (§H) — this document only
establishes that Tier 2 exists as a category and where it sits relative to 0 and 1.

### C.2 Tier 1: candidate derivation methods

Brief §2.2 names two candidates in the same sentence — "units digit or reverse digits of the attack
roll" — without ranking them against each other. Brief §9 additionally names the reverse-digit method
**"Zero-Step"** (attributed to Gemini 3.1-pro), a name Roadmap §8 step 5 also uses ("Zero-Step or digit
derivation"). Both names are reused here rather than invented.

Both methods are pure functions of the single historical Roll `R` already produced by the governing Core
Test / Opposed Contest. Neither introduces a new die. Both are formalized below; the base derivation is
a direct, essentially forced reading of the source's own description (not a judgment call). The one
genuine fork in each — how to handle the edge case where digit math would otherwise produce 0 — is
separated out as a proposed ruling in §D, since real alternatives exist there.

| Method | Effective output range | Behaves like a free… | Extra dice |
|---|---|---|---|
| **Zero-Step** (reverse-digit) | 1–100 | …second d100 | 0 |
| **Units-Digit** | 1–10 | …d10 | 0 |

**Zero-Step, base formula (R = 1–99):** write `R` as digit pair `(T, U)` where `T = floor(R / 10)`
(tens) and `U = R mod 10` (units) — e.g. `R=47 → (T,U)=(4,7)`. Location Index `L = 10×U + T` — i.e.,
swap the two digits. `R=47 → L=74`.

**Units-Digit, base formula:** Location Index `L = R mod 10` — e.g. `R=47 → L=7`.

`R = 100`'s digit pair, and the `R mod 10 = 0` case, are edge cases neither base formula resolves on its
own; §D.1/§D.2 propose specific rulings for both.

---

## D. Proposed Rulings (not locked — for designer sign-off + cross-review)

Unlike S-1 §D (which recorded rulings already reviewed and closed), the rulings below are **first-pass
proposals**. Each is precise and implementable as written, but none should be treated as settled until
the designer confirms it and it clears independent review.

### D.1 Zero-Step: handling R = 100

**Proposed ruling:** treat `R = 100`'s digit pair as `(0, 0)` (per Core Rules v2 §1's own "00 is read as
100, never 0" convention) and rule that the *reversed* pair is read the same way: `L = 100`, not `L = 0`.

This is not so much a new invention as an extension of an existing convention into territory Core Rules
v2 never anticipated (a second reading of a `(0,0)` pair, post-reversal) — Core §1 only specifies how to
read the *original* roll. Flagged as a ruling rather than "established" for exactly that reason: it's a
reasonable, consistent extension, not a re-derivation of something the source already settled.

**Consequence, verified by exhaustive enumeration** (all 100 possible Roll values, not sampled — see
§F): under this ruling, Zero-Step is a complete **bijection** on {1, …, 100} — every Location Index
1–100 is produced by exactly one Roll value, and vice versa. Its fixed points — Rolls where `L = R` —
are exactly `{11, 22, 33, 44, 55, 66, 77, 88, 99, 100}`, which is *exactly* the Core Rules v2 §1.1
Doubles set. This is a direct structural consequence of digit-reversal being an involution combined with
this ruling, not a coincidence requiring separate justification, and it changes no Core mechanic —
Double-eligibility and Advanced Skill triggers are entirely unaffected; this is a descriptive alignment
between two independently-defined sets, worth recording because the alternative ruling below would have
broken it.

**Alternative considered and set aside:** leaving `R=100 → L=0` (or treating it as invalid/out-of-range)
was considered. It isn't wrong, but it breaks the bijection, produces a Location Index (0) with no
natural table entry, and discards the Doubles-alignment property above for no stated benefit. Set aside
in favor of the proposal above; flagged for sign-off, not asserted as forced.

### D.2 Units-Digit: handling R mod 10 = 0

**Proposed ruling:** label the zero-remainder bucket **10**, not 0 — i.e., `L = 10` whenever
`R mod 10 = 0` (covering R ∈ {10, 20, 30, …, 90, 100}), giving output range {1, …, 10} rather than
{0, …, 9}.

This is a pure labeling choice — it doesn't change which Rolls land in that bucket, only what the bucket
is called (consistent with the project's general avoidance of zero-valued results: Core §1's "00 means
100" convention, Core §6.4's Skill-0 handling). Materially lower-stakes than D.1: unlike Zero-Step,
Units-Digit has no bijection or Doubles-alignment property to preserve or break, so the two labeling
choices are behaviorally identical except for the digit used to name the bucket. Recorded as a ruling
only for completeness and consistency with D.1's convention, not because it's a consequential fork.

**Note on R = 100 specifically:** under this ruling, R=100 (the universal Fumble, and a Double) falls
into the same units-digit bucket as the eight ordinary non-Fumble, non-Double rolls 10/20/…/90. Nothing
in source requires the Fumble to be distinguishable at the location layer, and this document proposes no
special-case beyond the ruling above — but flags that a table using Units-Digit will not, on its own,
mark a Fumble hit as anatomically special. If that distinction matters at a given table, it would need
to be added by whatever system consumes the Location Index (S-4/S-5/Setting), not by this derivation.

### D.3 How Tier selection is signaled

**Proposed mechanism: a single-valued, scene-level configuration flag**, `Location Tier ∈ {0, 1, 2}`.

- **Authority:** set by the GM (default authority; a setting module could delegate this, not addressed
  here), guided by — not bound to — §E's situational table.
- **Timing:** set **before** any test in the scene that could produce a hit is rolled. Roadmap Phase 2's
  acceptance criterion "location selection never changes the original attack roll" is read here to
  extend one step further: it also never *retroactively reinterprets* a roll already made. A mid-scene
  tier change (e.g., a formal duel at Tier 1 degenerating into a chaotic brawl, dropped to Tier 0) only
  affects rolls made **after** the change; earlier rolls in the same scene keep whatever Location Index
  (or absence of one) they already produced.
- **Scope:** persists for the scene/encounter unless the GM explicitly changes it.

**Open extension, not required or forbidden by source:** whether Tier could instead be assigned
*per-combatant* within a single scene (e.g., a tracked boss at Tier 1, background mooks left at Tier 0)
is not addressed by Brief §2.2 or Roadmap Phase 2, both of which frame Tier by *situation* (a scene-level
descriptor: "mass brawls," "formal duels"). Nothing here forbids per-combatant granularity — Roadmap's
own U-09 framing ("location provider interface," pluggable) would comfortably support it — but it is not
asserted as part of this proposal. Flagged for designer discussion (§J).

---

## E. Selecting a Tier

Restated directly from Brief §2.2, unmodified:

| Tier | Recommended situations | Why (Brief §2.2 / §0) |
|---|---|---|
| **0** | Mass brawls, cinematic fights, social-only scenes | Lowest cost, lowest fidelity — per-hit location tracking is overhead a large-cast or non-physical scene doesn't need |
| **1** | Standard simulation-grade play, formal duels | Medium-High fidelity at near-zero cost — matches the Priority-1/Priority-3 balance (§A.3) most directly |
| **2** | Optional gritty module only | Highest fidelity, highest cost — reserved for tables that explicitly opt into surgical/armor granularity |

**This table is guidance, not a default.** No tier is designated "the" default anywhere in this
document — per the explicit source constraint ("do not impose a universal Tier 0/1/2 default," Roadmap
Phase 2; "do not lock S-2 prematurely," Roadmap §9.2) — including Tier 1, even though Brief §2.2's own
language ("standard… play") makes it the closest thing to a general-purpose case. Actual selection is
per-scene, per §D.3, at GM discretion.

**GM override authority** is retained, consistent with S-1 §E's identical closing principle: this table
does not bind a GM whose scene doesn't fit its categories cleanly.

**Unconfirmed observation, flagged for cross-review only — not a rule:** Brief §2.2's Tier 1 situations
("formal duels," "standard simulation-grade play") and S-1 §E's Margin-mode situations ("precision /
efficiency… shooting, lockpicking, stealth") both cluster around controlled, deliberate scenes, while
Tier 0's "mass brawls" and Blackjack's "force / commitment… arm wrestling, shoving" both cluster around
chaotic or high-commitment ones. This may or may not reflect an intended pairing between Quality-mode
selection (S-1) and Tier selection (S-2) — nothing in either source document states this explicitly, and
this document does not act on it. Noted only because it's a legitimate design question worth putting in
front of the designer and ChatGPT, not because it should be assumed true.

---

## F. Tested Properties

**Methodology note:** unlike S-1's contest-outcome validation (which needed Monte Carlo simulation
because contest dynamics involve interacting probability distributions across paired Skill values,
multiple rounds, and threshold conditions — a space too large to enumerate), the claims below concern a
single, small, finite input space: the 100 possible Roll values. That space was **exhaustively
enumerated**, not sampled. Complete enumeration is strictly stronger evidence than any sampling pass
could be for a claim of this kind, so no `numpy`/seed methodology is used or needed here.

| Property | Result | Method |
|---|---|---|
| Zero-Step is a bijection on {1,…,100} | **Confirmed.** Every Location Index 1–100 produced by exactly one Roll | Exhaustive enumeration, R = 1–100 |
| Zero-Step fixed points = Core Doubles set | **Confirmed exactly.** `{11,22,33,44,55,66,77,88,99,100}` in both cases | Exhaustive enumeration |
| Units-Digit output is uniform over 10 buckets | **Confirmed.** Each of buckets 1–10 receives exactly 10 of 100 Rolls (10% each) | Exhaustive enumeration |
| Neither method ever modifies R | **Confirmed by construction** (§G) — R is read, never reassigned, by either formula | Direct inspection of both formulas |
| Both methods require zero extra dice | **Confirmed** — both are pure functions of the already-resolved Roll | Direct inspection |

### Resolution-step comparison (source-derived, not simulated)

| Tier | Additional steps beyond the Core Test Transaction | Additional dice | Source |
|---|---|---|---|
| 0 | 0 | 0 | Brief §2.2 ("Lowest" cost); Roadmap ("Tier 0 works without any location state") |
| 1 | 1 (single deterministic arithmetic step, applied to data already in hand) | 0 (Roadmap acceptance criterion: "No extra die is mandatory for Tier 1") | Brief §2.2 ("near-zero extra steps") |
| 2 | Not specified in source ("Higher," exact count undefined) | Not specified | Brief §2.2; deferred (§H) |

### Qualitative fidelity ordering

Tier 0 < Tier 1 < Tier 2, restated directly from Brief §2.2's own Simulation Fidelity column
(Lowest / Medium-High / Highest) — not independently re-derived, since fidelity in the quantitative sense
(does adding locations actually change simulated outcomes) requires S-4 and is explicitly not tested
here (§H).

---

## G. By-Construction Guarantees

These hold directly from how §C/§D are written, without needing separate empirical confirmation:

- **Location derivation never touches R.** Both formulas in §C.2/§D take `R` as a read-only input;
  neither assigns back to it. Cost, Outcome, Failure XP, Double-eligibility, and Recovery are computed
  exactly as Core Rules v2 §5 / S-1 §B already define, from the same unmodified `R`.
- **The Location Tier flag cannot reach the Core transaction.** It is external configuration state
  (§D.3) consumed only by the optional location-derivation step in §B's diagram; nothing in §C/§D writes
  to Roll, Cost, Outcome, or Recovery.
- **Both derivations are deterministic.** For a fixed `R`, Zero-Step and Units-Digit each always return
  the same `L`. There is no hidden randomness beyond the original Roll already spent by the governing
  test.
- **Tier 0 requires no location state by definition** (§C.1) — there is nothing to construct.

### Roadmap Phase 2 acceptance criteria — traceability check

| Roadmap Phase 2 criterion | Where satisfied |
|---|---|
| No extra die is mandatory for Tier 1 | §C.2 table; §F confirms both methods are 0-extra-dice by inspection |
| Tier 0 works without any location state | §C.1 |
| Tier 2 can support granular injury | **Not verified this pass** — Tier 2 mechanics undefined (§H) |
| Location selection never changes the original attack roll | §G above; extended to non-retroactivity in §D.3 |
| Location policy can change without changing the Core transaction | §B diagram; §G above |

---

## H. Explicitly Deferred / Out of Scope

Per Roadmap Phase 2's own simulation gate ("resolution steps; wound frequency; location distribution;
lethality; Priority-1 simulation fidelity") and the task's scope instruction: some of this gate
**cannot** be meaningfully evaluated without S-4, and this document says so rather than filling in
placeholder numbers.

| Item | Why deferred | Depends on |
|---|---|---|
| Wound frequency | No wound-activation model exists yet | S-4 |
| Lethality | No death/incapacitation model exists yet | S-4, S-7 |
| Quantitative Priority-1 fidelity (does Tier 1/2 actually change simulated outcomes, and by how much) | Requires a consuming wound model to measure against | S-4 |
| Tier 2 detailed mechanics (armor/surgery trees, its resolution-step count, its own distribution) | Brief/Roadmap name it as a category but define no internal mechanics | Future dedicated pass |
| The anatomical location table itself (zone names, weights, which Tier-1 method a given table uses) | No such table exists in any project document (confirmed via the v1 PDF check, preamble). Roadmap Phase 12 explicitly lists "location tables" among what **Setting Modules** may add — this may not even be Universal-Play/Core scope at all | Setting Module design, and/or Tier 2's own build-out |
| Interaction with the "Choose Location" Outcome Effect (Brief §4, item 10: "only if locations module active") | Whether a contest winner can spend Quality/Net Advantage to override the automatic Location Index from §C/§D is Effect-purchasing mechanics | S-3 |
| Per-combatant (vs. per-scene) Tier granularity | Plausible, not addressed by source either way | Designer discretion (§D.3) |
| Which Tier-1 sub-method (Zero-Step vs. Units-Digit) a given table actually uses | Contingent on the granularity of a location table that doesn't exist yet | Same as location table, above |
| Roadmap §4 dependency-chain ordering vs. §3.1/§5/§6 (§A.2) | Minor documentation inconsistency, not a blocking issue | Roadmap cleanup, out of band |

---

## I. Quick Reference

For downstream systems (S-3 Effects, S-4 Wounds, S-5 Armor, Setting location tables) that just need the
operational procedure:

1. GM sets `Location Tier ∈ {0, 1, 2}` for the scene, before any relevant roll, guided by §E — no tier
   is a mandated default.
2. Every test resolves as an ordinary, unmodified Core Test Transaction (Core Rules v2 §5) or Opposed
   Contest (S-1 §B). Location Tier has no effect on this resolution.
3. **Tier 0:** stop here. No Location Index is computed; no location state exists.
4. **Tier 1, on a hit** (trigger condition defined by future combat rules, not here): compute the
   Location Index from the hitting side's own natural Roll, using whichever method (§C.2) the table has
   selected — Zero-Step: `L = 10×U + T` (`L=100` if `R=100`); Units-Digit: `L = R mod 10` (`L=10` if
   that's 0).
5. **Tier 2, on a hit:** procedure not defined by this document (§H).
6. The Location Index is handed to whatever system consumes it (S-3's "Choose Location" Effect, S-4
   Wounds, S-5 Armor, a Setting-Module table) — not resolved here.
7. Tier may change between scenes, or mid-scene at GM discretion, but never retroactively reinterprets
   rolls already made (§D.3).

---

## J. Review Status

| Element | Status |
|---|---|
| Tier 0/1/2 definitions (§C.1) | Established — directly restated from Brief §2.2, not a judgment call |
| Zero-Step base formula (§C.2) | Established — the only sensible formalization of "reverse digits" |
| Units-Digit base formula (§C.2) | Established — the only sensible formalization of "units digit" |
| Zero-Step R=100 handling (§D.1) | **Proposed** — awaiting sign-off; alternative considered and recorded |
| Units-Digit zero-bucket labeling (§D.2) | **Proposed** — low-stakes labeling choice, awaiting sign-off |
| Tier-selection signaling mechanism (§D.3) | **Proposed** — scene-level flag, GM authority, non-retroactive |
| Per-combatant Tier granularity | **Open extension** — not proposed as part of this ruling, flagged for discussion |
| Situational selection guidance (§E) | Restated from source — explicitly not a universal default, per source constraint |
| Uniformity / bijection / Doubles-alignment properties (§F, §G) | **Verified** by exhaustive enumeration (all 100 Roll values) |
| Resolution-step comparison, Tier 0/1 (§F) | Established (source + direct inspection) |
| Wound frequency, lethality, quantitative Priority-1 fidelity | **Explicitly deferred** — requires S-4, not tested or guessed at here |
| Tier 2 detailed mechanics | **Deferred** — future dedicated pass |
| Anatomical location table content | **Deferred** — likely Setting-Module scope (Roadmap Phase 12), not S-2 |
| S-3 "Choose Location" Effect interaction | **Flagged dependency**, not resolved |

**Nothing in this document is locked.** It is a first-pass proposal, structured to match S-1's density
and rigor, for the designer's own review and then independent cross-review by ChatGPT — the same
two-step process S-1 went through before its §I acceptance table could say "Locked" anywhere.

### Proposed for cross-review

1. **D.1 — Zero-Step's R=100 → L=100 ruling** and its Doubles-alignment consequence: is extending the
   "00 reads as 100" convention to a reversed pair the right call, or should R=100 instead get a
   distinguished / forced location result given its Fumble status?
2. **D.3 — Tier-signaling mechanism**, specifically the open per-combatant-granularity extension: worth
   formalizing now, or hold until a concrete scene exposes the need?
3. **A.2 — the Roadmap §4 vs. §3.1/§5/§6 dependency-ordering inconsistency**: confirm §3.1's reading is
   the intended one, and flag §4 for a wording fix in a future Roadmap revision.
4. **§E's unconfirmed Quality-mode/Tier correlation observation**: worth stating as guidance somewhere,
   or better left unstated until it's tested?
5. Whether the Tier-1 sub-method choice (Zero-Step vs. Units-Digit) should be pinned now as a second
   situational-selection table (mirroring S-1 §C/§E), or genuinely has to wait on a location table that
   doesn't exist yet, as proposed in §H.

**Next, if S-2 closes:** S-3, Outcome Effect trigger thresholds — same situation-dependent treatment,
same "don't lock prematurely" discipline that served S-1 and this pass.
