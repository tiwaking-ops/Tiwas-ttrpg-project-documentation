---
document:
  title: "Tiwas — Reaction Trigger Taxonomy & Tag Vocabulary: Content-Authoring Options Brief"
  version: "0.1 (advisory — not executed, not a ruling)"
  status: "Advisory / Non-canonical. No DEC assigned. Content-authoring output per DEC-132.A(R1)/DEC-077.A. Pending Tiwa final sign-off / OpenCode recording."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
---

# Tiwas — Reaction Trigger Taxonomy & Tag Vocabulary

**Purpose.** Close the content-authoring task left open by DEC-132.A(R1): concrete trigger
categories, a `reaction:` Tag namespace, and one Tag per category. This brief incorporates
four decisions Tiwa has already made (§0) and proposes the remaining content for review.
**No DEC is inferred by this document.** Storage confers no authority.

---

## 0. Decisions Already Made (Tiwa, 2026-09-13 — recorded here for traceability only)

| # | Decision | Reason (Tiwa, verbatim) |
|---|---|---|
| 1 | **Reject** the declared-action-trigger category ("react before resolution") | "Adds complexity to decision making." |
| 2 | **New** `reaction:` namespace (not an extension of `combat:`) | "Can use them in non-combat situations." |
| 3 | **One Tag per category** (coarse grain) | "This may expand in the future." |
| 4 | Rename `combat:vigilant` (DEC-132's own worked example) → `reaction:vigilant` | Approved. |

These four items are **not re-opened or re-argued** anywhere below. Everything in §1–§5
is built on top of them.

---

## 1. Flag Raised by Decision #2 — Scope Wording Tension

DEC-132(2)(c) states a Reaction "resolves as a **full S-1 combat exchange**." Read
literally, "combat exchange" ties Reactions to combat. Decision #2's own stated reason —
non-combat usability — is in tension with that wording.

**Resolution used in this brief (assumption, not a ruling):** S-1 (DEC-013) is itself the
**universal** opposed-contest primitive, not a combat-only mechanic — it underlies S-8
mutual-failure adjudication (DEC-043), S-9/S-10 Extended Tests (DEC-067), and ordinary
non-combat opposed tests throughout the corpus. DEC-132's "combat exchange" phrasing is
read here as **descriptive of the playtest context DEC-132 was ruled in**, not as a scope
restriction — a Reaction is an ordinary S-1 exchange, usable wherever S-1 is usable.

**Flag for Tiwa:** if this reading is wrong — if Reactions were meant to stay combat-only
— Decision #2's stated rationale (non-combat usability) has no mechanical effect, since
the trigger Tag would exist but never fire outside combat. Recommend an explicit
one-line confirmation: *"Reactions may trigger during any S-1 opposed contest, combat or
not."* This brief proceeds on that assumption throughout.

---

## 2. Trigger Category Taxonomy (three categories, per Decision #1)

Per DEC-132.A(R1), the taxonomy is the rules-level content; exact trigger menus per
creature/class/equipment remain DEC-077.A content-authoring beyond this taxonomy layer.

| Category | Detects | Combat framing (example) | Non-combat framing (example) |
|---|---|---|---|
| **movement-trigger** | A tracked entity's position/band changes relative to the reactor | Target moves out of Engagement band (DEC-133 zone vocabulary) relative to the reactor | An NPC starts to leave a negotiation, a suspect bolts from a search |
| **ally-targeted-trigger** | Another tracked entity becomes the object of a hostile Effect or declared consequence | An ally within Short band is hit by a declared Effect | An ally's claim is challenged in a social S-1 contest; a companion is accused |
| **HP/state-threshold-trigger** | A StateRecord (DEC-115/117 schema) crosses a defined threshold on a tracked entity | A tracked target's HP drops below 0; a target gains Incapacitated | A target's Frightened Tier crosses a threshold; a Wounded StateRecord is applied to a tracked ally |

**Design note on grain:** each category is a *detection class*, not a specific event.
The concrete event (which band, which Effect type, which threshold value) is
per-creature/per-ability content authored under DEC-077.A, same as DEC-023.A's Effect
enumeration or DEC-079's Condition vocabulary. This taxonomy layer is what DEC-132.A(R1)
actually ruled; the brief does not attempt to lock specific trigger wording beyond the
worked examples above, which are illustrative only.

---

## 3. Tag Vocabulary — `reaction:` Namespace (new, per Decision #2)

Per DEC-116, Tags default to vocabulary-only (no Tier/Magnitude) unless a ruling supplies
numeric fields. None of the three Tags below need numeric fields — the Reaction's actual
mechanical weight is the S-1 exchange itself (DEC-132(2)(c)), not the Tag.

| Tag | Grants reaction eligibility for | Notes |
|---|---|---|
| `reaction:vigilant` | movement-trigger | Renamed from DEC-132's own `combat:vigilant` example per Decision #4 |
| `reaction:guardian` | ally-targeted-trigger | E.g. a "protect the flank / protect the claim" archetype |
| `reaction:opportunist` | HP/state-threshold-trigger | E.g. reacts when a tracked target crosses a state threshold |

**One Tag per category (Decision #3).** A character/creature/item needing eligibility
for more than one category simply carries more than one Tag — no combined Tag is
authored at this pass. This is the deliberate future-expansion hook Tiwa flagged: adding
a fourth category later means adding a fourth Tag, not restructuring the existing three.

**Ontology placement (per DEC-080 T1):** `reaction:` is registered as a new top-level
namespace, parallel to `slot:`, `damage:`, `offense:`, `handling:`, `defense:`, `state:`,
`env:`, `creature:`, and the reserved `magic:`/`ability:` prefixes (DEC-114 R3). No base
schema change — DEC-080 T1 already permits open extension.

---

## 4. Worked Example (illustrative only, no DEC)

A guard with `reaction:vigilant` and `reaction:opportunist`:

1. An intruder attempts to move out of Engagement band during the guard's off-turn.
   `reaction:vigilant` is present → movement-trigger fires → guard may resolve a full S-1
   exchange against the intruder as a Reaction. Normal Cost/Overflow/Failure XP apply
   (DEC-132(2)(c)).
2. Later, an ally guard is reduced below 0 HP nearby. `reaction:opportunist` is present →
   HP/state-threshold-trigger fires → a second, independent Reaction may resolve (DEC-047
   uncapped Defense precedent extends here per DEC-132.A(R3) — no frequency cap).
3. Both Reactions coexist with any Active Defense the guard also makes that round —
   DEC-132.A(R2): Reaction and Active Defense are always independent, never exclusive.

---

## 5. Cross-Checks Against Standing Rulings

| Check | Result |
|---|---|
| DEC-025 (Skills forbidden from requiring Tags) | Satisfied — these Tags gate a *Reaction opportunity*, not a Skill; the underlying S-1 exchange still uses an ordinary Skill chosen normally |
| DEC-115/116/117 (unified StateRecord schema) | Satisfied — all three Tags are vocabulary-only records, `duration: permanent` default (DEC-117 R2), no `Tier`/`Magnitude` needed |
| DEC-132.A(R1) (category taxonomy, not flat trigger list) | Satisfied — three categories, not a per-event list |
| DEC-132.A(R2) (Reaction/AD always independent) | Unaffected — this brief adds no interaction logic |
| DEC-132.A(R3) (uncapped frequency) | Unaffected — no counter field added to any Tag |
| DEC-082 (no action-point pool) | Satisfied — Reactions remain full Core Tests with their own Cost/Overflow, not a budgeted resource |
| Invariant 17 (no new resource/progression economy) | Satisfied — vocabulary-only Tags create no pool |
| DEC-077.A (content-authoring path) | Satisfied — this brief is advisory content, not a rules change; Tiwa retains final authorship |

No conflicts found against the live register.

---

## 6. Open Items for Tiwa

1. **§1 scope confirmation** — does a Reaction fire on any S-1 exchange (combat or not),
   or is DEC-132's "combat exchange" wording a deliberate scope limit? This is the one
   item that materially affects whether Decision #2's stated rationale has mechanical
   effect.
2. **Concrete per-creature/per-class trigger wording** beyond the three worked examples
   in §2 — remains DEC-077.A content-authoring, not resolved here.
3. **Whether `reaction:vigilant`/`guardian`/`opportunist` are the final names**, or
   placeholders pending actual naming preference.

No ruling is made on any of these three items; they are recorded as the next decision
points, not defaults.

---

## 7. Status

Advisory content proposal only. No DEC assigned. Pending Tiwa's review/acceptance before
OpenCode records it as adopted content (parallel to the DEC-137 Human Location Template
adoption pattern — accept as-is, edit, or reject).
