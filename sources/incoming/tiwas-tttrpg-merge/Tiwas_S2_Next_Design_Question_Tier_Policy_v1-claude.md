# Tiwas — Next S-2 Design Question: Tier 0/1/2 Situational Policy (Starter Brief v1.0)

**Use this to open a new chat.** It's self-contained — includes what's already settled, what this new
question does and doesn't cover, what's already been sketched about it, and a suggested approach.

---

## 1. What's already settled (don't re-litigate)

- **S-2 Tier-1 formula:** Zero-Step is the ruled, canonical Tier-1 Location Index provider. Deterministic,
  no player choice. See Canonical Rules §14.1–§14.2.
- **E9 (physical-dice usability):** Passed, for the tested two-physical-d10 method specifically. Other
  input methods (single d100, digital roller, verbal) remain untested — Canonical Rules §14.5.
- **Comparative derivation cost:** Units-Digit needs 0–1 extra operations across rolling modes, Zero-Step
  needs 1–2 — Canonical Rules §14.6. Structural, not a human-usability finding.
- None of the above is open for reconsideration here. This question is strictly about what comes next.

## 2. The question

**When does a scene, combatant, or action use Tier 0 (no location state), Tier 1 (Zero-Step Location
Index), or Tier 2 (future high-granularity model)?**

This is explicitly *not* the same question as "which Tier-1 formula" — it's one level up: whether Tier 1
gets invoked at all for a given roll, and by what mechanism that gets decided.

## 3. Why this one, not the anatomical mapping table

The anatomical mapping table (Location Index → named zone) is the other major open S-2 piece, but it's
downstream of this one: if Tier 0 applies to a given scene, the mapping table never gets consulted at all.
Tier policy is more foundational, doesn't require inventing zone content first, and is smaller in scope —
a policy/interface question, not a full content-design undertaking. If you'd rather start with the
anatomical table instead, that's a legitimate alternative; just flag it and this brief doesn't apply.

## 4. What's already on record about this

- Proposals/WIP §2.3 gives the three-tier table (model, resolution cost, intended use) but explicitly
  frames situational selection as "a design direction only, not a locked rule" (§2.5).
- An earlier design pass (predating the S-2 formula work) sketched a **Location Provider interface**:
  `LocationProvider(Context) → LocationTier`, where `Context` is a record (scene, attacker, target, action,
  declared_intent, equipment, setting_context), and the provider may ignore fields it doesn't need. This
  was accepted as an architectural direction but never built out or decided.
- Roadmap U-09 ("Location Provider — Tier 0/1/2 location architecture") is the subsystem this question
  resolves.

## 5. Open sub-questions

- Is tier selection fixed per-campaign, per-scene, per-combatant, or per-action? (The Provider interface
  above was designed to support any of these — the question is which the ruleset actually wants.)
- Who decides: a hard rule, GM discretion, a declared-intent trigger ("called shot" → Tier 1), or some
  combination?
- Does a *default* exist, or is tier always explicitly chosen with no fallback? (Design Direction doc
  currently resists naming any tier "the" default — worth deciding whether that resistance still holds
  once a concrete policy is on the table.)
- Interaction with Priority 1 ("granular physical simulation where the situation warrants it") — what
  counts as "warranting it"?

## 6. Suggested approach

This is a different kind of question than the formula choice was. That one had a clean mathematical
answer reachable through statistical comparison. This one is closer to a game-design/workflow question —
there's no equivalent of "run 5,040 permutations" that settles it. Likely more productive: sketch 2–3
concrete candidate policies (e.g., "always Tier 0 except called shots," "GM sets tier per scene,"
"Tier scales with combatant significance — mooks get Tier 0, named NPCs get Tier 1"), then evaluate them
against resolution-step cost, table-use friction, and Priority 1 — rather than trying to mathematically
derive the one correct policy the way Zero-Step vs. Units-Digit was resolved.

## 7. Source documents

Canonical Rules & Changelog v1.3, Proposals/WIP v1.3, Implementation Roadmap v1.3 — current project files.
Note: as of this brief, the Roadmap still has one unresolved internal inconsistency (§6 dependency diagram
vs. §4/Phase numbering on S-2/S-3 ordering) — unrelated to this question, flagged separately, not blocking.
