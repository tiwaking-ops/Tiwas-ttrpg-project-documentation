# Tiwas S-2 Design Investigation — Location Granularity Policy

**Status: Design investigation output — NON-CANONICAL until accepted by the designer**
**Question addressed:** What rule determines whether location information is required for a situation, and what granularity is appropriate?
**Explicitly not reopened:** Zero-Step (Canonical Rules §14.1–§14.2), S-1, anatomical mapping, Tier-2 mechanics, Wound/Armor/Defence/Effect numerical rules.

---

## 1. Executive Conclusion

**[Design inference]** Location granularity is best modeled as **consequence-driven**, not scene-driven or action-driven: location data (a Tier-1 Index or higher) should be generated only when an active downstream rule will actually consume it, not because a combat scene exists or because an action is labeled a certain way.

**[Recommendation]** Adopt a **hybrid consequence/action policy** (Candidate D, §4.4): a scene may set a *ceiling* on what tier is available, but within that ceiling, whether location is generated for any single resolution is triggered by a **short, closed list of consequence triggers** (declared called attack, active Effect selection, targeting equipment, or an active Wound-consuming rule) — never by the mere existence of combat.

**[Unresolved designer decision]** Two genuinely viable candidates remain after evaluation (Consequence-only vs. Hybrid). §9 presents both for designer ruling; this document does not force a winner between them.

---

## 2. Design Problem Definition

**[Architectural constraint, restated from source brief]** The question is not "which tier does a scene use" — that presumes tier-selection is scene-level. The actual open question is:

> What triggers the generation of location information at all, and at what granularity, for a given resolution?

**[Architectural constraint]** Per Canonical Rules §14.3, the following remain unresolved and are inputs to this investigation, not outputs of it:
- whether/when a scene uses Tier 0, 1, or 2;
- anatomical mapping;
- Wound/Armor/Defence/Effect interaction.

**[Architectural constraint]** Per Canonical Rules §14.2, Tier-1 derivation is a **read-only post-process** of the attacker's natural roll. This has one structural consequence for this investigation: Tier 1 is not costed like a normal subsystem call. It requires no additional roll, no additional resource expenditure, and no alteration of Cost/Overflow/Failure XP/Doubles/Recovery. Its "cost" is *procedural and cognitive* (does the table get consulted, does the GM/player have to do the digit-swap), not mechanical-resource cost. This matters directly for Priority 3 evaluation below.

---

## 3. What Each Tier Is Actually For

### 3.1 Tier 0 — No location state

**[Design inference]** Information deliberately discarded: which body part or zone was affected.

**[Design inference]** Why discarding it is acceptable: in scenes where no rule downstream of the Core Test consumes location (no Effect selects it, no Wound system reads it, no armor/defence interaction depends on it), retaining it produces bookkeeping with zero mechanical payoff — a direct violation of Priority 3. Tier 0 is not "a worse Tier 1"; it is the correct choice whenever nothing in the resolution chain needs a location.

### 3.2 Tier 1 — Zero-Step Location Index

**[Canonical fact]** The derivation mechanism (Zero-Step) is settled and out of scope here.

**[Design inference]** The open question is what *creates the need* for the index. Candidate consumers, treated as hypotheses rather than assumptions:

| Candidate trigger | Plausible? | Reasoning |
|---|---|---|
| Ordinary, undeclared attacks | Weak | Generates location data for the majority of rolls even when nothing reads it yet (no Wound/Armor system is locked) — pure overhead today |
| Called/aimed attacks (declared intent) | Strong | Player explicitly wants a location outcome; the index directly serves the declared intent |
| Attacks in formal duels | Situational | Only relevant if duel rules specifically consume location (not yet established) — otherwise it's a scene-based justification masquerading as intent |
| Attacks against equipment | Strong | Equipment Damage is already a named candidate Effect (Proposals §3.1 item 9); targeting gear plausibly needs a location-equivalent index |
| Any resolution invoking a location-consuming Effect (e.g., "Choose Location," future Wound trigger) | Strong | This is the direct, minimal-overhead case: the Effect layer asks for a location, S-2 supplies it |
| Gritty/high-granularity scenes generally | Weak as sole trigger | Reintroduces scene-based logic through the back door unless tied to an actual consequence within that scene |

**[Design inference]** Tier 1 is cheapest exactly in the cases where it is *needed* — declared called attacks and Effect/Wound consumption — because it piggybacks on a roll that already happened. This is a structural point in favor of consequence-based invocation: the "expensive" case (running the digit-swap on every roll of a mass battle) is also the case where nothing needs the result.

### 3.3 Tier 2 — reserved

**[Recommendation]** No sufficiently concrete purpose currently exists. S-4 (Wounds) is open, no anatomical mapping is canonical, and no rule currently claims to need finer-than-Zero-Step resolution. Per the brief's own instruction, this document **does not design Tier 2** and explicitly recommends it **remain Reserved** until a consuming rule (most likely a future surgery/precision-medical or optional gritty-combat module) articulates a specific need that Tier 1 cannot serve.

---

## 4. Candidate Policies

### 4.1 Candidate A — Scene-Based

A scene, encounter, or campaign is flagged with a fixed tier (e.g., "this campaign runs Tier 1 combat"). All qualifying tests within that scope generate location data at that tier, regardless of whether any specific resolution needs it.

### 4.2 Candidate B — Action/Intent-Based

Tier follows the declared action: an ordinary strike = Tier 0; a called/aimed strike = Tier 1; a surgical/precision action = Tier 2 (once Tier 2 exists). Determined per action, by the acting player's declaration.

### 4.3 Candidate C — Consequence-Based

Location data is generated only when an active rule in the resolution chain actually consumes it: an Effect selection requiring location, an active Wound-system read, an equipment-targeting rule, etc. No consequence-consumer present → no location data, regardless of scene or declared action flavor.

### 4.4 Candidate D — Hybrid (Ceiling + Consequence Trigger)

A scene may optionally set a **ceiling** ("this scene permits up to Tier 1"; a pure narrative brawl might cap at Tier 0 even if a called attack is declared). Within that ceiling, actual generation of location data per resolution is governed by a **closed trigger list**: declared called attack, active location-consuming Effect, equipment-targeting, or an active Wound-consuming rule. The ceiling prevents Tier 2 (once it exists) from appearing uninvited in a cinematic mass brawl; the trigger list prevents Tier 1 overhead on every ordinary swing.

---

## 5. Scenario Walkthroughs

For each scenario: does location generate, at what tier, who/what determines it, what extra step occurs, what is deliberately not generated — evaluated per candidate.

| Scenario | A — Scene-Based | B — Action-Based | C — Consequence-Based | D — Hybrid |
|---|---|---|---|---|
| **Mass brawl** (many combatants, low individual stakes) | Scene set to Tier 0 → no location ever, even if someone calls a shot | Tier follows each declaration; a called shot mid-brawl still forces Tier 1 bookkeeping the scene doesn't need | No Effect/Wound consumer active in a mass-brawl abstraction → Tier 0 by default; a called shot only generates if it also triggers a real consumer | Ceiling = Tier 0 for the scene; called-shot declarations are disallowed or narratively resolved without index generation |
| **Ordinary 1-on-1 combat**, no called shots | Depends entirely on scene's assigned tier (could be needlessly Tier 1) | Tier 0 by default (no called shot declared) | Tier 0 unless something downstream (e.g., a Wound trigger threshold) actively consumes location | Ceiling permits Tier 1 but trigger list is empty → Tier 0 in practice |
| **Formal duel** | Scene likely flagged Tier 1 "because it's a duel" — a scene-level assumption, not a mechanical need | Depends on individual declarations, not duel status itself | Tier 0 unless duel rules (not yet locked) explicitly define location consumption | Ceiling may be raised to Tier 1 for duels by convention, but generation still requires an actual trigger |
| **Called attack** ("I aim for the arm") | Generated only if the scene already permits it — a called attack in a Tier-0 scene is mechanically inert | Tier 1 always, by definition of the action type | Tier 1 generates because the declared intent *is* the consequence-trigger (declared called attack is one of the named triggers) | Tier 1 generates if within the scene's ceiling; blocked if ceiling is Tier 0 |
| **Attack targeting equipment** | Only if scene tier already covers it | Not naturally covered by "action type" unless equipment-targeting is defined as its own action category | Tier 1 generates directly — equipment-targeting is a named consequence-trigger | Tier 1 generates if within ceiling |
| **Attack with no mechanical consequence for location** (e.g., no Effect/Wound system active in this session) | Still generates if scene tier ≥1 — pure overhead | Still generates if declared as a called shot — pure overhead if nothing reads it | Never generates — correctly identifies there is nothing to serve | Never generates — trigger list finds nothing to fire |
| **Attack where a future Wound system would require location** | Generates only if scene tier happens to be set high enough — accidental correctness | Generates only if the specific action was declared "called" — misses ordinary attacks a Wound system might still care about | Generates directly, because the Wound system is itself the consequence-trigger | Generates directly, same as C, gated by ceiling (Wound-consumption should normally be within any combat scene's ceiling) |
| **Cinematic scene** (heroic action-movie combat, deliberately low granularity) | Scene set to Tier 0 — works well | Works if the table agrees not to declare called shots; a rules-lawyering player can still force Tier 1 bookkeeping mid-scene | Naturally stays Tier 0 unless a player forces a consequence-consumer into play | Ceiling = Tier 0 caps it regardless of declarations — strongest protection against genre-breaking bookkeeping |
| **Gritty/high-granularity scene** | Scene set to Tier 1 (or future Tier 2) — works, but forces the tier onto every roll in the scene even trivial ones | Works naturally — most actions get declared with intent in this mode anyway | Requires the table to actively invoke consequence-consumers (e.g., always selecting the "Choose Location" Effect) — correct but places burden on players to opt in each time | Ceiling raised to match the scene's granularity; consequence triggers still gate individual resolutions — avoids blanket overhead even in a "gritty" scene |

---

## 6. Comparative Evaluation

| Criterion | A — Scene | B — Action | C — Consequence | D — Hybrid |
|---|---|---|---|---|
| Resolution-step cost | Fixed, but often wasted (generates unused data) | Variable; scales with declaration frequency, not actual need | Minimal — only fires when needed | Minimal, with a small added check (ceiling lookup) |
| Table/reference friction | Low (one flag per scene) | Low-medium (per-action judgment) | Low, but requires the GM/players to recognize when a rule "wants" location | Medium — two-part rule (ceiling + trigger) is more to remember |
| Player agency | None over granularity | High — player declares tier via action | Indirect — agency exists only via choosing to trigger a consumer (e.g., selecting an Effect) | High within the ceiling; capped by GM/scene-level ceiling |
| GM burden | Low ongoing, but requires upfront scene-tagging discipline | Medium — GM must adjudicate whether a declared action qualifies as "called" | Low-medium — GM must recognize valid triggers consistently | Medium — GM sets ceiling once, then adjudicates triggers as in C |
| Simulation fidelity | Mismatched to situation (all-or-nothing per scene) | Good — fidelity follows genuine intent | Best — fidelity generated exactly where mechanically meaningful | Best, with a genre/tone safety rail added |
| Exploitability / manipulation | Low (fixed by GM) | **High** — a player can spam "called shot" declarations to force favorable location outcomes in scenes that shouldn't support it, or exploit ambiguity in what counts as "called" | Medium — a player could try to force triggers by always selecting the "Choose Location" Effect; but this is a fair use of an existing purchased Effect, not a loophole | Medium-low — ceiling limits how far action-declaration exploitation can go, since the scene tone still bounds what's possible |
| Consistency | High within a scene, low across scenes of the same "type" | Low — same fight can whipsaw between tiers turn to turn | High — consistent rule (does a consumer exist), independent of scene labeling | High — consistent two-layer rule |
| Compatibility with future Wounds (S-4) | Accidental — depends on whether scene tier happened to be set correctly | Accidental — depends on whether the relevant attack got declared "called" | **Direct** — Wound system becomes a first-class consequence-trigger by construction | Direct, same as C |
| Compatibility with future Armor (S-5) | Same accidental coupling issue | Same accidental coupling issue | Direct — armor/bypass interaction can be defined as another named trigger | Direct |
| Compatibility with Effects (S-3) | Indirect | Indirect | **Direct** — "Choose Location" Effect (Proposals §3.1 item 10) is literally already a consequence-trigger in this model | Direct |
| Compatibility with Core architecture | Fine — doesn't touch the Core Test | Fine | Fine — remains a pure post-process, consistent with §14.2's read-only framing | Fine |
| Priority 1 (granular simulation where warranted) | Weak — granularity is scene-wide, not situation-warranted | Medium — granularity follows stated intent, which is a reasonable proxy for "where warranted" | **Strong** — granularity generated exactly where the simulation need exists | Strong, with tone control added |
| Priority 3 (minimum resolution steps) | Weak — generates unused data in low-stakes scenes | Medium — still generates data for called shots that don't feed anything (if S-3/S-4 aren't active) | **Strongest** — by construction, nothing generates without a consumer | Strong — nearly as lean as C, with one extra ceiling check |

---

## 7. Architectural Implications

**[Architectural constraint]** Whichever policy is chosen, it must remain a pure *invocation* layer sitting in front of the already-locked Zero-Step provider. It selects *whether* and *when* to call Zero-Step; it must never modify what Zero-Step returns, and per §14.2 it cannot touch Cost, Overflow, Failure XP, Doubles, or Recovery.

**[Design inference]** Candidate C (and by extension D) creates a clean seam with S-3 (Outcome Effects): the existing candidate Effect "Choose Location" (Proposals §3.1 item 10) becomes the canonical example of a consequence-trigger, rather than a redundant or competing mechanism. This suggests S-3's Effect menu and S-2's granularity policy are more tightly coupled than the Roadmap's dependency graph currently shows them (S-2 listed as feeding S-4 primarily) — worth flagging to the designer as a possible dependency-graph refinement, not a rules change.

**[Design inference]** Candidate B's exploitability finding (spammable "called shot" declarations) is a genuine downstream risk: without a consequence gate, "call a shot" becomes a free way to manufacture location data even in scenes with no location-consuming rule active, since nothing constrains *why* a called shot should matter mechanically. This is the strongest single argument against B as a standalone policy.

**[Design inference]** Candidate A's core weakness is that it re-imports exactly the kind of upfront, blanket granularity decision that Priority 3 exists to avoid — it decides for an entire scene what should be decided per-resolution.

---

## 8. Recommendation

**[Recommendation]** Adopt **consequence-based invocation** as the governing principle (Candidate C), optionally wrapped in a scene-level **ceiling** (Candidate D) purely as a tone/genre control, not as the actual granularity-determining mechanism.

Concretely:
- Location data (Tier 1, and eventually Tier 2) is generated **only** when a specific, named downstream rule requires it for that resolution — an Effect selection, a Wound-system read, an equipment-targeting rule, or an explicitly declared called attack that the GM has confirmed maps to an actual mechanical consequence.
- A scene may optionally cap the maximum tier available (primarily to protect cinematic/mass-combat tone from being derailed by an isolated called-shot declaration), but the cap is a ceiling, not a trigger.
- Tier 0 remains the default state for any resolution where no trigger fires.

This directly serves Priority 3 (data is generated exactly where warranted, nowhere else) without weakening Priority 1 (any situation that genuinely needs granularity gets it, unconstrained by scene labeling).

---

## 9. Remaining Designer Decisions

**[Unresolved designer decision]** This document does not force a single winner between:

1. **Pure Consequence-Based (C)** — leanest, most consistent, no scene-level override; risk: no built-in protection against an edge case where a player forces a trigger (e.g., always selecting "Choose Location") in a scene the GM intended to keep abstract.
2. **Hybrid Ceiling + Consequence (D)** — same core benefits as C, plus a tone/genre safety rail for the GM; cost: one additional rule component to teach and remember.

The designer should rule on:
- whether a scene-level ceiling is worth the added rule surface, or whether trusting consequence-triggers alone (with ordinary GM adjudication) is sufficient;
- the exact closed list of valid Tier-1 triggers (this document proposes: active location-consuming Effect, active Wound-system read, equipment-targeting rule, GM-confirmed called attack — but the final list is a designer call, not derived here);
- whether "GM-confirmed called attack" needs its own light adjudication procedure to close the exploitability gap identified in §6/§7, or whether ordinary GM discretion is sufficient.

**[Unresolved designer decision]** Whether Tier 2, once a purpose is articulated, should be gated by the same trigger-list architecture or requires its own separate invocation rule (e.g., only reachable via an explicit non-combat "surgery" or "precision procedure" action type rather than any combat trigger).

---

## 10. Proposed Next Design Question

With a granularity-invocation policy pending designer ruling, the next coherent design step is:

> **S-2/S-3 interface:** Define the exact mechanical shape of the "Choose Location" Effect and any Wound-read trigger — i.e., specify the closed trigger list itself as a formal rule, rather than the illustrative list in §9 — without yet designing the anatomical mapping table or Tier-2 mechanics.

This keeps the dependency order intact: location policy → location invocation → location provider (done) → Location Index (done) → anatomical mapping (still not started) → wound/armor/effect consumers (still not started).
