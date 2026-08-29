---
document:
  title: "Document Inventory"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  assessor_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  last_modified_by_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Phase 1 — Document Inventory

**Source corpus supplied:** a single merged file, `TTTRPG-merge-v1.md`, containing five distinct embedded documents concatenated under `## <filename>.md` headers with `​```markdown` fences. The merged file itself is preserved verbatim at `sources/SOURCE_CORPUS_ORIGINAL_TTTRPG-merge-v1.md`; each embedded document has additionally been extracted verbatim to its own file in `sources/` for individual traceability.

No other corpus material (no prior repository, no separate audit files, no chat history outside this session) was supplied. This inventory covers exactly these five documents — nothing more is assumed to exist.

---

## D1 — Tiwas Canonical Rules & Changelog

| Field | Value |
|---|---|
| Original title | Tiwas — Canonical Rules & Changelog |
| Filename in corpus | `Tiwas TTRPG — Canonical Rules & Changelog-v1-3.md` |
| Extracted to | `sources/tiwas-canonical-rules-and-changelog-v1.3.md` |
| Declared document version | v1.3 |
| Declared document status (self-stated) | "Canonical Source of Truth" |
| Declared role (self-stated) | "Authoritative statement of the current Tiwas ruleset" |
| Declared supersession | Supersedes Canonical Rules & Changelog v1.2 and previous standalone Core Rules / locked subsystem documents, for any material incorporated here (v1.2 text itself is **not** present in the corpus) |
| Author/provider | Not established (no LLM or human authorship metadata present in the document itself) |
| Author LLM name/version | Not established |
| Date | Not stated in-document |
| Subject | Core dice/resolution mechanics, attribute matrix, derived statistics, skills, Core Test Transaction, resource cost/overflow, recovery, Failure XP, Skill Roll Pool, General XP, Advanced Skills, S-1 (Opposed Contest — locked), S-2 §14 (Tier-1 Location Index provider only — limited lock), Reserved Systems list, Core Architectural Invariants, Changelog |
| Contains decisions | Yes — this document *is* the record of locked decisions (Core mechanics, S-1, and the limited S-2 Tier-1 provider) |
| Contains requirements | Yes — Core Architectural Invariants (§16) function as binding requirements on all future subsystems |
| Relationships | Top of the authority hierarchy per its own §0.1 and per Roadmap §1/§2 and Proposals' own "Authority boundary" note |
| Proposed destination | `canonical/rules/` |
| Archive requirement | None — this is the current, self-declared canonical document; no full prior version text was supplied to archive |

---

## D2 — Tiwas Implementation Roadmap & Project Governance

| Field | Value |
|---|---|
| Original title | Tiwas — Implementation Roadmap & Project Governance |
| Filename in corpus | `Tiwas___Implementation_Roadmap___Project_Governance-v1_4_3.md` |
| Extracted to | `sources/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` |
| Declared document version | v1.4.3 |
| Declared document status (self-stated) | "Authoritative Project/Implementation Guidance" |
| Declared rule authority (self-stated) | **"None — this document does not create game mechanics"** |
| Declared supersession | Supersedes Implementation Roadmap & Project Governance v1.4.2, but **only** Phase 2/§9 and the S-2 row of §4; all other content carried forward unchanged. v1.4.2 full text is **not** present in the corpus. |
| Author/provider | Not established |
| Author LLM name/version | Not established |
| Date | Not stated in-document (version-only) |
| Subject | Authority boundary vs. Canonical Rules, locked Core invariants (restated, not created), development priorities, residual decision roadmap (S-1…S-12), Universal Play subsystem map (U-01…U-22), dependency architecture, phased implementation plan (Phase 0–13), regression matrix, acceptance standard, project governance (status lifecycle, evidence classes), LLM governance rules, documentation maintenance rule |
| Contains decisions | No new game-mechanic decisions (explicitly disclaims rule authority); it **records** implementation-relevant consequences of decisions made elsewhere (Canonical Rules; Proposals/WIP designer rulings) |
| Contains requirements | Yes — extensive: acceptance criteria per phase, regression requirements, LLM governance rules (§24), documentation maintenance rules (§25) |
| Relationships | Depends on and must not contradict D1 (Canonical Rules); records/implements non-canonical decisions from D3 (Proposals/WIP), specifically the v1.4.3 S-2 non-attack deferral originating in D3 §2.5A / D5 (Closure Record) |
| Proposed destination | `roadmap/` (new top-level folder; content is explicitly non-canonical project/implementation guidance, not a "canonical system," and not a "proposal" or "investigation" either) |
| Archive requirement | Prior v1.4.2 content not archivable — full text not supplied. Note only. |

---

## D3 — Tiwas Proposals, WIP & Design Direction

| Field | Value |
|---|---|
| Original title | Tiwas — Proposals, WIP & Design Direction |
| Filename in corpus | `Tiwas___Proposals__WIP___Design_Direction-v1_4_3.md` |
| Extracted to | `sources/tiwas-proposals-wip-and-design-direction-v1.4.3.md` |
| Declared document version | v1.4.3 |
| Declared document status (self-stated) | "Non-Canonical Design Repository" |
| Declared authority (self-stated) | "Design exploration only" |
| Declared supersession | Supersedes Proposals, WIP & Design Direction v1.4.2, §2.5 only; all other content carried forward. v1.4.2 full text is **not** present in the corpus (only its revision record, §23, is preserved inside D3 itself). |
| Author/provider | Not established |
| Author LLM name/version | Not established |
| Date | Not stated in-document (version-only) |
| Subject | Current design direction; S-2 hit-location architecture (candidate invocation policy §2.1A, non-attack deferral ruling §2.5A); S-3 Outcome Effects; S-4 Two-Track Harm/Wounds; S-5 Armor; S-6 Defense; S-7 Incapacitation/Death; S-8 Difficulty/Stakes; S-9/S-10 Extended Tests; Conditions; Tags; Time/Action; Equipment; Hazards; Magic/Special Abilities; NPC Compression; Setting Modules; S-1D (explicitly experimental, excluded); Open Residual Decision Register; Promotion Rule (8-step); v1.4.1/v1.4.2/v1.4.3 revision records |
| Contains decisions | Yes — **non-canonical** designer rulings are recorded here (e.g., explicit-only objectives; Structural Weak Points State 2; the S-2 non-attack deferral itself, §2.5A) — these are real human/designer decisions per the document's own account, but they are decisions *about non-canonical candidate material*, not amendments to Canonical Rules |
| Contains requirements | Some (e.g., the 8-step Promotion Rule in §21 is a process requirement for any future canonicalization) |
| Relationships | Subordinate to D1; incorporates findings from D4 (Investigation v5 Synthesis) into its §2 per its own §23 revision record ("Section 2 ... replaced with the S-2 Design Investigation v1–v5 candidate ... policy"); §2.5A closely mirrors and cross-references D5 (Closure Record) |
| Proposed destination | `proposals/` |
| Archive requirement | Prior §2.5 "still open" wording (pre-v1.4.3) is superseded in place within this same document by its own account, not a separate file — nothing separate to archive. Prior v1.4.2 §2 content (pre-investigation Section 2 text) is referenced as historically significant by D3 §23 but its full original text is **not** present in the corpus — cannot be archived because it was not supplied. |

---

## D4 — Tiwas S-2 Design Investigation v5 — Non-Canonical Synthesis (Correction Pass)

| Field | Value |
|---|---|
| Original title | Tiwas S-2 Design Investigation v5 — Non-Canonical Synthesis (Correction Pass) |
| Filename in corpus | `Tiwas___S2_Hit_Location_Investigation_v5_Synthesis.md` |
| Extracted to | `sources/tiwas-s2-hit-location-investigation-v5-synthesis.md` |
| Declared document version | v5, "Correction pass" (unversioned beyond "v5"; internally makes 4 numbered corrections to "the uploaded v5 synthesis") |
| Declared document status (self-stated) | "S-2 Candidate Policy — Accepted by designer ruling for further development/testing. NON-CANONICAL." |
| Declared supersession | Supersedes an earlier "uploaded v5 synthesis" (pre-correction-pass); that earlier text is **not** present in the corpus, only its four corrections are described |
| Author/provider | Not established |
| Author LLM name/version | Not established |
| Date | Not stated in-document |
| Subject | Four-state classification model for S-2 Location-Index invocation (attack-side); Named-Outcome Test (21/21 trial); Conceptual Anchor Challenge table; procedural rules (compound objectives, stale objectives, S-1 winner-only, lazy evaluation, explicit-only objectives); GM-facing simplified procedure; W3 cache role and current cache contents; open scope gap (non-attack roll provenance, §7 — explicitly *not* resolved by this document); designer decision log (§8); acceptance tests; governance impact if approved |
| Contains decisions | Yes, several explicit "RULED" entries in §8 (evidence-labeled as designer rulings, non-canonical) |
| Contains requirements | Acceptance tests (§9) framed as implementation-relevant if the policy is adopted |
| Relationships | Feeds into D3 §2.1A (Proposals/WIP records this synthesis as the current non-canonical S-2 invocation policy per D3 §23's v1.4.2 revision record). Explicitly does **not** resolve the question later closed by D5 — D4 §7 explicitly scopes that question out ("This synthesis does not resolve ... that remains open") |
| Proposed destination | `investigations/` |
| Archive requirement | None — this is the current, most-corrected version of this synthesis; the pre-correction "uploaded v5" is referenced but not supplied, so nothing to archive |

---

## D5 — Tiwas S-2 Non-Attack Location Index Source — Closure Record v1.2

| Field | Value |
|---|---|
| Original title | Tiwas — S-2 Non-Attack Location Index Source — Closure Record |
| Filename in corpus | `Tiwas___S2_Non_Attack_Location_Source-CLOSURE_RECORD-v1_2.md` |
| Extracted to | `sources/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` |
| Declared document version | v1.2 ("Final — supersedes Starter Brief v1.1 as the status record for this investigation thread") |
| Declared document status (self-stated) | "Closure record for a completed non-canonical design investigation" |
| Declared supersession | Supersedes "Starter Brief v1.1" for this investigation thread; that starter brief's full text is **not** present in the corpus, only summarized in D5 §2's timeline table |
| Author/provider | Not established |
| Author LLM name/version | Not established |
| Date | Not stated in-document |
| Subject | Binding (non-canonical) designer ruling closing the "S-2 Non-Attack Location Index Source" investigation as a categorical deferral; full investigation timeline; what was resolved vs. what remains an inert candidate record (H0 and its riders); reopening conditions (tied to S-4/S-7/S-8); preserved stress-test scenario set; explicit scope exclusions; cross-document consistency table |
| Contains decisions | Yes — this document's entire purpose is to record one binding (non-canonical) designer ruling and its full evidentiary trail |
| Contains requirements | Reopening-condition requirements (§4): what must happen before this deferral may be revisited, and how |
| Relationships | This is the fullest record of the ruling that D3 §2.5A states more briefly and that D2 (Roadmap) §9 records as an implementation consequence. D5 §7 explicitly cross-references its own presence in all three documents (D3, D2, itself) as "kept synchronized" |
| Proposed destination | `investigations/` |
| Archive requirement | "Starter Brief v1.1" referenced but not supplied — cannot be archived |

---

## Cross-cutting inventory notes

1. **No conflicting-authority documents were found.** All five documents are internally consistent about where they sit in the authority hierarchy: D1 is canonical; D2, D3, D4, D5 all explicitly disclaim canonical/rule-making authority for themselves. This is unusually clean for a "disorganized corpus" — the self-declared status headers are treated here as strong evidence (not blind trust — see `conflict-register.md` and `decision-register.md` for the underlying reasoning), because they are corroborated by cross-references between the documents rather than resting on any single document's say-so.
2. **Several referenced prior-version documents were not supplied in the corpus**: Canonical Rules v1.2 (and original "v1" Core Rules / standalone locked subsystem docs), Roadmap v1.4.2 (Phase 2/§9 and old S-2 row only), Proposals/WIP v1.4.2 (old §2 text) and v1.4.1, the pre-correction "uploaded v5" Investigation synthesis, and the Non-Attack "Starter Brief v1.1". These are **referenced by title/version and by summarized content** inside the supplied documents, but their full original text was not part of this corpus. They therefore cannot be archived (there is nothing to move) and no claim is made here about their exact original wording. See `conflict-register.md` item C5.
3. **No audits, no separate decision log, no requirements spec, and no prior repository structure** were supplied. `audits/`, and most of `canonical/systems/` and `canonical/decisions/` therefore start empty or near-empty in this consolidation — see those folders' own README notes.

---

## Phase 1 gate — Inventory review (self-check)

- Major omissions: none identified — the corpus contains exactly five documents and all five are accounted for above.
- Material uncertainty: authorship/LLM-provenance of all five source documents is **not established** by the documents themselves; this is recorded rather than guessed, per the governing specification's prohibition on inventing provenance.
- Obvious classification errors: none identified on this pass.
- Corpus sufficiently mapped to continue: yes.

This inventory does not make any document canonical. Destination proposals above are Phase 1 provisional findings, refined further in `relationship-map.md` and finalized (subject to your review) in `consolidation-plan.md`.
