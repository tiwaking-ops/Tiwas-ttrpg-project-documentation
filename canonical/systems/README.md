---
document:
  title: "Canonical Systems — Index"
  version: "1.0"
  status: "Governance pointer"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Canonical Systems

This folder is currently empty by design, not by omission.

The supplied corpus contains exactly one locked ruleset, held in a single document: `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`. That document already covers everything currently locked: Core dice/resolution, the attribute matrix, derived statistics, skills, the Core Test Transaction, resource cost/overflow, recovery, Failure XP, Skill Roll Pool, General XP, Advanced Skills, S-1 (Opposed Contest), and the limited S-2 Tier-1 Location Index provider.

No locked subsystem currently has enough independent, separately-versioned content to justify splitting it into its own file under `canonical/systems/` — doing so now would fragment a single coherent document without evidentiary benefit, and would risk the two halves drifting out of sync.

**Recommendation for future maintenance (not performed now):** if/when additional subsystems (S-3 onward) are formally locked via the Promotion Rule (`governance/status-model.md`), consider splitting `canonical/rules/` by system (Core, S-1, S-2, S-3, ...) at that point, since the single-file approach will scale less well as more subsystems lock. This is a recommendation, not an action taken by this consolidation.
