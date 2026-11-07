---
document:
  title: "G5 Seven Consuming Mechanics — Spec Card (DEC-133.A R3)"
  version: "1.0"
  status: "Spec card (non-canonical advisory)"
  provenance:
    author_llm: {name: "north-mini-code-1-0", version: "cohere/north-mini-code-1-0"}
    assessor_llm:
      - {name: "not established", version: "not established"}
    last_modified_by_llm: {name: "north-mini-code-1-0", version: "cohere/north-mini-code-1-0"}
    created_date: "2026-09-19"
    last_modified_date: "2026-09-19"
    note: "Spec card for the G5 seven-consuming-mechanics section (DEC-133.A R3). Non-canonical advisory material only. No DEC inferred. Nothing herein is Canonical."
  storage_note: "Created as part of the multi-LLM GDD pipeline P0 backbone. Spec card serves as the contract for P1 drafting."
---

# G5 Seven Consuming Mechanics — Spec Card (DEC-133.A R3)

**Status:** Spec card (non-canonical advisory). Candidate rules text for the seven consuming mechanics left open by **DEC-133.A R3**. Fused from five independent multi-LLM runs; no DEC is inferred or resolved hereby; nothing here is promoted, demoted, or superseded.

**Purpose.** Provide candidate implementations for: **Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position resolution, Seize/Deny Ground resolution**. Each candidate must (a) be expressible as rules text, (b) carry an evidence class per claim, (c) present open designer forks rather than silently collapsing them.

---

## 0. Scope, constraints, and shared substrate

### 0.1 Locked constraints any candidate must survive

| Constraint | Source | Implication for candidates |
|---|---|---|
| **Invariant 6** — Cost = natural roll | Canonical §16 | Every contested resolution is a full Core Test (DEC-006); natural d100 is never modified. Distance multipliers are position accounting, not a second Cost channel that violates the invariant, but they interact with the open consumption fork. |
| **Invariant 17** — no competing resource pools | Canonical §16 | No stored movement tokens, per-scene counters, or second progression channel. Only natural-roll Cost + ephemeral per-turn Movement Distance allowance. |
| **Invariant 18** — build on Core Test | Canonical §16 | No separate “movement engine.” Chase, ZoC contests, Disengage contests, etc. are S-1 (DEC-013). |
| **DEC-024 / DEC-030** | Designer ruling | One Effect per win; no graded outcomes. Forced Movement, Pin/Hold, Seize/Deny are mutually exclusive selections unless DEC-026 cash-out is engaged. |
| **DEC-123** — “never total” | Designer ruling | Never veto action declaration. Express denial as Effective Movement Speed = 0 / −Y or as a contested roll that must be won. |
| **DEC-082.A R2** | Designer ruling | Movement-denial × Movement Speed question is closed. Pin/Hold must reuse existing Condition stack (DEC-122/123/124/126/131), not reopen it. |
| **DEC-095** | Designer ruling | Movement is free/bundled side-activity; one substantive action per turn. |
| **DEC-133 Hybrid** | Designer ruling | Movement Distance = Effective Movement Speed (1 MS = 1 hex/turn). Band model remains; band↔hex boundaries are content-authoring (DEC-077.A). |

[EC: mechanical fact for Invariants; designer ruling for listed DECs]

### 0.2 Shared design substrate

- **Geometry:** All positional payloads stated in hexes with parenthetical band reading. Exact band names/widths = content. [EC: designer ruling — DEC-133 / 133.A R1]
- **Resolution:** Every meaningful contest is a full S-1 opposed contest (DEC-013) with normal Cost, Overflow, Failure XP, Doubles, Recovery. [EC: mechanical fact]
- **Effect selection:** Winner selects **one** Position-tier Effect their Skill-Tier permits (DEC-107: Effect Tier = causing Skill-Tier). Quality is success precondition / tie-break, not a magnitude dial. [EC: designer ruling]
- **Reactions:** Movement-triggers are a ruled category (DEC-132.A R1); exact Tags and eligibility are content-authoring (DEC-077.A).

### 0.3 Shared open forks (must NOT be resolved by this draft)

1. **Fork C — contested-movement consumption (DEC-133.A R2):** Does a failed movement contest consume the mover’s remaining Movement Distance allowance for the turn, only the distance already travelled, or nothing beyond the natural-roll Cost?
2. **Fork G — generic movement contest skill/payload:** Which Skill lineages and what payload selection rules apply to the shared primitive?
3. **Fork T — additional Skill-Tier gate on Position-tier Effects:** Does Position-tier require only the DEC-023.A unlock, or an extra Skill-Tier threshold?

These remain open. Candidates below present options without collapsing them.

---

## 1. Dependency chain

**DEC+line links:**
- DEC-133.A R3 (primary decision reference)
- DEC-023.A (Position-tier Effects unlock)
- DEC-133 (Movement Distance = Effective Movement Speed)
- DEC-095 (Movement free/bundled side-activity)
- DEC-082.A R2 (Pin/Hold must reuse existing Condition stack)
- DEC-123 (Never total action declaration)
- DEC-024/DEC-030 (One Effect per win; no graded outcomes)

**Open questions (from verification chain):**
- 14 designer questions from big-pickle verification report (Disengage shape, ZoC shape, Chase shape, etc.)
- U-series items (U-1–U-11, excluding U-3/U-4/U-5 ruled)
- SA-5/E5 provenance divergence (frontmatter author_llm mismatch)

**Locked invariants:** 6, 17, 18 (from Canonical §16)

**Ruled constraints (2026-09-19):**
- DEC-147: Movement Distance ephemeral per turn, never stored/banked/tracked per scene; mid-turn MS change: remaining = effective MS at query − hexes spent, floored at 0; no debt; rises grant movement
- DEC-148: DEC-133.A R3 means "consuming mechanics operating on the Position-tier substrate," not "added to the DEC-023.A alpha list"

---

## 2. Evidence-class discipline

Every claim in the candidate text must be tagged with one of:
- **mechanical fact** (invariant existence, Core Test structure, DEC-013 S-1 primitive)
- **empirical finding** (verification report findings, contradiction classifications)
- **designer ruling** (DEC-082.A R2, DEC-095, DEC-133, DEC-123, DEC-024/DEC-030)
- **recommendation** (candidate options, alternative framings, open fork preservation)

**Governance preamble (verbatim):**

> You are producing non-canonical advisory material only. Per this project's `governance/status-model.md` and the LLM Governance Rules, your output goes into `investigations/` or `proposals/`, is never Canonical, and must not silently resolve an open designer fork. Cite existing DEC IDs from `decision-register.md` where relevant. State your evidence class (mechanical fact / empirical finding / designer ruling / recommendation) for each claim.

---

## 3. Designer fork preservation requirement

**No fork resolution:** The draft must preserve rather than collapse:
- Fork C (contested-movement consumption)
- Fork G (generic movement contest skill/payload)
- Fork T (extra Skill-Tier gate on Position-tier Effects)
- Per-mechanic shape forks (Disengage D-A/D-B/hybrid; ZoC Z-A/Z-B/Z-C; Chase K-A/K-B; Forced Movement F-A/F-B/F-C; Pin P-A/P-B; Seize G-A/G-B/G-C)

**No DEC inferred:** All seven consuming mechanics remain carried-open as Position-tier Effects under DEC-023.A / DEC-133.A R3, exactly as the register establishes.

**Non-canonical advisory only:** Nothing herein is Canonical; no DEC is inferred; no authority is changed by this record.

---

## 4. Open designer questions (to be ruled by Tiwa)

**From verification chain:**
1. Disengage shape (D-A/D-B/hybrid; Skill lineages; failed exit consumption)
2. Zone of Control shape (Z-A/Z-B/Z-C; stack with Seize/Deny; default coverage)
3. Chase shape (K-A binary vs K-B margin track)
4. Generic movement contest Skill/payload (Fork G)
5. Forced Movement magnitude (F-A/F-B/F-C; DEC-107 consistency)
6. Pin/Hold vector (P-A full Restrained vs P-B lightweight)
7. Seize/Deny shape (G-A/G-B/G-C)
8. Fork C (contested-movement consumption)
9. Fork T (extra Skill-Tier gate on Position-tier Effects)
10. ZoC ↔ Seize/Deny relationship
11. Default Skill families for movement contests
12. Duration defaults for pins and ground claims
13. ZoC Z-A distance multiplier invariant status
14. Pin/Hold Condition-stack reference precision

**From U-series:**
- U-1: Z-A per-hex accounting rule on a zone-scoped record vs Tier-Y overlay on the mover
- U-2: Z-A floor clause preserving DEC-125 guarantee
- U-6: Whether Open/Close Lane is a silent eighth consuming mechanic
- U-7: Whether Disengage is a distinct Effect or maps to Base-tier Open Retreat / Compel Yield
- U-8: How Pin/Hold Position differs from Grappled
- U-9: Definition of Restrained's "Break Free" mechanism
- U-10: Relationship between ZoC and `reaction:vigilant` movement-trigger Reaction
- U-11: Whether Z-A and Disengage double-charge the same movement

**From SA-5/E5 divergence:**
- Frontmatter author_llm "grok-fusion" does not match §11 source-run list
- Nemotron E5-CONFIRM: frontmatter records author/assessor honestly — covered

---

## 5. DEC-147/148 corrections (applied)

**DEC-147 (RULED):**
- Movement Distance is derived per turn from live effective MS; never stored/banked/tracked per scene
- Mid-turn MS change: remaining = effective MS at query − hexes spent, floored at 0; no debt; rises grant movement
- Ephemerality is locked — stop flagging as assumption

**DEC-148 (RULED clarification):**
- DEC-133.A R3 means "consuming mechanics operating on the Position-tier substrate," not "added to the DEC-023.A alpha list"
- Do not route every mechanic through a Position-tier Effect selection unless its own design requires it

---

## 6. Storage and provenance

**File location:** `investigations/tiwas-g5-seven-consuming-mechanics-spec-card-2026-09-19.md`

**Provenance requirements:**
- author_llm: north-mini-code-1-0 (this spec card)
- assessor_llm: not established (independent assessment pending)
- last_modified_by_llm: north-mini-code-1-0
- created_date: 2026-09-19
- last_modified_date: 2026-09-19

**Evidence-class per claim:** Every claim in the candidate text must be tagged with EC: [mechanical fact / empirical finding / designer ruling / recommendation]

**No fork resolution:** All open designer forks preserved
**No DEC inferred:** Nothing herein is Canonical
**Non-canonical advisory only:** Placement in `investigations/` is appropriate; neither storage nor assessment confers authority

---

**End of spec card.** This document is non-canonical advisory material. It does not create game mechanics, does not close any open designer fork, and does not promote any draft or finding.
