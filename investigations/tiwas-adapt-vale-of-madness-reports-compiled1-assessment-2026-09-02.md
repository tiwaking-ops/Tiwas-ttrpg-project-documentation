---
document:
  title: "Tiwas - Beyond the Vale of Madness - Compiled1 Aggregate - Assessment Record"
  version: "1.0"
  status: "NON-CANONICAL - advisory assessment record. Records and assesses an as-supplied LLM-compiled aggregate; makes no rulings and confers no authority."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
---

# Tiwas - Beyond the Vale of Madness - Compiled1 Aggregate: Assessment Record

## Status and purpose

**Status**: NON-CANONICAL - advisory only. This record assesses and registers the as-supplied compiled file
`tiwas-btvm-system-comparison-compiled1.md` (stored in this repository as
`investigations/tiwas-adapt-vale-of-madness-reports-compiled1-arena-2026-09-02.md`).

The compiled file is an LLM-produced aggregate of 35 embedded Markdown documents: the 25 source LLM
adaptation/readiness reports for adapting *Beyond the Vale of Madness (GURPS)* to the Tiwas TTRPG, plus 10
system-by-system comparison/compilation variants produced by separate LLM sessions.

This record makes **no rulings**, promotes nothing, demotes nothing, and changes no document status. Storing
and registering the compiled file confers no authority on any position it records. As with the source reports,
agreement among LLMs is evidence of analytical convergence only; authority over Tiwas design remains with the
human designer through the established governance path (`_consolidation/decision-register.md`, Promotion Rule
REQ-021 per `governance/status-model.md`).

## File integrity verification (assessed 2026-09-02)

- Source as supplied: `C:\temp\tiwasttrpg0\adventures\reports2\tiwas-btvm-system-comparison-compiled1.md`
  (1,416,766 bytes; 23,772 lines).
- Stored copy: `investigations/tiwas-adapt-vale-of-madness-reports-compiled1-arena-2026-09-02.md`
- Verbatim copy confirmed: SHA-256 of source and stored copy are identical
  (`54BD7C4FCADB256748B837924944CC7CA88055FEB121C0FAC586C64D83883111`).
- Structural check: 35 top-level embedded-document headers detected; no block truncated; nested fenced
  content (e.g., an embedded HTML document inside `tttrpg-grok.md`) intact.

### Embedded-report verbatim check

All 25 embedded source-report blocks were compared against their standalone counterparts in
`C:\temp\tiwasttrpg0\adventures\reports\`. After normalising for harmless character-encoding variation only
(e.g., the compiled aggregate renders em-dashes / en-dashes as `\u2013`/`\u2014` where the standalone files use
ASCII `-`), all sampled blocks were **structurally identical** to their source files. No content was dropped or
reordered. The compiled aggregate therefore faithfully preserves the 25 reports as supplied.

## Inventory of the 35 embedded documents

### Part A - the 25 source adaptation/readiness reports (all already tracked in this repository)

These 25 reports are already stored in `investigations/` and are registered in the attribution manifest
`investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`:

| # | Embedded document (blocks 1-25) | Source-report author |
|---|---|---|
| 1 | btvmadness-adapt-report-chatgpt-5-2-1.md | ChatGPT 5.2 |
| 2 | btvmadness-adapt-report-chatgpt-5-5-high-1.md | ChatGPT 5.5-high |
| 3 | btvmadness-adapt-report-chatgpt-5-6-1.md | ChatGPT 5.6 |
| 4 | btvmadness-adapt-report-chatgpt-5-6-2.md | ChatGPT 5.6 |
| 5 | btvmadness-adapt-report-copilot-1.md | Copilot |
| 6 | btvmadness-adapt-report-copilot-2.md | Copilot |
| 7 | btvmadness-adapt-report-copilot365-1.md | Copilot 365 |
| 8 | btvmadness-adapt-report-copilot365-2.md | Copilot 365 |
| 9 | btvmadness-adapt-report-deepseek-1.md | DeepSeek-V3 |
| 10 | btvmadness-adapt-report-facebai-laguna-s-2-1-1.md | Laguna S 2.1 |
| 11 | btvmadness-adapt-report-gemini-1.md | Gemini 3.6 Flash |
| 12 | btvmadness-adapt-report-gemini-2.md | Gemini 3.6 Flash |
| 13 | btvmadness-adapt-report-grok-1.md | Grok 4.6 |
| 14 | btvmadness-adapt-report-grok-2.md | Grok 4.6 |
| 15 | btvmadness-adapt-report-kimi-1.md | Kimi K3 |
| 16 | btvmadness-adapt-report-metaai-1.md | Muse Spark 1.1 |
| 17 | btvmadness-adapt-report-metaai-2.md | Muse Spark 1.1 |
| 18 | btvmadness-adapt-report-mimo-2-5-1.md | Mimo 2.5 |
| 19 | btvmadness-adapt-report-mimo-2-5-2.md | Mimo 2.5 |
| 20 | btvmadness-adapt-report-mistral-1.md | Mistral |
| 21 | btvmadness-adapt-report-perplexity-1.md | Perplexity |
| 22 | btvmadness-adapt-report-perplexity-2.md | Perplexity |
| 23 | btvmadness-adapt-report-recallAI-1.md | RecallAI |
| 24 | Tiwas-Adventure-Readiness-Audit-Vale-of-Madness-2026-09-01.md | Claude 5 Sonnet |
| 25 | Tiwas-Adventure-Readiness-Audit.md | glm-4.5-air |

Note: blocks 5-8 (Copilot / Copilot 365) appear with the pre-repair filenames without the `_1` repair suffix.
The repaired duplicates (with `_1`) are the tracked copies. The embedded pre-repair names identify the same
reports. See `tiwas-adapt-vale-of-madness-reports-system-comparison-2026-09-02.md` for the duplicate-correction
note.

### Part B - the 10 comparison/compilation variants (blocks 26-35; NOT previously tracked)

These are the genuinely new material in the aggregate, each a separate LLM-authored system-by-system
comparison or synthesis of the same 25 reports. Each self-declares NON-CANONICAL, advisory status and
self-reports its producing model and provenance.

| # | Embedded document (blocks 26-35) | Self-reported author | Produced |
|---|---|---|---|
| 26 | tiwas-btvm-system-by-system-comparison-2026-09-02.md | Arena.ai Agent Mode (model unknown / not established) | 2026-09-02 |
| 27 | tttrpg-copilot.md | Copilot | - |
| 28 | tttrpg-deepseek.md | ChatGPT | - |
| 29 | tttrpg-gemini.md | Gemini 2.5 Flash | 2026-09-02 |
| 30 | tttrpg-grok.md | Grok 4.5 | - |
| 31 | tttrpg-recallAI.md | Claude 3.5 Sonnet (producing session for RecallAI) | - |
| 32 | tiwas-btvm-system-comparison.md | GLM | 2026-09-02 |
| 33 | tiwas-ttrpg-multi-llm-adaptation-report-comparison.md | Mistral Medium 3.5 | - |
| 34 | Tiwas-Multi-LLM-System-Comparison-FINAL.md | Muse Spark 1.1 | 2026-09-01 |
| 35 | tttrpg-qwen.md | Qwen3.7 | 2026-09-02 |

All Part B provenance claims are **self-reported** and, where stated, the producing platform exposes no
independently verifiable model-version metadata. These identity statements are recorded as claims, not as
independently verified signatures.

## Deduplication note

- Part A (block 25 reports) is **already tracked** in `investigations/` as individual files and as the merged
  `tiwas-adapt-vale-of-madness-reports-1.md`, plus the attribution manifest. Their embedded copies in the
  compiled1 aggregate are redundant copies; they are retained here only because the aggregate is being stored
  as an intact as-compiled artifact.
- Part B (blocks 26-35) is **new** and overlaps in content with the already-committed
  `tiwas-adapt-vale-of-madness-reports-system-comparison-2026-09-02.md` (opencode/big-pickle authored). The
  committed opencode comparison remains the repository's own system-by-system compilation; the Part B variants
  are preserved as distinct independently-produced viewpoints.

## Shared findings observed across the 25 source reports (basis for advisory assessment)

These are recorded solely as the analytical convergence present in the source reports; they are not rulings
and confer no authority:

- Core Test d100 (DEC-001-DEC-016) is Playtestable Now; unanimous.
- Cost/Overflow (DEC-007 / DEC-007.A) is Playtestable Now.
- XP / advancement (DEC-009-DEC-012) is Playtestable Now.
- S-1 Universal Opposed Contest is Playtestable Now (unanimous).
- S-8 Difficulty/Modifiers is architecturally ruled, but the per-tier numeric values are not supplied in the
  source baseline excerpt.
- S-12 creature content (Ice Troll, Blood Man) is the top blocker; no table-ready stat blocks exist (DEC-076/077
  framework only; Part C.1 Open).
- S-3 gated-tier Effect contents are not enumerated (Part C.3).
- OPEN-007 wound consequences are not table-ready (Part C.4).
- Equipment / encumbrance / magic / conditions are Reserved (DEC-015).
- No fear / fright subsystem exists anywhere in the source baseline.
- No skill-default / untrained-fallback rule is present.
- Damage magnitude of the base-tier "Inflict Injury" Effect is undefined (reported by Kimi).
- S-6 defender skill is unspecified (reported by Kimi).

## Disagreement / dispersion register (as reported by the 25 source reports)

- Readiness metrics are widely dispersed. Reported overall readiness estimates range from roughly 15% (Mistral)
  up to "75-85%" / 8/10 (Copilot 365). This wide spread is itself an advisory finding: different reports used
  different denominators and readiness categories (per the source prompt categories), so the percentages are
  not directly comparable.
- The variations are confined to how fully a subsystem is judged "ready"; no report disputes the underlying
  authority classification (Canonical / Ruled / Reserved / Open) of the baseline material.

## Source-grounding caveats (weight evidence accordingly)

Carried from `tiwas-adapt-vale-of-madness-reports-system-comparison-2026-09-02.md`:

- `glm` (glm-4.5-air): no direct PDF access; requirements inferred from generic GURPS patterns; least grounded.
- `copilot-2` / `copilot-2_1`: supplied extract truncated/garbled; inventory largely inferred.
- `mimo-2-5-2`: adventure text OCR-scanned with transcription errors; truncated in the Blood Man stat block.
- `chatgpt-5-2-1`: parsed pages 1-12 plus 16-19 (pregens).
- All others: full PDF or full provided adventure text.

## Assessment conclusion

The compiled aggregate is structurally sound, is a faithful (verbatim) preservation of the 25 source reports,
and adds 10 new independently-authored comparison variants. All material is NON-CANONICAL advisory material and
is recorded/stored as such. No promotion, demotion, or status change has been made by this record, and none
should follow from it without the repository's established human-governed authority path.

## Source and evidence register

- Compiled aggregate as supplied: `C:\temp\tiwasttrpg0\adventures\reports2\tiwas-btvm-system-comparison-compiled1.md`
- Stored verbatim copy: `investigations/tiwas-adapt-vale-of-madness-reports-compiled1-arena-2026-09-02.md`
- Attribution manifest (source of R1-R25 author numbering): `investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`
- Open-source standalone reports (comparison basis): `C:\temp\tiwasttrpg0\adventures\reports\`
- Part B standalone variants (comparison basis): `C:\temp\tiwasttrpg0\adventures\reports2\`
- Repository's own system-by-system comparison (overlap target): `investigations/tiwas-adapt-vale-of-madness-reports-system-comparison-2026-09-02.md`