---
document:
  title: "Tiwas — S-3 Outcome Effects: Documentarian Handoff Report (Final — Thread Closed)"
  version: "1.0"
  status: "Non-canonical working record — for project documentarian (opencode)"
  audience: "opencode (GitHub Documentarian)"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
  supersedes:
    - "tiwas-s3-documentarian-handoff-report-2026-08-29.md"
    - "tiwas-s3-documentarian-handoff-report-dec025-2026-08-29.md"
    - "tiwas-s3-documentarian-handoff-report-dec026-2026-08-29.md"
    - "tiwas-s3-documentarian-handoff-report-dec027-2026-08-29.md"
provenance:
  author: "Design Session 2026-08-29"
  prepared_by: "Grok 4.5 (Lead Systems Architect)"
---

# TIWAS — S-3 OUTCOME EFFECTS  
## Documentarian Handoff Report (Final — Thread Closed)

**For:** opencode (GitHub Documentarian)  
**From:** Design Session 2026-08-29  
**Status:** Non-Canonical Working Record  
**Focus:** Complete closure of the Effect Identity & Multi-Effect Opposition investigation thread (all Q-S3 items ruled)

---

## 1. Purpose of this Report

This report is the authoritative final handoff for the S-3 Effect Identity & Multi-Effect Opposition design thread. It records the complete set of in-session designer rulings issued 2026-08-29, confirms that every tracked open item has been closed, lists every file that must be treated as current, and supplies explicit filing instructions for the project documentarian.

This report **supersedes** all prior S-3 handoff reports issued the same day:
- `tiwas-s3-documentarian-handoff-report-2026-08-29.md`
- `tiwas-s3-documentarian-handoff-report-dec025-2026-08-29.md`
- `tiwas-s3-documentarian-handoff-report-dec026-2026-08-29.md`
- `tiwas-s3-documentarian-handoff-report-dec027-2026-08-29.md`

**Nothing in this report is Canonical.** All rulings remain non-canonical designer decisions pending the full 8-step Promotion Rule (Proposals/WIP §21 / REQ-021).

---

## 2. Executive Status — S-3 Rulings (Final)

Eight designer rulings are closed. Zero items remain open inside the Effect Identity & Multi-Effect Opposition investigation thread.

| ID | Subject | Decision Summary | Status |
|---|---|---|---|
| **DEC-023** | Effect menu structure (Q-S3-1) | Tiered menu. Base: Inflict Injury (HP-only) + Open Retreat / Compel Yield. Five gated tiers keyed to subsystem lock status. | **Ruled** |
| **DEC-024** | Multiplicity (Q-S3-2) | Flat one-Effect-per-win. No Quality scaling. Additional Effects require a separate opposed roll. | **Ruled** |
| **DEC-025** | Effect identity / naming (Q-S3-2a) | Pure declared intent. Skill name never entitles or gates any Effect. Formal tag/category system on Advanced Skills rejected. | **Ruled** |
| **DEC-026** | Second-Effect roll (Q-S3-2b) | Different Advanced Skill (domain-appropriate) + defensive roll deferred until S-6. Full 9-step Core Test Transaction. Same-Skill and flat-check rejected. | **Ruled** |
| **DEC-027** | Application mode (Q-S3-5) | Auto-apply. Winning S-1 with declared Effect applies it directly. Contested application rejected as default; residual resistance deferred to S-6. | **Ruled** |
| **DEC-028** | Tag+Location gating (Q-S3-3) | Disarm/Break Hold, Equipment Damage, Armor Bypass require both matching Tag **AND** supporting Location Index (Tier 1+). Function Impairment and Incapacitation deferred out of S-3. | **Ruled** |
| **DEC-029** | S-3/S-4 boundary (Q-S3-4) | Prototype-only boundary. No interface work needed yet. S-4 direction recorded as non-binding steer. | **Ruled** |
| **DEC-030** | Partial match (Q-S3-3a) | Fail-and-fall-back. Partial Tag/Location match → declared gated Effect fails; contest applies Base Inflict Injury (HP-only). No residual state. | **Ruled** |

**Thread status:** `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` is now **Closed**.

---

## 3. Ruling Summaries (Authoritative Text)

### DEC-023 — Tiered Effect Menu
Base tier (usable now): Inflict Injury (HP-only form) + Open Retreat / Compel Yield.  
Five gated tiers unlock automatically when their owning subsystem locks (Position → Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6; Location → S-2 invocation promotion).  
Disarm/Break Hold placed via DEC-028 combined Tag+Location gating.

### DEC-024 — Flat One-Effect-per-Win
No Quality-based scaling and no purchasing of additional Effects off a single win. Every successful S-1 contest earns exactly one Effect from currently unlocked tiers. Any second/additional Effect requires a separate opposed roll (mechanism settled by DEC-026).

### DEC-025 — Pure Declared Intent
Effects are granted solely by the declared outcome of a successful S-1 contest (subject to any other gates already ruled). Skill name carries zero mechanical weight and does not entitle or gate any Effect. Formal tag/category system on Advanced Skills is rejected (exploitation risk; player self-limitation to degenerate mechanical Skills).

### DEC-026 — Second-Effect Opposed-Roll Mechanism
- Skill basis: **Different Advanced Skill** that is domain-appropriate to the declared second Effect. Actor accepts the risk.
- Transaction: Full 9-step Core Test Transaction (REQ-018).
- Defensive roll: **Deferred / none until S-6 locks**. Any provisional resistance is non-canonical scaffolding only and must be discarded when S-6 locks.
- Same-Skill and flat-check options rejected.

### DEC-027 — Auto-Apply
Winning S-1 with a declared Effect applies that Effect directly (subject to existing gates). Contested application is rejected as the S-3 default. S-6 remains free to introduce Tags or options that counter or prevent specific Effects after they would otherwise auto-apply (example: locked gauntlets prevent Disarm). Any future contested-application mechanic is deferred to S-6 as an optional modifier.

### DEC-028 — Combined Location + Tag Gating
For the three in-scope Effects (Disarm/Break Hold, Equipment Damage, Armor Bypass): trigger requires **both** a matching gear/ability Tag **and** a supporting Zero-Step Location Index (Tier 1+).  
Function Impairment → deferred to S-4/Condition.  
Incapacitation → deferred to S-7.

### DEC-029 — S-3/S-4 Boundary
Confirmed prototype-only. No S-3/S-4 interface work needed yet (base-tier Injury is HP-only). Roadmap §10 boundary holds. S-4 *direction* recorded as non-binding steer for a future S-4 investigation only.

### DEC-030 — Fail-and-Fall-Back
On partial Tag/Location match (exactly one of the two gates satisfied), the declared gated Effect fails entirely. The successful contest instead applies Base-tier Inflict Injury (HP-only). No residual Advantage, magnitude, duration, or secondary state is generated. Disarm/Break Hold tier and failure behaviour are fully determined (binary gate identical to Equipment Damage and Armor Bypass).

---

## 4. Implementation Path (Buildable Now)

```
1. Actor declares Effect and nominates Skill.
2. S-1 opposed contest resolves under Core Test Transaction.
3. On win:
   a. Evaluate gates (Tag + Location Index where required by DEC-028).
   b. Full match → declared Effect applies (DEC-027 auto-apply).
   c. Partial or full miss on gated Effect → fall back to Base Inflict Injury HP-only (DEC-030).
4. Free Effect is now applied (or fallen back).
5. Actor may optionally declare a second Effect.
6. Actor nominates a *different* Advanced Skill that is domain-appropriate (DEC-026).
7. Full Core Test Transaction executes under that Skill.
8. Success → second Effect applies (re-evaluate its own gates independently).
9. Failure → second Effect denied; free Effect remains; normal Cost + Failure XP applied only to the second Skill.
```

No residual Margin, Advantage, or state is carried from the first contest into the second roll.

---

## 5. Files That Must Be Treated as Current

| File Path | Authority for |
|---|---|
| `_consolidation/decision-register.md` (§D) | All eight DEC-023…DEC-030 entries and carried-forward status |
| `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` | Full ruling text for DEC-025, DEC-026, DEC-027, DEC-030; thread status = Closed |
| `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` | Original DEC-023, 024, 028, 029 rulings and context |
| `investigations/tiwas-s3-outcome-effects-investigation-v0.1-draft.md` | Main S-3 investigation (must later absorb the closed items) |
| This report | Final status authority and filing instructions for documentarian |

---

## 6. Recommended Filing Actions for Documentarian

### Immediate

1. Commit the two primary updated files:
   - `_consolidation/decision-register.md`
   - `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md`
   with a clear message referencing DEC-026 and thread closure.
2. Confirm the investigation header status line reads:  
   `Closed. All items (Q-S3-2a / DEC-025, Q-S3-2b / DEC-026, Q-S3-5 / DEC-027, Q-S3-3a / DEC-030) ruled 2026-08-29.`
3. Archive or mark superseded the four earlier handoff reports listed in the document header.

### Near-term (proposals layer)

1. Mirror all eight session rulings into `proposals/` as §3.4 (or equivalent S-3 subsection).
2. Cross-reference the proposals subsection from decision-register §D.
3. Update the main S-3 Outcome Effects investigation draft to mark Q-S3-1 through Q-S3-5 and Q-S3-3a as Ruled and to incorporate the final mechanism text.

### Explicitly Do Not Do

- Do **not** promote any of these rulings to Canonical Rules. The 8-step Promotion Rule has not been run.
- Do **not** merge session-derived rulings (§D) into decision-register §B (corpus-derived). Preserve provenance distinction.
- Do **not** pre-build a permanent defensive layer for the second-effect roll (DEC-026 defers it).
- Do **not** introduce Skill-side tags, categories, or Effect-entitlement vocabulary (DEC-025 rejected that path).
- Do **not** treat the S-4 direction recorded under DEC-029 as binding.

---

## 7. Remaining Open Work (Outside This Thread)

| Area | Status | Notes |
|---|---|---|
| Main S-3 Outcome Effects investigation | Still open for proposal incorporation | Must absorb DEC-023…DEC-030 |
| S-6 Defense | Open | Defensive half of second-effect roll and any contested-application modifier deferred here |
| S-4 Wounds | Open | DEC-029 boundary and direction are non-binding steers only |
| Anatomical mapping table | Open | Required for DEC-028 Location Index consumption |
| Tags subsystem starter vocabulary | Open | Required for DEC-028 Tag gate |
| Promotion of any S-3 ruling to Canonical | Not started | Requires full 8-step process |

No open designer forks remain inside the Effect Identity & Multi-Effect Opposition investigation itself.

---

## 8. Governance Reminders

- **Authority hierarchy:** only `canonical/rules/` contains locked game mechanics. Everything else is non-canonical design material.
- **Evidence class:** all items in decision-register §D are “Non-canonical designer ruling.”
- **Roadmap §24 Rule 6:** never silently resolve an open designer fork. With DEC-026 closed, this thread has none left.
- **Provenance:** session-derived rulings (§D) must remain distinct from corpus-derived rulings (§B).
- **Canonical §12.3:** Skill names carry zero mechanical weight. “Domain-appropriate” under DEC-026 is a lineage/domain judgment only.
- **REQ-017 / REQ-018:** no competing economy introduced; all resolution remains inside the Core Test Transaction.

---

## 9. Suggested Next Step for Documentarian

1. Commit the closed-thread files.
2. Update the main S-3 investigation draft and proposals layer to reflect the eight closed rulings.
3. No further design prompts are required inside the now-closed Effect Identity & Multi-Effect Opposition thread.

---

*— End of Final Handoff Report —*  
*All content non-canonical. Prepared for internal project documentation use only.*  
*Prepared by Grok 4.5 (Lead Systems Architect) for opencode (GitHub Documentarian), 2026-08-29.*
