---
document:
  title: "Tiwas - Beyond the Vale of Madness - Multi-LLM Adaptation Reports - Compilation: Prioritized Checklist + Disagreement Register"
  version: "1.0"
  status: "NON-CANONICAL - advisory compilation. Synthesizes the 25 source reports; makes no rulings and confers no authority."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
---

# Tiwas - Beyond the Vale of Madness - Multi-LLM Adaptation Reports: Compilation

## Status and purpose

**Status**: NON-CANONICAL - advisory only. This document registers and synthesizes the positions of the 25 source LLM adaptation reports. It makes **no rulings**, promotes nothing, and changes no document status. Every item below carries exactly the authority (non-canonical advisory / Ruled-non-canonical / Open / Missing / Reserved) it had in its source report. Where reports disagree, both positions remain live and unresolved.

**Purpose**: One-stop view of what the 25 multi-LLM reports collectively say about Tiwas readiness for *Beyond the Vale of Madness*, so that downstream LLMs and Tiwa can see: (1) which development items are prioritized, by how many reports, (2) where the reports genuinely disagree, and (3) which findings are isolated narrow claims that would otherwise be dropped in a majority synthesis.

## Basis and method

- Compiled from the 25 reports in `investigations/tiwas-adapt-vale-of-madness-reports-1.md` (SHA-256 `2CED1D450C8C45A1986D970D9C1D9EA70C7FA02978CCBA1286D9769C7C7E6702`, repaired 2026-09-02).
- **Duplicate correction applied**: in the original merge the Copilot and Copilot 365 pairs were textually identical duplicate pairs (`copilot-1` == `copilot-2`; `copilot365-1` == `copilot365-2`). Tiwa supplied corrected versions; the four Copilot/Copilot 365 reports are now distinct. **Corroboration counts in this document therefore treat each of the 25 reports as one independent viewpoint** - no duplicate-pair discounting is needed.
- For report-by-report attribution (LLM + report number), see `investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`. Report cites below use the merged-file section names (e.g., `chatgpt-5-2-1.md`).
- Method: each report was read in full; per-report classifications were extracted for 14 named systems; priorities and isolated claims were collected verbatim-near. Corroboration figures are "X of 25" by named report, based on that extraction.

### Source-grounding caveats (weight evidence accordingly)

| Report | Source handling |
|---|---|
| `Tiwas-Adventure-Readiness-Audit.md` (glm) | No direct PDF access; mechanical requirements inferred from generic GURPS patterns ("Without direct PDF access..."). Least grounded in actual adventure text. |
| `mimo-2-5-2.md` | Adventure text OCR-scanned with transcription errors; **truncated mid-sentence in the Blood Man stat block**; pregens and tactical map not included. |
| `copilot-2_1.md` | Supplied extract truncated/garbled ("BeSe iy oes2a..."); inventory largely inferred and flagged. |
| `chatgpt-5-2-1.md` | Parsed pages 1-12 plus 16-19 (pregens). |
| All others | Full PDF or full provided adventure text. |

---

## Part 1 - Prioritized checklist (4 tiers)

Attribution format: **item** - corroboration (N of 25). The parenthesized reports are those that raise the item as a priority, blocker, dependency, or required ruling. Items in Tier 1 are predominantly "content authoring" tasks; items in Tier 2 are the ones where reports genuinely disagree on whether a gap exists.

### Tier 1 - unblock a full-fidelity run, near-unanimous corroboration

1. **S-3 gated Effect menu contents** (Position, Condition, Equipment, Defense, Location tiers) - 24 of 25. Named by: `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `copilot-1_1`, `copilot-2`, `copilot365-1_1`, `copilot365-2_1`, `deepseek-1`, `facebai-laguna-s-2-1-1`, `gemini-1`, `gemini-2`, `grok-1`, `kimi-1`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1` (via combat broadly), `perplexity-1`, `perplexity-2`, `recallAI-1`, `glm`. The single report that does **not** name S-3 contents as a blocker is `grok-2`. Most reports treat the menu *structure* as Ruled and only the *contents* as missing (range: "CRITICAL BLOCKER" in `gemini-2` down to "moderate gap" in `copilot365-1_1`).

2. **S-12 creature/NPC stat blocks + template method** (Ice Troll, Blood Man) - 23-24 of 25. Named by: `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `copilot-1_1`, `copilot-2`, `copilot365-1_1`, `copilot365-2_1`, `deepseek-1`, `gemini-1`, `gemini-2`, `grok-1`, `grok-2`, `kimi-1`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1`, `perplexity-1`, `perplexity-2`, `recallAI-1`, `claude5-1`, `glm`. Not discussed by `facebai-laguna-s-2-1-1`. P0 in `grok-1`, `grok-2`, `metaai-1`, `metaai-2`; Critical in `deepseek-1`, `glm`. This is the single most-cited blocker.

3. **Equipment/weapon stats + item Tags + encumbrance** - 20-22 of 25. Named by: `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `copilot365-1_1`, `copilot365-2_1`, `deepseek-1`, `facebai-laguna-s-2-1-1`, `grok-1`, `grok-2`, `kimi-1`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1`, `perplexity-1`, `perplexity-2`, `recallAI-1`, `claude5-1`, `glm` (~). Not treated as a blocker by `gemini-2` (narrative inventory, "non-blocking"). P0 in `metaai-1`; Priority 1 in `mimo-2-5-1`, `mimo-2-5-2`, `grok-1`, `grok-2`, `perplexity-1` (weapons/equipment model). `eliciting` weapon Tags (`Reach`, `Heavy`, etc.) is the concrete ask.

4. **Combat procedure / consequence-chain integration (incl. time/action economy)** - 10-12 of 25. Named by: `chatgpt-5-6-1` (Priority 1 "Combat Integration", Priority 2 "Time / Action Economy"), `chatgpt-5-6-2` (Priority 1 combat stack, Priority 5 tactical action economy), `perplexity-1` (Priority 1 "core combat procedure" incl. initiative/turn order), `perplexity-2` (Priority 1 combat consequence chain), `gemini-2`, `grok-1` (tactical grid - optional), `mimo-2-5-1`, `mimo-2-5-2`, `metaai-1`, `claude5-1`. Not a distinct item for reports that treat the S-1..S-7 chain as effectively complete (`recallAI-1`, `claude5-1`, `copilot-1_1`, `copilot365-1_1`).

### Tier 2 - real gaps or policy decisions, where reports genuinely disagree

5. **Wound consequences implementation (OPEN-007)** - damage magnitudes (-1/-5/-30/-80/-100), healing-cost scaling - 16-18 of 25. Named by: `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `copilot-1_1`, `copilot-2`, `copilot365-1_1`, `copilot365-2_1`, `grok-1`, `grok-2`, `kimi-1`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `perplexity-1`, `perplexity-2`, `glm`. Not discussed by `mistral-1`, `facebai-laguna-s-2-1-1`; treated as "architecture ready, zone numbers not locked" by `claude5-1` and as "Playtestable Now (with magnitude scaling remaining)" by `deepseek-1`. Blocking significance ranges from High (`metaai-1`, `metaai-2`) to Minor for this adventure (`mimo-2-5-2`: "the adventure primarily uses HP tracking").

6. **Fear / fright / morale condition system** - 19-21 of 25 raise it; categorization splits hard (see D3). Named as missing or design-stage by: `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2` (test available, consequence model not), `copilot-2` (sanity), `copilot365-2_1`, `facebai-laguna-s-2-1-1` (Warding/Conditions), `gemini-1`, `gemini-2`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `perplexity-1` (persistent mental conditions), `perplexity-2`, `recallAI-1` (Adaptation Mapping Required), `claude5-1` ("load-bearing for tone, not incidental"). `grok-1` (binary playtestable), `grok-2` (substitution), `copilot365-1_1` (Partially Playtestable), `mistral-1` (Playtestable Now via Will). Not classified by `kimi-1`, `glm`, `copilot-1_1`.

7. **Magic scope decision** - 19-21 of 25 name magic; the split is "missing subsystem" vs "excludable for alpha" (see D4). Missing/required: `chatgpt-5-2-1` (optional), `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2` (blocker if pyromancer used), `copilot-2`, `copilot365-2_1`, `deepseek-1` (low, avoidable), `gemini-1`, `gemini-2`, `grok-1` (low), `grok-2`, `kimi-1` (High if dwarf... wizard pregen avoided), `metaai-1`, `metaai-2`, `mimo-2-5-2`, `mistral-1`, `perplexity-1`, `perplexity-2`, `recallAI-1` (medium), `claude5-1` (not discussed), `glm` (Critical, Priority 1). Not required / excluded: `copilot365-1_1` ("NOT REQUIRED"), `perplexity-1`, `perplexity-2` (exclude optional wizard from minimum readiness). Not discussed: `copilot-1_1`, `mimo-2-5-1`. The concrete decision shape is: exclude the Enfys/mage pregen from alpha, or rule a minimal non-canonical fire-only stub.

8. **Continuous cold / environmental hazard content layer** (hypothermia/exhaustion rates, darkness/light conditions) - raised by 14-16 of 25 as a gap; ~9-10 treat it as already playtestable (see D7). Gap: `chatgpt-5-2-1` (Priority 5 hazard procedure; darkness Open), `chatgpt-5-5-high-1` (Priority 4), `chatgpt-5-6-1`, `copilot365-2_1`, `facebai-laguna-s-2-1-1` (light/timer), `grok-1` (P0 continuous cold model; P1 darkness), `grok-2` (P0), `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1`, `perplexity-2` (climbing/cold). Playtestable already: `copilot-1_1`, `copilot-2`, `copilot365-1_1`, `gemini-1`, `gemini-2`, `recallAI-1`, `glm`, `deepseek-1` (adaptation/optional).

### Tier 3 - mapping / content policy items, medium corroboration

9. **Difficulty / modifier mapping policy** (named grades vs the adventure's raw +3 / -5 / DX-5 modifiers) - 6-8 of 25. `perplexity-1`, `perplexity-2` (both: no universal modifier policy), `chatgpt-5-2-1` (values not in excerpt), `chatgpt-5-5-high-1` (Priority 5), `claude5-1` (M2 "+3" mapping unresolved), `metaai-2`, `grok-1`.

10. **Skill-default / untrained-fallback rule** - 4-5 of 25, but two of them put it at the top: `claude5-1` calls it the **single highest priority** exposed by the benchmark ("no existing investigation touches this at all"); `kimi-1` calls it an immediate pre-first-session ruling (8 untrained calls; notes a Skill-0 test on d100 "can never succeed" because roll <= 0 is impossible). Also raised by `chatgpt-5-5-high-1` (unskilled defaults), `metaai-1` (flagged guess), `metaai-2`.

11. **GURPS FP -> Tiwas Physical Energy conversion policy** (fixed costs vs Cost=Roll; zero-energy consequences) - 7 of 25. `perplexity-1` (P3), `perplexity-2` (P2), `recallAI-1` (assumption), `chatgpt-5-2-1`, `deepseek-1`, `metaai-1`, `metaai-2`. `mimo-2-5-2` adds the resource-contention risk (see Part 3).

12. **First Aid / immediate HP restoration mapping onto S-11** (1d-3 restoration vs S-11 Margin-based healing) - 5-7 of 25. `chatgpt-5-2-1`, `chatgpt-5-5-high-1` (Priority 6 healing), `metaai-1`, `metaai-2` (substitution), `kimi-1` (playtestable, blocking Low), `copilot-1_1`, `chatgpt-5-6-2` ("cannot simply declare the GURPS First Aid rule equivalent to S-11").

13. **GURPS -> Tiwas skill-list mapping policy** (skill names to Tier-1 lineages) - 5-6 of 25. `chatgpt-5-2-1` (no canonical skill list), `chatgpt-5-5-high-1`, `glm` (Appendix B conversion guide), `facebai-laguna-s-2-1-1` (optional P4), `metaai-2`, `kimi-1` (lineage assumptions flagged).

14. **Loot / treasure / currency / valuation procedure** - 7-8 of 25 as a gap; several others treat it as adventure content only. `deepseek-1` is the outlier - **Critical**, Priority 2 ("without an economy, the conclusion #60 cannot be resolved"; full treasure-valuation table). Also: `copilot-1_1` (mapping guess), `copilot-2`, `chatgpt-5-6-1` (currency Missing), `grok-1` (equipment economy Missing), `metaai-1` (treasure economy Missing), `glm`, `copilot365-2_1`. Adventure-content-only: `kimi-1`, `metaai-2`, `mistral-1`.

15. **Armor Tag starter vocabulary + conditional/gated Tags** (low-temperature DR, regeneration, specialities) - 6-8 of 25. `metaai-1` (P1), `metaai-2` (P1), `mimo-2-5-2`, `recallAI-1` (P3), `claude5-1` (P4 weapon Tags), `facebai-laguna-s-2-1-1`, `kimi-1` (generalized Trait/Tag framework), `grok-2` (temperature-gated regeneration).

16. **Time / action economy and tactical movement** (hex grid optional vs theater-of-mind) - 5-6 of 25. `chatgpt-5-6-1` (P2), `chatgpt-5-6-2` (P5), `perplexity-1` (P1), `mimo-2-5-1`, `mimo-2-5-2` (ToTM guidelines), `grok-1` (grid optional). `copilot365-1_1` explicitly dismisses it: "Assessment: OPTIONAL... Ignore entirely - No blocker."

### Tier 4 - narrow or isolated items (1-4 reports), kept visible per source-reports' own convention

17. **NPC morale / retreat-behaviour framework** (Ice Troll fight-to-death vs retreat) - 3-4 of 25. `mimo-2-5-1` (P5), `mimo-2-5-2` (P7), `metaai-1`, `chatgpt-5-6-1`.
18. **Damage-type differentiation & damage-magnitude formula** (crushing/cutting/corrosive; dice-to-HP conversion) - 4-5 of 25. `kimi-1` (Priority 1 ruling), `perplexity-1` (P2), `mimo-2-5-1`, `glm`, `chatgpt-5-2-1`.
19. **Grapple / ongoing-damage (Blood Seep) concrete Effects** - 4 of 25. `chatgpt-5-2-1`, `chatgpt-5-6-1` (P4), `chatgpt-5-6-2` (P4), `metaai-2`.
20. **Trait / Advantage framework beyond armor** (Fearlessness, Homogeneous, Night Vision, Regeneration) - 4-5 of 25. `mimo-2-5-2`, `chatgpt-5-6-1`, `glm` (special abilities), `kimi-1`, `metaai-2`.
21. **S-9/S-10 single-vs-extended task mapping policy** - 3 of 25. `perplexity-2` (design-stage unless treated as single-roll), `grok-1`/`grok-2` (continuous-attrition template question), `chatgpt-5-2-1` (adventure content only).
22. **Resource-contention feedback-loop risk** (Physical Energy used for BOTH skill costs and environmental depletion) - 1 of 25. `mimo-2-5-2` only.
23. **Hit-location / anatomy zone-number lock** (S-4 zone numbers not locked; OPEN-003 location names unassigned) - 2 of 25. `claude5-1`, `gemini-2`.
24. **A repeatable "development acceptance test" framing** (reuse this adventure as a fixed readiness benchmark for Tiwas) - 2-3 of 25. `chatgpt-5-6-1`, `grok-1`, `grok-2`.

---

## Part 2 - Disagreement register

Items where reports actively conflict (classification, not just emphasis). Both/all positions remain live; nothing here resolves them.

**D1 - Is the combat pipeline itself Playtestable Now or Design-Stage?** (the largest conflict)
- Playtestable-now-leaning (6): `recallAI-1` ("Combat: YES, Low blocking"), `claude5-1` (S-1..S-7 chain "genuinely playtest-ready"), `copilot-1_1` (basic combat playtestable), `copilot365-1_1` (combat "SUFFICIENT / Ready"), `gemini-1` (combat resolution Playtestable Now), `deepseek-1` (Playtestable Now "with stat blocks").
- Design-stage-leaning (16-17): `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `copilot-2`, `copilot365-2_1`, `gemini-2`, `grok-1`, `grok-2`, `kimi-1`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1`, `perplexity-1`, `perplexity-2`.
- **Consequence**: decides whether "author two monsters" is sufficient to unblock combat testing, or whether the combat consequence chain itself must be integrated/verified first. `grok-2`'s path: S-3 is NOT the blocker, environmental attrition + creatures + equipment are.

**D2 - S-12 taxonomy: Missing Subsystem vs content-authoring task under ruled architecture**
- Content-authoring task (no new mechanics): `claude5-1` ("content task under the already-Ruled S-12 process"), `kimi-1` ("Adventure Content Only... Blocking: None. Conversion is content work"), `copilot-1_1` ("does not require new mechanics"), `grok-1` ("content authoring under existing DEC-076 framework"), `copilot-2`, `deepseek-1` ("stat blocks are not system mechanics per se, but content").
- Missing Subsystem (system gap): `mistral-1` ("No equivalent"), `mimo-2-5-1`, `mimo-2-5-2`, `metaai-1`, `metaai-2` ("Missing Subsystem - content track"), `recallAI-1`, `grok-2`, `glm`.
- **Consequence**: scopes the resulting dev ticket - "author N stat blocks" vs "design creature system + author N stat blocks".

**D3 - Fear classification: Missing Subsystem vs playtestable via existing mental tests**
- Missing / design-stage (majority): `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `copilot-2`, `copilot365-2_1`, `facebai-laguna-s-2-1-1`, `gemini-1`, `gemini-2`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `perplexity-1` (persistent), `perplexity-2` (persistent), `recallAI-1` (adaptation), `copilot365-1_1` (partial), `claude5-1`.
- Playtestable / substitution (minority): `mistral-1` (Will test Playtestable Now), `grok-1` (binary Playtestable Now), `grok-2` (substitution), `perplexity-1/-2` (basic Will tests), `copilot365-1_1` (generic mental tests).

**D4 - Magic: Missing/Required vs Not required / excludable**
- Required or Missing (must decide): `chatgpt-5-6-2` (blocker if pyromancer used; "adventure does not merely mention magic"), `copilot365-2_1`, `glm` (Priority 1 Critical), `kimi-1` (High), `mistral-1`, `metaai-1`, `metaai-2` (decision doc: exclude OR fire-only stub).
- Not required / excludable: `copilot365-1_1` ("Adventure itself does not require magic to function"; "NOT REQUIRED for readiness"), `deepseek-1` (low, optional pregen), `chatgpt-5-2-1` (optional), `perplexity-1`, `perplexity-2` (exclude wizard from minimum readiness).
- **Consequence**: whether a magic ruling is needed before first playtest or only for full benchmark parity.

**D5 - Overall verdict: playtestable now vs restricted / not-yet**
- Yes today: `recallAI-1` ("playtest this adventure in Tiwas today", "System-Ready but Content-Empty"), `copilot365-1_1` ("75-85% ready", "can be run today"), `copilot-1_1` ("mechanically playtestable now" with scaffolding).
- Yes for restricted/non-combat routes only: `perplexity-1`, `perplexity-2` (exploration-and-resolution playtest), `kimi-1` (~15% degraded no-combat path), `glm` (90% shortest path), `metaai-1`, `metaai-2` (martial path ~70% with GM block).
- No (full adventure): `chatgpt-5-2-1`, `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `chatgpt-5-6-2`, `gemini-1`, `gemini-2`, `grok-1`, `grok-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1`, `facebai-laguna-s-2-1-1`, `copilot365-2_1`, `deepseek-1` (partial), `copilot-2`, `claude5-1` (not end-to-end without two gaps).
- **Consequence**: whether an alpha session can be scheduled now (minority yes) or only after Tier 1 items complete (majority).

**D6 - Economy/treasure: Critical blocker vs adventure content**
- Critical: `deepseek-1` only (Priority 2, "conclusion #60 cannot be resolved without an economy").
- Real but low/adaptation: `copilot-1_1`, `copilot-2`, `chatgpt-5-6-1`, `grok-1`, `metaai-1`, `glm`, `copilot365-2_1`.
- Adventure content / non-blocking: `kimi-1`, `metaai-2`, `mistral-1`, `perplexity-1`, `perplexity-2`.

**D7 - Continuous cold / environmental attrition: P0 blocker vs already covered**
- P0 blocker: `grok-1`, `grok-2` ("the adventure's opening risk economy cannot be reproduced" without a continuous cold model).
- Design-stage or missing: `chatgpt-5-5-high-1`, `chatgpt-5-6-1`, `copilot365-2_1`, `facebai-laguna-s-2-1-1`, `metaai-1`, `metaai-2`, `mimo-2-5-1`, `mimo-2-5-2`, `mistral-1`, `perplexity-2`, `chatgpt-5-2-1`.
- Already playtestable: `copilot-1_1`, `copilot-2`, `copilot365-1_1`, `gemini-1`, `gemini-2`, `recallAI-1`, `glm`, `perplexity-1` (via DEC-037).

**D8 - S-6 Active Defense: Playtestable Now vs Design-Stage**
- Playtestable Now (architecture Ruled): `recallAI-1`, `copilot-1_1`, `copilot-2`, `copilot365-1_1`, `copilot365-2_1`, `metaai-1`, `metaai-2`, `grok-1`, `grok-2`, `gemini-1`, `gemini-2`, `glm`.
- Design-Stage / unspecified (which skill or attribute the defender rolls): `chatgpt-5-2-1` (mitigation semantics undefined), `chatgpt-5-5-high-1`, `chatgpt-5-6-2` (major blocker), `kimi-1` ("which skill or attribute the defender rolls is not specified"), `perplexity-1`, `perplexity-2` ("complete defence procedure not demonstrated"), `mimo-2-5-1`, `mimo-2-5-2`.

---

## Part 3 - Isolated / narrow findings kept visible

Per the source reports' own §5 convention (isolated 1-2-report findings stay visible rather than being dropped from a majority synthesis):

- **Skill-default rule as top priority** - named by exactly two reports, `claude5-1` (highest priority) and `kimi-1` (immediate ruling), plus `chatgpt-5-5-high-1` (defaults). Includes `kimi-1`'s mechanical observation that a Skill-0 test on d100 (range 1-100) "can never succeed" because success requires a roll <= 0, which no roll in the range can satisfy.
- **`mimo-2-5-2`'s resource-contention risk** (unique): if Physical Energy funds both Body-skill Costs (DEC-007) and environmental cold depletion, an unintended feedback loop could make skill use impossible under environmental stress.
- **Numeric readiness divergence** (unordered, all non-authoritative): 57.9% (`deepseek-1`, 11/19); 52% -> ~70% martial -> ~85% potential (`metaai-2`); ~42/9/15/33% (`metaai-1`); ~38% (`grok-1`), ~40% (`grok-2`); 75-85% + "8/10" (`copilot365-1_1`); ~15% overall / ~60% if combat-magic avoided (`mistral-1`); 40% overall / 90% shortest path (`glm`); ~15% minimum no-combat path (`kimi-1`). These are incompatible with each other and should not be averaged.
- **`metaai-2`'s framing**: "the adventure proves that system architecture is not the blocker; content authoring is" - echoed as a theme by `claude5-1`, `recallAI-1`, `grok-1`, `deepseek-1`.
- **`grok-1`/`grok-2` claim a level of internal coherence**: all identified gaps are "additive subsystems, not contradictions"; no Core Invariant conflict. The closest thing to a consensus claim among the reports (`claude5-1` §1 and several others also note no fundamental engine failure).
- **`copilot365-1_1`'s quality-of-life claims**: tactical grid "Ignore entirely"; magic "NOT REQUIRED".
- **`claude5-1`'s S-3/S-4 nuance**: S-3 and S-4 considered Ready at *architecture* level with only contents/zone-numbers not locked - the strongest "system layer fine, content layer not" position.
- **Quality anomaly (flag only, not design content)**: `kimi-1` states "Twenty-two GURPS traits" in one place and "34 traits" in another for the same two pregens; `mimo-2-5-1` contains a repeated "Tihas" typo; `copilot-2_1` worked from the garbled/truncated extract.

---

## Closing note

This compilation is a registration aid. It does not choose between D1-D8 positions, does not set any item's status, and does not promote anything. Where reports disagree, all positions remain live and require Tiwa's decision through the repository's formal governance process before any of them acquires documentary weight.