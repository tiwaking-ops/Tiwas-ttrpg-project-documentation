---
document:
  title: "Tiwas TTRPG Project — LLM Usage Inventory"
  version: "1.0"
  status: "Advisory / informational — inventory record only. Lists every LLM recorded in repository evidence, with recorded name, recorded version, first recorded date, and an evidence pointer. Makes no rulings, assigns no DEC numbers, and confers no authority."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
---

# Tiwas TTRPG Project — LLM Usage Inventory

**Purpose.** Read-only, strictly informational register of every LLM that repository
evidence records as having been used in this project (authored material, assessed/stored
passes, playtest executions, arena test runs, verification/red-team work). This inventory
establishes no canonical status, makes no rulings, and changes nothing's authority.

## Method and caveats

1. **Identity = recorded `(name, version)`.** Rows reflect exactly what repository evidence
   records. Equivalent models recorded under different labels are **not** merged; likely
   aliases are flagged in the notes column (e.g. ChatGPT 5.6 vs GPT-5.6 Luna;
   Claude 5 Sonnet vs Claude Sonnet 5).
2. **First recorded date, not first used.** Exact first-use dates are not establishable
   from repository evidence in most cases. This report records the **first date an
   attribution appears in an unambiguously dated repository artifact** (filename with
   `YYYY-MM-DD`, frontmatter `created_date`, or dated content). Earlier usage may predate
   repository evidence.
3. **Placeholder/template identities excluded:** `...`, `[Your Model Name]`,
   `__REPLACE_WITH_YOUR_ACTUAL_MODEL_NAME__`, `<executing LLM name>`, `<model>`,
   and empty/`not established` version strings standing in for unused template fields.
4. **Unverified and self-reported identities are flagged**, never laundered through
   inference (per `governance/provenance.md`).
5. **Primary evidence sources:** frontmatter `author_llm` / `assessor_llm` /
   `last_modified_by_llm` blocks; `investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`
   (the 25-report BTVM attribution index, attributions confirmed by Tiwa 2026-09-02);
   `collated_llm_s3_analysis.md` (S-3 multi-LLM collation); `_consolidation/decision-register.md`
   (advisory annotation/storage records); the five arena batch session exports
   `investigations/multi-llm-test*.json` (recorded `modelID` / `providerID`).

## Inventory (43 distinct recorded identities)

| # | Recorded LLM identity | Recorded version | First recorded | Earliest evidence | Role evidence |
|---|---|---|---|---|---|
| 1 | Claude Sonnet 5 (also recorded as "Claude 5 Sonnet / claude sonnet-5") | claude-sonnet-5 | 2026-08-29 | `governance/provenance.md` (created 2026-08-29); `_consolidation/` governance docs | Core consolidation author/assessor; S-2/S-3/S-4 design sessions; BTVM 25-set report #24 (self-identified in its own front matter as `claude sonnet-5`); creature-template proposals 2026-09-12/13; playtest executions (mirror 2026-09-11, Bargle 2026-09-13); runner-packet reports (v0.2 2026-09-14) |
| 2 | opencode | big-pickle | 2026-08-29 | `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`; `sources/incoming/tiwas-s3-documentarian-handoff-report-2026-08-29.md`; `audits/` (`last_modified_by_llm`) | Project documentarian/steward; register annotations; storage/assessment of advisory material across the whole period; red-team verification of the G5 fusion 2026-09-19 |
| 3 | nemotron-3-super-120b-a12b:free | unknown | 2026-08-29 | `audits/INDEPENDENT-ASSESSMENT-2026-08-29.md` (created 2026-08-29; human-approved 2026-08-31) | Independent second-model assessment of the documentation consolidation (appended as independent assessor to governance docs 2026-08-31) |
| 4 | Model-A (Inkling-Reasoning v3) | identity / underlying model not established | 2026-01-23 | `investigations/llm-quality-s3-comparison-2026-01-23.md` (report timestamp 2026-01-23 11:45 UTC) | S-3 single-Effect outcome-resolution evaluation report (masked identity); merged into `collated_llm_s3_analysis.md` |
| 5 | Model-B (Cognitive-Gear v2) | identity / underlying model not established | 2026-01-23 | `investigations/llm-quality-s3-comparison-2026-01-23.md` (2026-01-23 11:50 UTC) | S-3 evaluation report (masked identity) |
| 6 | Model-C (Strategic-Forge v4) | identity / underlying model not established | 2026-01-23 | `investigations/llm-quality-s3-comparison-2026-01-23.md` (2026-01-23 11:55 UTC) | S-3 evaluation report (masked identity) |
| 7 | ChatGPT-5.4 Nano | (as recorded) | 2026-08-30 | `collated_llm_s3_analysis.md`; `investigations/llm-quality-s3-reports-2026-08-30.md` | S-3 meta-analysis participant (Quality gates eligible Effects) |
| 8 | ChatGPT | version not established | 2026-08-30 | `sources/incoming/ChatGPT-DONE Tiwas Location Index Analysis-20260830-share.md`; `sources/incoming/S2-Non-Attack-Location-Index-Source-ChatGPT-critique.md` | S-2 location-index analysis and critique |
| 9 | DeepSeek-V4-Flash-0731 | (as recorded) | 2026-08-30 | `collated_llm_s3_analysis.md` | S-3 meta-analysis participant (Quality scales potency) |
| 10 | DeepSeek | version not established | 2026-08-30 | `investigations/deepseek-harness-s4-wound-severity-and-s2-nonattack-reopening-RAW-2026-08-30.md` | S-4 wound-severity / S-2 non-attack reopening investigation (harnessed session) |
| 11 | Gemini 1.5 Pro (NZST) | (as recorded) | 2026-08-30 | `collated_llm_s3_analysis.md` | S-3 meta-analysis participant (Quality gates eligible Effects) |
| 12 | Gemini 1.5 Pro (UTC) | (as recorded) | 2026-08-30 | `collated_llm_s3_analysis.md` | S-3 meta-analysis participant (Quality gates eligible Effects) |
| 13 | Gemini | version not established | 2026-08-30 | `investigations/claude response to gemini-s4-chat2 - designer gaps and assessment-2026-08-30.md` | S-4 chat-2 responses to Claude's critique (reliability concern: fabricated citations flagged) |
| 14 | Meta AI — Muse Spark 1.1 | (as recorded; report filenames `metaai-1` / `metaai-2`) | 2026-08-30 | `collated_llm_s3_analysis.md`; BTVM 25-set reports #16–#17 | S-3 meta-analysis participant (Quality scales potency); BTVM adaptation reports 1 and 2 (2026-09-01) |
| 15 | Mistral Medium 3.5 | (as recorded) | 2026-08-30 | `collated_llm_s3_analysis.md` | S-3 meta-analysis participant (Quality scales potency) |
| 16 | Qwen3.7 | Qwen3.7 | 2026-08-30 | `collated_llm_s3_analysis.md` | S-3 meta-analysis participant (Quality gates eligible Effects); OpenChamber integration advisory `Qwen_markdown_20260918_iqidkhvja.md` (2026-09-18) |
| 17 | Grok 4.5 | grok 4.5 / grok-4.5 | 2026-08-30 | `sources/incoming/Grok-DONE ruled2 Designer Rules for Non-Attack Hazards-20260830-share.md`; `sources/incoming/S2-Non-Attack-Location-Index-Source-Architect-Assessment-grok.md`; `TTTRPG-grok4-5-syn1.md` | S-2 non-attack hazard design work; playtest executions (mirror 2026-09-11, Your First Adventure 2026-09-14, Bargle 2026-09-13, playtest-1) |
| 18 | ChatGPT 5.2 | (as recorded) | 2026-09-01 | BTVM 25-set report #1 (`btvmadness-adapt-report-chatgpt-5-2-1.md`) | BTVM adaptation report 1 |
| 19 | ChatGPT 5.5-high | (as recorded) | 2026-09-01 | BTVM 25-set report #2 | BTVM adaptation report 1 |
| 20 | ChatGPT 5.6 | (as recorded) | 2026-09-01 | BTVM 25-set reports #3–#4 | BTVM adaptation reports 1 and 2 |
| 21 | Copilot | version not recorded in repository evidence | 2026-09-01 | BTVM 25-set reports #5–#6 (`btvmadness-adapt-report-copilot-1_1.md`, `-2_1.md`) | BTVM adaptation reports 1 and 2 (corrected `_1` files stored 2026-09-02); runner-packet execution reports v0.2 (2026-09-14); unified-state-architecture multi-LLM consolidation 2026-09-06 |
| 22 | Copilot 365 | version not recorded in repository evidence | 2026-09-01 | BTVM 25-set reports #7–#8 (`btvmadness-adapt-report-copilot365-1_1.md`, `-2_1.md`) | BTVM adaptation reports 1 and 2 |
| 23 | DeepSeek-V3 | (as recorded) | 2026-09-01 | BTVM 25-set report #9 | BTVM adaptation report 1 |
| 24 | Laguna S 2.1 | facebai-laguna-s-2-1 | 2026-09-01 | BTVM 25-set report #10 (`btvmadness-adapt-report-facebai-laguna-s-2-1-1.md`) | BTVM adaptation report 1 |
| 25 | Gemini 3.6 Flash | (as recorded) | 2026-09-01 | BTVM 25-set reports #11–#12 | BTVM adaptation reports 1 and 2 |
| 26 | Grok 4.6 | (as recorded) | 2026-09-01 | BTVM 25-set reports #13–#14 | BTVM adaptation reports 1 and 2 |
| 27 | Kimi K3 | (as recorded) | 2026-09-01 | BTVM 25-set report #15 | BTVM adaptation report 1 |
| 28 | Mimo 2.5 | (as recorded) | 2026-09-01 | BTVM 25-set reports #18–#19 | BTVM adaptation reports 1 and 2; `.mimocode/` harness directory present in repo |
| 29 | Mistral | version not recorded in repository evidence | 2026-09-01 | BTVM 25-set report #20 | BTVM adaptation report 1 |
| 30 | Perplexity | version not recorded in repository evidence | 2026-09-01 | BTVM 25-set reports #21–#22 | BTVM adaptation reports 1 and 2; creature-conversion framework playtest `tiwas-perplexity-creature-conversion-framework-playtest-2026-09-03.md`; DEC-080 tags-vocabulary decision record 2026-09-03 |
| 31 | RecallAI | version not recorded in repository evidence | 2026-09-01 | BTVM 25-set report #23 | BTVM adaptation report 1 (only) |
| 32 | glm-4.5-air | (as recorded) | 2026-09-01 | BTVM 25-set report #25 (`Tiwas-Adventure-Readiness-Audit.md`, positional attribution from Tiwa's list) | BTVM adaptation report 1 |
| 33 | Arena.ai Agent Mode | unknown / not established (self-reported; platform exposes no non-forgeable model-version metadata) | 2026-09-02 | `investigations/tiwas-adapt-vale-of-madness-development-planning-arena-2026-09-02.md`; `investigations/tiwas-adapt-vale-of-madness-reports-compiled1-arena-2026-09-02.md` | 25-LLM meta-analysis compilation and development-planning report (Agent Mode session) |
| 34 | GPT-5.6 Luna | gpt-5.6-luna | 2026-09-04 | `investigations/tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md` | Ice-troll playtest; encumbrance investigation 2026-09-06; tag/effect/condition unification collation 2026-09-06; playtest executions (mirror 2026-09-11, Bargle 2026-09-13, Your First Adventure 2026-09-14, playtest-1). Likely the same underlying model as row 20 (ChatGPT 5.6); kept separate because the two labels are recorded separately in repo evidence |
| 35 | Grok 4 | (as recorded, grok-4) | 2026-09-06 | `investigations/tiwas-encumbrance-system-investigation-grok-4-2026-09-06.md` | Encumbrance system investigation |
| 36 | Muse Spark 1.3 | muse-spark-1.3-contributor-free | 2026-09-11 | `investigations/tiwas-mirror-combat-playtest-collated-2026-09-11.md` (author/assessor) | Mirror-combat playtest collation 2026-09-11; OpenChamber multi-LLM arena run (provider opencode, `multi-llm-test1-opencode-muse-spark-1-3-contributor-free.json`) 2026-09-18; G5 fusion storage agent + composer of several fused candidates 2026-09-19 |
| 37 | Kilo | kilo-auto-free (recorded as kilo-auto/free; version not established per register annotation) | 2026-09-16 | `_consolidation/decision-register.md` advisory annotation (assessed & stored four DEC-112 L-004 creature-template proposals) | Assessor/storage of L-004 proposals 2026-09-16; OpenChamber arena run (provider kilo) 2026-09-18; G5 fusion source run (dependency map + advisory direction) 2026-09-19 |
| 38 | Buffy / Codebuff | version not established (recorded as buffy/codebuff) | 2026-09-16 | `_consolidation/decision-register.md` advisory annotations (storage/second-assessor of L-004 proposals; IT-Q3 evidence record) | Storage/verification of dragon/goblin/orc + four L-004 proposals 2026-09-16; `.freebuff/` harness directory present in repo |
| 39 | Google Gemini 3.1 Flash Lite | gemini-3.1-flash-lite | 2026-09-18 | `investigations/multi-llm-test2-google-gemini-3-1-flash-lite.json` (provider google) | OpenChamber arena run; G5 fusion source run (compact framing notes) |
| 40 | OpenRouter (free-tier, unspecified) | openrouter/free (provider openrouter) | 2026-09-18 | `investigations/multi-llm-test2-openrouter-free.json` | OpenChamber arena run; G5 fusion source run (context hand-off only — no full candidate rules text) |
| 41 | grok-fusion | multi-llm-synthesis-2026-09-19 | 2026-09-19 | `investigations/tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` (self-reported author_llm) | Author identity of the G5 fusion synthesis. Note: provenance-defect flagged by the upstage red-team — this identity does not appear in the §11 source-run list and represents a fused output of the five arena runs, not an independent underlying model |
| 42 | upstage | solar-pro4:free | 2026-09-19 | `investigations/tiwas-g5-seven-consuming-mechanics-fusion-synthesis-adversarial-verification-chat-results-2026-09-19.md` | Adversarial verifier / red-team of the G5 fusion synthesis (finds RC-1–RC-4, SA-1–SA-6, UF-1–UF-5, EC-1–EC-6; no Invariant violations) |
| 43 | Nemotron 3 Ultra | nemotron-3-ultra-550b-a55b (nvidia provider via opencode run, 2026-09-19) | 2026-09-19 | `investigations/tiwas-g5-seven-consuming-mechanics-verification-chat-report-2026-09-19.md` | Independent assessment of the big-pickle verification (verdict FIT-FOR-G1) |

**Total distinct recorded LLM identities: 43.**

## Consolidated model families

| Family / provider | Recorded identities (rows) | Earliest family date |
|---|---|---|
| Anthropic | Claude Sonnet 5 (1) | 2026-08-29 |
| opencode (agent/harness identity) | opencode / big-pickle (2) | 2026-08-29 |
| NVIDIA (Nemotron) | nemotron-3-super-120b-a12b:free (3), Nemotron 3 Ultra (43) | 2026-08-29 |
| Masked / identity not established | Model-A, Model-B, Model-C (4–6) | 2026-01-23 |
| OpenAI / ChatGPT family | ChatGPT-5.4 Nano (7), ChatGPT (8), ChatGPT 5.2 (18), 5.5-high (19), 5.6 (20), GPT-5.6 Luna (34) | 2026-08-30 |
| DeepSeek | DeepSeek-V4-Flash-0731 (9), DeepSeek (10), DeepSeek-V3 (23) | 2026-08-30 |
| Google | Gemini 1.5 Pro NZST/UTC (11–12), Gemini (13), Gemini 3.6 Flash (25), Gemini 3.1 Flash Lite (39) | 2026-08-30 |
| Meta AI | Muse Spark 1.1 (14), Muse Spark 1.3 (36) | 2026-08-30 |
| Mistral | Mistral Medium 3.5 (15), Mistral (29) | 2026-08-30 |
| Alibaba/Qwen | Qwen3.7 (16) | 2026-08-30 |
| xAI | Grok 4.5 (17), Grok 4.6 (26), Grok 4 (35), grok-fusion (41) | 2026-08-30 |
| GitHub / Microsoft | Copilot (21), Copilot 365 (22) | 2026-09-01 |
| Facebai | Laguna S 2.1 (24) | 2026-09-01 |
| Moonshot | Kimi K3 (27) | 2026-09-01 |
| Mimo / Goose | Mimo 2.5 (28) | 2026-09-01 |
| Perplexity | Perplexity (30) | 2026-09-01 |
| RecallAI | RecallAI (31) | 2026-09-01 |
| Zhipu/GLM | glm-4.5-air (32) | 2026-09-01 |
| Arena.ai | Arena.ai Agent Mode (33) | 2026-09-02 |
| Kilo | Kilo / kilo-auto-free (37) | 2026-09-16 |
| Codebuff | Buffy / Codebuff (38) | 2026-09-16 |
| OpenRouter | OpenRouter free / openrouter/free (40) | 2026-09-18 |
| Upstage | upstage / solar-pro4:free (42) | 2026-09-19 |

## Notes

- **Earliest recorded LLM usage in the repository:** Model-A / Model-B / Model-C
  (masked identities), 2026-01-23 (`investigations/llm-quality-s3-comparison-2026-01-23.md`).
  These were later folded into the 2026-08-30 S-3 collation.
- **Playtesting rosters** (all participants already inventoried above): mirror-match combat
  stress test 2026-09-11 (GPT-5.6 Luna, Claude Sonnet 5, Grok 4.5); Bargle incident 2026-09-13
  (Claude Sonnet 5, GPT-5.6 Luna, Grok 4.5); Your First Adventure 2026-09-14 (GPT-5.6 Luna,
  Grok 4.5); playtest-1 comparative systems-readiness set (GPT-5.6 Luna, Claude Sonnet 5,
  Grok 4.5).
- **OpenChamber arena batch (2026-09-18)** recorded `modelID`/`providerID` pairs:
  opencode/big-pickle; opencode/muse-spark-1.3-contributor-free; google/gemini-3.1-flash-lite;
  kilo/kilo-auto-free; openrouter/openrouter-free. Session exports stored 2026-09-19
  (`investigations/multi-llm-test*.json`) and are the raw drafter-pool runs behind the G5 fusion.
- **Provenance-hygiene flags carried:** Arena.ai version is self-reported (platform exposes no
  model-version metadata); grok-fusion's author identity is disconnected from its own §11
  source-run list (flagged by the upstage red-team, recorded as a provenance defect); the
  masked Model-A/B/C underlying identities remain not established.
- **Excluded as unversioned template placeholders:** `...`, `[Your Model Name]`,
  `__REPLACE_WITH_YOUR_ACTUAL_MODEL_NAME__`, `<executing LLM name>`, `<model>`, and
  `unknown / not established` version strings where they reflect an empty template field
  rather than a real, distinct identity.

*This inventory is stored strictly as an informational, advisory record. Storage and
identification confer no authority under `governance/provenance.md` and the repository
governance model.*