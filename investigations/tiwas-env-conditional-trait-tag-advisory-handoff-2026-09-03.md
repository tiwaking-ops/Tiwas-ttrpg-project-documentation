---
document:
  title: "Advisory Session Report — Environment-Conditional Trait/Tag Binding (Option A)"
  version: "1.0"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-03"
  last_modified_date: "2026-09-03"
---

# Advisory Session Report — Environment-Conditional Trait/Tag Binding

## 0. Purpose and Origin

This report documents an advisory drafting pass on a gap identified during BToV-Madness
GURPS→Tiwas creature conversion review (DEC-077.A workflow). It is **not** a ruling. It
presents one option (selected by Tiwa from three candidates) drafted to formal rule-text
level, ready for Tiwa's review and, if approved, OpenCode's live-register cross-check and
DEC-number assignment.

**Constraints observed (per task-scoped snapshot §"Constraints binding your advice"):**
this document inspects, compares, and recommends. It does not resolve any Open decision,
promote anything to Canonical, or reclassify any document. No DEC number is assigned
below — DEC numbers are assigned only by OpenCode against the live register.

## 1. Triggering Gap

Source verification of `BeyondtheValeofMadnessGURPS.pdf` (direct text extraction,
2026-09-03) confirmed the Ice Troll GURPS stat block includes three Traits explicitly
gated on scene temperature:

> Traits: Appearance (Hideous); Bad Temper; Claws (Sharp); **Regeneration (Fast, 1
> HP/minute, only in freezing temperatures); Regrowth (only in freezing temperatures);
> DR 2 (only in freezing temperatures).**

No existing Tiwas rule allows a creature Trait or Tag to reference **scene/environmental
state** as an activation condition. Existing conditional-Tag precedent (DEC-059, S5-B
Bypass) only covers Tag-vs-Tag relationships between an Effect and a piece of gear — not
Tag-vs-scene-state. This is confirmed as a genuine gap, not a restatement of DEC-059.

**Evidence class:** Mechanical fact (gap identified by direct comparison against locked/
ruled material — DEC-058, DEC-059, DEC-080) + source-text finding (empirical, from the
adventure PDF itself, not simulation).

## 2. Options Considered (advisory pass, 2026-09-03)

Three candidate architectures were presented to Tiwa:

| Option | Summary | Outcome |
|---|---|---|
| A | New `env:` scene-state Tag + formal conditional-Trait binding rule generalizing DEC-059's Bypass pattern | **Selected by Tiwa (pending OpenCode confirmation — confirmed 2026-09-03)** |
| B | Duplicate creature template variants (freezing / non-freezing forks) | Not selected |
| C | GM Fiat / prose-only flag, no mechanical Tag representation | Not selected |

Full comparative analysis (pros/cons, Invariant checks) was presented in-session; not
reproduced verbatim here per this project's evidence-pointer convention. Available on
request if OpenCode needs the full comparison table re-stated.

## 3. Drafted Rule Text — Option A

### 3.A. New Tag — extension to DEC-080 Environment namespace

| Tag | Meaning |
|---|---|
| `env:freezing` | The current scene/zone is at freezing temperature or colder. Boolean presence/absence, GM-declared per scene. No numeric grade. |

**OpenCode verification (2026-09-03):** DEC-080 lists **6** Environment tags
(`env:hazard_physical`, `env:hazard_systemic`, `env:terrain_difficult`,
`env:terrain_hazardous`, `env:darkness`, `env:weather_obscuring`). Adding `env:freezing`
therefore makes it the **7th** entry in the Environment namespace — NOT the 8th as
framed in §3 of the original draft. The author's own text (listing 6, then saying 8th)
was internally inconsistent; it was flagged by the author for verification and is
corrected here to **7th**. No other `env:` tags exist anywhere in the corpus; this
extension is architecturally permitted by DEC-080 T1 (open extensible, namespace-based,
no base-model change required).

### 3.B. Conditional-Trait Binding Grammar (new mechanic — proposed amendment/extension to DEC-059's relational pattern)

> A creature Trait, or an Effect granted by a Tag, may declare a **Condition Clause**:
> `Active only while [env:X] is present.`
>
> - The Condition Clause references exactly one scene-state Tag from the `env:` namespace.
> - While the referenced Tag is **absent** from the current scene, the bound Trait/Effect
>   is treated as **not present** on the creature for all mechanical purposes — no DR, no
>   Regeneration tick, no Regrowth, etc.
> - Scene-state Tag presence/absence is **GM-declared**, evaluated at the time each
>   relevant mechanic would apply (e.g., each Regeneration tick, each DR check against an
>   incoming Effect).
> - This is **read-only, stateless** — identical in kind to DEC-059's Bypass check: it
>   consults Tag presence: it does not create, consume, or modify any resource pool.

**Invariant compliance check (self-assessed, for Tiwa/OpenCode verification):**

| Invariant | Assessment |
|---|---|
| 17 (no new resource/progression economy) | Satisfied — boolean gate on an existing Trait's effect; no pool created |
| 6 (Cost = natural roll) / 7 (Overflow→HP) | Satisfied — clause does not touch Cost, Overflow, or the natural roll |
| DEC-007.A (Overflow-immutability) | Satisfied by the same logic as the existing Armor-Tag corollary: a conditional Trait, like an Armor Tag, never modifies Overflow |

**OpenCode verification (2026-09-03):** the Invariant-compliance self-assessment is
confirmed as sound — the Condition Clause is a read-only, stateless boolean presence
check, structurally identical in kind to DEC-059's Bypass (which DEC-058/DEC-059/DEC-062
explicitly treat as never touching Overflow and never creating a pool). No Invariant is
violated.

### 3.C. Worked Example — Ice Troll (content-authoring illustration, not itself a rule)

| Ice Troll Trait (GURPS source) | Tiwas Candidate Representation |
|---|---|
| DR 2 (only in freezing temperatures) | Armor Tag (per DEC-058 Tags/Traits-only architecture) with Condition Clause: `Active only while [env:freezing] is present` |
| Regeneration (Fast, 1 HP/min, only in freezing) | Trait with Condition Clause: `Active only while [env:freezing] is present`. Magnitude/timing value (1 HP/min) is a content-authoring value under DEC-077.A, not part of the binding rule itself |
| Regrowth (only in freezing) | Same Condition Clause pattern |

All three Traits use the same single Tag (`env:freezing`) — no graded system needed for
this creature.

**OpenCode note (2026-09-03):** the worked example is content-authoring illustration for
the Ice Troll working stat block under DEC-077.A/DEC-085; it is not itself a rule and
remains provisional pending application to the stat block.

## 4. Explicitly Deferred (not resolved by this draft)

- **Graded temperature.** This draft scopes `env:freezing` to **binary presence/absence
  only**. A future creature requiring graded temperature (e.g., "cold" vs. "freezing" vs.
  "arctic") would require a separate ruling — not addressed here, to avoid building ahead
  of demonstrated need (consistent with DEC-041's "directional, not locked" caution).
- **Scene-state tracking mechanism.** How/when a GM formally declares `env:freezing`
  present or absent for a scene (a full Hazards/environment subsystem, §5.5, remains
  unbuilt) is out of scope for this draft. This rule only defines what happens *given*
  the Tag's presence/absence — it does not define the broader environmental-state system.
- **Numbering/placement conflicts.** The "8th entry" framing above must be checked by
  OpenCode against the live register — this document works from the 2026-09-02
  task-scoped snapshot, not live repository state. [**RESOLVED by OpenCode 2026-09-03:
  it is the 7th entry.**]

## 5. Reconfirmation Checklist for OpenCode

- [x] Confirm current live count/contents of DEC-080 Environment namespace (verified: 6; `env:freezing` = 7th)
- [x] Cross-check proposed `env:freezing` Tag and Condition Clause grammar against the register (no conflict found in conflict-register)
- [x] Confirm with Tiwa whether Option A is the final selection (confirmed 2026-09-03)
- [x] Assign DEC number(s) (recorded as DEC-088 — Tag extension + binding grammar as one ruling)
- [x] Record Invariant-compliance self-assessment for verification (confirmed sound)
- [ ] Apply the worked Ice Troll example (§3.C) to the actual BToV-Madness Ice Troll working stat block once the binding rule is formally recorded

## 6. Source Pointers

- `BeyondtheValeofMadnessGURPS.pdf` — source adventure; Ice Troll stat block (temperature-
  gated Traits verified via direct text extraction, 2026-09-03)
- `Tiwas-Task-Scoped-Snapshot-2026-09-02.md` — DEC-058, DEC-059, DEC-080 as consumed for
  this advisory pass (task-scoped snapshot, not live register — see checklist item 1)
- This document itself — advisory working record, to be superseded by whatever OpenCode
  records in the live register

---

**One-off notice:** this is a single advisory working document for one session's drafting
pass. It does not create, lock, or promote any rule. Authority remains with Tiwa via the
established Promotion Rule and register process.

---

## OpenCode Documentarian Record (added 2026-09-03)

Stored from `C:\Users\Tiwa Pene\Downloads\tiwas-env-conditional-trait-tag-advisory-handoff-2026-09-03.md` at Tiwa's instruction after Tiwa confirmed Option A and the 7th-entry count correction. `author_llm` remains Claude Sonnet 5; OpenCode appended as additional `assessor_llm` and set as `last_modified_by_llm` for the storage pass. Supersedes the advisory status: the Option A selection was **confirmed by Tiwa (2026-09-03)** and recorded as **DEC-088** in the live decision register (conditional-Trait Binding grammar + `env:freezing` Tag extension to DEC-080). The binding grammar and tag are now Ruled (non-canonical); all §4-deferred items (graded temperature, scene-state tracking mechanism) remain open.
