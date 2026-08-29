---
document:
  title: "Archive — Index"
  version: "1.0"
  status: "Governance pointer"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Archive

Empty. This is not an oversight — it reflects what the supplied corpus actually contains.

Every one of the five source documents references one or more **prior versions it supersedes** (Canonical Rules v1.2 and earlier "Core Rules"/standalone locked-subsystem docs; Roadmap v1.4.2's old Phase 2/§9 and old S-2 row; Proposals/WIP v1.4.1 and v1.4.2's old §2; the Investigation's pre-correction "uploaded v5"; the Non-Attack "Starter Brief v1.1"). **None of that prior-version full text was included in the supplied corpus** — only summaries of what changed, embedded in the current documents' own revision-record sections.

The archive preservation rule requires archived material to be preserved **unchanged**. There is nothing to move unchanged, because the originals were never supplied. Fabricating placeholder "archived" versions from the summaries would violate the prohibition on inventing content and would misrepresent guesses as historical record.

**As of 2026-08-29 (Priority 7), C5 was closed as a permanent limitation** — the human ruling accepted the missing prior-version text as an acknowledged, permanent gap, and recovery is **no longer required**. This folder therefore remains intentionally empty, and the gap is not treated as an unresolved recovery obligation.

**If a future designer ruling explicitly reverses that decision**, the then-available prior-version files (if any) should be:
1. added to `sources/` first (read-only evidence), then
2. moved into `archive/` with an external metadata wrapper recording their original title, version, and superseding relationship,
3. cross-referenced from `_consolidation/relationship-map.md` and `_consolidation/conflict-register.md` item C5.

Until such a reversal, `archive/` remains empty and `_consolidation/conflict-register.md` item C5 is recorded as an **accepted permanent limitation** (closed).
