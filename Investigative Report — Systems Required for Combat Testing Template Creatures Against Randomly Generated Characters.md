**Tiwas TTRPG — Investigative Report**  
**Combat Test Readiness: Template Creatures vs. Randomly Generated Characters**

```yaml
---
document:
  title: "Investigative Report — Systems Required for Combat Testing Template Creatures Against Randomly Generated Characters"
  version: "1.0"
  status: "Investigative / Advisory (non-canonical; does not rule, promote, or lock any mechanic)"
  scope: "Single-purpose gap analysis for S-12 creature combat testing against DEC-003 random PCs"
provenance:
  author_llm:
    name: "Grok"
    version: "4.5"
  assessor_llm: []
  last_modified_by_llm:
    name: "Grok"
    version: "4.5"
  created_date: "2026-09-03"
  last_modified_date: "2026-09-03"
---
```

### 1. Purpose and Scope
This report inventories every mechanical system required to run a combat test between S-12 template creatures (Ice Troll, Blood Man, and any additional provisional blocks under DEC-077.A) and characters generated via the locked 24-attribute matrix (DEC-003).  

It then identifies what is currently Ruled / Locked versus what remains missing or incomplete.  

No new rulings are proposed. The report is purely diagnostic.

### 2. Required Systems Inventory

| # | System / Subsystem | Core Function in Combat Test | Upstream Locked Dependencies |
|---|---|---|---|
| 1 | Attribute Generation & Derived Stats | Random PC creation (24 attributes → HP, MP, PE, Speed, Movement, Caps) | DEC-003, DEC-004, DEC-005 |
| 2 | Core Test Transaction | Universal resolution engine for all attacks, defenses, and skill uses | DEC-001, DEC-006, DEC-007, DEC-007.A, DEC-008–012 |
| 3 | S-1 Opposed Contest | Attack vs. defense framing, Margin / Quality determination | DEC-013 |
| 4 | S-3 Effect Menu & Application | Selection and auto-application of combat outcomes (Injury, Wound, Condition, Position, Equipment, Defense, Location) | DEC-023, DEC-023.A, DEC-024–031 |
| 5 | S-2 Location Index | Hit location generation and anatomical resolution | DEC-014, DEC-037–042 |
| 6 | S-4 Wounds | Localized lasting injury tracking and magnitude | DEC-032–036, DEC-035.A, DEC-035.B |
| 7 | S-5 Armor | Tag-based resolution sequence before Active Defense | DEC-058–062 |
| 8 | S-6 Active Defense | Post-hoc mitigation of auto-applied Effects | DEC-044–050, DEC-075 |
| 9 | S-7 Incapacitation / Death | HP = 0 forced down and permanent-loss conditions | DEC-052–057 |
| 10 | Conditions Subsystem | Mechanical effects of Grappled, Prone, Fatigued, etc. | DEC-079 (plus DEC-060, DEC-075, DEC-078) |
| 11 | Tags Ontology | Equipment, environment, and creature tagging | DEC-080 |
| 12 | Equipment State Model | Held / worn item location binding and state | DEC-081 |
| 13 | Time / Action Economy | Skill-side / Movement penalties only (no action points) | DEC-082 |
| 14 | Environment-Conditional Traits | Gating of creature Traits (e.g., Ice Troll on `env:freezing`) | DEC-088 |
| 15 | S-12 Creature Templates | Actual stat blocks, signature skills, Traits, and attack packages | DEC-076, DEC-077.A, DEC-083–088 |
| 16 | Hazard / Environmental Resolution | Optional scene-state effects during combat | DEC-089–093 (partial) |

### 3. Current Status of Each Required System

| System | Status | Notes |
|---|---|---|
| 1. Attribute Generation | **Canonical / Locked** | Fully operational for random PCs |
| 2. Core Test Transaction | **Canonical / Locked** | Fully operational |
| 3. S-1 Opposed Contest | **Canonical / Locked** | Fully operational |
| 4. S-3 Effect Menu | **Ruled** (structure + alpha content) | Magnitudes still open |
| 5. S-2 Location Index | **Ruled** (architecture) | Exact numeric ranges and promotion triggers deferred |
| 6. S-4 Wounds | **Ruled** (format + tier + Quality ceiling) | Accumulation-to-permanent-loss threshold open |
| 7. S-5 Armor | **Ruled** | Fully operational for Tag resolution |
| 8. S-6 Active Defense | **Ruled** (architecture) | Mitigation formula still open |
| 9. S-7 Incapacitation | **Ruled** | Fully operational |
| 10. Conditions | **Ruled** (format + 14-item alpha vocabulary) | Exact penalty magnitudes open |
| 11. Tags | **Ruled** (34-tag alpha vocabulary) | Extensible; sufficient for alpha |
| 12. Equipment State | **Ruled** | Fully operational |
| 13. Time / Action | **Ruled** | Fully operational |
| 14. Env-Conditional Traits | **Ruled** (binary only) | Graded temperature and scene-tracking open |
| 15. Creature Templates | **Provisional only** | Ice Troll & Blood Man under DEC-077.A; not affirmed |
| 16. Hazards | **Partially Ruled** | Cadence scoped; content detail open |

### 4. Critical Gaps for Combat Testing

The following items are **blocking or severely degrading** a clean combat test:

1. **Creature Templates (Highest Priority)**  
   - No affirmed, table-ready Ice Troll or Blood Man blocks exist.  
   - Provisional conversions remain subject to individual designer ruling.  
   - Missing: full Cap signature skills, exact Trait magnitudes, Regeneration/Regrowth/Fright values, and target-HP Inflict Injury magnitude.

2. **Active Defense Mitigation Formula**  
   - Architecture is locked, but no numerical rule exists for how much magnitude a successful Defense removes.  
   - Without this, every Defense roll is undefined in outcome.

3. **S-3 Effect Magnitudes**  
   - Alpha list is locked, but no numbers exist for Forced Movement distance, Knock Prone duration, Grapple strength, Lower Defense value, Impose Wound magnitude, etc.  
   - Defense-tier Effects cannot interact meaningfully with Active Defense until magnitudes are set.

4. **S-2 Anatomical Mapping Ranges**  
   - Exact zone weightings and Tier-1/Tier-2 promotion triggers are still deferred.  
   - Location-tier Effects and Armor coverage checks lack concrete tables.

5. **Wound Accumulation Threshold**  
   - No guidance on how many stacked wound negatives trigger permanent loss. Pure GM discretion currently.

6. **Condition Penalty Magnitudes**  
   - Vocabulary exists; mechanical values (e.g., Slowed = –X Movement, Grappled = –Y Skill) do not.

7. **Abbreviated Stat-Block Format**  
   - No formal tabletop presentation template under DEC-076 dual-mode.

### 5. Non-Blocking but Incomplete Items
- Graded temperature / scene-state tracking (DEC-088 residual).  
- Full Hazard content formalization.  
- Automated tooling for full 24-attribute mode (computerized play).  
- Second-Effect opposed-roll mechanical details (DEC-024/026).

### 6. Minimum Viable Combat Test Path
To run a single, functional combat test with the least additional design work:

1. Affirm (or produce) at least one provisional creature template under DEC-077.A constraints.  
2. Define a temporary, playtest-only Active Defense mitigation rule (e.g., Margin-based reduction table).  
3. Define temporary magnitudes for the 4–6 most common Effects expected in the encounter (Inflict Injury, Knock Prone, Grapple, Impose Wound, Lower Defense).  
4. Use GM fiat for anatomical ranges and wound accumulation for the duration of the test.  
5. Log all temporary values as explicit playtest scaffolding (not rulings).

### 7. Conclusion
The Core resolution engine, attribute generation, opposed contest, armor sequence, and Active Defense architecture are sufficiently locked to support combat testing.  

The primary blockers are:
- Absence of affirmed creature templates.
- Absence of numerical magnitudes across S-3 Effects, Active Defense mitigation, Conditions, and anatomical tables.

Until those numerical layers are supplied (even as temporary playtest values), any combat test will require continuous GM fiat and will not produce clean, reproducible data.

**Report complete.**  
No mechanics have been ruled, promoted, or altered by this document.