---
document:
  title: "Tiwas — S-3 Outcome Effects: Documentarian Handoff Report (DEC-026)"
  version: "1.0"
  status: "Non-canonical working record — for project documentarian (opencode)"
  audience: "opencode (GitHub Documentarian)"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
  supersedes: "tiwas-s3-documentarian-handoff-report-dec025-2026-08-29.md with respect to DEC-026 status and open-item priority"
provenance:
  author: "Design Session 2026-08-29"
  prepared_by: "Grok 4.5 (Lead Systems Architect)"
---

# TIWAS — S-3 OUTCOME EFFECTS  
## Documentarian Handoff Report (DEC-026)

**For:** opencode (GitHub Documentarian)  
**From:** Design Session 2026-08-29  
**Status:** Non-Canonical Working Record  
**Focus:** DEC-026 / Q-S3-2b — Second-Effect Opposed-Roll Mechanism

---

## 1. Purpose of this Report

This report records the designer ruling on **DEC-026 / Q-S3-2b** (Second-Effect opposed-roll mechanism) issued 2026-08-29. It updates the executive status of all S-3 session rulings, lists files modified to capture the ruling, and provides filing instructions for the project documentarian.

This report supersedes the open-item priority ordering in the prior handoff (`tiwas-s3-documentarian-handoff-report-dec025-2026-08-29.md`) with respect to DEC-026. All other content from prior reports remains valid unless contradicted here.

**Nothing in this report is Canonical.** All rulings remain non-canonical designer decisions pending the full 8-step Promotion Rule (Proposals/WIP §21 / REQ-021).

---

## 2. Executive Status — S-3 Rulings (Current)

Eight designer rulings are now closed. No items remain open in the Effect Identity & Multi-Effect Opposition thread.

| ID | Subject | Decision Summary | Status |
|---|---|---|---|
| **DEC-023** | Effect menu structure (Q-S3-1) | Tiered menu. Base: Inflict Injury (HP-only) + Open Retreat. Five gated tiers. | **Ruled** |
| **DEC-024** | Multiplicity (Q-S3-2) | Flat one-Effect-per-win. Additional Effects require separate opposed roll. | **Ruled** |
| **DEC-025** | Effect identity / naming (Q-S3-2a) | Pure declared intent. Skill name never entitles or gates any Effect. Formal tag system on Advanced Skills rejected. | **Ruled** |
| **DEC-026** | Second-Effect roll (Q-S3-2b) | **Different Advanced Skill + defensive deferred.** Full 9-step Core Test Transaction. Target receives no defensive roll until S-6 locks. | **Ruled** |
| **DEC-027** | Application mode (Q-S3-5) | Auto-apply. Winning S-1 with declared Effect applies it directly. Contested application rejected as default. | **Ruled** |
| **DEC-028** | Tag+Location gating (Q-S3-3) | Disarm/Break Hold, Equipment Damage, Armor Bypass require both Tag **AND** Location Index. | **Ruled** |
| **DEC-029** | S-3/S-4 boundary (Q-S3-4) | Prototype-only boundary. No interface work yet. S-4 direction recorded as non-binding steer. | **Ruled** |
| **DEC-030** | Partial match (Q-S3-3a) | Fail-and-fall-back. Partial match → Base Inflict Injury (HP-only). No residual state. | **Ruled** |

---

## 3. DEC-026 Detail — Second-Effect Opposed-Roll Mechanism

### Ruling Statement

> The separate opposed roll required for any Effect beyond the single free Effect (DEC-024) uses a **different Advanced Skill** that is domain-appropriate to the declared second Effect. The actor accepts the risk of the additional roll. The full 9-step Core Test Transaction applies (REQ-018). The target receives **no defensive roll** until S-6 is locked; any provisional resistance used in the interim is non-canonical scaffolding only and must be discarded when S-6 locks. Same-Skill and flat-check options are rejected.

### Designer Choices Recorded

| Axis | Choice | Notes |
|---|---|---|
| Skill / check basis | Different Advanced Skill (Option B) | Domain-appropriate; actor accepts risk |
| Target defensive roll | Deferred / none until S-6 (Option 2) | No permanent Defense-dependent rule pre-built |
| Transaction | Full 9-step Core Test | Already required by REQ-018; not a free variable |

### Architectural Consequences

| Item | Outcome |
|---|---|
| Multi-Effect path | High-friction; requires possession of (and risk to) a second relevant Advanced Skill |
| Resource economy | Full Cost / Overflow / Failure XP / Recovery on the second Skill only |
| Skill diversity pressure | Explicit — low-Skill-count characters are effectively capped at one Effect until they acquire appropriate Advanced Skills |
| Parallel resolution engine | None introduced (REQ-018 satisfied) |
| Competing economy | None introduced (REQ-017 satisfied) |
| Skill-name mechanical weight | Zero (Canonical §12.3 reinforced; appropriateness is domain/lineage judgment) |
| S-6 dependency | Defensive half only; core path is buildable today |
| Sequencing | Free Effect resolves first; second roll is a separate, subsequent transaction |

### Implementation Path (Buildable Now)

```
1. S-1 opposed contest resolves → free Effect (or DEC-030 fall-back) applied.
2. Actor may declare intent for a second Effect.
3. Actor nominates a different Advanced Skill that is domain-appropriate.
4. Full Core Test Transaction is executed under that Skill.
5. Success → second Effect applies (subject to its own Tag/Location gates if gated).
6. Failure → second Effect denied; free Effect remains; normal Failure XP + Cost applied to the second Skill only.
```

No residual Advantage, Margin, or state is carried from the first contest into the second roll.

---

## 4. Files Updated for DEC-026

Documentarian should treat the following as the authoritative current text for this ruling.

| File Path | Change Summary |
|---|---|
| `_consolidation/decision-register.md` | DEC-026 marked **RULED — Different Advanced Skill + defensive deferred**; carried-forward list updated (all Q-S3 items in this thread now closed) |
| `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` | Q-S3-2b closed with full ruling text; header status set to Closed; already-ruled list, recommended-next-steps, limitations, and document status updated |

---

## 5. Recommended Filing Actions for Documentarian

### Immediate (same commit if possible)

1. Commit the two updated files listed in §4 with a clear message referencing DEC-026.
2. Confirm header status line in the Effect Identity investigation reflects:  
   `Closed. All items (Q-S3-2a / DEC-025, Q-S3-2b / DEC-026, Q-S3-5 / DEC-027, Q-S3-3a / DEC-030) ruled 2026-08-29.`
3. Optionally note this report as the current status authority for DEC-026; prior handoffs remain valid for their original focus items.

### Near-term (proposals layer)

1. When mirroring session rulings into `proposals/` as §3.4 (or equivalent), include **DEC-026** alongside DEC-023, 024, 025, 027, 028, 029, 030.
2. Cross-reference the proposals subsection from decision-register §D so the records stay linked.

### Do not do

- Do **not** promote any of these rulings to Canonical Rules. The 8-step Promotion Rule has not been run.
- Do **not** merge session-derived rulings (§D) into decision-register §B (corpus-derived). Preserve provenance distinction.
- Do **not** pre-build a permanent defensive layer for the second-effect roll. DEC-026 explicitly defers that until S-6.
- Do **not** introduce a flat-check or same-Skill default; both were rejected.

---

## 6. Remaining Open Forks (Updated Priority Order)

| Pri | ID | Subject | Why Next |
|---|---|---|---|
| — | — | — | **None remaining inside the Effect Identity & Multi-Effect Opposition thread.** |

All Q-S3 items tracked by that investigation are closed. Future work returns to the main S-3 Outcome Effects investigation for proposal incorporation, or proceeds to other open subsystems (S-6, S-4, etc.).

---

## 7. Governance Reminders for Documentarian

- **Authority hierarchy:** only `canonical/rules/` is locked game mechanics. Everything else is non-canonical design material, process guidance, or governance-of-documentation.
- **Evidence class:** all Ruled items in §D are “Non-canonical designer ruling.” They do not modify Canonical Rules until the Promotion Rule completes.
- **Roadmap §24 Rule 6:** never silently resolve an open designer fork. With DEC-026 closed, no open forks remain in this thread.
- **Provenance:** session-derived rulings (§D) must remain distinct from corpus-derived rulings (§B). Do not collapse the distinction.
- **Skill names:** Canonical §12.3 is reinforced — names carry zero mechanical weight; “domain-appropriate” is a lineage/domain judgment only.

---

## 8. Suggested Next Step

The Effect Identity & Multi-Effect Opposition investigation thread is now complete. Highest-value follow-on actions:

1. Incorporate all eight S-3 session rulings (DEC-023…DEC-030) into the main S-3 Outcome Effects investigation / proposals layer.
2. When S-6 design begins, revisit the deferred defensive half of the second-effect roll.
3. No further design prompts are required inside this closed thread.

---

*— End of Handoff Report (DEC-026) —*  
*All content non-canonical. Prepared for internal project documentation use only.*
