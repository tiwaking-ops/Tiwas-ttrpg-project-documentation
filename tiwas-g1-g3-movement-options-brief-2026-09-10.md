---
document:
  title: "G1/G3 Options Brief — Movement-Penalty Magnitude Table & Duration/Time-Unit Scale"
  version: "0.1"
  status: "Advisory only. NOT a ruling. NOT canonical. No DEC number assigned."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-10"
  last_modified_date: "2026-09-10"
---

# G1/G3 Options Brief — Residuals of DEC-133

**Status:** Advisory options only. Per governance (`authority.md`, `status-model.md`), Claude
does not rule and does not assign DEC numbers. This document presents options for Tiwa's
ruling; OpenCode records the outcome against the live register once Tiwa decides.

**Scope note:** DEC-133 (G5 — movement resolution granularity) is itself Ruled. This brief
addresses only the two items DEC-133 explicitly left open: **G1** (movement-penalty
magnitude table) and **G3** (duration/time-unit scale).

---

## 1. G1 — Movement-penalty magnitude table

### 1.1 What currently exists

| Precedent | Mechanism | Source |
|---|---|---|
| General Condition penalty pattern | `Tier-Y Condition Value Z`, `Z = −Y` — flat overlay equal to the Condition's own Tier | DEC-079 C1/C2 |
| Encumbered | Explicit **band ladder**, not flat −Y-by-Tier: Bands 1–5 = −1/−2/−3/−4/−5, keyed to relative load `E`, not to a "Tier" the character rolled for | DEC-078 R2/R3 |
| Slowed | Standard −Y overlay to Movement Speed + Body Skills; explicitly **does not stack with Encumbered** — worse penalty applies | DEC-079 |
| Total-lock Conditions (Stunned/Incapacitated/Restrained/Grappled/Prone) | Self-referential Y: `Y` = the stat's own current value, so `Effective Stat = 0` — not a magnitude table, a zeroing rule | DEC-122 |
| Prone crawl | `max(1, floor(Movement Speed / 2))` — a guaranteed-nonzero floor on top of the Prone total-lock | DEC-125 |

**The actual gap:** every Condition *currently in the alpha vocabulary* already has a defined
penalty mechanism (flat −Y, Encumbered's band ladder, or self-referential zero). G1 asks
whether Movement Speed penalties **in general** — including future Conditions/Effects not
yet authored — should be read off a **dedicated magnitude table**, or whether the existing
flat −Y overlay is the standing default for anything that doesn't get its own explicit
ladder (as Encumbered did).

### 1.2 Options

**Option A — No table. Flat −Y is the universal default.**
Any Condition that imposes a Movement Speed penalty uses `Z = −Y` (its own Tier) unless a
future ruling explicitly authors a different ladder for that specific Condition (Encumbered
precedent). G1 closes as "confirmed default, not a new mechanic."

- *For:* Zero new machinery. Matches your stated preference for flat mechanics over scaling
  complexity (Core Priority 3). Consistent with DEC-115's minimal-schema direction — one
  more table is one more thing to maintain and remember at the table.
- *Against:* Doesn't distinguish "a Tier-3 slap of gravel underfoot" from "a Tier-3
  waist-deep swamp" — both would produce the same −3 unless content-authored otherwise.

**Option B — Dedicated general-purpose magnitude table**, independent of Tier, e.g. banded
like Encumbered (a numeric input like terrain difficulty or load maps to a penalty band).

- *For:* Gives GMs a reusable tool for hazards/terrain (`env:terrain_hazardous`) beyond the
  case-by-case Condition-tier authoring DEC-023.A already allows.
- *Against:* Real risk of just **relocating** complexity rather than reducing it — you'd be
  authoring and remembering a second scale alongside Tier. `env:terrain_*` is already ruled
  descriptive-only (DEC-091) specifically to avoid this; a new table risks reopening that
  boundary by the back door.

**Option C — Hybrid: named Conditions keep their explicit ladder where one is already
ruled (Encumbered); everything else defaults to flat −Y (Option A) unless a future DEC
authors a specific ladder for it.**

- *For:* This is arguably just a restatement of the status quo — it changes nothing, it
  documents the rule that's already implicit across DEC-078/079/122/125.
- *Against:* If it's really just documentation, it's not clear G1 needs a ruling at all
  rather than a closure note.

### 1.3 Flag

Option A/C converge on: **G1 may already be closed in substance** — the flat −Y default is
the operative rule every existing Condition already follows, with Encumbered as the one
explicitly-authored exception. The open question for you is narrower than "what's the
table": it's **whether you want the authority to author band-ladders like Encumbered's to
be a standing, reusable option** (Option B/C) **or whether Encumbered should be treated as
a one-off exception that shouldn't set a precedent** (Option A, strict).

---

## 2. G3 — Duration/time-unit scale

### 2.1 What currently exists

| Precedent | What it defines | What it explicitly does NOT define |
|---|---|---|
| DEC-095 | Turn order, one substantive action per combat turn, round structure | Real-world duration of a turn or round |
| DEC-133 | Movement Distance per combat turn = effective Movement Speed; 1 Speed = 1 hex | Explicitly declines to define real-world duration — "does not define real-world duration (kept out of G3)" |
| DEC-070/074 | Extended Test completion target = GM discretion, no formula | Any time-unit scale for an interval |
| DEC-088 | `env:freezing` etc. are scene-state presence/absence | No duration/tick-rate for how long a scene-state persists |

**The actual gap:** nothing in Tiwas currently reads a real-world clock. Turn = abstract
unit; interval = abstract unit; scene = abstract unit. No subsystem is currently blocked on
this — it's an open design fork, not a load-bearing dependency.

### 2.2 Options

**Option A — No fixed duration, ever. Combat turns/rounds/intervals remain purely abstract
narrative units.**

- *For:* Zero new mechanics; nothing currently needs it (checked against Disengage/Zone of
  Control/Chase — see §2.3 below, none of them strictly require real seconds to function).
  Consistent with Priority 3 (minimum resolution steps).
- *Against:* Forecloses any future subsystem that wants to reason in real time — burning
  buildings, poison ticking on a clock rather than "per interval," multi-party sync across
  simultaneous scenes. Once foreclosed, reopening it later is a bigger lift than ruling it
  now.

**Option B — Fix a flat real-world value per combat turn (e.g., "~6 seconds"), with no
mechanical hooks yet — pure flavor/reference value GMs may narrate against, not consumed
by any formula.**

- *For:* Cheap. Gives GMs a narration anchor ("that's about 30 seconds of fighting") without
  creating anything for a rule to read. Reversible — nothing built on it if you later change
  the number.
- *Against:* A number with literally zero mechanical function is the kind of thing that
  tends to attract feature creep once it exists (someone eventually proposes "and therefore
  fire spreads 1 hex per turn," etc.) — worth being explicit that adopting B does not imply
  any future formula gets to consume it without its own ruling.

**Option C — Tiered/context-variable: fix combat-turn duration (flavor only, per Option B),
but leave Extended Test / scene / campaign-scale duration fully GM-discretion, no formula —
mirroring the existing DEC-070/074 pattern for completion targets.**

- *For:* Reuses a pattern you've already ruled acceptable twice (S-9/10, S-11). Doesn't
  invent a new governance shape.
- *Against:* Slight inconsistency in that combat gets a fixed anchor and everything longer
  doesn't — though this mirrors how DEC-133 itself already treats combat (hex/turn) as more
  concretely specified than everything else.

### 2.3 Flag — is anything actually blocked on G3?

Checked against DEC-133's own explicitly-deferred list (Disengage, Zone of Control, Chase,
generic movement contests, Forced Movement magnitude, Pin/Hold Position, Seize/Deny
Ground): **none of these appear to require a real-world time value to resolve** — they all
read naturally off the existing turn/hex/Speed substrate (DEC-133) without needing seconds.
If that's correct, G3 is **not currently blocking any queued work**, which may make Option A
(defer indefinitely, no ruling needed yet) a live option distinct from A/B/C above — i.e., a
fourth choice: **rule nothing now, revisit only if/when a specific subsystem needs it.**

---

## 3. Required Tiwa ruling(s)

Two independent decisions — G1 and G3 do not depend on each other:

- [ ] **G1:** Option A (strict flat-default, no table) / Option B (dedicated table) /
      Option C (Encumbered stays the sole named exception; everything else flat-default)
- [ ] **G3:** Option A (no duration, ever) / Option B (flavor-only fixed turn duration) /
      Option C (fixed turn + GM-discretion for everything longer) / **defer — not currently
      blocking anything**

No DEC number is assigned by this brief. On your ruling, this closes to OpenCode for
recording against the live register (DEC-133's carried-open G1/G3 cells).
