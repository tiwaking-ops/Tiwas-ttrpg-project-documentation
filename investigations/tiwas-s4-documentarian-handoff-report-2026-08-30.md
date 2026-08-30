# Tiwas — S-4 (Wound Activation/Severity) Cross-Model Session — Documentarian Handoff Report

**Document Version:** v1.0
**Document Status:** Handoff record — consolidates a completed cross-model discussion thread; contains items ready to record and items still pending designer decision. Not itself a source of Canonical or Non-canonical rules.
**Rule Authority:** None — this document creates no game mechanics. It records what was discussed, what the designer ruled, and what remains open. All actual register/proposals edits are to be made by OpenCode against the live repository.
**Prepared By:** Claude Sonnet 5 (claude-sonnet-5), in the Lead Systems Architect / Design Assistant role for this project, working from the static project snapshot (`TTTRPG-merge-v1.md`) — no live repository access this session.
**Session Participants:**
- **Designer (Tiwa):** Sole ruling authority.
- **DeepSeek Harness:** Primary session agent, live repository/filesystem access, authoritative for current register state.
- **Gemini 3.6 Flash:** Advisory model, multiple turns, proposed rulings and register text.
- **Claude:** Cross-model audit/critique role, working from a static project snapshot (no live repo access this session).
**Purpose:** Consolidate the full S-4 discussion thread (four transcript exchanges) into one authoritative handoff so OpenCode can reconcile the live `_consolidation/decision-register.md` and `proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md` against it, and so Tiwa's final decision is applied against verified, not fabricated, content.

---

## 1. Session Chronology

| Stage | Actor | Content |
|---|---|---|
| Pre-session | Prior model (unspecified) | Initial S-4 pass ruled F1 "location-gated" using the now-superseded "repeated hits to same location" S-4 direction from DEC-029. F2–F6 left open. |
| Designer correction | Tiwa | Overturned the repeated-hits model. Established: Overflow never causes Wounds; Wound is a selectable Effect outcome, not an accumulation mechanic; Injury/Wound terminology split required; Wound severity is a numeric counter (more wounds = more severe, each individually equivalent); "Greater Wounds" (e.g. Serious Frost/Fire/Shock) are distinct, independent Effects, not upgrades to the base Wound state. |
| Revision (Gemini, session 1) | Gemini 3.6 Flash | Re-ruled F1–F6 under the new designer framing. Drafted `DEC-032`–`DEC-036`, opened `OPEN-006`–`OPEN-008`, reopened `DEC-020` (S-2 non-attack deferral). Reported these as written to the live register and proposals file. |
| Claude audit #1 | Claude | Flagged three issues in the Gemini-1 output: (1) "Wound" treated as a selectable Effect that does not actually exist on the S-3 candidate Effect menu; (2) unresolved ambiguity over whether the Location-Index gate applies to *Inflict Injury* as well as *Wound*; (3) proposed `DEC-037` passive-fallback clause ("defaults to Center Mass/Torso") bypasses Zero-Step and the still-open anatomical mapping question (`OPEN-003`). Also flagged an unverified ID-collision risk and an incompletely-run stress-test reopening protocol. |
| Designer resolution | Tiwa | **Gap 1:** Wound realized via the *existing* Effect #2 (Impose Condition) — "Wounded" as a Condition, not a new menu entry. **Gap 2:** Confirmed — Location Index requirement applies to both *Inflict Injury* and *Wound* when selected as Effects. **Gap 3 (stress-test):** Forwarded to DeepSeek Harness. **Gap 5 (ID collision):** Forwarded to DeepSeek Harness. **Gap 4 / 6:** Held for further discussion. |
| Gemini response (session 2) | Gemini 3.6 Flash | Responded to Claude's *original* critique only (designer's resolutions above had not yet reached it). Proposed adding a new 11th Effect, "Inflict Wound" — **conflicting with Tiwa's actual Gap-1 decision**. Recommended *Inflict Injury* does **not** need a Location Index — **directly contradicting Tiwa's confirmed Gap-2 "yes."** Accepted and correctly refined the passive-fallback clause to a numeric stub routed through Zero-Step. Reported the register as ID-collision-clean and `DEC-037` as the next available ID. Cited three stress-test scenarios (#5, #8, #12) with descriptions that **did not match** the source document. |
| Claude audit #2 | Claude | Flagged both contradictions between Gemini's session-2 recommendations and Tiwa's actual rulings. Confirmed the passive-fallback fix as sound. Flagged the scenario citations as fabricated (mismatched against the actual §5 table in `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md`), and cross-referenced this against a documented prior incident of Gemini fabricating citations in this project. |
| DeepSeek Harness response (session 3) | DeepSeek Harness | Accepted Claude's Point 1 (Wound-as-Condition) and Point 2 (Location Index gates both Injury and Wound) as correct, with proposed register text. Confirmed the passive-fallback numeric-stub wording. Reported having re-read the source document "lines 61–105" and produced a **new** four-scenario table (#1–#4) — which **still does not match** the actual source text (see §4 below). Reported `DEC-037` text ready to record, pending Tiwa's go-ahead. |
| Claude audit #3 | Claude | Confirmed Points 1–3 (Wound-as-Condition, Location Index scope, passive fallback) as now accurately captured and ready to record. Flagged that the "corrected" stress-test table is a **second, independent fabrication** — none of the four re-cited scenarios match the source document's actual numbered content — and recommended the reopening protocol's stress-test requirement not be treated as satisfied until the literal source text is verified and re-run. |
| **This report** | Tiwa → OpenCode | Consolidates the above for OpenCode's reconciliation against the live repository and Tiwa's final decision. |

---

## 2. Terminology Lock (Confirmed, Ready to Record)

| Term | Definition |
|------|-----------|
| **Injury** | Hit Point (HP) damage. Track A harm. |
| **Wound** | A localized, lasting state, tracked numerically (wound count), distinct from HP damage. Track B harm. Each individual Wound is functionally equivalent at base level; severity is purely numerical (more wounds = more severe). Healing is a numerical process. |
| **Greater Wound** | A distinct, independent S-3 Effect (e.g. Serious Frost, Serious Fire, Serious Shock), gated by Quality per `DEC-031`. Does not upgrade or alter the state of a base Wound or of a lower-tier version of the same effect. May not be curable by standard Wound-healing procedures. |

---

## 3. Ruled / Confirmed Positions (Designer-Confirmed, Ready for OpenCode to Record)

| # | Ruling | Status | Notes for OpenCode |
|---|--------|--------|-------------------|
| 1 | **Overflow never causes Wounds.** Overflow is exclusively Track A/HP damage — automatic, no Effect selection, no Location Index involved. | Confirmed by designer | Should already be reflected as `DEC-033`/`DEC-034` in the live register per Gemini session 1 — verify wording matches this exact framing. |
| 2 | **Wound is realized as the "Wounded" Condition, selected via existing Effect #2 (Impose Condition)** — not a new, separate "Inflict Wound" menu entry. | Confirmed by designer; supersedes Gemini's session-2 proposal to add an 11th Effect | **Correction required:** if the live register or proposals text currently describes "Inflict Wound" as a standalone Effect (per Gemini session 2's recommendation), this must be corrected to reflect Wound-as-Condition-via-Impose-Condition. |
| 3 | **Both *Inflict Injury* (Effect #1) and *Impose Condition: Wounded* require a Location Index when selected as Effects.** Overflow→HP damage remains exempt (no Effect selection occurs). | Confirmed by designer ("Gap 2. yes.") | **Correction required:** if the live register or proposals text states *Inflict Injury* does not require a Location Index (per Gemini session 2's recommendation), this must be corrected. |
| 4 | **Both Track A (Overflow→HP) and Track B (Wound Effects) may resolve from a single hit, sequentially** — cost/Overflow resolves first per the Core Test Transaction, then a successful contest allows Effect selection. | Confirmed, uncontested throughout | No correction needed. |
| 5 | **DEC-037 Passive Fallback (revised):** where a physical impact occurs with no roll of any kind, the system outputs a numeric stub Location Index (e.g. `00` or `50`), routed through Zero-Step exactly as any other index would be, deferring anatomical naming until `OPEN-003` (anatomical mapping) locks. Supersedes the earlier "defaults to Center Mass/Torso" wording, which bypassed Zero-Step and the unresolved anatomical mapping question. | Confirmed by all parties (Claude, Gemini, DeepSeek Harness) | Ready to record as the final Clause 4 wording for `DEC-037` once Tiwa approves `DEC-037` in full (see §5). |

---

## 4. Audit Finding: Stress-Test Citation Fabrication (Two Independent Instances)

The S-2 non-attack closure record's reopening conditions (`investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` §4) specify that reopening `DEC-020` should re-run or extend the preserved 14-scenario stress-test set (§5) against whatever the reopening subsystem (here, S-4) actually specifies. This step has been attempted twice in this thread, and **both attempts produced scenario descriptions that do not match the source document.**

### 4.1 Verified source table

The following is the actual §5 table, reproduced from the project snapshot for ground-truth reference:

| # | Scenario (verbatim from source) |
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

### 4.2 Instance 1 — Gemini, session 2

| Cited # | Gemini's description | Actual source content at that number |
|---|---|---|
| 5 | "Falling off cliff" | Environmental hazard with a resistance test |
| 8 | "Pit trap trigger" | Collapsing structure, test exists |
| 12 | "Unconscious in fire" | One character's test causes the event; a different character's test resolves its impact |

### 4.3 Instance 2 — DeepSeek Harness, session 3

Presented as a self-correction after being shown Instance 1, explicitly claiming to have re-read the source text directly. The resulting table still does not match:

| Cited # | DeepSeek's description | Actual source content at that number |
|---|---|---|
| 1 | "Single-character action, no opposition (e.g. leap across chasm)" | Character reacts to a fall, attempts to catch self |
| 2 | "Environmental hazard with a resistance test" | Character fails to react to a fall, no test offered |
| 3 | "Causal chain: Character A pushes Character B off cliff" | Character deliberately causes a hazard affecting themself |
| 4 | "Environmental hazard with NO test allowed (falling into pit trap while sleeping)" | Hazard affects its creator vs. affects a different character |

### 4.4 Assessment

This is a second, independent citation-accuracy failure from this model family within the project's history (a prior Gemini meta-analysis session separately surfaced fabricated citations, a conceptual mischaracterization, an invented menu item, and a tabulation error — all previously documented). The reopening protocol's stress-test step has **not** been genuinely satisfied by either attempt. **Recommendation: do not treat this requirement as closed.** If the stress-test step is to be completed, it should be done against the verified table in §4.1 above, ideally by an agent with direct read access re-quoting the literal text rather than summarizing from memory, with particular attention to scenarios #3, #4, #7, and #12 — the ones structurally closest to the causal-chain and no-test cases Tiwa's own Case B/C/D reasoning addressed earlier in this thread.

---

## 5. Proposed DEC-037 (Non-Attack Location Index Generation) — Pending Tiwa's Final Approval

Not yet recorded. Current agreed text, incorporating the passive-fallback correction from §3 item 5:

> **DEC-037 (S-2 / S-4 Non-Attack Location Index Generation):**
> 1. When a character fails a governing Core Test against an environmental hazard, obstacle, or physical risk (e.g. Jump, Climb, Evasion, Spot Trap), that same failed d100 roll supplies the digits for Zero-Step Tier-1 Location Index generation (exchanging tens and units digits per Canonical §14.1–14.2).
> 2. The failed test constitutes a "win" for the hazard. If the failure margin or hazard severity qualifies for an S-3 Effect, the applicable Effect (e.g. *Inflict Injury* or *Impose Condition: Wounded*) is applied to the location indicated by the character's failed roll.
> 3. Environmental threats that act globally/systemically (e.g. Drowning, Suffocation, Extreme Temperature, Poison) do not require a Location Index and apply direct HP damage or systemic Conditions instead.
> 4. If a passive impact occurs without any roll of any kind, the system outputs a numeric stub Location Index (e.g. `00` or `50`), routed through Zero-Step exactly as any other index, deferring anatomical naming until `OPEN-003` locks.

**Open items before this can be finalized:**
- Stress-test verification per §4 above is outstanding.
- ID-collision check (`DEC-032`–`036`, `OPEN-006`–`008` clean, `DEC-037` next available) was reported clean by DeepSeek Harness but has not been independently re-verified outside the models under audit in this thread.

---

## 6. Remaining Open Items (Unchanged by This Thread)

| ID | Item | Status |
|----|------|--------|
| `F2` | Track A/Track B interaction — already ruled concurrent (§3 item 4 above); not in dispute. | Ruled |
| `F4` / `OPEN-007` | Wound-state consequences (numerical accumulation and/or Greater Wound Effects) | Open — no candidate recorded |
| `F3` / `OPEN-006` | Numerical thresholds for Light/Serious/Critical descriptive categories | Open — requires simulation gate (effect frequency, exchange length, resource expenditure, wound frequency, severe-injury rate) before any threshold is locked |
| `F5` / `OPEN-003` | Anatomical mapping (Location Index → body/structural component) | Open — blocks all localized Wound Effect application; also gates when `DEC-037`'s passive-fallback stub can receive an anatomical name |
| `OPEN-008` | Non-attack Location Index generation mechanism | Pending — see `DEC-037` proposal above, not yet closed |

---

## 7. Recommended Action Items for OpenCode

1. Pull current live text of `DEC-032`–`DEC-036` and Proposals §4 from the repository; diff against §2–3 of this report.
2. Correct any live text describing "Inflict Wound" as a standalone 11th S-3 Effect — replace with Wound-as-Condition-via-Impose-Condition (§3 item 2).
3. Correct any live text stating *Inflict Injury* does not require a Location Index — both Injury and Wound require it when selected as Effects (§3 item 3).
4. Do **not** mark `OPEN-008` closed or record `DEC-037` until Tiwa gives explicit final approval, and until the stress-test verification gap in §4 is resolved to Tiwa's satisfaction (or explicitly waived by Tiwa).
5. Independently re-verify the ID-collision check reported in session 3 (`DEC-032`–`036`, `OPEN-006`–`008` clean; `DEC-037` next available) rather than relying solely on the report from the model under audit.
6. Once Tiwa's decision is received, update `_consolidation/decision-register.md` and `proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md` accordingly, and produce a closure note cross-referencing this handoff report.

---

## 8. Governance Notes

- All items in this report remain **Non-canonical** pending the 8-step Promotion Rule; nothing here modifies `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`.
- This report was produced by Claude Sonnet 5, working from a static project snapshot without live repository access this session; all "live register" state claims attributed to DeepSeek Harness or Gemini in this report are as reported by those sessions, not independently verified by Claude, except where directly cross-checked against the snapshot content as shown in §4.