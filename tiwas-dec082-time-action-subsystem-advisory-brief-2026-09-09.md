---
document:
  title: "DEC-082 Full Time/Action Subsystem — Tiwa's Selections, Consistency Check, Drafting Handoff"
  status: "Advisory brief — Claude-authored. NOT a ruling, NOT canonical. Records Tiwa's option selections; formal DEC recording is OpenCode's action pending Tiwa's final reconfirmation."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-09"
---

# DEC-082 Full Time/Action Subsystem — Advisory Brief

This records the option selections Tiwa made in this session against the nine open items
under DEC-082/Proposals §12, checks them for internal consistency and conflicts against
the live register (through DEC-135), and flags what still needs specification before
OpenCode can record clean DEC entries. **Nothing in this document is a ruling.** Claude
does not assign DEC numbers.

## 1. Selections as given

| Item | Selected | Tiwa's stated reason |
|---|---|---|
| G1 — Movement-penalty magnitude table | **Option C** — flat `−Y` default; per-Condition override via content-authoring (DEC-077.A), GM Fiat default | Flexible and mechanically simple |
| G3 — Duration/time-unit scale | **Option A** — fully abstract, no fixed real-world duration | Flexible and mechanically simple |
| Disengage | **Option B** — Reaction-gated opportunity cost (DEC-132 framework) | New reaction system has been proposed now |
| Zone of Control | **Option B** — Reaction-based, same machinery as Disengage | New reaction system has been proposed now |
| Chase | **Option B** — Chained S-1 opposed contests, Margin differential shifts relative Band position | More dramatic; Extended Test's GM-discretion completion target can be too arbitrary |
| Generic movement contests | **Option B** — Fold into Chase's mechanism | Avoids ruling the same mechanic twice |
| Forced Movement magnitude | **Option B** — Skill-Tier-based (DEC-107 pattern) | Higher Skill Tier → higher Effect |
| Pin/Hold Position | **Option A** — Reuse the existing Restrained Condition directly, no new Condition entry | Simplification |
| Seize/Deny Ground | **Option A** — Tag-based zone control (DEC-115–117 StateRecord architecture) | The Tag system is useful for resolving in-game complications |

## 2. Consistency check against the live register (through DEC-135)

No selection contradicts Locked Canonical material or an existing Ruled DEC. Detail:

- **G1-C / G3-A** — Pure defaults-plus-content-authoring; no new numeric surface, no new
  formula. Consistent with DEC-078/DEC-122's flat-`−Y`-overlay precedent and with DEC-133's
  deliberate omission of a real-world duration lock. No conflict.
- **Disengage-B / Zone of Control-B** — Both route through the already-Ruled DEC-132
  Reaction framework: tag-gated, full S-1 exchange, no new action economy, no bypass of
  DEC-095 turn order. Since both use identical machinery, they can be recorded as one
  ruling with two trigger definitions rather than two separate mechanisms. **This matches
  the pairing I flagged before you decided** — no rework needed.
- **Chase-B** — Chained S-1 contests. Each interval is a full Core Test for both
  participants (Cost = natural roll, Overflow risk, Failure XP, Recovery — DEC-006/007).
  No new resource pool is created (Invariant 17 intact — this is repeated use of the
  existing engine, not a parallel one). **Flag (not a conflict, a consequence you should
  be aware of):** a chase of any length now carries genuine Overflow/HP risk for both
  sides purely from movement, since Cost = Roll applies every interval. This is consistent
  with Priority 1 (granular simulation) and the system's general "every attempt costs
  resources" identity — flagging only so it's a deliberate outcome, not a surprise.
- **Generic movement contests-B** — Folds cleanly into Chase-B; no separate mechanism
  needed. No conflict.
- **Forced Movement-B (Skill-Tier basis)** — Consistent with DEC-107's now-dominant
  Effect-severity paradigm (Effect Tier = causing Skill's Skill-Tier).
- **Pin/Hold Position-A (reuse Restrained)** — No new Condition entry; Pin now has no
  independent identity from Restrained. **Flag:** Restrained is currently defined (DEC-079)
  as fairly strong (`−Y to all attacks + all Body Skills`, no movement). If "Pin" as a
  fictional concept was meant to be milder than full Restrained, that nuance is now gone —
  worth a one-line confirmation that this is intended, since it's a step stronger than what
  Option B (a dedicated weaker Condition) would have produced. Not a rules conflict; a
  design-intent check.
- **Seize/Deny Ground-A (Tag-based)** — Uses the DEC-115–117 unified StateRecord schema;
  stateless/read-only per the existing Tag discipline (DEC-058/080). No conflict.

**⚠ One cross-item consistency note, not a conflict but worth flagging explicitly:**
Chase-B uses **Margin differential** to shift relative Band position, while Forced
Movement-B uses **Skill-Tier** as its magnitude basis. These are the two different
magnitude paradigms currently live in the system (contest-delta vs. Skill-Tier — see
DEC-104 vs. DEC-107). You've now deliberately assigned Margin to Chase and Skill-Tier to
Forced Movement rather than harmonizing on one. That's a legitimate design choice (they
are different kinds of interaction — an extended contest vs. a single Effect), but it
means a future Position-tier Effect can't assume either paradigm by default; whichever it
resembles more closely should be decided explicitly when it comes up, same as here.

## 3. Open specification gaps before OpenCode can record these cleanly

These aren't additional decisions to make now — they're structural details a formal DEC
entry will need. Flagging so you can either supply them now or explicitly defer them as
content-authoring (DEC-077.A), consistent with how DEC-132 itself left its trigger menu
open.

| Item | What's still unspecified | Suggested disposition |
|---|---|---|
| Disengage / Zone of Control | Exact trigger wording (e.g., "target leaves Engagement band without a qualifying action") and the specific reaction-granting Tag name(s) | Content-authoring (DEC-077.A), same as DEC-132's own carried-open trigger menu — does not block recording the framework ruling |
| Chase | Which skill(s) qualify as "Speed-relevant" for the contest; whether Margin shifts one Band per point or per some divisor; win/end condition (catch = same Band? escape = Far reached?) | Needs at least a formula decision before this is table-ready — recommend a short follow-up ruling, not left to pure content-authoring, since it's a core mechanic rather than flavor |
| Generic movement contests | None beyond Chase's — inherits whatever Chase specifies | No independent action needed |
| Forced Movement | Whether displacement is in hexes 1:1 with Skill-Tier, or some other conversion against the DEC-133 band/hex model | Needs a short formula confirmation (e.g., "Displacement in hexes = Effect Tier") |
| Pin/Hold Position | None mechanically (fully inherits Restrained) — only the design-intent confirmation flagged above | Confirm intent, otherwise ready to record as-is |
| Seize/Deny Ground | The specific Tag name(s) and what "controlling a Band" means procedurally (who can apply/remove the tag, and when) | Content-authoring (DEC-077.A) — does not block recording the framework ruling |
| G1 | None — fully specified as ruled | Ready to record |
| G3 | None — fully specified as ruled | Ready to record |

## 4. Required OpenCode Actions (pending Tiwa's final reconfirmation)

1. Confirm each selection above with Tiwa individually (or as a batch) before recording.
2. For **Disengage/Zone of Control**, record as a single ruling extending DEC-132's
   framework with two trigger categories (leaving Engagement; being entered/crossed within
   Engagement), both content-authored per DEC-077.A.
3. For **Chase**, hold formal recording until the formula gap (Margin-per-Band conversion,
   qualifying skills, end condition) is resolved — do not record with an implicit default.
4. For **Forced Movement**, hold formal recording until the hex-conversion formula is
   confirmed.
5. **Pin/Hold Position, Seize/Deny Ground, G1, G3** may be recorded as-is once Tiwa
   reconfirms the Pin/Restrained intent note in §2.
6. Update the DEC-082/Proposals §12 open-items list to remove G1, G3, and (pending the
   above) the seven Position/Movement items from "open."

## 5. Reconfirmation checklist for Tiwa

- [ ] G1 Option C — confirm
- [ ] G3 Option A — confirm
- [ ] Disengage Option B — confirm
- [ ] Zone of Control Option B — confirm (paired with Disengage)
- [ ] Chase Option B — confirm, **and** supply/defer the Margin-per-Band formula, qualifying
      skill(s), and end condition
- [ ] Generic movement contests Option B — confirm (inherits Chase)
- [ ] Forced Movement Option B — confirm, **and** supply/defer the hex-conversion formula
- [ ] Pin/Hold Position Option A — confirm the Restrained-strength intent is acceptable
- [ ] Seize/Deny Ground Option A — confirm

