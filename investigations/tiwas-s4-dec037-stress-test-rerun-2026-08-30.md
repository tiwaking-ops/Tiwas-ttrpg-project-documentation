# DEC-037 Stress-Test Re-Run — Literal 14-Scenario Verification Against the Corrected Wound-as-Condition Model

**Date:** 2026-08-30
**Authoring context:** OpenCode (Lead Documentarian) — direct read of source text, no memory reconstruction
**Status:** Non-canonical design evidence — verification record for the S-2 reopening stress-test step
**Source verified against:** `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` §5 (read in full, lines 95–110)

---

## 1. Purpose

The S-2 non-attack closure record's reopening conditions (`tiwas-s2-non-attack-location-source-closure-record-v1.2.md` §4) require that reopening `DEC-020` re-run or extend the preserved 14-scenario stress-test set (§5) against whatever the reopening subsystem (i.e. S-4) actually specifies.

This step was attempted **twice** earlier in the S-4 thread and **both attempts fabricated scenario descriptions** (documented in `tiwas-s4-documentarian-handoff-report-2026-08-30.md` §4.2 and §4.3). This record is a **third, independent** attempt performed with direct read access to the literal source text, re-quoting each scenario verbatim rather than reconstructing from memory, as recommended in that report §4.4.

Human designer (Tiwa) authorised this re-run on 2026-08-30.

## 2. Corrected Model Under Test (DEC-033 / DEC-037, non-canonical)

1. **Wound-as-Condition (DEC-033):** Wound is realized as the **"Wounded" Condition**, selected via S-3 Effect #2 (Impose Condition) — not a standalone menu entry. **Both *Inflict Injury* (Effect #1) and *Impose Condition: Wounded* require a Location Index when selected as Effects.** Overflow→HP is automatic and exempt.
2. **Primary Provenance Rule (DEC-037 §1):** When a character fails a governing Core Test against an environmental hazard/obstacle/physical risk, that **same failed d100 roll** supplies the digits for Zero-Step Tier-1 Location Index generation (Canonical §14.1–14.2).
3. **Hazard "Win" (DEC-037 §2):** A failed test = "win" for the hazard; if failure margin/severity qualifies for an S-3 Effect, the Effect is applied at the location indicated by the failed roll.
4. **Systemic Exempt (DEC-037 §3):** Global/systemic threats (Drowning, Suffocation, Extreme Temperature, Poison) apply direct HP/Conditions, no Location Index.
5. **Passive Fallback (DEC-037 §4):** If a physical impact occurs with no roll of any kind, output a numeric stub Location Index (`00`/`50`) through Zero-Step, deferring anatomical naming to OPEN-003.

## 3. Literal Re-Run of All 14 Scenarios

| # | Verbatim scenario (source §5) | Resolution under corrected model | Verdict |
|---|---|---|---|
| 1 | Character reacts to a fall, attempts to catch self | Reaction test exists. If the character **fails** the catch/save test, that same failed d100 roll supplies the Zero-Step LI (DEC-037 §1). If the failure margin qualifies for an Effect, *Inflict Injury* or *Impose Condition: Wounded* applies at that LI (DEC-037 §2). A fall is physical/localized (not systemic), so a LI is required to apply a Wound Effect. | **Passes** |
| 2 | Character fails to react to a fall, no test offered | **No test offered = no roll of any kind.** Physical impact occurs. Passive Fallback (DEC-037 §4) applies: output numeric stub LI (`00`/`50`) through Zero-Step; anatomical naming deferred to OPEN-003. A LI is still produced so a Wound Effect is not blocked. | **Passes** (via passive fallback) |
| 3 | Character deliberately causes a hazard affecting themself | Self-inflicted. Two sub-cases: (a) if the character makes a governing test against their own hazard and **fails**, provenance rule (DEC-037 §1) — their own failed roll supplies the LI; (b) if **no test is made** (arbitrary self-harm), Passive Fallback (DEC-037 §4) supplies a stub LI for any physical impact. The model does not distinguish who caused the hazard, only whether a governing failed test exists. | **Passes** (both sub-cases covered) |
| 4 | Hazard affects its creator vs. affects a different character | Cross-character case (H0 Rider A: no cross-character roll-sharing). DEC-037 §1 as agreed uses the **affected character's** own governing test failure. If the affected character made **no** test of their own, no other character's roll is borrowed (Rider A preserved), and any physical impact falls to Passive Fallback (DEC-037 §4) → stub LI. Distinguishing creator vs. other-affected does not change the rule: provenance is per-affected-character. | **Passes** (Rider A honoured; passive fallback for no-test) |
| 5 | Environmental hazard with a resistance test | Character fails the resistance test → that same failed d100 roll supplies the LI (DEC-037 §1). Environmental hazard, localized physical → if Effect margin qualifies, apply at LI (DEC-037 §2). | **Passes** |
| 6 | Trap with a Perception/Reflexes reaction test | Character fails Perception/Reflexes reaction → failed roll supplies LI (DEC-037 §1). Trap is localized physical → Effect applies at LI (DEC-037 §2). | **Passes** |
| 7 | Automatic trap, no test offered | **No test offered = no roll.** Physical impact from a trap → Passive Fallback (DEC-037 §4) → stub LI (`00`/`50`) through Zero-Step. Localized physical, so a LI is generated so a Wound Effect remains possible. | **Passes** (via passive fallback) |
| 8 | Collapsing structure, test exists | Character fails the test (e.g. Evasion) vs. collapsing structure → failed roll supplies LI (DEC-037 §1); localized physical Effect applies at LI (DEC-037 §2). | **Passes** |
| 9 | Collapsing structure resolved entirely by narration | **No test made** (narration-only). If the narration establishes a physical impact warranting a Wound Effect, Passive Fallback (DEC-037 §4) supplies a stub LI. If the narration imposes only flat/systemic harm or no mechanical Wound Effect, no LI is needed at all. Both outcomes are consistent with the model. | **Passes** (passive fallback / no-LI as applicable) |
| 10 | Extended Test interval produces the physical consequence | Consequence emerges on an Extended Test interval (touches S-9). A governing failure within the interval supplies the LI (DEC-037 §1). If **multiple tests** are involved in the interval, **H0 Rider B's two sub-options remain unadjudicated** (governing test = the one determining the affected character's own outcome, vs. the first causally-relevant test) — original record §3 never resolved this. **Residual flag: Rider B needs its own adjudication before this scenario is fully deterministic.** | **Passing with residual flag (Rider B unadjudicated)** |
| 11 | Multiple affected characters, independent tests | Each affected character's **own** failed test supplies their **own** LI (DEC-037 §1; Rider A consistency). Independent, no sharing. | **Passes** |
| 12 | One character's test causes the event; a different character's test resolves its impact | Causal-chain (Rider A + Rider B territory). DEC-037 §1 as agreed uses the **affected character's resolving test**. If the affected character (whose body takes the impact) fails their resolving test, that same roll supplies their LI. A causing character's roll is **not** transferred (Rider A preserved). If the affected character makes no resolving test, Passive Fallback (DEC-037 §4) → stub LI. | **Passes** (Rider A honoured) |
| 13 | An S-1 opposed contest is involved | A contest between parties exists. The **losing** roll of the affected character supplies the LI (DEC-037 §1, consistent with the attack-side pattern that already routes through Zero-Step). This sits at the boundary of the "non-attack" definition but is handled uniformly by provenance. | **Passes** |
| 14 | Trap resolved retroactively via a Stakes Gate–style reaction | Depends on the S-8 Stakes Gate mechanism, which is **not yet defined** (S-8 is open). Provisional: if the retroactive reaction confers a failed governing roll → provenance (DEC-037 §1); if it confers **no roll** → Passive Fallback (DEC-037 §4) → stub LI. Fully deterministic resolution waits on S-8. | **Passing with S-8 dependency** |

## 4. Summary of the Re-Run

| Outcome | Count | Scenarios |
|---|---|---|
| Passes (provenance: failed governing roll supplies LI) | 8 | 1, 3(a), 5, 6, 8, 11, 12, 13 |
| Passes (passive-fallback: no roll of any kind → stub LI) | 5 | 2, 3(b), 4, 7, 9 (no-LI alternative), 14 (provisional) |
| Passing with residual flag | 2 | 10 (Rider B unadjudicated), 14 (S-8 dependency) |

**All 14 scenarios are handled by the corrected DEC-033/DEC-037 model** (each either by primary provenance, systemic exemption, or passive fallback). This contrasts with the two earlier fabricated attempts, which cited invented content.

## 5. Residual items surfaced by the re-run (not blocked, but flagged)

1. **H0 Rider B unadjudicated** (scenario 10): the Extended-Test multi-test tie-break (governing = affected character's own outcome vs. first causally-relevant test) was never decided by the original S-2 investigation (closure record §3, "never adjudicated against each other"). DEC-037 does not resolve it. This is a **separate open sub-question** to be adjudicated if/when S-9 (Extended Test) reaches the relevant stage.
2. **S-8 dependency** (scenario 14): retroactive Stakes Gate–style resolution cannot be fully determinised until the S-8 mechanism is defined.
3. **Anatomical naming deferred** (OPEN-003): the passive-fallback stub (`00`/`50`) is only ever an index; it cannot map to a body region until OPEN-003 locks. Consistent with DEC-037 §4.

**Neither residual item blocks DEC-037's own scope** (which defines *how* a Location Index is generated, not the still-open anatomical mapping or S-9 tie-break). These are recorded for traceability, not as open blockers on DEC-037.

---

## 6. Conclusion

The stress-test reopening-protocol step for `DEC-037` / `OPEN-008` is now **genuinely satisfied** against the literal §5 source text. `DEC-037`'s non-attack Location Index generation mechanism is consistent with all 14 scenarios under the corrected Wound-as-Condition model (DEC-033), with two non-blocking residual flags (Rider B, S-8).

This record supersedes the two fabricated stress-test attempts documented in `tiwas-s4-documentarian-handoff-report-2026-08-30.md` §4.2–§4.3 for the purpose of satisfying the reopening protocol.
