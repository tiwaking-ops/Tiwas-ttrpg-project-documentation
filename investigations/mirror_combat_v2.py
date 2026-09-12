"""
Tiwas TTRPG - Human-Templated Mirror Combat Stress Test v2
Implements the 2026-09-13 design brief. random.SystemRandom() for OS-entropy rolls.
Non-canonical playtest scaffold. See design brief for all flagged conventions.
"""
import csv
import json
import math
import random

rng = random.SystemRandom()

BODY_ATTRS = ["bee","bep","bes","bex","bpe","bpp","bps","bpx","bse","bsp","bss","bsx"]
MIND_ATTRS = ["mee","mep","mes","mex","mpe","mpp","mps","mpx","mse","msp","mss","msx"]
ALL_ATTRS = sorted(BODY_ATTRS + MIND_ATTRS)

DOUBLES = {11,22,33,44,55,66,77,88,99,100}

# ---- Skill definitions (name -> (attr_list, role, effect)) ----
BASE_SKILLS = {
    "Attack":           (["bpp","bps"], "offense", "Inflict Injury"),
    "Grapple":          (["bpp","bsp"], "offense", "Grappled"),
    "Trip":             (["bsp","bss"], "offense", "Prone"),
    "Disarm":           (["bss","bsx"], "offense", "Disarm"),
    "EquipmentDamage":  (["bpp","bpe"], "offense", "EquipmentDamage"),
    "Wound":            (["bps","bpe"], "offense", "Wounded"),
    "ArmorBypass":      (["bsp","bsx"], "offense", "ArmorBypass"),
    "Defense":          (["bss","bse"], "defense", None),
    "Guard":            (["bep","bee"], "defense", None),
}

TAG_GATED_EFFECTS = {"Disarm", "EquipmentDamage", "ArmorBypass"}
LOCATION_EFFECTS = {"Grapple", "Trip", "Disarm", "EquipmentDamage", "Wound", "ArmorBypass"}

# ---- DEC-137 Human v1 full address table (idx 1-100 -> leaf name, region) ----
def dec137_leaf(idx):
    table = [
        (1,5,"Thigh","Legs"), (6,7,"Knee","Legs"), (8,12,"Lower Leg","Legs"),
        (13,13,"Ankle","Legs"), (14,15,"Hallux","Legs"), (16,16,"2nd Toe","Legs"),
        (17,17,"3rd Toe","Legs"), (18,18,"4th Toe","Legs"), (19,19,"5th Toe","Legs"),
        (20,22,"Midfoot/Heel","Legs"), (23,25,"Femoral/Internal","Legs"),
        (26,29,"Chest Wall/Sternum/Ribs","Torso"), (30,31,"Heart","Torso"),
        (32,35,"Lungs","Torso"), (36,37,"Neck","Torso"), (38,40,"Abdomen Wall","Torso"),
        (41,41,"Stomach","Torso"), (42,43,"Liver","Torso"), (44,45,"Intestines","Torso"),
        (46,47,"Kidneys","Torso"), (48,48,"Pelvis","Torso"), (49,49,"Groin","Torso"),
        (50,50,"Spine","Torso"),
        (51,52,"Shoulder","Arms"), (53,58,"Upper Arm","Arms"), (59,60,"Elbow","Arms"),
        (61,65,"Forearm","Arms"), (66,67,"Wrist","Arms"), (68,69,"Thumb","Arms"),
        (70,70,"Index Finger","Arms"), (71,71,"Middle Finger","Arms"),
        (72,72,"Ring Finger","Arms"), (73,73,"Little Finger","Arms"),
        (74,75,"Palm/Back of Hand","Arms"),
        (76,91,"Skull","Head"), (92,93,"Eyes","Head"), (94,95,"Ears","Head"),
        (96,97,"Nose","Head"), (98,100,"Jaw/Teeth","Head"),
    ]
    for lo,hi,name,region in table:
        if lo <= idx <= hi:
            return name, region
    raise ValueError(f"idx {idx} out of range")

def dec100_quartile(idx):
    if 1 <= idx <= 25: return "Legs"
    if 26 <= idx <= 50: return "Torso"
    if 51 <= idx <= 75: return "Arms"
    if 76 <= idx <= 100: return "Head"
    raise ValueError(idx)

def zero_step(roll):
    if roll == 100:
        return 100
    tens, units = divmod(roll, 10)
    swapped = units*10 + tens
    return 100 if swapped == 0 else swapped

def parity(idx):
    return "Left" if idx % 2 == 1 else "Right"

ARMOR_COVERAGE = [(26,35,"Body armor (Chest)"), (76,91,"Helmet (Skull)")]
def armor_at(idx):
    for lo,hi,label in ARMOR_COVERAGE:
        if lo <= idx <= hi:
            return label
    return None

WEAPON_ZONE = "Arms"  # state:held weapon location for Disarm/EquipmentDamage matching
GEAR_ZONES = {"Arms": "Weapon", "Torso": "Body armor", "Head": "Helmet"}  # EquipmentDamage broad match


class Skill:
    def __init__(self, name, attrs, role, effect, tier_origin=1):
        self.name = name
        self.attrs = attrs[:]
        self.role = role
        self.effect = effect
        self.value = 0
        self.cap = 0

    @property
    def tier(self):
        return len(self.attrs)


class Combatant:
    def __init__(self, name):
        self.name = name
        self.attrs = {a: 50 for a in ALL_ATTRS}
        self.skills = {}
        for sname, (attrs, role, effect) in BASE_SKILLS.items():
            sk = Skill(sname, attrs, role, effect)
            self.skills[sname] = sk
        self.recalc_all()
        for sk in self.skills.values():
            sk.value = sk.cap // 2  # starting value = floor(cap/2)
        self.hp_current = self.hp_max
        self.pe_current = self.pe_max
        self.general_xp = 0
        self.records = []  # list of dicts: {type, tier, mag, location, attr(optional)}
        self.advanced_skills_log = []
        self.incapacitated = False

    def recalc_all(self):
        self.hp_max = sum(self.attrs[a] for a in BODY_ATTRS)
        self.mp_max = sum(self.attrs[a] for a in MIND_ATTRS)
        self.pe_max = self.attrs["bep"] + self.attrs["bes"] + self.attrs["bee"]
        self.speed = self.attrs["bsp"] + self.attrs["bss"] + self.attrs["bse"]
        self.energy_regen = self.attrs["bep"] + self.attrs["bes"]
        self.mp_regen = self.attrs["mep"] + self.attrs["mes"]
        self.movement_speed = (self.attrs["bsp"] + self.attrs["bss"]) // 15
        for sk in self.skills.values():
            sk.cap = sum(self.attrs[a] for a in sk.attrs) // len(sk.attrs)

    def spend_general_xp(self, log_list):
        while self.general_xp > 0:
            lowest_val = min(self.attrs[a] for a in ALL_ATTRS)
            candidates = sorted([a for a in ALL_ATTRS if self.attrs[a] == lowest_val])
            target = candidates[0]  # alphabetical tiebreak
            cost = self.attrs[target]
            if cost == 0:
                cost = 0  # increasing from 0 is free per DEC-011 pattern (cost=current value)
            if self.general_xp >= cost:
                self.general_xp -= cost
                self.attrs[target] += 1
                self.recalc_all()
                log_list.append(target)
            else:
                break

    def offense_pool(self):
        return [s for s in self.skills.values() if s.role == "offense"]

    def defense_pool(self):
        return [s for s in self.skills.values() if s.role == "defense"]

    def best_defense_skill(self):
        pool = self.defense_pool()
        maxval = max(s.value for s in pool)
        cands = sorted([s for s in pool if s.value == maxval], key=lambda s: s.name)
        return cands[0]

    def random_offense_skill(self):
        pool = self.offense_pool()
        return rng.choice(pool)

    def wound_target_attr(self, source_skill):
        cands = [a for a in source_skill.attrs if a in BODY_ATTRS]
        if not cands:
            cands = source_skill.attrs[:]
        return rng.choice(cands) if len(cands) > 1 else cands[0]

    def apply_wound(self, attr, magnitude, tier, location):
        # magnitude is negative (Z = -Y)
        self.attrs[attr] = self.attrs[attr] + magnitude
        self.recalc_all()
        self.records.append({"type":"Wound","tier":tier,"mag":magnitude,
                              "location":location,"attr":attr})

    def add_record(self, rtype, tier, mag, location):
        self.records.append({"type":rtype,"tier":tier,"mag":mag,"location":location,"attr":None})

    def core_test(self, skill, log_list):
        """Roll, pay cost, overflow, failure xp, skill roll pool, recovery, doubles.
        Returns (roll, success, margin)."""
        roll = rng.randint(1, 100)
        success = (roll <= skill.value) and (roll != 100)
        # cost
        cost = roll
        if self.pe_current >= cost:
            self.pe_current -= cost
            overflow = 0
        else:
            overflow = cost - self.pe_current
            self.pe_current = 0
            self.hp_current -= overflow
        # failure xp
        fxp = max(0, roll - skill.value)
        pool = fxp
        while pool >= skill.value and skill.value < skill.cap:
            pool -= skill.value
            skill.value += 1
        self.general_xp += pool
        self.spend_general_xp(log_list)
        # recovery (always last, this pool)
        self.pe_current = min(self.pe_max, self.pe_current + self.energy_regen // 2)
        # qualifying failed double -> advanced skill
        adv_created = None
        if roll in DOUBLES and not success:
            if roll == 100 or roll > skill.value:
                adv_created = self.create_advanced_skill(skill)
        margin = skill.value - roll if success else 0
        return roll, success, margin, overflow, adv_created

    def create_advanced_skill(self, parent_skill):
        available = [a for a in ALL_ATTRS if a not in parent_skill.attrs]
        if not available:
            return None
        new_attr = rng.choice(available)
        new_attrs = parent_skill.attrs + [new_attr]
        base_name = parent_skill.name.rstrip("0123456789+")
        existing = [n for n in self.skills if n.startswith(parent_skill.name + "+")]
        new_name = f"{parent_skill.name}+{new_attr}"
        if new_name in self.skills:
            new_name = f"{new_name}#{len(existing)+1}"
        sk = Skill(new_name, new_attrs, parent_skill.role, parent_skill.effect)
        sk.cap = sum(self.attrs[a] for a in new_attrs) // len(new_attrs)
        sk.value = 1
        self.skills[new_name] = sk
        self.advanced_skills_log.append({"name":new_name,"attrs":new_attrs,
                                          "parent":parent_skill.name,"tier":sk.tier})
        return new_name


def dec103_resolve(effect_tier, atk_tier, def_tier, def_margin):
    mag = effect_tier
    if atk_tier == def_tier:
        mag -= 1
    elif def_tier > atk_tier:
        mag -= (def_tier - atk_tier)
    else:
        mag += 1
    mag -= def_margin
    tier = effect_tier
    negated = False
    while mag <= 0 and tier > 0:
        tier -= 1
        mag = tier
    if tier <= 0:
        negated = True
    return tier, -tier if not negated else 0, negated  # (final_tier, magnitude Z=-Y, negated)


def run_exchange(actor, defender, ex_num, round_num, writer, general_xp_log):
    off_skill = actor.random_offense_skill()
    def_skill = defender.best_defense_skill()
    gxp_a, gxp_d = [], []
    repeats = 0
    while True:
        repeats += 1
        a_roll, a_succ, a_margin, a_overflow, a_adv = actor.core_test(off_skill, gxp_a)
        d_roll, d_succ, d_margin, d_overflow, d_adv = defender.core_test(def_skill, gxp_d)
        if not a_succ and not d_succ:
            outcome = "repeat_both_fail"
        elif a_succ and not d_succ:
            outcome = "attacker_wins"
        elif not a_succ and d_succ:
            outcome = "defender_wins"
        else:
            if a_margin == d_margin:
                outcome = "repeat_exact_tie"
            elif a_margin > d_margin:
                outcome = "attacker_wins"
            else:
                outcome = "defender_wins"
        if outcome not in ("repeat_both_fail", "repeat_exact_tie") or repeats >= 20:
            break

    effective_def_margin = d_margin if d_succ else 0
    effect_name = None
    location_str = ""
    tag_check = "n/a"
    record_str = ""

    if outcome == "attacker_wins":
        effect_name = off_skill.effect
        if effect_name == "Inflict Injury":
            dmg = max(0, a_margin - effective_def_margin)
            defender.hp_current -= dmg
            record_str = f"Inflict Injury: {dmg} HP"
        else:
            loc_idx = zero_step(a_roll)
            lat = parity(loc_idx)
            if off_skill.name.startswith("ArmorBypass") or (off_skill.effect == "ArmorBypass"):
                leaf, region = dec137_leaf(loc_idx)
                location_str = f"{leaf} ({region}, idx={loc_idx}, {lat})"
                armor = armor_at(loc_idx)
                if armor:
                    tag_check = f"pass ({armor})"
                    tier2, mag, neg = dec103_resolve(off_skill.tier, off_skill.tier, def_skill.tier, effective_def_margin)
                    if neg:
                        record_str = "Armor Bypass negated (Tier 0)"
                    else:
                        defender.add_record("ArmorBypass", tier2, mag, location_str)
                        record_str = f"ArmorBypass Tier-{tier2} Magnitude {mag} @ {location_str}"
                else:
                    tag_check = "fail_and_fallback (no armor here)"
                    dmg = max(0, a_margin - effective_def_margin)
                    defender.hp_current -= dmg
                    record_str = f"Fallback Inflict Injury: {dmg} HP"
            else:
                zone = dec100_quartile(loc_idx)
                location_str = f"{zone} (idx={loc_idx}, {lat})"
                if off_skill.effect in TAG_GATED_EFFECTS:
                    if off_skill.effect == "Disarm":
                        matched = (zone == WEAPON_ZONE)
                        gear = "Weapon" if matched else None
                    else:  # EquipmentDamage
                        gear = GEAR_ZONES.get(zone)
                        matched = gear is not None
                    if matched:
                        tag_check = f"pass ({gear})"
                        tier2, mag, neg = dec103_resolve(off_skill.tier, off_skill.tier, def_skill.tier, effective_def_margin)
                        if neg:
                            record_str = f"{off_skill.effect} negated (Tier 0)"
                        else:
                            defender.add_record(off_skill.effect, tier2, mag, location_str)
                            record_str = f"{off_skill.effect} Tier-{tier2} Magnitude {mag} @ {location_str}"
                    else:
                        tag_check = "fail_and_fallback (no matching gear)"
                        dmg = max(0, a_margin - effective_def_margin)
                        defender.hp_current -= dmg
                        record_str = f"Fallback Inflict Injury: {dmg} HP"
                else:
                    # Grapple / Trip / Wound: no tag gate
                    tier2, mag, neg = dec103_resolve(off_skill.tier, off_skill.tier, def_skill.tier, effective_def_margin)
                    if neg:
                        record_str = f"{off_skill.effect} negated (Tier 0)"
                    elif off_skill.effect == "Wounded":
                        target_attr = defender.wound_target_attr(off_skill)
                        defender.apply_wound(target_attr, mag, tier2, location_str)
                        record_str = f"{location_str} Tier-{tier2} Wound {mag} ({target_attr})"
                    else:
                        defender.add_record(off_skill.effect, tier2, mag, location_str)
                        record_str = f"{off_skill.effect} Tier-{tier2} Magnitude {mag} @ {location_str}"

    incap_a = actor.hp_current <= 0
    incap_d = defender.hp_current <= 0

    writer.writerow({
        "exchange": ex_num, "round": round_num, "actor": actor.name, "defender": defender.name,
        "offense_skill": off_skill.name, "off_val": off_skill.value, "off_tier": off_skill.tier,
        "defense_skill": def_skill.name, "def_val": def_skill.value, "def_tier": def_skill.tier,
        "atk_roll": a_roll, "def_roll": d_roll, "atk_margin": a_margin, "def_margin": effective_def_margin,
        "repeats": repeats, "outcome": outcome, "effect": effect_name or "",
        "location": location_str, "tag_check": tag_check, "record": record_str,
        "actor_hp": actor.hp_current, "defender_hp": defender.hp_current,
        "actor_pe": actor.pe_current, "defender_pe": defender.pe_current,
        "actor_overflow": a_overflow, "defender_overflow": d_overflow,
        "actor_gxp_spent": ";".join(gxp_a), "defender_gxp_spent": ";".join(gxp_d),
        "actor_adv_skill": a_adv or "", "defender_adv_skill": d_adv or "",
    })
    return incap_a, incap_d


def main():
    alpha = Combatant("Alpha")
    beta = Combatant("Beta")

    fieldnames = ["exchange","round","actor","defender","offense_skill","off_val","off_tier",
                  "defense_skill","def_val","def_tier","atk_roll","def_roll","atk_margin",
                  "def_margin","repeats","outcome","effect","location","tag_check","record",
                  "actor_hp","defender_hp","actor_pe","defender_pe","actor_overflow",
                  "defender_overflow","actor_gxp_spent","defender_gxp_spent",
                  "actor_adv_skill","defender_adv_skill"]

    ex_num = 0
    round_num = 0
    MAX_EXCHANGES = 400
    combat_over = False

    with open("/home/claude/playtest2/mirror_combat_v2_log.csv","w",newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        while ex_num < MAX_EXCHANGES and not combat_over:
            round_num += 1
            # Speed-based turn order, tie-break reroll
            if alpha.speed == beta.speed:
                while True:
                    ra, rb = rng.randint(1,100), rng.randint(1,100)
                    if ra != rb:
                        order = [alpha, beta] if ra > rb else [beta, alpha]
                        break
            else:
                order = sorted([alpha, beta], key=lambda c: -c.speed)

            for actor in order:
                defender = beta if actor is alpha else alpha
                if actor.hp_current <= 0 or defender.hp_current <= 0:
                    combat_over = True
                    break
                ex_num += 1
                gxp_log_placeholder = []
                incap_a, incap_d = run_exchange(actor, defender, ex_num, round_num, writer, gxp_log_placeholder)
                if incap_a or incap_d:
                    combat_over = True
                    break
                if ex_num >= MAX_EXCHANGES:
                    break

    summary = {
        "total_exchanges": ex_num,
        "total_rounds": round_num,
        "terminated_by_hp": combat_over and (alpha.hp_current <= 0 or beta.hp_current <= 0),
        "final_state": {}
    }
    for c in (alpha, beta):
        summary["final_state"][c.name] = {
            "hp_current": c.hp_current, "hp_max": c.hp_max,
            "pe_current": c.pe_current, "pe_max": c.pe_max,
            "attrs": c.attrs,
            "skills": {n: {"value": s.value, "cap": s.cap, "tier": s.tier, "role": s.role}
                       for n, s in c.skills.items()},
            "general_xp_banked": c.general_xp,
            "records": c.records,
            "advanced_skills_created": c.advanced_skills_log,
        }
    with open("/home/claude/playtest2/mirror_combat_v2_summary.json","w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps({
        "total_exchanges": ex_num,
        "total_rounds": round_num,
        "alpha_hp": alpha.hp_current, "beta_hp": beta.hp_current,
        "alpha_records": len(alpha.records), "beta_records": len(beta.records),
        "alpha_adv_skills": len(alpha.advanced_skills_log),
        "beta_adv_skills": len(beta.advanced_skills_log),
    }, indent=2))

if __name__ == "__main__":
    main()
