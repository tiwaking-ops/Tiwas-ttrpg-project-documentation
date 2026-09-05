---
document:
  title: "Tiwas TTRPG â€” Ice Troll Combat Playtest: Cross-Referenced Comparison Report"
  version: "1.0"
  status: "Advisory working document (not canonical). Comparative analysis only. Makes no rulings, assigns no DEC numbers, promotes nothing to the live register."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: [{name: "opencode", version: "big-pickle"}]
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
source_documents:
  - {file: "tiwas-ice-troll-playtest-execution-handoff-claude-2026-09-04.md", author: "Claude Sonnet 5", lineage: "A â€” original session", extracted_from: "merged-combat-reports-playtest1.md"}
  - {file: "tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md", author: "GPT-5.6 Luna", lineage: "A â€” continuation of Claude's session", extracted_from: "merged-combat-reports-playtest1.md"}
  - {file: "tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md", author: "Grok 4.5", lineage: "B â€” independent full run", extracted_from: "merged-combat-reports-playtest1.md"}
---

# Tiwas TTRPG â€” Ice Troll Combat Playtest: Cross-Referenced Comparison Report

**Authority note.** This document is advisory. It compares, cross-references, and flags contradictions between three existing playtest records. It resolves nothing, rules on nothing, and assigns no DEC numbers. Every candidate item listed in Â§8 remains Open pending Tiwa's individual ruling and OpenCode's subsequent register recording. Where source reports disagree, both positions are presented without a preferred resolution.

**Source note.** The three source records were extracted from `merged-combat-reports-playtest1.md`, a bundled file containing approximately thirty documents (nineteen independent Adventure Readiness Audits, eight System-by-System Comparison meta-documents, and these three combat-execution playtest reports). Only the three combat-execution reports identified below are in scope for this comparison; the readiness-audit and system-comparison documents in the same bundle are out of scope and not analyzed here. The extracted content of all three reports was confirmed identical in substance to previously reviewed versions.

---

## 1. Purpose and Scope

Three independent LLM-authored records document execution of `claude-playtest-prompt-version2.md` (v2.1) against the DEC-077.A Ice Troll conversion block:

| Ref | Document | Author | Role in this comparison |
|---|---|---|---|
| **D1** | `tiwas-ice-troll-playtest-execution-handoff-claude-2026-09-04.md` | Claude Sonnet 5 | Original session (2 rounds / 4 exchanges, explicit abort) |
| **D2** | `tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md` | GPT-5.6 Luna | Continuation of D1's abort state to combat resolution |
| **D3** | `tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md` | Grok 4.5 | Independent full 22-round run from the same starting conditions |

This report's purpose is narrow and specific: **determine which Ruled systems are validated for a full playtest, which remain unvalidated, which produced conflicting empirical results across the three records, and which numeric/mechanical gaps must be closed by Tiwa before proceeding.** It does not re-litigate any DEC. It does not judge whether either scaffold-value approach found below is "correct" â€” that determination is Tiwa's.

---

## 2. Execution Lineage â€” Critical Clarification

The three records do **not** describe three parallel trials of the same combat. They describe **two distinct empirical lineages**, and conflating them produces incorrect conclusions about sample size and convergence.

```
LINEAGE A (Claude â†’ Luna): one continuous combat
  D1: Round 1â€“2 (4 exchanges)  â†’  PC HP 600â†’585, Troll HP 705â†’698  â†’  explicit abort
  D2: continuation             â†’  PC HP 585â†’0,   Troll HP 698â†’569  â†’  Ice Troll victory (HP=0, DEC-052)

LINEAGE B (Grok): one independent combat, same starting stats, different rolls
  D3: 22 rounds                â†’  PC HP 600â†’0,   Troll HP 705â†’412  â†’  Ice Troll victory (HP=0, DEC-052)
```

**Implication for this report's confidence weighting:** any system exercised in *both* D1/D2 (Lineage A) and D3 (Lineage B) has **two independent empirical confirmations**. A system exercised only within Lineage A (D1+D2, which is one continuous combat) has **one** independent confirmation, not two, regardless of how many of the two documents mention it. This distinction is applied consistently in Â§5â€“Â§7 below.

### 2.1 Discrepancy identified between D1 and D2

D2 Â§3.1 records a "Designer Override" reading **"Round 1, Exchange 1 â€” PC attacks"** as the instruction that authorized its continuation. However, the state D2 Â§5 says it is continuing from is already **Round 2, Exchange 4 complete** (PC 585 / Troll 698, per D1 Â§3's own combat table). A literal "Round 1, Exchange 1" instruction does not match a mid-Round-2 resumption point. Neither D1 nor D2 explains this mismatch â€” D1 does not record receiving or requiring any Designer Override to begin, and D2 does not reconcile the override's stated round/exchange label against the state it demonstrably resumed from.

**Classification:** Documentation inconsistency between sources, not a mechanical contradiction. **Flagged, not resolved** â€” Tiwa may wish to clarify with OpenCode whether the override text was transcribed correctly or whether it originated in an out-of-band instruction not captured in either report.

---

## 3. Combat Outcome Comparison

| Parameter | D1 (Claude, partial) | D2 (Luna, Lineage A conclusion) | D3 (Grok, Lineage B) |
|---|---:|---:|---:|
| PC starting HP | 600 | 585 (carried from D1) | 600 |
| PC ending HP | 585 (abort, not terminal) | **0** | **0** |
| Troll starting HP | 705 | 698 (carried from D1) | 705 |
| Troll ending HP | 698 (abort, not terminal) | **569** | **412** |
| Rounds/exchanges | 2 rounds / 4 exchanges | ~11 further rounds (continuation) | 22 rounds |
| Terminal mechanism | N/A (explicit abort) | DEC-052 (HP=0) | DEC-052 (HP=0) |
| Result | Inconclusive | Ice Troll victory | Ice Troll victory |
| Real-time estimate | Not stated | Not stated | 45â€“60 minutes |

**Observation.** Both completed lineages independently terminated in Ice Troll victory via the identical DEC-052 mechanism (HP=0, no roll, forced incapacitation) â€” this is a genuine 2-of-2 independent confirmation that DEC-052 functions correctly as a combat-conclusion mechanism (Â§5.1).

**Observation.** The Troll's remaining HP differs substantially between lineages (569 vs. 412) despite identical starting stats. This is expected variance from (a) different dice sequences and (b) â€” critically â€” **different Inflict Injury/Active Defense scaffold formulas** (see Â§6), which is a confound, not pure randomness. The two outcomes are not directly comparable as "the same test twice."

---

## 4. Character/Opponent Construction â€” Consistency Check

| Parameter | D1 | D2 | D3 | Consistent? |
|---|---|---|---|---|
| PC attributes | 24Ã—50 | 24Ã—50 (carried) | 24Ã—50 | âœ… |
| PC derived HP/MP/PE/Speed/Regen | 600/600/150/150/100/100, MoveSpd 6 | carried, unchanged | 600/600/150/150/100/100, MoveSpd 6 | âœ… |
| Attack1/Defence1 Cap/Start | 50/25 | 50/25 (carried) | 50/25 | âœ… |
| Attack1/Defence1 attribute basis | Not specified in D1 | Not specified | bpp+bps / bsp+bss (D3 Â§3.1) | âš ï¸ Only D3 discloses which two tied attributes were selected â€” see Â§8, G-11 |
| Troll derived HP/MP/PE/Speed/Regen | 705/420/220/175/140/75, MoveSpd 7 | carried, unchanged | 705/420/220/175/140/75, MoveSpd 7 | âœ… |
| Icy Claws / Sharktoothed Maw Cap/Current | 67/67, 75/75 | carried | 67/67, 75/75 | âœ… |
| Regeneration/Regrowth/DR 2 (freezing-gated) | Inactive | Inactive (no `env:freezing`) | Inactive | âœ… 3/3 â€” never exercised in any lineage |

**Finding.** Base character/opponent construction is **fully consistent** across all three independently-authored records. This is a strong empirical confirmation that DEC-004 (derived statistics) and DEC-005 (Skill Cap/Starting Value) produce deterministic, reproducible results when three separate LLMs are given the same attribute inputs â€” a genuine 3-of-3 convergence with no scaffolding involved.

---

## 5. Systems Confirmed Working â€” Cross-Lineage Convergence

Systems below were exercised and functioned as specified (no invented rule, only invented *magnitudes* where the corpus is silent â€” see Â§6 for those). Confidence is graded by independent-lineage count per Â§2.

### 5.1 Confirmed in both Lineage A and Lineage B (2/2 independent confirmation â€” highest confidence)

| System | DEC ref | D1/D2 evidence | D3 evidence |
|---|---|---|---|
| d100 roll-under resolution | DEC-001 | Exercised throughout | Exercised throughout |
| 100-Fumble rule | DEC-001 | Exchange 3, PC rolls 100 | "100-Fumble... rules observed" Â§5.1 |
| Floor rounding | DEC-002 | Implicit throughout | Explicit Â§5.3 |
| Derived statistics (live) | DEC-004 | Confirmed Â§4 above | Confirmed Â§4 above |
| Skill Cap/Starting Value | DEC-005 | Confirmed Â§4 above | Confirmed Â§4 above |
| Core Test 9-step transaction | DEC-006 | Exercised every roll | Exercised every roll, explicit Â§5.3 |
| Cost=roll; Overflowâ†’HP; Overflow immutability | DEC-007/007.A | Exchange 3, 2 HP self-damage | "first Overflow events appeared... final rounds" Â§5.2 |
| Recovery, floor(Regen/2), clamped | DEC-008 | Implicit | Explicit Â§5.3 |
| Failure XP / Skill Roll Pool cascade | DEC-009/010 | Cited as exercised Â§3 | Explicit Â§5.3 |
| S-1 Opposed Contest (outcome matrix, Fail/Fail repeat) | DEC-013 | Exercised every exchange | Exercised every round |
| Effect auto-apply + Active Defense post-hoc mitigation (Model B) | DEC-027/048 | Exercised, incl. voluntary-decline mode | Exercised |
| HP=0 forced incapacitation | DEC-052 | N/A (combat not terminal in D1) | Confirmed â€” terminal mechanism |
| **DEC-052 as terminal mechanism specifically** | DEC-052 | Confirmed in D2 (Lineage A conclusion) | Confirmed in D3 |

**DEC-052 is therefore validated 2/2 independently as the correct, sufficient combat-termination mechanism** â€” the single strongest convergence finding in this comparison.

### 5.2 Confirmed only in Lineage A (D1+D2) â€” single independent confirmation

| System | DEC ref | Status in Lineage A | Status in D3 |
|---|---|---|---|
| Advanced Skill creation via failed Double | DEC-012 | Confirmed â€” multiple instances (D2 Â§8: Attack1 30â†’32, "Skill-(29)" Tier-3 creation) | **Not exercised** â€” "no qualifying failed Doubles occurred" (D3 Â§5.1) |
| S-2 Zero-Step Location Index generation | DEC-014 | Confirmed â€” Exchange 2 Wound applied to a rolled location | **Not exercised** â€” no Location-referencing Effect selected (D3 Â§4, Â§5.4) |
| DEC-041 Skill-Tier â‰¥2 gate / anatomical mapping (Location-Tier 1) | DEC-041 | Confirmed â€” Torso Tier-2 Wound | **Not exercised** |
| DEC-035.A/.B Wound creation, format, magnitude | DEC-035.A/.B | Confirmed â€” `Location Torso Tier-2 Wound âˆ’2 (bpe)` | **Not exercised** |
| DEC-079 Frightened Condition (mechanical, via won S-1 Effect) | DEC-079 | Confirmed â€” Tier-2 Frightened applied Exchange 4 | **Not selected** â€” "Ready but never selected" (D3 Â§4, SC-05) |
| DEC-031 Quality gating **above Base tier** | DEC-031 | Confirmed â€” Wound/Frightened both required gated-tier unlock | **Not exercised** â€” "Base-tier Inflict Injury was the only Effect selected" throughout all 22 rounds (D3 Â§5.1) |

**Finding â€” this is the most consequential single result in this report.** The entire Wound / Location-Index / gated-Effect pathway (DEC-014, DEC-035.A/.B, DEC-041, and DEC-031's above-Base gating) has been exercised in **exactly one independent lineage, not two**. D3's 22-round run â€” nearly six times the exchange count of D1's original session â€” never once selected a gated-tier Effect, relying exclusively on Base-tier Inflict Injury. This pathway has been flagged elsewhere in the corpus as critical to the Blood Man encounter (grapple/hold, darkness/vision, fear, tactical position). **A full playtest readiness assessment should not treat the Wound pathway as combat-validated on the strength of these three records; it has one confirmation, not three.**

### 5.3 Not exercised in any lineage (0/3)

| System | DEC ref | Note |
|---|---|---|
| S-5 Armor (Tags/Traits, Bypass, Sunder) | DEC-058â€“062 | Neither combatant possessed Armor Tags in any of the three records |
| Regeneration / Regrowth / freezing DR | DEC-088 (`env:freezing` gate) | No `env:freezing` Tag was ever declared present in any of the three records |
| Passive/aura Frightened trigger | â€” (no DEC exists) | Deliberately withheld in all three; see Â§7.3 |
| Second-Effect opposed roll (DEC-024/026, beyond the single free Effect) | DEC-024/026 | Not mentioned as attempted in any record |

---

## 6. Scaffold-Value Divergence â€” Primary Cross-Report Conflict

All three records independently invented placeholder numeric values for the same two unresolved magnitude gaps. **The values chosen are mutually incompatible formulas, not minor numeric variance**, and none of the three source reports flags this cross-report conflict against the others â€” it is identified here for the first time in this comparison.

### 6.1 Inflict Injury (Base-tier) magnitude

| Lineage | Formula used | Source |
|---|---|---|
| A (D1, carried into D2) | `Damage = Winner's Margin` (Skill âˆ’ Roll), applied on a straight Success/Failure win | D1 Â§4 row S-1; D2 Â§10.1 |
| B (D3) | **Flat 25 HP**, regardless of Margin | D3 Â§4, SC-01 |

### 6.2 Active Defense (S-6) mitigation amount

| Lineage | Formula used | Source |
|---|---|---|
| A (D1, carried into D2) | `Mitigation = Defender's own Margin` on a successful defense roll; `0` on failure | D1 Â§4 row S-2; D2 Â§10.2 |
| B (D3) | **Flat âˆ’20 HP**, or full cancellation if remaining Effect magnitude â‰¤ 20, on success; `0` on failure | D3 Â§4, SC-02 |

### 6.3 Why this matters

- **Damage scaling behavior differs fundamentally.** Margin-based damage scales with Skill level (a Skill-67 attacker beating a low roll can inflict a large Margin; a narrow win inflicts almost none). Flat-value damage is Skill-independent â€” a bare win and a dominant win inflict identical damage. These are not two implementations of one rule; they are two different combat-pacing philosophies.
- **This plausibly explains the outcome divergence in Â§3.** D3's flat-value system produced a stated "typical net damage per exchange of 5 HP after mitigation" (25 âˆ’ 20) â€” a slow, grinding attrition curve, consistent with 22 rounds to resolution. Lineage A's Margin-based system produced faster, more variable swings (e.g., a single Exchange-1 result of âˆ’7 HP against a Skill-25 PC, and a continuation that finished a 585-HP deficit in roughly 11 further rounds). The two combat-pacing outcomes are **not independently corroborating each other** â€” they are artifacts of two different, uncoordinated scaffold choices layered on top of the same Ruled corpus.
- **Neither formula has any register backing.** Both are explicitly non-canonical per their own source reports. Tiwa has not yet been asked to choose between them as a single cross-report question â€” each source report only flagged its own choice as an open item in isolation (CANDIDATE-01/02 in D1; Â§10.1/10.2 in D2; C-01/C-02 in D3).

**This divergence is elevated to Priority 1 in Â§9 â€” it blocks meaningful comparison of any future combat-duration or lethality data until Tiwa selects (or the corpus formally rules) one formula family.**

### 6.4 Other scaffold values â€” convergence check

| Gap | Lineage A value | Lineage B value | Convergent? |
|---|---|---|---|
| Ice Troll defensive skill (no dedicated Defence skill in v0.2 block) | Brawling (Tier-1) â€” D1 Â§4 row S-3, D2 Â§10.3 | "Defence / Brawling" â€” D3 Â§5.1 (uses same skill, though less explicitly flagged as a gap in D3's own candidate list, Â§7) | âœ… Same value chosen independently |
| Location-Tier-1 zone numeric ranges | 1â€“25 Legs / 26â€“50 Torso / 51â€“75 Arms / 76â€“100 Head â€” D1 Â§4 row S-5, D2 Â§10.4 | Not exercised â€” no Location Effect selected (Â§5.2 above) | Not independently tested by D3; cannot confirm convergence |
| Quality â†’ gated-tier unlock threshold | Quality â‰¥1 Base / Quality â‰¥10 gated â€” D1 Â§4 row S-4, D2 Â§10.5 | Not exercised â€” Base-tier only throughout | Not independently tested by D3; cannot confirm convergence |
| Turn order / initiative | Resolved via out-of-band Designer Override, not a self-invented scaffold (D2 Â§3.1) â€” **see discrepancy at Â§2.1** | Speed-based initiative, self-invented scaffold, no stop required (D3 Â§4, SC-04) | âš ï¸ Same underlying gap, handled by two different *mechanisms* (external override vs. self-invented rule) â€” see Â§7.2 |

**Where D3 never exercised a gap that Lineage A did resolve (zone ranges, Quality threshold), those Lineage-A values remain single-lineage-confirmed only, per Â§5.2's confidence standard.**

---

## 7. Governance / Process Discipline Comparison

### 7.1 Scaffold-logging discipline

All three reports comply with the standing rule (never assign a DEC, never claim Ruled/Locked status for an invented value, log every scaffold at point of invention). No violations found in any of the three.

One asymmetry: D1 and D2 both explicitly list "Ice Troll lacks a dedicated Active-Defense skill" as a numbered candidate item requiring Tiwa's attention (D1 CANDIDATE-06; D2 Â§10.3). **D3 uses the same substitution but does not carry it into its own Â§7 candidate-follow-up table** â€” it is used silently as a resolution detail rather than flagged as an open design question. This is a minor consistency gap in *candidate-tracking* discipline, not a corpus-invention violation.

### 7.2 Handling of the turn-order/initiative gap

This is the clearest process divergence between the two lineages:

- **Lineage A** treated "who acts first / next" as requiring an explicit out-of-band Designer Override rather than a self-invented scaffold â€” consistent with treating turn-order as a genuine GM-required judgment call rather than a numeric gap.
- **Lineage B (D3)** treated the same underlying gap (no Ruled initiative/turn-sequencing procedure exists â€” confirmed by both D2 Â§11.1 and D3 Â§7's "SC-04 surface" finding, since DEC-082 governs Time/Action *economy expression* only, not sequencing) as scaffold-eligible, and proceeded without stopping.

**Neither approach violated the prompt's own instructions** â€” the prompt authorized scaffolding for magnitude gaps and reserved GM-stops for "genuine subjective/narrative judgment calls," and turn order is arguably ambiguous between those categories. This ambiguity in the prompt itself is worth Tiwa's attention: **the prompt does not clearly state which category "no Ruled initiative procedure" belongs to**, and the two lineages resolved that ambiguity in opposite directions independently.

### 7.3 Handling of the passive Frightened trigger

Full 3/3 consensus: none of the three lineages invented a passive/aura Frightened trigger. D1 recorded it as a live GM-required stop (D1 Â§6, verbatim). D2 confirms the gap remains unresolved but does not reproduce a fresh stop since D2's continuation never re-encountered the triggering condition (D2 Â§11.2). D3 confirms it was "deliberately not invoked" and would have produced a mandatory GM-stop had it arisen (D3 Â§5.4, Â§6). **This is the cleanest example of correct, convergent discipline across all three records** â€” a genuine subsystem absence was recognized and respected identically by three independently-operating LLMs.

### 7.4 Defender-wins-opposed-attack interpretive gap

D1 (Â§5) and D2 (Â§11.3, same lineage) flagged this explicitly: when a defender wins an opposed S-1 attack contest, does the defender gain an Effect-declaration right, or does the attack simply fail? Both records in Lineage A applied the same conservative interpretation ("attack fails, no Effect for either side") and explicitly declined to treat it as a new rule.

**D3 does not mention this scenario at all.** It is not possible to determine from D3 whether the situation never arose in 22 rounds, or arose and was handled without being flagged. This is listed as an open verification item in Â§9, not treated as a contradiction (absence of evidence, not evidence of a differing interpretation).

---

## 8. Consolidated Candidate Gap List

The table below merges D1's CANDIDATE-01â€“09, D2's Â§10â€“11 items, and D3's C-01â€“04/SC-04â€“06/Â§7 items into a single de-duplicated list. **No item below has DEC status. All are Open pending Tiwa's ruling.**

| Consolidated ID | Subject | Cross-referenced source IDs | Independent lineages reporting it | Scaffold convergence |
|---|---|---|---|---|
| G-01 | Inflict Injury (Base-tier) numeric magnitude | D1 CANDIDATE-01; D2 Â§10.1; D3 C-01/SC-01 | 2/2 | **Diverges** â€” Margin-based (A) vs. flat 25 HP (B); see Â§6.1 |
| G-02 | Active Defense (S-6) numeric mitigation amount | D1 CANDIDATE-02; D2 Â§10.2; D3 C-02/SC-02 | 2/2 | **Diverges** â€” Defender's Margin (A) vs. flat âˆ’20 HP/cancel (B); see Â§6.2 |
| G-03 | S-3 Effect magnitudes generally, beyond Quality-scaling | D1 CANDIDATE-03; D3 C-03 | 2/2 (no fresh data from either) | No specific values proposed by either lineage |
| G-04 | Frightened Condition passive/aura trigger mechanic | D1 CANDIDATE-04; D2 Â§11.2; D3 C-04 | 3/3 | N/A â€” universally treated as GM-stop, not scaffolded (Â§7.3) |
| G-05 | Regeneration/Regrowth healing-magnitude vocabulary | D1 CANDIDATE-05; D2 (Troll traits inactive); D3 (inactive by disposition) | 3/3 non-exercise | Never tested in any lineage â€” remains fully open |
| G-06 | Ice Troll lacks a dedicated Active-Defense skill in the v0.2 block | D1 CANDIDATE-06; D2 Â§10.3; D3 (used, not separately flagged) | 2/3 flagged; 3/3 used the same substitute | Converges on Brawling as the substitute (Â§6.4) |
| G-07 | Quality â†’ gated-tier-Effect unlock numeric threshold | D1 CANDIDATE-07; D2 Â§10.5 | 1/2 (D3 never exercised gated tiers) | Single-lineage value only (Quality â‰¥1 Base / â‰¥10 gated) â€” not independently corroborated |
| G-08 | Location-Tier-1 coarse-zone numeric ranges | D1 CANDIDATE-08; D2 Â§10.4 | 1/2 (D3 never exercised) | Single-lineage value only â€” not independently corroborated |
| G-09 | Effect-declaration rights when a defender wins an opposed attack contest | D1 CANDIDATE-09; D2 Â§11.3 | 1/2 (D3 silent â€” see Â§7.4) | Single-lineage conservative interpretation only |
| G-10 (new in this comparison) | General combat action sequencing / initiative â€” no Ruled procedure exists | D2 Â§11.1; D3 SC-04/Â§7 "SC-04 surface" | 2/3 (D1 did not need to resolve it; handled via external override, not self-scaffold â€” Â§7.2) | **Diverges in kind**, not just value â€” see Â§7.2 |
| G-11 (new in this comparison) | Whether Attack1/Defence1's underlying attribute-pair selection (among tied Body attributes) is a fixed/reproducible construction detail or free per-execution choice | D3 Â§3.1 discloses `bpp+bps` / `bsp+bss`; D1/D2 do not disclose their selection | Cannot compare â€” D1/D2 never state which two attributes they used | Genuinely new observation from this comparison; not previously flagged by any source report |
| G-12 (new in this comparison) | Cross-lineage scaffold-formula conflict itself (Â§6.1â€“6.2) as a standalone tracking item | This report only | â€” | Not previously identified as a discrete open item by any of the three source reports |

---

## 9. Readiness Assessment for Full Playtest

Presented as a prioritized set of blocking vs. non-blocking items, per the advisory role â€” **options for Tiwa's consideration, not a recommendation of any single resolution.**

### 9.1 Priority 1 â€” blocks meaningful full-playtest data collection

| Item | Why it blocks | Consolidated ref |
|---|---|---|
| Inflict Injury magnitude AND Active Defense mitigation formula selection | Two mutually incompatible scaffold families are now in circulation (Margin-based vs. flat-value) with no register-level tie-breaker. Any full playtest run without a single chosen formula will produce combat-duration/lethality data that cannot be compared across sessions or referees. | G-01, G-02, G-12 |
| Turn-order / initiative procedure | No Ruled mechanism exists at all; the two lineages resolved this two different ways (external override vs. self-invented rule), and it is unclear from the prompt itself whether this class of gap should be scaffolded or GM-stopped. A full playtest run needs one procedure before combat can even begin without human intervention every session. | G-10 |

### 9.2 Priority 2 â€” should be closed before the *first* full playtest that includes location-based combat (i.e., any encounter where Wound/gated-Effects are expected, per the corpus's own flagging of this pathway as critical to the Blood Man encounter)

| Item | Consolidated ref |
|---|---|
| Location-Tier-1 zone numeric ranges (only single-lineage-tested) | G-08 |
| Quality â†’ gated-tier Effect unlock threshold (only single-lineage-tested) | G-07 |
| S-3 Effect magnitudes generally beyond Base-tier | G-03 |
| Defender-wins-opposed-attack Effect-declaration rights | G-09 |

### 9.3 Priority 3 â€” genuine subsystem absences, correctly un-scaffolded; require a design ruling, not a numeric patch

| Item | Consolidated ref |
|---|---|
| Passive/aura Frightened trigger mechanic | G-04 |
| Regeneration/Regrowth healing-magnitude vocabulary (still entirely untested â€” no lineage ever declared `env:freezing` present) | G-05 |

### 9.4 Non-blocking / informational only

| Item | Note |
|---|---|
| Ice Troll defensive-skill substitution (Brawling) | Converges 3/3 in practice; formalizing it in the v0.2 stat block (adding an explicit Defence skill) would remove the need for referee improvisation, but current behavior is consistent and low-risk. |
| Attack1/Defence1 attribute-pair disclosure | Only affects reproducibility of *this specific playtest scaffold*, not any Ruled system â€” since Attack1/Defence1 are themselves a prompt-level, non-register-backed exception (DEC-012 exception, carried in all three reports, Â§10 below). |

### 9.5 Validated and playtest-ready as-is

Per Â§5.1's 2/2 convergence: d100 core resolution, floor rounding, derived statistics, Skill Cap/Starting Value, the 9-step Core Test Transaction, Cost/Overflow/Overflow-immutability, Recovery, Failure XP/Skill Roll Pool cascade, S-1 Opposed Contest, Effect auto-apply + Active Defense post-hoc mitigation (mechanically, independent of the Â§6 magnitude dispute), and DEC-052 incapacitation. These require no further validation work before a full playtest.

---

## 10. Provenance of the DEC-012 Exception (carried forward unchanged, all three sources)

All three source reports carry the identical governing note, reproduced here for completeness since it governs every Attack1/Defence1 roll referenced throughout this comparison:

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack1, Defence1) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

---

## 11. What Was and Was Not Done by This Report

**Done:** Extracted and re-verified all three source records from the merged bundle file. Cross-referenced combat outcomes, character construction, systems exercised, scaffold values, and governance discipline. Identified one documentation inconsistency (Â§2.1) and one substantive unflagged scaffold-formula conflict (Â§6) not previously identified by any of the three source reports. Consolidated and de-duplicated all candidate gap items into a single tracked list (Â§8), adding three new items (G-10, G-11, G-12) surfaced only by this comparison. Produced a prioritized readiness assessment (Â§9) as options, not a ruling.

**Not done:** No DEC numbers assigned. No item in Â§8 or Â§9 resolved. No register, governance, canonical ruleset, or prompt file modified. No preference expressed between the Margin-based and flat-value scaffold families in Â§6 â€” that choice belongs to Tiwa. No analysis performed of the other ~27 documents present in the source bundle (Adventure Readiness Audits and System-by-System Comparison meta-documents) â€” those remain out of scope per this report's confirmed instructions.

**Recommended next step (procedural, not a design ruling):** Tiwa reviews Â§6 (scaffold-formula conflict) and Â§9.1 (Priority 1 blockers) first, since both bear directly on whether a full playtest can proceed with comparable data across sessions. G-01/G-02/G-10 are the minimum items requiring resolution before a full playtest is scheduled. OpenCode should repeat G-01 through G-12 back to Tiwa individually per standing reconfirmation-before-recording practice before any register entry is made.

---

*End of report.*

---

**Documentarian Verification (2026-09-04, opencode/big-pickle):**
- Factual claims verified against the three source execution reports and the decision register.
- Lineage structure, convergence/divergence table, and scaffold formula conflict accurately reported.
- No DEC numbers assigned. No rulings made. Classification preserved: advisory.
- **Assessor_llm updated** from empty to opencode/big-pickle; **last_modified_by_llm** updated to opencode/big-pickle.
