---
document:
  title: "Tiwas — S-3 Outcome Effects: Documentarian Handoff Report"
  version: "1.0"
  status: "Non-canonical working record — for project documentarian (opencode)"
  audience: "opencode (GitHub Documentarian)"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
provenance:
  author: "Design Session 2026-08-29"
  prepared_by: "Grok 4.5 (Lead Systems Architect)"
---

# TIWAS — S-3 OUTCOME EFFECTS  
## Documentarian Handoff Report

**For:** opencode (GitHub Documentarian)  
**From:** Design Session 2026-08-29  
**Status:** Non-Canonical Working Record  

---

## 1. Purpose of this Report

This report consolidates the current state of the S-3 Outcome Effects design thread for the project documentarian (opencode). It records all in-session designer rulings made on 2026-08-29, identifies which investigation and register files have been updated, lists remaining open forks, and provides explicit filing instructions so the GitHub documentation remains authoritative and consistent with the project's governance model.

**Nothing in this report is Canonical.** All rulings remain non-canonical designer decisions pending the full 8-step Promotion Rule (Proposals/WIP §21 / REQ-021).

---

## 2. Executive Status — S-3 Rulings

Five designer rulings were issued on 2026-08-29. One additional ruling (DEC-030) was confirmed in a follow-on exchange the same day.

| ID | Subject | Decision Summary | Status |
|---|---|---|---|
| **DEC-023** | Effect menu structure (Q-S3-1) | Tiered menu. Base: Inflict Injury (HP-only) + Open Retreat. Five gated tiers. | **Ruled** |
| **DEC-024** | Multiplicity (Q-S3-2) | Flat one-Effect-per-win. Additional Effects require separate opposed roll. | **Ruled** |
| **DEC-028** | Tag+Location gating (Q-S3-3) | Disarm/Break Hold, Equipment Damage, Armor Bypass require both Tag **AND** Location Index. | **Ruled** |
| **DEC-029** | S-3/S-4 boundary (Q-S3-4) | Prototype-only boundary. No interface work yet. S-4 direction recorded as non-binding steer. | **Ruled** |
| **DEC-030** | Partial match (Q-S3-3a) | Fail-and-fall-back. Partial match → Base Inflict Injury (HP-only). No residual state. | **Ruled** |
| **DEC-025** | Effect identity / naming (Q-S3-2a) | Formal tag system on Advanced Skills vs pure declared intent. | **Open** |
| **DEC-026** | Second-Effect roll (Q-S3-2b) | Skill selection + whether target gets defensive roll (S-6 still Open). | **Open** |
| **DEC-027** | Auto-apply vs contested (Q-S3-5) | Does winning S-1 auto-apply the Effect, or is a further check required? | **Open** |

---

## 3. DEC-030 Detail — Partial Tag/Location Match

This was the highest-priority open fork after the initial handoff. Designer confirmed **Option A — Fail-and-Fall-Back**.

### Ruling Statement

> On a partial Tag/Location match for any Tag+Location-gated Effect (Disarm/Break Hold, Equipment Damage, Armor Bypass), the declared Effect fails entirely. The successful S-1 contest instead applies the Base-tier Effect Inflict Injury (HP-only form). No residual Advantage, magnitude, duration, or secondary state is generated from the partial match.

### Designer Clarification

Any further Effect beyond the single free Effect earned by a win requires a **separate opposed roll** using an appropriate Advanced Skill. The actor accepts the risk of that additional roll. This is consistent with, and does not expand, DEC-024.

### Architectural Consequences

| Item | Outcome |
|---|---|
| Partial-match behaviour | Closed — binary fail/success only |
| Disarm/Break Hold tier | Fully determined: Tag+Location-gated category |
| Disarm/Break Hold failure | Identical to Equipment Damage & Armor Bypass (fall back to Base Inflict Injury) |
| Graded / residual Effects | Explicitly rejected for S-3 gated Effects |
| Multiplicity model | Confirmed: one free Effect; further Effects = new opposed roll + Advanced Skill |

---

## 4. Files Updated in this Session

The following files were modified to record DEC-030 and propagate the ruling. Documentarian should treat these as the authoritative current text.

| File Path | Change Summary |
|---|---|
| `_consolidation/decision-register.md` | DEC-030 marked **Ruled**; carried-forward list updated |
| `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` | Q-S3-3a closed; context section updated; Disarm/Break Hold carried-forward closed |
| `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` | Partial-match note updated to Ruled; Part 2 list revised |

---

## 5. Recommended Filing Actions for Documentarian

### Immediate (same commit if possible)

1. Commit the three updated files listed in §4 with a clear message referencing DEC-030.
2. Update the status line in the Effect Identity investigation header if any residual “no rulings yet” language remains (header status should reflect Q-S3-3a closed).
3. Add a short revision note to the designer-rulings handoff document provenance block recording the post-handoff DEC-030 confirmation.

### Near-term (proposals layer)

1. Mirror the five Ruled decisions (DEC-023, 024, 028, 029, 030) into `proposals/` as a new §3.4 (or equivalent) “S-3 Session Rulings” subsection, matching the pattern used for the S-2 candidate policy in §2.1A.
2. Cross-reference the new proposals subsection from the decision-register §D header so the two records stay linked.

### Do not do

- Do **not** promote any of these rulings to Canonical Rules. The 8-step Promotion Rule has not been run.
- Do **not** merge the session-derived rulings into decision-register §B (corpus-derived). Keep them in §D to preserve provenance distinction.
- Do **not** pre-build anatomical mapping tables or Tags vocabulary solely because of DEC-028/030. Those remain Reserved subsystems.

---

## 6. Remaining Open Forks (Priority Order)

Recommended sequence for the next design session. No silent resolution.

| Pri | ID | Subject | Why Next |
|---|---|---|---|
| 1 | DEC-026 / Q-S3-2b | Second-Effect opposed-roll mechanism | Designer already clarified Advanced Skill + risk; only Skill-selection and defensive-roll details remain. |
| 2 | DEC-027 / Q-S3-5 | Auto-apply vs contested application | Only auto-apply is buildable today (S-6 Open). Needs explicit confirmation or deferral. |
| 3 | DEC-025 / Q-S3-2a | Effect identity / naming gating | Lower urgency; naming collision is theoretical until Advanced Skills interact with named Effects in play. |

---

## 7. Governance Reminders for Documentarian

- **Authority hierarchy:** only `canonical/rules/` is locked game mechanics. Everything else is non-canonical design material, process guidance, or governance-of-documentation.
- **Evidence class:** all five Ruled items in §D are “Non-canonical designer ruling.” They do not modify Canonical Rules until the Promotion Rule completes.
- **Roadmap §24 Rule 6:** never silently resolve an open designer fork. The three remaining Open items must stay Open until human ruling.
- **Provenance:** session-derived rulings (§D) must remain distinct from corpus-derived rulings (§B). Do not collapse the distinction.

---

## 8. Suggested Next Step

Once the three files in §4 are committed, the highest-value follow-on is to open a short design prompt on **DEC-026 / Q-S3-2b** (Second-Effect opposed-roll mechanism). The designer has already constrained the Skill to “an appropriate Advanced Skill” and accepted risk; the remaining variables are:

1. Whether the target receives a defensive roll, and  
2. Exact resolution sequence.

That decision can be taken independently of S-6.

---

*— End of Handoff Report —*  
*All content non-canonical. Prepared for internal project documentation use only.*
