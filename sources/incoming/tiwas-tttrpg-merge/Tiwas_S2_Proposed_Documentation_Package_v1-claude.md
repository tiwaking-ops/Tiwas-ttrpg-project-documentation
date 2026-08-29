# Tiwas — S-2 Proposed Documentation Package (v1.0)

**Status:** Proposed only. Nothing in this document has been applied to `Tiwas_Core_Rules_v2.md`,
`Tiwas_Hit_Location_Default_Policy_S2_v1-1-claude.md`, or `Tiwas_Universal_System_Synthesized_Roadmap.md`.
Consolidates and refines text ChatGPT proposed across its round-4 review, incorporating the round-4
assessment's corrections (see the companion `Tiwas_S2_Round4_Assessment_v1.md`, §C). Intended for direct
designer review and, if approved, direct incorporation.

---

## 1. Evidence Record (E1–E9)

| ID | Finding | Basis |
|---|---|---|
| E1 | Domain resolution: Zero-Step provides 100 native index values (1% resolution); Units-Digit provides 10 (10% resolution). | S-2 v1.1 §C.2 |
| E2 | Uniform six-zone accuracy: Zero-Step's maximum distribution error is exactly 1/10 of Units-Digit's (0.667pp vs. 6.667pp) — algebraically exact, not approximate. | Round 1 §E.1; exhaustively reconfirmed, round 3 |
| E3 | Weighted seven-zone accuracy: Units-Digit can make a low-weight (3%) zone entirely unreachable under standard apportionment; Zero-Step reproduces the same table exactly — see E9's caveat on why that specific result is a degenerate case, not general evidence of Zero-Step's accuracy in general. | Round 1 §D.4 |
| E4 | Structural unreachability: the same low-weight zone (Neck, Fixture C) is unreachable under Units-Digit in **all 5,040 possible table orderings** — proven algebraically, not merely observed. | Round 3, exhaustive + proof |
| E5 | Shared order-dependence: both providers can inherit table-order-dependent symmetry breaks from the tested largest-remainder apportionment. On a fixture with weights that don't divide evenly into either domain, both break symmetry in exactly the same 80% of all 720 possible orderings. | Round 2 single case; round 3 exhaustive confirmation |
| E6 | Order-error magnitude: when order-dependence fires, Units-Digit's worst-case gap is exactly 10× Zero-Step's (10pp vs. 1pp) — a direct, provable consequence of the 10:1 domain-size ratio, not a fixture-specific coincidence. | Round 2/3 |
| E7 | MAE invariance: under the tested largest-remainder apportionment, table order changes *which* zone absorbs rounding error, never the *total* error. Proven algebraically for any weight set; confirmed exhaustively on two fixtures. Consequence: "Worst MAE" / "Best MAE" across permutations are redundant with "Mean MAE" for this apportionment method. | Round 3 §C.4, proof included |
| E8 | Pair-aware repair: a tested symmetry-preserving apportionment variant restores declared L/R equality but raises overall mean error (3.14pp → 4.29pp) and does not fix Neck's unreachability. Logged as a **rejected experimental repair** — not proof that no repair could work, only that this one traded one visible problem for a larger one. | Round 2 §C.2 |
| E9 | **Untested dimension — table usability at the derivation stage.** No round has compared the human/physical-dice cost of Roll → Index itself (S-2's actual job), as opposed to the well-characterized Index → Zone mapping stage (E1). Units-Digit ("read the last digit") is trivial regardless of rolling method. Zero-Step ("swap the two digits") is free when rolled as two physical d10s read in reverse order, but requires a small real mental step when the roll arrives as a single integer (app, single d100 die, GM calling out a number). Flagged as open, not evidence for either side. | Round 4 |

---

## 2. Proposed S-2 Status Block

```
S-2 -- Hit Location
Status: WIP. Tier-1 formula choice is evidence-backed and recommended
for designer lock (E1-E8, with E9 flagging one untested dimension
worth a recorded decision before finalizing). Tier 0/1/2 situational
policy remains open. Anatomical index-to-zone mapping remains a
separate, unresolved subsystem (likely Setting-Module scope --
S-2 v1.1 SS B, SS H; Roadmap Phase 12).

Tier-1 Location Index:
  Recommended:  Zero-Step
                (E1, E2, E3, E4, E6, E7 -- pending designer ruling)
  Retained as optional coarse/specialised alternative:
                Units-Digit
                (exact and mapping-stage-free only when a table has
                precisely ten equal-weight zones -- E1, E5)

Tier 0: Valid, unchanged.
Tier 2: Reserved / future, unchanged.

Apportionment algorithm (largest-remainder / Hare quota): the
experimental tool used to run this comparison. Not proposed as a
canonical mapping rule -- remains Location-Table/Mapping-spec scope
(S-2 v1.1 SS C.3).
```

---

## 3. Proposed S-2 v1.2 Section — "Tier-1 Location Index Provider"

> ## Tier-1 Location Index Provider
>
> **Status:** Preferred candidate — pending formal designer ruling. Not yet locked.
>
> Exhaustive comparison (Evidence Record, E1–E9) of the two Brief §2.2-named Tier-1 candidates indicates
> Zero-Step provides materially greater location-resolution capacity than Units-Digit, at a modest,
> well-characterized cost.
>
> | Provider | Native domain | Native resolution | Index→zone mapping stage required |
> |---|---|---|---|
> | Zero-Step | 1–100 | 1 percentage point | Yes, always |
> | Units-Digit | 1–10 | 10 percentage points | Only when zone count ≠ 10 |
>
> Units-Digit is exact and mapping-stage-free specifically when a table has precisely ten equal-weight
> zones (E1, E5). Outside that case, its coarser domain can leave low-weight zones structurally
> unreachable (E3, E4) and produces distribution error up to 10× larger than Zero-Step's under otherwise
> identical conditions (E2, E6).
>
> The choice of Tier-1 provider does not determine the anatomical mapping algorithm. The mapping layer —
> index → named zone, zone weights, symmetry, apportionment, table-order independence, reachability,
> anatomical hierarchy — remains a separate, unresolved subsystem (§B, §H of this document).
>
> **Before lock:** E9 (derivation-stage table usability) has not been evaluated and should be weighed
> alongside the evidence above, even if briefly.

---

## 4. Roadmap Annotation Proposal (lighter-weight alternative to a full S-2A/B/C split)

ChatGPT's round-4 review (§24) proposes decomposing S-2 into three new top-level residual IDs. The
round-4 assessment (§C.3) recommends a smaller edit that captures the same distinction without threading
new IDs through the Roadmap's dependency graph, phase mapping, and acceptance criteria. Proposed as a
targeted diff to the existing `Tiwas_Universal_System_Synthesized_Roadmap.md` §3.1 Ranked Residuals table:

**Current:**

| Priority | ID | Gap | Status | Primary dependency |
|---:|---|---|---|---|
| 2 | S-2 | Hit-location policy: Tier 0/1/2 and situation use | Open | S-1 |

**Proposed:**

| Priority | ID | Gap | Status | Primary dependency |
|---:|---|---|---|---|
| 2 | S-2 | Hit-location policy: Tier 0/1/2 and situation use. **Tier-1 formula sub-question (Zero-Step vs. Units-Digit) is evidence-backed — see S-2 Evidence Record — pending designer lock; tier-selection policy itself remains Open.** | **Formula: evidence-backed / Policy: Open** | S-1 |

No change to §4's dependency graph, §5's phase mapping, or §6's Phase 2 acceptance criteria is proposed —
the anatomical-mapping-belongs-to-Setting-Modules boundary these would otherwise restate already exists
(Roadmap Phase 12; S-2 v1.1 §B, §H).

**Alternative on file:** if the designer prefers explicit, separately-trackable IDs instead, ChatGPT's
S-2A (index provider) / S-2B (tier policy) / S-2C (anatomical mapping) split is a legitimate, more
thorough option — just a larger structural edit than the one proposed here.

---

## 5. What Remains Explicitly Open

Unchanged from every prior round — restated once here for a single point of reference:

- Tier 0/1/2 situational default (no tier is ever named "the" default — S-2 v1.1 §E, by source constraint)
- The anatomical location table itself (zone names, weights, hierarchy) — no such table exists yet
- The apportionment/index-to-zone mapping algorithm — largest-remainder was an experimental tool, not a proposed rule
- Symmetry-preservation mechanics for that future mapping algorithm
- Tier 2's internal mechanics
- E9 (table usability at the derivation stage) — flagged, not resolved
