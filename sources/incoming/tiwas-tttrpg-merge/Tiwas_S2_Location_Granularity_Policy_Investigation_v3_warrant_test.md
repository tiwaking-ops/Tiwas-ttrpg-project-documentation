# Tiwas S-2 Design Investigation v3 — Location Warrant Test

**Status: Design investigation output — NON-CANONICAL.**
**Question addressed (per cross-review):** What objectively makes location information necessary for a resolution, independent of currently locked downstream subsystems?
**Not revisited:** Zero-Step, S-1, anatomical mapping, Tier-2 mechanics, Wound/Armor numerical rules, S-3 implementation.

---

## 1. Executive Conclusion

**[Design inference]** Of the four warrant models, **W1 (bare intent) and W4 (unstructured GM judgment) are both dominated** — each is outperformed by W2 and/or W3 on nearly every evaluation criterion, with no criterion on which either is decisively necessary. **W2 (outcome-differentiation) and W3 (closed category list) are not actually rival architectures** once examined operationally: W3 is best understood as a **pre-computed, designer-maintained cache of W2's answer** for known recurring cases, with W2 serving as the underlying test and fallback for novel situations the cache hasn't caught up to yet. This reframes the remaining fork from "which single model wins" to "how much of W2's logic gets pre-compiled into W3's list vs. left to per-resolution judgment" — a real but narrower designer decision than the one this document started with.

**[Answering the framing question from the prior cross-review, §7]** The stress test below indicates location is a property of **the mechanical consequence being pursued, not the fictional action alone**. W1 fails precisely in the cases where narration and consequence diverge (a flavorfully described called shot with no branching outcome); W2 succeeds precisely because it tests the consequence directly.

**[Unresolved designer decision, narrowed but not closed]** How much of the category list can be written now, how it gets maintained as S-3/S-4/S-5 lock, and whether any table-facing shorthand for "does this differentiate?" is needed to keep W2's fallback usable without full GM-improvisation. See §7.

---

## 2. Operational Definitions

The prior round's critique (cross-review §4) is correct that "meaningful," "warranted," and "live mechanical stake" were not yet operational. Each model is restated here as an actual procedure, not a concept.

| Model | Operational rule |
|---|---|
| **W1 — Intent warrant** | Generate a Tier-1 Location Index if and only if the acting player declares, before the roll, that the action targets a specific location or location-bound object. No further test. |
| **W2 — Outcome-differentiation warrant** | Generate a Tier-1 Location Index if and only if the resolution's permissible outcome set would differ depending on which location the roll indicates — i.e., at least two distinct locations exist for which the fictional/mechanical logic of *this specific resolution* would license a different result. Evaluated against the current understanding of what the action is trying to accomplish, not against whether a specific numbered Effect/Wound rule happens to be locked (see §6 for why this avoids C1's flaw). |
| **W3 — Explicit category warrant** | Generate a Tier-1 Location Index if and only if the resolution matches an entry on a designer-authored, versioned, closed list of situation-types (e.g., "declared disarm attempt," "attack targeting carried equipment"). No entry, no generation, regardless of declaration or GM opinion. |
| **W4 — GM warrant** | Generate a Tier-1 Location Index if and only if the GM, using ordinary undefined GM authority and no codified test, judges in the moment that it matters. |

---

## 3. Scenario Matrix

For each scenario: does location generate, under each model, and on what basis.

| Scenario | W1 | W2 | W3 | W4 |
|---|---|---|---|---|
| **Ordinary attack**, no stated objective beyond "hit them" | No (no declaration) | No — no outcome branches by location | No (not a listed category) | Usually no |
| **Called attack, no stated objective** ("I aim for the arm") | **Yes** — declaration alone suffices | **No** — narrating a target doesn't itself create branching outcomes; nothing downstream distinguishes arm-hit from any other hit | Depends on list wording — a poorly written list ("any called shot") reproduces W1; a well-written list ("called shot **with a stated location-dependent objective**") correctly denies this case | Ambiguous — depends on individual GM instinct, no defined standard |
| **Disarm attempt** ("I attack his sword arm to make him drop it") | Yes | **Yes** — disarm's own logic requires knowing whether the weapon-bearing limb was hit; the outcome set genuinely branches (arm hit → disarm eligible; elsewhere → not), independent of whether the Disarm Effect's exact numbers are locked | Yes, if "disarm attempt" is a listed category | Yes, most GMs would grant this |
| **Equipment targeting** ("I strike the shield strap") | Yes | **Yes** — outcome (strap cut vs. not) is strictly location-dependent | Yes, if listed | Yes |
| **Incapacitation attempt** ("I go for a killing/disabling blow") | Yes | **Ambiguous** — no locked Wound/incapacitation rule exists yet to confirm branching; W2 requires reasoning about *plausible* future differentiation rather than confirmed current differentiation. This is the sharpest edge case W2 produces (see §5). | Yes, if explicitly listed (a defensible pre-emptive inclusion, since incapacitation is a near-certain future location-consumer) | Depends entirely on GM's individual judgment about how "serious" the attempt sounds |
| **Cinematic combat**, GM running the scene loosely on purpose | Called shots still force generation regardless of GM's tonal intent — reproduces the tone-protection problem previously used to justify the scene ceiling | Correctly stays Tier 0 throughout **without needing a ceiling**, because nothing in the scene's resolved outcomes actually branches by location if the GM hasn't set up any that do | Correctly stays Tier 0 unless a listed category is triggered | GM simply declines — works, but only because the GM is doing the job the rule should be doing |
| **Mass combat**, many combatants, abstracted | An isolated called shot mid-brawl still triggers bookkeeping for that one exchange | Stays Tier 0 for the abstraction; generates only for the rare exchange where a real branching stake exists (e.g., a leader's called shot with a real disarm objective) | Same as W2, gated by list membership | GM-dependent, same caveats as cinematic case |
| **Formal duel** | Called shots generate; ordinary strikes don't | **Correctly ties to the duel's actual win condition** — "first solid hit" duels never need location; "disable the weapon arm" duels do. Avoids Candidate A's earlier error of treating "duel" itself as tier-determining | Risk: if "formal duel" is listed as its own category (rather than the duel's specific win-condition), this silently reintroduces scene-based logic through the back door — a real trap for list authors to avoid | GM decides per the duel's actual terms — same outcome as W2, informally |
| **Environmental hazard** (e.g., collapsing floor, does it hit a specific limb) | **Structurally awkward** — W1 is built around an attacker declaring a target; hazards have no "attacker," so W1 doesn't naturally apply and defaults to no-generation for the wrong reason (framework mismatch, not evaluated absence of need) | Works cleanly — generates only if the hazard's consequence differs by which body part is affected | Works if hazards are explicitly included as their own category | Works, GM-dependent |
| **Non-combat action** (research, negotiation, a Mind-skill test) | Correctly returns no generation, but only because the "declare a target" frame doesn't apply — not because the model evaluated and rejected the need | Correctly and directly returns no generation — no physical location concept is even relevant to the test | Correctly excluded, not listed | Correctly declines |

---

## 4. Comparative Evaluation

| Criterion | W1 | W2 | W3 | W4 |
|---|---|---|---|---|
| Priority 1 (granular where warranted) | Weak — over-generates on flavor, structurally can't reach non-attack resolutions | **Strong** — directly tests the thing Priority 1 is about | Medium — as good as list coverage, systematically misses unanticipated cases | Potentially strong, but entirely GM-skill-dependent, no structural guarantee |
| Priority 3 (minimum resolution steps) | Weak — spam and flavor-driven generation | **Strong** — never fires without payoff | Medium-strong — clean when list is well-scoped, degrades if list entries are too broad (see duel trap) | Weak-to-strong, unpredictable |
| Player agency | **Highest** — pure declaration | Low-medium — indirect, via choice of objective | Low — governed by list, not declaration | Low — governed by persuasion, not a defined lever |
| GM burden | **Lowest** — no adjudication | Medium-high — requires reasoning about hypothetical branching each time, sharpest on unresolved-subsystem edge cases | **Low** — checklist lookup once the list exists | **Highest** — unstructured judgment every time, no supporting reference |
| Exploitability | **High** (confirmed, spam risk) | Low — can't be forced by words alone | Low-medium — a player can still try to frame actions to match category wording | Low against structural exploit, high against social/table-pressure exploit |
| Consistency | Medium — same rule, inconsistent payoff (flavor-only declarations treated identically to consequential ones) | High in principle; weakest link is the incapacitation-type edge case where "plausible future differentiation" requires judgment | **Highest** — auditable, checklist-based | **Lowest** — GM-to-GM and session-to-session variance, most likely to produce table disputes |
| Resolution inflation | **High risk** — directly rewards narrating harder to force mechanical detail | Low — narrating harder doesn't change the outcome menu | Low | Low structurally, but risks negotiation/haggling dynamics |
| Future compatibility (S-3/S-4/S-5) | Loose — generated data sometimes won't match what the eventual Effect/Wound rule actually needed | **Excellent** — asks exactly the question S-3/S-4/S-5 authors need answered when they write those rules | Good, contingent on active list maintenance | Fine but provides no scaffolding for those future rules to build on |
| Stability as later subsystems lock | Stable mechanism, unstable *payoff* (early data often unused, later data more often relevant) | **Stable and correctly so** — the test itself never changes; only which resolutions satisfy it legitimately grows as new rules genuinely create branching. This is the key distinction from C1: C1's rule *text* was contingent on lock status; W2's rule text is fixed, and only its evaluated result legitimately expands (§6) | Stable only if the list is deliberately and visibly updated — an intentional, versioned change, not a silent one (also distinguishes it from C1) | Trivially stable because it was never precisely defined |

---

## 5. Key Finding: The Incapacitation Edge Case

**[Design inference]** The incapacitation scenario in §3 exposes a real seam in W2 that the earlier rounds hadn't surfaced: W2 asks whether the outcome "would" branch by location, but for a subsystem that isn't locked yet (S-4/S-7), the honest answer requires reasoning about a *plausible future rule* rather than a *confirmed current one*.

**[Design inference]** This is not the same failure as C1. C1 failed because its rule *definition* referenced lock status directly ("generate if a locked rule consumes it"). W2's definition never references lock status — it references whether the *fictional/mechanical logic of the action* branches by location. The incapacitation case is hard not because W2's definition is contingent on implementation, but because judging "does this branch" for a domain with no rule yet written requires the same kind of design-level reasoning a rules author would use, applied ad hoc, at the table, by whoever is running the game. That is a genuine usability cost, not an architectural instability.

**[Design inference]** This is exactly the seam W3 exists to patch: a category list can pre-declare "incapacitation attempts" as warranted by designer fiat, removing the need for per-table speculative reasoning about unwritten future rules, without reintroducing C1's flaw — because the list entry doesn't reference *whether S-4 is locked*, it references *the category of action itself*, decided once by the designer and applied consistently regardless of S-4's implementation status.

---

## 6. Why W2 Does Not Repeat C1's Error

**[Architectural constraint, stated precisely to close this off]** C1 was eliminated because its truth-value for the *same fictional situation* would silently change based on unrelated roadmap progress — the rule's meaning drifted with implementation, not with the fiction. W2 is different in kind:

- W2's test ("would the outcome set branch by location") is fixed for all time.
- What legitimately changes as S-3/S-4/S-5 lock is not the test, but the **space of resolutions for which the answer is yes** — and that growth is *substantively correct*, not an artifact of sequencing. Once a Wound system exists that genuinely differentiates by location, resolutions feeding it genuinely do warrant location in a way they didn't before, because the fiction now has a mechanical hook it previously lacked. That is the system correctly tracking reality, not the architecture drifting.

This distinction should be preserved explicitly in any consolidated document, since it is easy to mistake W2 for a restatement of C1 at a glance.

---

## 7. W2/W3 Are Not Rivals — A Synthesis, Offered for Designer Testing

**[Design inference, offered as a candidate synthesis, not a ruling]** Given §5 and §6, the cleanest reading is that **W3 is an implementation strategy for W2**, not a competing principle:

- W2 is the **underlying test**: does the outcome set branch by location for this resolution.
- W3 is a **maintained cache**: a designer pre-computes W2's answer for known, recurring situation-types (disarm attempts, equipment targeting, likely incapacitation-adjacent attacks) so the table doesn't have to re-derive the answer from scratch every time.
- For situations not yet on the cache, W2 remains available as the fallback test — applied by the GM, but applied *to a defined question* ("does the outcome branch here") rather than an undefined one ("does this feel like it matters," which is W4).

**[Unresolved designer decision]** This synthesis needs its own stress test before being treated as settled: specifically, whether "apply W2 as fallback when nothing on the W3 list matches" is meaningfully lower GM-burden than pure W2, or whether in practice GMs will default to the cache and rarely invoke the fallback correctly. That is an empirical/table-practice question this document cannot resolve from first principles.

**[Unresolved designer decision]** Whether W1 (bare intent) should be preserved as an optional *table-preference* variant for groups who want called shots to be free narrative color regardless of mechanical payoff — this document finds W1 structurally weaker against Tiwas's stated priorities, but does not find it incoherent as a deliberate genre choice for tables that value that specific texture over Priority 3. That is a values question, not resolved here.

**[Unresolved designer decision]** W4 is not recommended as the core mechanism given its consistency and auditability failures, but some irreducible GM-judgment layer is likely unavoidable at the margins of any list-based system (W3) or any test-based system (W2) — the question is how much, not whether any exists at all.

---

## 8. Recommended Next Step

Two candidate next investigations follow directly from this result; the choice between them is itself worth flagging to the designer rather than picking unilaterally:

1. **Draft the W3 cache as a first pass**, explicitly built by applying the W2 test to the scenario set in §3 and a wider net of common Tiwas situations (this is now a well-defined exercise, unlike the premature "closed trigger list" attempted in v1, because the test each entry must satisfy — W2 — is now actually specified).
2. **Run a table-practice stress test** on the W2-fallback question from §7 (GM-burden in practice, not in theory) before committing resources to building out the cache, in case the fallback turns out to be unworkable and a different design is needed instead.

This document does not pick between (1) and (2) — both are reasonable orderings, and the designer's preference for "build the artifact first" vs. "validate the fallback mechanism first" should decide it.
