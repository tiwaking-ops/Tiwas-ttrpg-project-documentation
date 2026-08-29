---
document:
  title: "Consolidation Plan and Report"
  version: "1.0"
  status: "Consolidation-control record"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Consolidation Plan and Report

## What was consolidated

One supplied corpus file (`TTTRPG-merge-v1.md`), containing five embedded Tiwas TTRPG documents (D1–D5, see `document-inventory.md`), was mechanically split, verbatim-preserved in `sources/`, and reorganized into the target project structure. No sixth document, no prior repository, and no separate audit material was supplied — everything in this repository outside `sources/` and the wrapped copies in `canonical/`, `roadmap/`, `proposals/`, `investigations/` is newly written by this consolidation pass.

## What became canonical

Exactly one document: `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` (= D1), placed there because it **self-declares** "Canonical Source of Truth" status and that status is **corroborated**, not merely asserted — D2, D3, D4, and D5 all independently and consistently defer to it (see `relationship-map.md`, `conflict-register.md` item check). No content was added to, removed from, or reworded within D1. No item from D2/D3/D4/D5 was promoted to canonical status — in particular, the S-2 attack-side invocation policy and the S-2 non-attack deferral (both real designer rulings) remain in `proposals/` and `investigations/`, exactly where the source corpus itself places them, because none of them has completed the corpus's own 8-step Promotion Rule.

**This is the one placement in this consolidation you should explicitly confirm or override.** It is low-risk (unambiguous self-declaration, cross-corroborated, zero conflicting evidence found) but it is still, structurally, a canonicalization action, and the governing specification requires human review before canonical documentation is treated as settled — see "Human approval" in the specification and Phase 3/4 gates. If you disagree with this placement, say so and it can be moved to `_consolidation/proposed/` instead.

## What was archived

Nothing. `archive/` is empty. The corpus references several prior-version documents it supersedes, but none of that prior-version full text was supplied — there is nothing to move unchanged, and fabricating placeholder archived content would violate the prohibition on inventing material. See `archive/README.md` and `conflict-register.md` item C5.

## Major duplicates removed from active use

None found. Each of the five source documents covers distinct subject matter; no two documents in the corpus substantially duplicate each other's content (D4 and D5 cover related but explicitly distinct questions — D4 scopes out exactly what D5 later resolves, per `relationship-map.md`).

## Major conflicts discovered

Four recorded, three of them already resolved **within the corpus itself** (not resolved by this consolidation), one recorded as an open evidentiary gap:

- C1 — Structural Weak Points State 1→2 reclassification (resolved in-place, designer ruling).
- C2 — Armor Bypass basis wording overclaim (resolved in-place, wording correction only).
- C3 — Non-attack Location Index source, competing directions (resolved in-place, designer ruling: categorical deferral).
- C5 — Referenced prior-version documents not supplied in corpus (**unresolved**, evidentiary gap — see `archive/README.md`).

Full detail in `conflict-register.md`.

## Decisions relied upon

This consolidation relied on the corpus's own self-declared document-status headers (Canonical / Non-Canonical / Reserved / etc.) as primary evidence for structural placement, cross-checked against every explicit cross-reference between documents (see `relationship-map.md`). No decision was inferred that wasn't explicitly stated somewhere in the corpus. Full decision inventory in `decision-register.md`.

## Unresolved issues (left unresolved, as required)

- OPEN-001 through OPEN-005 in `decision-register.md` (H0 Rider B's sub-options; Tier-selection policy; anatomical mapping; Tier-2 procedure; all of S-3 through S-12).
- Conflict-register item C5 (missing prior-version source text).
- Whether the single canonical-placement decision above should stand as-is (flagged for your confirmation).

None of these were silently resolved. Where the corpus itself already resolved something (C1–C3), this consolidation recorded that resolution rather than re-litigating it.

## Newly created documents

`README.md`, `PROJECT_CONTEXT.md`, `governance/authority.md`, `governance/status-model.md`, `governance/provenance.md`, `audits/README.md`, `archive/README.md`, `canonical/systems/README.md`, `canonical/decisions/README.md`, `canonical/changelog/README.md`, and all seven `_consolidation/` files including this one. All carry the mandatory provenance metadata block.

## Modified canonical documents

None. D1 was placed into `canonical/rules/` with an external provenance header prepended; its substantive content was verified byte-identical to the source extraction (see the consolidation session's verification step). No wording inside the Canonical Rules document was altered.

## Archive coverage

N/A — nothing archived (see above).

## Known limitations

1. **Provenance of the five source documents is not established.** No author, LLM name, LLM version, or creation date could be recovered from the documents themselves. Recorded as `not established` throughout, per the prohibition on inventing provenance.
2. **The governing consolidation prompt is stored abbreviated**, not verbatim, in `prompts/` due to its length — see that file's own note and `SOURCE_CORPUS.md`.
3. **Prior-version documents referenced but not supplied** (Canonical v1.2, Roadmap v1.4.2's old sections, Proposals v1.4.1/v1.4.2's old §2, Investigation's pre-correction "uploaded v5," Non-Attack "Starter Brief v1.1") could not be archived or independently verified against the current documents' summaries of them.
4. **Single-model review.** Both `author_llm` and `assessor_llm` on every newly created document are the same model in the same session — a weaker review than an independent second pass. See `governance/provenance.md`.

## LLMs involved in this consolidation

Claude Sonnet 5 (`claude-sonnet-5`), single session, 2026-08-29. No other LLM is known to have contributed to this consolidation pass. (The five source documents' own authorship is separately "not established" — see above; nothing here implies they were also produced by this model.)

## Proposed actions not authorized (flagged, not performed)

- Splitting `canonical/rules/` into per-system files (recommended in `canonical/systems/README.md`) — not performed; recommendation only.
- Any archival of prior-version material — cannot be performed without the missing source text; flagged for a future session that has it.
- Independent (second-model) assessment of this consolidation's own output — recommended in `governance/provenance.md`, not performed here.
- Any Git commit or push — no Git repository is in use in this working environment; N/A, noted for completeness per the specification's Git-integrity checklist.

## Significant classification decisions

- D1 → Canonical (see "What became canonical" above; flagged for your confirmation).
- D2 → non-canonical implementation/process guidance, filed under a new top-level `roadmap/` folder (the target structure's `canonical/` / `proposals/` / `investigations/` categories did not fit D2's self-declared "no rule authority, but authoritative *process* guidance" status well; adding a sibling folder was judged truer to the evidence than forcing D2 into an ill-fitting category).
- D3 → `proposals/` (direct fit with self-declared status).
- D4, D5 → `investigations/` (direct fit with self-declared status).

## Significant repository actions

Directory structure created; five source documents extracted verbatim and copied into `sources/`; four of those five wrapped with external provenance headers and placed into `canonical/`, `roadmap/`, `proposals/`, and `investigations/` respectively (content verified unchanged); eleven new governance/index/consolidation documents authored.

## Human approval points

1. **Confirm or override the D1 → `canonical/` placement** (see above — this is the only placement judged to cross into canonicalization territory).
2. **Decide whether to pursue the missing prior-version documents** for `archive/`, or accept the current evidentiary gap (C5) as a permanent limitation of this repository's history.
3. **Decide whether a second model/session should independently assess** this consolidation before it is relied upon for further project work.

No other action in this repository requires approval before use — `roadmap/`, `proposals/`, and `investigations/` placements simply restate what those documents already say about themselves, and nothing was archived, deleted, or rewritten.

## Recommended future maintenance process

1. Any new locked mechanic goes through the 8-step Promotion Rule (`governance/status-model.md`) and is appended to `canonical/rules/...` §17's changelog, not written into a new file.
2. Any new non-canonical proposal or investigation is added to `proposals/` or `investigations/` respectively, with the same provenance-metadata discipline used here.
3. When prior-version source text becomes available, populate `archive/` per the process outlined in `archive/README.md`.
4. Future sessions should treat this repository — not prior conversational context — as the source of truth about project state, per the governing specification's "Repository as persistent project memory" principle.
