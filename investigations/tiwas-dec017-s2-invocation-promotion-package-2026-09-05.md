---
document:
  title: "DEC-017 S-2 Invocation/Warrant Policy — Promotion Package v2.1 (merged with ChatGPT package; all open decisions ruled)"
  version: "2.1"
  status: "Promotion package. Non-canonical. All open decisions ruled by designer (2026-09-05). Ready to begin the 8-step sequence — stop-and-confirm after every step."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  promotion_target: "DEC-017 (S-2 attack-side invocation/warrant policy) per _consolidation/decision-register.md"
  promotion_process: "D3 §21 / REQ-021 / governance/status-model.md §Promotion Rule (8 steps)"
  merge_record: "v2.0 merges v1.0 (opencode/big-pickle) with the ChatGPT DEC-017 package (ChatGPT-DEC-017 Invocation Policy-20260905-2034.md). v2.1 records the designer's rulings (2026-09-05): DEC-A1 = Option C; all other recommendations accepted. All 8 steps require human stop-and-confirm before proceeding."
  human_confirmations_required: "STOP after every step (1–8). No step may be recorded as promotion-approved without explicit human confirmation of that step."
---

# DEC-017 S-2 Invocation/Warrant Policy — Promotion Package v2 (merged)

This package prepares the **8-step Promotion Rule** (D3 §21 / REQ-021 /
`governance/status-model.md`) for promoting **DEC-017** — the S-2 attack-side
invocation/warrant policy (candidate four-state model + Named-Outcome Test).
Nothing in this package changes authority by itself; it documents each step,
marks what evidence already exists, and supplies draft artifacts.

**v2 merge record (2026-09-05):** v1.0 (opencode/big-pickle) merged with the
ChatGPT DEC-017 package. Merge dispositions are itemised in §0.

## 0. Merge dispositions (analysis of the two packages)

| Item | v1.0 (mine) | ChatGPT package | Merge disposition |
|---|---|---|---|
| §5A final wording | Verbatim validated draft + "actor" generalization proposed | Expanded wording + 6 numbered clauses + "cinematic framing" exclusion | **Adopted the structure** of ChatGPT's clause expansion; incumbent wording choice left open (see §D, DEC-A1) |
| Formal rule format | Prose-only §14.7 | W1∧W2∧W3 gate table + formula | **Adopted the gates** (W1 Explicit Objective / W2 Established Location-Dependence / W3 Current Resolvability) merged into §E |
| DEC-014 relation | Embedded in scope/exclusions | First-class baseline (§2.2): invocation layer around DEC-014, not a modification of Zero-Step | **Adopted as Section B baseline principle** |
| Step control | Confirm authority-changing steps only | STOP after every step 1–8 | **Adopted ChatGPT's per-step stop-and-confirm** (designer-selected) — Section I |
| Non-attack reference | Correct: DEC-037 operative; DEC-020 **closed** | Stale: "still governed separately by DEC-020" | **Corrected to DEC-037** throughout (DEC-020 formally CLOSED 2026-09-05) |
| Step 8 scope | Roadmap + snapshots/briefs/context | Plus decision-register move + 8 regression cases | **Adopted** the extra Step 8 items (§H) |
| Non-attack exclusion (do not alter) | Yes | Yes | Agreed — retained |
| "Do not delete the investigation" | Implied (§F preserves D4) | Explicit | **Adopted explicit** preservation note (§G) |

## A. What is being promoted

**DEC-017** (decision-register §B): *"S-2 attack-side invocation/warrant policy —
candidate four-state model + Named-Outcome Test accepted as 'current non-canonical
working direction' for when a Location Index is warranted (attack-side only)."*

The promoted content is the **attack-side invocation policy** consisting of:

1. **Four-state classification** (internal/documentation architecture):
   State 1 = Established & Resolvable → generate; State 2 = Established, Not Yet
   Resolvable → do not generate (record pending); State 3 = Plausible,
   Location-Dependence Unresolved → do not generate; State 4 = No Distinct
   Consequence → do not generate.
2. **GM-facing operational test** (wording decision pending, §D).
3. **Named-Outcome Test** (Warrant test): a declared objective is definite — and
   Warrant-eligible — only if the actor explicitly names a distinct consequence,
   other than ordinary damage, whose resolution depends on the specified
   location. Validated 21/21 in a single-designer blind trial.
4. **Explicit-only objectives** (DEC-018, folded in): the GM does not infer an
   unstated distinct objective from location/fictional context alone.
5. **Procedural riders**: compound objectives evaluated disjunctively; stale
   objectives void the match; S-1 winner-only (only the winning participant's
   natural roll is eligible, per Canonical §13.2); lazy evaluation (design
   inference, provisionally adopted).
6. **W3 reference-cache role**: maintained shorthand for States 1/2 already
   established; never independently establishes Warrant or Anchor status; novel
   cases always evaluated directly against the policy.

**Scope boundaries of the promotion (explicitly NOT included):**

- Non-attack Location Index generation **not** — governed separately by
  **DEC-037** (DEC-020 formally CLOSED 2026-09-05); do not alter.
- Scene/campaign Location-Tier selection **not** — that is DEC-040.
- Anatomical mapping, Tier-1 coarse-zone ranges, Tier-2 subdivision **not** —
  those are DEC-041/DEC-042/DEC-100 (separate items).
- The W3 cache's *contents* are illustrative, not locked: at promotion,
  Structural Weak Points stands at State 2 (Established, Not Yet Resolvable) and
  zero entries sit at State 1. The cache remains a maintained shorthand, not an
  independent authority.
- DEC-019 (Structural Weak Points reclassification State 1 → State 2) is a
  **classification outcome recorded within the policy's cache**, not a separate
  mechanic; it is not independently promoted.
- Structural Weak Points and all other cache entries may be reclassified by
  future subsystem locks (S-3/S-5/S-7/S-10) without reopening this policy.

## B. Baseline principles (adopted from ChatGPT §2 — DEC-014 boundary)

1. **DEC-014 already locks the Tier-1 Location Index provider (Zero-Step).** It
   does **not** determine when a Location Index is warranted, scene/campaign Tier
   selection, anatomical mapping, or downstream consumption.
2. **DEC-017 must be treated as an invocation/warrant rule layered around the
   existing DEC-014 provider — not as a modification of Zero-Step.** The
   Zero-Step transformation remains governed exclusively by DEC-014.
3. **Non-attack Location Index generation is DEC-037** (DEC-020 closed), a
   separate rule chain; this promotion does not touch it.

## C. The 8 steps — current state (stop-and-confirm after every step)

| Step | Requirement | State | Authority-changing? | Status |
|---|---|---|---|---|
| 1 | Design question explicitly identified | **Done** — DEC-017 answers "when should Tiwas generate a Tier-1 Location Index (attack-side)" (D4 §2/§3/§8; D3 §2.1A) | No | **CONFIRMED by Tiwa 2026-09-05** |
| 2 | Competing alternatives considered | **Done** — four-state derived across v1–v5; alternatives recorded (D4; D3 §2.1A; conflict-register C3/C4) | No | **CONFIRMED by Tiwa 2026-09-05** |
| 3 | Simulation/analysis complete | **Done** — Named-Outcome Test 21/21 blind trial; 14 + 21 novel-case trials; Conceptual Anchor Challenge; E9 playtest | No | **CONFIRMED by Tiwa 2026-09-05** |
| 4 | Human designer accepts the ruling | **ACCEPTED by Tiwa 2026-09-05** — promotion authorized | **Yes** | **CONFIRMED** |
| 5 | Mechanic documented as a formal rule | **APPLIED 2026-09-05** — §14.7 block recorded in D3 §2.1A (non-canonical until Step 6) | Potentially | **CONFIRMED by Tiwa; executed** |
| 6 | Canonical Rules & Changelog updated | **APPLIED 2026-09-05** — v1.4 at `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`; §14.7 added, §14.3/§15/§17 updated; `sources/` copy verified unmodified | **Yes** | **CONFIRMED by Tiwa; executed** |
| 7 | Former proposal marked Superseded/Locked | **APPLIED 2026-09-05** — D3 §2.1A marked Superseded by Canonical §14.7 + §23 promotion line; D4 status header + §8 item 2 marked promoted; investigation preserved as historical record | **Yes** | **CONFIRMED by Tiwa; executed** |
| 8 | Implementation documentation updated | **APPLIED 2026-09-05** — Roadmap §4 row + §9 Phase 2 status; session briefs + snapshot; PROJECT_CONTEXT.md; decision register DEC-017 → §A (Canonical), DEC-018 note updated, DEC-019 left non-canonical | **Yes** | **CONFIRMED by Tiwa; executed** |

Per the designer-selected control model, **no step is recorded as
promotion-approved without explicit human confirmation of that step**, including
steps 1–3 (which are confirmations of evidence completeness rather than of
authority).

## D. GM-facing wording — light-review record and decision (DEC-A1: RULED — Option C)

**DEC-A1 ruling (2026-09-05, Tiwa):** **Option C** selected — Option A's
blockquote as the operative text, with the six explanatory clauses below
attached as **non-normative guidance**. The Named-Outcome Test is adopted
verbatim (unchanged) as the formal Warrant test. No new blind test required.

**Review basis:** D4 §5A / §8 item 3 — draft implementing a directionally-ruled
design decision; "not yet separately validated at the table — worth a light
review pass before being treated as final phrasing, though it does not require
another blind test to adopt provisionally."

**Light review performed (2026-09-05, opencode/big-pickle):**

- **Four-state consistency:** "already established under current Tiwas design"
  = anchored (States 1/2) vs. open fork (State 3); "current rules can actually
  resolve it" = State 1 vs. State 2. Consistent.
- **Named-Outcome Test consistency:** "distinct outcome beyond ordinary damage"
  mirrors the validated test's "distinct consequence, other than ordinary
  damage." Consistent.
- **Explicit-only boundary:** preserved in both incumbent wordings.
- **Exploitability scan:** no path found that grants a Warrant absent an
  explicit named distinct outcome; conditional/inferential objectives do not
  establish definiteness under either incumbent wording.
- **Cinematic framing:** ChatGPT's explicit clause ("the GM does not infer an
  unstated distinct objective from … cinematic framing alone") is consistent
  with D4's W3 cache note (cinematic/tonal framing rejected as a trigger
  category — context, not warrant) and makes that exclusion visible in the
  operational wording. **Recommended for inclusion.**
- **"actor" vs "player":** the §5A governing text was NOT itself blind-tested
  (only the Named-Outcome Test was, 21/21). For an attack-side rule, the actor
  may be a PC, NPC, or creature under the GM. Terminology choice is open
  (DEC-A1 below).

**DEC-A1 — Wording variant (decision required):**

| Option | Operative text | Source | Notes |
|---|---|---|---|
| **A** | "…only when **the actor** has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design (not merely plausible or anticipated), and current rules can actually resolve it." | v1.0 package | Minimal change; "actor" generality; keeps draft's parenthetical |
| **B** | "…only when **the player** has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design, and current Tiwas rules can actually resolve that location-dependent outcome." | ChatGPT §3.1 blockquote | "player" retained; parenthetical moved into clause 3; reworded tail |
| **C (SELECTED)** | Keep **Option A's blockquote** as the operative text, then attach the 6 explanatory clauses below (incl. cinematic framing) as non-normative guidance | Merge | Preserves validated-language discipline (Named-Outcome Test verbatim) while adding ChatGPT's clarity layer as explanation, not as rule text |

Proposed explanatory clauses (attach under the operative text if **Option C**
is chosen):

1. **Explicit objective:** the GM does not infer an unstated distinct objective
   from location, attack description, fictional context, or cinematic framing
   alone.
2. **Distinct outcome:** the stated objective must identify a consequence beyond
   ordinary damage and must be tied to the specified location.
3. **Established location-dependence:** location must already be an established
   delivery mechanism for that consequence under current Tiwas design; a merely
   plausible future use of location does not establish warrant.
4. **Current resolvability:** a Location Index is not generated merely because a
   location-dependent outcome has been conceptually established; a current Tiwas
   rule must also exist that can act on the resulting Location Index.
5. **No warrant:** if any required condition is absent, no Location Index is
   generated.
6. **Internal state preservation:** the four-state classification remains
   available for documentation and future subsystem work, even though the
   GM-facing procedure is the single operational test above.

**DEC-A1 settled (Option C):** the Named-Outcome Test is adopted verbatim
(unchanged) as the formal Warrant test; no new blind test is required for the
§5A wording. The six clauses above are **non-normative guidance** — they explain
the operative text, they are not substitute rule language.

## E. Step 5 — Formal rule text (draft, with W-gates)

**Designer rulings applied (2026-09-05):** W-gate structure **accepted**;
cinematic-framing exclusion **included**; DEC-014 layering principle **accepted**
(§B); non-attack reference **corrected to DEC-037**; §5A operative text = the
blockquote below (DEC-A1 Option C).

Proposed addition to the Canonical Rules & Changelog (§14, new subsection
**14.7 — Attack-side invocation / warrant**; scope-limitation amendment already
carried from D1 §14.3 list where applicable):

> ### 14.7 Attack-side invocation — when a Location Index is warranted
>
> **Status: Canonical / Locked — attack-side invocation policy.**
>
> For an attack-side resolution, a Tier-1 Location Index is generated **only
> when all three gates are satisfied** for one declared attack objective:
>
> | Gate | Requirement |
> |---|---|
> | W1 — Explicit Objective | The actor explicitly states a distinct consequence beyond ordinary damage |
> | W2 — Established Location-Dependence | Current Tiwas design establishes that the stated consequence is delivered through location (not merely plausible or anticipated) |
> | W3 — Current Resolvability | Current Tiwas rules provide a mechanism that can act on the resulting Location Index |
>
> `Generate(LocationIndex) = W1 ∧ W2 ∧ W3`. If any gate is false, no Location
> Index is generated. The Zero-Step transformation itself remains governed
> exclusively by §14.1–§14.2 (DEC-014).
>
> **GM-facing operational test.** In play this is a single question:
>
> > Generate a Location Index only when the actor has explicitly stated a
> > distinct outcome beyond ordinary damage, that outcome's location-dependence
> > is already established under current Tiwas design (not merely plausible or
> > anticipated), and current rules can actually resolve it.
>
> **Warrant test (Named-Outcome Test).** A declared objective is definite — and
> therefore Warrant-eligible — if and only if the actor explicitly names a
> distinct consequence, other than ordinary damage, whose resolution depends on
> the specified location. Purpose or motivation language does not by itself
> create definiteness; conditional phrasing does not defeat definiteness; only
> the presence of a named distinct outcome matters.
>
> **Explicit-only boundary.** The GM does not infer an unstated distinct
> objective from location, attack description, fictional context, or cinematic
> framing alone. Only stated objectives are Warrant-eligible.
>
> **Procedural riders.**
> 1. Compound objectives are evaluated disjunctively: if any named branch of a
>    multi-part declaration satisfies the Named-Outcome Test, Warrant is
>    established for that branch.
> 2. Stale objectives void the match: a Warrant is invalid if the fictional
>    state on record no longer supports the rationale for the named outcome.
> 3. S-1 winner-only: in an opposed contest, only the winning participant's
>    natural roll is eligible for Location Index generation (per §13.2; Quality
>    never alters either participant's historical roll).
> 4. Lazy evaluation: because Zero-Step is a read-only post-process of an
>    already-recorded roll (§14.2), Warrant/resolvability evaluation may be
>    deferred to the point a downstream stage first requires the answer.
>
> **Classification architecture.** For documentation and cache maintenance,
> concepts are classified: State 1 = Established & Resolvable (generate); State 2
> = Established, Not Yet Resolvable (do not generate; record as pending); State 3
> = Outcome Plausible, Location-Dependence Unresolved (do not generate); State 4
> = No Distinct Consequence (do not generate). This four-state scheme is an
> internal/documentation architecture; a GM applying the operational test above
> is not required to classify a case by state at the table.
>
> **Reference cache (W3).** Maintained shorthand for situations already
> established at State 1 or 2; it never independently establishes Warrant or
> Anchor status. Novel situations are always evaluated directly against the
> operational test and Named-Outcome Test. Cache contents may be revised by later
> subsystem locks without reopening this policy.
>
> **Exclusions carried.** This section governs attack-side invocation only.
> Non-attack physical resolutions are governed separately (DEC-037). It does not
> determine scene/campaign Location-Tier selection, anatomical mapping, Tier-1
> zone ranges, Tier-2 subdivision, or downstream wound/armour/defence/Effect
> interaction.

**Scope-limitation amendment to §14.3** (proposed): add to the existing "not
established by this ruling" list — "the attack-side invocation/warrant policy and
Named-Outcome Test (established by §14.7), and the non-attack Location Index
generation rule (separately governed)"; the remaining §14.3 bullets otherwise
stand. *(Clarified wording provided on confirmation.)*

## F. Step 6 — Canonical Rules & Changelog update (draft — NOT APPLIED)

**Requires human designer confirmation immediately before execution.**

### F.1 Canonical document revision

- `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` would be:
  - bumped to **v1.4** (header version and title block);
  - given a `last_modified_by_llm: {name: "opencode", version: "big-pickle"}`
    and `last_modified_date: "2026-09-05"` update;
  - §14 gains the new **14.7** subsection from §E;
  - §14.3, §15 Reserved Systems, and the §17 Changelog are updated per §F.2–§F.3;
  - the source copy `sources/tiwas-canonical-rules-and-changelog-v1.3.md` is left
    unmodified (preserved verbatim); the edited `canonical/rules/` copy diverges
    from it and is verified by diff.

### F.2 Reserved Systems (§15) revision

`hit-location rules, except the Tier-1 Zero-Step Location Index provider in
Section 14` → `hit-location rules, except the Tier-1 Zero-Step Location Index
provider (§14.1–§14.2) and the attack-side invocation/warrant policy (§14.7)`

### F.3 Changelog (§17) addition — the entry will identify:

- DEC-017; S-2 attack-side invocation/warrant policy; the formal rule text;
- promotion date (2026-09-05); the human designer acceptance;
- that no new blind test was required for the §5A wording;
- the relationship to DEC-014 (invocation layer, Zero-Step unchanged);
- explicit exclusions that remain unresolved (tier selection, mapping, Tier-2,
  downstream subsystems; non-attack governed by DEC-037).

> ## S-2 attack-side invocation v1.3 → v1.4
>
> 1. Locked the attack-side invocation/warrant policy: the W1/W2/W3 gate rule,
>    the GM-facing operational test, the Named-Outcome Test, the explicit-only
>    boundary and the four procedural riders (§14.7).
> 2. Locked the four-state classification as an internal/documentation
>    architecture for cache maintenance.
> 3. Locked the W3 reference-cache role as shorthand only, never an independent
>    authority.
> 4. Recorded that cache contents (e.g., Structural Weak Points at State 2) are
>    revisable by later subsystem locks without reopening this policy.
> 5. Preserved the broader S-2 architecture (tier selection, anatomical mapping,
>    zone ranges, Tier-2 subdivision) as unresolved.
> 6. Preserved the separate non-attack Location Index generation rule as
>    unchanged (DEC-037; DEC-020 formally closed 2026-09-05).

## G. Step 7 — Source marking (draft — applies only after step 6)

- **D3** `proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md` §2.1A
  header: replace `(Non-Canonical)` with
  `(Superseded by Canonical §14.7 — attack-side invocation locked 2026-09-05;
  remaining items below unchanged)` and add a one-line note after the GM-facing
  wording: `[Wording finalized and adopted provisionally 2026-09-05;
  superseded-in-place by Canonical §14.7 upon formal promotion.]`
- **D3** §23 revision record (v1.4.2 acceptance text): append a line recording
  the 2026-09-05 promotion and its DEC/register reference.
- **D4** `investigations/tiwas-s2-hit-location-investigation-v5-synthesis.md`
  status header: change `S-2 Candidate Policy — Accepted by designer ruling for
  further development/testing. NON-CANONICAL.` to add
  `Promoted to Canonical §14.7 (attack-side invocation) 2026-09-05; §5A wording
  finalized; synthesis otherwise retained as historical investigation record.`
- **D4** §8 item 2 status cell: `RULED — Accepted; attack-side invocation
  promoted to Canonical §14.7 2026-09-05; S-2's remaining architecture (tier
  selection, mapping, Tier-2) remains unlocked`.
- **Preservation (explicit):** the investigation is **not deleted**. It remains
  evidence of derivation, testing, alternatives, rejected approaches,
  evidentiary limitations, and provenance.

## H. Step 8 — Implementation documentation (draft)

### H.1 Documentation updates

| Area | Action |
|---|---|
| Roadmap (D2, `roadmap/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` §4 S-2 row) | Invocation cell → "attack-side invocation/warrant policy — **Locked (Canonical §14.7)**; tier selection, anatomical mapping, Tier-2 subdivision remain Open"; dependency marked resolved/promoted |
| Snapshots/briefs (`Tiwas-Session-Brief-2026-08-31.md`, `Tiwas-Advisory-Session-Brief-2026-08-31.md`, `Tiwas-Task-Scoped-Snapshot-2026-09-02.md`) | DEC-017 rows → "Promoted to Canonical §14.7 (2026-09-05)" |
| `PROJECT_CONTEXT.md` | DEC-017 status → promoted |
| **Decision register** (`_consolidation/decision-register.md`) | Move DEC-017 to §A (Canonical); DEC-018 note updated; DEC-019 left non-canonical |
| Proposal (D3) | Mark promoted material Superseded (§G) |
| Investigation (D4) | Preserved; promoted outcome identified (§G) |
| Canonical changelog | Promotion recorded (§F.3) |

### H.2 Regression / acceptance cases (adopted from ChatGPT §11)

At minimum, implementation verification should cover:

1. Explicit named consequence + established location-dependence + resolvable →
   Generate.
2. No named consequence → Do not Generate.
3. Location-dependence unresolved → Do not Generate.
4. Established but not currently resolvable → Do not Generate.
5. Compound objective → qualifying branch evaluated independently.
6. Stale objective → no warrant.
7. S-1 loser roll → not eligible.
8. Zero-Step remains a read-only transformation of the eligible natural roll.

## I. Step control protocol (designer-selected: stop-and-confirm after every step)

> **Do not execute more than one step from this package without explicit human
> confirmation of that step.** Read-only verification may precede each
> confirmation, but approval must never be inferred from a previous approval,
> the existence of DEC-017, repetition in documentation, an LLM recommendation,
> implementation convenience, or apparent consistency.

```text
Step 1 → STOP → Human confirmation
Step 2 → STOP → Human confirmation
Step 3 → STOP → Human confirmation
Step 4 → STOP → Human confirmation
Step 5 → STOP → Human confirmation
Step 6 → STOP → Human confirmation
Step 7 → STOP → Human confirmation
Step 8 → STOP → Human confirmation
```

Current position: **All 8 steps CONFIRMED by Tiwa and executed (2026-09-05).**
DEC-017 is Canonical §14.7 (Canonical Rules & Changelog v1.4). The
stop-and-confirm protocol is complete; every step was explicitly confirmed
before execution. **Promotion COMPLETE.**

## J. Decision record (all ruled by Tiwa, 2026-09-05)

1. **DEC-A1 — §5A wording variant: RULED — Option C** (Option A blockquote +
   six clauses as non-normative guidance). §D applied.
2. **Step-control model — DECIDED**: stop-and-confirm after every step (§I).
3. **W-gate formal structure (W1∧W2∧W3): ACCEPTED** (§E).
4. **Cinematic-framing exclusion clause in §14.7: INCLUDED** (§E).
5. **DEC-014 layering principle: ACCEPTED** (§B).
6. **Non-attack reference correction (DEC-037, not DEC-020): ACCEPTED**
   (throughout).
7. **Step 6 mechanics — v1.4 bump; `sources/` copy verbatim: ACCEPTED** (§F.1).
8. **Step 8 regression cases + decision-register move: ACCEPTED** (§H).
9. **Step sequence — begin at Step 1 confirmation.** <sup>next action</sup>

All package content is now decided. **Current position: Step 1 presented below
for confirmation; no step yet confirmed.**

## K. Standing limitations

- Nothing in this package promotes any other S-2 or adjacent item. DEC-018
  (explicit-only) is promoted only as a component of §14.7; DEC-019's State-2
  classification is a cache-content record, not a promoted mechanic. All other
  decisions remain non-canonical.
- The package itself is a working record and does not establish authority.
- The broader S-2 architecture and the entire non-attack chain (DEC-037) remain
  non-canonical per their own records.
- No Canonical file is modified merely by receiving this package.