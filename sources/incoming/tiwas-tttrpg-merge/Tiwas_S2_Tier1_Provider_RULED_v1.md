# Tiwas — S-2 Tier-1 Location Index Provider: RULED (v1.0)

**Status: LOCKED.** Formally ruled by the designer: **Zero-Step is the accepted Tier-1 Location Index
provider.** This closes the formula-selection question S-2 v1.1 originally left open (§C.2, "Trade-off,
not hierarchy") and that five rounds of experimental collaboration between Claude and ChatGPT resolved
through evidence. **This ruling closes only the Tier-1 formula question.** The broader S-2 residual —
Tier 0/1/2 situational policy, and the anatomical index-to-zone mapping subsystem — remains open, exactly
as scoped throughout every prior round.

**Chain:** S-2 v1.1 → experiment (r1) → ChatGPT r2 → response → ChatGPT r3 → exhaustive sweep → ChatGPT r4
→ documentation package → ChatGPT r5 → corrected package (v1.1) → **designer ruling** → this document.

---

## A. The Ruling

> **Zero-Step is the accepted Tier-1 Location Index provider for Tiwas.**
> Ruled by the designer. Units-Digit is retained in the design record as a documented, optional,
> specialised alternative — not deleted, not deprecated to silence.

Made with E9's human-playtest component (round 5 §B.3) still open — one of the two paths that document
explicitly offered as legitimate ("rule now, accepting E9's human component as a small bounded risk, or
wait for playtest data first"). This is a recorded, informed acceptance of a disclosed gap, not an
oversight, and it's noted as such rather than quietly dropped.

---

## B. Frozen Evidence Record (E1–E9)

Final. No longer "pending" — carried forward unchanged from round 5 except for tense, now that it
supports an actual ruling rather than a recommendation.

| ID | Finding |
|---|---|
| E1 | Domain resolution: Zero-Step provides 100 native index values (1% resolution); Units-Digit provides 10 (10% resolution). |
| E2 | Uniform six-zone accuracy: Zero-Step's maximum distribution error was exactly 1/10 of Units-Digit's (0.667pp vs. 6.667pp) — algebraically exact. |
| E3 | Weighted seven-zone accuracy: Units-Digit made a low-weight (3%) zone entirely unreachable; Zero-Step reproduced that specific table exactly — a property of that table's weights aligning with the 100-point domain, not general evidence of Zero-Step's accuracy on arbitrary tables. |
| E4 | Structural unreachability: that same low-weight zone was unreachable under Units-Digit in **all 5,040 possible orderings** of the table — proven algebraically, not merely observed. |
| E5 | Shared order-dependence: both providers inherited table-order-dependent symmetry breaks from the tested largest-remainder apportionment, at the identical frequency (80% of 720 orderings) on a table whose weights didn't divide evenly into either domain. |
| E6 | Order-error magnitude: when order-dependence fired, Units-Digit's worst-case gap was exactly 10× Zero-Step's — a provable consequence of the domain-size ratio. |
| E7 | MAE invariance: under the tested apportionment, table order changed which zone absorbed rounding error, never the total error — proven algebraically, confirmed exhaustively. Retained as a general test-design lesson beyond S-2 itself. |
| E8 | Pair-aware repair: a tested symmetry-preserving apportionment variant restored declared L/R equality but raised overall mean error and did not fix the unreachable-zone problem. Logged as a rejected experimental repair — not proof no repair could work. |
| E9 | Derivation-stage usability: structural analysis established Units-Digit needs 0–1 extra operations across four practical rolling modes, Zero-Step needs 1–2. **Human-playtest component was never run; the ruling proceeded with this accepted as open** (§A). |

---

## C. Reference Text for the Documents Being Updated

**Caveat, stated plainly before this section:** my project files are `Tiwas_Core_Rules_v2.md` and
`Tiwas_Universal_System_Synthesized_Roadmap.md`. I don't have documents by the names ChatGPT cited —
"Canonical Rules & Changelog," "Proposals, WIP & Design Direction" — directly. They may be the same
documents under different names in your ChatGPT workspace, later-evolved versions, or reorganized files I
simply can't see. §C.1 (Roadmap) is reliable — I have that file. §C.2–C.3 are content-level reference
only, offered for Work mode's reconciliation to cross-check against, not a claim that it matches those
documents' actual current wording or structure.

### C.1 Roadmap annotation (reliable — I have this file directly)

Carried forward from round 5 §C.4, de-hedged now that the ruling exists:

| Priority | ID | Gap | Status | Primary dependency |
|---:|---|---|---|---|
| 2 | S-2 | Hit-location policy: Tier 0/1/2 and situation use. **Tier-1 provider: Zero-Step — ruled.** Separate from, and does not resolve, the decision of when Tier 1 is used at all, which remains Open. | **Provider: Ruled (Zero-Step) / Tier policy: Open** | S-1 |

### C.2 Rule text (content-level reference only — see caveat above)

> ## Tier-1 Location Index Provider
>
> **Status: Ruled.** Zero-Step is the accepted provider. *This rules which formula to use **if and when**
> Tier 1 is selected — it does not rule that Tier 1 itself is used in a given scene; that remains the
> open, situational Tier 0/1/2 policy question.*
>
> | Provider | Native domain | Native resolution | Mapping-stage-free condition |
> |---|---|---|---|
> | Zero-Step | 1–100 | 1 percentage point | None for arbitrary weighted tables |
> | Units-Digit | 1–10 | 10 percentage points | Exactly ten equal-weight zones |
>
> Units-Digit is retained as a specialised coarse provider — documented, not deleted — for tables with
> exactly ten equal-weight zones, or modes that deliberately trade fidelity for minimal derivation cost.
>
> The choice of Tier-1 provider does not determine the anatomical mapping algorithm — that remains a
> separate, unresolved subsystem.
>
> Full supporting evidence: §B above (E1–E9).

### C.3 Proposals/WIP status (content-level reference only)

Wherever the Zero-Step-vs-Units-Digit question is currently presented as an unresolved proposal, it should
be marked ruled, pointing to §A/§B above, and moved out of "open proposals" into "ruled" or whatever
equivalent category that document uses — exact mechanics depend on its actual structure, which I can't see.

### C.4 Step 6 — non-canonical player-choice design notes

I don't have the "future player-choice ideas" content ChatGPT's step 6 references anywhere in this thread
— nothing about letting players choose between providers at the table has come up here. I can't draft that
piece without seeing what it actually says; happy to fold it in if you share it.

---

## D. What This Ruling Does Not Touch

Unchanged, restated once more for a single closing reference point:

- Tier 0/1/2 situational policy — open
- The anatomical location table itself — doesn't exist yet
- The index-to-zone apportionment/mapping algorithm — largest-remainder was an experimental tool only
- Symmetry-preservation mechanics for that future algorithm — open
- Tier 2's internal mechanics — open
- E9's human-playtest component — open, accepted as a disclosed risk (§A)

---

## E. Status

This closes Claude's side of the S-2 Tier-1 provider experiment. Steps 2–7 of ChatGPT's plan are in
progress via Work mode; §C above is offered as a cross-check for that reconciliation, not a substitute for
it. If the resulting file edits come back this way for review, I'm glad to check them against the evidence
record in §B.
