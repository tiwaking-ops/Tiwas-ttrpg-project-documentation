---
document:
  title: "Advisory Session Decision Report — S-3 Content, Encumbrance, Wound Precedence & S-2 Residuals"
  version: "1.0"
  status: "Advisory working document (not canonical) — requires human confirmation before any register entry"
provenance:
  author_llm: {name: "Grok", version: "Grok 4.5 (xAI)"}
  assessor_llm: []
  last_modified_by_llm: {name: "Grok", version: "Grok 4.5 (xAI)"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
---

# Advisory Session Decision Report
**Session Date:** 2026-09-02  
**Prepared for:** OpenCode (live repository documentarian)  
**Prepared by:** Grok 4.5 (xAI) — Lead Systems Architect & TTRPG Design Assistant  
**Authority class:** Non-canonical advisory record only. No decision in this document is Canonical. All entries require explicit human confirmation and formal register processing.

---

## 1. Purpose

This document records the designer rulings made by Tiwa during the 2026-09-02 advisory session. It is a handoff artifact for OpenCode.  

**OpenCode is required to present each ruling below as a confirmation question to Tiwa before any entry is written into `_consolidation/decision-register.md` or any other repository file.**

No promotion, demotion, or canonicalisation is authorised by this document.

---

## 2. Rulings Requiring Explicit Confirmation

### 2.1 P3 — Encumbrance Model

**Proposed Register Entry (provisional ID: DEC-078)**

| Field | Value |
|---|---|
| Subject | P3 — Encumbrance Model |
| Decision | Option A — Load Thresholds/Penalties (Numeric Mechanic) |
| Sub-rulings | See below |
| Status | Ruled (non-canonical) |
| Date | 2026-09-02 |

**Sub-ruling package:**

| ID | Question | Ruling |
|---|---|---|
| A1 | Capacity source | (1) Body attribute — bpe / bee (Endurance-coded) |
| A2 | Penalty application | Skill-side modifier only (DEC-063 / Invariant 6 compliant) |
| A3 | Movement Speed interaction | Untouched — no modification to locked `floor((bsp+bss)/15)` formula (DEC-004) |
| A4 | Condition creation | Yes — exceeding threshold imposes the Condition **Encumbered** |
| A5 | Resource model | Static thresholds + Skill-side penalty only. No secondary pool. |

**Hard dependency created:** Conditions subsystem (Proposals §10, currently Reserved).

**OpenCode confirmation question:**  
> Tiwa, do you confirm the complete P3 / DEC-078 package as stated above (Option A + all five sub-rulings A1–A5)?

---

### 2.2 OPEN-007 Residual — Quality × Skill-Tier Ceiling Precedence

**Proposed Register Entry (provisional ID: DEC-035.B)**

| Field | Value |
|---|---|
| Subject | Quality × Skill-Tier Ceiling Precedence (OPEN-007 residual) |
| Decision | Option A — Quality is the hard ceiling on wound tier |
| Rule text | Wound tier ≤ Quality-gated Effect tier (DEC-031). Skill-Tier functions only as a production gate (DEC-041: Skill-Tier ≥ 2 required). Skill-Tier does not raise or lower maximum wound magnitude once the Quality gate is satisfied. GM Fiat remains universal override. |
| Status | Ruled (non-canonical) |
| Date | 2026-09-02 |

**Consequence:** OPEN-007 magnitude architecture is closed. Accumulation-to-permanent-loss threshold remains GM-discretion (DEC-055 / DEC-070 precedent).

**OpenCode confirmation question:**  
> Tiwa, do you confirm DEC-035.B (Option A — Quality is the hard ceiling on wound tier; Skill-Tier is production gate only)?

---

### 2.3 5.1 S-3 Gated-Tier Effect Content Enumeration

**Proposed Register Entry (provisional ID: DEC-023.A)**

| Field | Value |
|---|---|
| Subject | S-3 Gated-Tier Effect Content Enumeration |
| Scope policy | Package 1 Option A — Full alpha enumeration |
| Status | Ruled (non-canonical) |
| Date | 2026-09-02 |

**Content policy rulings:**

| # | Decision Point | Ruling |
|---|---|---|
| 1 | Candidate lists | Accepted as first-pass alpha content |
| 2 | Ongoing / damage-over-time Effects | Prohibited. All HP loss remains Base-tier Inflict Injury only |
| 3 | Prone / Grappled / Restrained | Distinct mechanical identities |
| 4 | Action-economy Effects | Resolved as Skill-side penalty or Movement penalty, magnitude scaled by Effect Quality |
| 5 | Beneficial Effects | In scope. Effects may be positive or negative |

**Locked alpha content by tier** (accepted candidate set):

**Base Tier (unchanged)**  
- Inflict Injury (HP-only)  
- Open Retreat / Compel Yield  

**Position Tier**  
- Forced Movement  
- Knock Prone  
- Seize / Deny Ground  
- Pin / Hold Position  
- Open / Close Lane  

**Condition Tier**  
- Encumbered (DEC-078)  
- Grappled  
- Restrained  
- Prone  
- Blinded  
- Deafened  
- Frightened  
- Slowed (Skill-side or Movement penalty, Quality-scaled)  
- Stunned / Incapacitated (Skill-side or Movement penalty at high magnitude, Quality-scaled)  
- Fatigued (DEC-075 routing)  
- Sunder — Condition form (DEC-060 routing)  
- Poisoned / Sickened (Skill-side penalty only; no ongoing HP)  

**Equipment Tier** (Tag + Location + Skill-Tier ≥ 2 gating where applicable)  
- Disarm  
- Break / Sunder Item  
- Armor Bypass  
- Disable Device / Weapon  
- Steal / Take Item  

**Defense Tier**  
- Lower Defense  
- Deny Defense  
- Force Defense  
- Expose  

**Location Tier**  
- Impose Wound  
- Critical Location  
- Cripple Limb  

**Explicit prohibitions locked with this package:**  
- No damage-over-time / persistent damage Effects  
- No Advantage / Disadvantage language  
- No modification of the natural d100 roll  
- No new resource pools  
- One Effect per win remains in force (DEC-024)

**OpenCode confirmation question:**  
> Tiwa, do you confirm DEC-023.A in full (Package 1 Option A + the five content policy rulings + the accepted alpha Effect lists + the explicit prohibitions)?

---

## 3. Items Explicitly Not Ruled in This Session

| Item | Status |
|---|---|
| 5.3 S-2 Residual Architecture (R1–R4) | Still open. R1 (Promotion triggers) explained; no ruling made. |
| Exact capacity formula for Encumbrance (bpe/bee) | Open |
| Numeric threshold values and Skill-side modifier magnitudes for Encumbrance | Open |
| Exact Quality → penalty magnitude tables | Open |
| Conditions subsystem vocabulary | Still Reserved |
| Anatomical mapping numeric ranges (DEC-041 deferred) | Still open |
| Tier-2 formal rule text (DEC-042 residual) | Still open |

---

## 4. Required OpenCode Actions

1. Present each of the three confirmation questions in §2 to Tiwa.  
2. Record only those rulings that receive explicit affirmative confirmation.  
3. Assign final sequential DEC numbers according to the live decision register.  
4. Do not promote any of these rulings to Canonical.  
5. Flag the new hard dependency on the Conditions subsystem created by DEC-078 (Encumbered) and by all Condition-tier Effects in DEC-023.A.  
6. Preserve this report as a dated advisory session artifact; do not treat it as a standing merge file.

---

## 5. Provenance Statement

This document was authored solely by Grok 4.5 (xAI) during the 2026-09-02 advisory session. No independent assessor_llm pass has been performed. All content is non-canonical. Authority remains exclusively with the human designer (Tiwa) and the formal 8-step Promotion Rule.

---

**End of Report**