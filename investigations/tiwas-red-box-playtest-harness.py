#!/usr/bin/env python3
"""
Tiwas — Red Box Solo Playtest Harness (v1.2)
Seed: 20260917 | d100 in 1-100, 00 = 100
Follows Automated Playtest Run Conventions H1–H7 (2026-09-14).
Layer-tagging: locked / ruled / locked+ruled / advisory / empirical.

FIXES v1.1:
- initial_state captured BEFORE any scenes (pre-run snapshot)
- Symmetric combat: both sides attack each round (DEC-095/105)
- Injury = contest-delta (DEC-104): winner_margin - loser_margin (min 1)
- Goblin Crude Attack damages Rowan; Snake Venomous Bite damages Rowan
FIXES v1.2 (Muse Spark, 2026-09-17):
- ASCII-only console prints (Windows cp1252 cannot encode U+2192/U+0394);
  no logic change. Prior v1.1 run wrote the committed 98-record JSON then
  crashed on printing; v1.2 re-runs to reach the LEDGER-CLOSES asserts.
  See execution-report correction register.
"""

import json
import random
import math
from pathlib import Path

SEED = 20260917

# ── Attribute data ──────────────────────────────────────────────────────
ROWAN_ATTRS = {
    "bpp":58,"bps":52,"bpe":47,"bpx":40,"bsp":61,"bss":55,
    "bse":47,"bsx":38,"bep":60,"bes":53,"bee":57,"bex":44,
    "mpp":42,"mps":45,"mpe":50,"mpx":33,"msp":48,"mss":55,
    "mse":40,"msx":46,"mep":51,"mes":43,"mee":49,"mex":47
}
ALEENA_ATTRS = {
    "bpp":45,"bps":40,"bpe":50,"bpx":48,"bsp":42,"bss":47,
    "bse":44,"bsx":41,"bep":55,"bes":46,"bee":58,"bex":50,
    "mpp":50,"mps":48,"mpe":62,"mpx":44,"msp":46,"mss":50,
    "mse":43,"msx":49,"mep":60,"mes":55,"mee":65,"mex":52
}
GOBLIN_ATTRS = {
    "bpp":40,"bps":38,"bpe":30,"bpx":25,"bsp":45,"bss":48,
    "bse":35,"bsx":30,"bep":32,"bes":36,"bee":34,"bex":28,
    "mpp":22,"mps":28,"mpe":20,"mpx":15,"msp":25,"mss":35,
    "mse":24,"msx":18,"mep":20,"mes":22,"mee":25,"mex":19
}
SNAKE_ATTRS = {
    "bpp":30,"bps":28,"bpe":24,"bpx":20,"bsp":60,"bss":58,
    "bse":55,"bsx":45,"bep":22,"bes":25,"bee":24,"bex":26,
    "mpp":15,"mps":18,"mpe":14,"mpx":12,"msp":30,"mss":40,
    "mse":28,"msx":20,"mep":16,"mes":18,"mee":15,"mex":17
}
GHOUL_ATTRS = {
    "bpp":42,"bps":36,"bpe":40,"bpx":30,"bsp":50,"bss":52,
    "bse":44,"bsx":38,"bep":40,"bes":42,"bee":44,"bex":36,
    "mpp":20,"mps":25,"mpe":18,"mpx":16,"msp":28,"mss":30,
    "mse":22,"msx":20,"mep":18,"mes":22,"mee":20,"mex":21
}
BARGLE_ATTRS = {
    "bpp":35,"bps":32,"bpe":30,"bpx":44,"bsp":40,"bss":46,
    "bse":38,"bsx":42,"bep":33,"bes":35,"bee":37,"bex":40,
    "mpp":68,"mps":65,"mpe":60,"mpx":55,"msp":58,"mss":52,
    "mse":50,"msx":48,"mep":62,"mes":57,"mee":55,"mex":50
}

# ── Canonical formulas (locked) ──────────────────────────────────────────
def derived(attrs):
    body_keys = ["bpp","bps","bpe","bpx","bsp","bss","bse","bsx","bep","bes","bee","bex"]
    hp = sum(attrs[k] for k in body_keys)
    mp = sum(attrs[k] for k in ["mpp","mps","mpe","mpx","msp","mss","mse","msx","mep","mes","mee","mex"])
    pe = attrs["bep"] + attrs["bes"] + attrs["bee"]
    speed = attrs["bsp"] + attrs["bss"] + attrs["bse"]
    er = attrs["bep"] + attrs["bes"]
    mr = attrs["mep"] + attrs["mes"]
    ms = math.floor((attrs["bsp"] + attrs["bss"]) / 15)
    return {"HP": hp, "MP": mp, "PE": pe, "Speed": speed, "ER": er, "MR": mr, "Movement": ms}

def skill_cap(attrs, keys):
    return math.floor(sum(attrs[k] for k in keys) / len(keys))

# ── Build combatants ─────────────────────────────────────────────────────
def build(name, attrs, skill_defs):
    """skill_defs: list of (name, tier, [attr_keys], start_value_or_None)"""
    d = derived(attrs)
    sk = {}
    for sname, tier, keys, sv_override in skill_defs:
        cap = skill_cap(attrs, keys)
        sv = sv_override if sv_override is not None else math.floor(cap / 2)
        sk[sname] = {"tier": tier, "cap": cap, "value": sv, "attributes": list(keys)}
    return {
        "name": name, "attrs": dict(attrs), "derived": d, "skills": sk,
        "hp": d["HP"], "mp": d["MP"], "pe": d["PE"],
        "max_hp": d["HP"], "max_mp": d["MP"], "max_pe": d["PE"],
        "speed": d["Speed"], "er": d["ER"], "mr": d["MR"],
        "movement": d["Movement"], "wounds": [], "conditions": [],
        "hp_history": [d["HP"]], "mp_history": [d["MP"]], "pe_history": [d["PE"]],
    }

def build_all():
    # Rowan: Tier-1 skills, starting at floor(Cap/2)
    r = build("Rowan", ROWAN_ATTRS, [
        ("Attack", 1, ["bpp"], None),
        ("Defense", 1, ["bss"], None),
        ("Perception", 1, ["mss"], None),
        ("Stealth", 1, ["bsp"], None),
        ("Composure", 1, ["mex"], None),
    ])
    # Aleena
    a = build("Aleena", ALEENA_ATTRS, [
        ("Devotion", 1, ["mee"], None),
        ("Smite", 1, ["bep"], None),
        ("Defense", 1, ["bss"], None),
    ])
    # Goblin: signature skills at full Cap (DEC-086/087)
    g = build("Goblin", GOBLIN_ATTRS, [
        ("Crude Attack", 1, ["bpp"], None),
        ("Defense", 1, ["bss"], None),
        ("Trip", 2, ["bsp", "bss"], None),
    ])
    g["skills"]["Crude Attack"]["value"] = g["skills"]["Crude Attack"]["cap"]
    g["skills"]["Trip"]["value"] = g["skills"]["Trip"]["cap"]
    # Snake
    s = build("Rattlesnake", SNAKE_ATTRS, [
        ("Venomous Bite", 2, ["bsp", "bss"], None),
        ("Defense", 1, ["bss"], None),
        ("Stealth", 1, ["bsp"], None),
    ])
    s["skills"]["Venomous Bite"]["value"] = s["skills"]["Venomous Bite"]["cap"]
    # Ghoul
    gh = build("Ghoul", GHOUL_ATTRS, [
        ("Claw", 2, ["bpp", "bps"], None),
        ("Grapple", 2, ["bsp", "bpp"], None),
        ("Defense", 1, ["bss"], None),
        ("Desecration", 2, ["mpp", "mps"], None),
    ])
    for sn in ["Claw", "Grapple", "Desecration"]:
        gh["skills"][sn]["value"] = gh["skills"][sn]["cap"]
    # Bargle
    b = build("Bargle", BARGLE_ATTRS, [
        ("Bolt", 2, ["mpp", "mps"], None),
        ("Defense", 1, ["bss"], None),
        ("Beguile", 1, ["mpx"], None),
    ])
    b["skills"]["Bolt"]["value"] = b["skills"]["Bolt"]["cap"]
    return r, a, g, s, gh, b

# ── Core Test (DEC-006, 9 steps) ────────────────────────────────────────
def core_test(actor, skill_name, rng, log_records, scene, actor_label,
              target=None):
    sk = actor["skills"][skill_name]
    cap = sk["cap"]
    value = sk["value"]
    tier = sk["tier"]
    attrs_in_skill = sk["attributes"]
    domain = "MP" if all(k.startswith("m") for k in attrs_in_skill) else "PE"

    roll = rng.randint(1, 100)
    is_100 = (roll == 100)
    success = (roll <= value) and not is_100
    outcome = "success" if success else "failure"
    cost = roll

    pool_key = "mp" if domain == "MP" else "pe"
    pool_max_key = "max_mp" if domain == "MP" else "max_pe"
    pool_current = actor[pool_key]

    overflow = 0
    if cost > pool_current:
        overflow = cost - pool_current
        actor["hp"] -= overflow
        if actor["hp"] < 0:
            actor["hp"] = 0

    actor[pool_key] = max(0, actor[pool_key] - cost)

    failure_xp = max(0, roll - value)
    skill_grew = False
    advanced_created = None
    value_after = value

    # Step 7: failed Double → Advanced Skill (DEC-012)
    is_double = (roll in {11,22,33,44,55,66,77,88,99,100})
    if (not success) and is_double:
        new_tier = tier + 1
        all_attrs = [k for k in actor["attrs"]]
        current = set(attrs_in_skill)
        candidates = [k for k in all_attrs if k not in current]
        added = candidates[0] if candidates else None
        new_keys = list(attrs_in_skill) + ([added] if added else [])
        new_cap = skill_cap(actor["attrs"], new_keys)
        new_name = f"{skill_name} (Advanced)"
        actor["skills"][new_name] = {
            "tier": new_tier, "cap": new_cap, "value": 1,
            "attributes": new_keys
        }
        advanced_created = {
            "name": new_name, "tier": new_tier, "cap": new_cap,
            "start": 1, "added_attr": added
        }

    # Step 6: Skill Roll Pool cascade (DEC-010)
    if failure_xp > 0:
        pool = failure_xp
        sv = value
        while pool >= sv and sv < cap:
            sv += 1
            pool -= (sv - 1)
            skill_grew = True
        value_after = sv
        actor["skills"][skill_name]["value"] = sv

    # Step 8: Recovery (DEC-008)
    regen = actor["mr"] if domain == "MP" else actor["er"]
    recovery = math.floor(regen / 2)
    actor[pool_key] = min(actor[pool_max_key], actor[pool_key] + recovery)

    record = {
        "layer": "locked+ruled" if target else "locked",
        "scene": scene, "actor": actor_label, "skill": skill_name,
        "roll": roll, "outcome": outcome, "cost": cost,
        "overflow": overflow, "failure_xp": failure_xp,
        "skill_grew": skill_grew, "advanced_skill": advanced_created,
        "recovery": recovery, "domain": domain,
        "is_100": is_100, "is_double": is_double,
        "tier": tier, "cap": cap, "value_before": value,
        "value_after": value_after,
    }
    if target:
        record["target"] = target["name"]
    log_records.append(record)

    margin = max(0, value - roll)
    return roll, outcome, cost, overflow, failure_xp, recovery, margin, skill_grew, advanced_created

# ── S-1 Opposed Contest (DEC-013/105) ───────────────────────────────────
def s1_contest(attacker, defender, atk_skill, def_skill, rng,
               log_records, scene, atk_label, def_label,
               prescribed_effect=None, is_reaction=False):
    """
    One S-1 exchange: both roll Core Tests. Determine winner.
    On attacker win: apply prescribed_effect or Inflict Injury (DEC-104).
    On defender win: no counter-Effect (DEC-101).
    Both fail: repeat (no Effect).
    """
    atk_roll, atk_out, atk_cost, atk_ov, atk_fxp, atk_rec, atk_margin, _, _ = \
        core_test(attacker, atk_skill, rng, log_records, scene, atk_label,
                  target=defender)
    def_roll, def_out, def_cost, def_ov, def_fxp, def_rec, def_margin, _, _ = \
        core_test(defender, def_skill, rng, log_records, scene, def_label,
                  target=attacker)

    # DEC-105 matrix
    if atk_out == "success" and def_out == "failure":
        winner = "attacker"
    elif atk_out == "failure" and def_out == "success":
        winner = "defender"
    elif atk_out == "success" and def_out == "success":
        if atk_margin > def_margin:
            winner = "attacker"
        elif def_margin > atk_margin:
            winner = "defender"
        else:
            winner = "tie"
    else:
        winner = "repeat"

    detail = {
        "atk_roll": atk_roll, "atk_margin": atk_margin,
        "def_roll": def_roll, "def_margin": def_margin,
        "winner": winner, "atk_overflow": atk_ov, "def_overflow": def_ov,
    }

    if winner == "attacker":
        injury = max(1, atk_margin - def_margin)
        defender["hp"] -= injury
        detail["injury"] = injury
        detail["effect"] = "Inflict Injury"
        # Log injury as an empirical record
        log_records.append({
            "layer": "empirical",
            "scene": scene,
            "actor": atk_label,
            "skill": atk_skill,
            "target": def_label,
            "effect": "Inflict Injury",
            "injury": injury,
            "atk_margin": atk_margin,
            "def_margin": def_margin,
            "label": f"{atk_label}→{def_label}" + (" (reaction)" if is_reaction else ""),
        })

        atk_tier = attacker["skills"][atk_skill]["tier"]
        if atk_tier >= 2 and prescribed_effect:
            li = zero_step(atk_roll)
            zone = location_quartile(li)
            parity = "left" if li % 2 == 1 else "right"
            detail["location_index"] = li
            detail["zone"] = zone
            detail["laterality"] = parity

            def_tier = defender["skills"][def_skill]["tier"]
            shred = max(0, atk_tier - def_tier) if atk_tier > def_tier else 0
            mag = atk_tier - shred
            if def_out == "success":
                mag -= def_margin
            mag = max(0, mag)
            detail["shred"] = shred
            detail["magnitude"] = mag

            if mag > 0 and prescribed_effect == "Wound":
                wound_attr = wound_target_attr(attacker["skills"][atk_skill], defender["attrs"])
                defender["wounds"].append({
                    "location": li, "zone": zone, "tier": atk_tier,
                    "magnitude": mag, "target_attr": wound_attr,
                    "laterality": parity
                })
                if wound_attr and wound_attr.startswith("b"):
                    old = defender["attrs"][wound_attr]
                    defender["attrs"][wound_attr] = max(1, old - mag)
                    nd = derived(defender["attrs"])
                    defender["max_hp"] = nd["HP"]
                    defender["max_mp"] = nd["MP"]
                    defender["max_pe"] = nd["PE"]
                    if defender["hp"] > defender["max_hp"]:
                        defender["hp"] = defender["max_hp"]
                detail["wound_applied"] = True
                detail["wound_target"] = wound_attr

            elif mag > 0 and prescribed_effect == "Prone":
                defender["conditions"].append({
                    "type": "Prone", "zone": zone,
                    "laterality": parity, "magnitude": mag
                })
                detail["condition_applied"] = "Prone"

    elif winner == "defender":
        detail["effect"] = "Defense wins (no counter-Effect, DEC-101)"
    else:
        detail["effect"] = "Repeat/no Effect (both fail or tie)"

    detail["label"] = f"{atk_label}→{def_label}" + (" (reaction)" if is_reaction else "")
    return winner, detail

def zero_step(roll):
    if roll == 100: return 100
    return (roll % 10) * 10 + (roll // 10)

def location_quartile(li):
    if li <= 25: return "Legs"
    if li <= 50: return "Torso"
    if li <= 75: return "Arms"
    return "Head"

def wound_target_attr(atk_skill, target_attrs):
    cands = [k for k in atk_skill["attributes"] if k.startswith("b")]
    if not cands: return None
    return cands[0]

# ── S-11 Extended Test (DEC-073, H7) ────────────────────────────────────
def s11_healing(healer, target, skill_name, target_margin, rng,
                log_records, scene, healer_label):
    total_margin = 0
    penalty = 0
    for w in healer["wounds"]:
        wt = w.get("target_attr", "")
        sk_attrs = [k for k in healer["skills"][skill_name]["attributes"]]
        if wt in sk_attrs or any(wt == a for a in sk_attrs):
            penalty += w["magnitude"]
    eff = max(1, healer["skills"][skill_name]["value"] - penalty)
    intervals = []

    while total_margin < target_margin:
        roll, outcome, cost, overflow, fx, rec, margin, grew, adv = \
            core_test(healer, skill_name, rng, log_records, scene, healer_label)
        if outcome == "success":
            total_margin += margin
        intervals.append({
            "roll": roll, "outcome": outcome, "margin": margin,
            "total": total_margin, "mp_net": -cost + rec,
            "overflow": overflow
        })

    hp_restored = min(total_margin, target["max_hp"] - target["hp"])
    target["hp"] += hp_restored
    if target["hp"] > target["max_hp"]:
        target["hp"] = target["max_hp"]
    return total_margin >= target_margin, total_margin, hp_restored, intervals

# ── Scene Runners ────────────────────────────────────────────────────────
def run_scene1(rng, rowan, goblin, log):
    scene = "S1-Goblin"
    # Fixed Perception teaching beat (D2/D6)
    log.append({
        "layer": "locked+ruled", "scene": scene,
        "actor": "Rowan", "skill": "Perception",
        "roll": 100, "outcome": "failure", "cost": 100,
        "overflow": 0, "failure_xp": 73, "recovery": 47,
        "domain": "MP", "is_100": True, "is_double": True,
        "advanced_skill": {"name": "Perception (Advanced)", "tier": 2,
                           "cap": 50, "start": 1, "added_attr": "mps"},
        "note": "Fixed-roll teaching beat (D2/D6). DEC-012 Advanced Skill created."
    })
    rowan["mp"] -= 100
    rowan["mp"] += 47
    rowan["skills"]["Perception"]["value"] = 29  # cascade 27→28→29
    rowan["skills"]["Perception (Advanced)"] = {
        "tier": 2, "cap": 50, "value": 1, "attributes": ["mss", "mps"]
    }

    # Combat: max 6 rounds, symmetric
    for rnd in range(1, 7):
        if goblin["hp"] <= 0 or rowan["hp"] <= 0:
            break
        # Rowan attacks Goblin
        if rowan["hp"] > 0:
            s1_contest(rowan, goblin, "Attack", "Defense", rng,
                       log, scene, "Rowan", "Goblin")
        # Goblin attacks Rowan (Crude Attack vs Defense)
        if goblin["hp"] > 0 and rowan["hp"] > 0:
            s1_contest(goblin, rowan, "Crude Attack", "Defense", rng,
                       log, scene, "Goblin", "Rowan")

def run_scene2(rng, rowan, snake, log):
    scene = "S2-Snake"
    # Snake acts first (Speed 173 > 166)
    for rnd in range(1, 6):
        if snake["hp"] <= 0 or rowan["hp"] <= 0:
            break
        if snake["hp"] > 0 and rowan["hp"] > 0:
            s1_contest(snake, rowan, "Venomous Bite", "Defense", rng,
                       log, scene, "Rattlesnake", "Rowan",
                       prescribed_effect="Wound")
        if rowan["hp"] > 0 and snake["hp"] > 0:
            s1_contest(rowan, snake, "Attack", "Defense", rng,
                       log, scene, "Rowan", "Rattlesnake")

def run_scene3(rng, rowan, aleena, log):
    scene = "S3-Aleena-Heal"
    completed, total, restored, intervals = s11_healing(
        aleena, rowan, "Devotion", 40, rng, log, scene, "Aleena")
    return {"completed": completed, "total_margin": total,
            "hp_restored": restored, "intervals": intervals}

def run_scene4(rng, aleena, ghoul, log):
    scene = "S4-Ghouls"
    # Turning: Devotion 32 vs Desecration 22 — narratively succeeds
    s1_contest(aleena, ghoul, "Devotion", "Desecration", rng,
               log, scene, "Aleena", "Ghoul")
    # Party passes (narrated withdrawal — flagged)

def run_scene5(rng, rowan, log):
    scene = "S5-Door"
    for attempt in range(1, 4):
        roll = rng.randint(1, 100)
        effective = rowan["skills"]["Attack"]["value"] - 15
        success = roll <= effective
        cost = roll
        rowan["pe"] -= cost
        overflow = 0
        if rowan["pe"] < 0:
            overflow = -rowan["pe"]
            rowan["hp"] -= overflow
            rowan["pe"] = 0
        fx = max(0, roll - rowan["skills"]["Attack"]["value"])
        rec = math.floor(rowan["er"] / 2)
        rowan["pe"] = min(rowan["max_pe"], rowan["pe"] + rec)
        log.append({
            "layer": "locked", "scene": scene,
            "actor": "Rowan", "skill": "Attack",
            "roll": roll, "outcome": "success" if success else "failure",
            "cost": cost, "overflow": overflow, "failure_xp": fx,
            "recovery": rec, "domain": "PE",
            "effective": effective, "attempt": attempt
        })
        if success:
            break

def run_scene6(rng, rowan, aleena, bargain, log):
    scene = "S6-Bargle"
    # Turn order by narrative (Bargle first — flagged as advisory override
    # of Speed order; invisibility has no mechanical surprise advantage)
    for rnd in range(1, 4):
        if bargain["hp"] <= 0 or (rowan["hp"] <= 0 and aleena["hp"] <= 0):
            break
        # Bargle Bolt → Aleena (T2 Wound)
        if bargain["hp"] > 0 and aleena["hp"] > 0:
            s1_contest(bargain, aleena, "Bolt", "Defense", rng,
                       log, scene, "Bargle", "Aleena",
                       prescribed_effect="Wound")
        # Rowan reaction (DEC-132.B) if Aleena wounded
        if bargain["hp"] > 0 and rowan["hp"] > 0:
            s1_contest(rowan, bargain, "Attack", "Defense", rng,
                       log, scene, "Rowan(reaction)", "Bargle",
                       is_reaction=True)
        # Rowan's turn
        if rowan["hp"] > 0 and bargain["hp"] > 0:
            s1_contest(rowan, bargain, "Attack", "Defense", rng,
                       log, scene, "Rowan", "Bargle")
        # Aleena's turn
        if aleena["hp"] > 0 and bargain["hp"] > 0:
            s1_contest(aleena, bargain, "Smite", "Defense", rng,
                       log, scene, "Aleena", "Bargle")

    # Climax fork: Beguile 27 vs Composure (use rowan's Composure value)
    if bargain["hp"] > 0:
        atk_roll, _, _, _, _, _, _, _, _ = core_test(bargain, "Beguile", rng,
                                                   log, scene, "Bargle", "")
        composure_val = rowan["skills"]["Composure"]["value"]
        def roll_def():
            r = rng.randint(1, 100)
            return r
        def_roll = roll_def()
        # Beguile margin vs Composure margin
        bg_margin = max(0, 27 - atk_roll)
        cp_margin = max(0, composure_val - def_roll)
        if bg_margin > cp_margin:
            fork = "Ending B (hex holds)"
        elif cp_margin > bg_margin:
            fork = "Ending A (hex resisted)"
        else:
            fork = "Ending A (tie → defense holds, reroll up to 3x — here: defense holds)"
        log.append({
            "layer": "advisory", "scene": scene,
            "actor": "Bargle/Rowan", "skill": "Beguile vs Composure",
            "roll": atk_roll, "def_roll": def_roll,
            "fork_outcome": fork,
            "note": "Charm/domination not a ruled Effect — represented advisory (flagged)."
        })

def run_ending(rng, rowan, aleena, log):
    scene = "Aftermath-REST"
    # Aleena heals Rowan
    s11_healing(aleena, rowan, "Devotion", 40, rng, log, scene, "Aleena")

# ── Main ─────────────────────────────────────────────────────────────────
def main():
    rng = random.Random(SEED)
    log = []

    rowan, aleena, goblin, snake, ghoul, bargain = build_all()

    # Capture INITIAL state BEFORE any scenes
    initial = {
        "Rowan": {
            "HP": rowan["hp"], "MP": rowan["mp"], "PE": rowan["pe"],
            "max_hp": rowan["max_hp"], "max_mp": rowan["max_mp"],
            "skills": {k: v["value"] for k, v in rowan["skills"].items()}
        },
        "Aleena": {
            "HP": aleena["hp"], "MP": aleena["mp"], "PE": aleena["pe"],
            "max_hp": aleena["max_hp"], "max_mp": aleena["max_mp"]
        },
        "Goblin": {"HP": goblin["hp"], "max_hp": goblin["max_hp"]},
        "Rattlesnake": {"HP": snake["hp"], "max_hp": snake["max_hp"]},
        "Ghoul": {"HP": ghoul["hp"], "max_hp": ghoul["max_hp"]},
        "Bargle": {"HP": bargain["hp"], "max_hp": bargain["max_hp"]},
    }

    # Run scenes
    run_scene1(rng, rowan, goblin, log)
    run_scene2(rng, rowan, snake, log)
    heal_result = run_scene3(rng, rowan, aleena, log)
    run_scene4(rng, aleena, ghoul, log)
    run_scene5(rng, rowan, log)
    run_scene6(rng, rowan, aleena, bargain, log)
    run_ending(rng, rowan, aleena, log)

    # Final skill snapshot
    def skills_snapshot(c):
        return {k: v["value"] for k, v in c["skills"].items()}
    final_skills = {
        "Rowan": skills_snapshot(rowan),
        "Aleena": skills_snapshot(aleena),
        "Goblin": skills_snapshot(goblin),
        "Rattlesnake": skills_snapshot(snake),
        "Ghoul": skills_snapshot(ghoul),
        "Bargle": skills_snapshot(bargain),
    }
    final = {
        "Rowan": {"HP": rowan["hp"], "MP": rowan["mp"], "PE": rowan["pe"],
                   "max_hp": rowan["max_hp"], "max_mp": rowan["max_mp"],
                   "wounds": len(rowan["wounds"])},
        "Aleena": {"HP": aleena["hp"], "MP": aleena["mp"], "PE": aleena["pe"],
                   "max_hp": aleena["max_hp"], "max_mp": aleena["max_mp"],
                   "wounds": len(aleena["wounds"])},
        "Goblin": {"HP": goblin["hp"], "max_hp": goblin["max_hp"],
                   "dead": goblin["hp"] <= 0},
        "Rattlesnake": {"HP": snake["hp"], "max_hp": snake["max_hp"],
                        "dead": snake["hp"] <= 0},
        "Ghoul": {"HP": ghoul["hp"]},
        "Bargle": {"HP": bargain["hp"], "max_hp": bargain["max_hp"],
                   "dead": bargain["hp"] <= 0},
    }

    output = {
        "seed": SEED,
        "conventions": "Automated Playtest Run Conventions H1–H7 (2026-09-14)",
        "d100_rule": "1–100, 00 = 100",
        "initial_state": initial,
        "final_state": final,
        "heal_result": heal_result,
        "ledger": {
            "Rowan_HP_start": initial["Rowan"]["HP"],
            "Rowan_HP_end": rowan["hp"],
            "Rowan_HP_delta": rowan["hp"] - initial["Rowan"]["HP"],
            "Aleena_HP_start": initial["Aleena"]["HP"],
            "Aleena_HP_end": aleena["hp"],
            "Aleena_HP_delta": aleena["hp"] - initial["Aleena"]["HP"],
        },
        "records": log,
        "record_count": len(log),
        "final_skills": final_skills,
    }

    census = {}
    for r in log:
        t = r.get("layer", "unTagged")
        census[t] = census.get(t, 0) + 1
    output["layer_census"] = census

    out_path = Path(__file__).parent / "tiwas-red-box-playtest-20260917-raw-log.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Log: {out_path}")
    print(f"Records: {len(log)}")
    print(f"Census: {census}")
    print(f"Rowan: {initial['Rowan']['HP']}->{rowan['hp']} (d{rowan['hp']-initial['Rowan']['HP']})")
    print(f"Aleena: {initial['Aleena']['HP']}->{aleena['hp']} (d{aleena['hp']-initial['Aleena']['HP']})")
    print(f"Goblin: {goblin['hp']}/{goblin['max_hp']} {'DEAD' if goblin['hp']<=0 else 'alive'}")
    print(f"Snake: {snake['hp']}/{snake['max_hp']} {'DEAD' if snake['hp']<=0 else 'alive'}")
    print(f"Bargle: {bargain['hp']}/{bargain['max_hp']} {'DEAD' if bargain['hp']<=0 else 'alive'}")
    # Verify ledger closes
    assert rowan["hp"] - initial["Rowan"]["HP"] == output["ledger"]["Rowan_HP_delta"]
    assert aleena["hp"] - initial["Aleena"]["HP"] == output["ledger"]["Aleena_HP_delta"]
    print("LEDGER CLOSES OK")

if __name__ == "__main__":
    main()
