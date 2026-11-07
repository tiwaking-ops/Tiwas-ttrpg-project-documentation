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
