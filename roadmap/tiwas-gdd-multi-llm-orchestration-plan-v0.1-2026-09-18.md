---
document:
  title: "Tiwas GDD — Multi-LLM Orchestration Plan"
  version: "v0.3"
  status: "Non-canonical advisory (self-declared: Rule Authority: None) — implementation/process guidance. Standing instruction for the multi-LLM GDD drafting workflow. Does not create game mechanics and changes no rule authority."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-19"
---

# Tiwas GDD — Multi-LLM Orchestration Plan

**Document Version:** v0.3
**Document Status:** Advisory implementation/process guidance

**Change note (v0.2, 2026-09-18):** folds three gaps from the advisory workflow plan `investigations/tiwas-openchamber-multi-llm-workflow-plan-2026-09-18.md` into this document — a promotion-backlog workstream (§3.1), a mandatory governance preamble for draft prompts (§3.2), and the disposition of the existing Tiwas LLM Router (§6.1). Process-only edits; no rule authority changed; no DEC inferred.
**Change note (v0.3, 2026-09-19):** appends §10 process lessons from the first executed P1→P2→assessment loop (DEC-133.A R3 seven consuming mechanics): tracked-session fusion, line-numbered verifier findings, codified P2b independent assessment, exports straight to `investigations/`. Process-only; no rule authority changed; no DEC inferred.
**Rule Authority:** None — this document does not create game mechanics
**No DEC inferred.** This is a workflow plan, not a designer ruling.
**Important:** Implementation guidance must never be mistaken for a design ruling. No output produced under this plan is authoritative until the designer accepts it (gate G1) and, where canonical status is sought, the 8-step Promotion Rule completes (gate G2).

## 0. Purpose

Rapidly develop the Game Development Document (GDD) — a structured outline/backbone of Tiwas (section structure, dependency graph, locked invariants, open questions) — by filling sections in parallel with multiple AI agents running across several API-based models. The plan chooses a control plane (opencode CLI, OpenChamber, or both), assigns specialised roles, and keeps the designer as the final human gate.

This document exists separately from the rules so that:

- drafting speed does not become game law;
- cross-LLM contradictions are surfaced as designer questions, not silently resolved;
- future LLM sessions have a stable, reusable development process; and
- provenance and promotion discipline remain enforceable.

## 1. Why multi-LLM

GDD work is two different labour types.

- **Divergent generation** — alternative framings for open subsystems (S-2..S-12 candidates). Parallelism pays hard here: N models surface N candidate designs, and cross-model disagreement is exactly the question list the designer must rule on.
- **Convergent unification** — invariant-checking, dependency ordering, merging, governance. This must be one disciplined agent with the repository in context; otherwise the result is five self-consistent but mutually contradictory doclets.

Rule of thumb: **front-end parallel, back-end serial.** Parallelism is spent on leaf sections of the dependency DAG, never on merge points.

## 2. Division of labour / agent roster

| Agent | Who / what | Job |
|---|---|---|
| Backbone Builder / Orchestrator | opencode (this environment) | Build spec cards, edit repository files, obey governance, perform final merges |
| Drafter pool | 3–5 different-vendor models | First-pass section content, alternative mechanic framings |
| Adversarial Verifier | One strong model NOT in the drafter pool | Red-team drafts against spec-card invariants + decision register; flag silent assumptions and contradictions |
| Synthesizer / Fusion | OpenChamber Fusion → opencode finalizes | Combine strongest parts; surviving disagreements become the human-question list |
| Registrar | opencode | Provenance headers, DEC references, decision-register annotations |
| Designer | Tiwa | Rulings only (gates G1 and G2) |

Verifier independence is deliberate: a model that drafted a section must not also vouch for it.

## 3. The pipeline

- **P0 — Backbone (opencode).** Extract the GDD skeleton from the Canonical Rules (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`), the roadmap, and the decision register (`_consolidation/decision-register.md`). One **spec card per section** = purpose, status, dependency chain, locked invariants, open questions, links (DEC / proposal / investigation). The spec card is the *contract* a drafter agent must satisfy.
- **P1 — Draft sprint (OpenChamber Multi-run).** Pick a ready leaf section; dispatch one prompt to 3–5 models, each in its own git worktree (zero collisions). Outcomes: N candidates.
- **P2 — Verify (Verifier).** Each candidate checked against spec-card invariants and the decision register → pass/fail + contradiction report.
- **P3 — Merge (opencode).** Keep the best, or Fusion the survivors; contradictions become the question list.
- **P4 — Human gate (G1).** Designer rules on the question list → adopt into the GDD working copy. Anything seeking canonical status then runs the existing proposal → DEC → 8-step Promotion path (G2) — executed as the §3.1 workstream. The GDD working document stays advisory until formal promotion.

### 3.1 Promotion backlog — separate workstream (gate G2)

The accepted-but-unpromoted rulings backlog is **not** a Multi-run/Fusion task: each item already carries one accepted designer ruling, so there is nothing to compare. Each only needs the formal 8-step Promotion Rule (`governance/status-model.md`) executed and the Canonical Rules & Changelog updated to match. This is single-model, direct-repo editing work — the §2 Backbone Builder / Orchestrator executes it one item at a time, with the §2 registrar discipline. DEC-017 remains the sole item to have completed the full 8-step rule to date. The advisory plan's register survey (`investigations/tiwas-openchamber-multi-llm-workflow-plan-2026-09-18.md`, §4) provides the open-content vs accepted-ruling split that governs which items reach this stream.

### 3.2 Mandatory governance preamble (draft sprints)

Every Multi-run / drafter prompt MUST carry the following preamble verbatim, so no model writes into `canonical/` or silently resolves an open designer fork:

> You are producing non-canonical advisory material only. Per this project's `governance/status-model.md` and the LLM Governance Rules, your output goes into `investigations/` or `proposals/`, is never Canonical, and must not silently resolve an open designer fork. Cite existing DEC IDs from `decision-register.md` where relevant. State your evidence class (mechanical fact / empirical finding / designer ruling / recommendation) for each claim.

Loop: a queue of leaf sections is drained by OpenChamber **scheduled tasks**; every drafting session gets a **Session Goal** («fill section to spec card v2; keep going until the invariant check passes»).

## 4. OpenChamber — what to use it for, concretely

OpenChamber is an MIT-licensed, open-source **visual control room on top of the OpenCode SDK — the same agent engine opencode uses.** It adds the supervision layer a single terminal lacks: parallel multi-model runs, Fusion, session goals, scheduling, diff walkthroughs, remote review. Version 1.23.2 is installed globally on the workstation (npm), so no new infrastructure is required.

| Feature | Project step |
|---|---|
| Multi-run (1 task → up to 5 models, worktree isolation) | P1 draft sprints |
| Fusion (combine strongest parts) | P3 merge input |
| Session Goals (continue toward a finish line, even with app closed) | Each section-fill session |
| Scheduled tasks (cron) | Nightly consistency audit of GDD vs decision register |
| Changes Walkthrough (AI-guided diff tour) | Review of merged backbone before G1 |
| Agent Control tool (agents create sessions from chat) | «Spin up a Sprint session for S-7 on gpt/gemini/claude» |
| Remote (browser/phone, QR + private relay) | Rule on question lists while away; end-to-end encrypted |

**One-time configuration.** Settings → Providers: paste API keys per vendor; use *Other/Custom* (base URL + key or `{env:VAR}`) for OpenAI-compatible endpoints (Ollama, LiteLLM). Settings → Agents: recreate the roster in §2 (model, temperature, standing instructions, tool rules). Agent definitions are stored through OpenCode, so they are shared with the opencode CLI — one setup, two surfaces.

**Caveats.** Single-maintainer project (fast-moving, so keep the opencode-CLI path as the control fallback); not an IDE (pair with the VS Code extension where useful); inference cost = the provider keys (the dashboard shows token use and cost per session).

## 5. Consistency & governance gates

- Spec cards are the contract. The Verifier rejects violations mechanically, not by taste.
- A terminology glossary is maintained by opencode; the Verifier checks keyword consistency across drafts.
- Provenance rules (`governance/provenance.md`) apply: `author_llm` / `assessor_llm` / `last_modified_by_llm` / dates per model; no overwriting of original authorship; unknown provenance recorded as unknown.
- **G1 and G2 are non-negotiable.** No LLM ever promotes, demotes, supersedes, or resolves rule authority. Ambiguous authority questions are escalated to the designer, never guessed.
- No authority inference from chronology, version number, filename, or detail — per repository governance.

## 6. Tool & model plan

- Control planes: OpenChamber (visual supervision, parallel runs) + opencode CLI (authoritative repository edits, merges, governance).
- Drafter pool: maximise vendor divergence — e.g. Claude + GPT + Gemini + Grok + one cheap/open model (LiteLLM / Ollama) for volume. Verifier: a strong model absent from the pool. Orchestrator: opencode's configured model.
- Fixtures: reuse existing cross-LLM playtest harnesses and exchange logs as regression material for consistency checks. Spec cards remain markdown-first to match repository conventions.
- Isolation: one git worktree per Multi-run; a single *integration* worktree for merges.

### 6.1 Disposition of the existing Tiwas LLM Router

The legacy "Tiwas LLM Router" (free-tier browser-automation orchestrator across Claude/ChatGPT/Grok, with fallback chain, broadcast/playtest mode, and a scheduler daemon) is **retired** as a drafting surface for this plan — OpenChamber's native Multi-run/Fusion and scheduled work replace it. One inherited caveat: if a valued model is reachable only through a free consumer chat UI with no corresponding OpenCode provider, the router (or equivalent) remains the only access path for that specific model; verify each router-only model against OpenCode's provider roster before fully decommissioning the router.

## 7. First-week path

- **Day 0 (designer):** open OpenChamber, connect providers, recreate the §2 agent roster.
- **Day 0 (opencode):** produce the backbone + spec cards for the first three leaf sections; designer approves the spec-card template.
- **Day 1:** first Multi-run sprint on one section (3 models) → Verifier → merge → G1 ruling → template is proven.
- **Day 2:** Session Goal + nightly scheduled audit live; second sprint; GDD conflict register opened.
- **Days 3–5:** drain the leaf queue; nightly audits; weekly checkpoint with designer question lists.
- Exit criterion: template proven on three sections → scale to the full backbone.

## 8. Failure modes

- **Contradiction drift** → killed by spec cards + Verifier contradiction reports; ambiguity escalates, never resolved by the swarm.
- **Coincident error** (several models agree on a wrong take) → 3+ model Fusion + G1 gate.
- **Token burn / open-ended drift** → Session Goals with «stop when invariant passes» limits + cost dashboard.
- **GDD blending into canonical** → provenance + G1/G2 enforcement; the GDD stays advisory.
- **Single-maintainer risk** → nothing critical lives only in OpenChamber; opencode CLI covers the same SDK.
- **Backbone mistake** → cheap and early: the nightly audit vs the roadmap re-opens a spec card before content accrues on it.

## 9. Open items / flagged guesses (recorded at v0.1)

1. GDD section scope — drafted for an *outline/backbone* target. If the GDD is intended to become a full canonical ruleset, G2 becomes the bottleneck and the pipeline phases change.
2. Verifier model pick — left open (depends on available keys); requirement is only that it is not in the drafter pool.
3. Spec-card format — markdown-first assumed; JSON/YAML machine-checkable structure may be added later.
4. Nightly scheduled audits — assumed acceptable; trivially manual if not.
5. Single-maintainer caveat on OpenChamber originates from third-party review (aireiter, 2026-08), not from OpenChamber's own documentation.
6. **v0.2 fold:** the promotion-backlog stream, governance preamble, and router disposition were folded in from `investigations/tiwas-openchamber-multi-llm-workflow-plan-2026-09-18.md` (see header change note); that advisory plan remains the read-only evidence source and is unchanged.

## 10. Lessons from the first executed loop (2026-09-19)

First full P1→P2→assessment loop executed 2026-09-18/19 on DEC-133.A R3 (seven consuming mechanics): five worktree-isolated drafter session logs → Grok fusion → two independent red-teams (opencode/big-pickle; Upstage solar-pro4:free, "Hermes") → Nemotron-3-Ultra independent assessment; all stored in `investigations/` and recorded on DEC-133.A, verdict FIT-FOR-G1. Four process fixes adopted for subsequent sprints:

1. **Tracked-session fusion.** Fusion must run inside a logged session (OpenChamber Fusion on the Multi-run sessions, or a logged opencode run) so `author_llm` is never ambiguous. Manual export-to-model fusion produced the SA-5 provenance defect (fusing model absent from the source-run list).
2. **Verifier must cite register line numbers.** The observable difference between the weak pass (findings without line references; missed the DEC-024/030 misattribution pattern, the Grappled-branch inaccuracy, and all six silent assumptions) and the strong pass (every finding pinned to register lines) was citation discipline. The §3 P2 verifier instruction now requires file + DEC/section + line references per finding.
3. **Codified P2b — independent assessment.** A second-model assessment of the verification is now a standing stage before G1 consumes findings (precedent: Nemotron-3-Ultra reply-only `opencode run --model <provider/model>`, output stored alongside). The assessor must sit outside the drafter pool, the fusion author, and the verification author.
4. **Session exports go straight to `investigations/`.** Raw run logs are stored under original filenames (raw-log precedent) at export time, never staged at repo root.

Process-only note; no rule authority changed; no DEC inferred.