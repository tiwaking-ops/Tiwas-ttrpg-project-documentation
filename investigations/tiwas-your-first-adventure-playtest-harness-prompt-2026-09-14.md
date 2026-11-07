---
document:
  title: "Tiwas — Your First Adventure: Unattended Multi-LLM Playtest Harness Prompt (Ready-to-Fire)"
  version: "0.2"
  status: "Advisory / Non-canonical. No DEC assigned. Execution harness for automated playtest runs of tiwas-adventure-your-first-adventure-2026-09-14.md (v0.2); not a ruling, not a register action."
  purpose: >
    One copy-paste prompt that operationalizes the module (v0.2) for unattended execution by
    multiple LLMs (Claude Sonnet 5, GPT-5.6 Luna, Grok 4.5) under the Automated Playtest
    Run Conventions (H1–H8, HC-1.1–1.4, DEC-072.A) plus the module's A1–A8 conventions.
    v0.2 applies Tiwa rulings D1–D7 (2026-09-14) and DEC-140.
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  source_module: "tiwas-adventure-your-first-adventure-2026-09-14.md"
  conventions: "tiwas-automated-playtest-run-conventions-2026-09-14.md"
  precedent: "tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md"
revision_note: >
  v0.2 (2026-09-14): applies Tiwa rulings D1–D7 and DEC-140 — D1 (Bargle HP≤0 in any Scene-6
  round → Ending A immediately, climax fork SKIPPED; resolves the R2 Luna BLOCKED outcome);
  D2/D6 (Scene-1 Perception test mandatory fixed-roll 00 (=100) teaching beat creating the
  named Advanced Skill Perception (Advanced) T2 mss+mps cap50 Start 1); D3 (Zero-Step quoted
  verbatim from Canonical §14.1; zone correction LI 30/LI 42 → Torso per DEC-100 quartiles;
  no rule gap); D4 (exclusive — exactly one Effect per winning exchange); D5 (budget-expiry
  withdrawal = intended primary scene end); D7 (rewrite; no re-run until Tiwa reviews).
  Ruleset cutoff advanced DEC-139 → DEC-140.
  **v0.2 text ACCEPTED by Tiwa, 2026-09-14 (in-session): approved for playtest use; the
  document remains Advisory / Non-canonical — acceptance confers no promotion.**
---

# Tiwas — Your First Adventure: Unattended Multi-LLM Playtest Harness Prompt

**This document holds a single ready-to-fire execution prompt.** Each target LLM is an
independent provenance unit; do not merge their numerical results. Each run states its
execution settings (RNG, conventions, ruleset) in its own report.

---

## 0. Governance Statement

- Assigns **no DEC number** and proposes none.
- Runs under this prompt are **advisory / non-canonical execution records**; no report
  produced by this harness triggers a ruling, promotion, demotion, or register action.
- The harness fixes execution conventions (module A1–A8 + H-conventions) for
  cross-comparable unattended runs only. Table play and GM discretion (DEC-070/074) are
  untouched.
- Provenance: authored by OpenCode (`opencode`, `big-pickle`) in a single pass;
  single-model authorship carries no authority.

---

## 1. Target LLMs and Run Logistics

| Run | Target LLM | Expected artifact |
|---|---|---|
| R1 | Claude Sonnet 5 (`claude-sonnet-5`) | `investigations/tiwas-your-first-adventure-playtest-execution-claude-2026-09-14.md` |
| R2 | GPT-5.6 Luna | `investigations/tiwas-your-first-adventure-playtest-execution-luna-2026-09-14.md` |
| R3 | Grok 4.5 (`grok-4.5`) | `investigations/tiwas-your-first-adventure-playtest-execution-grok-2026-09-14.md` |

Each run is exercised independently with the same prompt; logs/rolls CSVs are welcomed but
must be referenced and, if desired, stored beside the report. The module, this harness, and
the conventions file are all inputs a run must not modify.

---

## 2. The Ready-to-Fire Prompt

Copy this block verbatim to each target LLM.

```text
TIWAS — UNATTENDED MULTI-LLM PLAYTEST EXECUTION
TASK: EXECUTE and CERTIFY "Tiwas — Adventure Module: Your First Adventure" (advisory v0.2) end to end.

[A] PRE-INJECTION (execute in this order)
1. Read the module (investigations/tiwas-adventure-your-first-adventure-2026-09-14.md) in full.
2. Ruleset applied — STATE exactly, in your report frontmatter: Canonical Rules v1.4 +
   Decision Register through DEC-140 (incl. DEC-132/132.A/132.B, DEC-135, DEC-136–139,
   DEC-072.A amendment) + Automated Playtest Run Conventions 1.1 (H1–H8, HC-1.1/1.2/1.4)
   + module Run Conventions A1–A8. Cross-version comparisons are valid only within the
   same stated block.
3. Initialize the full 24-attribute stat blocks with the module's derived values verbatim.
   Do not edit, "fix," or reinterpret. RNG: random.SystemRandom() (fresh entropy).
4. Adopt A1–A8. Confirm each in one bullet in your report.

[B] NARRATOR CONTRACT
5. Narrate only what mechanics have resolved; resolution precedes description; never narrate
   a free hit, a "bloodied" threshold, a morale check, charm, poison, or an invisible ambush
   into mechanical advantage. Those are module-flagged: represent them exactly as the module
   does (contested S-1 / declared Wound / narrated beat).
6. When the module gives a worked example, follow the procedure, never the numbers — EXCEPT
   the Scene-1 Perception teaching beat, whose natural roll is FIXED at 00 (=100) by module
   text (D2/D6): execute that fixed roll exactly and create the named Advanced Skill
   Perception (Advanced) T2 mss+mps cap50 Start 1.
7. Every d100 is rolled and logged (fixed-roll teaching beat logged as "fixed 00"). Every
   Outcome, Cost, Overflow, Failure-XP/cascade, and Recovery value appears in your log;
   clamping and live recalculation (DEC-004, incl. the 452→449 and 615→612 and 624→621 steps)
   are shown where triggered.
8. Timestamp the phases. Keep a running character-state line after each exchange.

[C] SAMPLER RULES (determinism contract)
9. Core Test = the 9-step DEC-006 transaction (roll, Cost=natural roll to domain pool,
   Overflow→self-HP, Outcome, Margin, Failure XP → Skill Roll Pool cascade, Recovery,
   completion, restore) in exactly that order (H7). S-1 = margin contest: Margin =
   max(0, skill − roll); higher wins; ties = reroll ≤3 then defense holds.
10. Turn order Speed-desc (DEC-095), ties bss then bsp then reroll. ONE substantive
    exchange per combatant per round (A1). Movement = free/bundled (DEC-082).
11. Effect selection follows A8 rotation and is EXCLUSIVE (D4): exactly ONE declared Effect
    per winning exchange; contest resolves that Effect's magnitude only; NO sequential or
    compound multi-Effect path from a single win. Effects resolve via DEC-103 shred
    (+1 per attacker-Tier over defender-Tier), de-escalation (defender margin), and the
    DEC-100 quartiles + parity for Tier≥2 production. Records in DEC-115/117 schema.
12. Clamp HP restores at current max (HC-1.2) — never above. Sum applicable penalty
    magnitudes (HC-1.1) and apply only per DEC-072.A targeting (named Skill or governing
    Attribute).
13. Aleena-survives invariant (A4): if her resolved HP would cross 0, record the resolved
    outcome, clamp to 1, and narrate collapse. State that you did so if it happens.
14. Scene budgets: Sc.1 ≤6 rds, Sc.2 ≤5 rds (Snake acts first), Sc.4 fallback ≤3 rds,
    Sc.6 ≤3 rds + climax fork. Budget-expiry withdrawal is the PRIMARY end (D5); HP≤0
    (DEC-052, negative persists DEC-108) is the secondary end, whichever occurs first. No
    invented intermediate thresholds.
15. Advanced-Skill forcing is limited to the Scene-1 Perception teaching beat only (D2/D6,
    fixed roll 00): resolve it deterministically. Do NOT force any other failed Double; if one
    occurs naturally on Rowan's Attack, resolve Power Strike per the module's worked example;
    otherwise record "not exercised — probabilistic."

[D] ENDING SELECTION (D1)
16. If Bargle reaches HP≤0 in ANY Scene-6 round → ENDING A immediately; the climax fork is
    SKIPPED; do NOT resolve Beguile vs Composure (Bargle is down — attrition decided the
    scene, no fork). Otherwise, after Scene 6 Round 3, resolve the climax S-1:
    Beguile 27 vs Composure 23. Win → ENDING A (then resolve the decisive exchange);
    Loss → ENDING B. A drawn fork rerolls ≤3; final tie → ENDING A. Continue narration for
    the chosen ending, including treasure and aftermath per module. If Bargle reaches HP≤0
    exactly on the decisive-exchange step of Ending A, record him incapacitated per DEC-052.

[E] GRANULAR EVALUATOR (report contract)
17. Structured report with: (i) frontmatter (document/status advisory-non-canonical;
    provenance: execution_llm, created_date, conventions/ruleset applied, RNG, any
    conventions you altered and why); (ii) initial-state confirmation table;
    (iii) per-scene exchange logs (the C-block fields); (iv) final state per combatant;
    (v) coverage matrix vs the module's GM Coverage Checklist (PASS/PARTIAL/NOT EXERCISED)
    with one-line evidence each — the 100-Fumble and Advanced-Skill rows should go PASS
    (Sc.1 fixed teaching beat); (vi) module-correction compliance check (Perception
    domains charged MP; Body-Wound HP recalcs shown; no "cosmetic" Wound claim;
    Zero-Step per Canonical §14.1 verbatim); (vii) findings (open items for Tiwa only —
    never resolved by you); (viii) artifact-class: advisory/non-canonical, no DEC assigned.
18. Hard boundaries: no DEC inference, no promotion/demotion/supersession, no invented
    rules, no rule-edit anywhere, no edits to the module file; corrections and open items
    are reported, never silently applied. Treat your run as its own provenance unit.
19. Delivery: report artifact
    investigations/tiwas-your-first-adventure-playtest-execution-<model>-2026-09-14.md
    (+ rolls/effects logs if scripts used). Do not overwrite other runs' artifacts.
    Reply with (a) the report, (b) your 3-line executive summary, (c) any flagged guesses.
```

---

## 3. Usage Notes

- **Compare only within the stated block:** healing amounts and HP trajectories are
  comparable between runs only when both state Conventions 1.1 + A1–A8 and the same ruleset
  cutoff (through DEC-140).
- **Divergence is expected** (roll variance, probabilistic A6 branch, random DEC-102 target
  selection). The harness's purpose is to make the *procedure* identical so divergence is
  attributable to rolls, not interpretation — the collation (§4) failure mode this fixes.
- **Post-run collation:** a follow-up collation comparing the three execution reports should
  mirror `tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md`
  (convergent findings, divergent findings → Tiwa escalation, factual-discrepancy list).
- **Baseline note (§10 of conventions):** if any run alters an execution-level setting, it
  must state so in frontmatter (RNG, action economy, H-convention reuse) or the result is
  not cross-comparable.

---

**End of document.**