---
document:
  title: "Tiwas — G5 Seven Consuming Mechanics: Remaining Open Items (U-1–U-11, 14 Mechanics Questions, SA-5/E5 Divergence)"
  version: "1.0"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  assessor_llm:
    - {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  provenance_note: "Compiled from the stored G5 advisory chain for designer review (intended next reader: Claude, second-model check). No new findings; statuses updated for DEC-147/DEC-148 (ruled 2026-09-19). Advisory only; confers no authority."
---

# G5 Seven Consuming Mechanics — Remaining Open Items (2026-09-19)

**Status:** Advisory working document. **Nothing herein is Canonical; no DEC is inferred; nothing is ruled, promoted, or resolved by this record.**

## 0. Purpose and scope

Consolidates every item from the G5 seven-consuming-mechanics chain (DEC-133.A R3) that remains open after Tiwa's 2026-09-19 rulings (DEC-147 ephemerality lock; DEC-148 R3 substrate clarification). Three groups: the U-series from `investigations/tiwas-g5-fusion-review-items-1-5-advisory-report-2026-09-19.md` §9, the 14 mechanics questions from `investigations/tiwas-g5-seven-consuming-mechanics-verification-chat-report-2026-09-19.md` §3.3 (confirmed open by `investigations/tiwas-g5-seven-consuming-mechanics-independent-assessment-2026-09-19.md` §3), and the SA-5/E5 provenance divergence. Already-ruled items (U-3, U-4, U-5) are marked as such and excluded from the open list.

## 1. U-series status (source: Claude review §9)

| ID | Question | Status 2026-09-19 | Depends on |
|---|---|---|---|
| U-1 | Z-A: per-hex accounting rule on a zone-scoped record vs Tier-Y overlay on the mover | **Open fork** (Tiwa ruled (c): leave open; binary question deferred) | Q2 (ZoC shape), Q10 (ZoC↔Seize/Deny) |
| U-2 | Z-A floor clause preserving the DEC-125 guarantee (mover with A ≥ 1 may always enter one hex) | **Open** (candidate clause only; drafter to implement per sprint instructions §A) | U-1 |
| U-3 | Lock Movement-Distance ephemerality | **RULED — DEC-147** | — |
| U-4 | Mid-turn MS change formula (remaining = effective MS at query − hexes spent, floored at 0; no debt; rises grant movement) | **RULED — DEC-147** | — |
| U-5 | Record R3 as "consuming mechanics on the Position-tier substrate" | **RULED — DEC-148** (clarification, no list amendment) | — |
| U-6 | Whether Open/Close Lane is a silent eighth consuming mechanic | **Open, confirmed unaddressed** (single register match: DEC-023.A alpha list; no mechanics, no carrier; classification itself unruled) | U-5 |
| U-7 | Whether Disengage is a distinct Effect or maps to Base-tier Open Retreat / Compel Yield | **Open** | U-5 |
| U-8 | How Pin/Hold Position differs from Grappled (drafter to show, else Pin/Hold limited to Restrained) | **Open** (with drafter) | Item 4 fixes |
| U-9 | Definition of Restrained's "Break Free" mechanism (DEC-079 names it; no ruling defines it; DEC-124/131 define it for Grappled only — verified) | **Open unruled gap** | — |
| U-10 | Relationship between ZoC and the `reaction:vigilant` movement-trigger Reaction (redundancy) | **Open** | Q2 |
| U-11 | Whether Z-A and Disengage double-charge the same movement | **Open** | Z-A fork, Disengage shape |

## 2. The 14 mechanics questions (source: big-pickle report §3.3; all confirmed open by Nemotron)

1. **Disengage shape** — contested S-1 gate (D-A) vs free exit + reaction window (D-B) vs hybrid; Skill lineages; whether a failed D-A exit consumes movement allowance only or also the substantive action (DEC-095 interaction).
2. **Zone of Control shape** — cost-overlay (Z-A), pure reaction-enabler (Z-B), or gated pass-through contest (Z-C); whether ZoC and Seize/Deny Ground are exclusive or stackable; default hex/band coverage.
3. **Chase shape** — binary band steps (K-A) vs margin-accumulation track (K-B).
4. **Generic movement contest** — Skill lineages and payload selection rules for the shared primitive (Fork G).
5. **Forced Movement magnitude** — Tier-scaled hexes (F-A), fixed 1 hex (F-B), or MS-referenced (F-C); consistent with DEC-107 (Effect Tier = causing Skill-Tier).
6. **Pin/Hold vector** — full existing Condition (reuse Restrained per P-A) vs lightweight leave-contest mark (P-B).
7. **Seize/Deny shape** — denial-field (G-A), seize + displace (G-B), unified (G-C).
8. **Fork C (contested-movement consumption)** — mover's allowance, distance already travelled, or nothing beyond natural-roll Cost (carried-open by DEC-133.A R2).
9. **Fork T (extra Skill-Tier gate on Position-tier Effects)** — whether Position-tier requires a DEC-041-style gate beyond the DEC-023.A unlock.
10. **ZoC ↔ Seize/Deny relationship** — exclusive, layered, or soft/hard versions.
11. **Default Skill families for movement contests** (Disengage, Chase, generic M-0).
12. **Duration defaults for pins and ground claims** (G3/DEC-145 per-domain interaction not re-litigated).
13. **ZoC Z-A distance multiplier invariant status** (derives from C1) — own ruling or accounting framing sufficient?
14. **Pin/Hold Condition-stack reference precision** (derives from C2) — cite DEC-079's alpha vocabulary rather than/alongside DEC-122/123/124/126/131?

## 3. SA-5/E5 provenance divergence (unresolved, recorded)

- **Upstage SA-5** (`verifier-report-…` §4/SA-5): the fusion frontmatter `author_llm: grok-fusion` does not appear in the §11 source-run list (big-pickle, muse-spark, gemini-3.1-flash-lite, kilo-auto-free, openrouter-free) — authoring/fusion model ambiguous; a provenance-record defect.
- **Nemotron E5-CONFIRM** (assessment §4): frontmatter records author/assessor honestly — covered.
- **Status:** divergence recorded on DEC-133.A; unresolved. Drafter-side reconciliation listed in the sprint instructions (§D.4). Not a mechanics issue; matters only for provenance discipline.

## 4. Suggested ruling order (unchanged from prior advice)

B-item ephemerality and substrate readings are now ruled (DEC-147/148). Remaining sequence: drafter sprint fixes → Q2 + Q10 → U-1 binary question → Q1–Q12 mechanics in one ruling session (Z-A-adjacent items together) → U-6/U-7/U-9 as gap-closure rulings when reached.

## 5. Sources

Fusion draft, Hermes verifier-only report + summary, big-pickle chat report, Nemotron assessment, Claude Items 1–5 review, drafter sprint instructions — all in `investigations/`, all recorded on DEC-133.A; rulings DEC-147/DEC-148 in `_consolidation/decision-register.md`.
