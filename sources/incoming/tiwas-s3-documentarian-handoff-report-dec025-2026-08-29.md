---
document:
  title: "Tiwas — S-3 Outcome Effects: Documentarian Handoff Report (DEC-025)"
  version: "1.0"
  status: "Non-canonical working record — for project documentarian (opencode)"
  audience: "opencode (GitHub Documentarian)"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
  supersedes: "tiwas-s3-documentarian-handoff-report-dec027-2026-08-29.md (v1.1 — DEC-027 focus) with respect to DEC-025 status and open-item priority"
provenance:
  author: "Design Session 2026-08-29"
  prepared_by: "Grok 4.5 (Lead Systems Architect)"
---

# TIWAS — S-3 OUTCOME EFFECTS  
## Documentarian Handoff Report (DEC-025)

**For:** opencode (GitHub Documentarian)  
**From:** Design Session 2026-08-29  
**Status:** Non-Canonical Working Record  
**Focus:** DEC-025 / Q-S3-2a — Effect Identity / Naming Gate (Pure Declared Intent)

---

## 1. Purpose of this Report

This report records the designer ruling on **DEC-025 / Q-S3-2a** (Effect identity / naming gating) issued 2026-08-29. It updates the executive status of all S-3 session rulings, lists files modified to capture the ruling, and provides filing instructions for the project documentarian.

This report supersedes the open-item priority ordering in the prior handoff (`tiwas-s3-documentarian-handoff-report-dec027-2026-08-29.md`) with respect to DEC-025. All other content from that report remains valid unless contradicted here.

**Nothing in this report is Canonical.** All rulings remain non-canonical designer decisions pending the full 8-step Promotion Rule (Proposals/WIP §21 / REQ-021).

---

## 2. Executive Status — S-3 Rulings (Current)

Seven designer rulings are now closed. One item remains open.

| ID | Subject | Decision Summary | Status |
|---|---|---|---|
| **DEC-023** | Effect menu structure (Q-S3-1) | Tiered menu. Base: Inflict Injury (HP-only) + Open Retreat. Five gated tiers. | **Ruled** |
| **DEC-024** | Multiplicity (Q-S3-2) | Flat one-Effect-per-win. Additional Effects require separate opposed roll. | **Ruled** |
| **DEC-025** | Effect identity / naming (Q-S3-2a) | **Pure declared intent.** Skill name never entitles or gates any Effect. Formal tag system on Advanced Skills rejected. | **Ruled** |
| **DEC-027** | Application mode (Q-S3-5) | Auto-apply. Winning S-1 with declared Effect applies it directly. Contested application rejected as default. | **Ruled** |
| **DEC-028** | Tag+Location gating (Q-S3-3) | Disarm/Break Hold, Equipment Damage, Armor Bypass require both Tag **AND** Location Index. | **Ruled** |
| **DEC-029** | S-3/S-4 boundary (Q-S3-4) | Prototype-only boundary. No interface work yet. S-4 direction recorded as non-binding steer. | **Ruled** |
| **DEC-030** | Partial match (Q-S3-3a) | Fail-and-fall-back. Partial match → Base Inflict Injury (HP-only). No residual state. | **Ruled** |
| **DEC-026** | Second-Effect roll (Q-S3-2b) | Skill selection + whether target gets defensive roll (S-6 still Open). | **Open** |

---

## 3. DEC-025 Detail — Effect Identity / Naming Gate

### Ruling Statement

> Effects are granted solely by the declared outcome of a successful S-1 contest (subject to any other gates already ruled: gear/ability Tag + Location Index where required). The Skill name carries no mechanical weight and does not entitle or gate any Effect. Formal tag/category system on Advanced Skills is rejected.

### Designer Rationale

Formal tags and category systems can be exploited and will lead players to limit their Skill choices to only those that carry degenerate mechanical Effects.

### Architectural Consequences

| Item | Outcome |
|---|---|
| Effect identity source | Declared intent of the successful S-1 contest only |
| Skill name mechanical weight | Zero (already required by Canonical §12.3; now explicit for Effects) |
| Formal Skill-tag system | Rejected |
| New data on Advanced Skills | None |
| Dependency on Tags subsystem for Skill identity | None |
| Existing DEC-028 gates | Unaffected (Tags remain on gear/ability, not on Skills) |
| REQ-017 compliance | Satisfied — no competing classification economy introduced on Skills |
| Naming-collision surface | Closed mechanically; remains open only as fiction |

### Implementation Readiness

No additional Skill-side data or vocabulary is required for Effect identity. The application path remains:

```
Declare Effect
  → S-1 opposed contest
  → On win: evaluate existing gates (if any)
  → Gates pass → Effect applies
  → Gates fail (partial or full) → Base Inflict Injury (HP-only)
  → Core Test Transaction completes normally
```

Skill selection for the contest continues to be governed solely by the player’s declared intent and the Skill’s Cap / resource domain. The Skill’s string label is irrelevant to Effect entitlement.

---

## 4. Files Updated for DEC-025

Documentarian should treat the following as the authoritative current text for this ruling.

| File Path | Change Summary |
|---|---|
| `_consolidation/decision-register.md` | DEC-025 marked **RULED — Pure declared intent (Option B)**; carried-forward list updated (Q-S3-2a closed) |
| `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` | Q-S3-2a closed with full ruling text and designer rationale; header status reduced to one remaining open item (Q-S3-2b); already-ruled list, recommended-next-steps, and document status updated |

---

## 5. Recommended Filing Actions for Documentarian

### Immediate (same commit if possible)

1. Commit the two updated files listed in §4 with a clear message referencing DEC-025.
2. Confirm header status line in the Effect Identity investigation reflects:  
   `Open (Q-S3-2b remains). Q-S3-2a (DEC-025), Q-S3-5 (DEC-027) and Q-S3-3a (DEC-030) ruled.`
3. Optionally note this report as the current status authority for DEC-025; prior handoffs remain valid for their original focus items.

### Near-term (proposals layer)

1. When mirroring session rulings into `proposals/` as §3.4 (or equivalent), include **DEC-025** alongside DEC-023, 024, 027, 028, 029, 030.
2. Cross-reference the proposals subsection from decision-register §D so the records stay linked.

### Do not do

- Do **not** promote any of these rulings to Canonical Rules. The 8-step Promotion Rule has not been run.
- Do **not** merge session-derived rulings (§D) into decision-register §B (corpus-derived). Preserve provenance distinction.
- Do **not** introduce Skill-side tags, categories, or Effect-entitlement vocabulary. That path was explicitly rejected.
- Do **not** pre-build Tags vocabulary solely for Skill identity. Tags remain relevant only for gear/ability gates under DEC-028.

---

## 6. Remaining Open Forks (Updated Priority Order)

| Pri | ID | Subject | Why Next |
|---|---|---|---|
| 1 | DEC-026 / Q-S3-2b | Second-Effect opposed-roll mechanism | Sole remaining open item in the Effect Identity & Multi-Effect Opposition thread. Designer already clarified Advanced Skill + risk acceptance; only Skill-selection basis and defensive-roll details remain. Can proceed without S-6 lock. |

DEC-025 is closed and no longer appears in the open queue.

---

## 7. Governance Reminders for Documentarian

- **Authority hierarchy:** only `canonical/rules/` is locked game mechanics. Everything else is non-canonical design material, process guidance, or governance-of-documentation.
- **Evidence class:** all Ruled items in §D are “Non-canonical designer ruling.” They do not modify Canonical Rules until the Promotion Rule completes.
- **Roadmap §24 Rule 6:** never silently resolve an open designer fork. The one remaining Open item must stay Open until human ruling.
- **Provenance:** session-derived rulings (§D) must remain distinct from corpus-derived rulings (§B). Do not collapse the distinction.
- **Skill names:** Canonical §12.3 is reinforced — names carry zero mechanical weight for Effects as well as for resource domain and advancement.

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

*— End of Handoff Report (DEC-025) —*  
*All content non-canonical. Prepared for internal project documentation use only.*
