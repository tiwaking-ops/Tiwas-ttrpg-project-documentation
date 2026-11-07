---
document:
  title: "Tiwas — Multi-LLM Workflow Plan: OpenChamber for Reserved-Subsystem Development and the Promotion Backlog"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. Records a chat session's tooling research and workflow plan for using OpenChamber/OpenCode in Tiwas TTRPG development; not a ruling, not a register action, and confers no authority."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
storage_note: >
  Assessed & stored by opencode / big-pickle (2026-09-18) per the
  analyze-assess-record-store workflow. Original authorship preserved;
  assessment metadata only, document substance unaltered. Advisory-only,
  non-canonical, no DEC inferred; storage & assessment confer no authority,
  supersede nothing. Assessment verdict: consistent with the live decision
  register (see the advisory annotation appended to DEC-133.A); two details
  flagged as unverified as phrased. Topical companion:
  roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md.
---

# Tiwas — Multi-LLM Workflow Plan: OpenChamber for Reserved-Subsystem Development and the Promotion Backlog

**Author:** Claude — LLM name: `Claude Sonnet 5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-18
**Document class:** Advisory tooling/workflow plan, produced in a chat session at the user's (Tiwa's) request. **Not a ruling. Not a register action. No DEC assigned or inferred. Confers no authority on anything it describes or recommends.**

---

## 0. Governance Statement

This document:

- Assigns **no DEC number** and proposes none.
- Makes **no change to Canonical Rules, Proposals/WIP, or the Implementation Roadmap**.
- Records **tooling and process planning only** — which LLM-orchestration surface (OpenChamber vs. the user's existing custom router) to use for future non-canonical content generation, not any game-mechanic content itself.
- Is stored per the same "advisory — storage record" convention used throughout `_consolidation/decision-register.md` for research/options material contributed by an LLM session (e.g. the numerous 2026-09-1x entries tagged "advisory-only, non-canonical, no DEC inferred").
- Was produced entirely from the chat session's own research and the user's stated answers; no access to the user's actual local repository, OpenChamber instance, or OpenCode configuration was available to the author LLM. Any implementation-status claims below are flagged as such.

---

## 1. Purpose and Scope

The user (Tiwa) has been running a custom-built "Tiwas LLM Router" (free-tier browser-automation orchestrator across Claude/ChatGPT/Grok, with a fallback chain, broadcast/playtest mode, and a scheduler daemon) to support Tiwas TTRPG development, with OpenCode as the downstream documentarian. The user now has the **OpenChamber** desktop application (an open-source workspace built on top of the OpenCode SDK) running locally, and asked for a researched plan on how to use it to accelerate development of the game design document, using multiple LLMs and "as many tools as possible."

This document records:

1. The interview conducted at the start of the session and the user's answers.
2. Verified research findings on OpenChamber's relevant capabilities.
3. A correction to the session's initial framing of "what's still open" in the ruleset, checked against the live decision register.
4. The resulting recommended workflow, including where it replaces the existing router and where it does not.
5. Open items not resolved by this session.

---

## 2. Session Interview — Recorded Inputs

Per the user's own requested process (interview → tailored prompt → answer), the session asked three clarifying questions before producing a plan. Answers as given:

| Question | Answer |
|---|---|
| Near-term goal for OpenChamber relative to the existing router | **Replace** the router's free-tier browser automation with OpenChamber's native Multi-run/Fusion |
| Model access budget | **Mix** — paid API keys where they clearly help, free models otherwise (not strictly free-tier like the router) |
| Current bottleneck on the game-design document | Filling in the still-open/Reserved subsystems, as framed by the user: **"S-5 through S-12"** |

These are the user's own stated constraints, not conclusions of this session, and are recorded here as the basis for the plan in §5.

---

## 3. Research Findings — OpenChamber Capabilities (verified 2026-09-18)

Findings below are from web research conducted during the session (OpenChamber's own documentation site, GitHub repository/README, and third-party coverage), not from training-data recall, since OpenChamber postdates the author LLM's reliable knowledge cutoff.

| Capability | What it does |
|---|---|
| **Multi-run** | Sends one prompt to up to five models at once, each in its own session, optionally each in its own git worktree/branch ("isolate runs" — requires a git repo). If one run fails to start, the others still launch. |
| **Fusion** | Combines the strongest parts of multiple Multi-run sessions into a new session. Available as a context-menu action on Multi-run-generated sessions. |
| **Session Goals** | Turns one prompt into a persistent objective; an independent "auditor" checks progress after every turn and keeps the agent working until the goal completes, is blocked, or hits a set budget — including after the app is closed (as long as the OpenChamber server/desktop process itself keeps running). The auditor sees only the objective text and the latest reply, not full chat history, so goal text should be self-contained. |
| **Scheduled work** | Cron-style recurring prompts, optionally run as a Session Goal so a recurring task pursues an outcome rather than stopping after one reply. |
| **Underlying engine** | OpenChamber is a UI/workspace layer on top of the **OpenCode** agent SDK/CLI — it does not replace OpenCode, it wraps it. Desktop releases bundle a matching OpenCode CLI; non-bundled installs require OpenCode installed separately. |
| **Provider/model access** | Model access is configured through OpenCode's provider system (75+ supported providers via `opencode auth login` / the `/connect` command), which supports both paid API keys and some free-tier/free-model options (including OpenCode's own hosted free models and third-party plugins that add further free routes). Reliability of third-party free-model plugins was not independently verified in this session. |

No evidence was found of OpenChamber providing direct browser-automation access to consumer chat-UI-only ("no API") models; its model roster is bounded by what OpenCode can reach as a provider.

---

## 4. Framing Correction — Actual State of "S-5 through S-12"

The user's stated bottleneck ("S-5 through S-12") does not match the live register as closely as the phrasing suggests. Per `_consolidation/decision-register.md`, most of that numbered range already carries non-canonical **Ruled** designer decisions (S-5 Armor, S-6 Defense, S-7 Incapacitation/Death, S-8 Difficulty, S-9/S-10 Extended Tests, S-11 Rest/Healing, S-12 Creature/NPC content are all Ruled, non-canonical). What remains genuinely open or deferred, as of this session, is narrower:

| Item | Status | Reference |
|---|---|---|
| Magic / Special Abilities subsystem (§15) | Reserved — Design Direction only, no rulings | Canonical §15; DEC-015 |
| Seven "consuming mechanics" (Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position, Seize/Deny Ground) | Open | DEC-133.A R3 |
| Granular Tag-to-Reaction matching | Explicitly deferred, not adopted | DEC-132.B R2 |
| Remaining per-creature Location Address templates; DEC-100-quartile-reuse-vs-bespoke calls for un-classified creatures | Open per creature (partially closed for some via DEC-144's body-plan classification rule) | DEC-112 L-004; DEC-144 |
| **Promotion of already-Ruled non-canonical material to actual Canonical status** | Not run, except DEC-017 (the sole item promoted via the full 8-step Promotion Rule to date) | Proposals/WIP §21; `governance/status-model.md` |

The last row was flagged in-session as the likely larger practical constraint: a large volume of designer-ruled, non-canonical material exists that has never been run through the 8-step Promotion Rule into the Canonical Rules & Changelog. This is a materially different kind of work (formal promotion of an already-decided item) than the first four rows (generating new candidate content for a genuinely open question), and the recommended workflow in §5 treats them separately.

---

## 5. Recommended Workflow

### 5.1 Setup (unverified against the user's actual instance)

| Step | Detail |
|---|---|
| OpenCode present | Likely already satisfied — official OpenChamber desktop releases bundle a matching OpenCode CLI |
| Point at repository | Open the local Tiwas repository as an OpenChamber project |
| Provider auth | `opencode auth login` or in-session `/connect <provider>`, per model, to satisfy the user's "mix of paid and free" requirement |
| Free-model plugins | Treat as unverified until tested; do not assume parity with the user's router in reach or reliability |

### 5.2 Multi-run + Fusion — for genuinely-open content (§4 rows 1–4)

1. Open Multi-run from the session sidebar; select the project; write one narrowly-scoped prompt (not a whole numbered subsystem — e.g. the Magic subsystem, building on the already-stored `tiwas-magic-subsystem-project-proposal-2026-09-12.md`, was suggested as a pilot); select 3–5 models.
2. Enable "isolate runs" (git worktree/branch per run) so parallel sessions cannot collide on the same files.
3. **Every Multi-run prompt should carry a fixed governance preamble**, to prevent a model from writing directly into `canonical/` or silently resolving an open fork:

   > You are producing non-canonical advisory material only. Per this project's `governance/status-model.md` and the LLM Governance Rules, your output goes into `investigations/` or `proposals/`, is never Canonical, and must not silently resolve an open designer fork. Cite existing DEC IDs from `decision-register.md` where relevant. State your evidence class (mechanical fact / empirical finding / designer ruling / recommendation) for each claim.

4. Review the resulting sessions side by side; use **Fusion** to merge the strongest parts into one consolidated options/synthesis document — mirroring the project's existing precedent of comparing multiple independently-authored advisory drafts (e.g. the eight advisory inputs compared for the Tags/Effects/Conditions unification question).
5. The human designer (Tiwa) still rules on the fused output in an ordinary session; the ruling itself is recorded in `decision-register.md` by the user, exactly as with every existing DEC. Fusion output is a better-informed draft, never a ruling.
6. For a large multi-part question, arm a **Session Goal** with a self-contained objective (the auditor never sees chat history) rather than nudging turn by turn.
7. **Scheduled work** can replace the user's custom `scheduler-daemon.js`/`schedule.js` CLI outright — e.g. a recurring consistency-audit prompt run against the decision register.

### 5.3 Promotion backlog — separate workflow (§4 row 5)

This is not a Multi-run task: there is nothing to compare, since each item already has one accepted designer ruling — it only needs the formal 8-step Promotion Rule executed and the Canonical Rules & Changelog updated to match. This is closer to ordinary single-model, repo-editing agent work than to multi-model comparison, and was flagged in-session as a better fit for a single-session, direct-repo-access tool (see §6) than for Multi-run/Fusion.

### 5.4 Disposition of the existing Tiwas LLM Router

Per the user's stated "Replace" answer (§2), the recommendation is to retire the router's browser-automation layer. One caveat was flagged and left unverified: if any model the user values is reachable only through a free consumer chat UI with no corresponding OpenCode provider (e.g. some of the router's Tier-2 custom providers, such as ChatbotAI or FaceB AI, which were flagged in the router's own build history as unverified wrappers), the router remains the only access path for that specific model. This was not checked against OpenCode's provider list in this session.

---

## 6. Tooling Recommendation

Claude Code (desktop) was suggested in-session as a complementary tool specifically for the §5.3 Promotion-backlog work — single-model, direct local-repository editing — as distinct from OpenChamber's multi-model comparison role in §5.2. This is a tooling suggestion only, not an architectural ruling.

---

## 7. Open Items / Not Resolved by This Session

- Whether OpenCode is actually installed/bundled correctly on the user's machine — not verified; based on OpenChamber's documented default behavior only.
- Reliability of third-party free-model plugins for OpenCode (e.g. the `opencode-kilocode-auth` style community plugins) — not tested.
- Whether any model currently reachable only via the router (free consumer chat UI, no API) lacks any OpenCode provider path — not checked against OpenCode's full provider list.
- No pilot Multi-run/Fusion task has actually been run yet; the Magic subsystem was suggested as a first candidate but not committed to.
- No design content, ruling, or DEC was produced or altered by this session. This document is process/tooling planning only.

---

## 8. Filing Note

Recommended location, consistent with the project's existing directory conventions (`investigations/` for evidentiary/advisory, non-self-executing material): `investigations/tiwas-openchamber-multi-llm-workflow-plan-2026-09-18.md`. Storage confers no authority; nothing in this document is Canonical or Ruled.

**End of document.**