---
document:
  title: "Advisory Session Report — Reserved Systems (5.5) Decisions: Conditions, Tags, Equipment, Time/Action"
  version: "1.0"
  status: "Advisory working document (not canonical)"
provenance:
  author_llm: {name: "Grok", version: "4.5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Grok", version: "4.5"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
---

# Advisory Session Report — Reserved Systems (5.5)

**Session date:** 2026-09-02
**Scope:** DEC-015 Reserved Systems list (Conditions, Tags, Time/Action, Equipment, Hazards, Magic, Setting Interface/Integration)
**Authority:** Non-canonical designer direction only. No item in this report has completed the 8-step Promotion Rule. Nothing herein is Canonical / Locked.

---

## 1. Purpose

This report captures the complete set of designer decisions made during the 2026-09-02 advisory session on the Reserved Systems listed under §5.5 of the Task-Scoped Snapshot. It is intended for OpenCode to:

1. Record the decisions against the live decision register.
2. Present each decision back to the human designer (Tiwa) for explicit confirmation before any further action.
3. Preserve full provenance and evidence-class discipline.

OpenCode **must** solicit explicit designer confirmation on every decision listed in §4 before treating any item as a standing non-canonical ruling.

---

## 2. Governance Compliance

- All material is **non-canonical**.
- Evidence class for every entry: **Designer ruling** (candidate / non-canonical).
- No promotion, demotion, or reclassification is requested or performed by this document.
- Overflow immutability (DEC-007.A), Invariant 6, Invariant 17, and Invariant 18 remain binding constraints on every subsystem addressed.

---

## 3. Decision Summary Table

| ID (provisional) | Subject | Decision | Status |
|------------------|---------|----------|--------|
| ADV-5.5-01 | Conditions record format | `Tier-Y Condition Value Z` (global) or `Location X Tier-Y Condition Value Z` (localized) | Awaiting confirmation |
| ADV-5.5-02 | Condition magnitude scaling | Identical to Wound: Value Z = −Y | Awaiting confirmation |
| ADV-5.5-03 | Tags ontology model | Open extensible ontology, namespace-based | Awaiting confirmation |
| ADV-5.5-04 | Alpha Tags closed list | 34-tag closed vocabulary (Equipment 22 + Environment 6 + Creature 6) | Awaiting confirmation |
| ADV-5.5-05 | Equipment state model | Fully expressed through Conditions + Tags; held items automatically receive Location of the holding limb | Awaiting confirmation |
| ADV-5.5-06 | Time/Action economy model | Skill-side / Movement-penalty model only; no discrete action budget | Awaiting confirmation |
| ADV-5.5-07 | Conditions vocabulary (alpha) | Full 14-Condition table with mechanical effects, stacking, duration/removal (see §5) | Awaiting confirmation |
| ADV-5.5-08 | Stunned vs Incapacitated | Distinct Conditions | Awaiting confirmation |
| ADV-5.5-09 | Poisoned vs Sickened | Distinct Conditions | Awaiting confirmation |
| ADV-5.5-10 | Body-affecting Skill scope | All Skills that use a Body Attribute | Awaiting confirmation |
| ADV-5.5-11 | Movement Speed penalty magnitude | −Y is sufficient | Awaiting confirmation |
| ADV-5.5-12 | Sundered representation | Condition + Tag (`state:sundered`) | Awaiting confirmation |

---

## 4. Confirmation Questions for Designer (Mandatory)

OpenCode **must** present the following questions to Tiwa and record explicit answers before any register update:

1. Do you confirm the Conditions record format as `Tier-Y Condition Value Z` (global) or `Location X Tier-Y Condition Value Z` (localized)?
2. Do you confirm that Condition Value Z uses the identical scaling to Wound magnitude (Value Z = −Y)?
3. Do you confirm the Tags model as an open extensible ontology using namespaces?
4. Do you confirm the 34-tag closed alpha vocabulary listed in §6 of this report?
5. Do you confirm that Equipment state is fully expressed through Conditions + Tags, and that a held item automatically receives the Location of the holding limb?
6. Do you confirm the Time/Action economy model as Skill-side / Movement-penalty only (no discrete action budget or action points)?
7. Do you confirm the complete alpha Conditions vocabulary table in §5 (14 Conditions with the stated mechanical effects, stacking, and removal rules)?
8. Do you confirm that Stunned and Incapacitated remain distinct Conditions?
9. Do you confirm that Poisoned and Sickened remain distinct Conditions?
10. Do you confirm that body-affecting Conditions apply to **all Skills that use a Body Attribute**?
11. Do you confirm that a Movement Speed penalty of −Y is sufficient for the relevant Conditions?
12. Do you confirm that the Sundered Condition is represented as Condition + Tag (`state:sundered`)?

---

## 5. Conditions Vocabulary (Alpha) — Full Definition

**Format (confirmed direction):**
`Tier-Y Condition Value Z` or `Location X Tier-Y Condition Value Z`
**Magnitude:** Value Z = −Y
**Tier production:** Generating Effect Quality (hard ceiling) + Skill-Tier ≥ 2 production gate
**Constraints:** Overflow immutable; no advantage/disadvantage language; Skill-side or Movement-penalty expression only.

| Condition | Scope | Mechanical Effect | Stacking | Duration / Removal | Notes |
|-----------|-------|-------------------|----------|--------------------|-------|
| Encumbered | Global | −Y to Movement Speed; −Y to all Skills that use a Body Attribute when load thresholds exceeded | Same Tier: Values add; higher Tier replaces | Ends when load falls below threshold or by recovery action | DEC-078 |
| Grappled | Location (limb) or Global | Cannot move away from grappler; −Y to attacks not directed at grappler; Location-scoped limb unusable for other actions | Highest Tier only | Ends by Break Hold Effect, grappler incapacity, or forced separation | Distinct from Restrained |
| Restrained | Global or Location | Cannot move; −Y to all attack rolls and to all Skills that use a Body Attribute; may not declare movement intents | Same Tier: Values add; higher Tier replaces | Ends by Break Free Effect, ally intervention, or GM Fiat | Strictly stronger than Grappled |
| Prone | Global | −Y to attack rolls; Movement limited to crawl (or spend movement to stand); standing ends the Condition | Highest Tier only | Ends by spending movement to stand or by Effect | Combines with movement-denial Conditions |
| Blinded | Global | Auto-fail pure sight-based tests; −Y to Perception and to attack rolls | Same Tier: Values add; higher Tier replaces | Ends by removal Effect, time, or restoration of sight | Sensory |
| Deafened | Global | Auto-fail pure hearing-based tests; −Y to Perception involving sound | Same Tier: Values add; higher Tier replaces | Ends by removal Effect, time, or restoration of hearing | Sensory |
| Frightened | Global | −Y to all Skills while the source remains perceivable | Same Tier: Values add; higher Tier replaces | Ends when source no longer perceivable, by removal Effect, or time | Source-dependent |
| Slowed | Global | −Y to Movement Speed; −Y to Skills that use a Body Attribute (Speed-coded) | Same Tier: Values add; higher Tier replaces | Ends by time, removal Effect, or rest | Does not stack with Encumbered — apply worse penalty |
| Stunned | Global | Cannot declare actions or movement; auto-fail tests requiring active Body/Speed resistance | Highest Tier only | Ends by time, removal Effect, or ally action | Action denial |
| Incapacitated | Global | Cannot declare actions or movement; auto-fail all tests requiring active resistance; character is helpless | Highest Tier only | Ends by time, removal Effect, or ally action | Distinct from and stronger than Stunned |
| Fatigued | Global | −Y to all Skills that use a Body Attribute | Same Tier: Values add; higher Tier replaces | Ends by rest or recovery action | DEC-075: no fatigue from repeated Defense rolls |
| Sundered | Item or Location | Applies `state:sundered` Tag to the item; item functions at reduced effectiveness | Cumulative at same Tier | Permanent until repaired by appropriate Skill test or Effect | Condition + Tag model |
| Poisoned | Global | −Y to all Skills that use a Body Attribute (no HP loss over time) | Same Tier: Values add; higher Tier replaces | Ends by healing Effect, antidote, or time | No DoT |
| Sickened | Global | −Y to all Skills that use a Body Attribute (no HP loss over time) | Same Tier: Values add; higher Tier replaces | Ends by healing Effect or time | Distinct from Poisoned; No DoT |

---

## 6. Alpha Closed Tag List (34 Tags)

**Equipment (22)**
`slot:main_hand` · `slot:off_hand` · `slot:two_hand` · `slot:body` · `slot:head` · `slot:shield`
`damage:bludgeoning` · `damage:slashing` · `damage:piercing`
`offense:melee` · `offense:ranged` · `offense:thrown`
`handling:light` · `handling:heavy` · `handling:reach` · `handling:finesse`
`defense:armor` · `defense:shield`
`state:held` · `state:worn` · `state:sheathed` · `state:stowed`

**Environment (6)**
`env:hazard_physical` · `env:hazard_systemic` · `env:terrain_difficult` · `env:terrain_hazardous` · `env:darkness` · `env:weather_obscuring`

**Creature (6)**
`creature:type_humanoid` · `creature:type_beast` · `creature:type_undead` · `creature:size_small` · `creature:size_medium` · `creature:size_large`

---

## 7. Remaining Open Work (Priority Order)

1. Hazards formalization (`env:hazard_physical` vs `env:hazard_systemic` under DEC-037).
2. Position-tier Effect magnitudes (exact Skill-side / Movement penalties).
3. Magic / Special Abilities (still Design Direction only).
4. Setting Interface (§19) and Setting Integration (§20) — deferred.

---

## 8. Provenance & Handoff Notes

- All decisions originated in the 2026-09-02 advisory session with Grok 4.5.
- No simulation or empirical testing was performed in this session; all entries are pure designer direction.
- OpenCode is instructed to treat this document as an advisory handoff only and to obtain explicit confirmation on every item in §4 before any register write.

**End of report.**