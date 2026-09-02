---
note: >
  Complete, self-contained prompt for producing a SYSTEM-BY-SYSTEM COMPARISON
  OF THE MULTI-LLM ADAPTATION REPORTS (the 25-report set), with a mandatory
  author-identity requirement. This is the prompt that produces documents like
  the comparison compilation (system-indexed view: which reporting LLMs covered
  which Tiwas system, what each reported, where they agree, where they
  disagree). It merges the original comparison-prompt requirements (Role,
  Context, Audience, Format and length, Success criteria, Constraints, Examples
  and references, flag-guessing convention) with a first-class author-identity
  requirement and a standard report template.

  NOTE (v2 correction): an earlier version of this file framed the task as a
  fresh Tiwas-vs-adventure adaptation audit (that is a DIFFERENT prompt — the
  one used to generate each of the 25 individual reports). This is the
  comparison-of-the-25-reports task, which is what the user actually runs.
external_metadata:
  role: "Reusable complete prompt + template for the 25-report multi-LLM comparison compilation, with mandatory self-identification"
  author_llm: "opencode / big-pickle"
  created_date: "2026-09-02"
  revision_note: "v2 after user correction - task rebuilt as multi-LLM comparison compilation, not single-report adaptation audit"
---

# Multi-LLM Report Comparison — Complete Self-Contained Prompt (with Author Identity Requirement)

Use with any external LLM (ChatGPT, Claude, Gemini, Grok, Copilot, etc.). Copy
the **entire "Complete prompt" block** below into a fresh chat as the opening
message, and attach the listed source files. The block is a complete prompt:
it requires a system-by-system comparison of the 25 LLM adaptation reports AND
mandatory author self-identification.

## Complete prompt (copy this entire block, verbatim, into a new chat)

> ## Task
>
> Compile a comprehensive **system-by-system comparison of the 25 individual
> LLM adaptation reports** assessing whether the Tiwas TTRPG system can adapt
> the GURPS solo adventure *Beyond the Vale of Madness*. The 25 reports live in
> the attached attribution index. Produce the comparison **now**, in full,
> using the attached template, as a single response.
>
> "System-by-system comparison" means, **for every Tiwas system** covered by
> any of the 25 reports:
> 1. **Which LLMs reported on it** (list them by name).
> 2. **What each report said** about it (distilled position per report, plus
>    1–2 key direct quotes each).
> 3. **Collated synthesis** — where the reports agree.
> 4. **Where they disagree** — place the disagreement into a named table
>    (e.g. `D1`, `D2`, …) listing the reporting LLMs on each side.
>
> Do **not** produce a fresh single-LLM adaptation audit of the adventure. The
> deliverable is a comparison of the 25 existing reports.
>
> ## Role
>
> You are a documentation and governance analyst producing an advisory,
> system-indexed synthesis of a multi-LLM evaluation corpus. You are fluent in
> the Tiwas governance model: Canonical / Locked, Ruled non-canonical,
> Reserved, Open, Missing, Proposed, WIP, Experimental, Design Direction,
> Superseded, and the distinction between canonical material, proposal,
> investigation, roadmap, source, archive, and decision records.
>
> ## Context
>
> Twenty-five independently produced LLM adaptation reports assessed whether
> the Tiwas TTRPG system can adapt the GURPS solo adventure *Beyond the Vale of
> Madness*. An existing compilation organizes those reports by **priority tier
> and disagreement register**. This compilation is deliberately
> **complementary**: it is organized **system-by-system**, so that for any one
> Tiwas subsystem the reader can see which LLMs covered it, what each said,
> where they agree, and where they disagree. The result will inform Tiwas
> development and the first proper playtest.
>
> ## Audience
>
> Primary: Tiwa (the designer and governance authority) and the Tiwas
> development team. Secondary: Alpha playtest GMs who need a per-system
> readiness picture across the independent assessments.
>
> ## Format and length
>
> Output a **comprehensive formal project report in Markdown**, following the
> attached template section-for-section. The report must include:
> - Status + provenance front matter (NON-CANONICAL advisory; exactly the
>   template's structure, with every placeholder replaced)
> - Basis and method (source boundary, attribution discipline, per-report
>   source-grounding caveats)
> - Part 1: **System-by-system comparison** — every system, each with its
>   reporting LLMs, per-report distilled position + 1–2 key quotes, and a
>   collated synthesis
> - Part 2: **Named disagreement table(s)** — unresolved splits, each labelled
>   `D1`, `D2`, … with the reporting LLMs on each side and a consequence row
> - Part 3: Isolated / narrow findings that do not rise to a disagreement
> - Governance and authority boundary
> - Source register
>
> Length: detailed but focused — table-usable and governance-usable, no
> narrative padding.
>
> ## Success criteria (what makes this great)
>
> 1. **Every system mentioned by any report is listed**, with the reporting
>    LLM(s) named for that system.
> 2. **Multi-LLM agreement is collated** — shared positions are identified, not
>    merely repeated.
> 3. **Every disagreement between reports is explicit and named** (`D1`, `D2`,
>    …) with the LLMs on each side, not silently reconciled.
> 4. **Per-system depth** is a summarized per-report position plus 1–2 key
>    quotes, then a collated synthesis.
> 5. **Formal Tiwas reporting standards** are met: front matter with status +
>    provenance, evidence-discipline, no rulings, no promotion.
>
> ## Constraints
>
> - **Source boundary:** use only the attached sources — the attribution index
>   (25-report set), the Tiwas Alpha playtest corpus, and the adventure PDF.
>   Cross-reference any existing compilation; do not reproduce it.
> - **Evidence before interpretation:** determine each document's status
>   first; do not infer authority from repetition, chronology, majority,
>   ordering, or how strong a claim sounds.
> - **No authority changes:** do not promote, demote, supersede, or otherwise
>   alter any document's status. Every classification you report carries
>   exactly the authority it had in its source report.
> - **Do not fabricate:** record unknown provenance/missing evidence as
>   unknown; do not reconstruct missing material.
> - **Flag every inference/guess explicitly** (see "Flagging guesses" below).
> - Follow a formal report tone; no fiction, flavour text, or editorializing.
>
> ## Flagging guesses
>
> Add a section **"Guesses I had to make"** that explicitly lists every
> interpretation you adopted where the sources did not single-handedly decide —
> including, for this task, the expected author identity, the expected output
> file location/naming, what counts as a "system", and what "formal Tiwas
> reporting standards" means. If an item is genuinely unresolvable, mark it as
> such and state why rather than deciding silently.
>
> ## Author identity requirement
>
> **You MUST identify yourself as the author.** This is a first-class
> requirement, not optional.
>
> Instructions for self-identification:
> 1. **State your producing-model identity** precisely as you know it — the
>    model name/version you were instantiated under in this session (e.g.
>    "ChatGPT-5.5", "Claude-5-Sonnet", "Gemini-3.6-Flash"). Do **not** guess a
>    more specific version than you actually know.
> 2. **Do not copy an identity supplied in the template or prompt.** The
>    `provenance` block in the template is a *placeholder*, not your identity.
>    If the template already contains a filled-in author name/version that is
>    not you, replace it with your own identity, or record the producing model
>    as "unknown / not established" if you genuinely cannot determine it.
> 3. **The version field must name the producing model version, not a date.**
>    Putting the date in the version field fails this requirement. If your
>    platform does not expose the model version, write "unknown / not
>    established" — never the date.
> 4. **Distinguish your report (the document you are producing) from your
>    session identity.** Record what you know and what you do not know.
> 5. **Treat self-identification as produced evidence, not verified fact.**
>    Your self-reported identity is a claim by you; it is not a verified
>    signature. Where your platform gives a non-forgeable indicator (e.g. an
>    exported header, a metadata field you can read), note which mechanism you
>    used.
> 6. **Report identity in the `provenance` front matter and in a prose
>    "Provenance" note**, so a reader sees it in both places.
>
> The provenance fields you are responsible for reporting:
> - `author_llm.name` / `author_llm.version` — **your actual producing
>   identity** (or "unknown / not established"); version must not be a date.
> - `assessor_llm` — leave empty unless you are returning this document
>   specifically as an assessment of someone else's document.
> - `last_modified_by_llm` — you, if you produced or modified the document.
> - `created_date` / `last_modified_date` — the date you produced the document.
> - `identity_established_by` — how the identity was established
>   (self-reported, platform metadata, unknown).
>
> ## Output format
>
> Return exactly one artifact: a complete markdown report following the
> attached template section-for-section, with every provenance placeholder
> replaced. Placeholder tokens (`__REPLACE_WITH_...__`) must not remain in the
> final output. If you cannot determine a required provenance value, write
> "unknown / not established" in that field and say why.
>
> ## Examples / references
>
> Reference files (attach and use only those you actually consult; list exactly
> which in the report's Source register):
> - `tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md` —
>   the primary 25-report source: annotated attribution index with per-report
>   attribution, source-grounding caveats, and the repaired merge of all 25
>   reports.
> - `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` — Tiwas baseline and
>   authority/status boundary (referenced to interpret what each report meant
>   by a readiness claim).
> - `Beyond-the-Vale-of-Madness-GURPS.pdf` — the adventure benchmark (referenced
>   to interpret what each report was mapping).
> - Cross-reference, do not reproduce: the existing priority/disagreement
>   compilation and its system-by-system companion in `investigations/`.

## Standard report template (attach with the prompt above)

The template below is intentionally identity-neutral: every author field is a
placeholder that the producing LLM must replace with its own actual identity.

```markdown
---
document:
  title: "Tiwas — Beyond the Vale of Madness — Multi-LLM Adaptation Reports — System-by-System Comparison"
  version: "1.0"
  status: "NON-CANONICAL - advisory compilation. System-by-system synthesis of the 25 source reports; makes no rulings and confers no authority."
provenance:
  author_llm:
    name: "__REPLACE_WITH_YOUR_ACTUAL_MODEL_NAME__"
    version: "__REPLACE_WITH_YOUR_ACTUAL_MODEL_VERSION__"
  assessor_llm: []
  last_modified_by_llm:
    name: "__REPLACE_WITH_YOUR_ACTUAL_MODEL_NAME__"
    version: "__REPLACE_WITH_YOUR_ACTUAL_MODEL_VERSION__"
  created_date: "__REPLACE_WITH_TODAYS_DATE__"
  last_modified_date: "__REPLACE_WITH_TODAYS_DATE__"
  identity_established_by: "self-reported / platform metadata / unknown"   # choose one; the version field must NOT be a date
---

# Tiwas — Beyond the Vale of Madness — Multi-LLM Adaptation Reports: System-by-System Comparison

## Provenance note

This comparison was produced by **__REPLACE_WITH_YOUR_ACTUAL_MODEL_NAME__**
(__REPLACE_WITH_YOUR_ACTUAL_MODEL_VERSION__) on
__REPLACE_WITH_TODAYS_DATE__. The producing model identity stated here is
[choose one]:

- **self-reported**: this identity is what the session reports itself to be;
  it is a claim by the producing model, not an independently verified
  signature.
- **platform metadata**: the identity was read from a non-forgeable platform
  field (name it), which is stronger than a bare self-report.
- **unknown / not established**: the producing model could not determine its
  own identity; provenance is recorded as unknown rather than fabricated.

This comparison is NON-CANONICAL and advisory only. Repetition, chronology,
majority view, or report ordering confers no authority on any Tiwas
subsystem.

## 1. Status and purpose

_[status: NON-CANONICAL advisory; complementary to the existing
priority/disagreement compilation; makes no rulings]_

## 2. Basis and method

_[source boundary; attribution discipline; per-report source-grounding caveats;
readiness-label vocabulary used (documentary classifications, not rulings)]_

## 3. Part 1 — System-by-system comparison

For each Tiwas system:
- **Reporting LLMs (n):** the LLM/report abbreviations.
- **Per-report position:** distilled position per report + 1–2 key quotes.
- **Collated synthesis:** where the reports agree; pointers to disagreements.
- **(Disagreements are named in Part 2, not reconciled here.)**

## 4. Part 2 — Named disagreement table(s)

| ID | System / question | Side A (reporting LLMs) | Side B (reporting LLMs) | Consequence |
|---|---|---|---|---|
| D1 | _…_ | _…_ | _…_ | _…_ |

_Add rows D2, D3, … as needed. Do not merge conflicting classifications into a
new rule._

## 5. Part 3 — Isolated / narrow findings

_[findings unique to one or few reports that do not rise to a disagreement]_

## 6. Guesses I had to make

_[every inference/assumption; each marked with its basis and confidence]_

## 7. Governance and authority boundary

This report does **not**: promote, demote, supersede, or alter the status of
any document; convert repeated LLM agreement into a designer ruling; resolve
disagreements; treat the adventure as authority over Tiwas mechanics; infer
authority from chronology, majority, ordering, or apparent quality; or
fabricate missing mechanics or provenance.

## 8. Source register

| Source | Function in this report |
|---|---|
| `tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md` | Primary 25-report corpus, attribution manifest, source-grounding caveats |
| `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` | Tiwas baseline and authority/status boundary |
| `Beyond-the-Vale-of-Madness-GURPS.pdf` | Adventure requirements and mechanical benchmark |

*End of NON-CANONICAL advisory comparison.*
```

## Operational note on reliability

An LLM will *claim* an identity either way; the `identity_established_by`
field forces each one to say **how** it established that identity, and a bare
"self-reported" mark is the honest default. Known Copilot failure mode: it put
the date (`2026-09-02`) in the `version` field instead of a model version —
the prompt now explicitly forbids that. For non-forgeable attribution, capture
the producing model from the **API/session metadata** at run time (which the
model itself does not own) rather than trusting its prose. Record that external
capture under the template's `platform metadata` option.