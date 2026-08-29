---
document:
  title: "S-2 Non-Attack Location Index Source — ChatGPT critique (Round 1 review)"
  status: "LLM-produced assessment (not canonical, not a designer ruling)"
provenance:
  author_llm:
    name: "chatgpt"
    version: "not established"
  assessor_llm:
    name: "not yet assessed"
    version: ""
  last_modified_by_llm:
    name: "opencode"
    version: "big-pickle"
  created_date: "not established"
  last_modified_date: "2026-08-30"
recovery:
  source: "Shared ChatGPT conversation (title: 'DONE Tiwas Location Index Analysis')"
  share_link: "https://chatgpt.com/share/6a934e83-f1f0-83ec-8752-38c7fe566acb"
  recovery_method: "Headless-browser render of the share page; text extracted from the rendered DOM"
  recovery_date: "2026-08-30"
  notes: >
    This document was never saved as a standalone file. Its content was uploaded into a
    Claude chat as a blank-name attachment — evidenced in the Claude export only by the text
    "ChatGPT says:" at the upload line — and copy-pasted directly between ChatGPT and Claude.
    This standalone copy was transcribed from the ChatGPT share (first assistant message) on
    2026-08-30; it is a transcription, not an original file. The full five-message share is
    recorded in `sources/incoming/ChatGPT-DONE Tiwas Location Index Analysis-20260830-share.md`.
    The critique is ChatGPT's assessment of Claude's Round 1 synthesis for the S-2 Non-Attack
    Location Source investigation, before the designer's final ruling.
---
# S-2 Non-Attack Location Index Source — ChatGPT critique (Round 1 review)

**Evidence class:** LLM-generated assessment (ChatGPT) of Claude's Round 1 cross-review
material for the S-2 Non-Attack Location Source investigation, as it stood before the
designer's final ruling. **Not a designer ruling.** Nothing in this document is canonical.
The live position on this investigation is the designer deferral ruling in Proposals/WIP
v1.4.3 §2.5A.

Claude's Round 1 is stronger and more disciplined than my previous pass, particularly on one
point: it correctly separates the location-source question from the invocation-policy
transfer question instead of quietly resolving both at once.

I agree with its core candidate, with one qualification.

1. Where Claude is right

The strongest part is the A/C/D collapse:

> No Core Test roll → no Location Index. Where a Core Test exists, its natural roll is
> Zero-Step's input.

That is the cleanest architectural answer.

It preserves the existing Zero-Step rule rather than creating a new "hazard roll," and it
fits the established architecture that location is a read-only post-process of an
already-recorded natural roll. The Roadmap likewise says Universal Play modules must call
the Core Test transaction rather than create a competing resolution engine.

I would therefore accept Claude's rejection of Candidate B as the correct working position:

> Ad-hoc GM d100 solely to obtain location = not permitted under the current architecture.

That is stronger than merely saying it is "not preferred."

2. The important refinement

I would not yet adopt Claude's wording:

> "already adjudicated by an ordinary Core Test belonging to some character"

as the final architectural rule.

The broader and safer formulation is the one Claude itself reaches in §8:

> Where a Core Test exists, its natural roll is Zero-Step's input.

Why? Because "belonging to some character" potentially assumes something about future hazard
architecture that this investigation has not actually established.

The real invariant appears to be:

> Does the physical outcome have an existing governing Core Test with a natural d100 roll?
>
> If yes → that roll can feed Zero-Step.
>
> If no → Zero-Step has no input.

That leaves open, without deciding it, whether a future hazard subsystem might define a
legitimate Core Test whose participant isn't neatly described as "the affected character."

So I'd retain "governing Core Test" rather than "Core Test belonging to some character."

3. Claude correctly identifies the next unresolved question

This is where I think Claude's response improves substantially on mine.

It does not claim that the existing Named-Outcome Test automatically transfers to hazards.

That is correct.

The existing candidate policy specifically says:

> the player must explicitly state a distinct consequence.

And the accepted investigation explicitly framed the Named-Outcome Test around a declared
objective.

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

> Treat non-attack cases as categorically State 3 or State 4 by default until a future
> subsystem explicitly says otherwise.

I don't think we should adopt that as a candidate yet.

The reason is that it risks conflating "there is no player-declared objective" with
"location-dependence is unresolved or no distinct consequence exists."

Those aren't necessarily the same thing.

For example, imagine a future hazard rule explicitly establishes:

> A collapsing structure can cause a localized structural impact whose location matters.

That could establish location-dependence independently of an acting player's declared
objective.

Calling every such case State 3 merely because there was no player declaration would make
the four-state model do something it wasn't designed to do.

So I think Claude is right to leave this open.

5. Recommended next step

I agree with Claude that we should not make a designer ruling yet.

The next investigation round should test the candidate provenance rule while deliberately
keeping the warrant question separate.

I'd use the following working hypothesis:

> Working Hypothesis H1: A Tier-1 Location Index for a non-attack physical resolution can
> only be generated from the natural d100 roll of an existing governing Core Test. No
> separate location-only roll is generated. If no governing Core Test exists, there is no
> Zero-Step input and therefore no Location Index.

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
- A case where one character's test causes the event and another character's test resolves
  its impact.
- A case where an opposed contest is involved.

And crucially, for every case record two independent fields:

- Roll provenance: What natural roll, if any, supplies Zero-Step?
- Warrant status: Is a Location Index actually warranted under the existing candidate
  policy?

That prevents us from accidentally using the investigation to answer both questions
simultaneously.

Bottom line

I agree with Claude's Round 1 candidate analysis and would use it as the basis for Round 2.

The strongest current finding is:

> The absence of an attacker is not itself the architectural problem. The decisive question
> is whether there is an existing governing Core Test with a natural roll for Zero-Step to
> consume.

But non-attack warrant remains unresolved. We should not yet modify the Named-Outcome Test,
and we should not default all non-attack cases to State 3/4.

So my recommended status is:

> S-2 Non-Attack Location Source — Candidate H1 accepted for stress-testing; no designer
> ruling yet.

That keeps the investigation exactly where the Starter Brief intended it: source provenance
first, warrant transfer second.