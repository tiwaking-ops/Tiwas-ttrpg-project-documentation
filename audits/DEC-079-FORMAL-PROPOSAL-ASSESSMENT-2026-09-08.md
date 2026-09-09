---
document:
  title: "Assessment — DEC-079 Conditions: Numeric Tier Assignment and Action-Denial Interaction Resolution Proposal (DEC-079-CLOSURE-PROPOSAL-001)"
  version: "1.0"
  status: "Assessment record — read-only analytical review of a non-canonical proposal"
  provenance:
    author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
    assessor_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
    last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
    created_date: "2026-09-08"
    last_modified_date: "2026-09-08"
  scope: >
    Technical consistency analysis of DEC-079-CLOSURE-PROPOSAL-001 against the
    repository's existing decision register, canonical rules, and governance model.
    This is a read-only analytical activity and does not modify any document's
    authority status.
  target_document:
    title: "Tiwas — DEC-079 Conditions: Numeric Tier Assignment and Action-Denial Interaction Resolution Proposal"
    file: "DEC-079 Conditions — Formal Resolution Proposal.md"
    proposal_id: "DEC-079-CLOSURE-PROPOSAL-001"
    author: "GPT-5.6 Luna"
    date: "2026-09-08"
---

# Assessment — DEC-079-CLOSURE-PROPOSAL-001

## 1. Scope and Method

This assessment evaluates the technical consistency and architectural soundness of
the DEC-079 formal resolution proposal against:

- the existing decision register (`_consolidation/decision-register.md`, DEC-001
  through DEC-133);
- the canonical rules (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`,
  v1.4);
- the governance model (`governance/authority.md`, `governance/status-model.md`,
  `governance/provenance.md`);
- the 18 Core Architectural Invariants (DEC-016 / Canonical Rules §16).

The assessment is **read-only analytical work** and does not constitute promotion,
canonicalisation, or any authority-changing action. The proposal remains
**Non-Canonical — Pending Human Designer Ruling**.

---

## 2. Executive Assessment

**Overall verdict: TECHNICALLY SOUND. No conflicts found against the existing
decision register or canonical rules. The proposal is architecturally consistent
with the established Effect Tier Magnitude System and does not introduce
unauthorised mechanics.**

The proposal demonstrates strong governance awareness, correctly identifies its own
non-canonical status, and explicitly declines to imply promotion. The analytical
structure is thorough: constraint list is complete, consistency analysis covers all
major referenced DECs, and the proposed formal rule text is cleanly scoped.

---

## 3. Technical Validity — Detailed Findings

### 3.1 Numeric Tier Assignment (Proposal A)

**Verdict: CORRECT and consistent with existing architecture.**

The proposal's central claim — `Condition Tier = Skill-Tier of the causing Effect's
Skill` — is not new. It is the direct application of the already-established
Effect Tier Magnitude System (DEC-127 naming) to Condition instances.

**Chain of authority:**

1. DEC-107 established: `Effect Tier = Skill-Tier of the skill used`. This
   superseded DEC-035.B's Quality-ceiling model for Effect/Wound Tier assignment.
2. DEC-079 C2/C3 are explicitly cited by DEC-107 as preserved — the `Z = −Y`
   magnitude formula and the Skill-Tier ≥ 2 production gate remain operative.
3. DEC-115 unified Effect and Condition records into one schema (`Type / Tier Y /
   Magnitude Z / optional Location X`), confirming that Condition records use the
   same Tier/Magnitude semantics as Effect records.
4. DEC-127 names this the "Effect Tier Magnitude System" and explicitly states:
   "the Effect's Tier is the Skill-Roll Tier."

The proposal therefore correctly reads the existing architecture as already
determining Condition Tier from the causing Skill-Tier. It proposes no new
mechanism — it closes an open interpretive question by deferring to established
authority.

**Assessment of the rejected alternatives:**

| Rejected option | Reason | Assessment |
|---|---|---|
| Fixed Tier per Condition identity | Creates arbitrary second severity system | Correctly rejected — would contradict DEC-107's Skill-Tier basis |
| Condition Tier = Effect Quality | Superseded by DEC-107 | Correctly identified as historically superseded |
| Condition Tier = target-stat value for all Conditions | Confuses DEC-122 Y-source with record Tier | Correctly rejected — DEC-122's movement overlay Y is query-time-live and distinct from the record's originating Tier |

All three rejections are well-founded.

### 3.2 Movement Y-Source Distinction (Section 6)

**Verdict: CORRECT and architecturally critical.**

The proposal correctly identifies that `Y` is overloaded in the existing architecture:

- **Condition record Tier Y:** caused by the producing Effect's Skill-Tier
  (causing-Skill-Tier Y-source, DEC-107);
- **Movement-denial overlay Y:** the target's current Movement Speed at query time
  (target-stat-value Y-source, DEC-122, query-time-live).

These are two different Y-sources. The proposal correctly refuses to collapse them
into a single formula. This is consistent with DEC-122's own explicit naming of the
"target-stat-value" pattern as a distinct Y-source.

**Documentation recommendation:** The proposal's suggestion to explicitly label the
Y-source in rule text is practical and would prevent misreading of DEC-122 as
modifying the Condition's actual Tier. This is a documentation-level recommendation,
not a mechanical change.

### 3.3 Same-Condition Stacking (Proposal B)

**Verdict: CORRECT. Preserves existing Condition-specific rules.**

The proposal correctly declines to replace individual Condition stacking rules with a
universal stacking rule. The existing alpha vocabulary already defines stacking
behaviour per Condition:

- Encumbered: same-tier add; higher replaces
- Grappled: highest tier only
- Restrained: same-tier add; higher replaces
- Prone: highest tier only
- Stunned: highest tier
- Incapacitated: highest tier

These are heterogeneous — some use additive stacking, some use replacement. A
universal "highest Tier wins" or "all Tiers add" rule would contradict existing
decisions. The proposal's preservation of Condition-specific rules is correct.

### 3.4 Different Action-Denial Conditions — Scope Union (Proposal C)

**Verdict: SOUND. The scope union model is the cleanest resolution available.**

The proposal's core insight is that different Condition identities represent
different mechanical scopes, and their interaction should be resolved by evaluating
those scopes rather than by numeric Tier comparison.

**Why scope union is correct:**

1. **Incapacitated + Stunned:** Incapacitated's active-resistance denial is broader
   (all active resistance) than Stunned's (Body/Speed resistance only). Under scope
   union, the broader restriction naturally subsumes the narrower overlapping
   restriction. Both records remain active; no deletion or counter occurs.

2. **Stunned + Restrained:** These impose distinct restrictions (action/resistance
   denial vs. movement/body-skill restriction). Under scope union, both apply
   independently. No conflict arises because their scopes are orthogonal.

3. **No new engine required:** Scope union is a logical operation (set union of
   applicable restrictions), not a numerical stacking engine. It requires no new
   fields, no priority table, and no counter relationships.

**Rejected alternatives are correctly excluded:**

| Rejected approach | Problem | Assessment |
|---|---|---|
| Tier addition between Conditions | Creates new numerical stacking engine; produces severity neither Effect created | Correctly rejected |
| Highest Tier always wins | Destroys distinct Condition scopes; e.g. Tier-5 Stunned would erase Tier-2 Incapacitated despite Incapacitated being semantically broader | Correctly rejected |
| Global precedence hierarchy | Unnecessary; creates maintenance burden; creates false conflicts between non-competing Conditions | Correctly rejected |
| Counter Stunned with Incapacitated | Over-suppresses StateRecord; removes information; stronger than necessary | Correctly rejected — DEC-117 counters are explicit filters, not general resolution tools |

### 3.5 DEC-123 Integration

**Verdict: CORRECTLY INCORPORATED.**

DEC-123 established that Stunned/Incapacitated/Restrained characters may declare
and roll a test (guaranteed to fail via Effective Skill 0), and the complete Core
Test Transaction remains operative. The proposal correctly incorporates this:

- Character may declare test (GM Fiat permitting)
- Applicable Condition restrictions apply (Effective Skill = 0 via DEC-122
  self-referential-Y)
- Roll proceeds through full Core Test Transaction
- Cost paid, Overflow risk, Failure XP generated, Double-Trigger qualified

The proposal correctly notes this does not reintroduce categorical action
prohibition. DEC-123's "never total" principle is preserved.

### 3.6 Counter Rejection

**Verdict: CORRECT.**

The proposal correctly rejects using DEC-117 counters to resolve ordinary
action-denial overlap. DEC-117 R3 defines counters as:

> "If a target has a StateRecord whose `id` is in another record's `counters` list,
> the countered record's effects do not apply to that target."

If Incapacitated countered Stunned, the entire Stunned StateRecord would be
suppressed — including any distinct restrictions not overlapping with Incapacitated.
The scope union model is more precise: both records remain, overlapping restrictions
produce no additional effect, and distinct restrictions remain active.

---

## 4. Constraint Compliance

The proposal identifies 14 design constraints (C-01 through C-14). Assessment:

| Constraint | Status | Notes |
|---|---|---|
| C-01: No second Condition-specific Tier engine | SATISFIED | Scope union is a logical operation, not a Tier engine |
| C-02: Preserve Z = −Y | SATISFIED | Explicitly preserved throughout |
| C-03: Preserve DEC-107 Skill-Tier basis | SATISFIED | Proposal A directly applies DEC-107 |
| C-04: Preserve DEC-122 movement-denial architecture | SATISFIED | Y-source distinction maintained |
| C-05: Preserve DEC-123 never-total action declaration | SATISFIED | Section 13 explicitly incorporates DEC-123 |
| C-06: Preserve full Core Test Transaction | SATISFIED | Core Test Transaction flows unchanged |
| C-07: No new resource pool | SATISFIED | No pools introduced |
| C-08: No modification to natural d100 | SATISFIED | d100 mechanics untouched |
| C-09: No generic Tier addition | SATISFIED | Tier addition between Conditions explicitly rejected |
| C-10: No unnecessary new StateRecord fields | SATISFIED | No new fields proposed |
| C-11: Preserve distinct Condition identities | SATISFIED | Condition Identity ≠ Condition Tier explicitly stated |
| C-12: Preserve Incapacitated > Stunned semantic distinction | SATISFIED | Subsumption model preserves this without numeric hierarchy |
| C-13: Preserve existing Condition-specific stacking rules | SATISFIED | Proposal B explicitly preserves per-Condition rules |
| C-14: Avoid converting DEC-117 counters into general precedence engine | SATISFIED | Counters explicitly rejected as resolution mechanism |

**All 14 constraints satisfied.**

---

## 5. Consistency with Referenced Decisions

### 5.1 Decisions cited as preserved

| DEC | Claimed status | Verification |
|---|---|---|
| DEC-001–017 | No conflict | **Confirmed.** Proposal does not modify d100, Skills, Attributes, Core Test Transaction, Overflow, Failure XP, Advanced Skills, Recovery, S-1, S-2 |
| DEC-007.A | Preserved | **Confirmed.** No Condition may modify Overflow (reinforced by DEC-117) |
| DEC-107 | Preserved and relied upon | **Confirmed.** Proposal A directly applies DEC-107's Skill-Tier basis |
| DEC-115 | Preserved | **Confirmed.** No new record field required |
| DEC-117 | Preserved | **Confirmed.** Counter rule not repurposed |
| DEC-122 | Preserved | **Confirmed.** Movement overlay Y-source distinguished from Condition Tier Y |
| DEC-123 | Preserved | **Confirmed.** Action declaration fully incorporated |
| DEC-126 | Preserved | **Confirmed.** "Helpless" not assigned mechanical meaning |
| DEC-127 | Preserved | **Confirmed.** Proposal directly applies the named Effect Tier Magnitude System |

### 5.2 Decisions not cited but potentially relevant

| DEC | Relevance | Assessment |
|---|---|---|
| DEC-121 | Tier-mutation via qualifying Skill Test (Heal Effect System) | **No conflict.** Condition Tier assignment at creation (this proposal) is independent of removal via DEC-121 Tier-mutation. The Skill-Tier ≥ Condition-Tier removal gate (DEC-035.A cl.5) operates on the Condition's assigned Tier, which this proposal defines. |
| DEC-128/129 | Item Tier/Magnitude (Z = Y, not Z = −Y) | **No conflict.** DEC-128 explicitly places Item Tier/Magnitude outside the DEC-115/117 unified StateRecord schema. Items are not Conditions. |
| DEC-130 | GM Fiat bounded universality | **Consistent.** The proposal correctly references GM Fiat as a universal override. DEC-130's bounds (Locked Canonical Core exceptions) do not interact with this proposal. |
| DEC-132 | Reactions beyond Active Defense | **No interaction.** Reactions are tag-gated out-of-turn Core Tests. Condition interaction with reactions is not within this proposal's scope. |

---

## 6. Identified Gaps and Edge Cases

These are not flaws in the proposal but areas where the human designer may wish to
consider additional clarity during adoption.

### 6.1 Same-dimension Condition interaction beyond action denial

The proposal's scope union model (Section 17) distinguishes between "same mechanical
dimension" and "different mechanical dimensions" but focuses primarily on
action-denial Conditions. The interaction between Conditions that share a mechanical
dimension but have different stacking rules is not fully explored.

**Example:** Encumbered (same-tier add; higher replaces) + Slowed (worse penalty
applies, per the alpha vocabulary). Both affect Movement Speed. Under scope union,
which rule governs? The proposal preserves existing per-Condition rules but does not
explicitly address the case where two different Conditions impose overlapping
restrictions on the same stat with different stacking semantics.

**Assessment:** This is likely resolvable through content-level adjudication (the
existing rules already handle Encumbered + Slowed as a special case). But if the
proposal is adopted, the designer may wish to confirm whether the scope union model
extends to non-action-denial Condition overlaps or remains confined to action-denial
as presented.

### 6.2 Multiple instances of the same Condition at different Tiers

The proposal correctly notes that same-Condition stacking uses existing
Condition-specific rules (e.g., "highest tier only" for Stunned). However, the
removal interaction is not explicitly addressed: if a character has Tier-5 Stunned
and Tier-3 Stunned, and the Tier-5 instance is healed via DEC-121 Tier-mutation to
Tier-3, does the character now have two Tier-3 Stunned instances, or does the
healed instance merge with or replace the existing one?

**Assessment:** This is a content-level detail that the existing Condition-specific
stacking rules may already resolve (e.g., "highest tier only" implies only one
instance is operative). But it is not explicitly addressed in this proposal.

### 6.3 Condition Tier and removal difficulty

The proposal defines Condition Tier as the causing Skill-Tier. The Heal Effect
System (DEC-035.A cl.5 / DEC-121) gates removal by `Skill-Tier ≥ Condition Tier`.
This means a Tier-5 Condition requires a Tier-5+ Skill to remove — which is
correct and consistent. However, the proposal does not explicitly discuss this
implication.

**Assessment:** The implication is correct and consistent with the existing
architecture. No action needed, but the designer may wish to confirm this is the
intended removal-difficulty behavior.

### 6.4 Scope union — complete exhaustion not claimed

The proposal's action-denial resolution matrix (Section 12) covers the primary
action-denial Conditions (Stunned, Incapacitated, Restrained, Grappled, Prone) but
does not claim to exhaust all possible Condition interactions. This is appropriate —
the proposal resolves the specific DEC-079 open questions rather than attempting to
codify a universal Condition interaction manual.

**Assessment:** Correct scoping. Additional Condition interactions (e.g., Blinded +
Deafened, Poisoned + Sickened) remain content-authoring under DEC-077.A.

---

## 7. Governance Compliance

### 7.1 Self-declared status

The proposal correctly declares:
- Status: "Non-Canonical — Pending Human Designer Ruling"
- Authority: "Proposal only; does not modify Canonical Rules or the Decision Register"
- Canonical status: "No promotion implied by this proposal"

**Assessment:** The proposal is governance-literate and does not attempt to
self-execute any authority change. This is consistent with the repository's LLM
Governance Rules (governance/status-model.md §24).

### 7.2 Promotion path

If the human designer adopts this proposal, the governance action required is:

1. **Designer ruling** — Tiwa explicitly accepts or rejects the proposal
2. **Decision register entry** — the adoption is recorded as a new DEC (or as
   amendments to DEC-079)
3. **No silent rewrite** — DEC-079 should not be rewritten without explicit governance
   action
4. **No premature promotion** — adoption as a designer ruling does not constitute
   canonical promotion; the 8-step Promotion Rule (status-model.md §21) would
   additionally require formal documentation and Canonical Rules update

The proposal correctly identifies this governance path in Section 22.

### 7.3 Provenance

The proposal attributes authorship to GPT-5.6 Luna and identifies its source basis.
This is consistent with `governance/provenance.md` requirements.

---

## 8. Risk Assessment

### 8.1 Low risk: Scope union introduces ambiguity

**Risk:** The scope union model requires judgment about which restrictions are
"the same" versus "different" — e.g., is Stunned's attack penalty the same
restriction as Restrained's attack penalty, or different?

**Mitigation:** The existing Condition-specific vocabulary already defines each
Condition's mechanical effects. Scope union evaluates those defined effects; it does
not create new ones. The GM adjudicates edge cases via GM Fiat (DEC-130).

**Level: LOW.** The existing architecture already requires GM adjudication for
Condition interactions.

### 8.2 Low risk: Y-source documentation burden

**Risk:** The proposal recommends explicit Y-source labeling in rule text. If not
adopted as a documentation convention, the Y-overloading problem persists.

**Mitigation:** Even without explicit labeling, the architectural distinction is
already established by DEC-107/DEC-122/DEC-127. The risk is misreading, not
mechanical error.

**Level: LOW.** Documentation improvement, not a mechanical gate.

### 8.3 No risk: No architectural conflicts

**Risk:** None identified. The proposal does not modify any existing DEC, does not
introduce new mechanics, and does not conflict with any Core Architectural Invariant.

---

## 9. Recommendation

**The proposal is technically sound, architecturally consistent, and governance-
compliant. It should be presented to the human designer for adoption or rejection
through the project's formal governance process.**

The two proposed resolutions are:

1. **Condition Tier = causing Skill-Tier** (subject to existing rules) — closes the
   numeric Tier open question by applying already-established architecture. This is
   not a new mechanism.

2. **Scope union for different-Condition interaction** — resolves the action-denial
   overlap problem without introducing a second hierarchy engine. The model is
   clean, extensible, and consistent with the existing design direction.

Both recommendations are well-founded and correctly avoid the architectural pitfalls
of the rejected alternatives (fixed tiers, numeric addition, global precedence
hierarchy, counter-based resolution).

---

## 10. Recorded Observations

This assessment is a **read-only analytical activity** performed by
opencode/big-pickle. It does not:

- modify any document's authority status
- promote the proposal to canonical
- amend DEC-079 or any other decision
- create or modify any governance record

The proposal remains **Non-Canonical — Pending Human Designer Ruling** pending
Tiwa's explicit adoption or rejection through the project's governance process.

---

*Recorded by opencode/big-pickle, 2026-09-08.*
