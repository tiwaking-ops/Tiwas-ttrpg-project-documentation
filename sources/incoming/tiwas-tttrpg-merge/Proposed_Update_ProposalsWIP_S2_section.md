# Proposed replacement text — Proposals, WIP & Design Direction, Section 2 (S-2 — Hit-Location Architecture)

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
- Location Index evaluation may be deferred (lazy evaluation) to whenever a downstream stage first needs the answer, since Zero-Step is a read-only post-process of an already-recorded roll (Canonical §14.2).

**Conceptual Anchor findings (current, subject to revision as S-3/S-5/S-7/S-10 develop):**

| Concept | State | Basis |
|---|---|---|
| Structural weak points (hinges, supports, load-bearing components) | **1 (Established & Resolvable)** | Resolvable through ordinary physical narration; no subsystem dependency |
| Disarm / Break Hold | **3** | §3.2 below already contemplates Margin/Tag-gated triggering as an alternative to location; location-mechanism unresolved |
| Equipment damage | **3** | Same basis |
| Function impairment (blindness, movement) | **3** | §10 Conditions have no stated activation mechanism |
| Armor bypass | **3, most firmly** | §5 below states the current design direction is Tag/Trait-based, not location-based — direct contradiction, not silence |
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

- ~~whether the location tier is universally fixed or selected by situation, scene or campaign~~ — **addressed by the candidate invocation policy above** (consequence/warrant-driven, not scene- or tier-fixed).
- ~~when Tier 1 is invoked~~ — **addressed by the candidate invocation policy above.**
- the anatomical mapping table — still open, untouched by this investigation.
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
