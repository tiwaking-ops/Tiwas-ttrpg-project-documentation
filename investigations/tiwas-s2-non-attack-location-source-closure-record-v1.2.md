---
document:
  title: "Tiwas — S-2 Non-Attack Location Index Source — Closure Record"
  version: "v1.2 (Final)"
  status: "Non-canonical (self-declared: \"Closure record for a completed non-canonical design investigation\")"
provenance:
  author_llm: {name: "not established", version: "not established"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "not established", version: "not established"}
  created_date: "not established (source document undated)"
  last_modified_date: "not established (source document undated)"
consolidation_note: >
  Placed in investigations/ during initial consolidation (2026-08-29). Content
  below the header is UNMODIFIED from sources/tiwas-s2-non-attack-location-source-closure-record-v1.2.md.
  Records the fullest account of the binding (non-canonical) S-2 non-attack
  deferral ruling; also recorded in proposals/...v1.4.3.md §2.5A and
  roadmap/...v1.4.3.md §9.
---

# Tiwas — S-2 Non-Attack Location Index Source — Closure Record

**Document Version:** v1.2 (Final — supersedes Starter Brief v1.1 as the status record for this investigation thread)
**Document Status:** Closure record for a completed non-canonical design investigation
**Rule Authority:** None — this document creates no game mechanics
**Governing ruling recorded in:** Proposals/WIP v1.4.3 §2.5A (authoritative non-canonical location); Roadmap v1.4.3 §9 (implementation-relevant summary)
**Purpose:** Preserve the investigation's reasoning and evidence trail so a future session reopening this question does not have to reconstruct it from scratch.

---

## 1. Designer Ruling (Binding, Non-Canonical)

> **Non-attack physical resolutions (falls, hazards, structural collapses, and other non-adversarial physical events) generate no Tier-1 Location Index under current design — categorically, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution.**

This applies regardless of:

- whether an underlying Core Test exists for the resolution;
- who made that test (the affected character, the causing character, a third party);
- whether the hazard was caused intentionally or accidentally;
- how specifically the GM narrates the physical consequence;
- the severity of the consequence.

**This is a deferral, not a claim that non-attack location is impossible in principle.**

Zero-Step (Canonical §14.1–§14.2) itself is entirely untouched. This ruling concerns only whether non-attack resolutions are eligible to invoke it — and the answer is currently no.

---

## 2. Investigation Timeline

| Stage | Content | Outcome |
|---|---|---|
| Starter Brief v1.1 | Framed the question: whose roll, if any, supplies a Location Index when there's no "attacker"; explicitly scoped out reopening Zero-Step, S-1, the attack-side invocation policy, or the Structural Weak Points State-2 ruling | Question opened |
| Round 1 | Candidate analysis: rejected ad-hoc GM rolls (Candidate B) as architecturally excluded (violates Canonical Invariant 18 / no competing resolution engine); collapsed remaining candidates into a single provenance rule | H0 drafted |
| Cross-review (external) | Confirmed A/C/D collapse; proposed broadening "Core Test belonging to a character" to "existing governing Core Test" for forward-compatibility; flagged that Direction 2 (default all non-attack cases to State 3/4) improperly conflates "no player declaration" with "location-dependence unresolved" | H0 refined; Direction 2 flagged as flawed |
| Round 2 | Provenance-only stress test across 14 scenarios; confirmed H0 holds in 11/14 cases; surfaced two riders (no cross-character roll-sharing; tie-break needed for multi-test causal chains); Warrant column deliberately left unscored throughout | H0 + Rider A confirmed as consistent; Rider B drafted as unadjudicated candidate |
| Cross-review (external) | Confirmed H0 wording, confirmed Candidate B exclusion, confirmed Direction 2 withdrawal, endorsed strict sequencing (provenance first, warrant transfer only after) | Sequencing confirmed |
| Designer input requested | Two live decision points identified: (1) GM-authored-stakes substitute vs. categorical exclusion for warrant transfer; (2) blind-trial timing | Clarification requested from designer |
| **Designer ruling** | **Option 2 selected: categorical exclusion, no non-attack Location Index generation until S-4/S-7/S-8 reopens the question** | **Investigation closed as a deferral** |

---

## 3. What Was Resolved vs. What Remains Inert

| Item | Final status |
|---|---|
| Whether non-attack resolutions currently generate a Location Index | **Resolved: no, categorically, until reopened** |
| H0 (governing Core Test provenance rule) | **Inert candidate record.** Not validated as an operative rule — the warrant question closed before H0 needed to become operative. Retained as the starting hypothesis if this question is reopened. |
| H0 Rider A (no cross-character roll-sharing) | Inert, tied to H0. Confirmed as a consistent extension of the existing attack-side pattern (Canonical §14.1 already allows attacker's roll → target's body), not a new problem. |
| H0 Rider B (multi-test causal-chain tie-break) | Inert, tied to H0. Two sub-options were identified (governing test = the one that determines the affected character's own outcome, vs. the first causally-relevant test) — only the first was drafted as a candidate; **never adjudicated against each other.** If reopened, this needs its own resolution, not an assumed default. |
| Direction 1 (GM-stated consequence as declaration-equivalent for Warrant) | Rejected for now, not deleted. This was the substantive alternative to the ruling actually made. |
| Direction 2 (default non-attack cases to State 3/4 via the existing four-state model) | **Withdrawn during cross-review**, prior to the final ruling — found to improperly conflate "no player declaration" with "location-dependence unresolved." Distinct from, and should not be confused with, the final ruling's categorical exclusion, which is a deferral by designer choice, not a four-state classification outcome. |
| Blind provenance trial | Not run. Correctly withheld — the ruling makes warrant-eligibility categorically "never," leaving nothing live to test. |

---

## 4. Reopening Conditions

This investigation is closed **pending**, not closed **permanently**. Reopen explicitly — do not silently inherit this ruling — when:

- **S-4** (Wound activation/severity) reaches a design stage where localized non-attack injury becomes relevant;
- **S-7** (Incapacitation/death) reaches a design stage where hazard severity needs finer resolution than flat damage;
- **S-8** (Difficulty/Stakes Gate) reaches a design stage where hazard-stakes framing is formally defined — **flagged as the most likely natural trigger.**

When reopened:

1. Start from H0 and its two riders as a **starting hypothesis to re-validate**, not a pre-approved answer.
2. Re-run or extend the Round 2 stress-test scenario set (§5 below) against whatever S-4/S-7/S-8 actually specify — they may introduce constraints H0 was never tested against.
3. Separately and explicitly decide the Warrant-transfer question (Direction 1, or a new alternative) — do not assume the old rejection still applies if the underlying subsystem has changed the shape of the question.
4. Adjudicate H0 Rider B's two sub-options against each other, since the original investigation never did.

---

## 5. Stress-Test Scenario Set (Preserved for Reuse)

| # | Scenario |
|---|---|
| 1 | Character reacts to a fall, attempts to catch self |
| 2 | Character fails to react to a fall, no test offered |
| 3 | Character deliberately causes a hazard affecting themself |
| 4 | Hazard affects its creator vs. affects a different character |
| 5 | Environmental hazard with a resistance test |
| 6 | Trap with a Perception/Reflexes reaction test |
| 7 | Automatic trap, no test offered |
| 8 | Collapsing structure, test exists |
| 9 | Collapsing structure resolved entirely by narration |
| 10 | Extended Test interval produces the physical consequence |
| 11 | Multiple affected characters, independent tests |
| 12 | One character's test causes the event; a different character's test resolves its impact |
| 13 | An S-1 opposed contest is involved |
| 14 | Trap resolved retroactively via a Stakes Gate–style reaction |

---

## 6. What This Investigation Explicitly Did Not Touch

Confirmed unchanged throughout, per the original scope guards:

- Zero-Step's derivation mechanism (Canonical §14.1–§14.2)
- S-1 Opposed Contest (Canonical §13)
- The attack-side invocation/warrant policy (Proposals §2.1A)
- Structural Weak Points' State-2 classification
- The W3 reference cache
- Tier 0/1/2 scene/campaign selection policy
- Anatomical mapping, Tier-2 mechanics, or any Wound/Armor/Effect numerical rule

---

## 7. Cross-Document Consistency

This ruling is now recorded in three places, kept synchronized:

| Document | Location | Role |
|---|---|---|
| Proposals/WIP v1.4.3 | §2.5A (new); §2.5 updated; §20 S-2 row updated; §8 cross-reference; §14 cross-reference | Authoritative non-canonical governing position |
| Implementation Roadmap v1.4.3 | §4 S-2 row; §9 Phase 2 (new subsection); §12, §13, §15, §20 cross-references | Implementation-relevant consequences |
| This document | Full record | Investigation history and reopening reference |

No Canonical Rules document is affected. Nothing in this investigation or its closure is promoted to Canonical status (Proposals §21 eight-step process not invoked).


