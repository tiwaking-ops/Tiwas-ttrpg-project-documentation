"""
Tiwas -- The Bargle Incident: executed playtest simulation.

Advisory / non-canonical. No DEC assigned. This script exists purely to run the
adventure module (tiwas-adventure-the-bargle-incident-2026-09-13.md) with real
random rolls (random.SystemRandom(), OS entropy) rather than the illustrative
worked examples in the written module, per standing Tiwas playtest methodology.

Implements, with citations:
  - Core Test Transaction (Canonical S6): roll -> outcome -> cost -> overflow ->
    failure XP -> skill roll pool -> (advanced skill) -> recovery.
  - 100-Fumble (Canonical S2.3): roll of 100 always fails.
  - Doubles / Advanced Skill creation (Canonical S12; DEC-012; DEC-087 creatures
    excluded; DEC-086 creature signature skills start at full Cap).
  - S-1 opposed contest / DEC-105 standardized melee-exchange algorithm.
  - DEC-096/097/104 contest-delta Inflict Injury.
  - DEC-103 Skill-Tier shred + margin de-escalation for non-HP Effects.
  - DEC-014 Zero-Step Location Index; DEC-100 Tier-1 quartiles; DEC-041(3) parity.
  - DEC-102 Wound target selection (creature = random attribute; "player choice"
    is substituted with the same rng stream in this unattended run -- flagged).
  - DEC-035.A Wound record format; DEC-004 live recalculation of derived stats.
  - DEC-079/DEC-122 Prone Condition (Skill-side penalty, DEC-063/072 pattern).
  - DEC-106 creature multi-attack (Goblin has 2 legal combat actions; Bargle 1).
  - DEC-030/DEC-114 Armor Bypass Tag+Location match / fail-and-fall-back.
  - DEC-067/068/070/071/073 S-11 healing as an Extended Test instance.
  - DEC-052/DEC-108 forced incapacitation at HP=0, uncapped negative HP.

Scripting conventions used where the corpus leaves a choice to a live human
(documented, not presented as a rule):
  - Effect declaration policy is a fixed rotation per attacking skill (see
    EFFECT_POLICY below), standing in for DEC-025's "declared intent."
  - DEC-102 "Player chooses" wound-target-attribute clauses are resolved by the
    same rng stream (no live human present in an unattended run).
  - Prone auto-clears at the start of the Prone character's next turn (free
    movement to stand, DEC-082), matching the written module's convention.
  - Armor Bypass location-matching is simplified to "target has ANY
    `defense:armor` tag" rather than the full DEC-137 sub-zone address --
    a documented scripting simplification, not a ruling.
  - S-11 healing HP-restoration amount = accumulated Margin total (DEC-074
    leaves this GM discretion; no fixed formula is ruled).
"""

import csv
import json
import random
from copy import deepcopy

rng = random.SystemRandom()

DOUBLES = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100}


def roll_d100():
    return rng.randint(1, 100)


def zero_step(natural_roll):
    """DEC-014: exchange tens/units digits; 0 -> 100 under the 00=100 rule."""
    tens = (natural_roll // 10) % 10
    units = natural_roll % 10
    swapped = units * 10 + tens
    if swapped == 0:
        swapped = 100
    return swapped


def quartile(location_index):
    """DEC-100 Tier-1 coarse zones."""
    if 1 <= location_index <= 25:
        return "Legs"
    if 26 <= location_index <= 50:
        return "Torso"
    if 51 <= location_index <= 75:
        return "Arms"
    return "Head"


def laterality(location_index):
    """DEC-041(3): parity of the Zero-Step output's units digit."""
    return "Left" if (location_index % 10) % 2 == 1 else "Right"


# ---------------------------------------------------------------------------
# Character construction
# ---------------------------------------------------------------------------

def make_character(name, body_attrs, mind_attrs, skills, gear, is_pc_like):
    """
    body_attrs / mind_attrs: dict of 12 attribute codes -> value each.
    skills: dict name -> {"tier": int, "attrs": [codes], "domain": "PE"/"MP",
                           "signature": bool, "start_mode": "half"/"full"/"roll"}
    """
    attrs = {}
    attrs.update(body_attrs)
    attrs.update(mind_attrs)
    char = {
        "name": name,
        "attrs": attrs,
        "skills": {},
        "gear": gear,
        "is_pc_like": is_pc_like,
        "wounds": [],
        "conditions": {},  # e.g. {"Prone": tier}
        "advanced_skills_created": [],
        "general_xp": 0,
        "hp": 0,
        "pools": {"PE": 0, "MP": 0},
        "incapacitated": False,
    }
    recompute_derived(char)
    for sname, sdef in skills.items():
        add_skill(char, sname, sdef["tier"], sdef["attrs"], sdef["domain"],
                  sdef["signature"], sdef["start_mode"])
    char["hp"] = char["derived"]["HP"]
    char["pools"]["PE"] = char["derived"]["PE"]
    char["pools"]["MP"] = char["derived"]["MP"]
    return char


def recompute_derived(char):
    """Canonical S4: live derived statistics (DEC-004)."""
    a = char["attrs"]
    body = ["bpp", "bps", "bpe", "bpx", "bsp", "bss", "bse", "bsx", "bep", "bes", "bee", "bex"]
    mind = ["mpp", "mps", "mpe", "mpx", "msp", "mss", "mse", "msx", "mep", "mes", "mee", "mex"]
    hp_max = sum(a[c] for c in body)
    mp_max = sum(a[c] for c in mind)
    char["derived"] = {
        "HP": hp_max,
        "MP": mp_max,
        "PE": a["bep"] + a["bes"] + a["bee"],
        "Speed": a["bsp"] + a["bss"] + a["bse"],
        "EnergyRegen": a["bep"] + a["bes"],
        "MPRegen": a["mep"] + a["mes"],
        "MovementSpeed": (a["bsp"] + a["bss"]) // 15,
    }
    # Recompute every skill's Cap from the (possibly changed) attribute set.
    for sname, sk in char.get("skills", {}).items():
        sk["cap"] = sum(a[c] for c in sk["attrs"]) // len(sk["attrs"])


def add_skill(char, name, tier, attr_list, domain, signature, start_mode):
    cap = sum(char["attrs"][c] for c in attr_list) // len(attr_list)
    if start_mode == "half":
        start = cap // 2
    elif start_mode == "full":
        start = cap  # DEC-086 veteran signature convention
    else:
        start = cap  # placeholder; "roll" mode resolved at creation time by caller
    char["skills"][name] = {
        "tier": tier, "attrs": list(attr_list), "domain": domain,
        "signature": signature, "cap": cap, "current": start,
    }


def apply_attribute_change(char, attr_code, delta):
    char["attrs"][attr_code] += delta
    old_hp_max = char["derived"]["HP"]
    old_mp_max = char["derived"]["MP"]
    recompute_derived(char)
    # Clamp current pools/HP at the (possibly lowered) new maxima.
    if char["derived"]["HP"] < old_hp_max:
        char["hp"] = min(char["hp"], char["derived"]["HP"])
    if char["derived"]["MP"] < old_mp_max:
        char["pools"]["MP"] = min(char["pools"]["MP"], char["derived"]["MP"])
    if char["derived"]["PE"] < old_hp_max:  # PE never tied to HP; guard unused
        pass


# ---------------------------------------------------------------------------
# Core Test Transaction
# ---------------------------------------------------------------------------

def core_test(char, skill_name, rolls_log, scene, round_no, exch_id, actor_role):
    sk = char["skills"][skill_name]
    domain = sk["domain"]
    roll = roll_d100()
    skill_val = sk["current"]
    success = (roll <= skill_val) and (roll != 100)  # 100-Fumble, Canonical S2.3
    cost = roll
    pool_before = char["pools"][domain]
    pool_after = pool_before - cost
    overflow = 0
    if pool_after < 0:
        overflow = -pool_after
        pool_after = 0
        char["hp"] -= overflow
    char["pools"][domain] = pool_after

    failure_xp = max(0, roll - skill_val)
    skill_before = skill_val
    if not success:
        pool_xp = failure_xp
        while pool_xp >= sk["current"] and sk["current"] < sk["cap"]:
            pool_xp -= sk["current"]
            sk["current"] += 1
        char["general_xp"] += pool_xp

    is_double = roll in DOUBLES
    advanced_created = None
    if not success and is_double and char["is_pc_like"]:
        advanced_created = create_advanced_skill(char, skill_name)

    regen_key = "EnergyRegen" if domain == "PE" else "MPRegen"
    recovered = char["derived"][regen_key] // 2
    max_pool = char["derived"][domain]
    char["pools"][domain] = min(max_pool, char["pools"][domain] + recovered)

    margin = (skill_val - roll) if success else 0

    rolls_log.append({
        "scene": scene, "round": round_no, "exch_id": exch_id, "actor": char["name"],
        "role": actor_role, "skill": skill_name, "skill_tier": sk["tier"],
        "skill_value_at_roll": skill_before, "roll": roll, "success": success,
        "margin": margin, "cost": cost, "overflow": overflow, "failure_xp": failure_xp,
        "skill_value_after": sk["current"], "is_double": is_double,
        "advanced_skill_created": advanced_created or "",
        "pool_domain": domain, "pool_after_recovery": char["pools"][domain],
        "hp_after": char["hp"],
    })
    return {"roll": roll, "success": success, "margin": margin, "overflow": overflow,
            "is_double": is_double}


def create_advanced_skill(char, base_skill_name):
    sk = char["skills"][base_skill_name]
    domain = sk["domain"]
    body = ["bpp", "bps", "bpe", "bpx", "bsp", "bss", "bse", "bsx", "bep", "bes", "bee", "bex"]
    mind = ["mpp", "mps", "mpe", "mpx", "msp", "mss", "mse", "msx", "mep", "mes", "mee", "mex"]
    pool = body if domain == "PE" else mind
    candidates = [c for c in pool if c not in sk["attrs"]]
    if not candidates:
        return None
    new_attr = max(candidates, key=lambda c: char["attrs"][c])
    new_attrs = sk["attrs"] + [new_attr]
    new_tier = sk["tier"] + 1
    new_cap = sum(char["attrs"][c] for c in new_attrs) // new_tier

    # Named convention matching the written module: Rowan's Attack -> "Power
    # Strike" (rolled start); Aleena's Defense -> "Iron Faith" (flat start 1).
    if char["name"] == "Rowan" and base_skill_name == "Attack":
        new_name = "Power Strike"
        roll_for_start = roll_d100()
        start = min(roll_for_start, new_cap)
    elif char["name"] == "Aleena" and base_skill_name == "Defense":
        new_name = "Iron Faith"
        start = 1
    else:
        new_name = f"{base_skill_name} (Advanced)"
        start = 1

    if new_name in char["skills"]:
        return None  # DEC-012.2: same Advanced Skill cannot be created twice
    char["skills"][new_name] = {
        "tier": new_tier, "attrs": new_attrs, "domain": domain,
        "signature": False, "cap": new_cap, "current": start,
    }
    char["advanced_skills_created"].append(new_name)
    return new_name


# ---------------------------------------------------------------------------
# S-1 opposed contest / DEC-105 melee exchange
# ---------------------------------------------------------------------------

def shred_and_deescalate(atk_tier, def_tier, base_tier, defender_won, defender_margin):
    """DEC-103: Skill-Tier shred then margin de-escalation. Returns final tier
    (0 = Effect negated)."""
    mag = base_tier
    if atk_tier == def_tier:
        mag -= 1
    elif def_tier > atk_tier:
        mag -= (def_tier - atk_tier)
    else:
        mag += 1
    if defender_won:
        mag -= defender_margin
    # Unified carry rule: floor at 0 -> negated (simplified: no cascading
    # sub-tier borrowing beyond zero for this small-scale playtest).
    return max(0, mag)


def declare_effect_rowan(exch_count_for_skill, skill_tier):
    if skill_tier < 2:
        return "injury"
    m = exch_count_for_skill % 4
    if m == 0:
        return "armor_bypass"
    if m in (1, 2):
        return "wound"
    return "injury"


def declare_effect_bargle(hit_count):
    m = hit_count % 3
    if m == 0:
        return "wound"
    if m == 1:
        return "armor_bypass"
    return "injury"


def has_armor_tag(char):
    return any("defense:armor" in item.get("tags", []) for item in char["gear"])


def resolve_wound_or_condition(attacker, defender, atk_skill_name, atk_roll, atk_margin,
                                def_margin, defender_succeeded, kind, effects_log, ctx,
                                def_skill_tier):
    sk = attacker["skills"][atk_skill_name]
    li = zero_step(atk_roll)
    zone = quartile(li)
    side = laterality(li)
    final_tier = shred_and_deescalate(sk["tier"], def_skill_tier, sk["tier"],
                                       defender_succeeded, def_margin)
    note = ""
    if final_tier <= 0:
        note = "Effect fully negated by shred + de-escalation (DEC-103 carry rule)."
        effects_log.append({**ctx, "declared_effect": kind, "location_index": li,
                             "zone": zone, "laterality": side, "effect_tier": 0,
                             "effect_magnitude": 0, "wound_attribute": "",
                             "hp_change": 0, "notes": note})
        return

    if kind == "trip":
        existing = defender["conditions"].get("Prone", 0)
        if final_tier > existing:
            defender["conditions"]["Prone"] = final_tier
            note = f"Prone imposed/raised to Tier-{final_tier}."
        else:
            note = f"Prone attempt Tier-{final_tier} did not exceed existing Tier-{existing} (non-stacking, DEC-079)."
        effects_log.append({**ctx, "declared_effect": kind, "location_index": li,
                             "zone": zone, "laterality": side, "effect_tier": final_tier,
                             "effect_magnitude": -final_tier, "wound_attribute": "",
                             "hp_change": 0, "notes": note})
        return

    # kind == "wound"
    candidates = [c for c in sk["attrs"] if c in defender["attrs"]]
    chosen = rng.choice(candidates)  # DEC-102: creature random / player-choice
    apply_attribute_change(defender, chosen, -final_tier)
    defender["wounds"].append({
        "location": f"{zone} ({side})", "tier": final_tier, "magnitude": -final_tier,
        "attribute": chosen,
    })
    note = f"Wound: {zone} ({side}) Tier-{final_tier}, attribute {chosen} -{final_tier}."
    effects_log.append({**ctx, "declared_effect": kind, "location_index": li,
                         "zone": zone, "laterality": side, "effect_tier": final_tier,
                         "effect_magnitude": -final_tier, "wound_attribute": chosen,
                         "hp_change": 0, "notes": note})


def resolve_injury_or_bypass(attacker, defender, atk_margin, def_margin,
                              defender_succeeded, kind, effects_log, ctx):
    dmg = atk_margin - (def_margin if defender_succeeded else 0)
    dmg = max(1, dmg)  # DEC-104: never 0 on a win
    tag_note = ""
    if kind == "armor_bypass":
        matched = has_armor_tag(defender)
        tag_note = ("Tag+Location match: defense:armor present (simplified coarse "
                    "match, not full DEC-137 address)." if matched else
                    "No defense:armor tag on target -> DEC-030 fail-and-fall-back "
                    "to Base Inflict Injury.")
        tag_note += (" NOTE: no numeric plain-armor mitigation formula exists in the "
                     "ruled corpus, so match vs. fallback produce an IDENTICAL numeric "
                     "outcome here -- a genuine completeness gap, not a script bug.")
    defender["hp"] -= dmg
    effects_log.append({**ctx, "declared_effect": kind, "location_index": "",
                         "zone": "", "laterality": "", "effect_tier": "",
                         "effect_magnitude": "", "wound_attribute": "",
                         "hp_change": -dmg, "notes": tag_note})


def run_exchange(attacker, atk_skill_name, defender, def_skill_name, scene, round_no,
                  exch_counter, declared_effect, rolls_log, effects_log,
                  bargle_hit_counter=None, rowan_hit_counter=None):
    exch_id = exch_counter[0]
    exch_counter[0] += 1
    repeats = 0
    while True:
        repeats += 1
        if repeats > 20:
            effects_log.append({
                "scene": scene, "round": round_no, "exch_id": exch_id,
                "attacker": attacker["name"], "defender": defender["name"],
                "atk_skill": atk_skill_name, "def_skill": def_skill_name,
                "declared_effect": "REPEAT_CAP_HIT", "location_index": "", "zone": "",
                "laterality": "", "effect_tier": "", "effect_magnitude": "",
                "wound_attribute": "", "hp_change": 0,
                "notes": "20 repeat-contest safety cap reached; exchange abandoned "
                         "(script safety limit, not a rule).",
            })
            return
        atk = core_test(attacker, atk_skill_name, rolls_log, scene, round_no, exch_id, "attacker")
        dfn = core_test(defender, def_skill_name, rolls_log, scene, round_no, exch_id, "defender")

        if attacker["hp"] <= 0 or defender["hp"] <= 0:
            return  # Overflow during these very rolls may have ended the fight

        if atk["success"] and not dfn["success"]:
            winner_is_attacker, atk_margin, def_margin, def_succeeded = True, atk["margin"], 0, False
        elif dfn["success"] and not atk["success"]:
            # Defender wins: attack fails outright, no counter-Effect (DEC-101)
            effects_log.append({
                "scene": scene, "round": round_no, "exch_id": exch_id,
                "attacker": attacker["name"], "defender": defender["name"],
                "atk_skill": atk_skill_name, "def_skill": def_skill_name,
                "declared_effect": "defender_wins_no_effect", "location_index": "",
                "zone": "", "laterality": "", "effect_tier": "", "effect_magnitude": "",
                "wound_attribute": "", "hp_change": 0,
                "notes": "DEC-101: defender wins, attack fails, no counter-Effect.",
            })
            return
        elif atk["success"] and dfn["success"]:
            if atk["margin"] == dfn["margin"]:
                continue  # exact Quality tie -> repeat, DEC-013 S13.5
            winner_is_attacker = atk["margin"] > dfn["margin"]
            if winner_is_attacker:
                atk_margin, def_margin, def_succeeded = atk["margin"], dfn["margin"], True
            else:
                effects_log.append({
                    "scene": scene, "round": round_no, "exch_id": exch_id,
                    "attacker": attacker["name"], "defender": defender["name"],
                    "atk_skill": atk_skill_name, "def_skill": def_skill_name,
                    "declared_effect": "defender_wins_both_succeeded", "location_index": "",
                    "zone": "", "laterality": "", "effect_tier": "", "effect_magnitude": "",
                    "wound_attribute": "", "hp_change": 0,
                    "notes": "Both succeeded; defender's Margin was higher -> defender wins, no counter-Effect.",
                })
                return
        else:
            continue  # both fail -> repeat, DEC-013 S13.4

        break

    ctx = {"scene": scene, "round": round_no, "exch_id": exch_id,
           "attacker": attacker["name"], "defender": defender["name"],
           "atk_skill": atk_skill_name, "def_skill": def_skill_name}
    def_skill_tier = defender["skills"][def_skill_name]["tier"]

    if declared_effect in ("wound", "trip"):
        resolve_wound_or_condition(attacker, defender, atk_skill_name, atk["roll"],
                                    atk_margin, def_margin, def_succeeded, declared_effect,
                                    effects_log, ctx, def_skill_tier)
    else:
        resolve_injury_or_bypass(attacker, defender, atk_margin, def_margin, def_succeeded,
                                  declared_effect, effects_log, ctx)

    if defender["hp"] <= 0:
        defender["incapacitated"] = True  # DEC-052


def apply_prone_penalty(char, base_skill_name):
    """Returns the skill name to actually roll with: if Prone, a Skill-side
    -Y penalty (DEC-079/063 pattern) is represented here as a temporary skill
    value reduction restored after the roll."""
    tier = char["conditions"].get("Prone", 0)
    if tier <= 0:
        return None
    sk = char["skills"][base_skill_name]
    original = sk["current"]
    sk["current"] = max(0, sk["current"] - tier)
    return original


def clear_prone_if_present(char):
    if char["conditions"].get("Prone", 0) > 0:
        char["conditions"]["Prone"] = 0  # free movement to stand, DEC-082
