# Tiwas S-2 Design Investigation v5 — Non-Canonical Synthesis

**Status: S-2 Candidate Policy — Accepted by designer ruling for further development/testing. NON-CANONICAL. S-2 remains unlocked per Canonical §14.3. Cannot modify Canonical Rules under any circumstance; may inform Proposals/WIP and Roadmap updates per §11 (added below).**

**Designer rulings recorded this revision:**
- **Explicit-only objectives — RULED.** The GM does not infer a distinct mechanical objective from location, description, or fictional context alone; the player must state the distinct consequence. Formerly §8 item 1 ("Open"); reclassified below as a Designer Ruling, not an empirical finding.
- **This synthesis — ACCEPTED** as the current non-canonical S-2 candidate policy. Not a lock. Subject to revision if S-3/S-5/S-7/S-10 design work, the still-open non-attack-resolution scope question, or future evidence materially changes it.
**Supersedes (as a synthesis only, not as a record):** consolidates findings from v1–v4 and the six-round interactive investigation (falsification test, two blind table-practice tests, the Declared Objective Boundary Test, and the Conceptual Anchor Challenge). Those documents/rounds remain the evidentiary record; this document is the proposed policy built from them.
**Not touched:** Zero-Step derivation mechanics (Canonical §14.1–§14.2, locked, not reopened), S-1 (locked, not reopened), anatomical mapping, Tier-2 mechanics, and all S-3/S-4/S-5/S-7 numerical rules.

---

## 1. What This Document Is and Isn't

This is a **proposed answer to the open half of S-2** — the invocation/warrant policy that Canonical Rules §14.3 explicitly leaves unresolved. It is built entirely from the investigation record: two falsification rounds, two independent blind table-practice trials (14 items, then 21 items), and a document-grounded conceptual challenge. It does not, by itself, lock anything. Adoption requires your explicit ruling, and even then only Proposals/WIP and the Roadmap update — Canonical Rules change only through the eight-step promotion process already defined there (Proposals §21).

---

## 2. Core Policy — The Four-State Model

**[Design inference, synthesized from the full investigation]** Every resolution that could plausibly involve a physical impact is classified into exactly one of four states:

| State | Definition | Generate Location Index? |
|---|---|---|
| **1 — Established & Resolvable** | Location-dependence is conceptually anchored (not contingent on an unmade design choice) **and** current Tiwas rules provide a mechanism to act on the result | **Yes** |
| **2 — Established, Not Yet Resolvable** | Location-dependence is anchored, but no current rule can act on the result yet | **No** — record as a pending dependency |
| **3 — Outcome Plausible, Location-Dependence Unresolved** | The named consequence itself is a reasonable future Tiwas outcome, but whether *location specifically* is the mechanism that delivers it is an open design question, not merely an unimplemented one | **No** — do not treat as warranted; this is not a subsystem-completeness gap, it's an unmade design fork |
| **4 — No Distinct Consequence** | The declared action names no consequence beyond ordinary damage, or names none at all | **No** |

**[Architectural constraint, carried through every round of this investigation]** State 3 must never be quietly merged into State 2. Round 5's Conceptual Anchor Challenge exists specifically because the earlier cache draft (v4) had done exactly that — treating "Disarm is a plausible outcome" as equivalent to "location is how Disarm gets triggered," when the documents themselves (Proposals §3.2, §5) support at least one fully plausible alternative (Margin/Tag-gated triggering) that doesn't reference location at all.

---

## 3. The Warrant Test — Named-Outcome Rule

**[Empirical finding, single-designer trial, 21/21 consistent]**

> A declared objective is **definite** — and therefore Warrant-eligible — if and only if the player explicitly names a distinct consequence, other than ordinary damage, whose resolution depends on the specified location. Purpose or motivation language ("to really hurt him," "to get through his defenses") does not by itself create definiteness unless the named result is itself distinct from ordinary damage. Conditional phrasing ("if I get the chance...") does not defeat definiteness; only the presence or absence of a named distinct outcome matters.

This closes both confirmed cross-round instabilities (the armor-gap divergence and the conditional-objective divergence) — both were shown to be instances of the same underlying variable (definiteness of named outcome), not two separate problems.

---

## 4. Conceptual Anchor — Prerequisite to Warrant

**[Design inference, tested against source documents via the Conceptual Anchor Challenge, not against blind-trial data]**

> A named outcome's location-dependence is **anchored** if the Tiwas design documents do not contain a stated or clearly plausible alternative mechanism (e.g., Margin/Quality threshold, Tag-gated trigger) that would deliver the same outcome without reference to struck location. It is **unanchored** if such an alternative exists in the documented design space, whether or not that alternative is the one eventually chosen.

| Concept | Anchor status | Basis |
|---|---|---|
| Structural destruction (hinges, supports, weak points) | **Anchored** | No subsystem dependency at all; resolvable through ordinary physical narration today |
| Disarm / Break Hold | **Unanchored** | Proposals §3.2 explicitly contemplates Margin/Quality-band and Tag-gated Effect triggering as alternatives to location |
| Equipment damage | **Unanchored** | Same basis as Disarm |
| Function impairment (blindness, movement) | **Unanchored** | Conditions (§10) have no stated activation mechanism; nothing ties them to location specifically |
| Armor bypass | **Unanchored, most strongly** | Proposals §5 states the *actual current design direction* is Tag/Trait-based, not location-based — this is textual contradiction, not mere silence |
| Incapacitation / kill | **Unanchored, circularly** | Proposals §4.1/§7 condition localized injury mattering on locations already being active — S-7's own language depends on this S-2 decision, not the reverse |

**[Recommendation]** Only Structural Destruction currently qualifies for State 1 or State 2. Everything else in this table sits in **State 3** until the relevant future subsystem (S-3, S-5, S-7, S-10) makes an explicit design choice that location is the delivery mechanism — at which point, and only then, it may be re-evaluated for promotion to State 2.

---

## 5. Procedural Rules (Confirmed Across Multiple Rounds)

**[Empirical finding, replicated / [Architectural constraint], as marked]**

| Rule | Basis |
|---|---|
| **Compound objectives** are evaluated disjunctively — if any named branch of a multi-part declaration satisfies the Named-Outcome Test, Warrant is established for that branch, regardless of how the rest of the declaration reads | Confirmed twice (Round 1 #9-analog, Round 3 #15) |
| **Stale objectives void the match** — a category or Named-Outcome match is invalid if the fictional state on record no longer supports its rationale (e.g., declaring a disarm against an already-empty hand) | Confirmed (Round 1 #5, Round 2 #10) |
| **S-1 winner-only** — in an opposed contest, only the winning participant's natural roll is ever eligible for Location Index generation; per Canonical §13.2, Quality never alters either participant's historical roll, and the losing roll has no consumer for a Location Index under any current or proposed rule | Confirmed (Round 1 #10, Round 2 #11) — [Architectural constraint, Canonical §13.2] |
| **Lazy evaluation** — because Zero-Step is a read-only post-process of an already-recorded natural roll (Canonical §14.2), Warrant/Resolvability evaluation does not need to occur at declaration time; it may be deferred to whenever a downstream stage first requires the answer | [Design inference, Phase 2 finding D, not separately stress-tested at the table] |
| **Explicit-only objective boundary** — the GM does not infer an unstated distinct objective from location or fictional context alone; only stated objectives are Warrant-eligible | **[Designer ruling.]** Tested cleanly (21/21, Round 3, including the #16/#17 minimal pair); adopted by explicit designer decision, not derived from the test result alone |

---

## 5A. GM-Facing Procedure (Simplified) vs. Internal Architecture

**[Design inference, incorporating designer guidance this revision]** The four-state model in §2 is retained as the **internal/documentation architecture** — it explains *why* a given case resolves the way it does, and it is what the Anchor Challenge and the cache in §6 are built from. It is **not** intended as something a GM consciously walks through at the table. Per the second blind test's own result (`Generate = Warrant ∧ Resolvable`, holding exactly across all 14 trial cases with no independent third judgment needed at the point of play), the GM-facing rule collapses to one question:

> **Generate a Location Index only when the player has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design (not merely plausible or anticipated), and current rules can actually resolve it.**

Conceptual Anchor (§4) does real work in *determining* whether a given category's location-dependence counts as "already established," but a GM applying the rule in play is not asked to separately classify something as "State 3" — that classification work is front-loaded into which entries the W3 cache (§6) is allowed to contain. This keeps the table-facing rule to a single test while preserving the more careful internal distinctions that produced it. **This wording is a draft implementing the designer's stated direction, not yet separately validated at the table** — worth a light review pass before being treated as final phrasing, though it does not require another blind test to adopt provisionally.

---

## 6. W3's Role — Reference Layer, Not Independent Authority

**[Design inference, corrected from v4's original framing]** The investigation's early rounds treated W3 as a semi-independent gate ("Active cache entries authorize generation"). The evidence no longer supports that. Round 3's novel-instantiation cases (#8, #12 — a lantern-and-support-beam and a castle-wall breach, neither a verbatim cache entry) generated correctly by applying the *underlying* four-state test, not by cache lookup. **W3's corrected role: a maintained shorthand recording situations for which States 1 or 2 have already been established by the policy above, so recurring cases don't require re-deriving the answer from scratch at the table.** It never establishes Warrant or Anchor status on its own authority.

### Current cache (revised, honest framing per your approval)

| Category | State | Notes |
|---|---|---|
| Structural weak points (hinges, supports, load-bearing components) | **1 (Established & Resolvable)** | Only fully secure Active entry |
| Disarm | **3** | Outcome plausible; location-mechanism unresolved (§4) — not cache-eligible as a warrant until S-3 makes a locational design choice |
| Equipment damage | **3** | Same |
| Function impairment | **3** | Same |
| Armor bypass | **3, most firmly** | Directly contradicted by current design direction (§5) |
| Incapacitation/kill | **3, circularly** | Cannot be resolved independently of this S-2 decision |
| Bare called shots, no named outcome | **4** | Rejected consistently, all rounds |
| "Formal duel" as bare category | **Rejected pattern** | Location-dependence must attach to the duel's stated win condition, not duel status itself |
| Cinematic/tonal framing as a trigger or suppressor | **Rejected as a category; correctly treated as context, not warrant** | Confirmed — tonal framing never overrode the four-state test in trial data |
| Uniform-consequence hazards | **4** | No location-dependent branching by design |

---

## 7. Open Scope Gap — Not Resolved Here

**[Unresolved, carried forward, not solved by this synthesis]** Zero-Step's canonical wording (§14.1) is built around "the attacker's natural d100 roll," which presumes an adversarial impact. Non-combat physical resolutions (the rope-bridge fall, tested twice, State 3 both times on independent grounds) expose that hazards and similar non-attack physical events have no natural "attacker" whose roll Zero-Step consumes. This synthesis does not resolve **whose roll, if any, supplies the Location Index for a non-attack physical resolution** — that remains open and should be treated as a distinct, narrower question for a future investigation, not folded into the warrant policy above.

---

## 8. Designer Decisions — Ruled and Still Open

| # | Decision | Status |
|---|---|---|
| 1 | Explicit-only vs. inferred objectives | **RULED — Explicit-only** (this revision) |
| 2 | Whether this synthesis is accepted as the current S-2 candidate | **RULED — Accepted, non-canonical, S-2 remains unlocked** (this revision) |
| 3 | GM-facing presentation of the four-state model | **Directionally ruled — retain four states internally, simplify to one operational question for the table (§5A).** Exact wording in §5A is a draft implementing that direction, not yet separately validated; a light review pass is worth doing before treating the phrasing as final, but this does not block adoption or require another blind test |
| 4 | Whose roll supplies a Location Index for non-attack physical resolutions (§7) | **Open** — flagged by both parties as a separate, narrower rules-architecture question, not a playtest question |
| 5 | Whether/when State-3 entries (Disarm, Equipment, Impairment, Armor Bypass, Incapacitation) should be revisited | **Open**, dependent on S-3/S-5/S-7/S-10 locking a *location-specific* mechanism, not merely locking numbers |
| 6 | Multi-GM usability validation beyond the current single-evaluator record (two trials, 35 scenario-responses) | **Open, optional** — not required to understand what the rule means, per the investigation's own established framing; may be pursued later if desired |

---

## 9. Acceptance Tests (If Adopted)

In the style of Roadmap §9's existing S-2 acceptance criteria, extended:

- The Named-Outcome Test correctly separates bare location narration from stated distinct consequences (validated, 21/21, single trial).
- Conditional phrasing does not defeat definiteness (validated).
- Compound objectives are evaluated disjunctively (validated, two independent instances).
- Stale objectives void an otherwise-matching category (validated, two independent instances).
- Only the S-1 contest winner's roll is eligible for Location Index generation (validated, two independent instances; grounded in Canonical §13.2).
- No State-3 concept generates a Location Index under the current ruleset, regardless of how plausible or frequently-declared (validated by construction, cross-checked against Proposals §3.2/§5).
- Novel, uncached structural cases correctly resolve via the underlying test rather than requiring cache membership (validated, two independent novel instances).

---

## 10. Governance Impact If You Approve This

**Canonical Rules:** No change. §14.3 remains open exactly as written; this document does not claim to close it, only to propose an answer.

**Proposals/WIP:** Section 2 (S-2 — Hit-Location Architecture) would be updated to record this synthesis as a **pending candidate ruling**, with the current "Open design questions" list (§2.5) narrowed to reflect what this investigation actually resolved versus what remains open per §8 above.

**Roadmap:** Phase 2 (S-2) acceptance-test language would gain the four-state model and the acceptance tests in §9 above as implementation guidance, and the W3 cache-maintenance protocol would be updated to the corrected reference-layer framing (§6) rather than the earlier confidence-tier approach.

**No document is modified by this synthesis itself.** These are the changes that *would* follow your ruling, not changes made now.
