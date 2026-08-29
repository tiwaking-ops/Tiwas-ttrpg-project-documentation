# DONE Tiwas Location Index Analysis

**Source:** Shared ChatGPT Conversation  
**Share link:** [https://chatgpt.com/share/6a934e83-f1f0-83ec-8752-38c7fe566acb](https://chatgpt.com/share/6a934e83-f1f0-83ec-8752-38c7fe566acb)  
**Transcribed:** 8/30/2026 (headless-browser render of the share page)  
**Note:** This share verifies against the chat in which the user pasted Claude's "Round 1 Cross-Review Synthesis" and "Designer Ruling Recorded" outputs for ChatGPT's assessment. ChatGPT's critique of Round 1 (the first Assistant message below) is the text that was previously evidenced only as a blank-name attachment ("ChatGPT says:") in the Claude chat export. The "User:" messages below are ChatGPT's render of pasted Claude-authored text (which itself exists verbatim in the Claude chat export). Visible-date value: none rendered on the share page.

## Assistant:

> ChatGPT's critique of Claude's Round 1 (this is the previously missing blank-name attachment content, evidenced in the Claude export only as "ChatGPT says:")

Claude's Round 1 is stronger and more disciplined than my previous pass, particularly on one point: it correctly separates the location-source question from the invocation-policy transfer question instead of quietly resolving both at once.

I agree with its core candidate, with one qualification.

1. Where Claude is right

The strongest part is the A/C/D collapse:

> No Core Test roll → no Location Index. Where a Core Test exists, its natural roll is Zero-Step's input.

That is the cleanest architectural answer.

It preserves the existing Zero-Step rule rather than creating a new "hazard roll," and it fits the established architecture that location is a read-only post-process of an already-recorded natural roll. The Roadmap likewise says Universal Play modules must call the Core Test transaction rather than create a competing resolution engine. Tiwas TTRPG — Canonical Rules &… Tiwas___Implementation_Roadmap_…

I would therefore accept Claude's rejection of Candidate B as the correct working position:

> Ad-hoc GM d100 solely to obtain location = not permitted under the current architecture.

That is stronger than merely saying it is "not preferred."

2. The important refinement

I would not yet adopt Claude's wording:

> "already adjudicated by an ordinary Core Test belonging to some character"

as the final architectural rule.

The broader and safer formulation is the one Claude itself reaches in §8:

> Where a Core Test exists, its natural roll is Zero-Step's input.

Why? Because "belonging to some character" potentially assumes something about future hazard architecture that this investigation has not actually established.

The real invariant appears to be:

> Does the physical outcome have an existing governing Core Test with a natural d100 roll?
>
> If yes → that roll can feed Zero-Step.
>
> If no → Zero-Step has no input.

That leaves open, without deciding it, whether a future hazard subsystem might define a legitimate Core Test whose participant isn't neatly described as "the affected character."

So I'd retain "governing Core Test" rather than "Core Test belonging to some character."

3. Claude correctly identifies the next unresolved question

This is where I think Claude's response improves substantially on mine.

It does not claim that the existing Named-Outcome Test automatically transfers to hazards.

That is correct.

The existing candidate policy specifically says:

> the player must explicitly state a distinct consequence.

And the accepted investigation explicitly framed the Named-Outcome Test around a declared objective. Tiwas___S2_Hit_Location_Investi…

A collapsing bridge doesn't declare an objective.

Therefore there are actually two separate questions:

Question A — Location-source provenance

> Resolved provisionally:
>
> Existing governing Core Test → use its natural roll.

Question B — Non-attack warrant

> Still open:
>
> What makes a non-agentive hazard's Location Index warranted?

Claude correctly refuses to smuggle an answer to B into the answer to A.

That's exactly the kind of scope discipline the Starter Brief called for.

4. I would reject Claude's Direction 2 for now

Claude offers:

> Treat non-attack cases as categorically State 3 or State 4 by default until a future subsystem explicitly says otherwise.

I don't think we should adopt that as a candidate yet.

The reason is that it risks conflating "there is no player-declared objective" with "location-dependence is unresolved or no distinct consequence exists."

Those aren't necessarily the same thing.

For example, imagine a future hazard rule explicitly establishes:

> A collapsing structure can cause a localized structural impact whose location matters.

That could establish location-dependence independently of an acting player's declared objective.

Calling every such case State 3 merely because there was no player declaration would make the four-state model do something it wasn't designed to do.

So I think Claude is right to leave this open.

5. Recommended next step

I agree with Claude that we should not make a designer ruling yet.

The next investigation round should test the candidate provenance rule while deliberately keeping the warrant question separate.

I'd use the following working hypothesis:

> Working Hypothesis H1: A Tier-1 Location Index for a non-attack physical resolution can only be generated from the natural d100 roll of an existing governing Core Test. No separate location-only roll is generated. If no governing Core Test exists, there is no Zero-Step input and therefore no Location Index.

Then test at least:

- Character reacts to a fall.
- Character fails to react to a fall.
- Character deliberately causes a physical hazard.
- Hazard affects its creator.
- Hazard affects another character.
- Environmental hazard with a resistance test.
- Trap with a perception/reaction test.
- Automatic trap with no test.
- Collapsing structure with a test.
- Collapsing structure resolved entirely by narration.
- Extended Test where one interval produces the physical consequence.
- Multiple affected characters making independent tests.
- A case where one character's test causes the event and another character's test resolves its impact.
- A case where an opposed contest is involved.

And crucially, for every case record two independent fields:

- Roll provenance: What natural roll, if any, supplies Zero-Step?
- Warrant status: Is a Location Index actually warranted under the existing candidate policy?

That prevents us from accidentally using the investigation to answer both questions simultaneously.

Bottom line

I agree with Claude's Round 1 candidate analysis and would use it as the basis for Round 2.

The strongest current finding is:

> The absence of an attacker is not itself the architectural problem. The decisive question is whether there is an existing governing Core Test with a natural roll for Zero-Step to consume.

But non-attack warrant remains unresolved. We should not yet modify the Named-Outcome Test, and we should not default all non-attack cases to State 3/4.

So my recommended status is:

> S-2 Non-Attack Location Source — Candidate H1 accepted for stress-testing; no designer ruling yet.

That keeps the investigation exactly where the Starter Brief intended it: source provenance first, warrant transfer second.

## User:

> Pasted content (Claude-authored; exists verbatim in the Claude chat export)

claude says:

# S-2 Non-Attack Location Source — Round 1 Cross-Review Synthesis

**Evidence class: Design inference / methodology synthesis. No ruling made. No Canonical/Proposals/Roadmap document modified.**

---

## 1. Points of Agreement

| Point | External review position | Assessment |
| --- | --- | --- |
| A/C/D collapse | Correct, strongest finding of Round 1 | **Accepted** |
| Candidate B (ad-hoc GM roll) | Should be stated as **architecturally impermissible**, not merely disfavored | **Accepted — stronger framing is correct.** Candidate B doesn't fail a preference test; it fails Canonical Invariant 18 and Roadmap §2 directly. Round 1 already reached this via Invariant 18, but understated it as "closed for this investigation" rather than "excluded by existing Core architecture." Correcting that understatement now. |
| Separation of Question A (provenance) from Question B (warrant transfer) | Correct methodology; must not resolve both simultaneously | **Accepted — this is the central discipline to preserve going forward.** |

---

## 2. Wording Refinement — "Governing Core Test" vs. "Core Test Belonging to a Character"

The external review proposes replacing:

> "already adjudicated by an ordinary Core Test **belonging to some character**"

with:

> "**Does the physical outcome have an existing governing Core Test** with a natural d100 roll?"

### Evaluation

Under the **current** Core architecture (Canonical §3, §5–6), every Core Test is necessarily a Skill test, and every Skill belongs to a character (the 24-Attribute Matrix and Skill Cap formulas are defined only for characters — Canonical §3, §5.2). There is currently no mechanism for a "governing Core Test" that does not belong to some test-taking participant. So **under existing rules, the two phrasings are presently coextensive** — there is no live case where a "governing Core Test" exists but doesn't belong to a character.

However, the reviewer's caution is still valid as a **forward-compatibility choice**, not a present distinction: a future hazard subsystem (S-8 Stakes Gate, a hazard-specific test entity, etc.) could in principle introduce something that isn't cleanly "the affected character's" test — e.g., a test attributed to the hazard itself, or a test taken by a third party (a rescuer, a bystander) whose relationship to "the affected character" isn't 1:1.

**Resolution:** Adopt the broader wording. It costs nothing now (identical effect under current rules) and avoids baking in an assumption ("the test belongs to *the affected* character specifically") that Round 1's own stress-test table already showed doesn't hold — the "character deliberately destabilizes a shelf" and "third party rescues" scenarios both show the roll-supplying party is not fixed to any single role.

**Revised candidate rule (supersedes Round 1 §4):**

> **H0 (provenance rule):** A Location Index for a non-attack physical resolution may only be derived from the natural d100 roll of an **existing governing Core Test** for that resolution. If no such Core Test exists, Zero-Step has no valid input and no Location Index is generated. No location-only or hazard-only roll may be introduced to supply this input.

This is a wording refinement of Round 1's finding, not a new conclusion — same evidentiary basis, same scope.

---

## 3. Direction 2 (Default Non-Attack Hazards to State 3/4) — Withdrawn

The external review's objection is correct and is **accepted**:

> Conflating "no player-declared objective" with "location-dependence unresolved / no distinct consequence" misuses the four-state model's actual categories.

Round 1's Direction 2 proposed treating the *absence of a declaring party* as equivalent to a State-3/4 outcome. But State 3 specifically means "the outcome is plausible but whether *location* is the delivery mechanism is an open design fork" (Proposals §2.1A), and State 4 means "no distinct consequence was named" — neither of these is about *who* names the consequence, only *whether* one exists and *whether location delivers it*. A GM-authored hazard consequence could be just as definite and just as location-anchored as a player-declared one; defaulting it to State 3/4 solely because no player spoke would silently narrow the four-state model's actual test.

**Direction 2 is withdrawn from the candidate set.** Only Direction 1 (reformulate the Named-Outcome Test to admit a GM-stated distinct consequence as declaration-equivalent) remains live for Question B. This does not resolve Question B — it only removes an incorrect shortcut from consideration.

---

## 4. Working Hypothesis H1 — Adopted for Round 2

The external review's proposed hypothesis is accepted, restated to incorporate the H0 wording refinement:

> **H1 (working hypothesis, not a ruling):** A Tier-1 Location Index for a non-attack physical resolution can only be generated from the natural d100 roll of an existing governing Core Test (H0). If no governing Core Test exists, there is no Zero-Step input and therefore no Location Index. This rule is independent of, and does not by itself resolve, whether such a Location Index is *warranted* under the existing (player-declaration-based) invocation policy.

### Methodological requirement adopted

Per the external review, every stress-test scenario in Round 2 must record **two independent fields**, scored separately:

| Field | Question it answers | Governed by |
| --- | --- | --- |
| **Roll provenance** | Does a governing Core Test exist, and whose roll is it? | H0 (this round's subject) |
| **Warrant status** | Is a Location Index actually warranted for this resolution? | Existing candidate invocation policy (Proposals §2.1A) — **not reformulated here** |

Recording these separately prevents the same failure mode already caught twice in the prior investigation (Armor Bypass overclaim; Structural Weak Points State 1→2 correction): using stress-test results to silently answer a question the round wasn't scoped to answer.

---

## 5. Stress-Test Scenario Set for Round 2

Merging the external review's 14-scenario list with Round 1's original set (deduplicated, no scenario dropped):

| # | Scenario | Roll provenance (H0) | Warrant status (existing policy) |
| --- | --- | --- | --- |
| 1 | Character reacts to a fall, attempts to catch self | *To be scored* | *Out of scope this round* |
| 2 | Character fails to react to a fall (no test offered) | *To be scored* | *Out of scope this round* |
| 3 | Character deliberately causes a hazard affecting themself | *To be scored* | *Out of scope this round* |
| 4 | Hazard affects its creator vs. affects another character | *To be scored* | *Out of scope this round* |
| 5 | Environmental hazard with a resistance test | *To be scored* | *Out of scope this round* |
| 6 | Trap with a Perception/Reflexes reaction test | *To be scored* | *Out of scope this round* |
| 7 | Automatic trap, no test offered | *To be scored* | *Out of scope this round* |
| 8 | Collapsing structure, test exists | *To be scored* | *Out of scope this round* |
| 9 | Collapsing structure, resolved entirely by narration | *To be scored* | *Out of scope this round* |
| 10 | Extended Test interval produces the physical consequence | *To be scored* | *Out of scope this round* |
| 11 | Multiple affected characters, independent tests | *To be scored* | *Out of scope this round* |
| 12 | One character's test causes the event; another's resolves its impact | *To be scored* | *Out of scope this round* |
| 13 | An S-1 opposed contest is involved (e.g., a shove causing a fall) | *To be scored* | *Out of scope this round* |
| 14 | Trap resolved retroactively via a Stakes Gate–style reaction (S-8-adjacent) | *To be scored* | *Out of scope this round, flag as S-8 touchpoint only* |

**"Out of scope this round" is deliberate**, not an oversight: per §3 above, Warrant status depends on whether/how the Named-Outcome Test transfers to non-declaring hazards — a question this round does not resolve. Filling in that column now would repeat the exact conflation the external review flagged in Direction 2.

---

## 6. Scope-Guard Compliance Check

| Guard | Status |
| --- | --- |
| Zero-Step derivation mechanism reopened? | No |
| S-1 reopened? | No — scenario 13 uses S-1 as an *input source*, doesn't modify it |
| Invocation/warrant policy reopened or reformulated? | No — explicitly deferred (Warrant column left unscored) |
| Structural Weak Points State-2 ruling reopened? | No |
| W3 cache redesigned? | No |
| Tier 0/1/2 scene-selection touched? | No |
| Anatomical mapping / Tier-2 / Wound-Armor-Effect numerics designed? | No |

---

## 7. Status After This Synthesis

| Item | Status |
| --- | --- |
| H0 (provenance rule) | **Candidate, refined wording adopted** — supersedes Round 1 §4/§8 wording, same evidentiary basis |
| Candidate B (ad-hoc GM roll) | **Architecturally excluded**, not merely disfavored |
| Direction 2 (default non-attack to State 3/4) | **Withdrawn** |
| Direction 1 (GM-stated consequence as declaration-equivalent) | Sole remaining candidate for Question B — still undecided, requires designer ruling |
| H1 + 14-scenario stress test | **Adopted as Round 2 process**, provenance-only scoring |

**Still requires designer input before Round 2 can complete:** whether to pursue Direction 1's reformulation in parallel with the provenance stress test, or sequence it strictly after (run H0's provenance scoring first, decide Direction 1 only once H0 is stress-tested clean). This is a sequencing choice, not a mechanical one, and is left open per the same reasoning as the original Decision Point 2.

## Assistant:

I agree with Claude's cross-review synthesis. It is a good correction of Round 1, and I would proceed to Round 2 exactly as proposed, with one small methodological emphasis.

What I would lock in as the working position

H0 is now the right candidate formulation:

> A Location Index for a non-attack physical resolution may only be derived from the natural d100 roll of an existing governing Core Test for that resolution. If no such Core Test exists, Zero-Step has no valid input and no Location Index is generated. No location-only or hazard-only roll may be introduced to supply this input.

This is preferable to "affected character's roll" because it identifies the resolution transaction, rather than prematurely assigning the roll to a particular fictional role.

The strongest methodological decision

The insistence on two independent scores is exactly right:

| Score | Question |
| --- | --- |
| Roll provenance | Is there a governing Core Test, and what natural roll supplies Zero-Step? |
| Warrant | Is a Location Index actually warranted? |

For Round 2, only the first gets scored.

That prevents us from accidentally using the provenance experiments to establish that a non-attack hazard deserves a location roll. That second question remains genuinely open.

One correction to my earlier position

Claude's treatment of the "governing Core Test belonging to a character" wording is also right. Under current Canonical rules the distinction doesn't matter, but H0 is better forward-facing terminology. It doesn't assume in advance that the relevant test-taker must be the victim, initiator, or any other particular participant.

Candidate B

I agree with Claude's stronger classification:

> Ad-hoc GM/hazard d100 = architecturally excluded under the current system.

Not merely "not preferred." It would create a parallel resolution primitive outside the established Core Test transaction. If Tiwas eventually wants a genuine hazard-side roll, that would have to be a separately designed and governed mechanism—not something smuggled in as a Zero-Step input.

Direction 2

Also agree that it should be withdrawn.

"No player declaration" does not logically mean State 3 or State 4. The four states concern the consequence and its relationship to location, not whether an agent happened to verbalize an intention.

So the remaining Question B is cleanly:

> Can a GM/fiction-established distinct consequence function as the non-attack equivalent of the existing declared objective for warrant purposes?

And that should not be answered during the provenance experiment.

Recommendation: proceed to Round 2

I would therefore accept the current status as:

- H0: candidate, refined wording.
- Ad-hoc hazard/GM roll: architecturally excluded under current Core architecture.
- Direction 2: withdrawn.
- Direction 1: still open.
- Round 2: provenance-only stress test.
- Warrant column: deliberately left unscored.
- No Designer Ruling yet.

And I would sequence Direction 1 after the H0 stress test, rather than run both simultaneously.

That gives us a very clean investigation chain:

Round 1 → candidate H0 → Round 2 falsification/stress test → establish whether provenance survives → then separately investigate non-attack warrant transfer.

That is methodologically safer than introducing a second unresolved variable into the Round 2 trials.

## User:

> Pasted content (Claude-authored; exists verbatim in the Claude chat export)

I decided: Option 2 — No, not yet, for anyone, ever, until later rules exist.

Claude says:

# S-2 Non-Attack Location Source — Designer Ruling Recorded

**Evidence class: Designer Ruling. This is now binding for the non-canonical S-2 candidate policy, pending formal promotion per Proposals §21.**

---

## 1. Ruling

> **Non-attack physical resolutions (falls, hazards, structural collapses, and similar non-adversarial physical events) never generate a Tier-1 Location Index, categorically, regardless of GM framing or stated stakes, until a future subsystem (S-4, S-7, or S-8) explicitly establishes the grammar for it.**

This closes Decision Point 1 as **Option 2**. Option 1 (GM-authored stakes substitute) is rejected for now — not because it was flawed, but because you've chosen to defer hazard-location granularity rather than build it ahead of the subsystems it depends on.

---

## 2. Direct Consequences

| Item | Before this ruling | After this ruling |
| --- | --- | --- |
| Named-Outcome Test / Warrant policy transfer to hazards | Open question (Direction 1 vs. 2) | **Moot for now.** No warrant test runs at all for non-attack cases — there's nothing to warrant. |
| H0 (governing Core Test provenance rule, Round 2) | Candidate, stress-tested | **Provenance is now academic.** Even where a governing Core Test exists (e.g., a Reflexes test to dodge a falling shelf), no Location Index is generated regardless, because the category itself is closed. H0's findings aren't wrong, they're just currently inert — worth keeping on record for whenever S-4/S-7/S-8 reopens this. |
| H0 Rider B (multi-character causal chain tie-break) | Candidate, needed a decision | **No longer needs a decision right now.** Since no non-attack case produces a Location Index at all, there's nothing for the rider to arbitrate yet. |
| Decision Point 2 (blind trial timing) | Open | **Closed — no trial needed.** Per the Architect Assessment's own logic: Option 2 makes warrant-eligibility categorically "never," so there's nothing to stress-test. |

---

## 3. What This Means at the Table, Right Now

- A character falls off a cliff → damage, no location detail.
- A trap triggers, dodged or not → damage/effect, no location detail.
- A structure collapses on someone → damage, no location detail.
- This is true **no matter how specifically the GM narrates it** ("the beam catches your leg") — that's flavor text, not a mechanical Location Index. It doesn't feed into Wounds, Armor, or anything downstream, because those subsystems don't exist yet either.
- Attacks are completely unaffected — Zero-Step still works exactly as before for anything with an attacker.

---

## 4. What Reopens This Later

This ruling is explicitly **not permanent** — it's a deferral, tied to specific future work:

- **S-4 (Wound activation/severity)** — once wounds exist, there may be a reason to let hazards produce localized injury.
- **S-7 (Incapacitation/death)** — same logic, for consequences severe enough to matter structurally.
- **S-8 (Difficulty/Stakes Gate)** — this is the most likely reopening trigger, since Stakes Gate is specifically about deciding when a resolution has meaningful stakes worth extra mechanical weight; that's the natural home for "does this hazard deserve location detail."

When any of those get designed, this ruling should be revisited — not silently reversed, but explicitly reopened as its own decision point, the same way this one was.

---

## 5. Updated Status Table

| Item | Status |
| --- | --- |
| Zero-Step (attack-based location) | Unchanged — Canonical / Locked |
| Non-attack Location Index | **Ruled: never generated, until S-4/S-7/S-8 reopens the question** |
| H0 provenance rule | Retained as design record, currently inert |
| H0 Rider A/B | Retained as design record, currently inert |
| Named-Outcome/Warrant transfer to hazards (Direction 1) | Rejected for now, not deleted — revisit alongside S-4/S-7/S-8 |
| Blind trial | Not authorized — none needed |

---

## 6. Documentation Update (For When You're Ready to Formalize)

This ruling should eventually be reflected in:

- **Proposals/WIP §2.5** (open design questions) — move "whose roll supplies a non-attack Location Index" from "open" to "resolved: none, deferred pending S-4/S-7/S-8."
- **Roadmap §9 (Phase 2)** — note that non-attack Location Index generation is explicitly out of scope until those phases land.

No document has been edited yet — this is a record of the ruling, ready to merge whenever you want to run the formal update pass.

## Assistant:

Yes. I agree with the ruling, and Claude has recorded the decision correctly.

The important distinction is that this is a designer deferral, not a finding that non-attack location is impossible.

Current S-2 position

> Non-attack physical resolutions generate no Tier-1 Location Index under the current design.

That applies regardless of:

- whether there is an underlying Core Test;
- who made that test;
- whether the hazard was caused intentionally or accidentally;
- whether the GM describes a specific body location;
- whether the consequence is severe;
- whether the GM establishes explicit stakes.

So, for now:

> Zero-Step Location Index generation is attack-side only.

This leaves the canonical Zero-Step mechanism completely untouched. The existing canonical mechanism still derives location from the attacker's natural roll. Tiwas___S2_Hit_Location_Investi…

One terminology point I'd preserve

I would retain Claude's distinction between:

> "Non-attack Location Index is prohibited for now"

and

> "Non-attack Location Index can never exist."

The ruling is the former.

The future subsystems you've identified—S-4, S-7, and S-8—are reopening triggers, not merely implementation dependencies. When one of those systems is designed, the question should be explicitly reopened rather than assumed to inherit the old H0 answer.

What happens to H0?

I agree with Claude that H0 should remain in the investigation record rather than being deleted.

Its status is now:

> Superseded/inert candidate analysis — not an operative rule.

If non-attack location is reopened later, H0 provides a starting hypothesis:

> existing governing Core Test → natural roll → Zero-Step

But it has not been validated as an operative rule, because the designer ruling makes the question moot under the current rules.

I also agree that no blind trial is needed

A blind trial would test how to generate a non-attack Location Index.

You've explicitly decided that there is no such generation at present.

So running examples to determine which roll should feed Zero-Step would be testing a mechanism you've just ruled out. That would add evidence without answering a live design question.

Recommended status

I'd record the investigation as:

> S-2 Non-Attack Location Source — Deferred by Designer Ruling

| Item | Status |
| --- | --- |
| Attack Location Index / Zero-Step | Canonical / Locked |
| Non-attack Location Index | Ruled: none generated for now |
| H0 provenance rule | Retained as inert candidate record |
| GM-authored hazard warrant | Deferred/rejected for now |
| Named-Outcome transfer to hazards | Deferred |
| Blind provenance trial | Not required |
| Reopening trigger | S-4 / S-7 / S-8 design work |

And importantly, this does not alter Structural Weak Points = State 2 or any of the other previously settled S-2 classifications.

I would consider the S-2 Non-Attack Location Source investigation substantively closed for now, pending one of those explicit reopening triggers.