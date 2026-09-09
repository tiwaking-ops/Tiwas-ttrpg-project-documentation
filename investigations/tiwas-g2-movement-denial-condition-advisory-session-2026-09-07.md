---
document:
  title: "G2 — Movement-Denial Condition / Movement Speed Formula Interaction: Advisory Session Report"
  version: "1.0"
  status: "Advisory working document — Non-Canonical. Not a ruling. Pending Tiwa's review and disposition via OpenCode."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-07"
  last_modified_date: "2026-09-07"
role_note: >
  This document is produced by Claude in its advisory capacity only. It presents
  options, corrections, and open items for Tiwa's ruling. It makes no rulings,
  assigns no DEC numbers, and is not self-executing. Per standing project
  governance, OpenCode must ask Tiwa each open question below before recording
  anything to the Decision Register — OpenCode may not infer answers, assign
  DEC numbers, or record any content on this report's authority alone.
---

# G2 — Movement-Denial Condition / Movement Speed Formula Interaction

**Advisory Session Report — for OpenCode intake and Tiwa's ruling**

## 0. Purpose and Scope

This report consolidates a single advisory session addressing **Gap G2** from the Time/Action subsystem (Proposals/WIP §12, governed at the top level by **DEC-082**): the unresolved relationship between the five movement-denying Conditions in the DEC-079 alpha vocabulary (Stunned, Incapacitated, Restrained, Grappled, Prone) and the locked Movement Speed formula (**DEC-004**: `floor((bsp + bss) / 15)`).

This report does **not** rule on anything. It records:

1. The original gap identification (G2, plus five related gaps G1/G3/G4/G5 identified in the same session but not developed further here).
2. A first options analysis (Options A/B/C).
3. A designer-directed pivot toward a schema-internal ("never total") solution, including the mechanism proposed to achieve it.
4. A self-correction of the advisory's own initial recommendation, made in direct response to Tiwa's stated design philosophy.
5. A corrected treatment of Grappled and Prone, which the advisory had originally — incorrectly — described as unable to fit the Type/Tier/Magnitude schema.
6. A consolidated list of open items requiring Tiwa's explicit ruling.

## 1. Background — Where G2 Sits in the Time/Action Subsystem

A prior pass in this session inventoried the Time/Action subsystem (Proposals §12) against the live Decision Register and found the following already Ruled and not reopened by this report:

| Area | Governing DEC(s) | Status |
|---|---|---|
| Time/Action model type (no action-point pool) | DEC-082 | Ruled |
| Turn order / initiative | DEC-095 | Ruled |
| Creature/NPC multi-action override | DEC-106 | Ruled (Design Override of DEC-095 §3) |
| Active Defense (reactions) | DEC-044–050 | Ruled |
| Extended Tests | DEC-067–070, DEC-073 | Ruled |
| Rest | DEC-071–074 | Ruled |

Five gaps were identified as still open under the Time/Action umbrella. Only **G2** was developed in this session:

| ID | Gap | Developed this session? |
|---|---|---|
| **G2** | Movement-denial Condition ↔ Movement Speed formula interaction | **Yes — full content below** |
| G1 | Movement-penalty magnitude table | No — flagged only |
| G3 | Duration/time-unit scale (interacts with DEC-117's `duration` enum) | No — flagged only |
| G4 | Reactions beyond Active Defense | No — flagged only; noted as a true blank with no prior partial ruling |
| G5 | Movement resolution granularity (distance/turn, contested movement) | No — flagged only |

G1–G5 remain open and are not resolved or advanced by anything in this report.

## 2. Original Gap Statement (G2)

DEC-079 defines two families of movement interaction:

| Family | Conditions | DEC-079 Text | Mechanism (Ruled) |
|---|---|---|---|
| Numeric overlay | Encumbered, Slowed | "−Y to Movement Speed" | −Y overlay on the *effective* stat; formula itself untouched (DEC-004/DEC-078 A3 discipline) |
| Categorical lock (as originally worded) | Stunned, Incapacitated, Restrained, Grappled, Prone | "cannot move," "no movement intents," "movement limited to crawl" | **Undefined** at session start — no ruling specified whether this touches the Movement Speed *value*, or is a pure action-declaration prohibition independent of the stat |

The unresolved question as originally framed: when a categorical-lock Condition is active, does anything reading Movement Speed see a modified number, or does it see the unmodified DEC-004 output and rely entirely on the Condition flag?

## 3. First-Pass Options Analysis (A/B/C)

Three options were drafted before the designer's steering question was posed:

| Option | Mechanism | Key issue |
|---|---|---|
| **A — Pure action-lock** | Movement Speed's DEC-004 output never modified; Condition text alone is the prohibition, checked at action-declaration | Cleanest read of "formula untouched," but pushes the burden of checking Condition state onto every future consumer of Movement Speed, with no standing numeric answer |
| **B — Full overlay negation** | Extend DEC-079's `−Y` overlay to the lock family, defining a new non-Tier-derived `Y` sized to always zero the stat | Unifies the read interface, but invents a magnitude source outside the established `Y = Tier` pattern (DEC-079 C2), and does not fit Grappled (directional) or Prone (partial) without further carve-outs |
| **C — Hybrid (descriptive-only zero)** | Action-lock remains primary and authoritative; a separate read-only reporting convention returns 0 for any external numeric query, without this being a recorded Condition-driven stat change | Preserves DEC-004 discipline exactly; gives future subsystems a standing default answer without a new overlay mechanism |

At this stage, **Option C was advisory-recommended** as the best fit against existing precedent (DEC-004/A3 discipline; compatibility with the DEC-115/116/117 read-only StateRecord filter architecture).

Per-Condition applicability was noted even at this stage:

| Condition | Movement-action availability | Notes |
|---|---|---|
| Stunned / Incapacitated / Restrained | None | Total lock — fits any of A/B/C uniformly |
| Grappled | Directional only (cannot move *away from* grappler) | Not uniform with the other three — flagged as needing separate treatment regardless of A/B/C choice |
| Prone | Partial (crawl, or spend an action to stand) | Not uniform — flagged as surfacing an undefined "crawl speed" value regardless of A/B/C choice |

## 4. Designer Question and Pivot — "Never Total," Staying Inside Type/Tier/Magnitude

Tiwa asked whether it is possible to remain entirely within the existing Effect/Condition **Type / Tier Y / Magnitude Z / [Location X]** schema (DEC-115) and treat every Condition as **never categorically total** — i.e., avoid a true action-lock mechanism altogether.

### 4.1 Mechanism Identified

DEC-079 C2 fixes `Magnitude Z = −Tier Y`. In every existing Ruled entry, `Y` is sourced externally to the target stat (causing-Skill-Tier per DEC-107; load-band per DEC-078). Nothing in DEC-115/DEC-079 requires this — only that `Z = −Y` holds.

**Proposed new Y-source pattern:** `Y = the target stat's own current value`, giving:

```
Effective Stat = Stat + Z = Stat − Y = Stat − Stat = 0
```

This guarantees a full zero regardless of how high the underlying stat has grown via uncapped General XP advancement (§11) — a fixed numeric Y would eventually fail to zero out a sufficiently advanced stat; a self-referential Y cannot.

This was identified as a **genuine third Y-source pattern**, distinct from the two already in use, and flagged as such rather than presented as a reuse of existing precedent:

| Y-source pattern | Precedent | Used for |
|---|---|---|
| Causing-Skill-Tier | DEC-107 | Wounds, Frightened, most Conditions |
| Load-band (non-Tier) | DEC-078 | Encumbered |
| Target-stat-value (proposed, new) | — | Movement-lock Conditions, if adopted |

### 4.2 Applied to Movement Speed

```
Y = current Movement Speed (floor((bsp+bss)/15) at time of query)
Z = −Y
Effective Movement Speed = Movement Speed + Z = 0
```

- DEC-004's formula is never touched — satisfies DEC-078 A3 discipline exactly.
- No new field or record shape required — fits the existing `Type / Tier Y / Magnitude Z / [Location X]` shape as-is.
- Collapses the A/B/C fork for Stunned/Incapacitated/Restrained: these become ordinary overlay-typed Conditions, mechanically uniform with Encumbered/Slowed.

### 4.3 Extension to Action-Declaration (Broader Reading, Flagged Separately)

The same self-referential-Y trick was noted to extend mathematically to Skill values generally (`Y = current Skill` → `Effective Skill = 0` → guaranteed failure, since `Roll ∈ [1,100]` is always ≥ 1). This was explicitly distinguished from the movement-only application, because it is **not a reformatting of the current rule** — it changes what Stunned/Incapacitated/Restrained *do*:

| | Current DEC-079 wording (Ruled) | Magnitude-only ("never total") extension |
|---|---|---|
| Can the test be declared? | No — action prohibited outright | Yes — test proceeds |
| Resource Cost paid? | None | Yes — Cost = natural roll, from Energy/MP |
| Overflow risk? | None | Yes — DEC-007 applies |
| Failure XP generated? | None | Yes — `max(0, Roll − 0) = Roll` |
| Advanced Skill creation possible? | No | Yes — on a qualifying failed Double |

This was flagged as requiring a **Design Override** of DEC-079's Stunned/Incapacitated/Restrained entries (same class of amendment as DEC-107's supersession of DEC-035.B) rather than a silent reinterpretation.

## 5. Designer Correction — Philosophy of Choice, and Self-Correction of the Initial Recommendation

Tiwa stated the following design position directly:

> "If a player wants to attempt a roll they cannot possibly succeed at then that is a choice. It is not a good choice, but it is still a choice."

### 5.1 Re-derivation Against Canonical §1

Canonical §1 (Locked) states: *"every meaningful attempt uses the common resolution engine; every test costs resources; failure generates mechanical growth."* This is the first Locked section of the ruleset. A categorical "you may not even roll" prohibition is the one construction this Core Identity structurally cannot itself produce: it removes the test, the Cost, the Failure XP, and any chance of a qualifying failed Double — even when the chance of success is effectively zero.

### 5.2 Correction of the Prior Recommendation's Downstream-Conflict Claims

The original recommendation (favoring the movement-only, action-lock-preserving Option C) cited DEC-052 and DEC-054/055 as reasons for caution before extending "never total" to action-declaration. On re-examination:

| DEC | What it actually governs | Does a magnitude-only Incapacitated/Stunned/Restrained touch it? |
|---|---|---|
| DEC-052 | HP=0 → automatic Incapacitated, "no roll, no save/check" | **No.** This governs whether incapacitation *is triggered* (automatic, untestable) — a different question from what a character can attempt once incapacitated. |
| DEC-053 | Incapacitation is HP-driven only, independent of Wounds | **No.** Governs the *cause* of Incapacitated, not its internal mechanics. |
| DEC-054/055 | Stabilization = skill-test revival, GM discretion on procedure | No direct conflict; "helpless" as used there would need its meaning re-confirmed once the Condition itself stops being a hard action-lock, but this is a confirmation, not a contradiction. |

**Correction recorded:** the scope of amendment required to extend "never total" to action-declaration is narrower than the original advisory draft implied. It is confined to **DEC-079's own wording** for Stunned/Incapacitated/Restrained (the "cannot declare actions or movement," "auto-fail... helpless" clauses) — not a cascade through the S-7 subsystem. The requirement that this be an explicit **Design Override** (its own DEC, not a silent reinterpretation) stands, but the earlier characterization of this as multi-DEC-entangled and therefore something to defer was an overstatement, corrected here.

## 6. Corrected Treatment of Grappled and Prone

The original advisory draft stated that Grappled and Prone were "not resolved by any magnitude-only treatment" and implied they required a different mechanism from Type/Tier/Magnitude. Tiwa challenged this directly, noting that Grappled is an Effect caused by a Contest action and Prone is a State with Tier/Magnitude. On re-derivation, **both fit the existing schema without amendment** — the original claim was incorrect and is corrected below.

### 6.1 Grappled

| Component | Schema fit |
|---|---|
| "−Y to attacks not directed at grappler" | Already an ordinary DEC-079 Condition Magnitude — no gap. |
| "cannot move away from grappler" | Expressible via the same self-referential-Y mechanism (§4.1–4.2) — **but only when the precondition matches:** the declared movement's direction is "away from grappler." |

The movement-lock component is not a magnitude problem; it requires a **directional gate** on top of the magnitude. This is not a new invention — **DEC-059** (Armor Bypass) already establishes exactly this pattern: a stateless relational match ("Tag-pairing match AND location match") gating whether an effect applies at all. Grappled's movement restriction is the same shape: *the Magnitude applies only when the declared movement's direction matches "away from grappler."* The schema was never actually the blocker here.

### 6.2 Prone

| Component | Schema fit |
|---|---|
| Movement while Prone = "crawl" (reduced, not zero) | Expressible as an ordinary Magnitude using a **partial** Y-source (e.g., `Y = ceil(Movement Speed / 2)`, illustrative only — no value is ruled) rather than the full self-referential Y used for total locks. `Z = −Y` still holds; no schema change required. |
| "or spend [an action] to stand" | A **removal condition**, not a magnitude — DEC-079 already uses this exact pattern elsewhere (e.g., "ends by spending movement or by Effect"). No new mechanism required. |

What is actually missing for Prone is a single undetermined **number** — what fraction of Movement Speed "crawl" represents — not a missing mechanism. No candidate value exists anywhere in the current corpus.

### 6.3 Corrected Summary

| Condition | Fits Type/Tier/Magnitude? | What is actually still open |
|---|---|---|
| Stunned / Incapacitated / Restrained | Yes | Whether to extend the same "never total" logic to action-declaration (§5), requiring a Design Override of DEC-079's current wording |
| Grappled | Yes | A directional gate (DEC-059 pattern) needs to be stated explicitly alongside the existing Magnitude |
| Prone | Yes | A ruled crawl-speed fraction (a number, not a mechanism) |

None of the five Conditions requires leaving the Effect/Condition schema. The original advisory's claim to the contrary is superseded by this report.

## 7. Consolidated Open Items Requiring Tiwa's Ruling

The following are presented as discrete decision points. Per standing project discipline, none may be inferred or recorded by OpenCode without Tiwa's explicit answer to each.

| # | Item | Options on the table | Notes |
|---|---|---|---|
| **1** | Movement Speed interaction for Stunned / Incapacitated / Restrained / Grappled (directional) / Prone (partial) | Adopt the self-referential-Y mechanism (§4.1–4.2) as the uniform treatment | No DEC-004 amendment required; fits existing schema; introduces one new named Y-source pattern (target-stat-value) that should be recorded as such if adopted |
| **2** | Action-declaration for Stunned / Incapacitated / Restrained — total lock (current DEC-079 wording) vs. "never total" (magnitude-only, always-fails) | Retain current DEC-079 wording, **or** adopt magnitude-only via Design Override | Directly engages Canonical §1 Core Identity per Tiwa's stated philosophy (§5.1); requires its own DEC as a Design Override of DEC-079, not a silent reinterpretation; scope of amendment is confined to DEC-079's own wording (§5.2 correction) |
| **3** | Grappled's directional gate | Adopt DEC-059-pattern relational gate ("Magnitude applies only when declared movement direction = away from grappler") | Not a new mechanism — direct reuse of the Bypass precedent; needs to be written into the Grappled entry explicitly |
| **4** | Prone's crawl-speed fraction | No candidate value currently exists; needs a specific numeric ruling (e.g., a fraction of current Movement Speed) | Purely a content gap, not a mechanism gap |
| **5** | Naming/recording the new "target-stat-value" Y-source pattern | If Item 1 is adopted, should this be formally logged alongside the two existing Y-source patterns (Skill-Tier-derived, load-band-derived) so future Conditions don't assume its availability without justification? | Housekeeping item, low stakes, recommended for completeness |

Items G1, G3, G4, G5 (§1) remain separately open and are not addressed by this report.

## 8. Non-Findings / Explicit Non-Claims

For clarity and to prevent this report from being read as broader than it is:

- This report does **not** rule that Conditions must be magnitude-only; it presents the mechanism and its consequences for Tiwa's decision.
- This report does **not** claim DEC-052 (HP=0 forced incapacitation) is affected by Item 2 — it explicitly is not (§5.2).
- This report does **not** propose a value for Prone's crawl fraction — none is offered or implied.
- This report does **not** resolve G1, G3, G4, or G5.
- Nothing in this report is Canonical or Ruled. All content is advisory pending Tiwa's decision and the standard non-canonical designer-ruling recording process.

## 9. Provenance and Session Trail

This report consolidates a single continuous advisory chat session between Tiwa and Claude Sonnet 5 (model string `claude-sonnet-5`), conducted 2026-09-07. No other advisory LLM was consulted in this session. The session proceeded: (1) Time/Action subsystem gap inventory → (2) G2 first-pass options analysis (A/B/C) → (3) designer question on schema-internal "never total" treatment → (4) mechanism derivation (self-referential Y) → (5) designer philosophical correction (§5) → (6) advisory self-correction of its own prior recommendation and of its Grappled/Prone claims (§6) → (7) handoff to OpenCode (this report), issued at Tiwa's request due to advisory session token constraints.
