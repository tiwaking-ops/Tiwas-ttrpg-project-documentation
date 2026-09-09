---
document:
  title: "Assessment — DEC-088 Formal Proposal: Graded Temperature and Scene-State Tracking"
  version: "1.0"
  status: "Assessment record — read-only analytical review of a non-canonical proposal"
  provenance:
    author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
    assessor_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
    last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
    created_date: "2026-09-08"
    last_modified_date: "2026-09-08"
  scope: >
    Technical consistency analysis of the DEC-088 graded-temperature and
    scene-state-tracking proposal against the repository's existing decision
    register, canonical rules, and governance model. Read-only analytical
    activity; does not modify any document's authority status.
  target_document:
    title: "Tiwas DEC-088 Formal Proposal — Graded Temperature and Scene-State Tracking"
    file: "DEC-088 Formal Proposal — Graded Temperature and Scene-State Tracking.md"
    author: "GPT-5.6 Luna"
    date: "2026-09-08"
    decision_id: "DEC-088"
---

# Assessment — DEC-088 Graded Temperature / Scene-State Proposal

## 1. Scope and Method

This assessment evaluates the technical consistency and architectural soundness of
the DEC-088 graded-temperature and scene-state-tracking proposal against:

- the decision register (`_consolidation/decision-register.md`), DEC-001 through
  DEC-133, with emphasis on DEC-088 (target), DEC-080, DEC-089–093 (hazards),
  DEC-110, DEC-114–117 (Tags / unified StateRecord), DEC-130 (GM Fiat bounds);
- the canonical rules (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`);
- the governance model and the 18 Core Architectural Invariants (DEC-016).

The assessment is **read-only analytical work**. It does not promote, canonicalise,
or alter any document's authority. The proposal remains **Non-Canonical Design
Proposal**.

---

## 2. Executive Assessment

**Overall verdict: TECHNICALLY SOUND. No conflicts found against the existing
decision register or canonical rules. The proposal extends DEC-088 in a way closely
consistent with the project's established no-new-engine discipline and the unified
StateRecord architecture.**

The proposal correctly identifies the two DEC-088 carried-open items, correctly
defers them as an architecture decision (not a full environment simulation), and
defends its choices with well-reasoned rejections of the plausible alternatives. All
architectural invariants cited are preserved. Two implementation-level points
warrant explicit human attention at adoption (the numeric-grade-schema question
under DEC-116, and the new "derived Tag predicate" pattern) — these are not flaws but
areas where the boundary between "architecture ruling" and "implementation question"
should be confirmed.

---

## 3. Factual Verification

### 3.1 Characterization of DEC-088

The proposal states DEC-088 currently provides:
- `env:freezing`, a Boolean presence/absence scene-state Tag, GM-declared per scene,
  **with no numeric grade**;
- Conditional-Trait Binding grammar (`Active only while [env:X] is present`);
- read-only/stateless evaluation.

**Verified against the register (DEC-088):** All accurate. DEC-088 (1) establishes
`env:freezing` as the 7th Environment-namespace Tag under DEC-080, "boolean
presence/absence, GM-declared per scene, **no numeric grade**"; (2) establishes the
Conditional-Trait Binding grammar extending DEC-059; (3) explicitly records it as
read-only/stateless. The register does not attribute a declared "carried open" label
to DEC-088 for graded temperature in its own cell text, but the "no numeric grade"
wording and the later hazard-grading decisions (DEC-093) establish the same design
gap the proposal targets. The proposal's framing is reasonable and not contradicted
by the register.

### 3.2 Characterization of DEC-089/090/092/093 (Hazard architecture)

The proposal cites:
- DEC-089: systemic hazard = ongoing progress, no new economy;
- DEC-090: S-3 boundary — S-3 does not own all environmental simulation;
- DEC-092: hazard difficulty = existing Skill-side difficulty grade;
- DEC-093: hazard Intensity = graded but **lookup key only**.

**Verified:** All four accurately represented against the register.

### 3.3 Characterization of DEC-114

The proposal cites DEC-114 as establishing that environment-conditional hazard Tags
are "consulted by adjudication and do not independently initiate rolls, damage,
resource expenditure or a new engine."

**Verified:** DEC-114 R1 confirms `env:hazard_physical` / `env:hazard_systemic` do
not initiate resolution; presence is GM-declared per scene like `env:freezing`.
Accurate.

### 3.4 Characterization of DEC-115/116/117 (Unified StateRecord)

- **DEC-115 R4** confirms the unified schema governs state records on
  characters/items/**environments/scenes**/Effects/Conditions — supports the
  proposal's scene-state claim.
- **DEC-116 R1** establishes Tags carry Tier/Magnitude as OPTIONAL fields absent by
  default, numeric fields only where a specific ruling supplies them; its "Open"
  note states any future per-Tag numeric grading beyond existing authority is a
  **separate ruling**.
- **DEC-117** establishes the full unified StateRecord shape (Type / Tier Y /
  Magnitude Z / Location X / id / source / duration / removal_tags / counters),
  with Tag defaults `duration = permanent`.

**Verified:** All accurate.

---

## 4. Technical Validity — Detailed Findings

### 4.1 Graded Temperature Model (Ordered Grade, Grades 0–3)

**Verdict: SOUND.**

The proposal models temperature as one ordered Grade (Normal / Cold / Freezing /
Extreme Cold) rather than multiple Boolean Tags or a continuous numeric Celsius
value. This is the correct abstraction for the stated problem.

The integer representation is explicitly framed as an implementation representation
of an ordered grade, not a general-purpose numeric temperature mechanic. This
preserves DEC-116's "absence ≠ zero" discipline (Normal = Grade 0 is a **named grade**,
not a bare Tag at zero) and does not repurpose the Schema's Tier field as a
temperature quantity. The proposal is careful to separate "ordered grade" from "the
record's Tier Y".

### 4.2 `env:freezing` as a Derived Boolean Compatibility Predicate

**Verdict: SOUND, with one implementation-level note (see §5.2).**

Defining `env:freezing = present iff Temperature Grade >= Freezing` preserves all
existing DEC-088 content: an Ice Troll Regeneration clause referencing `env:freezing`
continues to work with no change. This is the strongest compatibility property of
the proposal.

The derivation is a **monotonic threshold function** of the Grade — mechanically
simple and unambiguous. It is not a counter relationship (DEC-117 R3 counters are
suppressed-record filters; this is a presence derivation), and not an implicit
Tag-vs-Tag interaction of the kind DEC-116 R4 cautions against.

### 4.3 Rejection of Multiple Independent Temperature Tags

**Verdict: CORRECT.**

The proposal's state-consistency critique of `env:cold` / `env:freezing` / `env:arctic`
as independent Booleans is well-founded: independent Tags create invalid or ambiguous
combinations (Present/Absent mixes, cumulative-vs-hierarchical ambiguity, whether
Arctic implies Freezing). These would require additional precedence/exclusivity rules
merely to describe temperature. The project's established preference for declarative
Tags over mutually-dependent predicate sets (DEC-080, DEC-116) supports the rejection.

### 4.4 Rejection of Continuous Numeric Celsius

**Verdict: CORRECT.**

The proposal declines to make physical temperature (e.g. −37°C) a mechanic input. The
listed reasons (threshold questions, update cadence, exposure time, wind chill,
shelter, equipment, body temperature, whether temperature initiates tests) are
genuine environmental-simulation questions beyond the current DEC-088 problem scope.
This is consistent with DEC-093's Intensity-as-lookup-key architecture and the
project's repeated "no unnecessary simulation engine" discipline.

The one caveat: the proposal **defers exact Celsius thresholds as content-authoring**
(section 19, "Open"). This is appropriate and consistent with DEC-077.A
content-authoring, provided the human confirms thresholds are content, not a
deferred rule.

### 4.5 Rejection of Dedicated Temperature Tracker

**Verdict: CORRECT.**

Rejected on the ground it would duplicate the unified StateRecord / scene-state
architecture. Verified consistent with the register's repeated no-parallel-engine
discipline (DEC-082, DEC-089, DEC-090, DEC-092, DEC-093, DEC-117, Invariant 17).

### 4.6 Rejection of Automatic Environmental Resolution

**Verdict: CORRECT and critical.**

The proposal explicitly prohibits the interpretation "the scene is Extreme Cold,
therefore every character automatically makes a test." This is essential to preserve:
- DEC-088 read-only scene-state semantics;
- DEC-089/090/092/093 hazard architecture;
- DEC-114 adjacency (Tags consulted by adjudication, no self-initiated resolution);
- the Core Test's ownership of resolution;
- Invariant 17.

The proposal correctly distinguishes **environmental state** (what the environment
is) from **hazard content** (whether that state is an active hazard for an actor)
from **resolution** (the existing mechanics). This separation is the strongest
architectural contribution of the proposal.

### 4.7 `Arctic` Deprecation as a Formal Grade Name

**Verdict: SOUND.**

"Arctic" as a geographic/climatic descriptor is distinct from a mechanical
temperature grade. Recommending "Extreme Cold" as the formal Grade 3 name and
allowing "Arctic" as setting content is a clean disambiguation. No register conflict.

### 4.8 Temperature Grade as Hazard Intensity Lookup Key

**Verdict: CORRECT and explicitly compatible with DEC-093.**

The proposal allows Temperature Grade to serve as the content lookup key for a
systemic temperature hazard without performing resolution itself. This is precisely
DEC-093's Intensity-as-lookup-key model applied to a specific environmental state.
Fully consistent.

---

## 5. Identified Gaps, Edge Cases, and Points for Human Attention

These are not flaws but boundary questions the human designer should confirm when
adopting, because they sit at the "architecture ruling" vs "implementation question"
line the proposal itself draws.

### 5.1 The numeric-Grade schema question (DEC-116 "Open" note)

**Point:** DEC-116's "Open" note states: *"any future request for per-Tag numeric
grading beyond existing authority is a separate ruling."* The Temperature Grade is a
numeric-graded environmental state. The proposal is careful (section 15) to state
that any implementation-specific field for the ordered Grade must be separately
reviewed against DEC-115–117 before being locked.

**Assessment:** This is the correct handling — the proposal resolves the
**architectural question** (there is an ordered Grade) while correctly flagging the
**schema-field question** (how the Grade is represented in the unified StateRecord)
as a separate review. However, because DEC-088 itself is a Tag-based ruling and DEC-116
explicitly reserves per-Tag numeric grading as a separate ruling, the human should
confirm at adoption whether the DEC-088 extension itself constitutes that "separate
ruling," or whether a further schema decision is required. The proposal's own
deference is correct; the human should close this explicitly.

### 5.2 The "derived Tag predicate" pattern is new

**Point:** Defining `env:freezing` as *derived from* the Temperature Grade (rather
than an independently-declared Boolean) introduces a **derivation relationship** that
the register does not currently formalize for scene-state Tags. DEC-088 currently
declares `env:freezing` as GM-declared presence/absence; this proposal makes it the
derived output of the Grade.

**Assessment:** The derivation itself is mechanically harmless (a monotonic
threshold predicate) and preserves content compatibility. But it changes the source
of authority for `env:freezing` — from "GM declares presence/absence" to "GM sets the
Grade, presence follows." The human should confirm this is intended (it appears to
be, and is arguably cleaner). Minor provenance/authority-of-state note only.

### 5.3 Scene-wide vs zone-local temperature

**Point:** The proposal flags in section 19 that scene-wide vs zone-local
environmental boundaries are open (implementation/content). Using a single Grade per
scene assumes one temperature per scene.

**Assessment:** Acceptably deferred, but the human may wish to note that the Grade
concept scales to zone-local by being a Grade *per state object* in the unified
StateRecord — the proposal's own "state ownership belongs to scene/environment, not
characters" framing supports this. No action required, just a noted extension
path.

### 5.4 Relationship to DEC-110 (Regeneration magnitude)

**Point:** The Ice Troll worked example relies on Regeneration gated by `env:freezing`.
DEC-110 established the Regeneration/Regrowth healing **magnitude** is
content-authoring per creature, and `env:freezing` determines *whether* a tick
applies, not its magnitude.

**Assessment:** The proposal's compatibility claim (Ice Troll clause still functions)
is consistent with DEC-110 — the Grade affects presence, not magnitude. No conflict.
Not explicitly cited by the proposal but relevant; no action needed.

### 5.5 GM Fiat boundary

**Point:** The proposal relies on GM Fiat (GM sets/declares scene state and Grade)
without citing DEC-130's bounded-universality ruling.

**Assessment:** Consistent. DEC-130 (2026-09-07) establishes GM Fiat is universal in
scope but bounded against the Locked Canonical Core (Overflow immutability, Cost =
natural roll, HP=0 incapacitation, no-damage-over-time). Temperature state-setting is
a discretionary decision point within DEC-130's scope; the proposal does not attempt
to place environmental state within the excluded Canonical Core. No conflict. The
human may optionally ask the proposal to cite DEC-130 for completeness, but this is
cosmetic, not substantive.

---

## 6. Constraint Compliance

| Constraint | Status | Notes |
|---|---|---|
| Core Test remains universal resolution | SATISFIED | Resolution flows unchanged |
| Natural roll authoritative | SATISFIED | Unmodified |
| Cost = natural roll | SATISFIED | Unmodified |
| Overflow → HP | SATISFIED | Unmodified |
| Overflow immutability | SATISFIED | Unmodified |
| Failure XP / Recovery | SATISFIED | Unmodified |
| No new resource pool | SATISFIED | None introduced |
| No parallel XP economy | SATISFIED | None |
| Hazard difficulty uses existing difficulty | SATISFIED | DEC-092 preserved |
| Hazard Intensity lookup-only | SATISFIED | DEC-093 preserved |
| Tags do not initiate resolution | SATISFIED | Section 12 prohibition |
| `env:freezing` compatibility | SATISFIED | Derived predicate preserves content |
| Unified StateRecord architecture | SATISFIED (extended, not replaced) | Section 15 |
| DEC-025 Skill-side Tag prohibition | SATISFIED | Not reopened |
| No dedicated environment engine | SATISFIED | Tracker explicitly rejected |

**All 15 cited constraints satisfied.**

---

## 7. Consistency with Referenced Decisions

| DEC | Claimed status | Verification |
|---|---|---|
| DEC-088 | Extended, not replaced | **Confirmed.** Grading extends the Boolean Tag; Conditional-Trait Binding intact |
| DEC-080 | Preserved (env: namespace) | **Confirmed.** No new namespace |
| DEC-089 | Preserved | **Confirmed** |
| DEC-090 | Preserved | **Confirmed** |
| DEC-092 | Preserved | **Confirmed** |
| DEC-093 | Preserved and relied upon | **Confirmed.** Intensity-as-lookup-key model applied |
| DEC-094 | (implicitly consistent) | Scene-state → Condition-Clause → Frightened pattern reused; no conflict |
| DEC-110 | (relevant, not cited) | **Consistent.** Grade affects presence, not Regeneration magnitude |
| DEC-114 | Preserved | **Confirmed.** No change to hazard routing |
| DEC-115 | Preserved | **Confirmed.** Schema governs environments/scenes |
| DEC-116 | Preserved | **Confirmed.** Absence≠zero; optional numeric fields; separate-ruling note honored |
| DEC-117 | Preserved | **Confirmed.** No new schema |
| DEC-130 | (relevant, not cited) | **Consistent.** Scene-state setting is discretionary within bounded GM Fiat |

**No conflicts identified.**

---

## 8. Risk Assessment

### 8.1 Schema-field ambiguity (numeric Grade representation)

**Risk:** LOW. The proposal defers the schema question correctly (section 15) and DEC-116
explicitly reserves it as a separate ruling. The architectural decision (there is a
Grade) and the schema decision (how it is stored) are cleanly separated. The only
risk is if a reader infers a concrete unified-StateRecord field was already locked;
the proposal does not do this.

### 8.2 Derived-predicate authority shift

**Risk:** LOW. The shift from GM-declared `env:freezing` to GM-set-Grade-with-derived-
presence is a simplification, but it changes the statement of authority. A human
confirmation is recommended (see §5.2), not a blocker.

### 8.3 Scope creep into environment simulation

**Risk:** LOW. The proposal explicitly defers exposure duration, wind chill, shelter,
acclimatisation, and threshold values (section 19), and Section 12 prohibits automatic
resolution. The architecture does not silently reach into unbuilt environment
subsystems.

### 8.4 No architectural conflicts

**Risk:** NONE identified.

---

## 9. Recommendation

**The proposal is technically sound, architecturally consistent, and governance-
compliant. It should be presented to the human designer for adoption or rejection
through the project's formal governance process.**

The two linked proposals are:

1. **Graded Temperature** — one ordered Grade (Normal/Cold/Freezing/Extreme Cold) as
   scene state, with `env:freezing` retained as a derived Boolean compatibility
   predicate. Correctly avoids the alternatives (multi-Tag, Celsius numeric,
   dedicated tracker, auto-resolution).

2. **Scene-State Tracking via unified StateRecord** — environmental state stored in
   the existing state architecture, not a parallel tracker. Correctly separates
   environmental state / hazard content / resolution.

Both are consistent with the project's no-new-engine discipline and the unified
StateRecord architecture (DEC-115–117).

**Adoption posture:** The proposal is appropriate as the architecture basis. At
adoption the human designer should (a) close the numeric-Grade schema question
explicitly against DEC-116 (or defer it as a named separate ruling — either way,
decide it, don't leave it ambiguous), and (b) confirm the intended authority shift
for `env:freezing` (GM sets Grade; presence is derived).

---

## 10. Recorded Observations

This assessment is a **read-only analytical activity** performed by
opencode/big-pickle. It does not:
- modify any document's authority status;
- promote the proposal to canonical;
- amend DEC-088 or any other decision;
- create or modify any governance record.

The proposal remains **Non-Canonical Design Proposal** pending Tiwa's explicit
adoption or rejection through the project's governance process. If adopted, the
resulting decision remains non-canonical until the project's required promotion
procedure is completed.

---

*Recorded by opencode/big-pickle, 2026-09-08.*
