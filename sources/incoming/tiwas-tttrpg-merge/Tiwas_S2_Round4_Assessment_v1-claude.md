# Tiwas — S-2 Round 4: Assessment & Advised Actions (v1.0)

**Status:** Response to `Tiwas S-2 Exhaustive Sweep — Analysis, Review & Recommended Decision`, ChatGPT's
review of the round-3 exhaustive order sweep. ChatGPT now formally recommends Zero-Step "for formal
designer lock" and proposes four concrete artifacts (an Evidence Record, an S-2 status block, S-2 v1.2
scope text, and a Roadmap restructuring). This document analyzes and assesses that recommendation,
accepts one correction, raises two independent points neither prior round addressed, and gives a clear
verdict plus an advised-actions list. **The consolidated, ready-to-review artifacts themselves are in the
companion document, §F below — nothing here or there is applied to any canonical file.**

**Chain position:** S-2 v1.1 → experiment → ChatGPT r2 → response → ChatGPT r3 → exhaustive sweep →
ChatGPT r4 (this document's subject) → **this document + companion package**.

---

## A. What ChatGPT's Round-4 Review Says, Condensed

Accepts all round-3 findings and reclassifies several from "demonstrated" to "proven" (§2's evidence
table). Explicitly separates the now-resolved question (which Tier-1 *formula*) from the still-open ones
(Tier 0/1/2 *policy*, the anatomical mapping table itself) and recommends treating them as formally
distinct going forward — proposing an S-2A (index provider) / S-2B (tier policy) / S-2C (anatomical
mapping) split in the Roadmap. States plainly: **"Select Zero-Step as the general-purpose Tier-1 Location
Index provider... recommended for formal designer lock"** — while explicitly not locking anything itself,
retaining Units-Digit as a documented coarse alternative, and leaving tier policy, the mapping algorithm,
and Tier 2 untouched. Offers one self-correction (§23): the earlier claim that a 1pp discrepancy is
"usually inconsequential" overreaches; acceptability is context-dependent. Proposes concrete text for an
Evidence Record (E1–E8), an S-2 status block, and an S-2 v1.2 section.

---

## B. Agreement

Full agreement with §2–§13, §15–§18, §22, §25 — restatements and extensions of already-established
findings, all consistent with what rounds 1–3 produced. No corrections needed there.

---

## C. Independent Assessment

### C.1 Accepted: the "1pp is usually inconsequential" phrasing overreached

ChatGPT's §23 is right. Round 2 and round 3 both used language along the lines of "the bug's worst case is
small enough not to matter in practice." That's an unsupported generalization — a 1pp shift concentrated on
a single strategically important zone, or compounded across many rolls, could matter a great deal depending
on what's built on top of the Location Index later (S-3 Effects, S-4 wounds). Adopting ChatGPT's more
careful formulation going forward: **a 1pp discrepancy is materially smaller than a 10pp one and less
likely to produce consequential distortion, but its acceptability is context-dependent, not a given.**

### C.2 An untested dimension: table usability, at the derivation stage rather than the mapping stage

Every metric used across all three rounds — mapping-stage count, MAE, symmetry, reachability — measures
either the *index-to-zone mapping* stage (explicitly not S-2's job, per the established scope boundary) or
the statistical shape of the *index itself*. Nobody, across any round or in S-2 v1.1 itself, has directly
compared the human/physical cost of the **derivation step S-2 actually owns: Roll → Index.**

That comparison isn't symmetric, and it's worth naming before treating the formula question as fully
closed. Units-Digit's derivation ("read the last digit") is trivial regardless of how the d100 is
physically produced. Zero-Step's derivation depends on method: if a table rolls percentile dice as two
separate d10s (the standard convention — Core Rules v2 §1), Zero-Step is **literally free** — reading the
tens-die as the units digit and the units-die as the tens digit costs nothing beyond relabeling the same
two physical objects already on the table. But if the roll arrives as a single integer — a single d100 die,
a dice-rolling app, or a GM simply calling out "you rolled 47" — Zero-Step requires an actual (small, but
real) mental digit-swap that Units-Digit never needs. This is squarely a Priority-3 concern ("minimum
resolution steps... without sacrificing Priority 1") applied to the one stage that's actually S-2's to
answer for, and it has gone unmeasured through four rounds of otherwise very thorough analysis. It doesn't
overturn anything above — digit-swapping is still easy — but it's a real, previously-unnamed gap, not a
rhetorical objection.

### C.3 A lighter-weight alternative to the proposed S-2A/B/C Roadmap split

ChatGPT's underlying observation is correct — "S-2" currently bundles two genuinely different questions
(which formula, and when to use Tier 1 at all) and the Roadmap's own S-2 simulation gate mixes criteria
that can't be evaluated yet (wound frequency, lethality — need S-4) with ones that already have been
(distribution, resolution). But **splitting this into three new top-level residual IDs (S-2A/B/C)** would
need to be threaded through the Roadmap's dependency graph (§4), its Residual-to-Roadmap phase mapping
(§5), and its Phase 2 acceptance criteria (§6) — a much larger structural change than the underlying
insight requires. It also risks duplicating something that already exists: the anatomical-mapping-belongs-
to-Setting-Modules boundary is already established (Roadmap Phase 12; S-2 v1.1 §B, §H) without a new
"S-2C" label to restate it.

**Lighter alternative:** annotate the *existing* S-2 row in the Roadmap's §3.1 Ranked Residuals table to
split its status field — "Formula: evidence-backed, pending designer lock / Tier policy: Open" — rather
than adding new IDs. Same clarity, no structural churn, no duplicate tracking of ground already covered by
Phase 12. Drafted as a proposed diff in the companion document §5; presented as the more conservative of
two legitimate options, not as a rejection of ChatGPT's read.

---

## D. Verdict: Is the Evidence Sufficient to Recommend Designer Lock?

Yes, on the specific, narrow question actually tested — **which Tier-1 formula to use as the general-
purpose default** — independently, not merely by deferring to ChatGPT's conclusion. The accuracy/
expressiveness case is no longer just a strong experimental result; parts of it (E4, E7 in the companion
Evidence Record) are algebraically proven, not merely observed across the fixtures tried. Units-Digit's one
real advantage (exact, mapping-stage-free performance on exactly-ten-equal-weight tables) is narrow and now
precisely characterized rather than assumed. Nothing found across four rounds provides a comparably strong
countervailing reason to prefer Units-Digit as the *general-purpose* choice.

The one qualification: §C.2's table-usability gap is real and untested. It's not large enough to withhold
a recommendation, but it belongs in the record as an open item rather than being silently absorbed into
"sufficiently mature to move to the decision stage."

---

## E. Advised Actions

1. **Designer reviews and decides** whether to formally lock Zero-Step as the Tier-1 default, using the
   companion Evidence Record and proposed v1.2 text (§F) as the basis — this document does not lock it.
2. **If locked:** the proposed v1.2 section (companion §3) is written to be merged directly into a real
   S-2 v1.2 with no further computation required — a text-integration step, not an experimental one.
3. **Before finalizing:** weigh §C.2 (table usability at the derivation stage) explicitly, even if briefly
   — record a decision rather than an omission.
4. **Roadmap:** apply the lighter-weight annotation (companion §5) unless the designer specifically wants
   ChatGPT's fuller S-2A/B/C decomposition — both are legitimate, the lighter one is recommended here.
5. **Everything else stays open, unchanged:** Tier 0/1/2 situational default, the anatomical location
   table itself, the apportionment/mapping algorithm, symmetry-preservation mechanics, Tier 2. No action
   recommended on any of these — consistent with every prior round.

---

## F. Companion Documentation

The consolidated Evidence Record, proposed S-2 status block, proposed S-2 v1.2 section, and the lighter-
weight Roadmap annotation are in `Tiwas_S2_Proposed_Documentation_Package_v1.md`, presented alongside this
report.

---

## G. Proposed for Cross-Review

1. Is §C.2's table-usability gap worth a genuine (if small) qualitative follow-up before lock, or is
   "digit-swap vs. last-digit, noted for the record" sufficient given how minor the burden is either way?
2. Lighter-weight Roadmap annotation (§C.3) vs. ChatGPT's fuller S-2A/B/C decomposition — which does the
   designer actually want on file?
3. If lock happens, should the companion §3 text be merged into an actual S-2 v1.2 file now, or held
   pending further designer edits first?

**Next:** designer decision on the above; no further computation is pending unless the answer to #1
requires one.
