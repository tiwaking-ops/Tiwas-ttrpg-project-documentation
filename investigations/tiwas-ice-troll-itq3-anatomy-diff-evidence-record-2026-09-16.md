---
document:
  title: "Tiwas — IT-Q3 Evidence Record — L-004 Ice Troll Template vs the v3–v6-Era Playtest Stat Block"
  version: "1.0"
  status: "Advisory evidence record — Non-canonical. Resolves IT-Q3's factual question (does the template contradict the playtest record?) with a verifiable diff; the adoption decision itself remains Tiwa's (agenda item A2). Rules nothing; no DEC inferred."
provenance:
  author_llm: {name: "buffy/codebuff", version: "not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "buffy/codebuff", version: "not established"}
  created_date: "2026-09-16"
  last_modified_date: "2026-09-16"
---

# IT-Q3 Evidence Record — Ice Troll Template vs v3–v6 Stat Block

## 1. What IT-Q3 asks

Open-questions inventory (P0 #2): *"Reconcile invented anatomy (4 digits, no Ears,
size) against any existing Ice Troll stat block."* Fear on record: if the stat block
the v3–v6 playtests used assumes five digits, ears, or a different size class, the
L-004 template contradicts the playtest record.

## 2. The operative stat block(s), identified

- **`tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md`** (git HEAD, deleted
  from working tree) — inline stat block at "Opponent — Ice Troll": 24 attributes,
  Derived Statistics "HP 705 · MP 420 · Physical Energy 220 · Speed 175", GURPS
  source values "reference only — not imported".
- **`tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md`** (git HEAD, deleted
  from working tree) — same inline stat block, plus the v4 changes (explicit
  scaffold table, mandatory Wound exercise).
- Supporting pipeline: `investigations/tiwas-btv-madness-ice-troll-combat-pipeline-gpt-5.6-luna-2026-09-03.md`
  and the conversion scratch (`…-v0.2-2026-09-03.md`), which carry the same
  "Flagged, not converted" trait rows.

This is the stat block lineage behind the v3, v3-unedited, v3-synthesis, v4, and
v4-synthesis playtest records (root files, git HEAD).

## 3. The diff — every anatomy-committed fact in the stat block vs the L-004 template

| # | v3–v6 stat block commits to | L-004 template says | Verdict |
|---|---|---|---|
| 1 | DEC-100 Tier-1 coarse zones: 1–25 Legs / 26–50 Torso / 51–75 Arms / 76–100 Head (v4 §C-08, explicit table) | Reuses the same DEC-100 quartiles (its own Q1 flags this as an assumption) | **Identical** — no conflict |
| 2 | Laterality via S-2 Zero-Step parity | Same convention (§3.5, "Same convention as Human … parity of the raw Zero-Step index") | **Identical** |
| 3 | HP 705; 24-attribute matrix; MP/PE/Speed | Not addressed by a location template (stat-block layer, not anatomy layer) | **Out of scope** — unaffected |
| 4 | Regeneration/Regrowth (freezing only): "Flagged, not converted" — **inactive in every run** | Template carries DEC-088/DEC-110 Regen as stat-block trait, not template content | **Consistent** — nothing to reconcile; TR-Q2 watch-item unaffected |
| 5 | DR 2 (freezing only): "Flagged, not converted. **No DR contribution; do not invent Armor**" (v3 L132, v4 L137) | Template proposes no standalone Armor Tag; the DEC-088 `defense:armor` Tag remains a stat-block trait with placement open (IT-Q2) | **Consistent** — v3–v6 played with *no* armor; the template adds none; IT-Q2 only matters if/when the DEC-088 Tag is ever activated |
| 6 | Four digits per hand/foot (template §2) | — | **Stat block is silent** — never committed, never exercised |
| 7 | No distinct Ears node; vestigial ear tissue inside Skull (template §2/§3.4) | — | **Stat block is silent** — Head was never resolved below Tier 1 in any run |
| 8 | `size_large` (template frontmatter/App B) | — | **Stat block is silent** — no size tag existed in the v3–v6 era |
| 9 | Tier-2+ anatomy (Skull 15, Jaw/Tusks 6, Hide nodes, Heart/Ice Gland/Lungs/Stomach/Intestines/Kidneys, Hide toughness) | — | **Never exercised**: v3 synthesis records "2/3 runs never touched" Location/Wound; v4's mandatory Wound exercise resolves at Tier-1 coarse zones only (C-08) — no Tier-2 address was ever authored or rolled |
| 10 | Skill-Tier→Wound scaffold (v4 Quality table) | — | Already invalidated by DEC-107 (register-noted); independent of template adoption |

**Search basis:** both prompts were grepped for digit/finger/toe/ear/size-tag
vocabulary — zero anatomy commitments found (the only matches are the
"Appearance (Hideous)" fear-binding rows). The stat block's only anatomical
commitments are #1 and #2, both of which the template reproduces exactly.

## 4. Finding

**Zero mechanical contradiction.** The v3–v6 playtests resolved locations only at
Tier-1 coarse zones under DEC-041/DEC-102, activated no armor, activated no
regeneration, and never committed to digit count, ears, size class, or any Tier-2+
anatomy. The L-004 template's Human-divergent content (4 digits, folded ears,
`size_large`, Hide nodes, Jaw/Tusks) faces nothing in the playtest record it could
contradict — those runs pre-date L-004 templates entirely.

**Consequence:** IT-Q3 is a **forward-looking adoption decision**, not a retroactive
repair. The agenda-A2 posture ("template is the anatomy baseline for all future
playtests; v3–v6 records stand as pre-template runs; re-base the stat block before
the next Ice Troll playtest") resolves it cleanly with no history rewriting. The
only genuine carry-forwards are IT-Q2 (Armor Tag placement, if the DEC-088 Tag is
ever activated) and the TR-Q2 watch-item — both unchanged by this record.

## 5. Explicit Non-Decisions

No proposal or stat block is edited; no playtest record is re-statused; IT-Q2 and
TR-Q2 remain open; nothing is accepted or rejected; no DEC is assigned. This record
only establishes that the template and the historical stat block do not conflict.

---

*Prepared by buffy/codebuff (advisory), 2026-09-16. Evidence pulled from git HEAD
where the working tree no longer holds the files; all quotes verbatim. Companion to
the P0/P1 ruling-session agenda (item A2), the DEC-143 acceptance draft (Row 1), and
the open-questions inventory (IT-Q3). Advisory only; confers no authority.*
