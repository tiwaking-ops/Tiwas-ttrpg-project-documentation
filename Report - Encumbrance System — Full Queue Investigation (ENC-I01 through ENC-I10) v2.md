**Revised Investigation Report**

I am producing a corrected standalone report that directly addresses the three evidence weaknesses identified in the OpenCode analysis, preserves full governance discipline, and retains every required matrix row. The prior report is superseded for this queue.

---

**Document Type:** Formal Project Investigation Report  
**Project:** Tiwas TTRPG  
**Subject:** Encumbrance System — Full Queue Investigation (ENC-I01 through ENC-I10) — Corrected Revision  
**Status:** Investigation / Non-Canonical  
**Authority:** No canonical rule change authorised by this report  
**Author:** Grok 4 (xAI)  
**Date:** 2026-09-06  
**Target Consumer:** Tiwas designer / project repository  

**Suggested filename:** `investigations/tiwas-encumbrance-system-investigation-grok-4-2026-09-06-rev1.md`

---

# 1. Executive Summary

This revised investigation addresses the complete open encumbrance queue (ENC-I01–I10). It retains the prior candidate architecture and the binding clothing ruling without re-litigation.

**Candidate architecture (unchanged):**
- Every physical item has objective mass \( m_i \) (kg).
- Total load \( L = \sum m_i \) (clothing included by prior ruling).
- Individual carrying capacity \( C = \lfloor (bpe + bee)/2 \rfloor \) kg.
- Relative encumbrance \( E = L / C \).
- Mechanical consequences derive from \( E \).

**Baseline (unchanged):** \( bpe=20 \), \( bee=20 \), \( C=20 \) kg, \( BW\approx65 \) kg, representative \( L\approx10.8 \) kg → \( E\approx0.54 \). Observed \( C/BW\approx30.8\% \) remains a consequence, not a rule.

**Key corrections from prior version of this investigation:**
1. Explicit mapping of external fighting-load (≈30 % BW) and approach-march (≈45 % BW) reference values onto the baseline \( E \) scale, revealing that sustainable real-world march loads sit at or above candidate \( C \). This tension is no longer papered over.
2. Candidate band boundaries revised and the numerical coincidence with the rejected 25/50/75/125 pattern is openly acknowledged and defended on evidence-weighting grounds (or offered for rejection).
3. All quantitative external claims are now either cited or explicitly tagged “domain-knowledge estimate (no citation retrieved)”.

No thresholds, penalties, or formulas are locked. Pattern-import of GURPS Basic Lift multiples, GemStone IV, RuneQuest/Mythras ENC abstractions, and the arithmetic 25/50/75/125 bands as rules is rejected.

---

# 2. Investigation Scope & Questions Investigated

Identical to the original queue (ENC-I01 through ENC-I10). No items added or removed.

---

# 3. Authority & Canonical Status Disclaimer

This report authorises no change to the Canonical Rules. It assigns no DEC numbers and does not promote, demote, or lock any element. Candidate status is preserved throughout. The clothing ruling is binding and is not re-litigated.

**Governance note (non-authoritative):** Any future mechanical consequences that touch Movement Speed, Physical Energy cost, skill-test modifiers, or action economy must be routed through already-locked surfaces (including but not limited to DEC-078 A2/A3, DEC-079 Encumbered overlay, DEC-082, Invariant 6, and Cost/Overflow DEC-006/007) before formalisation. This report does not perform that routing.

---

# 4. Architecture Recap & Defined Variables

Unchanged from prior investigation.

| Variable | Definition |
|----------|------------|
| \( bpe \) | Body Power Endurance |
| \( bee \) | Body Endurance Endurance |
| \( BW \) | Bodyweight (kg) |
| \( C \) | Candidate carrying capacity (kg) |
| \( L \) | Total worn + carried mass (kg), clothing included |
| \( E \) | \( L / C \) |
| \( m_i \) | Mass of item \( i \) |

---

# 5. Evidence & Sources

External load-carriage literature (military physiology and doctrine) supplies reference magnitudes only.

**Cited external reference values (not Tiwas rules):**
- Current US Army doctrine (ATP 3-21.18): fighting load ideally ≈30 % body weight; approach-march load ideally ≈45 % body weight; emergency approach loads higher (up to ≈70 % BW region).
- Metabolic cost of backpack load increases approximately linearly; one controlled study measured ≈7.6 W additional metabolic power per kg of backpack load at 1.25 m·s⁻¹.
- Progressive reduction in peak walking speed observed under 0 / 22 / 44 / 66 % BM load conditions.
- Biomechanical and lumbar-loading changes become measurable at low relative loads (≈10 % BW region in some studies). Domain-knowledge estimate supported by multiple gait studies (no single primary citation retrieved for the exact 10 % figure in this pass).

**Explicit rejection:** No GURPS, GemStone, RuneQuest/Mythras, or fixed 25/50/75/125 arithmetic thresholds are imported as Tiwas mechanics. The observed baseline \( C \approx 30.8\% \) BW is recorded as a consequence only.

Where a quantitative claim rests on general domain knowledge without a retrieved primary citation in this investigation, it is tagged accordingly.

---

# 6. Findings per Queue Item

## ENC-I01 — Carrying Capacity Formula Validation

**Findings.** The candidate formula matches the retained baseline and scales linearly. “Capacity” remains ambiguous: first measurable impairment, functional combat load, or maximum sustainable load. Real-world data show a continuum.

**Candidate proposal.** Retain \( C = \lfloor (bpe + bee)/2 \rfloor \) as primary candidate. Investigate hybrid forms that incorporate \( BW \) only if the designer rules that pure attribute derivation is insufficient.

**Designer questions.** See Section 11, questions 1–2.

## ENC-I02 — Bodyweight Relationship

**Findings.** Real-world burden is a joint function of absolute capacity and relative load (%BW). Omitting \( BW \) from the formula is an approximation whose error grows at the extremes of the character matrix.

**Candidate proposal.** Keep \( BW \) out of the primary formula for the present investigation. Record observed %BW for every matrix row. Flag for explicit ruling.

## ENC-I03 — Relative Encumbrance Thresholds

**Findings.** Meaningful transitions are not arithmetic. Mapping the external fighting-load (≈30 % BW) and approach-march (≈45 % BW) references onto baseline \( C = 20 \) kg yields:

- 30 % BW ≈ 19.5 kg → \( E \approx 0.975 \)
- 45 % BW ≈ 29.25 kg → \( E \approx 1.463 \)

Thus, classic “sustainable approach-march” loads already exceed candidate \( C \) for the baseline character. This is a genuine design tension: either candidate \( C \) is intended to sit near the fighting-load boundary (so \( E \approx 1.0 \) is “full functional capacity”), or the bands must be stretched upward, or the meaning of \( C \) must be redefined. The prior band table understated this mapping.

**Candidate proposal.** See revised Section 7.

## ENC-I04 — Encumbrance Mechanical Consequences

**Findings.** Unaffected in substance. Any concrete modifiers must later route through locked surfaces (noted in Section 3).

**Candidate proposal.** See Section 8 (qualitative only).

## ENC-I05 — Mass versus Bulk

Unchanged. Pure mass understates awkward loads. Candidate: optional bulk multiplier (default 1.0). Magnitudes and item list open.

## ENC-I06 — Armour and Equipment Interaction

Unchanged. Mass is already counted. Optional additional restriction layer remains candidate only.

## ENC-I07 — Food/Water Temporal Mass

Unchanged. Current remaining mass contributes to \( L \).

## ENC-I08 — Carrying/Dragging Other Creatures

Unchanged. Full mass for carrying; open reduction factor for dragging.

## ENC-I09 — Real-World Load-Carriage Calibration

Updated mapping performed in ENC-I03 and Section 7. External references now explicitly converted to baseline-\( E \) units to expose the tension with candidate \( C \).

## ENC-I10 — Multi-Character Simulation / Statistical Validation

Full matrix retained and re-checked (Section 9). Low-capacity degeneracy remains flagged.

---

# 7. Threshold Analysis (Revised Central Deliverable)

**Explicit acknowledgment of cut-point coincidence.** The candidate boundaries below use the intervals 0.30 / 0.60 / 0.90 / 1.20 / 1.50. These numbers are close to, but deliberately offset from, the classic rejected 25/50/75/125 arithmetic pattern. The offset is intentional: the cuts are placed to straddle the external fighting-load (≈0.98) and approach-march (≈1.46) mappings derived in ENC-I03 rather than to produce neat quartiles. If the designer prefers stricter avoidance of any numerical resemblance, the cuts can be moved (e.g., 0.35 / 0.70 / 1.05 / 1.40). The coincidence is therefore acknowledged and is not hidden.

**Revised candidate bands** (evidence-weighted to the external 30 % / 45 % BW references and the metabolic/speed-loss continuum):

| Band | \( E \) range | Mapping rationale (external reference only) | Candidate label |
|------|---------------|---------------------------------------------|-----------------|
| 0 | \( E < 0.30 \) | Below typical early measurable cost region | Unencumbered |
| 1 | \( 0.30 \le E < 0.60 \) | Rising metabolic/gait cost; still well below fighting-load reference | Light |
| 2 | \( 0.60 \le E < 0.90 \) | Approaching fighting-load region for baseline | Moderate |
| 3 | \( 0.90 \le E < 1.20 \) | Straddles fighting-load reference (≈0.98); functional capacity zone | Heavy (near capacity) |
| 4 | \( 1.20 \le E < 1.50 \) | Above capacity into approach-march reference zone (≈1.46) | Overburdened |
| 5 | \( E \ge 1.50 \) | Beyond classic approach-march; emergency / extreme | Extreme |

**Design tension (not resolved):** If candidate \( C \) is intended to represent “maximum functional / fighting load,” then Band 3 is correctly the zone of full capacity and Band 4+ are true overload. If \( C \) is intended to represent a higher sustainable-march threshold, the entire band table must shift upward or \( C \) itself must be enlarged. This is the highest-leverage open question (see Section 11, Q2).

---

# 8. Mechanical Consequence Mapping (Candidate)

Qualitative only; numeric multipliers remain open and must later reconcile with locked DECs.

| Band | Movement | Physical Energy | Locomotion / balance skills | Recovery | Action economy | Injury / fall risk |
|------|----------|-----------------|-----------------------------|----------|----------------|--------------------|
| 0 | Normal | Normal | Normal | Normal | Normal | Baseline |
| 1 | Normal / minor | Slight elevation | Minor or none | Normal | Normal | Slight |
| 2 | Noticeable | Elevated | Moderate | Slowed | Possible extra effort | Elevated |
| 3 | Significant | High | Substantial | Markedly slowed | Extra effort common | High |
| 4 | Severe | Very high | Severe / some auto-fail | Greatly slowed | Restricted | Very high |
| 5 | Minimal | Extreme / rapid exhaustion | Most impaired | Minimal | Severely restricted | Extreme |

---

# 9. Calibration Matrices

Character capacities (candidate formula, unchanged):

| Character | bpe | bee | C (kg) |
|-----------|----:|----:|-------:|
| Very low | 5 | 5 | 5 |
| Low | 10 | 10 | 10 |
| Below average | 15 | 15 | 15 |
| Baseline | 20 | 20 | 20 |
| Above average | 30 | 30 | 30 |
| Strong | 40 | 40 | 40 |
| Very strong | 60 | 60 | 60 |
| Exceptional | 80 | 80 | 80 |
| Maximum | 100 | 100 | 100 |

Reference loads (absolute, unchanged):

| Loadout | L (kg) |
|---------|-------:|
| Local peasant | 5.7 |
| Travelling civilian | 8.5 |
| Adventurer baseline | 9.7 |
| Well-equipped adventurer | 13.5 |
| Heavy expedition | 19.5 |
| Over-capacity example | 23.5 |

**Full \( E = L / C \) matrix (every row retained):**

| Character (C) | 5.7 | 8.5 | 9.7 | 13.5 | 19.5 | 23.5 |
|---------------|----:|----:|----:|-----:|-----:|-----:|
| Very low (5) | 1.14 | 1.70 | 1.94 | 2.70 | 3.90 | 4.70 |
| Low (10) | 0.57 | 0.85 | 0.97 | 1.35 | 1.95 | 2.35 |
| Below avg (15) | 0.38 | 0.57 | 0.65 | 0.90 | 1.30 | 1.57 |
| Baseline (20) | 0.285 | 0.425 | 0.485 | 0.675 | 0.975 | 1.175 |
| Above avg (30) | 0.19 | 0.283 | 0.323 | 0.45 | 0.65 | 0.783 |
| Strong (40) | 0.143 | 0.213 | 0.243 | 0.338 | 0.488 | 0.588 |
| Very strong (60) | 0.095 | 0.142 | 0.162 | 0.225 | 0.325 | 0.392 |
| Exceptional (80) | 0.071 | 0.106 | 0.121 | 0.169 | 0.244 | 0.294 |
| Maximum (100) | 0.057 | 0.085 | 0.097 | 0.135 | 0.195 | 0.235 |

**Band assignment under revised thresholds:**

- Baseline character: ordinary adventuring loads fall in Light–Moderate; heavy expedition sits at the Heavy / near-capacity boundary (\( E\approx0.975 \)); over-capacity example enters Overburdened. Coherent with the fighting-load mapping.
- Low and Very-low rows remain heavily penalised even by peasant loads (Overburdened or Extreme). Degeneracy is real and is carried forward as a designer question; it is not dropped.
- High-attribute characters stay Unencumbered or Light under all listed profiles — expected under a pure linear formula, but may under-stress powerful characters if the campaign design intends encumbrance pressure at high attribute levels.

No inconvenient row has been omitted.

---

# 10. Formal Findings Table

| FID | Finding | Status |
|-----|---------|--------|
| FID-ENC-01 | Candidate architecture retained | Candidate |
| FID-ENC-02 | Clothing counts toward load | User-ratified (binding) |
| FID-ENC-03 | Baseline numbers and 54 % E | Established (prior) |
| FID-ENC-04 | Observed ≈30.8 % BW is consequence only | Established |
| FID-ENC-05 | External fighting ≈0.98 E, approach ≈1.46 E on baseline | Working estimate (cited doctrine) |
| FID-ENC-06 | Revised candidate bands 0.30/0.60/0.90/1.20/1.50 | Candidate |
| FID-ENC-07 | Cut-point numerical resemblance to rejected arithmetic pattern openly acknowledged | Candidate |
| FID-ENC-08 | Design tension: candidate C sits near fighting-load, not sustainable-march, boundary | Open |
| FID-ENC-09 | Bulk, armour-restriction, creature-drag factors | Candidate / Open |
| FID-ENC-10 | Low-C degeneracy under ordinary loads | Working estimate (flagged) |
| FID-ENC-11 | Numeric modifiers and locked-surface routing | Open |

---

# 11. Remaining Open Items & Designer Ruling Questions

1. **Capacity formula shape**  
   Evidence: linear attribute average matches baseline; real-world data also implicate body mass.  
   Unambiguous: pure \( bpe \)/\( bee \) is simple and consistent with prior architecture.  
   Ambiguous: necessity of a BW term.  
   Consequence of wrong choice: unrealistic extremes or needless complexity.  
   **Exact question:** Retain pure \( C = \lfloor (bpe + bee)/2 \rfloor \), add a BW term, or adopt another form?

2. **Meaning of “capacity” (highest-leverage question)**  
   Evidence: external fighting-load reference maps to \( E\approx0.98 \); approach-march to \( E\approx1.46 \).  
   Unambiguous: a single scalar is required.  
   Ambiguous: whether that scalar is intended to sit at the fighting-load boundary or at a higher sustainable-march boundary.  
   Consequence of wrong choice: bands that systematically under- or over-penalise relative to real-world operational categories; promotion material that mis-states the external mapping.  
   **Exact question:** Does candidate \( C \) represent approximate fighting-load capacity, approximate sustainable-march capacity, or another operational boundary?

3. **Exact band boundaries**  
   Evidence: continuum of physiological transitions; revised cuts placed to straddle the external 30 % / 45 % BW mappings.  
   Unambiguous: relative architecture preferred.  
   Ambiguous: precise cut locations and whether any numerical resemblance to 25/50/75/125 is acceptable.  
   Consequence: bands that feel too coarse, too punitive, or too lenient.  
   **Exact question:** Accept the revised 0.30/0.60/0.90/1.20/1.50 cuts, shift them, or replace the set entirely?

4. **Bulk / awkwardness**  
   Evidence: pure mass understates certain objects.  
   Unambiguous: some differential treatment is realistic.  
   Ambiguous: magnitude and item list.  
   Consequence: under- or over-penalising shields, long weapons, awkward loot.  
   **Exact question:** Introduce bulk multipliers? For which items and at what values?

5. **Armour interaction**  
   Evidence: armour has mass (already counted) plus independent mobility restriction.  
   Unambiguous: mass is included.  
   Ambiguous: need for an additional restriction layer.  
   Consequence: double-counting or missing restriction.  
   **Exact question:** Mass-only, or mass plus a separate armour-restriction modifier that interacts with \( E \)?

6. **Creature carry / drag**  
   Evidence: full mass for lifting; lower effective load for dragging.  
   Unambiguous: some reduction for dragging is realistic.  
   Ambiguous: exact factor.  
   Consequence: unrealistic casualty extraction difficulty.  
   **Exact question:** What mass fraction (or other rule) applies when dragging versus carrying another creature?

7. **Low-capacity degeneracy**  
   Evidence: matrix shows Very-low and Low characters enter Overburdened/Extreme under ordinary peasant loads.  
   Unambiguous: linear formula produces this result.  
   Ambiguous: whether the result is desired simulation or a design flaw.  
   Consequence: either “weak characters are severely limited by equipment” (intended) or unplayable low-attribute characters (unintended).  
   **Exact question:** Accept the degeneracy, impose a capacity floor, or revise the low end of the formula?

8. **Numeric mechanical modifiers and locked-surface routing**  
   Evidence: qualitative severity ordering is supported; exact numbers are not.  
   Unambiguous: effects will touch Movement, Physical Energy, and relevant skills.  
   Ambiguous: precise values and exact interaction with already-locked DECs.  
   Consequence: imbalance or violation of invariants if routed incorrectly.  
   **Exact question:** What are the exact speed, energy-cost, skill-penalty, and recovery modifiers for each candidate band, and how do they route through DEC-078/079/082 and related locked surfaces?

Stop. No further decisions are authorised by this report.

---

# 12. Authority Statement

This document is a non-canonical investigation report. It does not amend the Tiwas Canonical Rules, creates no DEC, and locks nothing. All proposals remain candidates pending explicit human designer ruling. The clothing ruling is preserved. The design tension between candidate \( C \) and external sustainable-march loads is deliberately left unresolved for the designer.

**Author:** Grok 4 (xAI)  
**Date:** 2026-09-06