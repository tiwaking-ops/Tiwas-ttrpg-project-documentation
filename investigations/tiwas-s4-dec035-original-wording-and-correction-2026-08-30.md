# S-4 — DEC-035 Original Designer Wording and Correction Record

**Date:** 2026-08-30
**Status:** Non-canonical design evidence — documents an LLM misreading of a designer statement and its correction
**Purpose:** Preserve the designer's original verbatim wording so future sessions do not repeat the distortion, and record why the recorded "severity = accumulated count" rule is superseded.

---

## 1. The designer's original statements (verbatim)

The designer (Tiwa) originally stated:

> "wound is a lasting effect not hit point damage.
> S-3 has ruled for effects from a success which are gated.
> localized wound is recorded. caused by an action which caused an effect.
> intended wound states should only be recorded numerically. **more wounds = more severe.** a single wound might not bother an adult, but would be dangerous to a child. each individual wound is functionally equivalent."

## 2. The misreading

Gemini 3.6 Flash (and subsequently DeepSeek Harness) interpreted the phrase **"more wounds = more severe"** as a mechanical rule that **severity is produced by an accumulated count of wounds** — i.e. "how many light wounds until someone becomes seriously wounded?"

That interpretation is **incorrect**. The designer clarifies:

> "This is incorrect. A 'serious wound' is an actual effect. we have S-3 gated effects which can cause these things. 'how many light wounds until someone becomes seriously wounded?' it depends on the character. but a serious wound will cause a character to become seriously wounded by definition."

So:
- **Severity/quality comes from the S-3 gated Effect** that inflicts the wound, not from accumulating count.
- A **"Serious wound" is a distinct S-3 Effect** which, **by definition**, makes the character seriously wounded.
- The sentence "more wounds = more severe" was casual phrasing about the *consequence/load* of many wounds — not a definition of what makes a wound "serious."

## 3. What the phrase actually means (designer clarification)

When the designer said "more wounds = more severe," the intended meaning is about the **mechanical load** a character accumulates:

- Wounds cause **debilitating (mechanical negative) effects** on attributes.
- More wounds / more severe wounds → more mechanical negatives.
- Accumulating too many negatives → the character is "game overed."
- A weaker character (with weaker/lesser resources) reaches that failure point **faster**.

This is a **consequence** model, not a **severity-category-generation** model. Count does not generate descriptive tiers; count feeds the accumulating penalty that drives a character toward failure.

## 4. What this corrects in the record

- **DEC-035** as previously recorded ("Wound severity is numerical — number of Wounds inflicted; Light/Serious/Critical are descriptive categories for accumulated numerical Wounds") is **superseded/corrected**. New wording: severity/quality comes from the **S-3 gated Effect**; a Serious wound is a distinct S-3 Effect that by definition seriously wounds the character; what varies by character is capacity to *endure* mechanical negatives, not what makes a wound "serious."
- **OPEN-006** ("numerical thresholds for Light/Serious/Critical categories") was **mis-framed** and is closed via corrected DEC-035 — no count-to-tier gate exists.
- **OPEN-007** (wound consequences) is **ruled** as the individual mechanical attribute-penalty / endgame model above.

## 5. Broader process note (designer)

> "I need to be more careful talking to LLM's as they hyper-fixate on the weirdest things."

This record exists so the original wording and the correction are both preserved verbatim and so a future session can distinguish the designer's actual meaning from any LLM paraphrase.
