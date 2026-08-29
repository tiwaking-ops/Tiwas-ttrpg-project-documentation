# Tiwas S-2 Design Investigation v2 — Response to Cross-Review

**Status: Design investigation output — NON-CANONICAL. Supersedes the analysis (not the raw scenario data) in v1.**
**Purpose:** Address the cross-review critique point by point, correct the errors it identifies, and re-run the investigation where the error was load-bearing rather than cosmetic.

---

## 1. Disposition of Each Critique Point

| # | Critique | Disposition |
|---|---|---|
| 1 | Reframing (invocation policy, not tier-selection) is correct | **Accepted, unchanged.** |
| 2 | Consequence-driven is a strong candidate but was treated as leading prematurely | **Accepted.** v1's Executive Conclusion stated a recommendation in §8 that should have stayed a candidate under test. Retracted below. |
| 3 | "A downstream consumer exists" was quietly substituted for "the design intends location to exist" | **Accepted — this is the most serious error.** Analyzed in §2. |
| 4 | "Called attack" treated inconsistently — sometimes intent, sometimes consequence | **Accepted — genuine conflation.** Analyzed in §3. |
| 5 | Scene ceiling reintroduces scene-based state after scene-based selection was criticized, without being tested | **Accepted.** Analyzed in §4. |
| 6 | "Priority 1 = where warranted" was silently redefined as "where a currently-locked mechanic reads it" | **Accepted — same root cause as #3.** See §2. |
| 7 | Closed trigger list is not rule-ready | **Accepted.** It is downgraded from "recommended" to "illustrative, contingent on §2 being resolved" in v1 and remains so here. |
| 8 | S-2/S-3 dependency note should stay an observation | **Accepted.** |
| 9 | Should not proceed to the S-2/S-3 interface question yet | **Accepted.** §9 of v1 is withdrawn as "next question." Replaced by §8 here (continue policy stress-testing). |

---

## 2. The Core Error: Consumer-Existence vs. Design-Warrant

**[Design inference — correcting v1]** v1's Candidate C operationalized "consequence-based" as: *generate location data when a currently locked rule (an Effect, a Wound read, an equipment rule) will read it.* This is not the same proposition as Priority 1's "granular physical simulation **where the situation warrants it**," and the difference is not cosmetic:

- **Rule-triggered test:** "Does a rule that exists *right now, in the locked ruleset* consume this data?"
- **Warrant-based test:** "Does *this resolution*, on its own merits, have a property that makes location differentiation meaningful to the fiction or the stakes — independent of whether a numbered rule happens to be written yet?"

**[Design inference]** These diverge badly under current conditions: S-3 and S-4 are both open (Reserved). Under the rule-triggered test, almost **no** resolution in Tiwas today would generate location data, because almost nothing downstream is locked yet to consume it. That is not a description of "when location is warranted" — it is a description of "how much of S-3/S-4 happens to be implemented so far." A granularity-invocation policy that produces a different practical answer depending on unrelated implementation progress elsewhere in the roadmap is not a stable architectural rule; it is an accident of sequencing.

**[Design inference]** This also explains why v1's recommendation implicitly depended on unlocked material: the "closed trigger list" in v1 §9 named the *candidate* "Choose Location" Effect and a *hypothetical* Wound-read as if they were settled consumers. They are not settled (Proposals §3.1, Reserved). v1 therefore came close to violating its own hard constraint — "do not resolve Wound/Armor/Defence/Effect mechanics" — by quietly assuming their shape in order to make Candidate C concrete.

**[Consequence for the investigation]** "Consequence-based" must be split into two genuinely different candidates that were previously merged:

- **C1 — Rule-triggered:** fires only when a currently-locked rule reads the data. Deterministic and unambiguous, but bootstraps to "almost always Tier 0" until S-3/S-4 lock, and its behavior silently changes every time a new subsystem locks — an architecture whose meaning is a moving target.
- **C2 — Warrant-triggered:** fires when the resolution has a property, defined by a **stable, closed category list set now** (not deferred to future rule text), that the designer judges to make location differentiation meaningful — regardless of whether a consuming rule is locked yet. This requires naming the categories now, which is harder, but doesn't drift as later subsystems lock.

Both are examined in §6–7 below as separate candidates rather than one blurred "Candidate C."

---

## 3. Disentangling "Called Attack"

**[Critique accepted as identified]** v1's scenario table listed a *declared* called attack as a Tier-1 trigger under "Consequence-Based," but a mere declaration is not itself a consequence — it is exactly the mechanism Candidate B (action/intent-based) uses. v1 smuggled a B-style trigger into a C-style policy without justifying the move.

**[Design inference]** There are two structurally different claims that both use the words "called attack," and the investigation must keep them separate:

1. **Called attack as sufficient cause (pure intent-based, Candidate B logic):** the player's declaration alone is enough to generate location data, on the theory that the *intent to affect a specific location* is itself the thing being simulated. No further check is needed.
2. **Called attack as necessary-but-not-sufficient (warrant-gated, C2 logic):** the declaration signals that location *might* matter, but generation only occurs if the GM confirms the declaration maps to an actual stake in the current resolution (e.g., "aiming for the sword-arm to make it drop the weapon" only generates data if disarming is actually a live possible outcome of this exchange — otherwise it is flavor text with no mechanical referent).

**[Design inference]** Model 1 is exactly what produces the exploitability finding from v1 §6/§7: if declaration alone is sufficient, a player can declare "called attack" every single turn purely to manufacture location rolls, with no cost gate (Tier 1 is a free post-process per §14.2 — there is no resource tax that would naturally discourage spamming it). Model 2 closes that hole but reintroduces GM adjudication burden and a subjective judgment call similar in kind to ordinary Candidate B — meaning "called attack" cannot be cleanly claimed as a *consequence*-based trigger at all. It is, honestly, a form of action/intent-based triggering with a warrant check bolted on, not a pure consequence trigger.

**[Corrected conclusion]** "Called attack" should be removed from the C1/C2 trigger lists as a first-class independent entry. It survives only as an *instance* of C2's warrant category ("declared intent to affect a specific location, confirmed by the GM to have a live mechanical stake") — not as its own separate trigger. This closes the conflation identified in the critique.

---

## 4. The Scene Ceiling: Tested, Not Assumed

**[Critique accepted]** v1 introduced the ceiling (Candidate D) to solve a specific problem — protecting cinematic/mass-combat tone from an isolated called-shot declaration — without testing whether that problem is real under a corrected trigger model, or whether it was only a problem because of the Model-1 "declaration alone suffices" flaw identified in §3.

**[Re-test]** Under the corrected model (called attack requires GM-confirmed live stake, §3 Model 2), does the tone-protection problem still exist?

| Scenario | Without ceiling, corrected trigger model | With ceiling |
|---|---|---|
| Player declares a called shot mid-mass-brawl the GM is running as abstract/cinematic | GM confirms whether the declaration maps to a live stake; in an abstraction the GM has chosen to keep coarse, there typically **is no live stake to confirm**, so generation is denied on the merits, not by a scene-level override | Same outcome, reached via a blanket rule instead of a per-case judgment |
| Player declares a called shot in a scene the GM *is* willing to individuate, but only occasionally | GM confirms per-case as normal | Ceiling must have been pre-set to allow it, or the GM must break the ceiling ad hoc — adds friction the no-ceiling version doesn't have |

**[Design inference]** Once the trigger is corrected to require GM confirmation of a live stake (rather than bare declaration), the ceiling appears to be **solving a problem that the corrected C2 trigger already solves**, at the cost of reintroducing exactly the scene-level state the investigation flagged as architecturally weak in v1 §6 (Candidate A's core failure mode: deciding in advance, for a whole scene, something that should be decided per-resolution). The ceiling's marginal value is a *procedural* one — it lets a GM pre-commit to "don't ask me, the answer is no all night" for table-management reasons — not a *design-correctness* one.

**[Corrected conclusion]** The ceiling is **not validated as a necessary component of the policy.** It may still be worth keeping as an optional GM table-management convenience layered on top of whichever core policy is chosen, but it must not be presented as solving an exploitability or correctness problem — the corrected trigger model already solves that. This is now marked explicitly as a separable, optional add-on rather than part of the core candidate.

---

## 5. Revised Candidate Set

| ID | Description | Status relative to v1 |
|---|---|---|
| A — Scene-based | Unchanged from v1 | Retained for comparison |
| B — Action/intent-based (bare declaration sufficient) | Unchanged from v1, now explicitly the "Model 1" form from §3 | Retained, exploitability finding stands |
| C1 — Rule-triggered | New: what v1 called "Consequence-based," narrowed to *only* currently-locked-rule consumption | Split out from v1's Candidate C |
| C2 — Warrant-triggered | New: consequence-based, defined by a closed *category* list judged stable now, independent of which specific Effect/Wound rule text is locked; called attacks fold in here as GM-confirmed instances | Split out from v1's Candidate C; incorporates the corrected §3 model |
| D — Ceiling as optional add-on | Demoted from "core hybrid policy" to "optional layer over A/B/C1/C2" | Downgraded per §4 |

---

## 6. Adversarial Scenario Stress-Test (Focused on the Corrected Issues)

| Adversarial scenario | A | B (Model 1) | C1 (rule-triggered) | C2 (warrant-triggered) |
|---|---|---|---|---|
| Player spams "called shot" every turn purely to generate favorable location rolls, in a scene with no locked consumer | Irrelevant to scene-tier, but if scene tier ≥1, spam still generates unused data every time — no defense | **Fails** — declaration alone is sufficient, so spam always succeeds; this is the exploit identified in v1 §6 | **Fully immune** — no locked rule exists to consume it, so nothing generates, regardless of spam volume | **Immune by design** — GM must confirm a live stake each time; repeated declarations with no live stake are repeatedly denied, at the cost of repeated GM adjudication |
| A genuinely warranted called shot occurs (disarm attempt with a locked "Disarm" Effect available) before S-3 fully locks the general Effect menu | Depends on accidental scene-tier setting | Generates correctly (declaration matches genuine intent) | **Fails to generate** if the specific consuming rule isn't locked yet, even though the design clearly warrants it — this is the bootstrapping failure from §2 | Generates correctly — GM confirms the live stake exists independent of exact rule-text lock status |
| GM wants a "no called shots tonight" cinematic session | Achieved by setting scene tier to 0 | Achieved only informally (house rule / table agreement); a rules-lawyer could contest it since B has no built-in refusal mechanism | Achieved automatically if nothing is locked yet; **not guaranteed** once S-3/S-4 lock, since C1 would then start generating in exactly the scenes the GM wanted to keep coarse | Achieved via ordinary GM adjudication — GM declines to confirm any live stake tonight; consistent with normal GM authority rather than a special rule |
| Equipment-targeting attack (e.g., "I go for the shield strap") with no Equipment Damage Effect locked yet | Depends on scene tier, accidentally | Generates if declared as the relevant action type | **Fails to generate** — no locked consumer | Generates if GM judges equipment-targeting to be a stable warrant category (it is a reasonable candidate for the closed category list) |

**[Design inference]** The stress test surfaces a clean, decisive finding: **C1 (rule-triggered) is structurally unfit as a standalone policy.** Its behavior is contingent on unrelated roadmap sequencing (whether S-3/S-4 happen to be locked yet) rather than on the merits of the resolution in front of the table. It should not advance as a candidate on its own — noted here as a **negative finding**, which the investigation is allowed to produce per the brief's own instruction not to manufacture a winner where analysis doesn't support one, and equally not to preserve a candidate the evidence eliminates.

**[Design inference]** B fails the exploitability test outright, as v1 already found, and the corrected analysis confirms rather than weakens that finding.

**[Design inference]** C2, once "called attack" is folded in correctly as a GM-confirmed instance rather than a standalone trigger, resists both failure modes: it doesn't bootstrap-fail like C1, and it doesn't spam-fail like B. Its cost is recurring GM adjudication — the same cost ordinary Candidate B already carried, but now paired with a principled test ("is there a live stake") instead of a bare declaration check.

---

## 7. Comparative Re-Evaluation (Delta from v1)

| Criterion | A | B | C1 | C2 |
|---|---|---|---|---|
| Resolution-step cost | Fixed, often wasted | Variable, spam-prone | Minimal but arbitrarily under-fires pre-lock | Minimal, one GM judgment call per candidate trigger |
| Exploitability | Low (GM sets scene) | **High (confirmed)** | Low (nothing fires) — but this is under-firing, not correctness | Low — spam is denied at the judgment gate |
| Stability across roadmap sequencing | Stable | Stable | **Unstable — changes meaning as S-3/S-4 lock** | Stable — categories defined now, independent of specific rule text |
| Matches Priority 1 ("where warranted") | Weak | Medium | **Fails — conflates "warranted" with "implemented"** | Strong — directly tests warrant, not implementation status |
| GM burden | Low | Medium | Low | Medium (same order as B, but principled rather than bare) |
| Requires a defined category list now | No | No | No | **Yes — this is real design work still owed, not yet done here** |

**[Design inference]** C1 is downgraded from "viable candidate" to "eliminated by the stress test" — this is a genuine change in the field of candidates, not a restatement of v1.

---

## 8. What Remains Genuinely Open

**[Unresolved designer decision]** Between **B** and **C2**, the deciding question is not resolved by this document, because it depends on a table-culture judgment the investigation cannot make on the designer's behalf:

- **B** trusts the *player's declaration* as sufficient, accepting the spam-exploit risk as a social-contract problem for the table to manage rather than a rules problem to close.
- **C2** trusts the *GM's confirmation of live stake*, closing the exploit at the cost of a recurring adjudication step every table will feel.

**[Unresolved designer decision — new, and this is real outstanding work]** C2 is not yet a concrete policy. It requires the designer (or a follow-up investigation) to actually **write the closed category list** of what counts as a "live stake" — equipment-targeting, disarm-adjacent Effects, duel-scoring, and so on — as a *stable* list defined independent of which specific S-3/S-4 rule text ends up locked. v1's list was not this; it borrowed unlocked rule names directly. That list does not yet exist in a form that satisfies §2's stability requirement.

**[Unresolved designer decision]** The ceiling (§4) is demoted to optional and should be ruled on separately, purely as a table-management convenience, not as part of the correctness argument for any core candidate.

**[No dominant candidate declared.]** Per the brief's own success criteria, this document does not manufacture a winner between B and C2. It does, however, report a genuine elimination (C1) and a genuine demotion (the ceiling), both defensible on the evidence above rather than asserted.

---

## 9. Process Recommendation

**[Recommendation, matching the reviewer's proposed process]** Do not proceed to the "S-2/S-3 interface" question yet. The immediate next step should be one of:

1. Draft the stable closed category list for C2 (§8) as its own tightly scoped investigation, independent of S-3/S-4's eventual rule text — this is the piece of real design work the critique correctly identified as missing.
2. Run B vs. C2 through further adversarial scenarios specifically targeting GM-burden cost at the table (session-length impact, adjudication fatigue) rather than correctness, since correctness no longer separates them as cleanly as v1 assumed.

Only after one of these produces a clearer separation — or a designer ruling accepts the GM-burden tradeoff directly — should the S-2/S-3 interface question (v1 §10) be reopened.
