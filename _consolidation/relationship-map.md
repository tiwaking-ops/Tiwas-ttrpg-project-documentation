---
document:
  title: "Relationship Map"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Phase 2 — Relationship Map

```text
                         D1  Canonical Rules & Changelog v1.3
                         (Canonical / Locked — top of authority hierarchy)
                                        │
                     ┌──────────────────┼──────────────────────┐
                     │ constrains        │ constrains            │ constrains
                     ▼                   ▼                       ▼
        D2  Implementation Roadmap   D3  Proposals/WIP        (any future
        & Project Governance v1.4.3  & Design Direction        Canonical
        "Rule Authority: None"       v1.4.3                     update)
        implements / sequences ──────▶ "Non-Canonical Design
        (must not contradict D1)       Repository"
                     ▲                        ▲   │
                     │ records/consumes        │   │ incorporates (per D3 §23
                     │ (§9 Phase 2, §4 S-2 row)│   │  v1.4.2 revision record:
                     │                         │   │  "Section 2 ... replaced
                     │                         │   │  with the S-2 Design
                     │                         │   │  Investigation v1–v5
                     │                         │   │  candidate ... policy")
                     │                         │   ▼
                     │                    D4  S-2 Design Investigation v5
                     │                    Synthesis (Correction Pass)
                     │                    "NON-CANONICAL ... S-2 remains
                     │                     unlocked"
                     │                         │
                     │                         │ explicitly scopes OUT
                     │                         │ (D4 §7: "does not resolve...
                     │                         │  whose roll... for a
                     │                         │  non-attack physical
                     │                         │  resolution")
                     │                         ▼
                     │                    (leaves a gap that D5 later closes —
                     │                     D4 and D5 are siblings, not
                     │                     parent/child; D5 does not modify D4)
                     │
                     │              D3 §2.5A  ◄──── authoritative non-canonical
                     │                                 location for the ruling
                     │                                 (per D3's own header)
                     │                    ▲
                     │                    │ recorded fully in
                     │                    │
                     └────────────────────┼──────────────────────────┐
                                           │                          │
                                    D5  S-2 Non-Attack Location        │
                                    Index Source — Closure Record      │
                                    v1.2 ("Final")                     │
                                    fullest record of the same ruling  │
                                    also recorded in D2 §9 ◄───────────┘
```

## Explicit relationship list

| From | To | Relationship type | Evidence |
|---|---|---|---|
| D2 | D1 | depends on / must not contradict | D2 §1 ("The Roadmap may explain... It may not independently decide... other unresolved designer decisions"), §2 (restates D1's locked invariants without alteration) |
| D3 | D1 | depends on / subordinate | D3 header ("Authority boundary... Where this document conflicts with the Canonical Rules... the Canonical Rules... prevail") |
| D3 §2 (as of v1.4.2, per its own revision record) | D4 | incorporates / summarizes | D3 §23: "Section 2 ... replaced with the S-2 Design Investigation v1–v5 candidate invocation/warrant policy... accepted as the current non-canonical working direction" |
| D4 | D1 §14 (Zero-Step) | builds on, does not modify | D4 header ("Not touched: Zero-Step derivation mechanics (Canonical §14.1–§14.2, locked, not reopened)") |
| D4 §7 | D5 | leaves open a question later closed by | D4 §7 explicitly declines to resolve "whose roll, if any, supplies the Location Index for a non-attack physical resolution," calling it "a distinct, narrower question for a future investigation" |
| D5 | D3 §2.5A | fuller record of the same designer ruling recorded more briefly in | D5 header: "Governing ruling recorded in: Proposals/WIP v1.4.3 §2.5A (authoritative non-canonical location)" |
| D5 | D2 §9 | fuller record of the same designer ruling, implementation consequences recorded in | D5 header: "Roadmap v1.4.3 §9 (implementation-relevant summary)"; D2 §9's own "Non-Attack..." subsection cross-references D3 §2.5A |
| D5 §3 | D3 §2.5A "Investigation record retained" table | duplicate/parallel record (same facts, same status per item) | Both tables list H0, Rider A, Rider B, GM-authored-stakes-rejected, Named-Outcome-transfer-deferred, blind-trial-not-run — content matches across both documents |
| D2 §4 (S-2 row), §12, §13, §15, §20 | D3 §2.5A / D5 | cross-references the non-attack deferral as an implementation consequence | D2 change note (top of document) and inline notes in §4, §5 (U-16), §9, §12, §13, §15, §20 |
| D3 §8 | D3 §2.5A / D5 | cross-references S-8 as the flagged most-likely reopening trigger, without narrowing S-8's own scope | D3 §8 "Note (v1.4.3)" |
| D3 §14 (Environmental Hazards) | D3 §2.5A | cross-references the deferral | D3 §14 "Note (v1.4.3)" |

## Non-relationships worth recording explicitly (to prevent future misreading)

- D4 does **not** supersede D1 §14 (Zero-Step) — it is additive/candidate material about a *different, still-open* half of S-2 (invocation policy), not a revision of the locked Tier-1 provider.
- D5 does **not** modify D4 — D5 closes a question D4 explicitly left open; D4's own content (the four-state model, Named-Outcome Test, etc.) is untouched and D5 says so explicitly (§6, "What This Investigation Explicitly Did Not Touch").
- D3's acceptance of D4's policy (DEC-017) does **not** promote it to Canonical — D3 §23 is explicit this is "not... a promotion to Canonical status."
- Neither D2 nor D3 nor D4 nor D5 claims to modify D1. No instance of an attempted or actual Canonical-Rules amendment by a non-canonical document was found anywhere in the corpus.

## Version-numbering note (recorded, not corrected)

D3's own header states: "Earlier minor-revision files in this series used a `1.4x` filename pattern by accident. Later files use the correct `x.y.z` format." This is preserved verbatim as the corpus's own account of its versioning history; this consolidation does not attempt to renumber or "fix" any prior version label.
