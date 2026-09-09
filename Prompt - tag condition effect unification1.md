Role You are a senior TTRPG systems designer reviewing an architectural change to an in-development game. You have full license to challenge the proposal's premises, surface conflicts with existing rulings, and rank trade-offs honestly — even against the designer's stated direction. Be direct, not deferential.

Context I'm designing Tiwas, a d100 TTRPG. It currently maintains three separate but overlapping subsystems — Tags, Effects (Outcome Effects), and Conditions — each with its own record format, production rule, and removal rules. My goal is to reduce rulebook complexity. I want to define them as three fiction-level concepts sharing one mechanical backbone (a single record type with Tier Y, Magnitude Z, and optional Location X), rather than three genuinely independent subsystems.

My proposal, expressed as a difficulty-reduction hypothesis:

Tags are like Effects, but Tags are Permanent; Effects are caused by a Skill Roll.
Clarify: "Permanent" is a default state, not an absolute — Tags default to persistent but can be removed by named actions/Effects. Effects default to temporary but can be made permanent via Tier/Magnitude.
Tags, like Effects, have Tier Y Magnitude Z. Tags may also have Location X.
Tags can counter other Tags (e.g., a creature-side ignores darkness countering env:darkness).
Tags and Conditions are NOT distinct.
Tags can be Removed.
The existing system makes several claims that interact with these ideas:

Proposals §11: "Tags are classification and permission metadata … Tags are not Conditions."
Tags carry identity/vocabulary only (DEC-080 Q4); mechanical effects live in consuming subsystems.
Tags are read-only, stateless — no resource economy, never create/consume/modify pools (Decisions DEC-058/079/080/088; Invariant 17 / REQ-017; DEC-007.A makes Overflow immutable against any Tag/Trait/Effect/Condition).
Conditions have a distinct record format Tier-Y Condition Value Z (global) or Location X … (localized), with Z = −Y (Decision DEC-079) and specific stacking/removal rules per condition.
Effects are selectable payloads from winning an S-1 opposed contest (DEC-023–030, 107), one per win, auto-apply (DEC-027), tag+location gated for equipment-tier (DEC-028/041/114).
No general tag-removal rule exists; only the Sundered tag is "permanent until repaired" (DEC-060/079).
A formal tag/category system on Skills was already rejected (DEC-025).
None of this is canonical — all these rulings are non-canonical "designer rulings" pending an 8-step promotion process.
Deliverable I'm after: a Decision Draft (not merely options-analysis) — a concrete, adoptable unification proposal.

Audience Myself only. It's a working document to evaluate and refine before I rule on it. No players, no collaborators will read it directly — though it may later seed a governance document. Technical fluency assumed; no need to pad for laypeople.

Format and length Structured markdown, aimed at roughly 1,500–2,500 words (flexible). Suggested sections:

Executive verdict — is the unification worth it (or not), in 5–10 lines.
What "one mechanical backbone" actually means — the unified record schema (Tier Y, Magnitude Z, optional Location X) and how Types/Subtypes preserve Tags/Effects/Conditions as fiction-level concepts.
Impact analysis of each of my five ideas — for each: what it changes, what it breaks or conflicts with (cite DEC/Invariant where relevant), what it fixes.
The complexity math — does this actually reduce rulebook complexity, or just move it? (Be honest: a shared schema + a permanence rule + a counter rule + removal rules could add as much as it removes.)
Conflicts and honest tensions — especially: (a) "Tags counter Tags" vs. the stateless/read-only guardrail; (b) "Tags and Conditions are NOT distinct" vs. the current distinct-format/stacking design; (c) my permanence/removal phrasing (which I've partially resolved above); (d) whether UNIFYING re-opens DEC-025 (the rejected Skill-tag system).
Concrete recommended design — the minimal unification that maximizes complexity reduction while respecting the non-canonical status of prior rulings (i.e., it doesn't need to preserve them, but should flag where it departs and what's lost).
Open questions I must rule on — a short bulleted list, not a full decision-register.
Success criteria A great answer, versus a mediocre one:

Honesty about the core tension — it cannot just affirm the unification; it must grapple with whether one backbone genuinely reduces total system weight, or merely relocates it. A mediocre answer promotes the merge uncritically.
Concreteness — the recommended schema and rules are specific enough to adopt (exact fields, exact precedence when Tag-counter meets Tag), not a high-level "Tags and Conditions are the same now."
Conflict fidelity — it correctly identifies which existing rulings (by DEC number / Invariant) the proposal breaks or touches, and distinguishes the "this is a real conflict" cases from the "this was never truly specified" cases.
Constraints

Do not present the unification as canonical or final. Everything proposed here is a designer's ruling draft pending formal promotion; frame accordingly.
Do not invent rules the original text doesn't have (e.g., don't invent a "permanence attribute" field unless you specify it crisply).
Do not reintroduce a resource economy — tags must stay stateless in the sense of no HP/Overflow/pool modification (respect DEC-007.A / Invariant 17), even if your counter-mechanic differs from the current read-only model. If you think the counter-mechanic requires violating this, say so explicitly and weigh it.
Preserve the no-double-roll / single-resolution-engine constraints — no unified system may create a second resolution engine or a second primary resource.
Keep the fiction-level distinction of Tags/Effects/Conditions (per my stated intent), even as the mechanics merge.
Examples No written examples exist yet — this is the first articulation. You may use the concrete cases I mentioned (the Ice Troll's env:freezing-gated Traits; the env:darkness/Night-Vision counter-tag gap; the Sundered condition-as-tag) as worked illustrations.