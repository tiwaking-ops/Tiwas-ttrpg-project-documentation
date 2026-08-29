# AGENTS.md — Tiwas TTRPG Project Documentation Repository

## Purpose and boundary

`AGENTS.md` is an agent operating-control document. It defines **how agents
must behave** when working within this repository. It does **not** establish the
canonical status of game mechanics, design propositions, historical claims, or
other project content.

This document is **not** a canonical game-design document and **not** a second
copy of the repository's governance/authority model. It must not be used as
evidence that a mechanic or design proposition is canonical, and it must not
bypass the existing formal authority/promotion process.

## Consulting the authority model

Determine documentary status from the **repository's established
governance/authority model**, not from this document. `AGENTS.md` defines how
the agent must behave when using that model.

Before making any authority-dependent claim or modification, consult the
repository's existing governance/authority material as relevant, including:

- `governance/authority.md`
- `governance/status-model.md`
- `governance/provenance.md`
- the records in `_consolidation/` (decision register, conflict register,
  relationship map, requirement register)

Do not independently reclassify repository documents, and do not redefine which
documents are canonical. Preserve the existing distinctions (canonical,
proposal, investigation, roadmap, source, archive, decision records, summaries,
implementation guidance, and other explicitly classified material) exactly as the
repository's own governance establishes them.

## No authority from chronology or metadata

An agent MUST NOT infer authority from: creation date, modification date,
chronology, version number, filename, directory location, Git commit chronology,
apparent recency, document length, amount of detail, writing quality,
sophistication, repetition, or similarity to another document. None of these
establishes greater authority.

## No automatic authority inheritance

Authority is not automatically inherited through copying, quotation,
summarisation, derivation, reference, citation, paraphrase, extraction,
provenance enrichment, or placement in another directory.

Where the repository explicitly establishes a relationship and status, follow
that explicit evidence. Where authority depends on an unresolved relationship or
status, do not infer it — human confirmation is required where necessary.

## Formal promotion controls authority changes

Authority changes only through the repository's established formal promotion
mechanism (the 8-step Promotion Rule in `governance/status-model.md` and
`_consolidation/requirement-register.md` REQ-021). An agent must not promote,
demote, supersede, or otherwise alter authority through its own judgement. A
human/designer ruling may exist in non-canonical material and remains
non-canonical until it passes through that formal process.

## LLM analysis does not resolve authority

The LLM may inspect, compare, classify, explain, identify contradictions,
identify ambiguity, present evidence, present possible interpretations, and make
recommendations when requested. But analysis and recommendation do not
themselves establish authority. An LLM assessment, recommendation, simulation
result, or synthesis does not establish canonical authority.

## Principle of evidence before interpretation

Determine what the repository explicitly establishes before deciding how
material may be used. Determine the **status** of a document first, not its
authority from how authoritative the content appears. If the repository does not
establish an answer, do not manufacture one.

## Human escalation workflow

The preferred workflow is:

```
INSPECT → ANALYSE → IDENTIFY AMBIGUITY → EXPLAIN EVIDENCE
→ IDENTIFY CONSEQUENCE → PRESENT HUMAN QUESTION → STOP
→ HUMAN RULING → IMPLEMENT IF AUTHORISED
```

When an authority question is unresolved, the agent must present:

1. **Evidence** — what the relevant repository material actually says.
2. **Established governance** — what the repository explicitly establishes.
3. **Ambiguity** — what remains unresolved.
4. **Consequence** — what operation cannot safely proceed.
5. **Human question** — the precise decision requiring human direction.

During the ambiguity stage the LLM is expected to be useful: explain what
happened, what the evidence says, what is uncertain, what interpretations are
possible, and why the uncertainty matters. It must **stop** the authority-
dependent operation and **not** silently select one interpretation.

## Analysis versus action

**Read-only analytical activities** require no special authority: inspection,
search, comparison, audit, classification, reporting, identification of
conflicts, provenance analysis.

**Authority-changing activities** require the appropriate human authority and
formal process: promotion, demotion, supersession, canonicalisation, resolution
of unresolved design decisions, changes to governance authority. These must not
be performed by the agent's own judgement.

## Repository modification control

Before modifying repository files, the agent MUST:

1. determine exactly what operation has been requested;
2. determine which files are within the requested scope;
3. consult relevant governance and authority controls;
4. determine the status of the affected material;
5. determine whether the operation requires human clarification or formal approval;
6. confirm that the requested modification is permitted;
7. inspect the current Git working-tree state.

The agent must then:

8. modify only the authorised files and content;
9. avoid unrelated cleanup or opportunistic changes;
10. review the resulting diff;
11. verify that no unintended files were changed;
12. report what was changed and what was not changed.

The agent MUST NOT expand the task merely because it notices other issues. If
another issue is discovered, report it separately unless the user explicitly
authorises work on it and governance permits that work.

## Git pre/post control

For controlled repository modifications, use Git as a verification/control
mechanism.

**Before modification:** record the current branch, working-tree state, and
relevant existing diff/state where practical.

**After modification:** record the resulting working-tree state, the exact files
changed, the relevant diff, and confirmation that unrelated files were not
changed.

Git chronology remains NON-AUTHORITATIVE for design authority. Do not confuse
"Git tells me what changed" with "Git tells me which design is authoritative."
The first is permitted; the second is prohibited.

## Provenance

Preserve the repository's existing provenance model
(`governance/provenance.md`). Where applicable, maintain the distinction between
`author_llm`, `assessor_llm`, `last_modified_by_llm`, `created_date`, and
`last_modified_date`. Do not overwrite original authorship merely because another
LLM later modifies the document. Do not treat assessment as conferring
authority. Do not fabricate provenance — record unknown provenance as
unknown/not established.

## Missing or incomplete evidence

Do not reconstruct missing historical material as fact. When evidence is
missing: state that it is missing, distinguish known from unknown, preserve
uncertainty, and do not fabricate historical wording, provenance, or decisions.

## Authority claims

A document's statement that it is authoritative, final, approved, superseding,
accepted, locked, or canonical must not automatically be accepted as proof of
authority — nor automatically rejected. Validate such claims against the
repository's established governance and authority model. If the repository
cannot establish the claim's authority, escalate rather than deciding.

## Unresolved governing specification

The authority/status of the incomplete or abbreviated governing specification
(`prompts/project-documentation-consolidation-prompt.md`) remains unresolved.
Do not resolve it, do not classify it as authoritative or non-authoritative, do
not reconstruct the missing material, and do not infer what it contained. If its
status becomes operationally relevant, escalate to the human.
