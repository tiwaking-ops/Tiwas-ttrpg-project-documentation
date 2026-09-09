**Decision Draft: Unified State Record for Tags / Effects / Conditions**  
**Status:** Non-canonical designer ruling candidate. Pending formal 8-step promotion. Does not alter Canonical Rules.  
**Author intent:** Evaluate the five-point unification hypothesis against existing non-canonical rulings and complexity budget.  

---

### Executive Verdict

The unification is **conditionally worth adopting**, but only in a minimal form that collapses record format and production/removal surface area while preserving three fiction-level Types.  

A shared backbone (Tier Y, Magnitude Z, optional Location X) removes parallel schemas and duplicate removal language. It does **not** eliminate the need for Type-specific production rules, stacking precedence, counter rules, and duration defaults. Net complexity reduction is real but modest: roughly one full subsystem description disappears; three specialized rule sets remain.  

The core tension is real. “Tags counter Tags” and “Tags and Conditions are not distinct” both pressure the existing read-only / stateless guardrail (DEC-058/079/080/088, Invariant 17 / REQ-017, DEC-007.A). If those guards are treated as soft, the merge works cleanly. If they are treated as hard architectural invariants, the counter mechanic and any active Condition-like behavior on Tags become second-resolution or resource-adjacent and must be rejected or tightly scoped.  

Recommended path: adopt the shared schema + Type enum + permanence default + named-action removal. Explicitly reject unrestricted Tag-vs-Tag counters that modify pools. Flag every departure from prior non-canonical rulings.

---

### What “One Mechanical Backbone” Actually Means

**Unified State Record**

```
StateRecord {
  Type:        enum { Tag, Effect, Condition }   // fiction-level distinction only
  Identity:    string                            // vocabulary token (env:darkness, Sundered, Bleeding, etc.)
  Tier:        integer Y ≥ 0                     // severity / quality band
  Magnitude:   integer Z                         // signed intensity; default Z = −Y for Conditions
  Location:    optional LocationIndex or null    // X; required only when the consumer demands localization
  Source:      optional reference                // Skill roll, environmental assertion, Trait, etc.
  Duration:    enum { Permanent, Temporary, Named } + optional timer or trigger
  StackRule:   enum { Replace, Add, Highest, Special }
}
```

- **Type** is pure classification. It does not create separate mechanical engines.  
- **Tier Y / Magnitude Z / Location X** are the only numeric fields. All prior Condition “Value Z = −Y” and Effect magnitude language map onto these.  
- Production, application, and removal are Type-gated rules that operate on the same record.  
- No second resolution engine. No new primary resource. No pool modification by the record itself (DEC-007.A / Invariant 17 preserved).

Fiction-level concepts survive:

| Fiction Concept | Type value | Default Duration | Typical Production |
|-----------------|------------|------------------|--------------------|
| Tag             | Tag        | Permanent        | Assertion, Trait, environment, equipment |
| Effect          | Effect     | Temporary        | Winning S-1 contest (DEC-023–030, 107) |
| Condition       | Condition  | Temporary or Named | Effect payload, hazard, injury |

Tags and Conditions are no longer required to be ontologically distinct; they differ only by Type label and default Duration/StackRule. Effects remain the only Type whose production is strictly gated by an S-1 win + auto-apply (DEC-027).

---

### Impact Analysis of the Five Ideas

**1. Tags are like Effects, but Tags are Permanent; Effects are caused by a Skill Roll**

- **Change:** Duration becomes an explicit field with Type defaults. Permanent is default for Tag, Temporary for Effect.  
- **Breaks / Conflicts:** None hard. Existing “Sundered is permanent until repaired” (DEC-060/079) becomes a specific instance of Named duration.  
- **Fixes:** Removes the need for a separate “Tags have no duration language” vs “Conditions have duration language” split.  
- **Caveat:** Permanent is a default, not an absolute. Removal is always possible via Named actions or higher-Tier Effects. This matches the clarified hypothesis.

**2. Tags, like Effects, have Tier Y Magnitude Z. Tags may also have Location X**

- **Change:** Single numeric triple for all three Types.  
- **Breaks / Conflicts:** Soft conflict with “Tags carry identity/vocabulary only” (DEC-080 Q4). That ruling treated Tags as pure metadata; attaching Y/Z makes them quantitative.  
- **Fixes:** Enables consistent gating (env:freezing Tier-2 vs Tier-1) and location-aware Tags (env:darkness on a specific zone).  
- **Net:** Acceptable. The identity token remains the primary key; Y/Z are optional intensity modifiers consumed by other subsystems.

**3. Tags can counter other Tags (e.g., creature-side ignores-darkness counters env:darkness)**

- **Change:** Introduces an active interaction rule between records of Type=Tag.  
- **Breaks / Conflicts:** Direct tension with the read-only / stateless guardrail (DEC-058/079/080/088, Invariant 17, REQ-017). Current doctrine says Tags never create/consume/modify pools and are not themselves mechanical actors. A counter that suppresses another Tag’s permission effect is a mechanical actor.  
- **Fixes:** Closes the explicit design gap (Night-Vision / ignores-darkness vs env:darkness).  
- **Honest assessment:** This is the highest-risk idea. If the counter is implemented as pure permission negation (“the consuming subsystem sees the higher-Tier or more-specific Tag and ignores the lower one”), it stays inside the read-only model. If it requires a roll, resource spend, or state change on the Tag itself, it violates the guardrail and must be rejected. Recommendation: permission-precedence only, no second contest.

**4. Tags and Conditions are NOT distinct**

- **Change:** Collapses the explicit architectural requirement in Proposals §10/§11 (“They must remain distinct from Tags”; “Tags are not Conditions”).  
- **Breaks / Conflicts:** Direct contradiction of the current non-canonical stance. Also pressures the distinct Condition record format and Z = −Y rule (DEC-079).  
- **Fixes:** Eliminates parallel schemas, duplicate stacking language, and the artificial “is Sundered a Tag or a Condition?” question.  
- **Net:** This is the largest complexity win. The fiction-level distinction is retained via the Type field; the mechanical distinction is discarded.

**5. Tags can be Removed**

- **Change:** General removal rule for Type=Tag (previously only Sundered had explicit language).  
- **Breaks / Conflicts:** None; it fills an explicit gap.  
- **Fixes:** Consistent removal surface: Named action, higher-Tier Effect of appropriate Identity, or explicit Duration expiry.  
- **Constraint:** Removal never touches Overflow/HP/pools (DEC-007.A preserved).

---

### The Complexity Math

**Before (current non-canonical surface)**  
- Three record formats  
- Three production rulesets  
- Three (or more) removal/stacking rule sets  
- Special-case language for Sundered  
- Explicit “Tags ≠ Conditions” invariant that must be policed  
- Open counter-gap for environmental Tags  

**After (minimal unification)**  
- One record schema  
- Type-gated production defaults  
- One removal interface + Type-specific triggers  
- One stacking precedence table  
- Explicit permanence default  
- Explicit permission-precedence counter rule  

**Net change**  
- Schema and boilerplate text: −40–50 %  
- Specialized interaction rules: roughly neutral (some old rules disappear, new counter + permanence language appears)  
- Cognitive load for the designer: lower (one place to look)  
- Cognitive load for the GM at the table: slightly lower if the Type field is visible and defaults are strong; higher if the counter rule is under-specified  

Honest conclusion: the unification **does** reduce total system weight, but only if the counter rule stays extremely thin (permission precedence, no rolls, no pools). Any attempt to make Tags “active” beyond that re-introduces a second mechanical engine and the savings evaporate.

---

### Conflicts and Honest Tensions

**(a) “Tags counter Tags” vs. stateless/read-only guardrail**  
Real conflict. Current doctrine (DEC-058/079/080/088 + Invariant 17) treats Tags as inert metadata. A counter that is more than a static precedence table becomes an actor. Solution: define counter strictly as consumer-side filtering (“when both env:darkness and ignores-darkness are present, the higher-Tier or more-specific Tag wins; the suppressed Tag remains on the record but is ignored by permission checks”). No modification of the Tag record itself, no resource spend.

**(b) “Tags and Conditions are NOT distinct” vs. distinct-format / stacking design**  
Real conflict with Proposals §10/§11 and DEC-079. The distinct-format claim is non-canonical and can be superseded. Stacking rules move into a single table keyed by Type + Identity. Loss: any future Condition-specific stacking quirks that cannot be expressed as StackRule enum values.

**(c) Permanence / removal phrasing**  
Already clarified by the hypothesis. Permanent = default Duration for Type=Tag; removal is always available via Named means. No absolute permanence. Compatible with Sundered.

**(d) Does unification re-open DEC-025?**  
No. DEC-025 rejected a formal tag/category system **on Skills** for Effect entitlement. The unified StateRecord lives on characters, environments, equipment, and effects—not on the Skill list. Skill identity remains pure declared intent. The rejection stands.

Additional soft tension: attaching Tier/Magnitude to Tags softens “Tags carry identity/vocabulary only.” Acceptable if Identity remains the primary key and Y/Z are optional intensity.

---

### Concrete Recommended Design (Minimal Unification)

1. **Adopt the Unified State Record** exactly as specified above.  
2. **Type defaults**  
   - Tag → Duration = Permanent, StackRule = Highest (or Special for known pairs)  
   - Effect → Duration = Temporary, StackRule = Replace (or Add if Identity allows)  
   - Condition → Duration = Temporary or Named, Magnitude default Z = −Y, StackRule = Add or Highest per Identity  
3. **Production**  
   - Effect: only via successful S-1 + auto-apply (existing DEC-023–030, 107, 027).  
   - Tag / Condition: by assertion, Trait, hazard, or as payload of an Effect.  
4. **Counter / Permission Precedence** (thin rule only)  
   - When two Tags of conflicting Identity are present, the consumer evaluates the higher Tier; on tie, the more specific Identity or the one with Location match wins.  
   - The losing Tag remains on the record; it is simply ignored by permission checks. No roll, no resource, no mutation of the Tag.  
5. **Removal**  
   - Any StateRecord may be removed by: (a) its own Duration expiry, (b) a Named action or Effect whose Identity is defined as a remover for that Identity, (c) explicit higher-Tier Effect of opposing Identity.  
   - Sundered becomes Identity = Sundered, Type = Tag or Condition (designer choice), Duration = Named (“until repaired”).  
6. **No pool interaction**  
   - StateRecords never modify Overflow, HP, or any primary resource (DEC-007.A / Invariant 17 held).  
7. **Fiction-level language**  
   - Rulebook and GM text continue to say “Tag”, “Effect”, “Condition”. The Type field is the only mechanical distinction.

This package supersedes the “Tags are not Conditions” and pure-metadata stances in the non-canonical corpus. It does not touch Canonical Rules. It does not re-open DEC-025.

---

### Open Questions That Must Be Ruled On

- Exact StackRule table for the first wave of Identities (Bleeding, Sundered, env:darkness, ignores-darkness, etc.).  
- Whether Magnitude on a Tag is ever allowed to be negative, or is always unsigned intensity.  
- Whether Location is required, optional, or forbidden for each major Identity class.  
- Precedence tie-breaker when two Tags have identical Tier and no Location match (specificity hierarchy? source priority? GM fiat?).  
- Whether “Condition” as a Type label is retained long-term or collapsed into Tag + Duration = Temporary (pure terminology decision).  
- Formal promotion path and which prior DEC numbers are explicitly superseded once this draft is accepted.

---

**End of Decision Draft.**  
This is a working proposal only. It is not Canonical, not promoted, and not binding until the formal process is completed.