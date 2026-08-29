# Tiwas — S-3 Outcome Effects: Round 2 — Effect Identity

**Document Version:** v1.1 (Correction pass — supersedes v1.0 as the working Round 2 baseline)
**Document Status:** Non-canonical design investigation — Round 2 of N
**Rule Authority:** None. This document creates no game mechanics and modifies no other document.
**Governing hierarchy:** Canonical Rules & Changelog v1.3 (authoritative) → Proposals/WIP v1.4.3 (this work's home once accepted) → Implementation Roadmap v1.4.3 (sequencing only).
**Predecessor:** S-3 Round 1 Candidate Analysis v1.3 (`Tiwas___S3_Effects_Round1_Candidate_Analysis-v1_3_1.md`). This document follows the Recommended Sequencing fixed there (§8): Round 2 = Effect Identity only. It does **not** perform Round 2b (Effect Weight), and it does **not** revisit Decision Points 1–3 (Eligibility model, Eligibility scope, "Choose Location" interpretation choice) — those remain carried forward, unruled.
**Promotion status:** Nothing in this document is canonical, accepted, or ruled. Promotion requires the full eight-step process (Proposals §21).

**Correction pass (this revision, v1.0 → v1.1):** Four minor corrections applied after independent external review. **No Effect's identity conclusion, dependency finding, or open-question status changed in substance — only wording precision.** Each fix is marked inline with a `[Corrected v1.1]` tag at point of change.

1. §2 (Effect 1 — Inflict Injury) — Added an explicit boundary sentence distinguishing the newly-surfaced attack-side Injury/location fork from the already-ruled S-2 non-attack Location Index exclusion (Proposals §2.5A), so this document cannot be misread as reopening that closed question.
2. §3 (Effect 2 — Impose Condition) — "Persistent by definition" reworded. Conditions' own duration/removal procedures remain explicitly unresolved (Proposals §10); asserting persistence as a definitional fact overstated what is currently established.
3. §9 (Effect 8 — Open Retreat / Compel Yield) — "May not fit the Track A/Track B interface" reworded to avoid reading as a premature architectural rejection of a candidate the menu deliberately includes. The observation (its state transition doesn't obviously belong to either harm track) is preserved; the implication that this counts against the candidate is removed.
4. §10 (Effect 9 — Damage Equipment) — S-5 dependency narrowed from a blanket "direct" dependency to a conditional one: direct dependency on Equipment (Proposals §13) in all cases, with additional direct S-5 interaction specifically when the damaged equipment is armor or the damage mechanism crosses the armor model.

Reviewer observations not adopted as corrections (recorded for completeness, not applied): a proposed three-level identity/dependency/open-question vocabulary (methodological preference, not an error); the Effect 7/Effect 2 (Bleed vs. Bleeding-Condition) redundancy finding and the Disarm/Guard Break/Damage Equipment structural-precondition parallel were both endorsed as-is and are unchanged.

---

## 0. Scope Guards (Inherited and Restated)

This round does **not**:

- reopen S-1, S-2's Tier-1 provider, S-2's attack-side invocation policy, or the S-2 non-attack deferral;
- decide S-4 wound activation, severity, or thresholds;
- decide S-5 (Armor) or S-6 (Defense) mechanics, even where an Effect's identity touches those subsystems — it may only note the touchpoint;
- lock any numerical threshold, Quality band, or Tag list;
- rule on Decision Point 1 (T1/T2/T3), Decision Point 2 (SCOPE-A/B), or Decision Point 3 ("Choose Location" interpretation) from Round 1 §8;
- resolve the per-Effect Q3 delivery-mechanism fork (location vs. Margin/Tag) for Disarm, Damage Equipment, or Function-Impairment-flavored Conditions — Round 1 §5 surfaced these deliberately as **open**, and identity work does not require closing them; where an Effect's identity depends on the fork's outcome, this document records the dependency rather than assuming an answer;
- perform Round 2b (Effect Weight/Consequence) — relative mechanical or narrative impact between Effects is explicitly deferred, per Round 1 §8's sequencing correction.

This round **does**:

- answer the eleven-question identity checklist (Round 1 §8) for each of the ten candidate Effects (Proposals §3.1);
- flag, per Effect, whether its identity is fully self-contained or depends on an open fork/subsystem elsewhere in the document set;
- surface apparent overlap or redundancy between candidate Effects, per checklist question 11, without resolving whether any should be merged or cut (that judgment call is Round 2b/3 territory, not identity work).

---

## 1. Reading the Checklist Answers

Each Effect below is run through the eleven questions from Round 1 §8, verbatim:

1. What state does it change?
2. What does success actually do, mechanically?
3. Is it instantaneous or persistent?
4. Does it require a target state to apply?
5. Does it require Tags to function?
6. Does it require a Location Index to function?
7. Can it stack, and with what?
8. Does it interact with S-4 (Wounds)?
9. Does it interact with S-5 (Armor) or S-6 (Defense)?
10. Is it fundamentally tactical, physical, positional, or narrative in character?
11. What makes it materially different from the other nine candidate Effects?

Every answer below is **[Design inference]** unless otherwise tagged — this document adds no new evidence class beyond what Round 1 already established (Roadmap §23.2). Where an answer depends on an unresolved fork or subsystem, that is stated explicitly rather than assumed.

---

## 2. Effect 1 — Inflict Injury

| Q | Answer |
|---|---|
| 1. State changed | Localized physical harm state (Track B, per the Roadmap §10 two-track interface) — distinct from the ordinary Cost/Overflow/HP path (Track A), which already exists independent of any Effect. |
| 2. Mechanical action | Marks the target as having sustained a *meaningful* injury beyond ordinary Overflow-to-HP damage, for eventual S-4 Wound Engine consumption. |
| 3. Instantaneous or persistent | Persistent — the injury state is expected to outlive the triggering exchange, pending S-4's (open) severity/activation rules. |
| 4. Target-state requirement | None identified — any successful contest with a target capable of taking physical harm can plausibly select this Effect. |
| 5. Tags required | Not inherently — but a per-Effect Tag gate (Round 1 P2/P4) could restrict which weapons/techniques may select it. Not decided here. |
| 6. Location Index required | **Open, per Round 1 §5's boundary.** Injury *could* be location-flavored (a Location Index feeding S-4 severity) or location-independent (severity from Quality/Margin alone). This is not one of Round 1's named State-3 concepts, so it inherits no existing S-2 classification — it is a fresh fork this document surfaces for the first time. Not resolved here. **[Corrected v1.1]** This fork concerns only how an eligible *attack-side* Injury Effect may consume Location information once one exists; it does not reopen, narrow, or otherwise touch the already-ruled categorical exclusion of Tier-1 Location Index generation for non-attack physical resolutions (Proposals §2.5A). |
| 7. Stacking | Plausibly cumulative (multiple Injury Effects across exchanges building toward incapacitation) — but stacking behavior is S-4 severity-model territory, not Effect-identity territory. |
| 8. S-4 interaction | Direct and primary — this Effect appears to be the main producer of S-4 Wound Engine input. |
| 9. S-5/S-6 interaction | Indirect — Armor (S-5) would presumably be able to reduce or negate this Effect's application, but that interaction is S-5's to define. |
| 10. Character | Physical. |
| 11. Differentiation | The most Track-B-central of the ten candidates — closest to the "default" outcome the whole Effect menu is built to enrich beyond flat HP loss. Its breadth (applies to almost any successful physical contest) is itself a differentiator: most other Effects are narrower/situational. |

---

## 3. Effect 2 — Impose Condition

| Q | Answer |
|---|---|
| 1. State changed | Applies a named Condition (Proposals §10: e.g., Stunned, Prone, Impaired, Bleeding, Restrained) to the target. |
| 2. Mechanical action | Adds a Condition-state flag; the Condition's own rules (still Reserved, Proposals §10) govern its effect on subsequent tests/actions. |
| 3. Instantaneous or persistent | **[Corrected v1.1]** Creates or applies a Condition state; whether the resulting state persists, for how long, and how it is removed is unresolved — final Condition definitions, stacking, durations, and removal procedures all remain explicitly Reserved (Proposals §10). A Condition will ordinarily behave as persistent in the everyday sense of the word, but that is not yet a mechanical assertion this document is entitled to make. |
| 4. Target-state requirement | Depends entirely on which Condition is applied — e.g., Restrained may require the target not already be Restrained; this varies per sub-Condition and is not resolvable at the level of "Impose Condition" as a single menu item. |
| 5. Tags required | Not inherently at the top level; individual Conditions may be Tag-gated once Conditions are further defined. |
| 6. Location Index required | **Depends on which Condition.** Function-impairment-flavored Conditions (blindness, movement impairment) are explicitly named in Round 1 §5 as State-3/Open — their location-dependence is an unresolved fork. Other Conditions (Stunned, Prone) show no obvious location-dependence at all. "Impose Condition" is therefore not identity-uniform across its own sub-cases; this document flags that internal split rather than resolving it. |
| 7. Stacking | Condition stacking rules are explicitly Reserved (Proposals §10, "stacking... remain unresolved") — not decided here. |
| 8. S-4 interaction | Likely — some Conditions (Bleeding) look like they overlap with, or feed, the Wound/harm loop; others (Prone, Stunned) look purely positional/tactical. This split is noted, not resolved. |
| 9. S-5/S-6 interaction | Plausible for movement/defense-impairing Conditions (an Impaired or Prone target may face different S-6 Defense terms), but S-6 does not yet define how. |
| 10. Character | Mixed — spans physical (Bleeding), positional (Prone), and cognitive/narrative (Impaired) depending on sub-Condition. |
| 11. Differentiation | The only candidate Effect that is itself a *container* for further undefined sub-mechanics (the individual Conditions) rather than a single self-contained mechanical action. This makes its identity inherently less resolved than the other nine until Conditions (Proposals §10) receive their own definition pass — flagged as a dependency, not treated as a defect unique to this analysis. |

---

## 4. Effect 3 — Disarm / Break Hold

| Q | Answer |
|---|---|
| 1. State changed | Target's held item (weapon/equipment) or held grip (on another character, object, or position) is forcibly released. |
| 2. Mechanical action | Removes the item from the target's hand, or breaks a grapple/hold state, without itself dealing Injury. |
| 3. Instantaneous or persistent | Instantaneous action with a persistent consequence (item now on the ground / grip now broken) — the state change itself does not decay over time. |
| 4. Target-state requirement | **Yes — hard requirement.** Target must currently be holding something (weapon, object) or maintaining a hold. Round 1 §5's Procedural Rules (inherited from the S-2 investigation, Proposals §2.1A) already flag this exact case as the paradigm example of a **stale-objective check**: declaring Disarm against an already-empty hand voids the match. This Effect's identity is therefore bound to a state-validity check at the point of Selection, not just at declaration. |
| 5. Tags required | Plausible per Round 1 §4.2 (P2) — a weapon/technique Tag permitting grip-breaking is one candidate gating mechanism, not yet decided. |
| 6. Location Index required | **Open — named State-3 fork (Round 1 §5).** Location-dependent path: Location Index lands on a grip/weapon-bearing zone. Location-independent path: Margin/Quality-band or Tag-gated trigger. Neither is chosen; this Effect's mechanical trigger condition cannot be fully specified until S-3 (or S-5) resolves this fork. |
| 7. Stacking | Not meaningfully stackable — a target is either holding the item or not; a second Disarm against an already-disarmed target has no target state to act on (see Q4). |
| 8. S-4 interaction | None identified — Disarm removes an item/hold, not HP or a Wound. |
| 9. S-5/S-6 interaction | Plausible interaction with S-6 (Defense) — a disarmed target's subsequent defensive options may be constrained — but S-6 does not yet specify how. |
| 10. Character | Tactical/positional. |
| 11. Differentiation | The only candidate whose target-state precondition is already partially specified by name in prior documentation (the stale-objective rule), rather than left fully open. Distinct from Force Movement/Seize Position in that it removes an *object/grip* rather than repositioning a *character*. |

---

## 5. Effect 4 — Force Movement / Seize Position

| Q | Answer |
|---|---|
| 1. State changed | Target's (or actor's) physical position/facing/spatial relationship on the battlefield. |
| 2. Mechanical action | Relocates or repositions a character (push, pull, reposition self relative to target) as a direct consequence of a successful contest. |
| 3. Instantaneous or persistent | Instantaneous — the positional change itself does not decay, though its tactical consequences (e.g., now flanked, now at range) may persist until further action. |
| 4. Target-state requirement | Plausibly requires available space/terrain to move into — an environmental precondition rather than a target-character-state precondition, distinct from Disarm's requirement. Not specified further here. |
| 5. Tags required | Not obviously — this looks like one of the more Tag-independent candidates, though a technique/weapon Tag gate (e.g., only reach/leverage weapons can Force Movement) is not ruled out. |
| 6. Location Index required | No — not a State-3 concept in Round 1's table, and no plausible mechanism ties battlefield repositioning to a struck body location. Lowest apparent location-dependence of the ten candidates. |
| 7. Stacking | Plausibly cumulative across a scene (repeated repositioning), but this is a Time/Action-economy (Proposals §12) question, not an Effect-identity one. |
| 8. S-4 interaction | None identified. |
| 9. S-5/S-6 interaction | Direct and likely — Time/Action economy and Defense (S-6) both plausibly interact with forced repositioning (e.g., movement provoking a reaction, or removing a target from an ally's engagement range), but neither subsystem currently defines this. |
| 10. Character | Positional/tactical. |
| 11. Differentiation | The clearest candidate with essentially zero Location Index dependence and no direct S-4 touchpoint at all — sits almost entirely in the tactical/positional lane, distinct from the physical-harm-adjacent Effects (Injury, Disarm, Damage Equipment). |

---

## 6. Effect 5 — Seize Tempo

| Q | Answer |
|---|---|
| 1. State changed | Initiative/turn-order or action-economy advantage (exact mechanism dependent on the still-Reserved Time/Action Economy system, Proposals §12). |
| 2. Mechanical action | Grants the actor some form of extra or accelerated action, or denies/delays the target's next action — cannot be specified more precisely without a defined turn structure, which does not yet exist. |
| 3. Instantaneous or persistent | Ambiguous pending Time/Action Economy definition — could be a one-time extra action (instantaneous) or an ongoing tempo advantage (persistent). Not resolvable at Effect-identity level alone. |
| 4. Target-state requirement | Unknown — depends entirely on turn-structure rules not yet written. |
| 5. Tags required | Not obviously. |
| 6. Location Index required | No — no plausible location-dependence identified. |
| 7. Stacking | Unknown pending Time/Action Economy definition. |
| 8. S-4 interaction | None identified. |
| 9. S-5/S-6 interaction | Likely interacts with S-6 (Defense timing, reactions) once both are defined, but neither currently specifies how. |
| 10. Character | Tactical. |
| 11. Differentiation | **The candidate Effect with the least-resolvable identity in this round** — its mechanical content is almost entirely downstream of Proposals §12 (Time/Action Economy), which is itself fully Reserved with no draft direction at all (unlike Conditions or Tags, which at least have partial structure). This document flags Seize Tempo as **blocked on a prerequisite subsystem**, not merely under-specified by choice. |

---

## 7. Effect 6 — Guard Break

| Q | Answer |
|---|---|
| 1. State changed | Target's defensive capability/posture (S-6 Defense state). |
| 2. Mechanical action | Reduces or removes the target's Defense option for some scope (next test, next exchange, until repositioned) — exact scope undefined pending S-6. |
| 3. Instantaneous or persistent | Ambiguous pending S-6 — likely persistent for a bounded duration (e.g., "until the target's next action"), but that duration model does not exist yet. |
| 4. Target-state requirement | Plausibly requires the target to currently have an active defensive option to break — mirrors Disarm's stale-objective pattern (Q4 in §4 above) but against a Defense state rather than a held item. This document notes the structural parallel without asserting the two Effects should share a rule. |
| 5. Tags required | Not obviously. |
| 6. Location Index required | No — no plausible location-dependence identified; this is a Defense-state Effect, not a physical-harm one. |
| 7. Stacking | Unclear — a target with Guard already broken has no further state to act on for a second Guard Break (structurally resembles Disarm's non-stacking, §4 Q7), but this is provisional pending S-6. |
| 8. S-4 interaction | None identified directly, though a broken guard plausibly increases subsequent Injury/Overflow exposure indirectly (an S-6/S-4 interaction, not a direct one). |
| 9. S-5/S-6 interaction | **Direct and primary** — this Effect's entire identity is defined in terms of S-6 (Defense), which is itself fully Reserved (Proposals §6, no locked model). Guard Break's mechanical content cannot be finalized before S-6 is. |
| 10. Character | Tactical. |
| 11. Differentiation | Like Seize Tempo, this candidate is **blocked on a prerequisite subsystem** (S-6 rather than Proposals §12) rather than being independently specifiable. Distinct from Force Movement in that it targets a defensive *capability* rather than spatial *position*. |

---

## 8. Effect 7 — Bleed / Ongoing Drain

| Q | Answer |
|---|---|
| 1. State changed | Establishes a recurring, per-interval harm or resource-drain state on the target. |
| 2. Mechanical action | Applies ongoing HP loss, or ongoing PE/MP drain, at defined intervals (round, turn, or Extended Test interval) until removed or resolved. |
| 3. Instantaneous or persistent | Persistent by definition — this is the most explicitly duration-bound candidate on the menu (name implies an ongoing process, not a one-time state change). |
| 4. Target-state requirement | None identified beyond being a valid harm target. |
| 5. Tags required | Not obviously. |
| 6. Location Index required | Not obviously required for the *drain mechanism* itself, though a location-flavored narrative justification (bleeding *from* a wound) could exist without the mechanic requiring a Location Index number. This is a narrative/mechanical distinction worth carrying into Round 2b, not resolved here. |
| 7. Stacking | **Central open question for this Effect specifically.** Does a second Bleed application increase drain rate, extend duration, or fail to stack? Canonical Invariant 17 (no competing progression economy, Canonical §16) is potentially relevant if a stacking Bleed effect were to accumulate as a persistent numeric pool across many sources — flagged as a possible future invariant-check item for Round 3, not resolved here. |
| 8. S-4 interaction | **Direct** — this is explicitly a Wound-and-Condition-adjacent Effect (Proposals §10 lists Bleeding as an example Condition), meaning "Bleed / Ongoing Drain" (menu item 7) and "Impose Condition → Bleeding" (menu item 2's sub-case) may be the *same mechanic named twice* rather than two distinct Effects. This document flags this as a candidate redundancy for Round 2b/3 to resolve, per checklist question 11 below — it is not resolved here. |
| 9. S-5/S-6 interaction | None identified directly. |
| 10. Character | Physical (harm-track), with a temporal/persistent character distinct from the other harm Effects. |
| 11. Differentiation | **Likely overlaps with Effect 2 (Impose Condition → Bleeding)** — flagged explicitly as a redundancy candidate. If both remain on the final menu, their relationship (is Bleed/Drain a stand-alone Effect, or is it the mechanical backing for the Bleeding Condition specifically?) needs an explicit decision before Round 3; this document does not assume an answer. |

---

## 9. Effect 8 — Open Retreat / Compel Yield

| Q | Answer |
|---|---|
| 1. State changed | Target's willingness or ability to continue the contest — either grants the actor a withdrawal opportunity or compels the target toward yielding/ending the conflict. |
| 2. Mechanical action | Unclear at the mechanical level — "Compel Yield" implies a social/morale consequence (target chooses or is compelled to stop fighting), which is a different *kind* of state change than any other candidate (none of the other nine touch willpower/morale directly). |
| 3. Instantaneous or persistent | Ambiguous — a yield decision is plausibly a one-time state transition (combat ends for that participant) rather than a duration-bound Condition. |
| 4. Target-state requirement | Plausibly requires the contest to already be at some threshold of desperation/disadvantage for a "Compel Yield" framing to make narrative sense, but nothing in current documentation defines such a threshold. |
| 5. Tags required | Not obviously. |
| 6. Location Index required | No — no plausible location-dependence; this looks like the most narrative/morale-driven candidate on the menu, not a physical-target mechanism at all. |
| 7. Stacking | Not meaningfully stackable — yield/retreat is close to a binary outcome, not an accumulating value. |
| 8. S-4 interaction | None identified. |
| 9. S-5/S-6 interaction | None identified. |
| 10. Character | **Narrative**, distinctly more so than any other candidate — the only Effect whose primary consequence is social/psychological rather than physical, positional, or tactical. |
| 11. Differentiation | The clearest outlier on the menu: every other candidate acts on a physical, positional, or equipment state; this one acts on the fictional trajectory of the conflict itself. Its mechanical hook (what actually happens in system terms when "Compel Yield" triggers — an NPC morale check? A GM-adjudicated narrative beat with no numeric component at all?) is the least defined of the ten. **[Corrected v1.1]** Its state transition — changing the target's participation state in the current contest/conflict — is a legitimate state change in its own right; it simply does not obviously belong to either harm track (Track A: PE/MP→Overflow→HP, or Track B: Location→Wound, per Roadmap §7). That is an open question about which universal state interface should carry it, not evidence against including the candidate. |

---

## 10. Effect 9 — Damage Equipment

| Q | Answer |
|---|---|
| 1. State changed | Target's equipped item's condition/durability state. |
| 2. Mechanical action | Reduces an item's functional state (damaged, degraded, destroyed) — exact granularity (binary broken/intact vs. a durability track) depends on Equipment (Proposals §13), which is itself Reserved. |
| 3. Instantaneous or persistent | Persistent — a damaged item stays damaged pending repair (Proposals §13, "repair/replacement" listed but unresolved). |
| 4. Target-state requirement | Requires the target to have a valid, damageable equipped item — structurally similar to Disarm's target-state check (§4 Q4), but against item durability rather than item possession. |
| 5. Tags required | Plausible — an item's Tags might specify whether it is damage-vulnerable (Proposals §11 lists "weapons; armour" as Tag consumers). |
| 6. Location Index required | **Open — named State-3 fork (Round 1 §5).** Location-dependent path: Location Index lands on the equipped item's carried location. Location-independent path: Margin/Quality-band or Tag-gated trigger. Same unresolved status as Disarm — not decided here. |
| 7. Stacking | Plausibly cumulative if Equipment (S-13) eventually defines a multi-step durability track rather than a binary state; not decided, since Equipment is Reserved. |
| 8. S-4 interaction | None identified — this Effect targets gear, not the character's body. |
| 9. S-5/S-6 interaction | **[Corrected v1.1]** Direct dependency on Equipment (Proposals §13, which lists "equipment damage" among its required areas) in all cases, since any damageable item — weapon, shield, tool, structure, clothing, magical item — falls under that subsystem. Additional, more specific direct interaction with S-5 (Armor) arises **only** when the damaged equipment is armor or the damage mechanism crosses the armor-interaction model (Proposals §5's "Bypass-style armour interaction"). S-5 is therefore a conditional dependency layered on top of the unconditional Equipment dependency, not an equally-weighted second dependency for every instance of this Effect. |
| 10. Character | Physical/tactical, targeting gear rather than the body. |
| 11. Differentiation | Distinct from Disarm in that it degrades an item's function rather than removing it from the target's grip — an item can be Damaged without being Disarmed and vice versa, so despite structural similarity in their Q4/Q6 answers, this document does not treat them as redundant. |

---

## 11. Effect 10 — Choose Location

**This Effect's identity is already partially addressed by Round 1 §5.1, which disambiguated three distinct interpretations. That disambiguation is restated here rather than repeated in full, then run through the checklist per-interpretation where the interpretations diverge.**

| Q | Interpretation A (declare intent) | Interpretation B (choose the Index result) | Interpretation C (convert Index to actionable result) |
|---|---|---|---|
| 1. State changed | Declared narrative/tactical intent only — no mechanical state change | Would change *which* Location Index value is used | Adds a downstream mechanism that consumes an already-generated Location Index and produces a mechanical consequence at a mapped zone/component |
| 2. Mechanical action | None — framing only, close to the S-2 attack-side "named distinct outcome" declaration (Proposals §2.1A) | Overrides or selects Zero-Step's deterministic output | Maps Index → zone/component and applies an effect there |
| 3. Instantaneous/persistent | N/A (declaration, not a state) | Instantaneous | Instantaneous trigger, persistent consequence (comparable to Injury) |
| 4. Target-state requirement | None | None | Requires an already-generated Location Index (i.e., a resolution where a Location Index exists at all — itself gated by S-2's attack-side warrant policy, Proposals §2.1A, and categorically excluded for non-attack resolutions, Proposals §2.5A) |
| 5. Tags required | No | No | Possibly, for which zones/components are actionable |
| 6. Location Index required | No — this interpretation doesn't touch the Index at all | Yes, directly — and this is exactly what makes it fail the invariant check | Yes — this is its entire purpose |
| 7. Stacking | N/A | N/A | Unclear — depends on whether multiple Index-derived consequences on the same target compound |
| 8. S-4 interaction | None | None | Direct — the "mapped zone/component" consequence is naturally Wound-Engine-adjacent |
| 9. S-5/S-6 interaction | None | None | Plausible if armor coverage varies by zone (S-5) |
| 10. Character | Narrative | Mechanical (excluded) | Physical/mechanical |
| **Invariant status** | No conflict identified | **Fails — Canonical §14.2, locked.** Excluded from current S-3 design space (Round 1 §5.1, §9). Not carried further in this document. | No conflict identified, with the dependency caveat below |

**11. Differentiation (Effect-level, not per-interpretation):** "Choose Location" is unique among the ten candidates in that its identity question is not "what does it mechanically do" in isolation, but "which of three non-equivalent things is it." Interpretation A is closest in character to a no-op flavor declaration (weakest mechanical identity of the ten). Interpretation C is the only one of the three with a fully specified mechanical role, but that role is explicitly a **dependency on S-2's still-open anatomical mapping** (Proposals §2.4–§2.5), not something S-3 can complete unilaterally — per Round 1 §5.1's "dependency, not identity" note, developing Interpretation C would consume that mapping as a named prerequisite, not discharge S-2's obligation to define it. This document does not select among A/B/C; per Round 1 Decision Point 3, that remains open.

---

## 12. Cross-Effect Observations (Checklist Question 11, Consolidated)

**[Design inference — pattern-level synthesis across the ten individual answers above, not a new evidence class]**

| Observation | Effects involved | Status |
|---|---|---|
| Possible redundancy | Effect 7 (Bleed/Ongoing Drain) and Effect 2 (Impose Condition → Bleeding) | Flagged, not resolved — see §8 Q8/Q11 |
| Structurally parallel target-state preconditions (stale-objective pattern) | Effect 3 (Disarm), Effect 6 (Guard Break), Effect 9 (Damage Equipment) | Noted as a shared *shape*, not asserted to require a shared *rule* |
| Blocked on a wholly undefined prerequisite subsystem | Effect 5 (Seize Tempo) — blocked on Proposals §12 (Time/Action Economy, no draft direction at all); Effect 6 (Guard Break) — blocked on Proposals §6 (S-6 Defense, Reserved/Proposed with only a rejected Passive Guard candidate on record) | These two candidates have the least resolvable identities in this round, for different reasons than the location-dependence forks affecting Effects 3, 9, and (partially) 2 and 1 |
| Location Index dependence status, consolidated | Effect 1 (Injury) — newly surfaced open fork, not previously named by S-2; Effect 2 (Condition, function-impairment sub-case) — inherited State-3 fork; Effect 3 (Disarm) — inherited State-3 fork; Effect 9 (Damage Equipment) — inherited State-3 fork; Effect 10 (Choose Location, Interpretation C only) — dependency on S-2's anatomical mapping, distinct in kind from the State-3 forks | None of these five are resolved by this document; Round 1 §0 and this document's own §0 both exclude resolving them here |
| No plausible Location Index dependence identified | Effect 4 (Force Movement/Seize Position), Effect 5 (Seize Tempo), Effect 6 (Guard Break), Effect 8 (Open Retreat/Compel Yield) | These four appear location-independent by nature of what they act on (position, tempo, defense state, morale) rather than by an explicit ruling |
| Sole narrative/morale-primary Effect | Effect 8 (Open Retreat/Compel Yield) | Its mechanical hook is the least defined of the ten and may not fit the Track A/Track B interface (Roadmap §7) as currently drawn — flagged for Round 2b, not resolved |

---

## 13. Scope-Guard Compliance Check

*[Mechanical fact — verification against §0]*

| Guard | Compliance |
|---|---|
| S-1, S-2 Tier-1 provider, S-2 attack-side policy, S-2 non-attack deferral not reopened | Confirmed — all references above are read-only citations; Interpretation B (§11) is reaffirmed excluded, not reconsidered. |
| S-4 wound severity/activation not decided | Confirmed — every S-4 touchpoint above is noted as a dependency, not specified. |
| S-5/S-6 mechanics not decided | Confirmed — Guard Break (§7), Damage Equipment (§10), and Choose Location Interpretation C (§11) all note S-5/S-6 touchpoints without specifying them. |
| No numerical thresholds locked | Confirmed — no Quality band, Tag list, drain rate, or durability value appears anywhere above. |
| Decision Points 1–3 (Round 1 §8) not ruled | Confirmed — not referenced as resolved anywhere in this document. |
| Q3 delivery-mechanism forks (Disarm, Damage Equipment, function-impairment Conditions) not resolved | Confirmed — each is explicitly marked "open" at point of reference (§4, §10, §4 within §12). |
| Round 2b (Effect Weight) not performed | Confirmed — no relative-impact ranking or balance judgment appears; redundancy and blocked-subsystem flags (§12) are identity-level observations, not weight judgments. |

---

## 14. Summary Table — What Round 2 Established vs. What Remains Open

| Item | Status after this round |
|---|---|
| All ten Effects' identity-checklist answers | Recorded (§2–§11); several answers depend on other open forks/subsystems rather than being fully self-contained |
| v1.1 correction pass | Applied — four wording-precision corrections (Injury/non-attack boundary; Condition persistence; Compel Yield/Track interface framing; Damage Equipment's conditional S-5 dependency). No identity conclusion or dependency finding changed in substance. |
| "Choose Location" Interpretation B | Reaffirmed excluded (inherits Round 1 §5.1/§9 status; not re-litigated) |
| Possible Bleed/Ongoing Drain ↔ Bleeding-Condition redundancy | **Newly flagged this round** — not previously noted in Round 1 |
| Seize Tempo and Guard Break identified as blocked on wholly undefined prerequisite subsystems (Time/Action Economy, Defense) | **Newly flagged this round** — distinct in kind from the location-dependence forks |
| Injury's own Location Index dependence | **Newly surfaced this round** as an open fork not previously named by the S-2 State-3 table (which covers Disarm, Equipment, Impairment, Armor Bypass, Incapacitation, but not Injury itself) |
| Stale-objective structural pattern across Disarm/Guard Break/Damage Equipment | Noted as a shared shape, not a shared rule — for Round 3 to consider |
| Effect Weight / relative balance (Round 2b) | Not performed — remains the next step per Round 1 §8's sequencing |
| Decision Points 1–3 (Round 1 §8) | Unchanged — still carried forward, unruled |

**No candidate Effect's identity is finalized by this document, and no ruling is made.** Per the sequencing fixed in Round 1 §8, the next step is Round 2b (Effect Weight/Consequence) — evaluating relative mechanical/narrative impact and S-2/S-4/S-5/S-6 boundary interactions now that identity is on record — followed by Round 3 (Effect Access: Eligibility × Capacity × Selection).
