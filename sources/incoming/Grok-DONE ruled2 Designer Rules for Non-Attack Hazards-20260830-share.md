# DONE ruled2 Designer Rules for Non-Attack Hazards

**Source:** Shared Grok Conversation  
**Share link:** [https://grok.com/share/c2hhcmQtMg_9cc88786-34db-407a-a501-44409131dfef](https://grok.com/share/c2hhcmQtMg_9cc88786-34db-407a-a501-44409131dfef)  
**Transcribed:** 8/30/2026 (headless-browser render of the share page)  
**Note:** This share verifies against the chat in which the user pasted the "S-2 Non-Attack Location Index Source — Architect Assessment" content for Grok's assessment. The Architect Assessment text itself appears in the Assistant message below.

## User:

> Pasted content (with attached file `Tiwas RPG Project Documentation.pdf`)

@Tiwas RPG Project Documentation.pdf

**Tiwas — Next S-2 Design Question: Non-Attack Location Index Source (Starter Brief v1.1)**

**Claude Says:**

**Designer Input Required — Explanation**

Two decision points in the Round 1 analysis are designer rulings, not derivable from existing rules. Here's why each one can't be closed by inference alone, and what's actually being decided.

**Decision Point 1: How does the Named-Outcome Test apply to a party that doesn't "declare" anything?**

**The problem**

The existing invocation policy (Proposals §2.1A) is built entirely around a player speech act: "I aim to disarm him" is what makes an outcome "definite" and Warrant-eligible. A collapsing bridge doesn't say anything. There is no declaring party for a hazard in the way there is for an attacker.

This isn't a wording gap I can quietly patch — the original policy's entire evidentiary basis (the 21/21 Named-Outcome trial, Proposals §2.1A) tested declared player intent specifically. Extending it to non-declared cases means extending a rule past the boundary of its own evidence, which is exactly the kind of move Roadmap §24 Rule 6 ("never silently resolve an open designer fork") prohibits an LLM from doing unilaterally.

**The two live options**

| Option | What it means mechanically | Cost |
|---|---|---|
| 1. GM-authored stakes substitute for player declaration | Before the hazard is rolled, the GM states the distinct non-damage consequence in the same way a player would ("if this bridge collapses under you, you'll be pinned under a support beam" = a stated, distinct outcome). Warrant-eligibility then works exactly like the existing policy, just with GM as the declaring party. | Requires no new test type, but needs its own validation — the existing 21/21 trial evidence doesn't cover GM-declared cases, only player-declared ones. |
| 2. Default non-attack hazards to State 3/4 until further subsystems exist | Non-attack physical resolution never generates a Location Index today, categorically — not because of a warrant judgment, but because there's no declaring party to run the test against. Revisit only once S-4 (Wounds), S-7 (Incapacitation), or S-8 (Stakes Gate) gives hazards their own resolution grammar. | Simpler, zero new evidence needed, but effectively shelves hazard-location entirely for an unknown number of future subsystems. |

These produce different real outcomes at the table today (Option 1 lets a well-framed trap generate a Location Index right now; Option 2 never does until later systems exist). That's a designer trade-off between "more granularity sooner" and "wait for the grammar to be built properly" — which is precisely a Priority-1-vs-Priority-3 tension (Canonical §1: granular simulation vs. minimum resolution steps). I can't resolve a stated design-priority trade-off; only you can weight it.

**Decision Point 2: Run a blind trial now, or wait?**

**The problem**

The starter brief (§5) explicitly says to decide this after a candidate answer exists, not in advance. I now have a candidate (§4's collapsed rule), but it's downstream of Decision Point 1 — the trial scenarios would need to actually exercise the GM-declaration mechanism (if Option 1 is chosen) or wouldn't need to test warrant-eligibility at all (if Option 2 is chosen, since the answer is just "never, categorically").

Running a blind trial before Decision Point 1 is settled risks the same failure mode the original investigation caught and corrected twice already (the Armor Bypass overclaim, the Structural Weak Points State 1→2 correction) — generating "confirmed" evidence for a rule that hasn't actually been fixed in its final shape yet, then having to walk back the evidence-labeling later.

**The trade-off**

- Trial now → faster iteration, but risk of re-labeling work later if Option 1/2 changes the test's shape.
- Trial after Decision 1 → slower, but the trial tests the actual candidate rule once, cleanly.

**Bottom line**

Neither point is something the existing documents settle, and neither is a "convenience" call I should make unilaterally per Roadmap §24 (Rules 4, 6, 9): both change what the ruleset does at the table, not just how it's implemented or worded. I can draft the mechanics for either option in detail once you pick one — I just can't pick for you.

## Assistant:

> Worked for 4s

**S-2 Non-Attack Location Index Source — Architect Assessment**

**Decision Point 1: Named-Outcome Test Application to Non-Declared Hazards**

**Core Constraint**

Existing Named-Outcome / Warrant policy (Proposals §2.1A) is evidence-bound to player speech acts. A hazard has no declaring party. Extending the rule past its evidentiary base without explicit designer choice violates Roadmap §24 Rule 6.

**Option Comparison**

| Criterion | Option 1: GM-Authored Stakes Substitute | Option 2: Default Non-Attack Hazards to State 3/4 |
|---|---|---|
| **Mechanics** | GM states distinct non-damage consequence before roll ("pinned under support beam"). Warrant test runs identically with GM as declaring party. | No Location Index generated for any non-attack physical resolution. Revisit only after S-4 / S-7 / S-8 supply dedicated grammar. |
| **Table Outcome Today** | Well-framed hazard can produce Location Index immediately. | Zero hazard-location output until later subsystems. |
| **Evidence Cost** | Requires new validation set (existing 21/21 trial covers only player declaration). | Zero new evidence required. |
| **Priority Alignment** | Favors Priority-1 (granular simulation) sooner. | Favors Priority-3 (minimum resolution steps) and structural integrity. |
| **Consistency Risk** | Medium — must keep GM declaration strictly parallel to player form or the test drifts. | None — categorical exclusion is clean. |
| **Future Coupling** | Couples S-2 tightly to future stakes language; risk of rework if S-8 changes stake grammar. | Clean deferral; S-2 remains stable while S-4/S-7/S-8 mature. |

**Mechanical Implication if Option 1 Chosen**

- Pre-roll GM statement becomes a formal "Declared Stake" record.
- Warrant-eligibility proceeds exactly as for player Named-Outcome.
- Failure mode: vague or multi-outcome GM phrasing must be rejected or force State 3/4 (same rejection logic as player side).

**Mechanical Implication if Option 2 Chosen**

- Non-attack resolution path simply never queries the Location Index table.
- All location generation remains attack-only until explicit future subsystem unlock.

**Decision Point 2: Blind Trial Timing**

**Dependency**

Any trial scenario set is downstream of Decision Point 1.

- Option 1 → trial must exercise GM-declaration form.
- Option 2 → trial is unnecessary for warrant-eligibility (answer is categorical "never").

**Risk Matrix**

| Timing | Benefit | Failure Mode |
|---|---|---|
| Trial now | Faster iteration cycle | Evidence labeled against provisional rule; later re-labeling required if Option changes. |
| Trial after Decision 1 | Single clean evidence pass | One extra design cycle. |

Prior investigations already produced two re-labeling events (Armor Bypass overclaim; Structural Weak Points State 1→2). Repeating that cost is avoidable.

**Architect Recommendation Structure (Not a Choice)**

- Resolve Decision Point 1 first. Weight Priority-1 vs Priority-3 explicitly. Record the ruling in the canonical decision log.
- Only after Decision Point 1 is locked, decide trial timing.
- If Option 1: construct trial scenarios that force GM-declaration language and edge cases (ambiguous stakes, multi-consequence phrasing, simultaneous hazard + attack).
- If Option 2: no warrant trial required; document categorical exclusion and move S-2 to "deferred pending S-4/S-7/S-8".
- No silent default. Either path changes observable table behavior. Both are Priority-1/3 trade-offs that only the designer can weight.

**Required Designer Input**

- Select Option 1 or Option 2 for Decision Point 1.
- Once selected, state whether a blind trial is authorized under the chosen option.

Once the ruling is received, the candidate rule text, formal test procedure, and (if authorized) trial scenario set will be drafted to the exact mechanical grain required by the system.