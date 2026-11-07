---
document:
  title: "Archive / Root Duplicates — Index"
  version: "1.0"
  status: "Archive index — deduplication holding area (advisory, non-canonical)"
provenance:
  author_llm: {name: "tencent", version: "hy4-preview-free"}
  assessor_llm: {}
  last_modified_by_llm: {name: "tencent", version: "hy4-preview-free"}
  created_date: "2026-11-08"
  last_modified_date: "2026-11-08"
---

# `archive/root-duplicates/` — Root-Level Duplicate Copies

**What this directory is.** Repository-maintenance holding area for files that were sitting at the repository root and were **byte-identical duplicates** of a copy already retained under another tracked directory. Directed by the human (Tiwa) 2026-11-08: "move to an archive directory".

**What it is not — distinction from the parent `archive/` directory.** `archive/README.md` records that `archive/` is intentionally empty as of 2026-08-29, because conflict-register item **C5** (missing prior-version full text) was closed as an **accepted permanent limitation**, and defines an archival process for *superseded prior versions* (add to `sources/` first, then move into `archive/` with an external metadata wrapper, cross-referenced from the relationship map and conflict register). The files here are **not** prior versions recovered under C5 and they are not superseded material: they are duplicate copies of documents that remain in place, unchanged, in their original locations. Nothing here reverses or affects C5, and C5 remains closed as recorded in `archive/README.md`.

**Effect of the move.** Content is unchanged (renames only; Git records them as `R`). No document was promoted, demoted, superseded, reclassified, or edited. Original root paths remain recoverable from Git history.

## Moved files (2026-11-08)

| File (SHA256 prefix) | Byte-identical counterpart retained at |
|---|---|
| `tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14 (1).md` (`3287C873…`) | `investigations/tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md` |
| `tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14 (2).md` (`3287C873…`) | `investigations/tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md` |
| `investigations-tiwas-your-first-adventure-playtest-execution-luna-2026-09-14.md` (`B8B63567…`) | `investigations/tiwas-your-first-adventure-playtest-execution-gpt-5.6-luna-v0.2-2026-09-14.md` |
| `tiwas-blood-man-location-template-proposal-2026-09-13.md` (`1A90E012…`) | `investigations/tiwas-blood-man-location-template-proposal-2026-09-13.md` |
| `tiwas-ice-troll-location-template-proposal-2026-09-13.md` (`8AA3408F…`) | `investigations/tiwas-ice-troll-location-template-proposal-2026-09-13.md` |
| `tiwas-combat-test-readiness-investigation-2026-09-04.md` (`24EB6A36…`) | `investigations/tiwas-combat-test-readiness-investigation-claude-2026-09-04.md` |

Note on the two Grok copies: they are byte-identical **to each other** as well as to the retained `investigations/` copy. The `(1)`/`(2)` suffixes were filesystem-level duplicate-download suffixes, not distinct versions.

## Known downstream references (unamended)

Two repository statements describe one of these files at its former root location:

- `investigations/tiwas-your-first-adventure-playtest-collation-cross-llm-comparison-2026-09-14.md` — §"R3 execution report" table row ("root copy retained (v0.1 run facts preserved)") and the pass note recording the `(1).md` attachment as byte-identical.

These records describe the **pre-move** state and were **not amended** by this maintenance pass; amending another document's substantive records is outside the authorisation for this pass. The documents themselves are unaffected in content, and their `investigations/` counterparts remain in place.

No Markdown link anywhere in the repository pointed at any of these six root paths (verified before the move), so no link was broken by it.

## Second batch — recovered S-1 files (2026-11-08)

A set of files recovered from an external chat share (supplied by the human: Tiwa) was delivered to the repository root on 2026-11-08. Duplicates in that delivery were moved here; files not already held anywhere in the repository were placed as intake evidence (read-only) in `sources/incoming/tiwas-tttrpg-merge/`.

**Duplicates moved here (2026-11-08):**

| File (SHA256 prefix) | Byte-identical counterpart retained at |
|---|---|
| `Tiwas_S1_Opposed_Contest_Candidates.md` (`723B5F09…`) | `sources/incoming/tiwas-tttrpg-merge/Tiwas_S1_Opposed_Contest_Candidates.md` |
| `Tiwas_S1_Correction_Verified_Hybrid.md` (`ADCFDAC6…`) | `sources/incoming/tiwas-tttrpg-merge/Tiwas_S1_Correction_Verified_Hybrid.md` |
| `Tiwas Reserved Subsystems — Comparative Design Direction Brief.md` | `sources/incoming/tiwas-tttrpg-merge/Tiwas Reserved Subsystems — Comparative Design Direction Brief.md` |

Note on the third row: the two copies are **line-ending variants of the same text** — 236 lines, identical content, existing copy LF-only (14,436 bytes), delivered copy CRLF (14,672 bytes). Not distinct versions; treated as a duplicate per the human's instruction. Git records them as the same blob once normalised.

**Not duplicates — placed as intake evidence** in `sources/incoming/tiwas-tttrpg-merge/` (same 2026-11-08 pass): `Tiwas_S1_Simulation.py`, `Tiwas_S1_Simulation_v2_Corrected.py`, `Tiwas_S1_Response_to_ChatGPT.md`, `chatgpt_to_claude_conv1.md`, `Tiwas_Opposed_Contest_GM_Guide.md`, `quality_vs_skill.png`, `quality_vs_skill_corrected.png`. The two PNGs are the figures referenced by `Tiwas_S1_Opposed_Contest_Candidates.md` (§"Fig. 1") and `Tiwas_S1_Correction_Verified_Hybrid.md`; placing them beside those documents resolves the last two broken local-link targets recorded in `audits/PROJECT-STATUS-REPORT-2026-10-26.md` finding F-3.

Placement here or in intake is **storage only**. It confers no status: none of these files is canonical, none is promoted, demoted, superseded, or reclassified by this pass, and no decision (DEC) is inferred from them.
