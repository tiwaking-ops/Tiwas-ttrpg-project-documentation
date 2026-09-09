# Tiwas TTRPG — Formal Project Documentation Report

## Document Metadata

| Field | Value |
|-------|-------|
| **Document Title** | Tag-Condition-Effect Unification Decision Draft — Execution Report |
| **Project** | Tiwas TTRPG (d100 percentile universal RPG) |
| **Document Type** | Formal Project Documentation Report |
| **Document Version** | 1.0 |
| **Document Status** | Non-canonical designer ruling draft (pending formal promotion via 8-step process) |
| **Report Date** | 2026-09-06 |
| **Report Time** | 20:37 NZST |
| **Author (LLM)** | Perplexity AI |
| **Author (LLM Version)** | perplexity-sonnet (current production model) |
| **Source Prompt File** | `Prompt - tag condition effect unification1.md` |
| **Related Project Files** | `PROJECT_CONTEXT.md`, `decision-register.md`, `tiwas-implementation-roadmap-and-project-governance-v1.4.3.md`, `authority.md` |
| **Purpose** | Record complete results from LLM advisory session executing the Tag-Condition-Effect Unification prompt; provide adoptable Decision Draft for designer evaluation |

***

## 1. Executive Summary

This report documents the complete output of an LLM advisory session executed on 2026-09-06, in which the prompt contained in `Prompt - tag condition effect unification1.md` was executed against the Tiwas TTRPG project corpus.  The session produced a formal Decision Draft evaluating a proposed unification of the game's Tags, Effects, and Conditions subsystems under a single mechanical backbone (`StateRecord`).  The draft concludes that unification is worthwhile provided that "permanence" and "counter" behaviours are implemented as derived meta-rules rather than new core fields, preserving the existing constraints against resource economy modification and single-resolution-engine architecture. [Prompt](Prompt - tag condition effect unification1.md)

***

## 2. Scope and Objectives

### 2.1 Scope

This report covers:

- Execution of the unification prompt as specified in `Prompt - tag condition effect unification1.md`. [Prompt](Prompt - tag condition effect unification1.md)
- Production of a structured Decision Draft meeting the prompt's success criteria (honesty about core tensions, concreteness of schema/rules, conflict fidelity with existing DEC numbers and Invariants). [Prompt](Prompt - tag condition effect unification1.md)
- Documentation of the draft's recommendations, conflict analysis, and open questions for designer ruling. [Prompt](Prompt - tag condition effect unification1.md)

### 2.2 Objectives

- Provide the designer (Tiwaking) with a concrete, adoptable unification proposal that reduces rulebook complexity while respecting existing architectural invariants. [Prompt](Prompt - tag condition effect unification1.md)
- Identify all points of tension with prior non-canonical rulings (DEC-058/079/080/088, Invariant 17/REQ-017, DEC-007.A, DEC-025, DEC-079). [Prompt](Prompt - tag condition effect unification1.md)
- Flag open questions requiring explicit designer decisions before any promotion to Canonical status. [Prompt](Prompt - tag condition effect unification1.md)

***

## 3. Methodology

### 3.1 Source Material

The following project files were consulted to ensure alignment with existing governance and decision structures:

- `Prompt - tag condition effect unification1.md` — source prompt specifying the unification hypothesis and deliverable requirements. [Prompt](Prompt - tag condition effect unification1.md)
- `PROJECT_CONTEXT.md` — project overview, locked vs. non-canonical distinctions, and governance structure. 
- `decision-register.md` — canonical and non-canonical decision registry (DEC-001 through DEC-016 and beyond). 
- `tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` — implementation sequencing and governance framework.[2]
- `authority.md` — document authority hierarchy and promotion process. 

### 3.2 Execution Process

1. **File discovery**: Identified `Prompt - tag condition effect unification1.md` via project file listing. [Prompt](Prompt - tag condition effect unification1.md)
2. **Content extraction**: Retrieved full prompt text specifying the unification proposal, constraints, and success criteria. [Prompt](Prompt - tag condition effect unification1.md)
3. **Draft production**: Generated a structured Decision Draft (~2,000 words) addressing all required sections per the prompt. [Prompt](Prompt - tag condition effect unification1.md)
4. **Conflict mapping**: Cross-referenced draft recommendations against existing DEC numbers and Invariants to identify tensions. [Prompt](Prompt - tag condition effect unification1.md)
5. **Documentation**: Compiled this formal report recording the session output for project governance and audit purposes. [Prompt](Prompt - tag condition effect unification1.md)

***

## 4. Results

### 4.1 Unified Record Schema (`StateRecord`)

The draft proposes a single state record type shared by Tags, Effects, and Conditions:

```text
StateRecord {
  type: enum { Tag, Effect, Condition }        // fiction-level label only
  subtype: text?                               // e.g. "env", "creature", "injury"
  id: text                                     // stable identifier (e.g. "darkness", "sundered")
  tier: integer Y                              // potency tier
  magnitude: integer Z                         // intensity within tier
  location: text?                              // optional location X (body part, slot, zone)
  source: text?                                // what created it (skill, trait, environment)
  duration: enum { instant, scene, session, permanent }?  // optional, default by type
  removal_tags: list<text>?                    // named actions/effects that can remove it
  counters: list<text>?                        // ids of records this record neutralizes
}
```

**Key design principles:**

- **Tier Y and Magnitude Z** are the only mechanical potency axes; all stacking and precedence rules are expressed in these terms. [Prompt](Prompt - tag condition effect unification1.md)
- **Type** (Tag/Effect/Condition) is fictional classification only; the engine sees one shape. [Prompt](Prompt - tag condition effect unification1.md)
- **Duration** encodes "permanence" as a default state, not an absolute property. [Prompt](Prompt - tag condition effect unification1.md)
- **removal_tags** provides an explicit, auditable allowlist of what can remove each record. [Prompt](Prompt - tag condition effect unification1.md)
- **counters** enables declarative Tag-vs-Tag counter relationships without introducing rolls or pools. [Prompt](Prompt - tag condition effect unification1.md)

### 4.2 Impact Analysis of Five Proposal Ideas

| # | Proposal Idea | Net Impact | Key Conflicts |
|---|---------------|------------|---------------|
| 1 | Tags are like Effects, but Tags are Permanent; Effects are caused by a Skill Roll | Collapses creation grammars; permanence becomes default duration | Tension with read-only/stateless guardrail (DEC-058/079/080/088; Invariant 17/REQ-017); respects DEC-007.A if no pool modification |
| 2 | Tags have Tier Y, Magnitude Z; may have Location X | Uniform potency axes; eliminates special cases | Risks Tags feeling mechanically active; must stay read-only re: pools |
| 3 | Tags can counter other Tags | Systematic environmental/creature interactions (e.g. Night-Vision vs darkness) | Biggest tension with stateless guardrail; must be simple filter, not second engine |
| 4 | Tags and Conditions are NOT distinct | Collapses two record formats; removes "Z = −Y" Condition rule | Departs from DEC-079; must encode negative scaling via interpretation, not schema |
| 5 | Tags can be Removed | Uniform removal grammar via `removal_tags` and named actions | Departs from implicit Tag immutability; respects no-resource-economy constraint |

### 4.3 Complexity Assessment

**Complexity reductions:**

- One schema instead of three record shapes. [Prompt](Prompt - tag condition effect unification1.md)
- One stacking/expiration model. [Prompt](Prompt - tag condition effect unification1.md)
- One removal grammar. [Prompt](Prompt - tag condition effect unification1.md)
- Fewer special cases (Night-Vision, Sundered, localized injuries). [Prompt](Prompt - tag condition effect unification1.md)

**Complexity risks:**

- Counter relationships could become a web of pairwise rules if overused. [Prompt](Prompt - tag condition effect unification1.md)
- Additional fields (`duration`, `removal_tags`, `counters`) increase record size. [Prompt](Prompt - tag condition effect unification1.md)
- Meta-rules must remain simple and declarative to avoid rebuilding a second engine. [Prompt](Prompt - tag condition effect unification1.md)

**Net verdict:** Complexity decreases if counter and removal rules are kept simple and auditable. [Prompt](Prompt - tag condition effect unification1.md)

### 4.4 Conflicts and Tensions

| Tension | Existing Ruling | Proposed Departure | Mitigation |
|---------|-----------------|-------------------|------------|
| Tags counter Tags vs. stateless guardrail | DEC-058/079/080/088; Invariant 17/REQ-017 (Tags read-only, no resource economy) | Counter relationships encode mechanical interactions | Treat counters as pure filter on effect application; no rolls, no pools |
| Tags/Conditions not distinct vs. distinct formats | DEC-079 (Conditions have own format/stacking/removal) | Unified schema; drop "Z = −Y" rule | Encode negative scaling via interpretation (e.g. Tier-based disadvantage tables) |
| Tag removal vs. Tag immutability | DEC-060/079 (only specific cases like Sundered have removal) | General removal model via `removal_tags` | Removal actions are Effects created by normal resolution engine |
| Unification re-opening DEC-025 (Skill-tag system) | DEC-025 (rejected formal tag/category system on Skills) | Tags more mechanically expressive | Keep gating at trait/equipment/environment level, not Skill level |

### 4.5 Concrete Recommended Design

**Minimal unification proposal:**

1. Adopt `StateRecord` as the only state shape for Tags, Effects, and Conditions. [Prompt](Prompt - tag condition effect unification1.md)
2. Define defaults by `type`:
   - Tag: `duration = permanent` unless specified; `removal_tags` usually empty or small. [Prompt](Prompt - tag condition effect unification1.md)
   - Effect: `duration = instant` or `scene`; created by S-1 contest payloads. [Prompt](Prompt - tag condition effect unification1.md)
   - Condition: `duration` varies; typically negative fiction. [Prompt](Prompt - tag condition effect unification1.md)
3. Counter rule (simple, declarative):
   - Add optional `counters: list<text>` to `StateRecord`. [Prompt](Prompt - tag condition effect unification1.md)
   - Meta-rule: "If a target has a StateRecord whose `id` is in another record's `counters` list, the countered record's effects do not apply to that target." [Prompt](Prompt - tag condition effect unification1.md)
4. Removal rule:
   - Add `removal_tags: list<text>` to `StateRecord`. [Prompt](Prompt - tag condition effect unification1.md)
   - Meta-rule: "An Effect can remove a StateRecord if the Effect's `id` is in that record's `removal_tags`." [Prompt](Prompt - tag condition effect unification1.md)
5. Preserve no pool modification:
   - Explicit invariant: "No StateRecord may directly modify HP, Overflow, or any pool." [Prompt](Prompt - tag condition effect unification1.md)
6. Keep fiction-level distinctions:
   - Rules text still talks about "Tags", "Effects", and "Conditions" as distinct concepts. [Prompt](Prompt - tag condition effect unification1.md)

### 4.6 Open Questions for Designer Ruling

- **Default counter policy**: Counters only when explicitly listed, or general rule (e.g. creature Tags counter matching environmental Tags by default)? [Prompt](Prompt - tag condition effect unification1.md)
- **Magnitude in counters**: Can higher Magnitude Tags counter lower Magnitude Tags of the same id, or is counter purely by id match? [Prompt](Prompt - tag condition effect unification1.md)
- **Condition negativity**: How exactly do Condition records translate into negative outcomes (existing disadvantage rules vs. new Tier-based tables)? [Prompt](Prompt - tag condition effect unification1.md)
- **Removal scope**: Can an Effect remove multiple records at once if its id is in multiple `removal_tags` lists? [Prompt](Prompt - tag condition effect unification1.md)
- **Skill gating**: Comfortable with Traits/Equipment gated by Tags, but explicitly forbidding Skills from requiring Tags (to avoid re-opening DEC-025)? [Prompt](Prompt - tag condition effect unification1.md)

***

## 5. Governance and Authority

### 5.1 Document Status

This Decision Draft is **non-canonical** and constitutes a **designer ruling draft** pending formal promotion via the project's 8-step promotion process.  It does not modify any Canonical material (DEC-001 through DEC-016 and associated Invariants).[2]

### 5.2 Relationship to Existing Decisions

The draft explicitly identifies tensions with the following non-canonical rulings:

- **DEC-058/079/080/088** — Tags as read-only, stateless metadata. [Prompt](Prompt - tag condition effect unification1.md)
- **Invariant 17 / REQ-017** — No resource economy modification by Tags. [Prompt](Prompt - tag condition effect unification1.md)
- **DEC-007.A** — Overflow immutability (respected by proposal). [Prompt](Prompt - tag condition effect unification1.md)
- **DEC-079** — Conditions' distinct format and "Z = −Y" rule. [Prompt](Prompt - tag condition effect unification1.md)
- **DEC-025** — Rejected Skill-tag system (proposal must avoid re-opening). [Prompt](Prompt - tag condition effect unification1.md)

### 5.3 Promotion Path

To advance this proposal to Canonical status, the designer must:

1. Explicitly rule on the open questions in §4.6. [Prompt](Prompt - tag condition effect unification1.md)
2. Integrate the `StateRecord` schema and meta-rules into the Canonical rules document (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`). 
3. Update the Decision Register (`decision-register.md`) with new DEC entries for the unification. 
4. Follow the 8-step promotion process documented in `authority.md`. 

***

## 6. Provenance and Audit Trail

| Item | Value |
|------|-------|
| **Session Date** | 2026-09-06 |
| **Session Time** | 20:35–20:37 NZST |
| **Executing LLM** | Perplexity AI |
| **LLM Version** | perplexity-sonnet (current production model) |
| **Source Prompt** | `Prompt - tag condition effect unification1.md` (file:5) |
| **Consulted Files** | `PROJECT_CONTEXT.md` (file:4), `decision-register.md` (file:3), `tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` (file:11), `authority.md` (file:1) |
| **Output Format** | Markdown Decision Draft (~2,000 words) + this Formal Report |
| **Intended Audience** | Tiwaking (designer) only; working document for evaluation before ruling |

***

## 7. Appendices

### Appendix A — Source Prompt Excerpt

The source prompt (`Prompt - tag condition effect unification1.md`) specifies:

- **Role**: Senior TTRPG systems designer with license to challenge premises and surface conflicts. [Prompt](Prompt - tag condition effect unification1.md)
- **Context**: Tiwas d100 TTRPG with three overlapping subsystems (Tags, Effects, Conditions) to be unified. [Prompt](Prompt - tag condition effect unification1.md)
- **Proposal**: Five ideas (Tags permanent like Effects; Tier/Magnitude/Location for Tags; Tags counter Tags; Tags/Conditions not distinct; Tags removable). [Prompt](Prompt - tag condition effect unification1.md)
- **Deliverable**: Decision Draft (~1,500–2,500 words) with specific sections (executive verdict, schema, impact analysis, complexity math, conflicts, recommended design, open questions). [Prompt](Prompt - tag condition effect unification1.md)
- **Constraints**: No resource economy; single resolution engine; fiction-level distinctions preserved; non-canonical status acknowledged. [Prompt](Prompt - tag condition effect unification1.md)

### Appendix B — Related Canonical Material

- **DEC-007.A** — Overflow immutability clause (designer-approved wording amendment, 2026-09-01). 
- **DEC-013** — S-1 Universal Opposed Contest (locked). 
- **DEC-014** — S-2 Tier-1 Location Index provider (locked, limited scope). 
- **DEC-016** — Core Architectural Invariants (18 invariants binding on all future subsystem work). 

### Appendix C — Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-09-06 | Perplexity AI (perplexity-sonnet) | Initial formal report documenting unification Decision Draft execution |

***

## 8. Distribution and Access

- **Primary Recipient**: Tiwaking (designer)
- **Storage Location**: Tiwas TTRPG project repository (OpenCode)
- **Access Level**: Project team only; not for player distribution
- **Retention**: Permanent project record; to be updated if/when proposal is promoted to Canonical status

***

**End of Report**