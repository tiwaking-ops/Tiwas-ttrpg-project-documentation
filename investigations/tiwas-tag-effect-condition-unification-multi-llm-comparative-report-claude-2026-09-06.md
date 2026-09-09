---
document:
  title: "Tags/Effects/Conditions Unification — Multi-LLM Comparative Report"
  version: "1.0"
  status: "Advisory synthesis — Non-canonical. Not a ruling. Prepared for OpenCode documentation and Tiwa's review/ruling."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-06"
  last_modified_date: "2026-09-06"
governance_note: >
  This report compares six design-advisory outputs (Claude Sonnet 5's own prior
  draft plus five uploaded reports) produced against the same source prompt
  (`Prompt - tag condition effect unification1.md`). It makes no ruling and
  changes no DEC entry. Per project governance, OpenCode's live repository view
  is authoritative over any LLM's inference, including this one's; all
  cross-report claims below should be checked against the live register before
  being treated as settled.
---

# Tags / Effects / Conditions Unification — Multi-LLM Comparative Report

## 1. Executive Summary

Six independent advisory outputs were produced against the same prompt. All six
converge on the same headline verdict — **unify the record shape, do not collapse
the fiction-level Types** — and all six independently reject literal Tag-vs-Tag
resource arithmetic. That is a strong 6/6 convergence signal by the project's own
standard (independent-LLM convergence is documentary evidence, not
self-promotion — see `decision-register.md` governance note).

Real, unresolved forks remain on four points: (1) whether Tag Tier/Magnitude fields
should be *optional/inert* or *always-present-at-zero*; (2) whether a universal
`Persistence`/`Duration` field should exist at all, or whether persistence should be
pure Type-default with no stored field; (3) whether a Tag-counter relation is
declared **on the countering Tag's own record** (a list field) or **on the
consuming rule/mechanic** (a predicate evaluated externally); and (4) whether
"countering" should exist as a primitive at all, versus being reframed as an
existing Difficulty/permission-gate mechanism.

Cross-referencing all six against the live register surfaces one finding none of
the six reports made explicit: **DEC-059 (Armor Bypass) is a closer existing
precedent for "Tags relate to Tags" than DEC-088**, and its exact wording
("An Armor Tag's rule text may specify it does not trigger against Effects
carrying a designated other Tag") favors the *record-declares-its-own-counters*
design over the *consumer-declares-the-predicate* design that four of the six
reports preferred. This is addressed in §7.

Two governance issues were found in the source materials themselves (§10): one
report carries no YAML provenance header identifying its producing model, in
direct tension with the project's own provenance requirement, and one report
self-labels as an "OpenCode Project Documentation Report" despite OpenCode being
the project's designated documentarian role, not an LLM identity any of these
sessions hold.

## 2. Purpose, Scope, and Governance Framing

This document does not rule on the unification proposal. It:

1. Inventories the six reports produced against `Prompt - tag condition effect
   unification1.md`.
2. Compares their proposed schemas, verdicts, and treatment of the five original
   hypotheses.
3. Identifies genuine points of convergence (high evidentiary weight) versus
   genuine forks (require Tiwa's ruling).
4. Flags provenance/governance defects in the source reports themselves.
5. Produces one consolidated, deduplicated open-question register.
6. Offers an advisory synthesis recommendation — not a ruling, not a promotion.

Authority hierarchy for this document is unchanged: `canonical/` outranks
everything here; none of the six source reports outrank each other by default
(cross-model convergence is corroborating evidence, not automatic authority); and
this comparative report itself carries no more authority than any one of the six
it compares. Nothing here is table-ready until Tiwa rules and OpenCode records.

## 3. Session Inventory

| Ref | Report | Self-Reported Author (LLM / Version) | Independent Run? |
|---|---|---|---|
| A | `tiwas-tag-effect-condition-unification-decision-draft-2026-09-06.md` | Claude Sonnet 5 (`claude-sonnet-5`) | Yes |
| B | `tiwas-tag-condition-effect-unification-draft-execution-report-perplexity-2026-09-06.md` | Perplexity AI — "perplexity-sonnet (current production model)" | Yes |
| C | `tiwas-unified-state-record-architecture-decision-draft-2026-09-06.md` | "GPT-5.6 Luna" | Yes |
| D | `tiwas-unified-state-architecture-multi-llm-output-consolidation-copilot-2026-09-06.md` | Microsoft Copilot — "Model Identity: unknown / not established" | **No — self-declared as a consolidation/summary of a prior chat**, not a fresh independent analysis |
| E | `tiwas-tag-condition-effect-unification-evaluation-gemini-2026-09-06.md` | Gemini 2.5 Pro | Yes |
| F | `tiwas-unified-state-record-tags-effects-conditions-decision-draft-2026-09-06.md` | **Not stated — no YAML header, no author field anywhere in the document** | Unknown |

Report D is excluded from "independent convergence" counts below (§5) because it
explicitly frames itself as summarizing session outputs rather than performing
its own first-principles analysis; its agreement with the others therefore
carries the evidentiary weight of a restatement, not a second data point. Report
F's content is evaluated on its merits, but its authorship is unverified — see
§10.

## 4. Comparative Schema Table

| Field | A (Claude) | B (Perplexity) | C (Luna) | D (Copilot) | E (Gemini) | F (Unattributed) |
|---|---|---|---|---|---|---|
| `Type` enum (Tag/Effect/Condition) | Yes | Yes | Yes | Yes | Yes | Yes |
| Tier `Y` | Optional for Tag | Present, unqualified | **Optional, Type-gated** | Present, unqualified (`≥0`) | Present, always (`0` = Universal) | Present, unqualified |
| Magnitude `Z` | Optional; populated only for graded Tags | Present, unqualified | **Optional, Type-gated** | Present, always (`integer`) | **Always present; `Z=0` for Tags by convention** | Present, unqualified |
| Location `X` | Optional | Optional | Optional | Enum `{None, Tier1, Tier2}` | Optional | Optional |
| Persistence/Duration field | Yes (`Persistence` field, default-driven) | Yes (`duration` enum) | **No — explicitly rejected as a universal field**; Type-default only | Yes (`Persistence` enum) | Yes (`State Flags`) | Yes (`Duration` enum) |
| Removal mechanism | `Removal` trigger string, required if Persistent | `removal_tags: list<text>` | Authorised removal/replacement action per Type rule (no dedicated field) | Not specified as a field | Structural repair/GM action, no dedicated field | Named action / higher-Tier Effect |
| Stacking field | Not specified (defers to per-Condition rule) | Not specified | Not specified (defers to per-Condition rule) | `StackRule` enum `{Add, Replace, Highest, Special}` | Not specified | `StackRule` enum `{Replace, Add, Highest, Special}` |
| Counter mechanism location | On the **consuming Trait/Effect** (extends DEC-088 clause) | On the **countering record itself** (`counters: list<text>`) | On the **consuming rule** (formal predicate `Active(A,C) = Present(A) ∧ ¬Countered(B,A,C)`) | Unspecified ("relational Tag counters override numeric fields") | **Rejected as a primitive** — reframed as an S-8-style permission/difficulty gate | On the **countering record itself** (implied identity-based) |

Note the D/F `StackRule` enum overlap (`{Replace, Add, Highest, Special}` /
`{Add, Replace, Highest, Special}`) is identical in substance and near-identical
in wording. Combined with D's self-declared consolidation role, this suggests F
(or a document very like it) may be one of the source materials D was
summarizing, rather than the two being fully independent data points. This
should be confirmed against the live chat log before F and D are counted as two
separate convergence votes anywhere in this report.

## 5. Points of Convergence

Counting only independent runs (A, B, C, E, F — D excluded per §3):

1. **5/5** reject literal Tag-to-Tag resource/pool arithmetic as a violation of
   DEC-058/079/080/088 and Invariant 17/REQ-017; all propose some read-only or
   permission-based substitute instead.
2. **5/5** confirm the proposal does **not** reopen DEC-025, on the same
   grounds: DEC-025 concerns Skill-side tag/category entitlement specifically,
   and this proposal concerns state records on characters/items/environment/
   scenes, not Skills.
3. **5/5** hold DEC-007.A and Invariant 17 as absolute and unmodified regardless
   of which schema variant is adopted.
4. **5/5** treat "Tags and Conditions are literally the same thing" as the
   single highest-conflict idea, citing DEC-079's Tier/Magnitude/stacking/
   removal machinery as real, non-trivial semantic content that a bare schema
   merge would otherwise discard.
5. **4/5** (A, C, D, E; B is ambivalent/less explicit) explicitly recommend
   **against** forcing Tier/Magnitude onto every Tag, on the grounds that most
   of DEC-080's alpha vocabulary (`slot:main_hand`, `damage:slashing`, etc.) is
   boolean/classificatory and gains nothing from a numeric field.
6. **5/5** treat "permanence is a default, not an absolute" as already
   effectively precedented by DEC-060/DEC-079 §C8 (Sundered), and as the
   lowest-conflict of the five original ideas.
7. **5/5** independently identify DEC-088's Conditional-Trait Binding grammar
   (`Active only while [env:X] is present`) as the existing mechanism closest
   in kind to whatever "Tag counters Tag" ends up meaning.

## 6. Points of Divergence — Genuine Forks

| Fork | Position 1 | Position 2 | Held by |
|---|---|---|---|
| **Tier/Magnitude on Tags: optional-and-absent vs. always-present-at-zero** | Field is *absent* on non-graded Tags (no field = no meaning) | Field is *always present*, conventionally `Z=0`/`Y=0` for non-graded Tags | Pos.1: A, C, F. Pos.2: B, E (D is ambiguous — states the field is `integer ≥ 0` with no exemption clause) |
| **Universal Persistence/Duration field: exists vs. does not exist** | Add a `Persistence`/`Duration` field to the schema | Reject a stored field entirely; persistence is a **Type-default behavior**, not schema data | Pos.1: A, B, D, E, F. Pos.2: **C only** — but C's argument (a stored universal field is an unnecessary fourth axis) is not answered by any other report, and should not be dismissed by vote count alone. |
| **Counter relation ownership: on the Tag itself vs. on the consuming rule** | Countering Tag declares its own counter-list (`counters`/similar field) | Consuming Trait/Effect/mechanic declares which Tags it treats as mutually exclusive; Tags never reference each other | Pos.1: B, F (and, per §7, the closest existing precedent, DEC-059, also matches Pos.1). Pos.2: A, C, E |
| **Does "Tag counters Tag" exist as a primitive at all?** | Yes, in some read-only form | No — replace with existing Difficulty/permission-gate machinery (S-8) so no new primitive is created | Pos.1: A, B, C, F. Pos.2: **E only** |
| **StackRule as a first-class schema field vs. left to per-Condition/per-Identity rule text** | Add a `StackRule` enum to the shared schema | Leave stacking as Type/Identity-specific rule text, not a schema field | Pos.1: D, F. Pos.2: A, B, C, E |

None of these forks is a "someone is simply wrong" situation — each position is
internally defensible and grounded in a real project constraint (schema economy
vs. field reuse vs. fidelity to DEC-059/060/079/088 precedent). They are exactly
the kind of fork the project's own governance rules (`status-model.md` LLM Rule
6: "Never silently resolve an open designer fork") require surfacing rather than
collapsing.

## 7. Cross-Report Finding: DEC-059 Is the Strongest Existing Precedent, and It Was Under-Cited

All five independent reports (A, B, C, E, F) reach for **DEC-088** (Conditional-
Trait Binding: `Active only while [env:X] is present`) as the nearest existing
precedent for a Tag participating in a mechanical decision without becoming
stateful. Only **Copilot's derivative summary (D)** and, briefly, this report's
own author (A) name **DEC-059** at all, and none of the six develops it.

DEC-059's actual text is a closer match to the specific "Tags counter Tags"
hypothesis than DEC-088 is:

> "Bypass = a relational property between specific Tag pairs. **An Armor Tag's
> rule text may specify it does not trigger against Effects carrying a
> designated other Tag.** Requires both a Tag-pairing match and a location
> match... Stateless; neither Tag is altered."

This is materially different from DEC-088 in one important way: DEC-088 is a
*consumer* (a Trait/Effect) reading a scene-state Tag's presence. DEC-059 is one
**Tag's own rule text** declaring a relation to another Tag/Effect identity —
i.e., the relation is authored **on the countering record itself**, not on a
third-party consumer. That is precisely the schema shape Reports B and F
proposed (`counters: list<text>` / identity-declared counters) and precisely the
shape Reports A, C, and E argued against in favor of consumer-side predicates.

**This changes the balance of the fork in §6, row 3.** The existing corpus
already contains a working, non-canonical, Invariant-safe example of exactly the
record-side design — it just does it for Armor Tags vs. Effect-carried Tags,
not yet for Tag-vs-Tag. A future ruling should treat DEC-059 as the load-bearing
precedent for this fork, and additionally decide whether DEC-059's **location-
match requirement** ("also inapplicable at Location Tier 0") should carry over
to scene-scoped counters like `env:darkness` vs. `ignores:darkness` — none of
the six reports considered whether an environmental counter-Tag needs a location
match the way an equipment Bypass Tag does. This is added to the open-question
register in §9.

## 8. Per-Report Critical Assessment

Scored against the source prompt's own three success criteria: (i) honesty about
whether the merge reduces or relocates complexity, (ii) concreteness of the
schema/rules, (iii) conflict fidelity (correct DEC citation, and distinguishing
"real conflict" from "never specified").

| Report | (i) Honesty | (ii) Concreteness | (iii) Conflict Fidelity | Notable strength | Notable weakness |
|---|---|---|---|---|---|
| A (Claude) | Strong — explicit partial-merge verdict, net-negative call on full Tag merger | Moderate — full schema + rules, fewer worked before/after translations | Good, but **missed DEC-059** (see §7) | Clean Type/Subtype resolution of the Sundered precedent | Fewer concrete worked examples than C |
| B (Perplexity) | Moderate — leans toward "yes, conditionally" more readily than others | Good — compact schema, tabular impact analysis | Good — correctly ties each idea to specific DECs | `counters`/`removal_tags` design is well-specified and (per §7) the best-precedented | Heavy self-citation formatting noise; unverifiable session timestamps |
| C (GPT-5.6 Luna) | **Strongest** — explicit "not a 3→1 reduction," names the "mini programming language" failure mode | **Strongest** — literal syntax, formal predicate logic, five worked before/after translations (darkness, night-vision, Frightened, Wound, Sundered) | Strong — precise DEC-023/024/027/060/079/088 mapping | Best worked-example coverage in the set | Rejects a Persistence field outright without addressing the removal-trigger bookkeeping the other five all found necessary |
| D (Copilot) | Weak — largely declarative ("unification is viable"), does not grapple with the tension as hard as A/C/E | Weak — restates a schema without derivation or worked translation | Weak — cites DEC numbers in a list without explaining the mapping | Introduces `StackRule` as a first-class field (useful, if under-argued) | **Self-identifies as an "OpenCode Project Documentation Report"** despite being an LLM chat output, and is explicitly a derivative summary, not an independent analysis (§3) |
| E (Gemini) | Strong — explicit "net-negative in full, positive if partial" framing | Good — formal schema notation, diagram, quantified complexity table | Good, and **uniquely cites DEC-059** among the fully independent reports | Only report to reject "counter" as a primitive outright, reframing via S-8 difficulty-gating | Complexity table uses fabricated-looking precision (page counts, "~40%") with no grounding in an actual rulebook page count — presented with more confidence than the evidence supports |
| F (Unattributed) | Strong — explicit "conditionally worth adopting... only in minimal form" | Good — full schema, clear Type-default table | Good — correctly scopes DEC-025 non-reopening and DEC-007.A preservation | Cleanest statement of the permission-precedence counter rule ("losing Tag remains on the record, simply ignored") | **No provenance header at all** — see §10 |

## 9. Consolidated Open-Question Register

Deduplicated across all six reports; each retains a `Source` column mapping back
to which report(s) raised it.

| # | Open Question | Raised By |
|---|---|---|
| 1 | Is Tier/Magnitude on a Tag record *absent-when-unused* or *always-present-at-zero*? | A, B, C, D, E, F (§6) |
| 2 | Does a universal `Persistence`/`Duration` field belong in the shared schema, or is persistence purely a Type-default with no stored field? | A, B, C, D, E, F (§6) |
| 3 | Is a Tag-counter relation declared on the countering record itself, or on the consuming rule/mechanic? | A, B, C, E, F — **see §7 for the DEC-059 precedent bearing directly on this** |
| 4 | Should "Tag counters Tag" exist as a primitive at all, or should it be retired in favor of an existing Difficulty/permission-gate mechanism (S-8)? | E (uniquely) |
| 5 | If an environmental/scene-scoped counter-Tag relation is adopted, must it carry a **location-match requirement** the way DEC-059's Armor Bypass does, or is that requirement specific to equipment and inapplicable to scene state? | New — surfaced in §7, not raised by name in any of the six source reports |
| 6 | Is `StackRule` a first-class schema field, or left to per-Condition/per-Identity rule text as today? | D, F |
| 7 | Is `Sundered` represented as one record with a Tag-facing "projection," or does it remain two records (a Condition and a Tag) because a consuming rule genuinely needs both? | C (explicit worked proposal), F (implied) |
| 8 | Should Wounds be formally reclassified as `Condition: Wounded` under the unified schema, or retained as a fourth semantic Type despite sharing the same backbone? | C |
| 9 | Does the unified schema supersede DEC-079's Condition format immediately, or only after a dedicated Condition-semantics audit confirms nothing is silently lost? | A, C |
| 10 | Can Conditions counter Tags (or only Tag-to-Tag), and can a Condition's Tier/Magnitude influence a counter outcome, or is counter resolution purely boolean presence/absence? | C |
| 11 | Should this be recorded as one architectural DEC with Type-specific amendments, or as separate DEC rulings per Type (Tag / Effect / Condition)? | C |
| 12 | Default counter policy: must every counter relation be explicitly declared (per pair), or should some class of counters (e.g., creature immunity Tags vs. matching environmental Tags) apply by a general rule? | B |
| 13 | Should removal ever be multi-target (one Effect closing several records at once), or strictly one Effect → one record? | B |

## 10. Governance and Provenance Flags

These are process findings, independent of the merits of any proposal, and are
raised because the project's own governance rules require them to be surfaced
rather than quietly absorbed:

1. **Report F carries no YAML provenance header and no author field anywhere in
   the document.** Project governance requires "All LLM-authored artifacts must
   carry YAML provenance headers identifying the producing model and version."
   Report F's content is sound on the merits (§8), but it cannot currently be
   attributed, and its convergence with the other reports should not be counted
   as a fully independent corroborating vote until its origin is confirmed.
2. **Report D self-titles as an "OpenCode Project Documentation Report" with
   "Author (LLM): Microsoft Copilot."** OpenCode is the project's designated
   documentarian role with live repository access (`authority.md`); it is not
   an identity any advisory LLM session — including this one — holds. An LLM
   chat output describing itself as an OpenCode report, rather than as input
   *to* OpenCode, blurs a distinction the project's governance model depends
   on. This report (the one you are reading) is deliberately framed as
   *prepared for OpenCode's documentation use*, not as an OpenCode artifact
   itself, for that reason.
3. **Report D is a derivative summary, not an independent analysis**, by its
   own description ("This report consolidates all outcomes produced during the
   chat session"). It has been weighted accordingly in §5's convergence counts.
4. **Report B's timestamps** ("2026-09-06, 20:35–20:37 NZST") and dense
   per-sentence self-citation are unverifiable from the transcript context and
   should not be read as authoritative session metadata.
5. **All self-reported model version strings in this document** (e.g.,
   "perplexity-sonnet (current production model)," "GPT-5.6 Luna") are exactly
   that — self-reported by the respective sessions, not independently verified
   by this report. Per standing project practice, OpenCode's filesystem/session
   records, where they exist, are authoritative over any LLM's self-report.

## 11. Advisory Recommendation

This is Claude's advisory synthesis only. It is not a ruling and does not bind
Tiwa's decision.

1. **Adopt the Effect+Condition schema merger now.** All six reports agree this
   is close to free; DEC-035.A and DEC-079 are already the same shape.
2. **Extend the schema to Tags with fields optional/absent-by-default**, not
   always-present-at-zero (§6 fork 1). Absent is cheaper to reason about at the
   table than a field that is always there but almost always meaningless.
3. **Do not add a stored universal `Persistence` field.** Report C's argument —
   persistence is a Type-default behavior, and a fourth universal axis is
   schema bloat the other five reports' own complexity-math sections warn
   against — is not answered by the other five, and is consistent with the
   project's general preference for the minimum viable mechanic (Invariant 17
   spirit, applied by analogy).
4. **Resolve the counter-ownership fork (§6 fork 3) in favor of the
   record-declares-its-own-counter design**, on the strength of the DEC-059
   precedent identified in §7 — not because more reports voted for the
   opposite position, but because the closest existing operative rule already
   works this way.
5. **Do not adopt Gemini's "retire counter as a primitive" position (§6 fork
   4) by default, but flag it for Tiwa's direct attention** — it is the single
   most structurally different proposal in the set (moves the mechanic into
   S-8 Difficulty rather than a new Tag-layer primitive) and deserves a
   yes/no ruling on its own, not a majority-vote dismissal.
6. **Carry forward the location-match question from §7/§9 item 5** as a
   genuinely new open item this comparative pass surfaced that no single
   source report asked outright.
7. **Treat Reports D and F's process defects (§10) as blocking for citation
   purposes**, even though F's content is usable: confirm F's authorship before
   recording it in the decision register as a corroborating independent run.

## 12. Document Control

| Version | Date | Author (LLM / Version) | Change |
|---|---|---|---|
| 1.0 | 2026-09-06 | Claude Sonnet 5 (`claude-sonnet-5`) | Initial comparative synthesis of Reports A–F |

**Distribution:** Tiwa (for ruling); OpenCode (for recording, pending Tiwa's
ruling on §11 and the open questions in §9). Not for player distribution.
**Retention:** Permanent project record pending any future ruling that
supersedes it.
