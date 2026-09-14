---
document:
  title: "Tiwas — Automated Playtest Run Conventions"
  version: "1.1"
  status: "Advisory / Non-canonical. No DEC assigned. Records a single designer-approved conventions block (H-rule set) scoped to automated playtests only. HC-1.1/1.2/1.4 confirmed 2026-09-14; HC-1.3(b) DEC-072.A amendment applied to register 2026-09-14."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  rulings:
    - "Tiwa (human), 2026-09-14 — H1(a) HP = accumulated Margin (adopted); H2–H8 approved; H4 Option 2 (targeted penalty) ruled"
    - "Tiwa (human), 2026-09-14 — HC-1.1 (sum all applicable penalty magnitudes), HC-1.2 (clamp at current HP max), HC-1.4 (filing location) confirmed; HC-1.3(b) approved (draft DEC-072 amendment text)"
  source_module: "tiwas-adventure-the-bargle-incident-2026-09-13.md"
  collation_report: "tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md"
---

# Tiwas — Automated Playtest Run Conventions

**Prepared by (Author):** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Document class:** Advisory conventions block for unattended/automated playtest executions. Records designer-approved (H1–H8) conventions. Not a proposal, not a Decision Record, not a canonical or non-canonical rule change.

---

## 0. Governance Statement

This document records a single, consolidated block of conventions — labelled the **"Automated Playtest Run Conventions"** — adopted by Tiwa (human, sole ruling authority) on 2026-09-14, following the cross-LLM collation of three playtest executions of **The Bargle Incident** (`tiwas-adventure-the-bargle-incident-2026-09-13.md`; see `tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md`).

This document:

- Assigns **no DEC number** and proposes none.
- Is **scoped to automated/unattended playtest runs only**. It does **not** alter tabletop/GM-discretion play, DEC-070 (GM-discretion completion target), DEC-074 (no HP-deficit lock), or any other table rule.
- Promotes **nothing**; no authority change is requested or implied.
- Records **HC-1 as confirmed 2026-09-14:** HC-1.1 (sum all applicable penalty magnitudes), HC-1.2 (clamp at current HP max), and HC-1.4 (filing location) are ruled; HC-1.3(b) approved (draft the DEC-072 amendment text — register application happens only after Tiwa approves the wording).
- References but does **not** implement the **DEC-072 clarifying amendment** (blanket → targeted penalty wording), which is a separate register action requiring Tiwa's explicit direction (see §6 and §8).

**Provenance note per `governance/provenance.md`:** this document was authored, assessed, and last-modified by the same model (OpenCode `big-pickle`) in a single pass. A single-model self-assessment is a weaker form of review than an independent second pass; it is recorded honestly as such and confers no authority. The rulings recorded here are Tiwa's human decisions, not LLM decisions.

---

## 1. Purpose and Scope

Three independent playtests (R1 Claude Sonnet 5, R2 GPT-5.6 Luna, R3 Grok 4.5) operationalized the same open S-11 boundary (DEC-074 GM-discretion healing amount) in three different ways as unattended simulations. To make automated-run results deterministic and cross-comparable, this block fixes the conventions an automated run must follow. It applies **only** where no GM is present to adjudicate; it never overrides a GM-discretion decision in a human-run game.

| Convention | Applied to |
|---|---|
| H1–H8 (this block) | Automated playtest executions of Tiwas adventure modules (primary reference: The Bargle Incident) |
| Tabletop / GM-run play | Excluded — DEC-070 / DEC-074 GM discretion governs |

---

## 2. Authority Record

| ID | Ruling / approval | Authority | Date |
|---|---|---|---|
| H1(a) | Automated rest heal: **HP restored = accumulated Margin**, capped at current HP max | Tiwa (adopted) | 2026-09-14 |
| H2 | Completion target = **fixed 40 Margin** (adjustable per playtest) | Tiwa | 2026-09-14 |
| H3 | Healing skill = **module-designated only** (Devotion here); **MP-domain cost = natural roll**; **HP-only restore**; **cost ≠ restore** | Tiwa | 2026-09-14 |
| H4 | **Targeted penalty** — Wound/Effect penalizes healing only if it names the healing skill or its governing attribute; DEC-072 needs a clarifying amendment | Tiwa | 2026-09-14 |
| H5 | **Wound-record healing excluded** from automated scope initially (Wounds/Effects must be actively healed/removed) | Tiwa | 2026-09-14 |
| H6 | **Revival / negative HP: terminal** for this playtest | Tiwa | 2026-09-14 |
| H7 | **Lock the interval accounting order** (module's sequence, §7) | Tiwa | 2026-09-14 |
| H8 | **Record as a single "Automated Playtest Run Conventions" block** | Tiwa | 2026-09-14 |
| HC-1.1 | Multiple applicable Wound/Effect penalty magnitudes on a healing test | **Sum all magnitudes.** Effect Tier = difficulty of healing/removing; Magnitude = the numerical effect amount | Tiwa | 2026-09-14 |
| HC-1.2 | H1(a) restore clamp | **Clamped at current HP max** — cannot heal above a character's maximum HP | Tiwa | 2026-09-14 |
| HC-1.3 | DEC-072 amendment | **Option (b)** — amendment drafted (§12), approved by Tiwa, applied to the register as **DEC-072.A** | Tiwa | 2026-09-14 |
| HC-1.4 | Filing location | **Standalone advisory document in `investigations/`** (this file) + register advisory annotation (applied with the DEC-072.A update, after wording approval) | Tiwa | 2026-09-14 |

All entries are **non-canonical ruling/approval records**, consistent with the repository's Ruled (Non-canonical designer ruling) register convention. Nothing in this table is canonical and nothing is promoted.

---

## 3. H1(a) — Automated Healing Amount

During an automated playtest Rest/interlude (an S-11 Extended Test instance per DEC-073), when the completion target is reached:

> **HP restored = accumulated Margin (sum of successful intervals' Margin), capped at current HP max.**

- The cap uses the **current** HP max (post-Wound live recalculation per DEC-004/DEC-102).
- Restoration is **HP-only**; MP/PE recovery remains with the Recovery mechanic (DEC-008), never with healing.
- Restoration does **not** heal Wounds or Effects (see H5 — wound-record healing is out of automated scope initially).

**Note:** this is a *playtest-run convention*, adopted for unattended determinism. It is **not** a ruling that the tabletop GM must restore Margin-for-Margin; DEC-074 GM discretion is untouched at the table.

---

## 4. H2 — Completion Target

- **Default: fixed 40 accumulated Margin.**
- The value 40 is the module's own worked-example target and was demonstrated end-to-end (R1 completed at Margin 43 in 8 intervals; worked example completes at 51).
- It is **adjustable per playtest** — a convention constant, not a formula and not tied to HP deficit (respects DEC-074's no-HP-deficit-lock intent, and DEC-070's "no fixed default" applies to table play, not to this automated convention).

---

## 5. H3 — Healing Skill, Cost, and Restored Pool

| Item | Convention | Rationale / evidence |
|---|---|---|
| **Skill** | Module-designated healing skill only (here: **Devotion**, Skill 32 start). Extendable to "any skill the module explicitly designates as healing" in future modules | Deterministic skill selection for unattended runs |
| **Cost** | One ordinary Core Test per interval (DEC-071/DEC-073); **cost = the natural d100 roll, in the skill's resource domain = MP** (Devotion is `mee`-Mind-domain; DEC-003/DEC-007) | Module interlude charges MP (12+25+41+8 = 86); Perception precedent routes Mind-domain to MP |
| **Restored pool** | **HP only.** Never MP or PE | Recovery (DEC-008) handles MP/PE |

### 5.1 Confirmed: MP cost ≠ HP restored

Approved as a property of the system, not an anomaly:

- **MP cost** = natural roll per interval, paid every interval (win or lose; DEC-068 failures still cost).
- **HP restored** = accumulated **Margin** over successful intervals, paid once at completion (H1(a)).
- Margin `= effective Skill − roll` is bounded by the skill's value (~32 Devotion start), while a roll can reach 99; the transaction is **lossy by design** (resources consumed during, quality-based restore at end).

| Run | MP spent (sum of rolls) | Margin total → HP restored |
|---|---:|---:|
| Module worked example | 86 | 51 |
| R1 (Claude) | 8 intervals, large rolls | 43 |

---

## 6. H4 — Wounded-Healer Penalty (DEC-072) — Targeted Reading

**Ruling (Tiwa, 2026-09-14):** option 2 — **targeted penalty**:

> A Wound or Effect penalizes healing **only if its record names the healing skill directly or its governing attribute** (e.g., `mee`/Resolve → Devotion). Otherwise the heal is **unaffected**.

**Designer rationale (recorded verbatim):** "The previous wording was created before the creation of the Skill Tier Effect System. Unless the Wound or Effect affects the skill, then Wounds or Effects will never cause a penalty. If a Wound affects a skill, that skill will never be penalized. Wounds or Effects on underlying Attributes will cause a reduction in all related Skills."

Mechanically:

- **Skill-targeted** Wound/Effect → that Skill drops by magnitude Y; the heal uses the reduced Skill.
- **Attribute-targeted** Wound/Effect → the Attribute drops by Y (DEC-035.A/DEC-102 record target; DEC-004 live recalculation); every **related** Skill (formula uses that attribute) drops accordingly.
- **Unrelated** Wound/Effect (e.g., `mpp`/Wits wound vs a `mee`-based heal) → **no healing penalty.** R1/R2's Aleena Wounds are `mpp`-targeted; under the targeted reading they do **not** penalize her Devotion heal.

**DEC-072 clarifying amendment (applied 2026-09-14 as DEC-072.A):** DEC-072's original wording ("Wound magnitude penalizes the healer's EFFECTIVE Skill for the healing test") was blanket and predated the Skill Tier Effect System. Per HC-1.3(b) the amendment text was drafted (§12), approved by Tiwa, and applied to the decision register as **DEC-072.A** on 2026-09-14, implementing the targeted reading below.

---

## 7. H7 — Locked Interval Accounting Order

Each Rest interval is a **full, ordinary 9-step Core Test Transaction** (DEC-006; DEC-071; DEC-073), executed in this exact order:

1. **Roll** d100 against **effective** healing Skill (post-H4 penalties).
2. **Cost** = natural roll, paid from the skill's domain pool (MP).
3. **Overflow check** (DEC-007): if cost > current pool, the shortfall is **self-HP overflow** damage.
4. **Outcome:** success if roll ≤ effective Skill.
5. **On success:** Margin = effective Skill − roll; **add to accumulated total** (DEC-067).
6. **On failure:** Failure XP = max(0, roll − effective Skill) → Skill Roll Pool cascade (DEC-009/DEC-010); **no** Margin added, **no** progress loss (DEC-068).
7. **Recovery** (DEC-008): pool += `floor(Regen/2)` (= 57 for Aleena), clamped at the **current** pool max.
8. **Completion check:** accumulated Margin vs target 40 (H2).
9. **On completion:** apply H1(a) — restore HP = accumulated Margin, capped at current HP max. Intervals stop.

This is a restatement of the module's interlude worked example in full-transaction form; the module's compressed table lists only cost + recovery, which is why the sequence is written out for automation.

---

## 8. HC-1 — Confirmed Entries (2026-09-14)

All four HC-1 items are resolved by Tiwa:

| # | Item | Ruling |
|---|---|---|
| HC-1.1 | Multiple applicable Wounds/Effects on the healer — penalty accumulation | **Sum all applicable magnitudes.** Designer rationale: Effect Tier is the difficulty of healing/removing the effect; Magnitude is the numerical effect amount (magnitudes sum for the effective-Skill penalty) |
| HC-1.2 | H1(a) restore cap | **Clamped at current HP max** — cannot heal above a character's maximum HP |
| HC-1.3 | DEC-072 amendment | **Option (b)** — drafted (§12), approved by Tiwa, and **applied to the register as DEC-072.A** (2026-09-14); DEC-072's status now reads `Ruled (amended by DEC-072.A)` |
| HC-1.4 | Filing location | **Agreed: standalone advisory document in `investigations/`** (this file), cross-referenced as an advisory storage annotation in the decision register (applied with DEC-072.A once wording is approved) |

---

## 9. Adopted-but-Out-of-Scope Conventions

- **H5 — Wound-record healing:** the automated Extended Test never heals Wounds or removes Effects during this playtest. Wounds and Effects must be **actively healed or removed** as a separate, conscious action; they are out of the automated-rest scope initially.
- **H6 — Revival / negative HP:** for this playtest, a combatant at HP ≤ 0 (forced incapacitation per DEC-052; negative-HP persistence per DEC-108) is **terminal** for the automated run. No revival mechanic is exercised, invented, or assumed.

---

## 10. Notes for Future Automated Runs

- **Baseline for comparisons:** future automated runs should state their convention version ("Automated Playtest Run Conventions 1.0") and their execution-level settings (RNG, action-economy reading of DEC-106, and reuse/alteration of H1–H8). Healing amounts are comparable between runs **only** when both use H1(a).
- **Module corrections:** carry the module-side flags already raised in the storage assessment and collation (Scene 1 PE→MP domain error; Bargle "cosmetic" bps Wound; Power Strike Cap 55-vs-59; R1 `initial_state` snapshot semantics). Do not silently patch these in a stored run record.
- **Re-run baseline:** **R1** (Claude) is the current adopt-as-reference interlude execution under H1(a). Re-running the interlude with the locked conventions (H1(a)+H2+H7) is an open follow-up; not required for this document.

---

## 11. OpenCode Action Boundary

1. Store this document as an **advisory / non-canonical investigation artifact**.
2. Do **not** infer, assign, or request a DEC.
3. Do **not** promote or demote anything on the basis of this document.
4. **DONE (2026-09-14):** DEC-072.A applied to the decision register and the advisory storage annotation added per HC-1.4, after Tiwa approved the §12 wording.
5. Convention text is fully locked per the HC-1 confirmations recorded in §2 and §8.

---

## 12. DEC-072.A — Wound/Effect Healing Penalty: Targeted Reading (Amendment to DEC-072)

Drafted per HC-1.3(b) and **applied to the decision register as DEC-072.A on 2026-09-14** following Tiwa's approval. DEC-072's Status column reads `Ruled (amended by DEC-072.A)`; DEC-072's original verdict text is preserved per register amendment convention.

**Proposed register row (matches the `_consolidation/decision-register.md` column format):**

> | DEC-072.A | S11-B — Wound magnitude healing penalty: targeted attribute/skill alignment (**AMENDMENT to DEC-072**) | **RULED — Targeted penalty.** A Wound or Effect penalizes a healing Skill test **only if its record names that Skill directly or its governing Attribute**; otherwise the test is unaffected. A Skill-targeted Wound/Effect reduces that Skill by its magnitude Y. An Attribute-targeted Wound/Effect reduces the Attribute by Y (DEC-035.A/DEC-102 record target; DEC-004 live recalculation) and thereby every related Skill whose formula uses that Attribute. Where multiple applicable records bear on the same test, their magnitudes **sum** — Effect Tier is the difficulty of healing/removing the effect; Magnitude is the numerical effect amount. Supersedes DEC-072's blanket wording ("Wound magnitude penalizes the healer's EFFECTIVE Skill for the healing test"), which predates the Skill Tier Effect System and would otherwise let unrelated Wounds/Effects (records that neither name the healing Skill nor its governing Attribute) penalize the heal. Penalty touches the healer's effective Skill only — never the natural roll, the resource Cost, or the HP amount restored directly (DEC-064 S8-B pattern retained). | Designer ruling (amendment), 2026-09-14 (Tiwa, following the cross-LLM Bargle Incident playtest collation); confirmed by Tiwa to OpenCode | Non-canonical designer ruling (amendment) | Ruled |

**Optional companion note (for Tiwa's awareness, not part of the amendment):** the underlying principle — a Wound/Effect penalizes a test only when its record names that Skill or a governing Attribute — generalizes beyond healing to any Skill test. If Tiwa wants that stated as a general penalty-model rule rather than only within the healing amendment, that is a separate, larger register item to raise separately.

---

**End of document.**

**Author:** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Classification:** Advisory conventions block — Automated Playtest Run Conventions 1.1, No DEC assigned