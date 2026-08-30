---
document:
  title: "Tiwas — S-3 Outcome Effects: Documentarian Handoff Report (DEC-027)"
  version: "1.1"
  status: "Non-canonical working record — for project documentarian (opencode)"
  audience: "opencode (GitHub Documentarian)"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
  supersedes: "tiwas-s3-documentarian-handoff-report-2026-08-29.md (v1.0 — DEC-030 focus)"
provenance:
  author: "Design Session 2026-08-29"
  prepared_by: "Grok 4.5 (Lead Systems Architect)"
---

# TIWAS — S-3 OUTCOME EFFECTS  
## Documentarian Handoff Report (DEC-027)

**For:** opencode (GitHub Documentarian)  
**From:** Design Session 2026-08-29  
**Status:** Non-Canonical Working Record  
**Focus:** DEC-027 / Q-S3-5 — Effect Application Mode (Auto-apply)

---

## 1. Purpose of this Report

This report records the designer ruling on **DEC-027 / Q-S3-5** (Auto-apply vs contested application) issued 2026-08-29. It updates the executive status of all S-3 session rulings, lists files modified to capture the ruling, and provides filing instructions for the project documentarian.

This report supersedes the open-item priority ordering in the prior handoff (`tiwas-s3-documentarian-handoff-report-2026-08-29.md` v1.0) with respect to DEC-027. All other content from that report remains valid unless contradicted here.

**Nothing in this report is Canonical.** All rulings remain non-canonical designer decisions pending the full 8-step Promotion Rule (Proposals/WIP §21 / REQ-021).

---

## 2. Executive Status — S-3 Rulings (Current)

Six designer rulings are now closed. Two items remain open.

| ID | Subject | Decision Summary | Status |
|---|---|---|---|
| **DEC-023** | Effect menu structure (Q-S3-1) | Tiered menu. Base: Inflict Injury (HP-only) + Open Retreat. Five gated tiers. | **Ruled** |
| **DEC-024** | Multiplicity (Q-S3-2) | Flat one-Effect-per-win. Additional Effects require separate opposed roll. | **Ruled** |
| **DEC-027** | Application mode (Q-S3-5) | **Auto-apply.** Winning S-1 with declared Effect applies it directly. Contested application rejected as default. | **Ruled** |
| **DEC-028** | Tag+Location gating (Q-S3-3) | Disarm/Break Hold, Equipment Damage, Armor Bypass require both Tag **AND** Location Index. | **Ruled** |
| **DEC-029** | S-3/S-4 boundary (Q-S3-4) | Prototype-only boundary. No interface work yet. S-4 direction recorded as non-binding steer. | **Ruled** |
| **DEC-030** | Partial match (Q-S3-3a) | Fail-and-fall-back. Partial match → Base Inflict Injury (HP-only). No residual state. | **Ruled** |
| **DEC-025** | Effect identity / naming (Q-S3-2a) | Formal tag system on Advanced Skills vs pure declared intent. | **Open** |
| **DEC-026** | Second-Effect roll (Q-S3-2b) | Skill selection + whether target gets defensive roll (S-6 still Open). | **Open** |

---

## 3. DEC-027 Detail — Effect Application Mode

### Ruling Statement

> Winning an S-1 opposed contest with a declared Effect applies that Effect directly. No secondary application contest is required. Gate checks (Tag + Location Index where required by DEC-028; fail-and-fall-back per DEC-030) remain in force and are evaluated once, post-win.

### Designer Clarification

S-6 (Defense) remains free to introduce Tags or equipment options that counter or prevent specific Effects after they would otherwise auto-apply.  
**Example given:** locked gauntlets prevent Disarm.

Contested application is **rejected as the S-3 default**. Any future contested-application mechanic is deferred to S-6 as an optional modifier, not an S-3 default rule.

### Architectural Consequences

| Item | Outcome |
|---|---|
| Default application path | Auto-apply (buildable against locked Core + S-1 + Zero-Step) |
| Contested application | Rejected as S-3 default; deferred to possible S-6 modifier |
| S-6 extensibility | Additive — Tags/options may nullify or interrupt specific Effects |
| Interaction with DEC-024 | Clean: one win → one Effect applied |
| Interaction with DEC-030 | Unchanged: binary gate evaluation still occurs before application |
| Extra resolution steps | None |
| Parallel resolution engine risk | None (REQ-018 preserved) |

### Implementation Readiness

The one-Effect-per-win path is now fully specified for all currently unlocked Effects:

```
Declare Effect
  → S-1 opposed contest
  → On win: evaluate gates (if any)
  → Gates pass → Effect applies
  → Gates fail (partial or full) → Base Inflict Injury (HP-only)
  → Core Test Transaction completes normally
```

No further designer decision is required to implement Base-tier Effects or the three Tag+Location-gated Effects against the locked surface.

---

## 4. Files Updated for DEC-027

Documentarian should treat the following as the authoritative current text for this ruling.

| File Path | Change Summary |
|---|---|
| `_consolidation/decision-register.md` | DEC-027 marked **RULED — Auto-apply**; carried-forward list updated (Q-S3-5 closed) |
| `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` | Q-S3-5 closed with full ruling text; context section updated to six ruled items; header status and recommended-next-steps revised; remaining open items reduced to Q-S3-2a and Q-S3-2b |

---

## 5. Recommended Filing Actions for Documentarian

### Immediate (same commit if possible)

1. Commit the two updated files listed in §4 with a clear message referencing DEC-027.
2. Confirm header status line in the Effect Identity investigation reflects:  
   `Open (Q-S3-2a, Q-S3-2b remain). Q-S3-5 and Q-S3-3a ruled.`
3. Optionally archive or note the prior handoff report (v1.0) as superseded for the DEC-027 priority row only.

### Near-term (proposals layer)

1. When mirroring session rulings into `proposals/` as §3.4 (or equivalent), include **DEC-027** alongside DEC-023, 024, 028, 029, 030.
2. Cross-reference the proposals subsection from decision-register §D so the records stay linked.

### Do not do

- Do **not** promote any of these rulings to Canonical Rules. The 8-step Promotion Rule has not been run.
- Do **not** merge session-derived rulings (§D) into decision-register §B (corpus-derived). Preserve provenance distinction.
- Do **not** pre-build S-6 Defense mechanics, anatomical mapping tables, or Tags vocabulary solely because of these rulings. Those subsystems remain Reserved / Open.
- Do **not** invent interim contested-application rules inside S-3. Contested application is explicitly deferred.

---

## 6. Remaining Open Forks (Updated Priority Order)

| Pri | ID | Subject | Why Next |
|---|---|---|---|
| 1 | DEC-026 / Q-S3-2b | Second-Effect opposed-roll mechanism | Designer already clarified Advanced Skill + risk acceptance; only Skill-selection basis and defensive-roll details remain. Can proceed without S-6 lock. |
| 2 | DEC-025 / Q-S3-2a | Effect identity / naming gating | Lower urgency; naming collision is theoretical until Advanced Skills interact with named Effects in play. |

DEC-027 is closed and no longer appears in the open queue.

---

## 7. Governance Reminders for Documentarian

- **Authority hierarchy:** only `canonical/rules/` is locked game mechanics. Everything else is non-canonical design material, process guidance, or governance-of-documentation.
- **Evidence class:** all Ruled items in §D are “Non-canonical designer ruling.” They do not modify Canonical Rules until the Promotion Rule completes.
- **Roadmap §24 Rule 6:** never silently resolve an open designer fork. The two remaining Open items must stay Open until human ruling.
- **Provenance:** session-derived rulings (§D) must remain distinct from corpus-derived rulings (§B). Do not collapse the distinction.
- **S-6 boundary:** residual resistance / counter-Effect design is explicitly owned by the future S-6 investigation. S-3 must not prototype it.

---

## 8. Suggested Next Step

Once the two files in §4 are committed, the highest-value follow-on is a design prompt on **DEC-026 / Q-S3-2b** (Second-Effect opposed-roll mechanism).

Already constrained by designer:
- Uses an appropriate Advanced Skill
- Actor accepts the risk of the additional roll

Remaining variables:
1. Exact Skill-selection rule (same Skill as original contest / different Skill / flat check)
2. Whether the target receives a defensive roll (and, if so, what primitive is used while S-6 remains Open)
3. Resolution sequence relative to the original contest’s Core Test Transaction steps

That decision can be taken independently of a full S-6 lock, provided any defensive-roll option is flagged as provisional.

---

*— End of Handoff Report (DEC-027) —*  
*All content non-canonical. Prepared for internal project documentation use only.*
