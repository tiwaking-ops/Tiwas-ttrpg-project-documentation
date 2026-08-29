# Proposed replacement text — Proposals, WIP & Design Direction, Section 2 (S-2 — Hit-Location Architecture)

**Target version: v1.4.2** (update to Proposals, WIP & Design Direction v1.4.1). **Correction pass (this revision):** three fixes applied after independent review and re-verification against the source synthesis, matching the corrections made in the synthesis document itself. No classification (Anchor status, W3 State) or open/closed status changed — only overclaiming or incomplete basis text was reworded.

1. §2.1A Conceptual Anchor table — **Armor bypass** basis reworded; "direct contradiction, not silence" overclaimed against what Proposals §5 (this same document) actually says. §5 states a Tags-based preference and never addresses location; that's a documented alternative mechanism (which is what the Anchor test requires for Unanchored status), not a stated contradiction.
2. §2.1A Conceptual Anchor table — **Structural weak points** given a scope note distinguishing narrative resolvability (settled) from the Index→component anatomical mapping (still open per §2.5).
3. §2.1A Procedural riders — **lazy evaluation** flagged with its correct evidence class (design inference, not equivalent to the other three replicated procedural riders), matching the correction made to the source synthesis §5 and to the Roadmap patch.

Also added: a lead-in caution above the Conceptual Anchor table clarifying its evidence class relative to the Named-Outcome Test.

**How to use this file:** this is drafted as a direct replacement for the current §2 of the Proposals/WIP document (and a light addition to §2.5 and the §20 decision register), reflecting the S-2 Design Investigation v1–v5 record. It does not change Canonical Rules. It does not lock S-2. Insert in place of the existing §2 after your own review.

---

# 2. S-2 — Hit-Location Architecture

**Status: Partially locked / WIP — Tier-1 Location Index provider locked. Invocation/warrant policy: Candidate policy accepted for further development; not yet promoted to Canonical.**

**Zero-Step is locked; the broader S-2 architecture, including the warrant policy below, is not.**

The Canonical Rules record a **Canonical / Locked — limited S-2 decision**: only the Tier-1 Location Index provider (Zero-Step) is locked. Tier policy, anatomical mapping, and downstream interactions remain unresolved. A separate, extensive non-canonical investigation (S-2 Design Investigation v1–v5) has produced a **candidate invocation/warrant policy**, summarized below and detailed in the investigation record. This candidate policy is accepted as the current working direction for S-2's invocation question but has not completed the promotion process in §21 and does not modify this document's non-canonical status.

## 2.1 Limited locked S-2 decision

Unchanged from v1.4.1 — Zero-Step remains the locked Tier-1 provider per Canonical Rules §14.1–§14.2. Not reopened by this update.

## 2.1A S-2 Candidate Invocation Policy (New — Non-Canonical)

The S-2 Design Investigation (v1–v5) proposes the following as a candidate answer to "when should Tiwas generate a Tier-1 Location Index":

**Four-state classification (internal/documentation architecture):**

1. **Established & Resolvable** — location-dependence is conceptually anchored and current rules can act on it → generate.
2. **Established, Not Yet Resolvable** — anchored, but no current rule can act on the result yet → do not generate; record as pending.
3. **Outcome Plausible, Location-Dependence Unresolved** — the named consequence is a reasonable future outcome, but whether location specifically delivers it is an open design fork, not just an unimplemented detail → do not generate.
4. **No Distinct Consequence** — no distinct outcome named → do not generate.

**GM-facing procedure (simplified, draft):**

> Generate a Location Index only when the player has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design (not merely plausible or anticipated), and current rules can actually resolve it.

**Warrant test (Named-Outcome Test):** a declared objective is definite — and Warrant-eligible — only if the player explicitly names a distinct consequence, other than ordinary damage, tied to the specified location. Conditional phrasing does not defeat definiteness; stated purpose/motivation without a named distinct outcome does not establish it.

**Designer rulings adopted into this candidate policy:**
- **Explicit-only objectives.** The GM does not infer an unstated distinct objective from location or fictional context alone.

**Procedural riders (carried into the candidate policy):**
- Compound objectives evaluated disjunctively.
- Stale objectives (fictional state no longer supports the category's rationale) void an otherwise-matching case.
- In S-1 opposed contests, only the winning participant's natural roll is eligible for Location Index generation (per Canonical §13.2 — Quality never alters either participant's historical roll).
- Location Index evaluation may be deferred (lazy evaluation) to whenever a downstream stage first needs the answer, since Zero-Step is a read-only post-process of an already-recorded roll (Canonical §14.2). *(Design inference, provisionally adopted — not separately stress-tested at the table, unlike the three procedural riders above.)*

**Conceptual Anchor findings (current, subject to revision as S-3/S-5/S-7/S-10 develop):**

**Note:** the table below reflects design inference tested against source documents (the Conceptual Anchor Challenge), not blind-trial data. It does not carry the same evidentiary weight as the Named-Outcome Test above, which was validated against 21/21 trial cases.

| Concept | State | Basis |
|---|---|---|
| Structural weak points (hinges, supports, load-bearing components) | **1 (Established & Resolvable)** | Resolvable via ordinary GM narration; no subsystem dependency. This covers narrative differentiation only — the numeric Location Index→component mapping remains a separate, still-open question (see §2.5), not settled by this status. |
| Disarm / Break Hold | **3** | §3.2 below already contemplates Margin/Tag-gated triggering as an alternative to location; location-mechanism unresolved |
| Equipment damage | **3** | Same basis |
| Function impairment (blindness, movement) | **3** | §10 Conditions have no stated activation mechanism |
| Armor bypass | **3** | §5 below documents Tag/Trait-based interaction as the current design direction — a documented alternative mechanism, which is what this table's Anchor test requires for Unanchored/State-3 status. §5 emphasizes Tags and does not itself address whether location also participates; that is a gap, not a stated contradiction. |
| Incapacitation / kill | **3, circularly** | §4.1/§7 below condition localized injury on locations already being active — this concept cannot be resolved independently of the S-2 decision itself |

**Important:** entries at State 3 are *not* Watch-list entries pending implementation. They record an unresolved design fork (is location the mechanism at all), not merely missing numbers. They should be revisited only when the relevant future subsystem makes an explicit choice that location is how the outcome is delivered — not merely when that subsystem locks in any form.

**W3 cache role (revised):** the cache is a maintained shorthand for situations already established at State 1 or 2 by the policy above. It does not independently establish Warrant or Anchor status. Novel, uncached situations are still evaluated directly against the policy (confirmed by two independent novel-case trials during the investigation, both resolving correctly without cache membership).

## 2.2 Purpose of remaining S-2 work

Unchanged from v1.4.1.

## 2.3 Location-granularity tiers

Unchanged from v1.4.1.

## 2.4 Architecture retained as WIP

Unchanged from v1.4.1.

## 2.5 Open design questions

Revise the existing list to reflect what the investigation resolved and what remains:

- whether the location tier is universally fixed or selected by situation, scene or campaign — **still open.** The candidate invocation policy determines *when a Location Index is warranted within whatever tier is in use*; it does not determine *whether a scene/campaign uses Tier 0, Tier 1, or Tier 2* in the first place. The candidate policy is a relevant input to that future decision, not a resolution of it.
- when Tier 1 is invoked — **the mechanism for this is now addressed** (the candidate invocation policy directly answers "does this specific resolution warrant a Location Index"), but this is narrower than the scene/campaign tier-selection question above, which remains open.
- the anatomical mapping table (numeric Location Index → structural/anatomical component) — still open, untouched by this investigation. This includes the structural-destruction case in §2.1A's Conceptual Anchor table: its State-1 status establishes narrative resolvability only, not a settled mapping.
- Tier-2 procedure and resolution cost — still open, untouched.
- interaction with wounds, armour, defence and Outcome Effects — still open; the investigation's State-3 findings (Disarm, Equipment, Impairment, Armor Bypass, Incapacitation all currently unanchored to location) are directly relevant inputs to this future work.
- **New:** whose roll, if any, supplies a Location Index for non-attack physical resolutions (hazards, falls, structural interactions with no adversarial "attacker") — identified by the investigation as a distinct, narrower open question, not resolved here.
- **New:** final GM-facing wording for the simplified invocation procedure (§2.1A) — drafted, not yet separately validated.

## 2.6–2.8

Unchanged from v1.4.1, except that the E9 usability finding and derivation-cost residual remain scoped exactly as before — this update does not touch that material.

---

# Proposed addition to Section 20 (Open Residual Decision Register)

Update the S-2 row:

| ID | Decision | Current status |
|---|---|---|
| S-2 | Broader hit-location architecture: tier policy, mapping and downstream interaction. Zero-Step (Tier-1 Location Index provider) is locked. **Invocation/warrant policy: candidate accepted (S-2 Design Investigation v1–v5), non-canonical, pending promotion.** Anatomical mapping, Tier-2 procedure, and non-attack-resolution scope remain fully open. | Partially locked / WIP — Tier-1 provider locked; candidate invocation policy accepted for further development |
