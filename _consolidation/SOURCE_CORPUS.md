---
document:
  title: "Source Corpus Index"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Source Corpus Index

This consolidation was run against exactly one supplied corpus file: `TTTRPG-merge-v1.md`, containing five embedded Tiwas TTRPG design/governance documents (D1–D5), plus a separate governing specification document (the consolidation prompt itself, treated as process input, not project subject matter).

| Copy | Location | Nature |
|---|---|---|
| Full merged original, byte-for-byte | `sources/SOURCE_CORPUS_ORIGINAL_TTTRPG-merge-v1.md` | Unmodified copy of the as-supplied file |
| D1 extracted | `sources/tiwas-canonical-rules-and-changelog-v1.3.md` | Unmodified extracted content (fence markers removed only) |
| D2 extracted | `sources/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` | Same |
| D3 extracted | `sources/tiwas-proposals-wip-and-design-direction-v1.4.3.md` | Same |
| D4 extracted | `sources/tiwas-s2-hit-location-investigation-v5-synthesis.md` | Same |
| D5 extracted | `sources/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` | Same |
| Governing specification | `prompts/project-documentation-consolidation-prompt.md` | Abbreviated capture — see limitations note below |

See `document-inventory.md` for per-document detail, `decision-register.md` / `requirement-register.md` / `conflict-register.md` / `relationship-map.md` for extracted knowledge, and `consolidation-plan.md` for what was built from this corpus and why.

## Extraction method note

The five embedded documents were mechanically separated on their top-level `## <filename>.md` headers and un-fenced from their surrounding ` ```markdown ` code blocks. No wording inside any document was altered. This was verified by line/character-count comparison during extraction (see the bash history of this session for the exact commands run).

## Known limitation

The `prompts/` copy of the governing consolidation specification is an abbreviated capture, not a verbatim reproduction, due to its length. The full specification governed this run in-session. If a byte-for-byte copy of the specification is required for future reuse, it should be re-supplied and saved in full.
