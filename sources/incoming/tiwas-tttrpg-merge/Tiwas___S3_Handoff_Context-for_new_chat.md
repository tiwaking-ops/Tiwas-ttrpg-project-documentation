# Tiwas — Session Handoff: Starting S-3 Outcome Effects Investigation

**Purpose of this document:** Paste this into a new chat (along with the four project documents: Canonical Rules v1.3, Proposals/WIP v1.4.3, Implementation Roadmap v1.4.3, and the S-2 Non-Attack Closure Record v1.2) to continue exactly where this session left off. This document is a **handoff/context record**, not a rules document — it creates no mechanics and should not be treated as canonical or non-canonical design content itself.

---

## 1. Immediate Next Task

> **Draft a Round 1 candidate analysis for S-3 (Outcome Effects), covering the Effect menu and trigger/purchasing architecture — using the same methodology as the S-2 Non-Attack Location Source investigation.**

The requested output is a **Round 1 candidate analysis document**, structured the same way as the S-2 investigation's Round 1 (see §4 below for the methodology to replicate).

---

## 2. Governing Instruction Set (Restate at Top of New Chat)

The new chat should operate under the same system instruction as this one — Tiwas Lead Systems Architect / Design Assistant, ultra-crunch simulation-grade d100 TTRPG, with:

- Hierarchical headings, tables for stats/formulas/mechanics.
- Every variable/constraint defined before use.
- Absolute mathematical/logical consistency across subsystems; flag any conflict with existing formulas.
- No narrative flavor unless explicitly requested; mechanics over fluff; no simplification.
- No new attributes/skills/resolution methods invented; no rounding-up; no partial leveling; no ignoring overflow-to-HP; no reference to other RPG systems; no "optional simplified" variants offered unprompted.

If the new chat's system prompt does not already contain this instruction set, paste it in full alongside this handoff document.

---

## 3. Authority Hierarchy (Unchanged, Restate as Ground Truth)

1. **Canonical Rules & Changelog v1.3** — current locked mechanics. Nothing here may be contradicted.
2. **Proposals, WIP & Design Direction v1.4.3** — non-canonical design repository. S-3 work happens here until formally promoted.
3. **Implementation Roadmap & Project Governance v1.4.3** — implementation sequencing, non-canonical, cannot independently decide numerical thresholds or mechanics.

**Promotion rule (Proposals §21):** nothing drafted in the upcoming S-3 investigation becomes canonical merely by being detailed. Requires the full eight-step process (design question identified → alternatives considered → analysis complete → designer accepts → documented as formal rule → Canonical Rules updated → proposal marked Superseded/Locked → implementation docs updated).

---

## 4. Methodology to Replicate (From the S-2 Investigation)

The S-2 investigation established a working pattern across several rounds. Apply the same discipline to S-3:

| Step | What it means for S-3 |
|---|---|
| **Round 1 — Candidate analysis** | Lay out candidate answers for the Effect menu and trigger/purchasing question; classify each candidate by evidence type (mechanical fact / architectural constraint / design inference / recommendation); explicitly reject any candidate that would violate a locked Core invariant, the same way Candidate B (ad-hoc GM roll) was excluded in S-2 for violating Invariant 18. |
| **Explicit scope guards** | State up front what this round does *not* touch — e.g., does not reopen S-1, does not alter the S-2 candidate invocation policy, does not decide S-4 wound severity, does not decide numerical Quality/Margin thresholds. |
| **Separate independent questions** | S-2's key discipline was refusing to conflate "roll provenance" with "warrant." S-3 likely has an analogous split — e.g., "does a successful contest grant an Effect at all" (trigger) is a different question from "which Effect, and how many" (purchasing/menu), and both are different again from "does this specific Effect require location as a delivery mechanism" (the State-3 cross-reference below). Keep these as separate columns/sections, not one merged judgment call. |
| **Flag designer decision points, don't resolve them** | Where a choice is a value trade-off (e.g., simplicity vs. granularity, the same Priority-1-vs-Priority-3 tension seen in S-2 Decision Point 1), present it as an options table with consequences, not a recommendation disguised as a default. |
| **Evidence-class labeling** | Use the Roadmap §23.2 categories throughout: Mechanical fact / Empirical finding / Designer ruling / Recommendation / Architectural constraint. Every claim in the Round 1 document should be tagged. |

---

## 5. What S-3 Needs to Resolve (Scope for Round 1)

Per Proposals §3 and Roadmap §10:

1. **Final Effect menu** — candidate list already exists (not locked):
 Inflict Injury; Impose Condition; Disarm/Break Hold; Force Movement/Seize Position; Seize Tempo; Guard Break; Bleed/Ongoing Drain; Open Retreat/Compel Yield; Damage Equipment; Choose Location.
2. **Trigger rules** — when does a successful contest grant an Effect at all? (Currently undefined.)
3. **Purchasing rules** — current proposal only, not locked: one free/basic Effect per successful contest; additional Effects may require Net Advantage/Quality bands; some Effects may be Tag-gated; some exceptional Effects may require qualifying successes.
4. **Numerical thresholds** — none exist yet. Explicitly out of scope for a candidate-analysis round per Roadmap §10 ("Do not lock numerical thresholds without required evidence and a designer ruling").
5. **S-3/S-4 interface** — Roadmap §10 permits prototyping the Effect→Wound Engine handoff architecturally, but this must not silently decide S-4 wound severity, activation, disability, or death — those remain fully open (Proposals §4).

---

## 6. Critical Cross-Reference: S-2's State-3 Findings Feed Directly Into S-3

This is the load-bearing connection between the two investigations and should anchor the new Round 1 analysis.

The S-2 candidate invocation policy (Proposals §2.1A) currently classifies these concepts as **State 3 — "Outcome Plausible, Location-Dependence Unresolved"**:

| Concept | S-2 State | Why it's S-3's problem now |
|---|---|---|
| Disarm / Break Hold | 3 | Also a candidate S-3 Effect. §3.2 already floats Margin/Tag-gated triggering as a location-independent alternative — this is exactly the fork S-3 must resolve. |
| Equipment damage | 3 | Also a candidate S-3 Effect ("Damage Equipment"). Same fork. |
| Function impairment (blindness, movement) | 3 | Maps to Conditions (§10), not a listed Effect directly, but Impose Condition is on the menu. |
| Armor bypass | 3 | Not on the S-3 Effect menu directly — lives at the S-3/S-5 boundary. Relevant if Bypass becomes an Effect-triggered mechanism. |
| Incapacitation / kill | 3, circularly | Downstream of S-3/S-4/S-7, cannot resolve independently. |

**The mechanism, not just the mention:** Per Proposals §2.1A, these State-3 entries "should be revisited only when the relevant future subsystem makes an explicit choice that **location is the delivery mechanism**." That means Round 1 of S-3 should explicitly ask, for each Effect on the candidate menu that overlaps this table: **does triggering this Effect require a Location Index, or does it trigger off Margin/Quality/Tags instead?** This is a genuine open fork, not a default — S-2 deliberately left it unresolved and handed it to S-3 (and S-5/S-7/S-10 for the remainder).

**Do not,** in the new chat, let this cross-reference quietly resolve itself in one direction (e.g., "Effects should generally use location" or "Effects should generally use Margin") without flagging it as a designer decision point, per Roadmap §24 Rule 6 (never silently resolve an open designer fork).

---

## 7. Locked Invariants That Constrain Any S-3 Candidate (Non-Negotiable)

Any Effect trigger/purchasing candidate must satisfy, without exception:

- Effects must never modify the historical die roll (Proposals §3.3 — explicit non-negotiable constraint).
- No competing primary resource or progression economy may be introduced (Canonical Invariant 17; Roadmap §2).
- Universal Play modules must call the Core Test Transaction, not replace or duplicate it (Canonical Invariant 18; Roadmap §2, §26).
- Cost = natural roll, Overflow → HP, Failure XP, Recovery timing — all untouched by anything S-3 does (Canonical §6–9).
- Quality (Margin/Blackjack/Hybrid) never alters the historical roll, Cost, Failure XP, Double eligibility, or Recovery (Canonical §13.2) — any Quality-gated Effect-purchasing candidate must respect this.

---

## 8. Explicit Scope Guards for the Upcoming Round 1

State these at the top of the new Round 1 document, mirroring S-2's practice:

- Does **not** reopen S-1, S-2's Tier-1 provider, S-2's attack-side invocation policy, or the S-2 non-attack deferral.
- Does **not** decide S-4 wound severity, activation thresholds, or death triggers — may prototype the interface only, per Roadmap §10.
- Does **not** lock numerical thresholds (Quality bands, Tag requirements, XP costs) — candidate structure only.
- Does **not** resolve S-5 (Armor) or S-6 (Defense) mechanics, even where Effects like "Damage Equipment" or "Guard Break" touch those subsystems.
- **Does** explicitly surface, without resolving, the location-vs-Margin/Tag fork for the overlapping S-2 State-3 concepts (§6 above) — this is the one place S-3 Round 1 must engage with S-2's findings rather than defer them further.

---

## 9. Suggested Opening Structure for the New Chat's Round 1 Document

1. Locked inputs (restate, not reopened) — Canonical invariants + S-1/S-2 status.
2. The two-part question, restated (trigger vs. menu/purchasing — kept separate).
3. Candidate trigger models (e.g., "any success grants a free Effect" vs. "Effects require Quality threshold" vs. hybrid) — evaluated against Canonical Invariant compliance.
4. Candidate purchasing/gating models for the existing Effect menu.
5. The State-3 cross-reference table (§6 above), explicitly flagged as unresolved forks requiring designer input, not defaults.
6. Scope-guard compliance check (mirror S-2's format).
7. Recommendation section — candidates only, explicitly labeled Recommendation, not Designer Ruling.
8. Designer input required — the actual open decision points, framed as trade-offs the same way S-2's Decision Points 1 and 2 were.

---

## 10. Prompt to Paste at the Start of the New Chat

> *"Continuing Tiwas design work. Attached: Canonical Rules v1.3, Proposals/WIP v1.4.3, Implementation Roadmap v1.4.3, S-2 Non-Attack Closure Record v1.2, and this handoff document. Please draft a Round 1 candidate analysis for S-3 (Outcome Effects) — Effect menu and trigger/purchasing architecture — following the methodology in §4 of the handoff document and the scope guards in §8."*

---

*End of handoff document. No mechanics, rulings, or canonical content are established by this file.*
