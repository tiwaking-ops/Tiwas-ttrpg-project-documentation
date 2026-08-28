---
document:
  title: "Conflict Register"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Phase 2 — Conflict Register

The corpus is unusually self-consistent (it appears to already be a governed documentation set, not raw disorganized material). Most "conflicts" found are **resolved-in-place** — i.e., the corpus itself records a correction or ruling that supersedes an earlier position, and both the earlier position and the resolution are visible in the same document. These are recorded below for traceability, distinguished from the one genuine **evidentiary gap** (C5) this consolidation cannot resolve.

## C1 — Structural Weak Points: State 1 vs. State 2

- **Conflicting statements:** D4's own §4/§6 table originally classified "Structural destruction" as State 1 (Established & Resolvable); D4's correction-pass header and D3 §23 both record this as reclassified to State 2 (Established, Not Yet Resolvable).
- **Documents containing them:** D4 (correction #4, and the corrected table itself), D3 §23 (second correction round).
- **Nature of conflict:** Classification conflict, fully explained as a **designer ruling, not a wording fix** — D4 is explicit that this "changes table behavior."
- **Relevant decision:** DEC-019.
- **Resolution:** Resolved in-place. The corpus does not present two live conflicting positions — it presents the correction and the corrected state, with the prior position preserved only as documented history within D4/D3's own revision-record sections. Both source documents (D3, D4) agree on the outcome (State 2, zero State-1 cache entries).
- **Status:** Resolved (non-canonical).

## C2 — Armor Bypass basis: "contradiction" vs. "silence with a stated preference"

- **Conflicting statements:** An earlier framing (referenced but not fully quoted) claimed Proposals §5 "directly contradicted" location-based Armor Bypass; the correction pass in D4 (and echoed in D3 §23) states this overclaimed — §5 favors Tags but never addresses location at all, which is silence, not contradiction.
- **Documents containing them:** D4 §4/§6 (correction #1), D3 §23.
- **Resolution:** Resolved in-place — the classification itself (Unanchored / State 3) is explicitly unchanged; only the stated basis/wording was corrected. No open question remains.
- **Status:** Resolved (non-canonical, wording-only).

## C3 — Non-attack Location Index source: two competing directions

- **Conflicting statements:** Direction 1 (GM-authored/stated hazard consequence treated as declaration-equivalent, enabling case-by-case Warrant transfer) vs. Direction 2 (default all non-attack cases to State 3/4 via the existing four-state model, which was itself withdrawn during cross-review as conflating "no player declaration" with "location-dependence unresolved") vs. the ruling actually adopted (categorical exclusion / deferral, independent of either direction).
- **Documents containing them:** D5 §2 (timeline), §3 (resolved-vs-inert table); D3 §2.5A investigation-record table.
- **Relevant decision:** DEC-020, DEC-021.
- **Resolution:** Resolved by explicit designer ruling — "Option 2" (categorical exclusion) per D5 §2's timeline row "Designer ruling." Direction 1 is recorded as rejected-not-deleted (DEC-021); Direction 2 was withdrawn pre-ruling by the investigators themselves, before the designer decision was even requested, and is explicitly distinguished from the final ruling in D5 §3's own notes ("Distinct from... the final ruling's categorical exclusion, which is a deferral by designer choice, not a four-state classification outcome").
- **Status:** Resolved (non-canonical), with reopening conditions attached (see DEC-020, D5 §4).

## C4 — Does the S-2 invocation policy narrow the Tier-selection question?

- **Apparent tension:** DEC-017 (the accepted candidate invocation policy) could be misread as implying Tier 1 is now the default/required granularity, since it defines *when* a Tier-1 index is warranted.
- **Documents containing the clarification:** D3 §2.5 (explicit: "does not determine whether a scene/campaign uses Tier 0, Tier 1, or Tier 2... That selection question remains unresolved and is not narrowed to 'Tier 2 only' by this policy" — note the source text says "Tier 2 only," which appears to be the source document's own wording choice, preserved verbatim rather than corrected here); D4's own architectural-constraint note at the top of §2; D2 §9 ("does not determine whether a scene or campaign uses Tier 0, Tier 1, or Tier 2").
- **Resolution:** Not a real conflict — every document that touches this question gives the same answer (Tier selection remains fully open). Recorded here only because a future LLM might otherwise infer narrowing from DEC-017's existence, which the corpus repeatedly and explicitly forecloses. See OPEN-002 in `decision-register.md`.
- **Status:** No conflict — clarified by repeated, consistent explicit statement (recorded verbatim in D3 §2.5; not independently re-verified as a possible transcription artifact of the source corpus).

## C5 — Referenced prior-version documents not present in corpus (evidentiary gap, not a content conflict)

- **What's missing:** Canonical Rules v1.2 and earlier "Core Rules"/standalone locked-subsystem documents; Roadmap v1.4.2 (old Phase 2/§9, old S-2 row of §4); Proposals/WIP v1.4.1 and v1.4.2 (old §2 text pre-investigation); Investigation D4's pre-correction "uploaded v5" synthesis; Non-Attack "Starter Brief v1.1" (D5's own predecessor).
- **Why this matters:** Every one of these is referenced as being superseded/corrected/replaced by the current documents, and the current documents summarize *what changed*, but this consolidation cannot independently verify those summaries against the original prior text, because that text was never supplied.
- **Resolution:** None possible from this corpus. This is recorded as an explicit evidentiary limitation, not resolved, not archived (nothing to archive), and not treated as if the missing documents' content is known. See `document-inventory.md` note 2 and `consolidation-plan.md` "Known limitations."
- **Status:** Unresolved — evidentiary gap, flagged for any future session that gains access to the missing prior-version files.

## Summary

No unresolved *substantive rules conflict* exists in the supplied corpus. The one standing item requiring future-session awareness is C5 (missing prior-version source text), which is an evidence gap rather than a contradiction between documents that were actually supplied.
