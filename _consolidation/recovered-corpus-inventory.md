---
document:
  title: "Recovered Corpus Inventory — Tiwas historical material staged from C:\\temp\\tttrpg-merge"
  version: "1.1"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm:
    name: "opencode"
    version: "big-pickle"
  assessor_llm:
    name: "not yet assessed"
    version: ""
  last_modified_by_llm:
    name: "opencode"
    version: "big-pickle"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-30"
---

# Recovered Corpus Inventory — `sources/incoming/tiwas-tttrpg-merge/`

## Purpose

This document inventories the **recovered historical Tiwas TTRPG material** that was
staged verbatim into `sources/incoming/tiwas-tttrpg-merge/` from the local directory
`C:\temp\tttrpg-merge`, per the OpenCode handoff report
(`opencode-handoff-report.md`) and the continuation-session decision log
(`session-decision-log-2026-08-29-part2.md`).

The original consolidation (`_consolidation/document-inventory.md`) covered the single
`TTTRPG-merge-v1.md` snapshot (5 embedded documents: Canonical Rules v1.3, Roadmap v1.4.3,
Proposals/WIP v1.4.3, S-2 v5 synthesis, S-2 Non-Attack Closure Record v1.2). That snapshot
was **incomplete** — it omitted the earlier versions and investigation rounds listed here.
This is the **inventory of the recovered, previously-missing corpus** (92 `.md` + 1 `.docx`
= 93 files). It is a separate working record held distinct from the original
`document-inventory.md` so the two phases do not blur.

## Provenance note (important)

**Original authorship of every recovered document is `not established`** from any in-file
metadata. The source files themselves do not carry reliable authorship fields, and per
`governance/provenance.md` and `AGENTS.md` authorship must not be inferred from filename,
formatting, tool-suffix (`-claude`, `-chatgpt`, etc.), or stylistic cues. The `-claude` /
`-chatgpt` / `-grok` / `-gemini` filename suffixes indicate **likely generation tooling of
the producing model** but are not recorded here as confirmed authorship. This inventory's own
provenance (author_llm = opencode) refers only to the inventory artifact itself, not to the
inventoried documents.

Nothing in this directory has been promoted to canonical, archived, or otherwise processed
beyond staging. All files remain byte-identical to their source in `C:\temp\tttrpg-merge`.

## 1. Staging summary

- **Source:** `C:\temp\tttrpg-merge` (flat, 91 `.md` files); plus 2 items recovered from the
  Windows Recycle Bin (see §1.1)
- **Destination:** `sources/incoming/tiwas-tttrpg-merge/` (93 files verbatim: 92 `.md` +
  1 `.docx`)
- **Byte-identity:** verified — all 91 original files copied with matching byte lengths;
  spot-check SHA256/binary comparison confirmed identical on Canonical Rules v1.1, v1.2,
  v1.3, and the S-2 Tier-1 Provider RULED record.
- **Status:** STAGED ONLY. Not yet archived, not yet written into any register, not yet
  assessed by the independent second-model review.

### 1.1 Recovered additions (Recycle Bin)

A missing-files audit (2026-08-29) recovered these items from the Recycle Bin. Four other
Recycle Bin items were **confirmed byte-identical duplicates** of already-staged files and
were therefore **not** added (per the owner's rule that deleted files are often duplicates):

`Tiwas___S2_Hit_Location_Investigation_v5_Synthesis_1.md` and `_2.md` — SHA256-identical to
staged `..._v5_Synthesis.md`; **not** re-added.
`Tiwas___S2_Next_Investigation-NonAttack_Location_Source-v1_1_1.md` and `v1_1_2.md` —
SHA256-identical to staged `...-v1_1.md`; **not** re-added.

Two genuinely-new items were recovered into staging:

- `Tiwas___S3_Effects_Round2_Effect_Identity-v1_4.md` — a later S-3 Round 2 version (staged
  set previously ended at v1_3); SHA256 differs from v1_3. Original location
  `C:\temp\tcindustries` (included per owner decision).
- `Tiwas_S2_Next_Design_Question_NonAttack_Location_Source_v1.docx` — the Word-format
  counterpart of `..._v1.md`; no byte comparison possible across formats.

Other Recycle Bin items were **not** recovered into staging: the `TTTRPG - ... v2.0/v2.1`
files (a *separate, failed* consolidation attempt per the owner — current work is v3), the
`%26`-encoded duplicate of Canonical Rules v1.3, the large PDF merge exports
(`tiwasttrpg-merge1.pdf` etc.), `Tiwas TTRPG - Canonical Rules %26 Changelog-v1-3.md` (a
duplicate of the staged v1.3), and all out-of-scope TCIndustries / non-Tiwas items.

## 2. Per-file inventory (grouped by document family)

Family counts: Canonical Rules 6 · Implementation Roadmap 13 · Proposals/WIP 14 · S-1
Opposed Contest 5 · S-2 Hit Location / Location Source 28 · S-2 Non-Attack / Closure /
Ruling 10 · S-3 Effects 10 · Synthesized Universe / Universal Roadmap 5 · Other 2.
**Total 93 (92 `.md`, 1 `.docx`).**

### 2.1 Canonical Rules (6)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas TTRPG — Canonical Rules & Changelog-v1-1-chatgpt.md | v1.1 | Canonical Source of Truth | First consolidated Canonical Rules + changelog | superseded by v1.2 |
| Tiwas TTRPG — Canonical Rules & Changelog-v1-2.md | v1.2 | Canonical Source of Truth | Canonical v1.2 | supersedes v1.1 |
| Tiwas TTRPG — Canonical Rules & Changelog-v1-3.md | v1.3 | Canonical Source of Truth | Canonical v1.3 | variants: rows 27, 88 in full list |
| Tiwas_TTRPG___Canonical_Rules___Changelog-v1-3.md | v1.3 | Canonical Source of Truth | v1.4.2-delivery variant | near-dup of the em-dash v1.3 |
| Tiwas_TTRPG___Canonical_Rules___Changelog-v1-3-claude.md | v1.3 | Canonical Source of Truth | claude export; §14.5 heading variant | near-dup of v1.3 |
| Tiwas_Core_Rules_v2.md | v2 | Supersedes v1; resolves ambiguities | Core Rules v2 (engine ambig. closed) | superseded by Canonical series |

### 2.2 Implementation Roadmap & Project Governance (13)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas — Implementation Roadmap & Project Governance-v1-1-chatgpt.md | v1.1 | Authoritative Guidance | Early roadmap | superseded by v1.2 |
| Tiwas — Implementation Roadmap & Project Governance-v1-2.md | v1.2 | Authoritative Guidance | Roadmap v1.2 | supersedes v1.1 |
| Tiwas — Implementation Roadmap & Project Governance-v1-3.md | v1.3 | Authoritative Guidance | Roadmap v1.3 | near-dup of v1-3-claude |
| Tiwas___Implementation_Roadmap___Project_Governance-v1-3-claude.md | v1.3 | Authoritative Guidance | claude export | near-dup of v1-3 |
| Tiwas___Implementation_Roadmap___Project_Governance-v1-4.md | v1.4 | Authoritative Guidance | Roadmap v1.4 | supersedes v1.3 |
| Tiwas — Implementation Roadmap & Project Governance-v1.4.1.md | v1.4.1 | Authoritative Guidance | current mainline (pre-v1.4.2) | near-dup (alt export) |
| Tiwas___Implementation_Roadmap___Project_Governance-v1_4_2.md | v1.4.2 | Authoritative Guidance | Phase 2 §9 + S-2 candidate policy | unique |
| Tiwas___Implementation_Roadmap___Project_Governance-v1_4_3.md | v1.4.3 | Authoritative Guidance | Non-Attack closure ruling | unique |
| Proposed_Update_Roadmap_Phase2_section.md | — | Proposed replacement text | §9 patch draft | near-dup of _1 |
| Proposed_Update_Roadmap_Phase2_section_1.md | — | Proposed replacement text | §9 patch refined | near-dup of base |
| Proposed_Update_Roadmap_Phase2_section_2.md | — | Proposed replacement text | pre-CORRECTED patch | dup lineage |
| Proposed_Update_Roadmap_Phase2_section_2_CORRECTED.md | — | Proposed replacement text | correction pass (§9) | identical to _1 |
| Proposed_Update_Roadmap_Phase2_section_2_CORRECTED_1.md | — | Proposed replacement text | same as CORRECTED | identical to CORRECTED |

### 2.3 Proposals / WIP & Design Direction (14)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas — Proposals, WIP & Design Direction-v1-1-chatgpt.md | v1.1 | Non-Canonical Design Repository | Early Proposals/WIP | superseded by v1.2 |
| Tiwas — Proposals, WIP & Design Direction-v1-2.md | v1.2 | Non-Canonical Design Repository | v1.2 | supersedes v1.1 |
| Tiwas — Proposals, WIP & Design Direction-v1-3.md | v1.3 | Non-Canonical Design Repository | v1.3 | near-dup of v1-3-claude |
| Tiwas___Proposals__WIP___Design_Direction-v1-3-claude.md | v1.3 | Non-Canonical Design Repository | claude export | near-dup of v1-3 |
| Tiwas___Proposals__WIP___Design_Direction-v1-4.md | v1.4 | Non-Canonical Design Repository | v1.4 | supersedes v1.3 |
| Tiwas — Proposals, WIP & Design Direction-v1.4.1.md | v1.4.1 | Non-Canonical Design Repository | current mainline | near-dup of v1.41 |
| Tiwas — Proposals, WIP & Design Direction-v1.41.md | v1.41 | Non-Canonical Design Repository | 1.4x filename accident, same content | near-dup of v1.4.1 |
| Tiwas___Proposals__WIP___Design_Direction-v1_4_2.md | v1.4.2 | Non-Canonical Design Repository | §2 S-2 candidate policy | supersedes v1.4.1 |
| Tiwas___Proposals__WIP___Design_Direction-v1_4_3.md | v1.4.3 | Non-Canonical Design Repository | §2.5A Non-Attack closure | supersedes v1.4.2 |
| Proposed_Update_ProposalsWIP_S2_section.md | — | Proposed replacement text | §2 draft patch | near-dup of _1 |
| Proposed_Update_ProposalsWIP_S2_section_1.md | — | Proposed replacement text | §2 refined | near-dup of base |
| Proposed_Update_ProposalsWIP_S2_section_2.md | — | Proposed replacement text | pre-CORRECTED patch | dup lineage |
| Proposed_Update_ProposalsWIP_S2_section_2_CORRECTED.md | — | Proposed replacement text | correction pass (§2) | identical to _1 |
| Proposed_Update_ProposalsWIP_S2_section_2_CORRECTED_1.md | — | Proposed replacement text | same as CORRECTED | identical to CORRECTED |

### 2.4 S-1 Opposed Contest (5)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas_S1_Opposed_Contest_Candidates.md | — | OPEN candidate comparison | Margin/Blackjack/Hybrid | unique |
| Tiwas_S1_Correction_Verified_Hybrid.md | — | Correction | hybrid formula verified | unique |
| Tiwas_S1_Validation_Pass_and_Acceptance.md | — | Validation & acceptance | S-1 acceptance rec. | unique |
| Tiwas_Opposed_Contest_Resolution_S1_v1.md | v1 | First canonical version | S-1 resolution v1 | superseded by v1.1 |
| Tiwas_Opposed_Contest_Resolution_S1_v1_1.md | v1.1 | Canonical / Locked | **LOCKED** S-1 resolution | supersedes v1 |

### 2.5 S-2 Hit Location / Location Source (28)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas_S2_Location_Granularity_Policy_Investigation_v1.md | v1 | Investigation (non-canonical) | granularity baseline | superseded |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v2_response_to_review.md | v2 | Investigation | review response | supersedes v1 |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v3_warrant_test.md | v3 | Investigation | W1–W4 warrant test | supersedes v2 |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v4_w3_cache_draft.md | v4 | Investigation | W3 cache draft | supersedes v3 |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v5_synthesis.md | v5 | Synthesis | consolidated recommendation | superseded |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v5_synthesis_1.md | v5 | Synthesis (accepted) | accepted candidate | supersedes base |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v5_synthesis_2.md | v5 | Synthesis (accepted) | + tier-selection clarity | identical to _3 |
| Tiwas_S2_Location_Granularity_Policy_Investigation_v5_synthesis_3.md | v5 | Synthesis (accepted) | same as _2 | identical to _2 |
| Tiwas_S2_Design_Investigation_v5_synthesis_CORRECTED.md | v5 | Synthesis (correction) | 3-fix correction | identical to _1 |
| Tiwas_S2_Design_Investigation_v5_synthesis_CORRECTED_1.md | v5 | Synthesis (correction) | same | identical to base |
| Tiwas_S2_Design_Investigation_v5_synthesis_CORRECTED_2.md | v5 | Synthesis (correction + State-2) | **State-2 ruling added** | identical to Hit_Location_v5 |
| Tiwas___S2_Hit_Location_Investigation_v5_Synthesis.md | v5 | Synthesis (correction) | latest v5 + State-2 | identical to CORRECTED_2 |
| Tiwas_Hit_Location_Default_Policy_S2_v1-claude.md | v1 | Draft, Not Locked | default policy first pass | superseded by v1.1 |
| Tiwas_Hit_Location_Default_Policy_S2_v1-1-claude.md | v1.1 | Draft, Not Locked | default policy revision | supersedes v1 |
| Tiwas_S2_Tier1_Provider_RULED_v1.md | v1.0 | **LOCKED** ruling | Zero-Step = Tier-1 provider | identical to v1-claude |
| Tiwas_S2_Tier1_Provider_RULED_v1-claude.md | v1.0 | **LOCKED** ruling | same | identical to v1 |
| Tiwas_S2_Documentation_Package_v1-1.md | v1.1 | Proposed package | E1–E9 evidence record | identical to _1, _1-claude |
| Tiwas_S2_Documentation_Package_v1-1_1.md | v1.1 | Proposed package | same | identical |
| Tiwas_S2_Documentation_Package_v1-1_1-claude.md | v1.1 | Proposed package | same | identical |
| Tiwas_S2_Proposed_Documentation_Package_v1-claude.md | v1.0 | Proposed package | earlier package | superseded by v1.1 |
| Tiwas_S2_Experiment_ChatGPT_Response_v1-claude.md | v1.0 | Response (no lock) | candidate-table experiment | unique |
| Tiwas S-2 Experiment — Analysis, Review & Recommendations-v1-chatgpt.md | v1.0 | Analysis & recommendations | ChatGPT experiment review | unique |
| Tiwas_S2_Response_to_ChatGPT_Round2_v1-claude.md | v1.0 | Response (r2) | review response | unique |
| Tiwas_S2_OrderSweep_Round3_v1-claude.md | v1.0 | Response (r3) | order-sweep results | unique |
| Tiwas_S2_Round4_Assessment_v1-claude.md | v1.0 | Response (r4) | verdict + advised actions | unique |
| Tiwas_S2_ZeroStep_Assessment_v1-1-chatgpt.md | v1.1 | ChatGPT assessment | Zero-Step determinism | unique |
| Tiwas_S2_Next_Design_Question_Tier_Policy_v1-claude.md | v1.0 | Starter Brief | Tier 0/1/2 brief | superseded by Location_Granularity v2 |
| Tiwas_S2_Next_Design_Question_Location_Granularity_v2.md | v2 | Starter Brief | granularity brief | supersedes Tier_Policy |

### 2.6 S-2 Non-Attack / Closure / Ruling (10)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas_S2_Next_Design_Question_NonAttack_Location_Resolution_v1.md | v1 | Starter Brief | resolution brief | superseded by v2 |
| Tiwas_S2_Next_Design_Question_NonAttack_Location_Resolution_v2.md | v2 | Starter Brief (Corrected) | Contact Branch / warrant | supersedes v1 |
| Tiwas_S2_NonAttack_Location_Resolution_Position_v1.md | v1 | Position paper | position | superseded by v2 |
| Tiwas_S2_NonAttack_Location_Resolution_Position_v2.md | v2 | Position paper | corrected position | supersedes v1 |
| Tiwas_S2_NonAttack_Location_Resolution_Starter_Brief_v1.md | v1 | Starter Brief | early brief | distinct (earlier) |
| Tiwas_S2_Next_Design_Question_NonAttack_Location_Source_v1.md | v1.0 | Starter Brief | source brief | superseded by v1.1 |
| Tiwas_S2_Next_Design_Question_NonAttack_Location_Source_v1_1.md | v1.1 | Starter Brief | corrected brief | identical to row 75 |
| Tiwas___S2_Next_Investigation-NonAttack_Location_Source-v1_1.md | v1.1 | Starter Brief | corrected brief | identical to v1_1 |
| Tiwas___S2_Non_Attack_Location_Source-CLOSURE_RECORD-v1_2.md | v1.2 | **Closure Record** | **binding (non-canonical) ruling** | supersedes Starter Brief v1.1 |
| Tiwas_S2_Next_Design_Question_NonAttack_Location_Source_v1.docx | v1.0 | Starter Brief (.docx) | source brief in Word format; recovered from Recycle Bin | Word-format counterpart of the `.md` v1.0 |

### 2.7 S-3 Effects (10)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas___S3_Effects_Round1_Candidate_Analysis-v1_0.md | v1.0 | Investigation (R1) | R1 baseline | superseded |
| Tiwas___S3_Effects_Round1_Candidate_Analysis-v1_1.md | v1.1 | Investigation (R1) | correction pass | supersedes v1.0 |
| Tiwas___S3_Effects_Round1_Candidate_Analysis-v1_2.md | v1.2 | Investigation (R1) | 2nd correction | supersedes v1.1 |
| Tiwas___S3_Effects_Round1_Candidate_Analysis-v1_3.md | v1.3 | Investigation (R1) | 3rd correction | near-dup of v1_3_1 |
| Tiwas___S3_Effects_Round1_Candidate_Analysis-v1_3_1.md | v1.3 | Investigation (R1) | same v1.3 | near-dup of v1_3 |
| Tiwas___S3_Effects_Round2_Effect_Identity-v1_0.md | v1.0 | Investigation (R2) | R2 baseline | superseded |
| Tiwas___S3_Effects_Round2_Effect_Identity-v1_1.md | v1.1 | Investigation (R2) | correction pass | supersedes v1.0 |
| Tiwas___S3_Effects_Round2_Effect_Identity-v1_2.md | v1.2 | Investigation (R2) | cleanup pass | supersedes v1.1 |
| Tiwas___S3_Effects_Round2_Effect_Identity-v1_3.md | v1.3 | Investigation (R2) | attribution correction | superseded by v1.4 |
| Tiwas___S3_Effects_Round2_Effect_Identity-v1_4.md | v1.4 | Investigation (R2) | later round; recovered from Recycle Bin | latest R2 |

### 2.8 Synthesized Universe / Universal Roadmap (5)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| Tiwas_Universal_System_Synthesized_Roadmap.md | — | Synthesized Roadmap | mechanical gap audit | unique |
| Tiwas Reserved Subsystems — Comparative Design Direction Brief.md | — | Comparative Design Direction Brief | Locked Identity + Priority | unique |
| TTTRPG-gem3-1-pro-syn1.md | — | Comparative synthesis | Gemini synthesis | unique |
| TTTRPG-grok4-5-syn1.md | — | Comparative synthesis | Grok synthesis | unique |
| perplexityai-tiwas_ttrpg-compare-existing1.md | — | Comparative analysis | Perplexity lean-toward | unique |

### 2.9 Other — external audit + original source (2)

| Filename | Version | Status | Subject | Duplicates |
|---|---|---|---|---|
| perplexityai-Phase One_ Reverse Engineering and Initial Audit.md | — | External audit | d100 engine audit | unique |
| Tiwas RPG Project Documentation.md | v1 | Original rules document | original v1 rules text | unique |

*Note:* the explore-agent extraction reported an S-2 `Tiwas_S2_Experiment_ChatGPT_Response_v1-claude_2.md` alt export not present in the original copy list; it is retained here as recorded during extraction and should be reconciled against the actual staged file set at the archive step.

## 3. Likely duplicate / alternate-export groups (global)

Threading the `_1/_2/_3`, `CORRECTED`, `-claude`, `-chatgpt`, and em-dash/underscore naming
variants, the following are alternate exports / same-version iterations of the same
underlying document (byte-identity confirmed where noted):

1. **Canonical Rules v1.3** — 3 files (em-dash `.md`, underscore `.md` v1.4.2-variant, `-claude`).
2. **Implementation Roadmap v1.3** — em-dash vs `-claude` twin.
3. **Proposals/WIP v1.3** — em-dash vs `-claude` twin.
4. **Proposals/WIP v1.4.1 vs v1.41** — identical content, version-label accident only.
5. **Proposed_Update_ProposalsWIP_S2_section** — 5-file patch set (`_2_CORRECTED` = `_2_CORRECTED_1`).
6. **Proposed_Update_Roadmap_Phase2_section** — 5-file patch set (mirror of 5).
7. **S-2 Design Investigation v5 CORRECTED** — `_CORRECTED` = `_CORRECTED_1`; `_CORRECTED_2` = `_Hit_Location_Investigation_v5_Synthesis`.
8. **S-2 Location Granularity v5 synthesis** — 5 files; `_2` = `_3`.
9. **S-2 Documentation Package v1.1** — 3 identical files.
10. **S-2 Tier1 Provider RULED** — 2 identical files.
11. **S-2 NonAttack Location Source v1.1 / Next Investigation** — 2 identical files.
12. **S-3 R1 v1.3 vs v1.3_1** — same version, minor header note.
13. **External synth trio** — overlapping cross-model analyses, not byte-identical.

## 4. Inferred version / chronology structure

- **Canonical Rules & Changelog:** v1.1 → v1.2 → v1.3 (current). Preceded by Core Rules v2
  and the original v1 rules document.
- **Implementation Roadmap:** v1.1 → v1.2 → v1.3 → v1.4 → v1.4.1 → v1.4.2 → v1.4.3 (current).
- **Proposals/WIP:** v1.1 → v1.2 → v1.3 → v1.4 → v1.4.1(=v1.41) → v1.4.2 → v1.4.3 (current).
- **S-1 Opposed Contest:** candidates (OPEN) → v1 → **v1.1 (LOCKED)**.
- **S-2 Hit Location / Location Source:** Tier-Policy brief → Location-Granularity paper,
  v1→v2→v3→v4→v5 synthesis (accepted) → **Tier-1 Provider RULED (LOCKED Zero-Step)**.
- **S-2 Non-Attack:** resolution briefs/positions → Source brief v1.0/v1.1 → **CLOSURE
  RECORD v1.2** (binding, non-canonical), mirrored into Roadmap/Proposals v1.4.3.
- **S-3 Effects:** Round 1 Candidate Analysis v1.0→v1.3; Round 2 Effect Identity v1.0→v1.3→
  **v1.4** (recovered; investigation only, no rulings yet — consistent with the rules needing
  the full promotion process).

## 5. Cross-cutting note

The inferred version ladders and self-declared status labels above are **read from the
documents' own headers**, not independently verified against each other. They are recorded
as the corpus's self-report for inventory purposes; per `AGENTS.md`, chronology and
self-labels do **not** establish authority. Verification, conflict-checking against the
in-repo material, and any promotion decisions remain separate, human-gated steps.

## 6. Status of this record

- **Non-canonical** consolidation working record.
- The staged files are **not** archived, not entered into `conflict-register.md` /
  `relationship-map.md` / `decision-register.md`, and **not** yet assessed by the
  independent second-model review. Those steps (handoff Steps 3–5 and the §5 review) are
  pending and will be performed only with the human operator's explicit go-ahead.

## 7. Claude-chat-derived files staged in `sources/incoming/` (2026-08-30)

Distinct from the `tiwas-tttrpg-merge/` corpus above (which was staged from
`C:\temp\tttrpg-merge`). These five files were staged **directly into `sources/incoming/`**
from a Claude chat export (Claude Exporter) and follow-on downloads of that export's
outputs. Byte-identity vs. the download originals was verified via SHA256.

### 7.1 Chat export (record of the conversation itself)

| Filename | Bytes | SHA256 | Subject |
|---|---|---|---|
| Claude-DONE S2 next design nonattack-20260830-0826.md | 54,289 | `32C4C52F…49F5B3` | Full export of the Claude chat "DONE S2 next design nonattack" (link `https://claude.ai/chat/819d984b…`), created 8/23/2026, exported 8/30/2026 08:26 |

### 7.2 Chat outputs (merged correction-pass files) — lineage note

These three files are the **final merged outputs of that chat** (chat line: "These three now
merge the best of both correction passes"). They were the files that were **previously
missing** from this project, and whose existence was evidenced only by the chat export
(`sources/incoming/` §7.1). They are **not duplicates** of the long-named CORRECTED variants
already staged in `sources/incoming/tiwas-tttrpg-merge/` (i.e.
`Tiwas_S2_Design_Investigation_v5_synthesis_CORRECTED[_1|_2].md`,
`Proposed_Update_ProposalsWIP_S2_section_2_CORRECTED[_1].md`,
`Proposed_Update_Roadmap_Phase2_section_2_CORRECTED[_1].md`). Git diff confirms each differs:
the short-named files carry the merged improvements (4-item correction preamble for v5 /
Proposals, §3-vs-§4 evidentiary contrast, propagated structural-mapping caveat, leaner rider
tagging; split two-bullet lazy-eval handling in Roadmap). The long-named variants are the
alternative pass, not the merged result.

| Filename | Bytes | SHA256 | Relationship to staged long-named variants |
|---|---|---|---|
| Tiwas_S2_v5_synthesis_CORRECTED.md | 20,464 | `FD5C4CD5…C6502B` | distinct — merged pass (short-named), differs from `Design_Investigation_v5_synthesis_CORRECTED.md` (21 diff lines) |
| Proposed_Update_ProposalsWIP_S2_CORRECTED.md | 10,748 | `A3E6727F…63A4A5` | distinct — merged pass, differs from `...ProposalsWIP_S2_section_2_CORRECTED.md` (17 diff lines) |
| Proposed_Update_Roadmap_Phase2_CORRECTED.md | 6,429 | `C9A1DD31…6006CC` | distinct — merged pass, differs from `...Roadmap_Phase2_section_2_CORRECTED.md` (6 diff lines) |

**Status scope:** all five files are non-canonical chat/LLM-produced material —
**investigation/working records only**. No promotion, no merge into live
Proposals/WIP or Roadmap documents was performed; the live v1.4.3 documents already
carry the superseding non-attack deferral ruling. Provenance per §2 header: original
authorship is `not established` (chat contents, not designer-authored documents).

### 7.3 Grok-derived files staged in `sources/incoming/` (2026-08-30)

Two further files were staged from a **shared Grok conversation** (title: "DONE ruled2
Designer Rules for Non-Attack Hazards", share link
`https://grok.com/share/c2hhcmQtMg_9cc88786-34db-407a-a501-44409131dfef`). The Grok share
page renders its content client-side, so a static fetch returns only the page shell; the
content was recovered via a headless-browser render of the share page and extraction from
the rendered DOM. The share contains exactly two messages: the user message (Starter Brief
v1.1 + Claude's "Designer Input Required" text) and Grok's reply — the **S-2 Non-Attack
Location Index Source — Architect Assessment**. The Architect Assessment was never saved as
a standalone file (it was copy-pasted between Grok and Claude directly); the standalone
file below is a **transcription** from the share, recorded as such, not an original file.

| Filename | Bytes | SHA256 | Subject |
|---|---|---|---|
| Grok-DONE ruled2 Designer Rules for Non-Attack Hazards-20260830-share.md | 8,907 | `EEBD4397…ED5AFFB` | Full transcription of the shared Grok conversation (2 messages: user paste + Grok's Architect Assessment reply) |
| S2-Non-Attack-Location-Index-Source-Architect-Assessment-grok.md | 5,555 | `2F3FB42C…56E459` | Standalone transcription of Grok's Architect Assessment reply (same reply as in the share transcript above); previously missing, evidenced only as a blank-name upload in chat |

**Status scope:** both files are non-canonical LLM-produced assessment/working material —
**source evidence only**, not a designer ruling. The live position on the S-2 Non-Attack
investigation remains the designer deferral ruling in Proposals/WIP v1.4.3 §2.5A.

### 7.4 ChatGPT-derived files staged in `sources/incoming/` (2026-08-30)

Two further files were staged from a **shared ChatGPT conversation** (title: "DONE Tiwas
Location Index Analysis", share link
`https://chatgpt.com/share/6a934e83-f1f0-83ec-8752-38c7fe566acb`). The ChatGPT share page
renders its content client-side, so a static fetch returns only the page shell; the content
was recovered via a headless-browser render of the share page (verifying UTF-8 byte-integrity
of the render before extraction) and extraction from the rendered DOM. The share contains
five messages: ChatGPT's critique of Claude's Round 1 (assistant), the user's paste of
Claude's "Round 1 Cross-Review Synthesis" (user), ChatGPT's agreement (assistant), the
user's paste of "I decided: Option 2 …" + Claude's "Designer Ruling Recorded" (user), and
ChatGPT's final agreement (assistant). The first assistant message — the **ChatGPT critique**
— was never saved as a standalone file; it entered the Claude chat as a blank-name
attachment evidenced only by the text "ChatGPT says:" in the Claude export. The standalone
file below is a **transcription** from the share, recorded as such, not an original file.

| Filename | Bytes | SHA256 | Subject |
|---|---|---|---|
| ChatGPT-DONE Tiwas Location Index Analysis-20260830-share.md | 28,268 | `96B6D641…871D339` | Full transcription of the shared ChatGPT conversation (5 messages: ChatGPT critique + 2 pasted Claude texts + 2 ChatGPT agreements); the user-side pasted Claude texts exist verbatim in the Claude chat export |
| S2-Non-Attack-Location-Index-Source-ChatGPT-critique.md | 8,230 | `A6D1FE22…682377BB` | Standalone transcription of ChatGPT's critique of Claude's Round 1 (first assistant message of the share); previously missing, evidenced only as a blank-name upload in the Claude chat |

**Status scope:** both files are non-canonical LLM-produced assessment/working material —
**source evidence only**, not a designer ruling. The live position on the S-2 Non-Attack
investigation remains the designer deferral ruling in Proposals/WIP v1.4.3 §2.5A.
