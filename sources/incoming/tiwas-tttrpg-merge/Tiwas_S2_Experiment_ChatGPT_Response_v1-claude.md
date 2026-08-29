# Tiwas — S-2 Candidate-Table Experiment & ChatGPT Review Response (v1.0)

**Status:** Response to ChatGPT's cross-review of `Tiwas_Hit_Location_Default_Policy_S2_v1-1-claude.md`
(the v1.1 revision). Three things happen in this document: (1) every item in ChatGPT's review is
triaged against S-2 v1.1's actual text — agreed, refined, or (nowhere, this pass) rejected; (2)
ChatGPT's recommended candidate-table experiment (its §11–§12) is executed in full, with real computed
data, against all three fixtures ChatGPT specified; (3) ChatGPT's smaller wording/interpretation fixes
are logged as drafted text for a future v1.2 pass, per explicit instruction not to touch the canonical
S-2 v1.1 file yet. **This document does not lock S-2, and does not select between Zero-Step and
Units-Digit** — consistent with Roadmap §9's "Do not lock S-2 prematurely" and ChatGPT's own "neither
should be selected yet."

**Relationship to prior documents:** Downstream of S-2 v1.1 and of ChatGPT's review of it (both supplied
as source material). Upstream of nothing yet — this is itself now the next artifact awaiting cross-review
(§I).

**Methodology note:** all numeric results below were computed, not estimated — exact rational arithmetic
(`fractions.Fraction`), not floating point, exhaustive enumeration where the input space is small enough
(all 100 Roll values, per S-2 v1.1's own §F precedent), independently re-run rather than assumed from
S-2 v1.1's prior claims.

---

## A. Disposition of ChatGPT's Review

Every substantive item from ChatGPT's document, triaged.

| # | ChatGPT § | Item | Assessment | Disposition |
|---|---|---|---|---|
| 1 | §1 | Overall verdict: architecturally sound, not lock-ready | Agree | No action — confirmed |
| 2 | §2 | Standardize Provider signature to `LocationProvider(Context) → LocationTier` with a `LocationContext` record | Agree, real clarity gain | **Logged for v1.2** — drafted text in §F.1 |
| 3 | §3 | Soften "likely Setting-Module scope" to acknowledge Universal-Play ownership is also possible | Agree, low-stakes hedge | **Logged for v1.2** — drafted text in §F.2 |
| 4 | §4 | Zero-Step's bijection elegance is not evidence it's the better method | Agree — S-2 v1.1 already says this | No action — already correct in current text |
| 5 | §5 | Reframe Zero-Step vs. Units-Digit as "which interfaces better with a location table," not "which is mathematically nicer" | Agree | No document action — this framing *is* the experiment (§C–§E) |
| 6 | §6 | Leave `100→100` as a proposed ruling; a downstream Fumble-special rule is a separate, later question | Agree | No action — confirmed still out of scope of this pass (§G) |
| 7 | §7 | Roadmap §4 vs. §3.1/§5/§6 dependency-ordering conflict: documentation defect, don't re-litigate | Agree | No action — S-2 v1.1 §A.2 already reaches the identical conclusion in near-identical language |
| 8 | §8 | Reinterpret "Tier 2 can support granular injury" as *S-2 must expose an extension point*, not *S-2 must demonstrate granular injury* | Agree, genuinely useful — resolves an apparent tension between the acceptance criterion and §H's deferral | **Logged for v1.2** — drafted text in §F.3 |
| 9 | §9 | Optional rename of the document title | Agree it's optional; mild lean noted | **Logged as optional** in §F.4, not applied |
| 10 | §10 | Correctly identifies Zero-Step vs. Units-Digit as the one real remaining S-2 fork | Agree | Basis for §C–§E below |
| 11–12 | §11–§12 | Run the 3-fixture candidate-table experiment; report raw distribution, anatomical-result stats, defer system-level consequences | Agree on scope — **with one methodological refinement**, see §B.1 | **Executed** — §C–§E |
| 13 | §13 | Update S-2 status to "WIP / Architecture Accepted / Mechanism Selection Pending Experimental Comparison" | Agree, more informative than plain "WIP" | Recommended in §H, not applied to S-2 v1.1 itself |

No item is rejected outright. The one place this document diverges from a literal reading of ChatGPT's
brief is §B.1 — a methodology gap in Fixture C, not a disagreement with ChatGPT's conclusions.

---

## B. Independent Assessment

Per the actual instruction governing this document — *analyze, assess, and execute*, not merely execute
— three points below are this document's own judgment, not restatements of ChatGPT's.

### B.1 Fixture C, as literally written, is not neutral between the two methods

ChatGPT specifies Fixture C directly as explicit 1–100 ranges (`Torso 09–48`, etc.). That representation
*is already a Zero-Step lookup table* — Zero-Step's Location Index (native range 1–100) maps onto it with
zero transformation. Running "Zero-Step against Fixture C" under a literal reading therefore measures how
exactly a domain reproduces a table defined in its own domain's terms, which is close to tautological
(confirmed below: Zero-Step's error is exactly 0.00pp on every zone of Fixture C — §D.4). It does not, by
itself, show Zero-Step is a good fit for weighted tables in general; it shows Zero-Step is a good fit for
*tables already expressed as 1–100 ranges*, a narrower and less interesting claim.

**Resolution used here:** Fixture C's ranges are read as *relative weight specifications* (Head ≈ 5%,
Neck ≈ 3%, Torso ≈ 40%, etc. — recovered from each range's span), and each method's own zone boundaries
are re-derived independently from those weights, onto that method's own native domain (§C.3). This makes
Zero-Step's and Units-Digit's results on Fixture C comparable on equal footing, rather than one of them
getting a free pass by construction. It is a deviation from a literal reading of ChatGPT §11 — flagged
here since it changes how Zero-Step's "exact match" result should be read (domain-matches-shape, not
generalizable evidence).

### B.2 Fixture B does not actually favor Units-Digit on accuracy — only on step count

ChatGPT frames Fixture B (10 uniform zones) as "give Units-Digit its strongest natural case." That's
correct for *mapping operations* (§D.5: Units-Digit needs zero lookup steps here, since index value IS
zone number; Zero-Step still needs one range lookup even though it divides evenly). It is not correct for
*accuracy*: both methods reproduce Fixture B's intended weights exactly, 0.00pp error across all ten
zones, for both methods (§D.3). Units-Digit's real advantage on a 10-zone table is implementation
simplicity, not precision — S-2 v1.1 §C.2 already gestures at this ("need no further processing") but
frames it as a general trade-off; the experiment confirms it's specifically a *step-count* advantage, not
an *accuracy* one, at least at this tested granularity. Worth folding into whatever eventually
replaces or extends §C.2's trade-off paragraph — not drafted into §F since it's a substantive framing
change, not a wording fix, and belongs to whoever does the real v1.2 pass with full context.

### B.3 A finding beyond either document: coarse binning can manufacture asymmetry a table never intended

Neither S-2 v1.1 nor ChatGPT's review anticipated this specific failure mode. §D.4 shows Units-Digit,
applied to Fixture C, assigns **R Leg 2 slots (20%) and L Leg 1 slot (10%)** — despite both being
specified at an identical 14% in the source table. This is not a hand-tuning error; it is a structural
consequence of forcing a 14%-of-100 weight onto a 10-slot domain: 14% of 10 slots is 1.4, an inherently
non-integer quantity, and *some* integer resolution must break the tie between two zones that are supposed
to be identical. No tie-break rule fixes this in general — it is a discreteness problem, not an
implementation bug (detailed in §E.2, verified directly by a reordering test). S-2 v1.1 §C.2's existing
"uneven bucket-grouping" language names the general problem in the abstract; it does not identify this
specific consequence — silent, table-order-dependent L/R asymmetry in a table the designer explicitly
intended to be symmetric. That is new evidence from this pass, not a restatement of either source
document.

---

## C. Experiment — Methodology

### C.1 Derivation formulas under test

Both restated exactly from S-2 v1.1 (§C.2, §D.1, §D.2) — not modified here.

| Method | Formula | Domain | Special case |
|---|---|---|---|
| **Zero-Step** | For `R` = 1–99: `T = floor(R/10)`, `U = R mod 10`, `L = 10×U + T` | 1–100 | `R = 100 → L = 100` (§D.1 ruling) |
| **Units-Digit** | `L = R mod 10` | 1–10 | `R mod 10 = 0 → L = 10` (§D.2 ruling), covers `R ∈ {10,20,...,90,100}` |

**Independent re-verification of S-2 v1.1 §F's claims** (exhaustive enumeration, `R` = 1–100, this pass's
own run, not reused from S-2):

| Claim (S-2 v1.1 §F) | This pass's result |
|---|---|
| Zero-Step is a bijection on {1,…,100} | **Confirmed** |
| Zero-Step fixed points = Core Doubles set exactly | **Confirmed** — `{11,22,33,44,55,66,77,88,99,100}` |
| Units-Digit output is uniform over 10 buckets | **Confirmed** — exactly 10 of 100 rolls per bucket |

### C.2 Fixtures (restated exactly from ChatGPT §11 — disposable, non-canonical)

| Fixture | Zones (table order) | Intended weight |
|---|---|---|
| **A** (6-zone) | Head, Torso, R Arm, L Arm, R Leg, L Leg | Uniform, 1/6 each (not specified by ChatGPT — inferred as the only sensible default for an unweighted list) |
| **B** (10-zone) | Head, Face/Neck, Chest, Abdomen, Pelvis, R Arm, L Arm, R Hand, L Hand, Legs | Uniform, 1/10 each (same inference). Note: *Legs* is one combined zone in ChatGPT's own fixture — not split L/R, unlike Arms/Hands. Used as-is; leg symmetry is not testable on this fixture, only arm/hand symmetry is. |
| **C** (100-slot weighted) | Head 5%, Neck 3%, Torso 40%, R Arm 12%, L Arm 12%, R Leg 14%, L Leg 14% | Explicit (recovered from ChatGPT's literal 1–100 ranges as relative weights — §B.1) |

### C.3 Apportionment method (not specified by either source document — supplied here, flagged)

Converting a fixture's intended weights into a method's actual integer slot count (out of the method's
native domain size `N` = 100 for Zero-Step, 10 for Units-Digit) is an apportionment problem: `weight × N`
is rarely an integer. This document uses the **Largest-Remainder / Hare-quota method**, a standard,
named, reproducible proportional-apportionment algorithm (not invented for this pass):

1. `quota[zone] = weight[zone] × N`
2. `base[zone] = floor(quota[zone])`
3. `remainder_units = N − Σ base[zone]`
4. Sort zones by descending fractional part `(quota[zone] − base[zone])`; award one extra slot each to
   the top `remainder_units` zones.
5. **Tie-break:** equal fractional parts are resolved by table order (the earlier-listed zone in §C.2
   wins). This is a real modeling choice, not a neutral default — see §E.2 for its consequence.

All arithmetic used exact rational numbers (Python `fractions.Fraction`), not floating point, to avoid
rounding artifacts of the project's own kind (Core Rules v2 §1's "round down, no exceptions" ethos
extended to this experiment's own tooling).

### C.4 Metrics, as ChatGPT §12 requested, defined precisely where ChatGPT left them undefined

| Metric | Definition used |
|---|---|
| Actual % | `slots[zone] / N × 100` |
| Weighting error | `actual% − intended%`, in percentage points (pp); reported per-zone, plus mean and max absolute error per fixture×method |
| Unused zones | Zones receiving 0 slots |
| Most/least probable zone | By slot count; ties reported as ties, not arbitrarily broken |
| L/R symmetry | Paired zones (R Arm/L Arm, R Leg/L Leg, R Hand/L Hand where present) compared by slot count |
| **Number of mapping operations** (undefined by ChatGPT — supplied here) | `0` if `N` equals the zone count **and** the apportionment is a pure 1-slot-per-zone identity (index value = zone number directly, no lookup table needed); `1` otherwise (a single range/bucket lookup is one operation regardless of table complexity, per S-2 v1.1's own "near-zero-step" framing) |

System-level consequences (wound frequency, lethality, exchange length) are **not computed** — per
ChatGPT §12's own deferral and Roadmap Phase 2's simulation gate, these require a wound model (S-4) that
doesn't exist yet (§G).

---

## D. Experiment — Results

### D.1 Raw derivation distribution (trivial, per ChatGPT §12)

| Method | Index range | Distribution |
|---|---|---|
| Zero-Step | 1–100 | 1% per value (100 values) |
| Units-Digit | 1–10 | 10% per value (10 values) |

### D.2 Fixture A (6 zones, uniform)

| Zone | ZS slots/100 | ZS % | ZS error (pp) | UD slots/10 | UD % | UD error (pp) |
|---|---|---|---|---|---|---|
| Head | 17 | 17.00 | +0.33 | 2 | 20.00 | +3.33 |
| Torso | 17 | 17.00 | +0.33 | 2 | 20.00 | +3.33 |
| R Arm | 17 | 17.00 | +0.33 | 2 | 20.00 | +3.33 |
| L Arm | 17 | 17.00 | +0.33 | 2 | 20.00 | +3.33 |
| R Leg | 16 | 16.00 | −0.67 | 1 | 10.00 | −6.67 |
| L Leg | 16 | 16.00 | −0.67 | 1 | 10.00 | −6.67 |

- Mean abs. error: Zero-Step **0.444pp**, Units-Digit **4.444pp** (exactly 10× — §E.1)
- Max abs. error: Zero-Step 0.667pp (R Leg), Units-Digit 6.667pp (R Leg)
- Unused zones: none, either method
- Most probable: Head/Torso/R Arm/L Arm (tied); least probable: R Leg/L Leg (tied) — both methods
- L/R symmetry: **holds** for both methods (R Arm=L Arm, R Leg=L Leg) — §E.2 explains why this is not
  guaranteed in general
- Arms aggregate / Legs aggregate: Zero-Step 34.00% / 32.00%; Units-Digit 40.00% / 20.00%
- Mapping operations: **1** for both (neither domain size equals 6)

### D.3 Fixture B (10 zones, uniform)

| Zone | ZS slots/100 | ZS % | UD slots/10 | UD % |
|---|---|---|---|---|
| Head | 10 | 10.00 | 1 | 10.00 |
| Face/Neck | 10 | 10.00 | 1 | 10.00 |
| Chest | 10 | 10.00 | 1 | 10.00 |
| Abdomen | 10 | 10.00 | 1 | 10.00 |
| Pelvis | 10 | 10.00 | 1 | 10.00 |
| R Arm | 10 | 10.00 | 1 | 10.00 |
| L Arm | 10 | 10.00 | 1 | 10.00 |
| R Hand | 10 | 10.00 | 1 | 10.00 |
| L Hand | 10 | 10.00 | 1 | 10.00 |
| Legs | 10 | 10.00 | 1 | 10.00 |

- Mean/max abs. error: **0.00pp for both methods** — every zone matches its intended weight exactly
- Unused zones: none
- All 10 zones tied for most/least probable, both methods
- L/R symmetry: holds trivially (all zones equal)
- Arms(+hands) aggregate / Legs aggregate: **identical for both methods** — 40.00% / 10.00%
- Mapping operations: Zero-Step **1** (100 ≠ 10, still needs a range lookup even though it divides
  evenly); Units-Digit **0** (10 = 10, index value is the zone number directly)

This is ChatGPT's "strongest case for Units-Digit" fixture, and the data supports that framing for step
count only (§B.2) — not for accuracy, where the two methods tie exactly.

### D.4 Fixture C (7 zones, weighted)

| Zone | Intended % | ZS slots/100 | ZS % | ZS error | UD slots/10 | UD % | UD error |
|---|---|---|---|---|---|---|---|
| Head | 5.00 | 5 | 5.00 | +0.00 | 1 | 10.00 | **+5.00** |
| Neck | 3.00 | 3 | 3.00 | +0.00 | **0** | **0.00** | **−3.00** |
| Torso | 40.00 | 40 | 40.00 | +0.00 | 4 | 40.00 | +0.00 |
| R Arm | 12.00 | 12 | 12.00 | +0.00 | 1 | 10.00 | −2.00 |
| L Arm | 12.00 | 12 | 12.00 | +0.00 | 1 | 10.00 | −2.00 |
| R Leg | 14.00 | 14 | 14.00 | +0.00 | **2** | **20.00** | **+6.00** |
| L Leg | 14.00 | 14 | 14.00 | +0.00 | 1 | 10.00 | −4.00 |

- Mean abs. error: Zero-Step **0.000pp** (tautological — §B.1), Units-Digit **3.143pp**
- Max abs. error: Zero-Step 0.000pp, Units-Digit **6.000pp** (R Leg)
- Unused zones: Zero-Step none; Units-Digit **Neck** (structurally unreachable — its 3% weight rounds to
  0 of 10 slots)
- Most probable: Torso, both methods (40%); least probable: Zero-Step → Neck (3%), Units-Digit →
  **Neck (0%, unreachable)**
- L/R symmetry: Zero-Step holds (R Arm=L Arm=12, R Leg=L Leg=14). **Units-Digit breaks it**:
  R Arm=L Arm=1 (holds), but **R Leg=2 ≠ L Leg=1** — a table-order artifact of the largest-remainder
  tie-break (§E.2), not an authored asymmetry
- Arms aggregate: Zero-Step 24.00%, Units-Digit 20.00% (intended 24%). Legs aggregate: Zero-Step 28.00%,
  Units-Digit 30.00% (intended 28%) — **the aggregate Legs figure looks mild (+2pp) and conceals the
  20%-vs-10% internal R/L split**; aggregating away the asymmetry is itself a finding (§E.3)
- Mapping operations: **1** for both (neither domain size equals 7)

---

## E. Cross-Fixture Findings

### E.1 Zero-Step's error scales down with its domain size, exactly

On Fixture A (equal zone count, equal weight-uniformity for both methods), Units-Digit's max error
(6.667pp) is **exactly 10×** Zero-Step's (0.667pp) — algebraically exact (both reduce to a `2/3`-slot
rounding gap, worth `100/6` vs. `10/6` percentage points respectively; the ratio is exactly the domain
ratio, 10), not a decimal coincidence. This confirms, with an exact figure, what S-2 v1.1 §C.2 already
states qualitatively — a continuous 1–100 range "can be cut into proportional ranges for any zone count"
more precisely than a 10-value range can.

### E.2 Fine-grained weights on a coarse domain can manufacture asymmetry a table never authored

Fixture C's Units-Digit result is the clearest evidence in this pass. `14% of 10 slots = 1.4` — an
inherently non-integer quantity for a pair of zones the table specifies as identical. Any integer
resolution must give one of {R Leg, L Leg} 1 slot and the other 2; **no tie-break rule avoids this** — it
is a discreteness problem, not a bug in this document's specific tie-break choice (table order). A
designer wanting guaranteed L/R symmetry under Units-Digit would need to either (a) constrain all
paired-zone weights to exact multiples of 10% (severely limiting what tables are expressible), or (b)
hand-author symmetric pairs as a special case rather than relying on generic proportional apportionment.

Fixture A's symmetry held only because its uniform 1/6 weights happened to place both members of each L/R
pair on the same side of the remainder cutoff — a coincidence of table order, not a general guarantee.
**Verified directly:** reordering Fixture A's zone list (Head, L Leg, R Arm, L Arm, R Leg, Torso — same
weights, different order) flips the outcome to R Leg=1, L Leg=2 slots, breaking the symmetry that held
under the original order. This confirms the effect is a property of table order interacting with the
tie-break rule, not of the weights themselves.

### E.3 Aggregate stats can hide the exact failure mode a granular system cares about most

Fixture C's Units-Digit aggregate Legs figure (30% vs. 28% intended) undersells the problem by roughly an
order of magnitude relative to what a hit-location system exists to model: one specific leg getting hit
twice as often as its mirror twin (20% vs. 10%) is a much larger practical distortion than a 2pp aggregate
error suggests. Given Priority 1 in the Brief (§0) is explicitly "granular physical simulation… where the
situation warrants it," per-zone reporting — not aggregate Arms%/Legs% alone — is the metric that actually
matters for evaluating a candidate method against that priority.

### E.4 Units-Digit's demonstrated advantage is implementation simplicity, not precision

Across all three fixtures, Units-Digit never has *lower* error than Zero-Step, and matches it exactly only
on Fixture B (§D.3, §B.2). Its one unambiguous win is mapping operations on a 10-zone table (0 vs. 1).
This narrows, rather than widens, the case for Units-Digit relative to how S-2 v1.1 §E currently frames
the trade-off ("neither method is inherently better"): the data doesn't say Units-Digit is worse in every
respect, but it does say its case rests specifically on step-count/implementation simplicity for tables
that happen to have exactly 10 zones, not on accuracy at any tested granularity. Offered as evidence for
the next reviewer, not as grounds to lock anything (§G).

---

## F. Ready for v1.2 — Drafted Text, Not Applied

Per instruction, S-2 v1.1 itself is untouched. The text below is drafted and ready to merge whenever a
v1.2 pass actually happens.

### F.1 §D.3 Provider signature (ChatGPT §2)

Replace the current informal signature with:

```
LocationProvider(Context) → LocationTier
```

where `Context` is a record, not a positional argument list:

```
LocationContext {
    scene,
    attacker,
    target,
    action,
    declared_intent,
    equipment,
    setting_context
}
```

A Provider implementation may ignore any field it doesn't need — a scene-only implementation reads only
`Context.scene`, exactly as the current minimum-context default already describes.

### F.2 §B boundary table wording (ChatGPT §3)

Replace "likely Setting-Module scope" with:

> Location tables are deliberately outside S-2; their ownership may be Universal Play or Setting Module
> depending on the eventual design.

### F.3 §G acceptance-criteria table, Tier 2 row (ChatGPT §8)

Replace the current row ("Tier 2 can support granular injury | Not verified this pass — Tier 2 mechanics
undefined (§H)") with a reinterpretation of the criterion itself:

> Read as *"S-2 must expose a Tier-2 extension point capable of receiving a future granular-location
> implementation"* rather than *"S-2 must demonstrate Tier 2 already produces granular injury"* (the
> latter needs S-4/S-5, out of S-2 scope). Under that reading: **Satisfied** — §B's diagram and §C.1 both
> name Tier 2 as a category with a defined slot in the Provider's output range; internal mechanics remain
> deferred (§H).

### F.4 Title (ChatGPT §9, optional)

ChatGPT proposed "Tiwas — Hit-Location Policy and Location Provider (S-2)" or "Tiwas — Hit-Location
Granularity Policy (S-2)." Both remove the "Default Policy" vs. "no universal default" tension in the
current title. Logged as optional, not applied — a naming call is a designer preference rather than a
correctness fix, and the current title is not wrong, only slightly confusing on first read.

---

## G. Explicitly Not Resolved by This Pass

Matching S-2 v1.1's own §H discipline — stated rather than silently skipped.

| Item | Why not resolved here |
|---|---|
| Zero-Step vs. Units-Digit final selection | Explicitly out of scope — evidence only (Roadmap §9: "Do not lock S-2 prematurely") |
| System-level consequences (wound frequency, lethality, exchange length) | Requires a wound model (S-4) that doesn't exist yet — ChatGPT §12 and Roadmap Phase 2 both defer this identically |
| The `100→100`-gets-Fumble-special-treatment downstream variant (S-2 v1.1 §D.1 synthesis note) | S-4/S-5 scope, not tested here |
| Whether a real location table should use proportional apportionment at all, vs. hand-authored zone boundaries | This experiment assumes apportionment because Fixture C was given as ranges; a real table's designer may simply assign boundaries directly, sidestepping §E.2's asymmetry risk entirely — that option isn't excluded by anything here |
| Per-combatant/per-action Provider richness (S-2 v1.1 §D.3) | Interface question, orthogonal to the derivation math tested here |
| Whether Fixtures A/B/C should become anything beyond disposable | They remain explicitly non-canonical, per ChatGPT §11 and S-2 v1.1's own "kept as a separate, clearly-labeled deliverable so experimental fixtures cannot drift into accidental canon" (§J) |

---

## H. Recommended Status Update

Adopt ChatGPT §13's proposed label for S-2, optionally extended for precision:

> **S-2 — WIP / Architecture Accepted / Mechanism Selection Pending Experimental Comparison**
> *(fixture-level comparison complete as of this document; system-level comparison pending S-4)*

Not applied to S-2 v1.1 itself — recorded here as a recommendation, consistent with §F's "log, don't
touch the canonical file" treatment.

---

## I. Proposed for Cross-Review

Continuing the chain: this document is now the artifact awaiting review, same as S-2 v1.1 was.

1. **Apportionment method (§C.3):** Largest-Remainder with table-order tie-break was chosen because it's
   standard and reproducible, not because either source document specified it. Does a symmetry-aware
   tie-break (e.g., detect declared L/R pairs and force matched rounding) belong in the *methodology* for
   future comparisons, or is the finding in §E.2 — that no tie-break rule fixes this in general — reason
   enough to treat proportional apportionment itself as unsuitable for tables with symmetric pairs at
   non-10%-multiple weights?
2. **Fixture C's neutrality (§B.1):** should the disposable fixture be revised to a method-neutral weight
   specification (percentages, not literal 1–100 ranges) before any further comparison work reuses it —
   or was the literal-range version intentional, on the reasoning that a real weighted table would
   plausibly be authored in Zero-Step's native terms anyway?
3. **§B.2's reframing:** does "Units-Digit's advantage is step-count, not accuracy" belong as an edit to
   S-2 v1.1 §C.2's trade-off paragraph in the eventual v1.2, or is it too close to a substantive design
   claim (rather than a wording fix) to bundle with §F's logged items?
4. **§F's four drafted blocks:** ready to merge as-is into an actual v1.2, or hold for a single
   consolidated v1.2 pass alongside whatever else surfaces before then?

**Next:** per S-2 v1.1's own sequencing, only after this kind of comparison work (and, separately, an
eventual S-4 wound model) would locking S-2 be on the table.
