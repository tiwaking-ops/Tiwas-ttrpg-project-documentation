---
document:
  title: "Tiwas — L-004 Creature Location Templates: Open Per-Creature Questions — Advisory Session Report"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. Session report and recommendations only; not a ruling, not a register action. Nothing in this report is promoted, demoted, superseded, or resolved."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-20"
  last_modified_date: "2026-09-20"
  source_conversation: "Claude.ai Project session 'Tiwas-ttrpg', 2026-09-20 (three user turns: advice request; OpenCode plan pasted for review; report request)"
  primary_register: "decision-register.md (live register as supplied in the session; ceiling DEC-148)"
---

# Tiwas — L-004 Creature Location Templates: Open Per-Creature Questions — Advisory Session Report

**Author:** Claude Sonnet 5 — LLM name: `Claude Sonnet 5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-20
**Prepared for:** OpenCode (documentarian role) and Tiwa (sole ruling authority)
**Document class:** Advisory session report. Records findings, candidate recommendations, and unresolved items. Not a proposal for promotion, not a Decision Record.

---

## 0. Governance Statement

| Item | Statement |
|---|---|
| DEC assignment | None assigned or inferred. The next free number per the live register is DEC-149 (register ceiling DEC-148, verified in the supplied register). |
| Ruling authority | Tiwa (human) alone. Every recommendation below is advisory (LLM Governance Rules 4, 5, 6, 10). |
| Canonical impact | None. No Canonical Rules text is affected. |
| Promotion | Nothing promoted. REQ-021 (8-step Promotion Rule) not invoked. |
| Content authority | Creature template content is authored under DEC-077 / DEC-077.A: advisory models draft candidates only; Tiwa authors, accepts, edits, or rejects. |
| Provenance quality | Single-model authorship with no independent assessment. A weaker form of review than an independent second pass. It confers no authority (per `governance/provenance.md`). |

---

## 1. Purpose and Scope

Record the complete results of the 2026-09-20 advisory session on the open per-creature questions in the L-004 creature Location Template proposals (Giant Spider, Hobgoblin, Kobold, Troll, Dragon, Goblin, Orc), and on OpenCode's plan for getting those questions ruled.

| Turn | Content | Output |
|---|---|---|
| 1 | Tiwa asked for advice and recommendations on the open per-creature questions (examples given: Orc `size_medium`/`size_large`; Dragon size and armor-exclusion granularity); rulings await Tiwa | Advisory analysis (§4–§5) |
| 2 | Tiwa pasted OpenCode's plan for ruling the questions (family acceptance, three decision surfaces, "cheapest path", offer of a sign-off sheet) | Advisory review of the plan (§6) |
| 3 | Tiwa requested this report | This document |

---

## 2. Sources and Limitations

| Source | Use | Limitation |
|---|---|---|
| Decision register (`decision-register.md`, through DEC-148) | Verified closure status, cited DECs, register annotations on the L-004 proposals | Contains annotations *about* the proposals, not the proposals' own text |
| Canonical Rules v1.4, Proposals/WIP v1.4.3, Roadmap v1.4.3, Alpha Playtest Corpus (2026-09-08) | Governance, status vocabulary, invariants | Superseded in detail by the live register |
| OpenCode message (pasted by Tiwa) | Question IDs, draft sign-off structure, prerequisites | Reported by OpenCode; not independently verified except where noted in §3 |

**Limitations that bear on every recommendation:**

1. The proposals' own §6 question text was **not supplied**. Items known only from register annotations are marked "unseen detail".
2. OpenCode's Q-IDs (GO-, OR-, DR-, GS-, KB-, HG-, TR-, IT-, BM-, ACC) were **not verifiable** against the proposals. Recommendations were mapped onto them from register descriptions.
3. The Dragon "exception-carving" armor registration was read from the register annotation ("Foreback not Torso; Throat, Face, Wing-Membrane, Underbelly excluded"). That it is *literally* a positive registration at a deeper node is an interpretation and needs checking against the proposal text.

---

## 3. Verification Results (Register Cross-Check)

| Claim | Source | Result |
|---|---|---|
| Register ceiling is DEC-148; next free DEC-149 | OpenCode | **Verified** (DEC-147 and DEC-148 are the last rows) |
| Draft batch-acceptance number was consumed by the Grappled-movement ruling | OpenCode | **Consistent**: DEC-143 in the register is the non-escape Grappled movement ruling |
| DEC-144 ruled T1 (body-plan classification) | OpenCode | **Verified** (DEC-144, 2026-09-18) |
| Draft batch acceptance file never signed | OpenCode | **Not verifiable** from supplied documents |
| Ice Troll and Blood Man proposals exist only in git HEAD | OpenCode | **Not verified.** The register annotates both as stored 2026-09-13; treat as a possible discrepancy for OpenCode to check |
| "Nine proposals" | OpenCode | **Partly reconciled.** The register refers to a "ten-instance family" and a "ten stored L-004 proposals". The difference from nine is presumably the Human proposal (adopted separately as DEC-137). **Inference, not verified.** |
| Q-ID list (ACC, TR-Q2, OR-Q2, DR-Q2/Q3, GS-Q3, KB-Q2, HG-Q1, IT-Q2, BM-Q2/Q4 etc.) | OpenCode | **Not verifiable**; used as given |

---

## 4. Findings: Current State of the L-004 Questions

### 4.1 Already closed (should not be re-ruled)

| Item | Closed by | Effect on the open queue |
|---|---|---|
| Tier-1 reuse vs bespoke (the T1 fork) | DEC-144 (2026-09-18): bipedal-humanoid reuses DEC-100 quartiles; every other body-plan class is bespoke by default | Giant Spider (multi-limbed/segmented), Dragon (quadrupedal), Blood Man (amorphous) stay bespoke. Goblin, Orc, Hobgoblin, Kobold, Troll keep DEC-100. |
| Terminal-leaf saturation | DEC-137 fork (1); DEC-139 | Not an open question in any template |
| Full-depth resolution of a qualifying Tier-2 Effect | DEC-139 | Not open |
| Secondary roll | DEC-136 R1 (removed for all Effects) | Not open |
| Human v1 template and 100-state allocation | DEC-137 | Human comparison numbers now have an adopted reference |

### 4.2 Gap identified

DEC-144 rules **Tier-1 zone boundaries only**. No register entry found addresses whether Tier-2+ intra-zone allocations may be copied or adapted from Human v1 for other bipedal humanoids. DEC-137 states other creature templates "remain content-authoring". Candidate cross-cutting rule C1 (§5) proposes how to fill this gap; alternatively Tiwa may extend DEC-144's copy-permission to Tier-2+.

### 4.3 Stale comparison data in proposals

Several proposals were authored against the pre-adoption Human candidate. Register-recorded mismatches with the adopted DEC-137 allocation:

| Statement in proposals | Adopted DEC-137 value |
|---|---|
| Thigh width 13 | Thigh 1–5 (width 5) |
| Skull width 13 | Skull 76–91 (width 16) |
| Five internal organs | Six (Heart, Lungs, Stomach, Liver, Intestines, Kidneys) |
| Heart width 1 (vital-target convention "Narrow") | Heart 30–31 (width 2) |

The templates themselves are internally consistent (all trees sum to 100 per the register). Only the Human-comparative prose is stale.

---

## 5. Advisory Recommendations (Turn 1)

All entries are candidates. None is a ruling.

### 5.1 Cross-cutting candidate rulings

| ID | Candidate ruling | Rationale (register anchor) | Would settle |
|---|---|---|---|
| C1 | **Humanoid delta convention.** A bipedal-humanoid template derives from Human v1. Permitted deltas: reallocate widths within a Tier-1 zone; add or remove named nodes. Invariants: Tier-1 zone totals stay 25 each; total 100; every state assigned to a named node (no reserves, DEC-137 fork 7). | DEC-041(5), DEC-100, DEC-137, DEC-144. Converts proportion questions into pass/fail checks. | Goblin pot-belly, 4-wide Ears, dropped Kidney; Orc 16/9 chest split, no Ears; Kobold minor features |
| C2 | **Armor registration is a positive list.** Register `defense:armor` on covered nodes; a parent covers its children (L-007/L-012). No "except" grammar. | An exception grammar would contradict L-007's literal parent-covers-children text and need its own amendment. | Dragon armor-exclusion granularity; Troll and Ice Troll armor placement |
| C3 | **Size tags are descriptive.** Choose for monotone scale ordering; add no new size vocabulary until a mechanic consumes one. | No ruled consumer of `creature:size_*` found in the register; DEC-116 makes Tags vocabulary-only by default; new tags need a DEC-080 T1 ruling. | Orc size; Dragon `size_huge`/`size_gargantuan` |
| C4 | **Paired-leaf authoring rule.** Allocate paired structures an even number (≥2) of consecutive states so parity reaches both sides; a single-state paired leaf only deliberately. | DEC-137 content convention: a single-state paired leaf fixes its side; the sibling is reachable only via GM Fiat. | Giant Spider eight legs; Kobold; Goblin toes |
| C5 | **Re-derive every Human comparison from the adopted DEC-137 table.** | See §4.3. | All proposals |

**Assumption flagged:** the proposed size ordering (Goblin/Kobold small < Hobgoblin/Orc medium < Troll large) is this session's proposal. The register records only Goblin/Orc-level `size_small`/`size_medium` usage and Dragon's provisional `size_large`; Hobgoblin and Kobold sizes are not recorded.

### 5.2 Per-creature recommendations

| Creature | Open question | Recommendation | Confidence |
|---|---|---|---|
| Goblin | Pot-belly reversal (Abdomen > Chest) | Accept; pure exposure shift, no rule conflict under C1 | High |
| Goblin | Ears node 4 wide | Accept; Head stays at 25 with width taken from other Head nodes | High |
| Goblin | Kidney dropped | Accept only if freed states go to a named node (DEC-137 fork 7); otherwise restore | Medium |
| Orc | `size_medium` vs `size_large` | `size_medium` (C3, scale ordering) | Medium |
| Orc | 16/9 chest split | Accept if extra chest states go to Heart/Lungs, not padding; this widens chest exposure by a deliberate amount | Medium |
| Orc | No Ears node | Rule one Ears convention across humanoid templates (Goblin keeps a node, Orc folds it) | Medium |
| Hobgoblin | Interpolation between Goblin and Orc | Author explicitly with each node width between Goblin's and Orc's (inclusive) and sum 100; checkable, no formula | Medium |
| Kobold | Minor-feature reuse | Reuse where no distinct anatomy exists; apply C4 to paired minors | Medium (unseen detail) |
| Troll | Ice Troll derivation | Accept; the register's spot-check found the derivation sound (frost/DEC-088-tied items subtracted; troll-generic features retained) | High |
| Troll | Regeneration | Keep off the location template (DEC-110 content; DEC-088 gate); no template change | High |
| Troll | Armor Tag | Author none until a stat block needs one; if so use C2. Unregistered Head means Armor Bypass on Head hits falls back per DEC-030 (harmless if intended) | Medium |
| Dragon | Underbelly width | Content decision; keep Torso zone at 40 with every state named | n/a (unseen number) |
| Dragon | Size tag | Keep provisional `size_large`; defer `size_huge` (C3) | High |
| Dragon | Armor-exclusion granularity as a pattern | Positive list (C2); do not generalize an exception grammar | High |
| Dragon | Unarmored Jaws | Keep; Armor Bypass falls back per DEC-030, giving a designed weak point with no rule side effects | Medium |
| Giant Spider | Eight-leg laterality | Confirm branch × parity (consistent with L-008); apply C4 to each leg leaf | Medium |

### 5.3 Suggested ruling order (Turn 1)

1. C1, C2, C5.
2. C3, then C4 as an authoring guideline.
3. Goblin, Orc, then Hobgoblin (Hobgoblin depends on the other two).
4. Troll, Kobold, Dragon, Giant Spider content items.
5. Optional: extend DEC-144's copy-permission to Tier-2+ allocations if C1 is not adopted.

---

## 6. Review of OpenCode's Ruling Plan (Turn 2)

### 6.1 OpenCode's plan (as reported)

| Element | Content |
|---|---|
| Decision surface 1 | Family acceptance (ACC ×9): accept as-authored working playtest content per DEC-137 precedent (options: as-authored / conditions-binding / subset / as-edited / reject); Ice Troll and Blood Man carry the same acceptance question plus IT-Q2, BM-Q2, BM-Q4 |
| Decision surface 2 | Combat-mechanical knobs: TR-Q2 (Reading A vs direct DEC-088 amendment; the only item touching ruled text), OR-Q2, DR-Q2, DR-Q3, GS-Q3, KB-Q2, HG-Q1 |
| Decision surface 3 | Cosmetic questions (GO-Q2/3/4, OR-Q3/4, DR-Q1/4, KB-Q3/4, HG-Q3/4, GS-Q4) |
| Form | Valid only when Tiwa signs and it is recorded in the decision register as a non-canonical designer ruling (DEC-137 precedent); Ice Troll and Blood Man files must be restored to `investigations/` first; fresh numbering DEC-149+ |
| Cheapest path | "Accept all nine, conditions binding" + confirm DR-Q3 + the two flagged confirmations (Orc `size_medium`, Dragon provisional `size_large` and armor granularity); OpenCode offered a consolidated sign-off sheet |

### 6.2 Verdict and recommended defaults

**Verdict:** take the cheapest path and ask OpenCode to draft the sign-off sheet with the §6.4 amendments. Family acceptance also removes the ordering dependency in §5.3 step 3.

| Q-ID | Recommended default | Confidence | Note |
|---|---|---|---|
| ACC ×9 (P0) | Accept all nine as working playtest content, conditions binding (DEC-137 precedent) | High | All trees sum to 100 (register-verified); no conflict with Canonical rules found |
| TR-Q2 | Reading A: DEC-088 untouched, plus a playtest watch-item | Medium (unseen text) | Avoids amending ruled text; fits the simplification trajectory (DEC-136/138/141/142) |
| OR-Q2 | `size_medium` | Medium | Tags descriptive only (DEC-116) |
| DR-Q2 | Keep provisional `size_large` | High | New tag needs a DEC-080 T1 ruling |
| DR-Q3 | Confirm the pattern, worded as positive registration | High | Frames the whole armor cluster |
| GS-Q3 | Prefer the two-registration model | Low | Six-registration only if per-leg exposure matters; text not seen |
| KB-Q2 | No innate Tag | Low–Medium | Consistent with Troll and Blood Man; a Tag can be added at stat-block time |
| HG-Q1 (framework) | Split (OpenCode's recommendation) | Medium | Check the split satisfies the width-between-Goblin-and-Orc constraint (§5.2) |
| Cosmetic set | Accept as authored | High | Non-blocking |

### 6.3 Cautions

| Issue | Advice |
|---|---|
| "Exception-carving" wording (DR-Q3) | Register armor on nodes covered; to exclude Throat or Face, register sibling nodes directly. Do not rule an "except" grammar (contradicts L-007's literal text). |
| Stale Human comparisons | Add a binding condition that Human-comparative statements are non-normative and must be re-derived from DEC-137 before reuse. |
| HG-Q1 "split" | Content of OpenCode's split policy is unknown to this session; verify per-node widths lie between Goblin's and Orc's, inclusive, summing to 100. |
| Single-state paired leaves | Add a condition that each is deliberate (DEC-137 convention). |
| Ice Troll and Blood Man | Rule in the same pass. For IT-Q2 use the positive-registration principle. For BM-Q2 prefer relabelling parity ("Pseudopod A/B") over suppressing laterality: suppression collapses the two parity buckets and changes same-tier same-location stacking under DEC-035.A cl.4. Restore both files from git HEAD first, as OpenCode states. |

### 6.4 Requested amendments to the sign-off sheet

| # | Request |
|---|---|
| 1 | One DEC with R-sub-rulings (DEC-114 / DEC-146 shape), or two (acceptance, then knobs); avoid one DEC per creature |
| 2 | Number from DEC-149 |
| 3 | Layout: P0 acceptance block; then combat-mechanical knobs (flagged register-adjacent or not); then cosmetic knobs as a single "accept as authored" checkbox |
| 4 | Per row: Q-ID, options, recommended default, confidence, ruled text touched |
| 5 | Binding conditions: stale-Human-comparison note; deliberate single-state paired leaves; DEC-144 cited, not re-ruled |
| 6 | Boilerplate: non-canonical designer ruling, no promotion (REQ-021), content authored under DEC-077/077.A, advisory drafters do not rule |

---

## 7. Decisions Made in This Session

**None.** No designer ruling was given in this session. All decisions listed in §5–§6 remain awaiting Tiwa. This report assigns no DEC and infers none.

---

## 8. Unresolved Issues and Open Items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Family acceptance (ACC ×9) and its conditions | Tiwa | Awaiting ruling |
| 2 | TR-Q2: Reading A vs DEC-088 amendment (only item touching ruled text) | Tiwa | Awaiting ruling |
| 3 | DR-Q3 armor-exclusion pattern (recommended: positive registration) | Tiwa | Awaiting ruling |
| 4 | Size tags: OR-Q2 (`size_medium`/`size_large`), DR-Q2 (provisional `size_large` vs `size_huge`/`size_gargantuan`, which would need a DEC-080 T1 ruling) | Tiwa | Awaiting ruling |
| 5 | GS-Q3 (six vs two registrations); KB-Q2 (Tag vs Torso-only fallback); HG-Q1 (authoring policy) | Tiwa | Awaiting ruling |
| 6 | Cosmetic knobs (GO-, OR-Q3/4, DR-Q1/4, KB-Q3/4, HG-Q3/4, GS-Q4) | Tiwa | Awaiting; non-blocking |
| 7 | Ice Troll and Blood Man in the same pass (IT-Q2, BM-Q2, BM-Q4); register already notes IT-Q3 is a forward-looking adoption decision, not a retroactive repair | Tiwa | Awaiting decision whether to include |
| 8 | Tier-2+ copy-permission gap (DEC-144 covers Tier-1 only) | Tiwa | Unruled; C1 offered as one route |
| 9 | Restore Ice Troll and Blood Man proposals to `investigations/`; reconcile with register annotations that record them as stored | OpenCode | Unverified state; check |
| 10 | Whether the unsigned draft batch-acceptance file is retired or superseded by the new sign-off sheet | OpenCode / Tiwa | Unverified |
| 11 | Reconcile "nine" (OpenCode) vs "ten-instance family" (register) | OpenCode | Inference only (Human proposal presumed to be the tenth) |
| 12 | Proposals' §6 text not seen by this session; every "unseen detail" row and the Dragon exception-carving reading need checking | Claude / OpenCode | Pending; offered on receipt of §6 text |

---

## 9. Requested OpenCode Actions (Advisory Requests, Not Directives)

1. Store this report as an advisory / non-canonical investigation artifact in `investigations/`. Do not infer or assign a DEC.
2. Optionally add an advisory storage annotation to the register on the DEC-112 / DEC-144 L-004 lineage (HC-1.4 and prior storage-record precedent), stating that storage confers no authority.
3. Draft the consolidated sign-off sheet per §6.4, numbered from DEC-149, for Tiwa's review. Send the DR-Q3 and TR-Q2 wording to this session for a register cross-check before signing (offered by Claude).
4. Do not record any ruling in the register until Tiwa signs.
5. Report the §8 items 9–11 verification outcomes back to Tiwa.

---

## 10. Provenance Note

Authored by Claude Sonnet 5 (`claude-sonnet-5`) in a single pass; no independent assessment. Recommendations in §5–§6 were produced within the session and are candidate advice. Register citations were checked against the live register text supplied in the session; OpenCode-sourced statements not confirmable from supplied documents are labeled as such in §3. Storage and assessment of this report confer no authority.

---

**End of document.**

**Author:** Claude Sonnet 5 — LLM name: `Claude Sonnet 5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-20
**Classification:** Advisory session report — no DEC assigned; non-canonical.
