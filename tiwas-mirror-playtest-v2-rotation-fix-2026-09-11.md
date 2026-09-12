---
document:
  title: "Mirror-Match Combat Stress Test v2 — Rotation Fix (Addendum)"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. Scaffolding fix to the playtest scenario only — proposes no Tiwas rule change. Pending Tiwa review."
  supersedes: "Scope note only — does not replace the v1 results; documents the monoculture fix and its outcome."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-11"
  requested_by: "Tiwa"
---

# Mirror-Match Combat Stress Test v2 — Rotation Fix

**Problem being fixed:** in both v1 runs, offense-skill selection ("currently
highest value") plus Failure-XP-only growth caused permanent single-skill
lock-in — only Attack fired in Run A; only Equipment Damage / Grapple fired
in Run B. 6–7 of the brief's 10 test objectives never triggered as a result.

**Scope, per Tiwa's constraints:** combatants remain identical (no
asymmetry); no new skill→Effect pairings; no new actions. The fix is
confined to the AI-selection convention only.

---

## 1. The fix

Offense-skill selection is replaced with a **fixed round-robin rotation**:
`Attack → Grapple → Trip → Disarm → Equipment Damage → repeat`, advanced
**once per turn taken** (not per internal repeat-roll — a repeat re-rolls
the *same* declared contest per DEC-013 §13.4/13.5, it isn't a fresh
declaration). Skill *value* still grows exactly as before (Failure XP /
Skill Roll Pool, unchanged); only which skill gets tested each turn is no
longer value-driven.

**This is non-canonical scaffolding for this scenario, not a Tiwas rule.**
DEC-025 already establishes that a Skill's name carries no mechanical
weight; this rotation is simply this playtest's substitute for "the actor's
tactical judgment," in the same spirit as the original "highest value"
convention it replaces — neither is a corpus rule.

---

## 2. Execution

Three independent replicate runs (dice via `random.SystemRandom()`; no
reproducible seed exists for this source, so replicates check robustness
rather than reproduce identical rolls). Full combined log:
`exchange_log_v2_rotation.csv` (384 data rows, `replicate` column
distinguishes the three runs).

| Metric | Replicate 1 | Replicate 2 | Replicate 3 |
|---|---|---|---|
| Rounds | 40 | 44 | 22 |
| Exchanges logged | 147 | 144 | 93 |
| Winner | Beta | Beta | Alpha |
| Loser's final HP | Alpha: −2 | Alpha: −15 | Beta: −8 |
| Skill usage (Attack / Grapple / Trip / Disarm / Equip.Dmg) | 24 / 38 / 23 / 34 / 28 | 31 / 26 / 31 / 31 / 25 | 12 / 29 / 19 / 14 / 19 |
| Tag-check (pass / fail-fallback / n/a) | 2 / 7 / 14 | 5 / 13 / 13 | 1 / 8 / 6 |

All five offense skills fired in every replicate, at broadly comparable
frequency (rotation guarantees this structurally — the count differences
above just reflect how many full turns each combatant got before the fight
ended, not selection bias).

---

## 3. Objective coverage (all three replicates)

| # | Objective | Governing DEC(s) | Rep 1 | Rep 2 | Rep 3 |
|---|---|---|---|---|---|
| 1 | S-1 melee-exchange algorithm | 013, 105 | ✅ | ✅ | ✅ |
| 2 | Contest-delta HP resolution | 096, 097, 104 | ✅ | ✅ | ✅ |
| 3 | Effect Tier/Magnitude = Skill-Tier | 107 | ✅ | ✅ | ✅ |
| 4 | Skill-Tier shred + margin de-escalation | 103 | ✅ | ✅ | ✅ |
| 5 | Zero-Step + Tier-1 location resolution | 014, 100 | ✅ | ✅ | ✅ |
| 6 | Tag+Location gating / fail-and-fall-back | 028, 030, 114 | ✅ | ✅ | ✅ |
| 7a | Grappled imposition | 079 | ✅ | ✅ | ✅ |
| 7b | Break-Hold escape | 124, 131 | ⛔ out of scope (no escape action exists in this scenario, per Tiwa's constraint) | ⛔ | ⛔ |
| 8 | Wound target selection | 102 | ⛔ unreachable (no skill pairs to a Wound Effect, per Tiwa's constraint) | ⛔ | ⛔ |
| 9 | Incidental Advanced Skill creation | 012 | ✅ | ✅ | ✅ |
| 10 | Armor Bypass Tier-2 path | 112, 113 | N/A — intentionally out of scope since v1 (brief §8.5), unchanged | N/A | N/A |

**Result: 8/8 reachable objectives fire in all 3 of 3 replicates.** 7b and 8
are correctly and consistently excluded rather than silently passing or
silently vanishing — they are structurally impossible under the "no new
actions / no new pairings" constraint, exactly as flagged before execution.

This directly satisfies the three success criteria set going in: reachable
objectives fire (not just theoretically possible — empirically confirmed
across 3 runs); the Grappled/Break-Hold split is reported honestly (7a
passes, 7b doesn't silently count as passed); and the fix is labeled
scaffolding throughout, not a rule proposal.

---

## 4. What this does and doesn't tell you

**Confirms:** the monoculture problem was specifically caused by
value-driven selection interacting with irreversible skill growth — not by
any flaw in DEC-103/104/105/014/100/114/030 themselves. Replacing only the
selection heuristic, with zero other changes, fully resolves it.

**Doesn't tell you:** whether round-robin is a *good* model of how a real
GM or player would actually choose actions in play — it isn't meant to be;
it's a coverage-maximizing scaffold, explicitly not a proposed Tiwas
mechanic (per DEC-025, Skill choice already carries no gating weight, so
there is no "correct" AI to model here regardless).

**Still open, unaffected by this fix:** DEC-112/DEC-113's Armor Bypass
contradiction (excluded from this scenario since v1, §8.5); Break-Hold
escape and Wound-target coverage remain untested in this scenario family —
closing those would require the scope expansion Tiwa declined this round
(new escape action, new Wound pairing), which stays available as a future,
separately-scoped addendum if wanted.

---

## 5. Files produced

| File | Contents |
|---|---|
| `mirror_playtest_v2_rotation.py` | v2 script (rotation-based selection; 3-replicate driver) |
| `exchange_log_v2_rotation.csv` | Combined per-roll log, all 3 replicates (384 rows) |
| `summary_v2_rotation.json` | Machine-readable per-replicate summary incl. objective-coverage flags |
| `tiwas-mirror-playtest-v2-rotation-fix-2026-09-11.md` | This document |

No DEC assigned. No registry action requested or implied.
