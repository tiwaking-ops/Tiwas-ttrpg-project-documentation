# Tiwas — S-2 Documentation Package (v1.1) & E9 Structural Analysis

**Status:** Supersedes `Tiwas_S2_Proposed_Documentation_Package_v1.md` for every point in the changelog
below. Responds to ChatGPT's round-5 review, which agreed with the round-4 package but flagged one real
imprecision, one governance-language risk, and one open item (E9) that needs a human playtest ChatGPT
proposed but did not run either. **Still proposed only — nothing here is applied to any canonical file.**

**Chain position:** S-2 v1.1 → experiment → r2 → r3 exhaustive sweep → r4 package → ChatGPT r5 (this
document's subject) → **this document**.

---

## 0. Changelog (v1.0 → v1.1)

| # | Correction | Source |
|---|---|---|
| 1 | Units-Digit's mapping-stage-free condition corrected: **"exactly ten equal-weight zones,"** not "zone count = 10" — a 10-zone table with unequal weights still needs a mapping stage | ChatGPT §4 |
| 2 | "Tier-1 default" language (used in the round-4 assessment's own Advised Actions) replaced with **"recommended Tier-1 provider"** throughout | ChatGPT §5 |
| 3 | Status block: "recommended for designer **lock**" → "recommended for designer **ruling**" — the designer's ruling does the locking; the evidence only recommends | ChatGPT §6 |
| 4 | E7 reframed to note it doubles as a general test-design lesson, not only an S-2-specific result | ChatGPT §10 |
| 5 | E9 rewritten; its structural component is now actually executed (§B.2), its human-subjective component is honestly flagged as not executable by me and given a tightened, ready-to-run protocol (§B.3) | ChatGPT §17; this document |
| 6 | Roadmap annotation: explicit provider-vs-tier-selection distinction added (was already substantially present; tightened per ChatGPT §14) | ChatGPT §14 |

---

## A. Assessment of ChatGPT's Round-5 Review

All four corrections above (#1–4, #6) are accepted without qualification — each is a genuine precision
gain, not a matter of preference. #1 in particular was a real error: my round-4 table said Units-Digit
needed no mapping stage whenever "zone count ≠ 10," which is wrong — a 10-zone table with unequal weights
(e.g., one zone at 20%, the rest sharing the remainder) still needs apportionment under Units-Digit. Fixed.

§12 of ChatGPT's review is worth noting explicitly: **ChatGPT changed its own position**, dropping its
earlier S-2A/B/C Roadmap proposal in favor of the round-4 assessment's lighter annotation. No action
needed there beyond confirming the convergence — both parties now agree on the lighter form.

The one place this document adds something rather than just applying a correction is E9 (§B) — ChatGPT's
proposed micro-test (§2–§3 of its review) asks for human data (perceived ease, hesitation, error rate
across repetitions) that I cannot generate. Rather than either ignoring that gap or fabricating plausible-
looking numbers, §B splits E9 into the part that's a legitimate desk exercise (counting the actual steps
each method requires) and the part that genuinely needs people rolling actual dice.

---

## B. E9 — Structural Analysis (Executed) and the Human Playtest (Not Executed)

### B.1 What can and can't be established without human subjects

ChatGPT's proposed protocol (its §3) asks to record "perceived ease," "hesitation/error," and whether the
operation "becomes automatic after a few repetitions." All three are properties of actual people doing the
task, not of the task's structure — no amount of reasoning from this chair produces that data honestly.
What *can* be established without subjects: the exact sequence of discrete reading/parsing/recall steps
each method requires in each rolling mode. That's a procedural fact, not a subjective one, and it's done in
§B.2. §B.3 sets up the part that still needs people.

### B.2 Structural task analysis

An "extra operation" here means a discrete step beyond whatever is already required to obtain the natural
roll — since Cost = Roll (Core Rules v2 §5 step 1) requires reading the full roll regardless of which
location-derivation method is used, so that baseline read is shared, not counted as "extra" for either
method.

| Mode | Shared baseline (both methods) | Units-Digit extra ops | Zero-Step extra ops |
|---|---|---|---|
| **A** — two physical d10s (tens-die + units-die) | Read both dice — already required for the natural roll | **0** — simply discard the tens-die's value, use the units-die's value as-is | **1** — restate the two already-read digits with their roles swapped |
| **B** — single d100 die (one face shows both digits) | Read the 2-digit face as one number | **1** — extract the units digit | **~2** — extract both digits, then reorder them |
| **C** — digital roller (displayed integer) | Read the displayed integer | **1** — extract the units digit | **~2** — extract both digits, then reorder them |
| **D** — GM announces the result verbally | Hear the announced integer | **1** — extract the units digit, from memory | **~2** — extract both digits from memory, then reorder — *whether auditory recall makes the reorder step relatively (not just absolutely) harder than in visual modes is a hypothesis, not established here* |

**This corrects a round-4 overclaim.** Round 4 called Zero-Step "free" in Mode A. It isn't, quite —
Units-Digit's ability to simply *discard* information is a strictly smaller act than Zero-Step's need to
*actively restate* it, even though both are close to instantaneous with two dice already in hand. The gap
is real but small in Mode A, and grows (roughly 1 op → roughly 2 ops) whenever the roll arrives as a single
integer instead. This is the corrected, more precise version of the round-4 claim, not a reversal of it.

### B.3 Human playtest protocol — designed, not run

ChatGPT's proposed protocol (its §3) is sound in outline. Two tightenings, offered because the predicted
result is explicitly experience-dependent and the original design doesn't test for that directly:

1. **Split participants by experience** — recruit both players unfamiliar with the system and players who
   have used it across several sessions, since ChatGPT's own prediction ("negligible... for experienced
   users; small but real... for a single integer presentation") is an experience-level hypothesis the
   protocol should actually be able to confirm or reject, not just an expected average.
2. **Add one objective measure alongside the subjective ones** — time-to-derive (a simple stopwatch split),
   alongside ChatGPT's self-reported ease and observed hesitation/error, so the result isn't purely
   self-report.

**Minimum practical scope:** a handful of participants in each experience group (roughly 5–10 each is
enough to see whether the effect ChatGPT predicts shows up at all — this is a small design check, not a
formal study), ~10–15 rolls per mode per participant, all four of ChatGPT's modes (A–D) unchanged. Record:
time-to-derive, self-reported difficulty (a simple 1–5 scale is enough), and error rate (wrong digit
extracted or wrong swap performed).

**This is offered as a ready-to-run tool, not a result.** Nothing about its outcome is assumed anywhere
else in this document.

---

## C. Corrected, Consolidated Artifacts (v1.1)

### C.1 Evidence Record (E1–E9, corrected)

| ID | Finding |
|---|---|
| E1 | Domain resolution: Zero-Step provides 100 native index values (1% resolution); Units-Digit provides 10 (10% resolution). |
| E2 | Uniform six-zone accuracy: Zero-Step's maximum distribution error is exactly 1/10 of Units-Digit's (0.667pp vs. 6.667pp) — algebraically exact. |
| E3 | Weighted seven-zone accuracy: Units-Digit can make a low-weight (3%) zone entirely unreachable; Zero-Step reproduces that specific table exactly, which is a property of that table's weights aligning with the 100-point domain, not general evidence of Zero-Step's accuracy on arbitrary tables. |
| E4 | Structural unreachability: the same low-weight zone is unreachable under Units-Digit in **all 5,040 possible orderings** of that table — proven algebraically, not merely observed. |
| E5 | Shared order-dependence: both providers can inherit table-order-dependent symmetry breaks from the tested largest-remainder apportionment, at exactly the same frequency (80% of 720 orderings) on a table whose weights don't divide evenly into either domain. |
| E6 | Order-error magnitude: when order-dependence fires, Units-Digit's worst-case gap is exactly 10× Zero-Step's — a direct, provable consequence of the domain-size ratio. |
| E7 | MAE invariance: under the tested largest-remainder apportionment, table order changes which zone absorbs rounding error, never the total error — proven algebraically, confirmed exhaustively. **Doubles as a general test-design lesson:** "Worst/Best MAE across permutations" is a redundant metric for any fixture under this apportionment method; per-zone worst-case error is where the real signal is. |
| E8 | Pair-aware repair: a tested symmetry-preserving apportionment variant restores declared L/R equality but raises overall mean error and does not fix the unreachable-zone problem. Logged as a **rejected experimental repair** — not proof that no repair could work. |
| E9 | **Derivation-stage usability — structural component established, human component pending.** Units-Digit needs 0–1 extra operations across four practical rolling modes; Zero-Step needs 1–2 (§B.2). This is a step-count, not a measurement of difficulty, time, or error — those require the playtest protocol in §B.3, which has not been run. |

### C.2 Proposed S-2 Status Block

```
S-2 -- Hit Location
Status: WIP. Tier-1 provider choice is evidence-backed and recommended
for designer ruling (E1-E8; E9's structural half supports the
recommendation, its human-playtest half remains open -- SS B.3). Tier
0/1/2 situational policy remains open, independent of this decision.
Anatomical index-to-zone mapping remains a separate, unresolved
subsystem (likely Setting-Module scope -- S-2 v1.1 SS B, SS H;
Roadmap Phase 12).

Tier-1 Location Index:
  Recommended provider:  Zero-Step
                          (E1, E2, E3, E4, E6, E7 -- pending designer
                          ruling; E9's human component still open)
  Retained as optional coarse/specialised provider:
                          Units-Digit
                          (exact and mapping-stage-free only for
                          exactly ten equal-weight zones -- E1, E5)

Tier 0: Valid, unchanged.
Tier 2: Reserved / future, unchanged.

Apportionment algorithm (largest-remainder / Hare quota): the
experimental tool used to run this comparison. Not proposed as a
canonical mapping rule -- remains Location-Table/Mapping-spec scope
(S-2 v1.1 SS C.3).
```

### C.3 Proposed S-2 v1.2 Section — "Tier-1 Location Index Provider"

> ## Tier-1 Location Index Provider
>
> **Status:** Recommended provider — pending formal designer ruling. Not yet locked. *This is a
> recommendation for which formula to use **if and when** Tier 1 is selected — it does not decide whether
> Tier 1 itself is used in a given scene; that remains the open, situational Tier 0/1/2 policy question
> (S-2 v1.1 §E).*
>
> Exhaustive comparison (Evidence Record, E1–E9) of the two Brief §2.2-named Tier-1 candidates indicates
> Zero-Step provides materially greater location-resolution capacity than Units-Digit, at a modest,
> now-structurally-characterized cost.
>
> | Provider | Native domain | Native resolution | Mapping-stage-free condition |
> |---|---|---|---|
> | Zero-Step | 1–100 | 1 percentage point | None for arbitrary weighted tables |
> | Units-Digit | 1–10 | 10 percentage points | Exactly ten equal-weight zones |
>
> Units-Digit is exact and mapping-stage-free specifically when a table has precisely ten *equal-weight*
> zones (E1, E5) — not merely ten zones of any weighting. Outside that narrow case, its coarser domain can
> leave low-weight zones structurally unreachable (E3, E4) and produces distribution error up to 10×
> larger than Zero-Step's under otherwise identical conditions (E2, E6). Units-Digit is therefore retained
> as a specialised coarse provider rather than the recommended general-purpose Tier-1 provider.
>
> The choice of Tier-1 provider does not determine the anatomical mapping algorithm. The mapping layer —
> index → named zone, zone weights, symmetry, apportionment, table-order independence, reachability,
> anatomical hierarchy — remains a separate, unresolved subsystem (§B, §H of this document).
>
> **Before ruling:** E9's structural component (§B.2) is established; its human-playtest component (§B.3)
> is designed but not run. The designer may rule now, treating that gap as a small, disclosed, accepted
> risk, or wait for playtest data first — both are legitimate (§D).

### C.4 Roadmap Annotation (unchanged in substance from round 4, confirmed by ChatGPT §12–§14)

**Proposed row for `Tiwas_Universal_System_Synthesized_Roadmap.md` §3.1:**

| Priority | ID | Gap | Status | Primary dependency |
|---:|---|---|---|---|
| 2 | S-2 | Hit-location policy: Tier 0/1/2 and situation use. **Tier-1 provider formula (Zero-Step vs. Units-Digit) is evidence-backed — see S-2 Evidence Record — pending designer ruling. This is separate from, and does not resolve, the decision of when Tier 1 is used at all, which remains Open.** | **Provider: evidence-backed / Tier policy: Open** | S-1 |

No change to §4's dependency graph, §5's phase mapping, or §6's Phase 2 acceptance criteria — both parties
now agree this stays a targeted annotation, not a new set of residual IDs.

---

## D. Required Further Actions

1. **Requires a human, not further computation:** run the E9 playtest (§B.3), even a small pass, if the
   human-usability question is to be closed rather than left as a disclosed gap.
2. **Requires the designer, not further analysis:** choose between (a) ruling on Zero-Step now, accepting
   E9's human component as a small bounded risk, or (b) waiting for playtest data first. This document
   does not choose for them — both are legitimate, and §C.3 is written to make that choice explicit rather
   than assumed.
3. **If ruled now:** §C's artifacts are ready to merge directly into a real S-2 v1.2 and a Roadmap edit —
   a text-integration step, requiring no further computation.
4. **Nothing else is pending from either side.** No further statistical experiment is recommended by
   ChatGPT or by this document. Tier 0/1/2 policy, the anatomical location table, the apportionment
   algorithm, symmetry mechanics, and Tier 2 remain untouched and open, unchanged from every prior round.

---

## E. What Remains Explicitly Open

Unchanged from round 4 §5, restated once more for a single current reference point:

- Tier 0/1/2 situational default (no tier is ever named "the" default, by source constraint)
- The anatomical location table itself — no such table exists yet
- The apportionment/index-to-zone mapping algorithm — largest-remainder was an experimental tool
- Symmetry-preservation mechanics for that future algorithm
- Tier 2's internal mechanics
- E9's human-playtest component (§B.3) — protocol ready, not run

---

## F. Proposed for Cross-Review

1. Run the E9 playtest before ruling, or rule now and log E9's human component as an accepted, disclosed
   gap? Both this document and ChatGPT's review present this as the designer's call, not a settled one.
2. Is §B.3's tightened protocol (experience-level split, added time-to-derive measure) the right scope, or
   does ChatGPT's original lighter version suffice for a decision this narrow?
3. With this round's corrections applied and both parties converged on the Roadmap annotation, is there
   anything else standing between this package and an actual designer ruling — or is the next message in
   this chain expected to be that ruling itself?

**Next:** awaiting either E9 playtest results or a designer ruling — whichever the designer chooses first.
