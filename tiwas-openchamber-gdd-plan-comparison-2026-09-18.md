---
document:
  title: "Tiwas — Comparison: OpenChamber Multi-LLM Workflow Plan (Claude) vs. GDD Multi-LLM Orchestration Plan (opencode/big-pickle)"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. Comparative assessment of two independently-authored, same-day advisory tooling plans; not a ruling, not a register action, and confers no authority."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
---

# Tiwas — Comparison: Two OpenChamber Multi-LLM Workflow Plans (2026-09-18)

**Author:** Claude — LLM name: `Claude Sonnet 5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-18
**Document class:** Advisory comparative assessment, produced in a chat session at the user's (Tiwa's) request. **Not a ruling. Not a register action. No DEC assigned or inferred. Confers no authority on either compared document or on anything recommended below.**

---

## 0. Governance Statement

This document:

- Assigns **no DEC number** and proposes none.
- Makes **no change to Canonical Rules, Proposals/WIP, or the Implementation Roadmap**.
- Compares two **advisory, non-canonical, same-day** tooling plans produced independently by two LLM sessions on the same underlying question (how to use OpenChamber for Tiwas multi-LLM development). Neither compared document is authoritative; this comparison does not make either one so.
- Follows the project's established precedent of comparing multiple independently-authored advisory drafts before any human ruling (e.g. the eight advisory inputs compared for the Tags/Effects/Conditions unification question, `decision-register.md` DEC-080 cell) — this document is that kind of comparison, not a new kind of artifact.
- Documents **`Claude Sonnet 5`'s own session output** (`tiwas-openchamber-multi-llm-workflow-plan-2026-09-18.md`) being assessed against a second document from a different author; where this document finds the second document's claims unverified, that is recorded as unverified-by-both, not as an error.

---

## 1. Documents Compared

| | Document A | Document B |
|---|---|---|
| Title | `tiwas-openchamber-multi-llm-workflow-plan-2026-09-18.md` | `tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md` |
| Author | Claude Sonnet 5 (`claude-sonnet-5`) | opencode (`big-pickle`) |
| assessor_llm | not established | not established |
| Scope as stated | "How do I use OpenChamber given my situation" — router retirement, genuinely-open content gaps, promotion backlog | "How do I rapidly build the GDD backbone" — full multi-agent drafting pipeline, agent roster, rollout schedule |
| Status | Advisory / Non-canonical, no DEC | Advisory / Non-canonical, no DEC (self-declared "Rule Authority: None") |

Both were produced the same day, independently, on overlapping but not identical questions. Per project convention, overlapping advisory material is compared rather than treated as redundant or as a tie-break contest.

---

## 2. Accuracy Check — OpenChamber Feature Claims

Cross-checked against this session's own independent research (§3 of Document A) rather than against Document B's text alone, since neither document's `assessor_llm` field shows prior verification.

| Claim (Document B) | Independent finding (this session) | Verdict |
|---|---|---|
| Multi-run: 1 task → up to 5 models, worktree isolation | Matches | Corroborated |
| Fusion: combine strongest parts into a new session | Matches | Corroborated |
| Session Goals: continue toward a finish line, survives app closure | Matches | Corroborated |
| Scheduled tasks (cron) | Matches | Corroborated |
| Changes Walkthrough (AI-guided diff tour) | Matches | Corroborated |
| Remote (QR + private relay) | Matches | Corroborated |
| Agent Control tool (agents spin up sessions from chat) | Not encountered in this session's research | **Unverified by either document** |
| Settings → Providers/Agents UI configuration flow | Not encountered; this session found `opencode auth login` / `/connect` / `opencode.json` as the documented provider-config path instead | **Unverified** — plausible, not confirmed against primary docs |
| Single-maintainer caveat, sourced to third-party review (aireiter, 2026-08) | Document B itself labels this evidence class explicitly | Good practice — self-flagged, not asserted as OpenChamber's own claim |

Where the two documents' claims overlap, they agree. Two claims in Document B — the Agent Control tool and the Settings-panel configuration flow — remain unverified by either document and should not be treated as confirmed until checked against OpenChamber's own current documentation.

---

## 3. Structural Comparison

| Dimension | Document A (Claude) | Document B (opencode) |
|---|---|---|
| Governance mechanism for drafts | Pasted preamble instructing models to stay non-canonical | **Spec cards** (purpose, status, dependency chain, locked invariants, open questions) as a machine-checkable contract, plus a dedicated **Adversarial Verifier** model excluded from the drafter pool |
| Provenance handling | Left implicit (user expected to file it) | Explicit **Registrar** role (opencode) — provenance headers, DEC references, register annotations |
| Parallelism discipline | Implicit split (Multi-run for open content; single-model for backlog) | Explicit rule: **"front-end parallel, back-end serial"** — parallelism confined to dependency-DAG leaf sections, never at merge points, tied to the Roadmap's own §6.1 dependency diagram |
| Promotion backlog (Ruled-but-non-canonical material never run through the 8-step Promotion Rule) | Identified as a distinct, likely-larger bottleneck, given its own workflow (§5.3 of Document A) | Not treated as a distinct workstream — folded silently into "anything seeking canonical status runs the existing G2 gate" |
| Disposition of the user's existing custom LLM Router | Explicit recommendation (retire it), with one flagged caveat (consumer-chat-only models with no OpenCode provider path) | Out of scope, not mentioned |
| Concrete rollout plan | One suggested pilot (Magic subsystem), no schedule | Full Day 0–5 rollout with a stated exit criterion |
| Risk analysis | None | Dedicated failure-modes table with mitigations |

---

## 4. Where Document B Is Stronger

- **Verifier independence** (a model that drafted a section must not also assess it) is a real methodological safeguard absent from Document A. It is also a natural extension of a pattern already present throughout this project's own provenance conventions (`author_llm` kept distinct from `assessor_llm`), applied here as a live pipeline step rather than only a static record field.
- **Spec cards** are a stronger enforcement mechanism than Document A's fixed preamble: a preamble can be ignored mid-generation, while a spec card gives the Verifier a concrete, checkable contract — making several of the LLM Governance Rules (Roadmap §24, rules 4–10) testable rather than merely requested.
- The **DAG-leaf-only parallelism rule** is a sharper and more general version of the informal split Document A only applied ad hoc.
- The **day-by-day rollout with an exit criterion** has no counterpart in Document A.

## 5. Where Document B Has a Gap, Demonstrated by Its Own Worked Example

Document B does not distinguish "genuinely open design questions" from "already-Ruled material only awaiting formal Promotion." This is not a hypothetical concern: Document B's own worked example in its §4 Loop description —

> «Spin up a Sprint session for **S-7** on gpt/gemini/claude»

— targets Incapacitation/Death, which per `decision-register.md` is already fully Ruled (DEC-052 through DEC-057, DEC-108, DEC-111, DEC-130). Running the full P0–P4 divergent-drafting pipeline against an already-settled subsystem would spend a sprint re-deriving decided ground, and risks the mirror image of what LLM Governance Rule 4 forbids: instead of promoting a proposal because it appears repeatedly, this pattern would generate *fresh, unnecessary* proposals against ground already closed, because the pipeline's P0 backbone-extraction step is not specified to check the register before selecting leaf sections. Document B does not state that P0 must do this — it is assumed, not required.

## 6. Recommended Synthesis

Consistent with the project's established handling of overlapping advisory drafts (compare, then fuse the strongest parts into one working document, with no automatic promotion of either):

1. **Adopt Document B's pipeline** (P0–P4, spec cards, Verifier independence, Registrar role) as the operating model for genuinely-open items — the Magic subsystem, the seven consuming mechanics (DEC-133.A R3), granular Tag-to-Reaction matching (DEC-132.B R2), and remaining creature Location templates (DEC-112 L-004). This is the stronger mechanism for that class of work.
2. **Add two elements from Document A that Document B lacks:**
   - Treat the Promotion backlog as its **own P0 output category**, routed not to divergent leaf-drafting but to a single-model, direct-repo-edit session executing the known 8 Promotion Rule steps against material already Ruled.
   - Carry forward the router-retirement recommendation and its one flagged caveat (models reachable only via a free consumer chat UI with no OpenCode provider path), since Document B does not address disposition of the existing router at all.
3. **Require Document B's P0 step to check `decision-register.md` before selecting a leaf section for drafting**, closing the gap identified in §5 — this is a process addition, not a ruling on any subsystem.
4. Neither source document changes status because of this comparison; both remain Advisory / Non-canonical per their own headers, and this synthesis recommendation is itself non-binding pending the human designer's (Tiwa's) review.

---

## 7. Open Items / Not Resolved by This Comparison

- Whether to formally merge the two documents into one adopted working plan, or keep both as separate standing references.
- Document B's own open item #2 (Verifier model selection) remains open.
- The "Agent Control tool" and Settings-panel configuration claims in Document B remain unverified by either document.
- Whether Document B's pipeline will actually be amended to check the register before leaf-section selection (§5/§6.3) has not been decided.

---

## 8. Filing Note

Recommended location, consistent with the project's `investigations/` directory convention for evidentiary/advisory, non-self-executing material: `investigations/tiwas-openchamber-gdd-plan-comparison-2026-09-18.md`. Storage confers no authority; nothing in this document is Canonical or Ruled.

**End of document.**
