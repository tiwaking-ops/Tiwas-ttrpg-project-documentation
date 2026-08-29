# Tiwas — Hit-Location Default Policy (S-2, v1.1 — Draft, Not Locked)

**Status:** Draft. Revised once, incorporating two rounds of independent cross-review (ChatGPT) since
v1 — see Closure changelog below. **Still not locked, and not yet eligible to be:** the agreed
three-stage process is (1) this revision, (2) an independent review of *this* revision, v1.1, not v1,
(3) only then the candidate-table comparison experiment, and only after that any locking discussion.
Comparative Design Direction Brief §2.2 and Synthesized Roadmap §3.1 list "Hit-location policy: Tier
0/1/2 and situation use" as Open, ranked residual S-2, dependency S-1 (satisfied — S-1 is locked). Scope
remains the tier-selection question and Tier 1's derivation mechanics; wound thresholds (S-4), Tier 2's
detailed mechanics, and the anatomical location table remain out of scope (§H).

**Source confirmation:** unchanged since v1 — see v1's own preamble for the full check. In short: the
Brief, the Roadmap, and locked S-1 are all present and current; a fourth project file
(`Tiwas_RPG_Project_Documentation_v1.pdf`) is the superseded v1 rules doc and contains no location
content of any kind.

**Closure changelog (v1 → v1.1):** incorporates Claude's own synthesis plus two rounds of ChatGPT
review. This is a **revision pass, not a locking pass** — see the status note above.
1. §B: added an explicit boundary/pipeline statement — S-2 provides a Location Index; it does not
   define what that index means. Previously this was scattered across several mentions rather than
   stated once, in one place.
2. §D.1: added a synthesis note — the bijective `100→100` ruling and a downstream "the Fumble gets
   forced/special treatment" rule are not mutually exclusive. A consuming system can add the latter
   without touching this document's math.
3. §D.3: reframed from a single scene-level scalar flag to a **Location Provider interface**
   (`Provider(context) → Tier`), matching Roadmap U-09's own naming rather than narrowing it to one
   implementation. Scene-level constant-function selection remains the recommended default; per-combatant
   or per-action selection is now a natively-supported implementation of the same interface, not a
   bolted-on extension.
4. §C.2: added an explicit Zero-Step/Units-Digit trade-off paragraph, and a disclaimer that formalizing
   "reverse digits" / "units digit" precisely does not, by itself, select either method for actual play.
5. §H: added an explicit row naming Armor interaction as an S-5 dependency (Roadmap Phase 4.1: "Location
   interaction"), previously left implicit in general "downstream systems" language.
6. §H/§J: updated the per-combatant-granularity item to reflect that D.3's revised interface now
   supports it architecturally; whether §E's situational guidance should also recommend it stays open.

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
                (nothing              Location Provider
                 happens)             resolves Tier for
                                      this hit (§D.3) —
                                     scene-level by default
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

The Location Provider's output and the Location Index it produces sit **entirely outside** the Core Test
Transaction's data. Switching Tier 0↔1↔2 changes only whether a post-hoc derived value is computed; it
cannot be wired back into Roll, Cost, Outcome, Failure XP, Double-eligibility, or Recovery — this is true
by construction (§G), not by convention, since nothing in §C or §D touches those fields.

**Location Index (definition):** the integer output of a Tier-1 (or Tier-2) derivation procedure,
computed once per hit from that hit's own historical Roll. It is **not** itself a body-part label.
Mapping a Location Index onto a named anatomical zone requires a location table, which does not
currently exist in any project document and is out of scope here (§H).

**S-2's boundary, stated explicitly (added v1.1):** S-2 selects/provides a Location Index. It does not
define what that index *means*. This document resolves only the first row below:

| Stage | Transformation | Owner |
|---|---|---|
| **S-2 (this document)** | `Roll → Location Index` | Resolved here |
| Setting / location table | `Location Index → named zone (Head, Torso, …)` | Not yet built (§H) — likely Setting-Module scope |
| S-3 | `Quality/Effect → possible location override` ("Choose Location," Brief §4 item 10) | Open (§H) |
| S-4 | `Location + Damage → Wound` | Open |
| S-5 | `Location + Armor → armor interaction` (named "Location interaction," Roadmap Phase 4.1) | Open (§H) |

Each downstream stage is free to consume the Location Index however its own design requires; this
document guarantees only that a well-defined integer exists for them to consume when Tier ≥ 1.

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
a direct, essentially forced reading of the source's own *description* (not a judgment call) — that is
a claim about what the words "reverse digits" / "units digit" can only reasonably mean, and it implies
**nothing** about which method should actually be selected for play. That selection is a separate,
open question (§H, §J).

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

**Trade-off, not hierarchy (added v1.1):** neither method is inherently better — usefulness depends
entirely on a location table that doesn't exist yet (§H). Units-Digit's ten buckets need no further
processing if a table lands on, or evenly divides into, ten zones — but 10's only divisors are 1, 2, 5,
and 10, so tables of other sizes (a 6-zone table, for instance) force uneven bucket-grouping. Zero-Step's
continuous 1–100 range can be cut into proportional ranges for *any* zone count, including weighted,
non-uniform ones, but it always requires that binning step — the raw Location Index is never itself the
zone. Resolving this trade-off needs both methods tested against actual candidate tables, not just their
raw output distributions in isolation (§H, §J item 5).

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

**Synthesis note (added v1.1):** the choice is not strictly binary between "preserve the elegant
bijection" and "give R=100 special location behavior" — those aren't mutually exclusive. R=100 is
already distinguished at the Core level (forced Failure, guaranteed Double) independent of anything this
document does. A downstream system (S-4 wound severity, S-5 armor/vitals) could still rule that a
Fumble-triggered hit gets forced/critical treatment *regardless* of which Location Index the derivation
produced — e.g., "if the triggering Roll was 100, treat as a vital-zone hit regardless of L." That would
preserve this ruling's clean, bijective, Doubles-aligned math while still letting the Fumble carry extra
weight wherever it's actually consumed. This document takes no position on whether that downstream rule
should exist — it only notes that this ruling doesn't foreclose it.

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

**Proposed mechanism (revised v1.1): a Location Provider**, not a single global scalar — a resolution
step returning `Location Tier ∈ {0, 1, 2}` given a context. This follows Roadmap U-09's own naming
("Location provider interface") directly, rather than narrowing it to one implementation:

```
Provider(context) → Location Tier ∈ {0, 1, 2}
```

- **Minimum context: scene.** The simplest valid implementation is a constant function of the scene
  alone — `Provider(scene) → Tier`, set by the GM (default authority; a setting module could delegate
  this, not addressed here), guided by — not bound to — §E's situational table. This remains the
  **recommended default** GM-facing behavior; nothing else in this document assumes anything richer.
- **Richer context is the same interface, not a different one.** A table wanting per-combatant,
  per-target, or per-action granularity (a tracked boss at Tier 1 while background mooks stay at Tier 0;
  a declared "called shot" bumping a single attack to Tier 1 inside an otherwise Tier-0 scene)
  implements `Provider(scene, attacker, target, action, …)` against the identical signature. §B's flow
  and §C/§D's derivation math consume only whichever Tier comes back — they do not care how many
  arguments the Provider needed to decide it. This was previously written as a bolted-on "open
  extension" to a scalar flag; v1.1 corrects that — it is a native implementation of the same interface,
  not an add-on.
- **Timing:** queried **before** any roll it will govern. Roadmap Phase 2's acceptance criterion
  "location selection never changes the original attack roll" is read here to extend one step further:
  it also never *retroactively reinterprets* a roll already made, regardless of how rich the Provider's
  context is. A mid-scene change (e.g., a formal duel at Tier 1 degenerating into a chaotic brawl,
  dropped to Tier 0) only affects rolls made **after** the change; earlier rolls keep whatever Location
  Index (or absence of one) they already produced.
- **Scope:** a given Provider configuration persists until the GM (or setting-defined authority)
  explicitly changes it.

Whether §E's situational guidance table should be extended with per-combatant *examples*, now that the
interface natively supports them, remains open (§J) — the architecture supports it either way.

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
- **The Location Provider cannot reach the Core transaction.** Whatever context it consults (§D.3), it
  is external configuration state feeding only the optional location-derivation step in §B's diagram;
  nothing in §C/§D writes to Roll, Cost, Outcome, or Recovery.
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
| Interaction with Armor (coverage, Bypass/Sunder) | Named as an explicit S-5 deliverable ("Location interaction," Roadmap Phase 4.1) — not addressed here | S-5 |
| Whether §E's situational guidance should include per-combatant examples | D.3's Provider interface (v1.1) now supports per-combatant/per-action selection architecturally; §E still only illustrates scene-level cases | Designer discretion |
| Which Tier-1 sub-method (Zero-Step vs. Units-Digit) a given table actually uses | Contingent on the granularity of a location table that doesn't exist yet | Same as location table, above |
| Roadmap §4 dependency-chain ordering vs. §3.1/§5/§6 (§A.2) | Minor documentation inconsistency, not a blocking issue | Roadmap cleanup, out of band |

---

## I. Quick Reference

For downstream systems (S-3 Effects, S-4 Wounds, S-5 Armor, Setting location tables) that just need the
operational procedure:

1. The Location Provider (§D.3) resolves `Location Tier ∈ {0, 1, 2}` before any roll it will govern —
   in the simplest case a GM-set scene-level value guided by §E, optionally richer (per-combatant,
   per-action). No tier is a mandated default.
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
| Zero-Step base formula (§C.2) | Established — "reverse digits" has essentially one sensible arithmetic reading; does **not** imply Zero-Step is the selected method (§H) |
| Units-Digit base formula (§C.2) | Established — "units digit" has essentially one sensible arithmetic reading; method selection remains open (§H) |
| Zero-Step R=100 handling (§D.1) | **Proposed** — awaiting sign-off; alternative considered and recorded; v1.1 adds a downstream-override synthesis note |
| Units-Digit zero-bucket labeling (§D.2) | **Proposed** — low-stakes labeling choice, awaiting sign-off |
| S-2 boundary/pipeline statement (§B, added v1.1) | Established — restates existing dependencies (S-3/S-4/S-5/Setting) in one place, resolves nothing new |
| Tier-selection signaling mechanism (§D.3) | **Proposed, revised v1.1** — Location Provider interface; scene-level constant function as default implementation; per-combatant/per-action natively supported, not bolted on |
| Situational selection guidance (§E) | Restated from source — explicitly not a universal default, per source constraint; not yet updated with per-combatant examples (§H) |
| Uniformity / bijection / Doubles-alignment properties (§F, §G) | **Verified** by exhaustive enumeration (all 100 Roll values) |
| Resolution-step comparison, Tier 0/1 (§F) | Established (source + direct inspection) |
| Wound frequency, lethality, quantitative Priority-1 fidelity | **Explicitly deferred** — requires S-4, not tested or guessed at here |
| Tier 2 detailed mechanics | **Deferred** — future dedicated pass |
| Anatomical location table content | **Deferred** — likely Setting-Module scope (Roadmap Phase 12), not S-2 |
| S-3 "Choose Location" Effect interaction | **Flagged dependency**, not resolved |

**Nothing in this document is locked.** It is a revised proposal, structured to match S-1's density and
rigor, now awaiting an independent review of *this* revision (v1.1) — not a re-litigation of v1 — before
the candidate-table experiment begins and before any locking discussion.

### Proposed for cross-review (updated for v1.1)

1. **D.1 — Zero-Step's R=100 → L=100 ruling**, now with the v1.1 synthesis note: is extending the "00
   reads as 100" convention to a reversed pair the right call — optionally paired with a *downstream*
   forced-vital-hit rule for Fumbles — or should R=100 get something different at the derivation layer
   itself?
2. **D.3 — the Location Provider interface (revised v1.1):** does the architecture read as correct now
   that per-combatant/per-action selection is native rather than bolted on? Separately: should §E's
   guidance table itself be extended with per-combatant examples, or left at scene-level illustrations
   with richer use left implicit in the interface?
3. **A.2 — the Roadmap §4 vs. §3.1/§5/§6 dependency-ordering inconsistency**: confirm §3.1's reading is
   the intended one, and flag §4 for a wording fix in a future Roadmap revision.
4. **§E's unconfirmed Quality-mode/Tier correlation observation**: worth stating as guidance somewhere,
   or better left unstated until it's tested?
5. **§C.2's trade-off (added v1.1)**: does the divisors-of-10 / continuous-range framing change which
   candidate anatomical tables are worth building for the comparison experiment?

**Next:** independent review of this v1.1 revision, then the candidate-table comparison experiment
(Zero-Step vs. Units-Digit against explicitly non-canonical test fixtures), kept as a separate,
clearly-labeled deliverable so experimental fixtures cannot drift into accidental canon. Only after both
of those would locking S-2 be on the table. If S-2 eventually closes: S-3, Outcome Effect trigger
thresholds, next — same situation-dependent treatment, same "don't lock prematurely" discipline.
