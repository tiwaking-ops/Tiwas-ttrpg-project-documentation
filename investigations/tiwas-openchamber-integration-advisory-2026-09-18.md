---
document:
  title: "Tiwas — OpenChamber Integration Advisory Report"
  version: "1.0"
  status: "Advisory — Project Documentation (Non-Canonical)"
provenance:
  author_llm: {name: "Qwen3.7", version: "Qwen3.7"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
---

# Purpose and Origin

Advisory report produced by **Qwen3.7** on **2026-09-18** (chat session, the Tiwas OpenChamber integration discussion). It is advisory and non-canonical: it recommends tooling/integration strategy only and makes no rulings. Assessed and stored by opencode / big-pickle on 2026-09-18 against the live decision register and governance model; storage and assessment confer no authority.

# Tiwas — OpenChamber Integration Advisory Report

## 1. Purpose and Scope
This report documents the advisory session regarding the selection and integration of an external AI workspace tool for the Tiwas TTRPG project. It records the initial evaluation of "Orca" and the subsequent pivot to "OpenChamber," detailing how OpenChamber's capabilities align with Tiwas's strict governance, provenance, and multi-model advisory requirements. 

This document is advisory and non-canonical. It does not alter, promote, or lock any game mechanics, nor does it modify the established documentation hierarchy.

## 2. Background and Tool Selection
The Tiwas project requires an external AI environment capable of handling massive context windows (the Decision Register and Canonical Rules), routing between hundreds of models for multi-LLM advisory sessions, maintaining extensive archival space for playtest logs and investigations, and utilizing frontier cloud compute without relying on local LLMs. 

- **Initial Evaluation (Orca):** Orca was initially evaluated against these criteria. It was found to support infinite tokens, infinite space, hundreds of models, and no local LLMs, making it a theoretically viable environment for managing the Tiwas ruleset.
- **Pivot to OpenChamber:** The designer (Tiwa) subsequently decided to pivot to OpenChamber. The primary rationale was OpenChamber's superior compatibility with the existing OpenCode workflow. Maintaining toolchain consistency reduces friction and ensures that the strict provenance and governance rules of the Tiwas project are not compromised by environment-switching overhead.

## 3. OpenChamber Integration Strategy
The following strategies were established for leveraging OpenChamber in the Tiwas development workflow, mapping directly to the project's established governance and documentation standards:

### 3.1 Context Management for Complete Governance
Tiwas relies on a massive, interdependent ruleset (e.g., the Decision Register tracking 140+ DECs, 18 Core Invariants, and the Canonical Rules).
- **Strategy:** Utilize OpenChamber's context retention to load the entire `decision-register.md`, `tiwas-canonical-rules-and-changelog-v1.3.md`, and the active `proposals/` document into the workspace context at the start of every session.
- **Benefit:** Eliminates the risk of the model hallucinating mechanics or violating Invariants (e.g., Invariant 6: Cost = natural roll, or Invariant 17: no competing resource pools) because the full, authoritative text is always present in the active context.

### 3.2 Model Routing for Multi-LLM Advisory Sessions
Tiwas governance explicitly requires "Multi-LLM Advisory Sessions" and independent second-model assessments before any proposal can be considered for the 8-step Promotion Rule (REQ-021).
- **Strategy:** Use OpenChamber's model-switching capabilities to assign specific cognitive roles to different models within the same workspace:
  - **Primary Drafter (e.g., Claude Sonnet 5):** Drafting formal proposals, synthesizing advisory reports, and writing rule text.
  - **Stress-Tester (e.g., Grok 4.5 / GPT-5.6 Luna):** Exploring edge cases, running text-based combat pipeline simulations, and challenging the draft's mechanical coherence.
  - **Independent Assessor (e.g., Nemotron / Gemini):** Acting strictly as the auditor to verify the draft against the Canonical Rules and the 18 Invariants, checking for contradictions or silent resolutions of open forks.

### 3.3 Workspace Persistence for the Investigation Archive
Tiwas generates extensive non-canonical but vital artifacts: playtest execution logs, mirror-combat stress tests, location templates, and advisory drafts.
- **Strategy:** Use OpenChamber's native file-system integration to maintain the `investigations/` and `audits/` directories directly within the OpenCode project structure.
- **Benefit:** Maintains perfect provenance and satisfies the Documentation Maintenance Rule (REQ-023). Instead of re-uploading massive playtest logs, the AI can be instructed to reference stored logs (e.g., the Mirror Combat v2 log) directly from the workspace to verify rulings like the DEC-136 R2 full-depth reading.

### 3.4 Enforce LLM Governance Rules via Custom Instructions
OpenChamber allows for persistent system prompts or custom instructions tied to the workspace.
- **Strategy:** Embed the **LLM Governance Rules** (from `governance/status-model.md` §24) directly into OpenChamber's system prompt for this project.
- **Key Directives to Hardcode:**
  1. Treat Canonical Rules as authoritative; treat Proposals/WIP as non-canonical.
  2. Never silently resolve an open designer fork.
  3. Never create a parallel Core resolution engine merely to implement a subsystem.
  4. Always state clearly when an answer depends on a proposal rather than a Canonical rule.

## 4. Findings and Conclusions
- **Tool Selection Finalized:** OpenChamber is confirmed as the optimal environment for Tiwas development, primarily due to its seamless integration with the existing OpenCode workflow.
- **Infrastructure Alignment:** The tool's capabilities perfectly map to the project's four critical infrastructure needs: massive context ingestion, multi-model routing, persistent file-system archival, and strict LLM governance enforcement.
- **Documentation Standards Preserved:** No new Markdown standards or external skills are required or created; the project will continue to use its established documentation conventions and provenance metadata blocks.

## 5. Unresolved Issues / Next Steps
- **Master Context Prompt Generation:** The generation of a concise, highly optimized system prompt encapsulating the Tiwas Core Invariants, the 9-Step Core Test Transaction, and the LLM Governance Rules for OpenChamber's custom instructions is pending designer approval.
- **Next Design Fork Selection:** The specific open design fork to be tackled next in the new environment (e.g., S-5 Armor interaction, S-12 NPC Compression, or the remaining Time/Action economy questions) remains to be selected by the designer.

---

## Storage Assessment (opencode / big-pickle, 2026-09-18)

**Assessment verdict:** Consistent with the live register on all Core citations; one flagged inconsistency (not fixed).

- **Status:** Advisory / non-canonical (self-declared). Validated against the governance model — the document makes no rulings, infers no DEC, and claims no authority. No reclassification performed.
- **Verified accurate references:** 18 Core Architectural Invariants (DEC-016); Invariant 6 (Cost = natural roll) and Invariant 17 (no competing resource pools) as cited; REQ-021 (8-step Promotion Rule); REQ-023 (Documentation Maintenance Rule); LLM Governance Rules at `governance/status-model.md` (D2 §24), incl. the "no parallel Core resolution engine" directive (Governance Rule 11 / Invariant 18); DEC-006 9-step Core Test Transaction; DEC-136 R2 unbounded Location Tier and the DEC-139 full-depth reading confirmation; Mirror Combat v2 log exists (`investigations/tiwas-playtest-human-mirror-combat-v2-results-2026-09-13.md`); `audits/` directory exists.
- **Flagged inconsistency (not fixed, per workflow):** §5 names "S-5 Armor interaction" and "S-12 NPC Compression" as open design forks. In the live register these are **Ruled** — S-5 Armor = DEC-058–062; S-12 Creature/NPC = DEC-076–077; OPEN-005 was closed 2026-09-01. Genuinely-open work today is narrower: Magic §15 (Reserved, DEC-015/DEC-146 sub-rulings 2026-09-18), DEC-133.A R3 seven consuming mechanics, DEC-132.B R2 Tag-to-Reaction granularity deferral, DEC-112 L-004 creature templates / DEC-144 body-plan classes (content-template advisory work in progress). The "Time/Action economy questions" reference also overstates the open set: DEC-132.B R2 and DEC-133.A R3 already narrowed it.
- **Advisory details left open per workflow:** Master context prompt generation (designer approval pending) and next design-fork selection remain the designer's to resolve. None are decided or inferred here.

**Recorded:** annotation appended to DEC-133.A (sibling home of the OpenChamber advisory chain). **Stored:** this file, `investigations/tiwas-openchamber-integration-advisory-2026-09-18.md`. Nothing promoted, demoted, superseded, or reclassified. Storage and assessment confer no authority.