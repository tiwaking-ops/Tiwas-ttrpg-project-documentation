---
document:
  title: "Tiwas — DEC-088.A Designer Ruling: Ordered Temperature Tags + Condition-Clause Implication + Scene-State Tracking"
  version: "1.0"
  status: "Designer-ruled record — accepted by Tiwa on 2026-09-17. Non-canonical designer ruling (amendment/closure to DEC-088). Recording does not confer canonical status — any future Canonical entry still requires the 8-step Promotion Rule (REQ-021 / governance/status-model.md)."
  decision_id: "DEC-088.A"
  amends: "DEC-088"
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
---

# Tiwas — DEC-088.A Designer Ruling

**Status: designer-ruled.** This document records Tiwa's ruling of **2026-09-17**
closing the two items DEC-088 carried open — **graded temperature** and the
**scene-state tracking mechanism**. Register effect (recorded separately in
`_consolidation/decision-register.md`): new **DEC-088.A** amendment/closure row plus
an in-cell closure annotation on **DEC-088**, preserving original cell text.

---

## 0. Governance Notice

Per the standing role separation — **Tiwa rules; OpenCode records**. The ruling was
given in-session with OpenCode (big-pickle); OpenCode asked three clarifications,
which Tiwa answered in full before this record was written. Denominator authority: the
ruling applies to candidate/non-canonical design material (DEC-088 is a Non-canonical
designer ruling) and does not by itself alter Canonical Rules.

Advisory basis that was **reviewed but NOT adopted**:

- `DEC-088 Formal Proposal — Graded Temperature and Scene-State Tracking.md`
  (GPT-5.6 Luna, 2026-09-08) — assessed by read-only analysis
  `audits/DEC-088-GRADED-TEMPERATURE-PROPOSAL-ASSESSMENT-2026-09-08.md`
  (opencode/big-pickle, 2026-09-08; verdict TECHNICALLY SOUND for that proposal's
  own single-ordered-Grade model). Tiwa did **not** adopt the single Grade 0–3
  model; the ordered-Tag model below supersedes it.

---

## 1. Ruling Summary

1. **Graded temperature = three ordered Tags in the temperature family.**
   `env:cold < env:freezing < env:extreme_cold`. `env:freezing` is retained
   unchanged; two Tags are added to the DEC-080 `env:` namespace (T1 extension;
   Environment namespace now 9 entries).
2. **Condition-Clause grammar is unchanged in surface form.** The proposed `+`
   comparator is **rejected** — under the implication rule it duplicates the truth
   table. Tiwa: "TIWAS preference is minimal grammar."
3. **One implication rule, stated once, permanent:** within the temperature family,
   presence of any higher Tag satisfies Condition Clauses written against any lower
   Tag. **Cross-family implication is forbidden.**
4. **Scene-state tracking = the set of active `env:` Tags declared on the current
   zone/scene.** Tags are zone-scoped, not character-scoped.
5. **No automatic damage or penalty from the Tags themselves.** Damage routes through
   existing systemic-hazard Effects. Terrain Tags stay descriptive (DEC-091).
6. **Continuous simulation, personal temperature residue, and automatic
   environmental damage ticks remain deferred to the Hazards subsystem.**

---

## 2. Ruled Items

### 2.1 Graded temperature — ordered Tags, not a numeric Grade

| Grade | Tag | Meaning |
|---:|---|---|
| 1 | `env:cold` | Mild / uncomfortable cold |
| 2 | `env:freezing` | Freezing point and below (existing Tag retained, no numeric grade) |
| 3 | `env:extreme_cold` | Severe / arctic / supernatural cold |

**Top-grade name ruling:** `env:extreme_cold`, **not `env:arctic`**. Tiwa:

> "env:arctic conflates a geographic biome with a temperature intensity. The system
> already treats environment Tags as mechanical state, not descriptive geography.
> env:extreme_cold is parallel in form to the lower two Tags, is free of real-world
> place-name collision, and matches the earlier advisory/audit preference. Existing
> env:freezing is left untouched; only the new top grade is renamed."

The Tags are **activation** Tags within the DEC-080 Environment namespace
(Environment total: 6 alpha + `env:freezing` + `env:cold` + `env:extreme_cold` = 9),
preserving the DEC-091 descriptive/activation distinction (temperature Tags activate;
`env:terrain_*` remain descriptive).

### 2.2 Condition-Clause grammar — implication, no `+` comparator

Tiwa:

> "Under the ordered chain env:cold < env:freezing < env:arctic, any clause written
> against a lower Tag already evaluates true when a higher Tag is present. Adding an
> explicit + produces identical truth tables and creates authoring surface that does
> nothing."

The Clause surface stays `Active only while [env:X] is present`, still referencing
exactly one `env:` Tag (DEC-088 single-Tag grammar preserved). Authors needing strict
presence of exactly one intensity would write a compound Condition Clause if the
future grammar ever supports Boolean combination — currently out of scope; no existing
worked example requires exact-match.

### 2.3 Implication rule (stated once, permanent)

- Scoped **exclusively** to the temperature family:
  `env:cold < env:freezing < env:extreme_cold`.
- Presence of any higher Tag in this chain satisfies Condition Clauses written
  against any lower Tag in the same chain.
- **No cross-family implication.** `env:darkness`, `env:hazard_systemic`,
  `env:terrain_difficult`, etc. never satisfy a temperature Condition Clause, and
  vice versa.
- This is a **one-time, permanent statement of the ordering**. Future
  temperature-related Tags, if any, must be inserted into this total order or
  explicitly declared outside it.

### 2.4 Scene-state tracking mechanism

| Component | Ruling |
|---|---|
| Scene container | Every scene/zone carries a set of active `env:` Tags (and any future environmental StateRecords). Scene-state for temperature (and all other `env:` Tags) is the set of active Tags declared on the current zone/scene. Tags are **zone-scoped, not character-scoped**. |
| Declaration timing | Tags are declared (or changed) at scene start and on any event the GM rules alters the environment. |
| Propagation | When a character moves between zones, the destination zone's Tag set becomes the active set for that character. No residual "personal temperature" unless a Condition is applied. |
| Change events | Weather, magic, fire, time-of-day, or scripted hazard progress may add/remove Tags. A change is itself an Effect or GM fiat; **no automatic tick**. |
| Persistence | Tags are scene-scoped, not character-scoped. A character does not carry `env:freezing` after leaving the zone. |

Declarative; no continuous simulation loop required. Maintaining per-zone Tag sets
may be delegated to a digital tracker but is not a mechanical requirement.

### 2.5 Interaction with existing systems

- **Regeneration / Regrowth (DEC-110):** magnitude remains content-authored per
  creature. The Condition Clause answers only the *whether* question. Graded
  temperature may optionally gate different magnitudes via separate authored Traits
  (e.g. "Regeneration 2 while [env:freezing]"; "Regeneration 1 while [env:cold]").
- **Systemic cold damage:** continues via the `env:hazard_systemic` → direct
  HP/Condition route (DEC-114 R1). Temperature Tags may be consulted by an Effect's
  own Condition Clause or by the GM when choosing Effect magnitude.
- **Terrain Tags (`env:terrain_*`):** remain descriptive only (DEC-091); not
  conflated with activation Tags.
- **StateRecord unification (DEC-117):** if temperature later becomes a StateRecord,
  the Condition Clause can read either Tag presence or StateRecord magnitude without
  changing the grammar surface.
- **DEC-116:** no per-Tag numeric grading is introduced; the implication surface is
  clause grammar, not a Tier/Magnitude field — DEC-116's "separate ruling" note is
  not triggered.

### 2.6 Deferred (Hazards subsystem)

- Continuous scene tracking / simulation.
- Personal temperature residue.
- Automatic environmental damage ticks.
- Future promotion of temperature intensity to a StateRecord (would carry
  `duration: scene` / `duration: permanent` + explicit `removal_tags` per DEC-117).

---

## 3. Compatibility and Authoring Consequence

Existing Ice Troll clauses written `Active only while [env:freezing] is present`
continue to function correctly in both freezing and extreme-cold scenes.
**No migration of prior content is required.**

The ordering + single-statement implication resolves the audit §4.3 state-consistency
objection to *un-ordered* independent temperature Tags; the assessed single-Grade
proposal (audit §5.1/§5.2 points) is superseded in favour of this model.

---

## 4. Register Effect

- `_consolidation/decision-register.md`: new **DEC-088.A** row in §B (Non-canonical
  designer rulings; amendment/closure to DEC-088) and in-cell closure annotation on
  **DEC-088**'s carried-open sentence and status column.
- This record: `investigations/tiwas-dec088a-graded-temperature-scene-state-designer-ruling-2026-09-17.md`.

No Canonical Rules change occurs. Any future promotion requires the 8-step Promotion
Rule (REQ-021).

---

*Recorded by opencode/big-pickle, 2026-09-17, at Tiwa's instruction following the
in-session ruling.*