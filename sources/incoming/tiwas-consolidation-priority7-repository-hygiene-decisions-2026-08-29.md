---
document:
  title: "Tiwas — Consolidation Priority 7: Repository Hygiene Decisions"
  version: "1.0"
  status: "Non-canonical working record — for project documentarian (opencode)"
  audience: "opencode (GitHub Documentarian)"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
provenance:
  author: "Design Session 2026-08-29"
  prepared_by: "Grok 4.5 (Lead Systems Architect)"
---

# TIWAS — CONSOLIDATION PRIORITY 7  
## Repository Hygiene Decisions Report

**For:** opencode (GitHub Documentarian)  
**From:** Design Session 2026-08-29  
**Status:** Non-Canonical Working Record  

---

## 1. Purpose of this Report

This report records the two explicit human decisions that close the remaining human-approval gates identified under Priority 7 (Repository Hygiene) in `_consolidation/consolidation-plan.md`.  

It does **not** create, modify, or reopen any game mechanic. All actions are purely structural / governance.

---

## 2. Decisions Recorded

| Decision | Human Ruling | Effective Date | Effect |
|---|---|---|---|
| **C5 Evidence Gap** | Accept as **permanent limitation**; close C5 | 2026-08-29 | `archive/` remains empty; missing prior-version full text is not pursued; C5 status changes from “Unresolved — evidentiary gap” to “Accepted permanent limitation” |
| **Independent Second-Model Assessment** | **Required** before further reliance on the consolidated repository | 2026-08-29 | Consolidation output may not be treated as the authoritative baseline for subsequent design work until an independent second-model / second-session assessment has been completed and recorded |

---

## 3. Decision Detail — C5 (Prior-Version Documents)

### 3.1 Scope of Gap (unchanged)

| Missing Document | Referenced In | Nature of Reference |
|---|---|---|
| Canonical Rules v1.2 (and earlier Core / standalone locked-subsystem docs) | Current Canonical + changelog | Supersession / correction summaries |
| Roadmap v1.4.2 (Phase 2/§9, old S-2 row) | Current Roadmap | Revision history |
| Proposals/WIP v1.4.1 & v1.4.2 (old §2) | Current Proposals | Pre-investigation wording |
| Investigation “uploaded v5” (pre-correction) | D4 synthesis | Correction baseline |
| Non-Attack Starter Brief v1.1 | D5 | Predecessor |

### 3.2 Ruling Rationale (recorded)

- No locked rule, promotion path, or current resolution engine depends on the original wording of the superseded documents.
- The corpus already records the *outcomes* of the corrections (C1–C3 resolved in-place with designer rulings).
- Fabricating or reconstructing prior text is forbidden.
- Leaving the gap open indefinitely creates permanent housekeeping noise with no corresponding mechanical benefit.

### 3.3 Post-Ruling State

| Item | Pre-Ruling | Post-Ruling |
|---|---|---|
| `archive/` contents | Empty | Empty (permanent) |
| C5 status in conflict-register | Unresolved — evidentiary gap | **Accepted permanent limitation** |
| Recovery obligation | Open for future session | **Closed** — recovery not required |
| Impact on locked mechanics | None | None |

---

## 4. Decision Detail — Independent Second-Model Assessment

### 4.1 Current Limitation (unchanged)

Every newly authored document in the 2026-08-29 consolidation pass carries identical `author_llm` and `assessor_llm` (Claude Sonnet 5, same session). `governance/provenance.md` explicitly flags this as a weaker review form than an independent second pass.

### 4.2 Ruling

An independent second-model / second-session assessment **is required** before the consolidated repository may be treated as the authoritative baseline for further design work.

### 4.3 Minimum Scope of Required Assessment

1. Verify D1 → `canonical/` placement against the corpus’s own self-declaration + cross-references (the single canonicalization action).  
2. Confirm that no content was altered in any source document (byte-identity check).  
3. Confirm that C1–C3 resolutions were recorded, not re-litigated.  
4. Confirm that C5 and all OPEN items were left unresolved exactly as required (now updated: C5 closed as permanent limitation).  
5. Confirm directory classification of D2–D5 matches each document’s self-declared status.  
6. Flag any inference that was not explicitly supported by the source corpus.

### 4.4 Required Deliverable

Outcome of the second pass must be recorded as a new entry under `audits/` and must update (or append) the `assessor_llm` fields on the affected consolidation documents.

Until that audit record exists, the consolidation remains under a **provisional** governance status for reliance purposes.

---

## 5. Effect on Consolidation State

| Axis | Pre-Priority-7 | Post-Priority-7 |
|---|---|---|
| C5 Evidence Gap | Open | **Closed — accepted permanent limitation** |
| Second-model assessment gate | Recommended / optional | **Mandatory** (blocking further reliance) |
| Canonical-placement axis (Priority 5) | Confirmed | Confirmed (unaffected) |
| Mechanical rules / locked decisions | Unchanged | Unchanged |
| Archive population | Deferred | Permanently not required |

---

## 6. Files Relevant to this Record

| File Path | Role |
|---|---|
| `_consolidation/conflict-register.md` | Source of C5 definition; must be updated to reflect “Accepted permanent limitation” |
| `_consolidation/consolidation-plan.md` | Original human-approval points 2 and 3; source of Priority 7 |
| `archive/README.md` | States the empty-archive rationale; remains accurate under the permanent-gap ruling |
| `governance/provenance.md` | Records single-model limitation and recommends second-model pass |
| `_consolidation/document-inventory.md` | Lists the missing prior-version documents (note 2) |
| `audits/` | Target location for the required second-model assessment record |

---

## 7. Recommended Filing Actions for Documentarian

### Immediate

1. Update `_consolidation/conflict-register.md` item C5:
   - Change status from “Unresolved — evidentiary gap” to **“Accepted permanent limitation (2026-08-29)”**.
   - Add a short note that recovery is no longer required and that the gap is closed by designer decision.
2. Optionally append a revision block to `_consolidation/consolidation-plan.md` under “Human approval points” recording both Priority-7 rulings with date 2026-08-29.
3. Leave `archive/` empty. Do **not** create placeholder files.
4. Create (or reserve) an entry point under `audits/` for the forthcoming independent second-model assessment. Do not mark the consolidation as fully settled for reliance until that assessment is filed.

### Do not do

- Do **not** invent, reconstruct, or summarize prior-version text into `archive/`.
- Do **not** treat the consolidation as the authoritative baseline for new design work until the second-model assessment record exists in `audits/`.
- Do **not** alter any substantive text inside Canonical Rules, Proposals, Investigations, or Roadmap on the strength of these hygiene decisions.
- Do **not** reopen C1–C3 or any locked mechanic.

---

## 8. Governance Notes

- Both decisions satisfy the explicit human-review gates listed in `_consolidation/consolidation-plan.md` § Human approval points (items 2 and 3).
- The 8-step Promotion Rule (Proposals/WIP §21 / REQ-021) is **not** implicated; no new mechanic was locked.
- Future sessions must treat the C5 gap as closed and must not re-open an obligation to recover the missing prior-version files unless a new designer ruling explicitly reverses the permanent-limitation decision.
- The second-model assessment remains a hard gate on further reliance.

---

**End of Report**
