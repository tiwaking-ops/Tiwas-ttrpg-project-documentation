#!/usr/bin/env python3
"""
Tiwas TTRPG -- Mirror-Match Combat Stress Test
Executes the scenario defined in
tiwas-playtest-mirror-combat-design-brief-2026-09-10.md (v0.2).

Uses random.SystemRandom() for all dice per standing playtest methodology.
Non-canonical. No DEC assigned. Advisory simulation only.
"""

import csv
import random
import json

rng = random.SystemRandom()

DOUBLES = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100}

# ---------------------------------------------------------------------------
# Core dice / Core Test primitives
# ---------------------------------------------------------------------------

def roll_d100():
    return rng.randint(1, 100)


def zero_step(roll):
    """DEC-014 Zero-Step: exchange tens/units digits of the natural roll."""
    if roll == 100:
        return 100
    tens = roll // 10
    units = roll % 10
    swapped = units * 10 + tens
    return swapped if swapped != 0 else 100


def zone_of(index):
    """DEC-100 Tier-1 coarse-zone quartiles."""
    if 1 <= index <= 25:
        return 'Legs'
    if 26 <= index <= 50:
        return 'Torso'
    if 51 <= index <= 75:
        return 'Arms'
    if 76 <= index <= 100:
        return 'Head'
    return 'Unknown'


def laterality_of(index):
    """DEC-041(3): digit-parity odd=left, even=right (applied to the Location Index)."""
    return 'Left' if index % 2 == 1 else 'Right'


def resolve_effect_tier_magnitude(atk_tier, def_tier, defender_margin):
    """DEC-103: Skill-Tier shred + margin de-escalation, unified carry rule."""
    base_mag = atk_tier  # Y
    tier = atk_tier
    if atk_tier == def_tier:
        mag = base_mag - 1
    elif def_tier > atk_tier:
        mag = base_mag - (def_tier - atk_tier)
    else:
        mag = base_mag + 1
    mag -= defender_margin
    if mag <= 0:
        tier -= 1
        if tier <= 0:
            return 0, 0  # negated
        mag = tier
    return tier, -tier  # final Tier, Magnitude (Z = -Y)


def inflict_injury_damage(atk_margin, defender_margin):
    """DEC-104: Winner's Margin - Defender's Margin; DEC-104 'never 0 on a win' -> floor 1."""
    dmg = atk_margin - defender_margin
    return dmg if dmg > 0 else 1


# ---------------------------------------------------------------------------
# Combatant
# ---------------------------------------------------------------------------

class Combatant:
    def __init__(self, name):
        self.name = name
        self.hp = 600
        self.hp_max = 600
        self.pe = 150
        self.pe_max = 150
        self.energy_regen = 100
        self.speed = 150
        self.movement_speed = 6

        self.skills = {
            'Attack':          {'value': 25, 'cap': 50, 'tier': 2},
            'Grapple':         {'value': 25, 'cap': 50, 'tier': 2},
            'Trip':            {'value': 25, 'cap': 50, 'tier': 2},
            'Disarm':          {'value': 25, 'cap': 50, 'tier': 2},
            'EquipmentDamage': {'value': 25, 'cap': 50, 'tier': 2},
            'Defense':         {'value': 25, 'cap': 50, 'tier': 2},
        }
        self.offense_pool = ['Attack', 'Grapple', 'Trip', 'Disarm', 'EquipmentDamage']
        self.priority = ['Attack', 'Grapple', 'Trip', 'Disarm', 'EquipmentDamage']

        self.conditions = []       # StateRecords currently on this combatant
        self.advanced_skills = []  # names of advanced skills created (excluded from offense pool)
        self.general_xp = 0
        self.total_failure_xp = 0

    # -- selection -----------------------------------------------------
    def select_offense_skill(self, tie_break='priority'):
        best_val = max(self.skills[s]['value'] for s in self.offense_pool)
        candidates = [s for s in self.offense_pool if self.skills[s]['value'] == best_val]
        if len(candidates) == 1:
            return candidates[0]
        if tie_break == 'random':
            return rng.choice(candidates)
        for p in self.priority:
            if p in candidates:
                return p
        return candidates[0]

    # -- Core Test bookkeeping -----------------------------------------
    def pay_cost_and_recover(self, roll):
        overflow = 0
        if self.pe >= roll:
            self.pe -= roll
        else:
            overflow = roll - self.pe
            self.pe = 0
            self.hp -= overflow
        recover = self.energy_regen // 2
        self.pe = min(self.pe_max, self.pe + recover)
        return overflow

    def apply_failure_xp_and_pool(self, skill_name, roll, success):
        skill = self.skills[skill_name]
        failure_xp = max(0, roll - skill['value']) if not success else 0
        self.total_failure_xp += failure_xp
        pool = failure_xp
        while pool >= skill['value'] and skill['value'] < skill['cap']:
            pool -= skill['value']
            skill['value'] += 1
        self.general_xp += pool
        return failure_xp

    def check_failed_double(self, skill_name, roll, success):
        if roll in DOUBLES and not success:
            old = self.skills[skill_name]
            new_tier = old['tier'] + 1
            new_name = f"{skill_name}-Adv{len(self.advanced_skills) + 1}(T{new_tier})"
            self.skills[new_name] = {'value': 1, 'cap': 50, 'tier': new_tier}
            self.advanced_skills.append(new_name)
            # Per brief step 9: excluded from offense-skill-selection pool
            # (never added to self.offense_pool).
            return new_name
        return None


def core_test(combatant, skill_name):
    roll = roll_d100()
    skill_val = combatant.skills[skill_name]['value']
    success = (roll <= skill_val) and (roll != 100)
    margin = skill_val - roll if success else None
    overflow = combatant.pay_cost_and_recover(roll)
    failure_xp = combatant.apply_failure_xp_and_pool(skill_name, roll, success)
    adv = combatant.check_failed_double(skill_name, roll, success)
    return {
        'roll': roll, 'skill_val_at_roll': skill_val, 'success': success,
        'margin': margin, 'overflow': overflow, 'failure_xp': failure_xp,
        'advanced_skill_created': adv,
    }


EFFECT_NAME = {
    'Trip': 'Prone',
    'Disarm': 'Disarmed',
    'EquipmentDamage': 'EquipmentDamaged',
    'Grapple': 'Grappled',
}
DECLARED_NAME = {
    'Attack': 'Inflict Injury',
    'Grapple': 'Impose Condition: Grappled',
    'Trip': 'Knock Prone',
    'Disarm': 'Disarm/Break Hold',
    'EquipmentDamage': 'Equipment Damage',
}


def resolve_exchange(actor, defender, log, ctr, round_num, tie_break='priority', max_repeats=50):
    """One 'turn' = repeat-loop of Core Test pairs until a definitive win/lose."""
    repeats = 0
    while True:
        repeats += 1
        ctr[0] += 1
        exch_id = ctr[0]

        offense_skill = actor.select_offense_skill(tie_break)
        atk_res = core_test(actor, offense_skill)
        def_res = core_test(defender, 'Defense')

        if not atk_res['success'] and not def_res['success']:
            outcome = 'repeat-bothfail'
        elif atk_res['success'] and not def_res['success']:
            outcome = 'attacker-wins'
        elif not atk_res['success'] and def_res['success']:
            outcome = 'defender-wins'
        else:
            if atk_res['margin'] > def_res['margin']:
                outcome = 'attacker-wins'
            elif def_res['margin'] > atk_res['margin']:
                outcome = 'defender-wins'
            else:
                outcome = 'repeat-tie'

        effect_declared = ''
        location_index = zone = laterality = ''
        tag_check = ''
        resulting_staterecord = ''

        if outcome == 'attacker-wins':
            mitigation = def_res['margin'] if def_res['success'] else 0
            effect_declared = DECLARED_NAME[offense_skill]

            if offense_skill == 'Attack':
                dmg = inflict_injury_damage(atk_res['margin'], mitigation)
                defender.hp -= dmg
                resulting_staterecord = f"HP -{dmg}"
            else:
                loc_referencing = offense_skill in ('Trip', 'Disarm', 'EquipmentDamage')
                if loc_referencing:
                    location_index = zero_step(atk_res['roll'])
                    zone = zone_of(location_index)
                    laterality = laterality_of(location_index)

                if offense_skill == 'Disarm':
                    match = (zone == 'Arms')       # weapon held -> Arms
                    tag_check = 'pass' if match else 'fail-and-fall-back'
                elif offense_skill == 'EquipmentDamage':
                    match = zone in ('Arms', 'Torso')  # weapon(Arms) or armor(Torso)
                    tag_check = 'pass' if match else 'fail-and-fall-back'
                else:  # Trip, Grapple: no Tag+Location gate (DEC-028 scope)
                    match = True
                    tag_check = 'n/a'

                if not match:
                    dmg = inflict_injury_damage(atk_res['margin'], mitigation)
                    defender.hp -= dmg
                    resulting_staterecord = f"Fallback HP -{dmg} (Base Inflict Injury, DEC-030)"
                    effect_declared += ' -> FAIL-AND-FALL-BACK -> Inflict Injury'
                else:
                    atk_tier = actor.skills[offense_skill]['tier']
                    def_tier = defender.skills['Defense']['tier']
                    tier, mag = resolve_effect_tier_magnitude(atk_tier, def_tier, mitigation)
                    if tier == 0:
                        resulting_staterecord = 'Negated (Tier reduced to 0)'
                    else:
                        loc_str = f"Location {location_index}({zone}/{laterality}) " if loc_referencing else ''
                        cond_name = EFFECT_NAME[offense_skill]
                        resulting_staterecord = f"{loc_str}Tier-{tier} {cond_name} Magnitude {mag}"
                        defender.conditions.append({
                            'type': cond_name, 'tier': tier, 'magnitude': mag,
                            'location': location_index if loc_referencing else None,
                            'zone': zone if loc_referencing else None,
                            'source_exchange': exch_id,
                        })

        row = {
            'exchange_#': exch_id, 'round': round_num, 'repeat_seq': repeats,
            'actor': actor.name, 'defender': defender.name,
            'offense_skill_chosen': offense_skill,
            'offense_skill_value_at_roll': atk_res['skill_val_at_roll'],
            'atk_roll': atk_res['roll'], 'def_roll': def_res['roll'],
            'atk_success': atk_res['success'], 'def_success': def_res['success'],
            'atk_margin': atk_res['margin'], 'def_margin': def_res['margin'],
            'outcome': outcome,
            'effect_declared': effect_declared,
            'location_index': location_index, 'zone': zone, 'laterality': laterality,
            'tag_check': tag_check,
            'resulting_staterecord': resulting_staterecord,
            'hp_alpha_after': alpha.hp, 'hp_beta_after': beta.hp,
            'pe_alpha_after': alpha.pe, 'pe_beta_after': beta.pe,
            'atk_overflow': atk_res['overflow'], 'def_overflow': def_res['overflow'],
            'atk_failure_xp': atk_res['failure_xp'], 'def_failure_xp': def_res['failure_xp'],
            'atk_advanced_skill_created': atk_res['advanced_skill_created'] or '',
            'def_advanced_skill_created': def_res['advanced_skill_created'] or '',
        }
        log.append(row)

        if outcome in ('attacker-wins', 'defender-wins'):
            return outcome
        if repeats >= max_repeats:
            row['outcome'] = outcome + ' [SAFETY-CAP-FORCED-END]'
            return 'defender-wins'


# ---------------------------------------------------------------------------
# Main run function
# ---------------------------------------------------------------------------

from collections import Counter

def run_scenario(tie_break, max_rounds=500):
    global alpha, beta  # resolve_exchange reads these for hp_*_after logging
    alpha = Combatant('Alpha')
    beta = Combatant('Beta')
    log = []
    ctr = [0]
    round_num = 0
    terminated = False
    victor = None
    cause = None

    while round_num < max_rounds and not terminated:
        round_num += 1

        if alpha.speed == beta.speed:
            while True:
                a_r, b_r = roll_d100(), roll_d100()
                if a_r != b_r:
                    break
            order = [alpha, beta] if a_r > b_r else [beta, alpha]
        else:
            order = sorted([alpha, beta], key=lambda c: -c.speed)

        for actor in order:
            defender = beta if actor is alpha else alpha
            if actor.hp <= 0 or defender.hp <= 0:
                terminated = True
                break
            resolve_exchange(actor, defender, log, ctr, round_num, tie_break=tie_break)
            if alpha.hp <= 0 or beta.hp <= 0:
                terminated = True
                if alpha.hp <= 0 and beta.hp <= 0:
                    victor = 'Simultaneous (both HP<=0)'
                elif alpha.hp <= 0:
                    victor = 'Beta'
                else:
                    victor = 'Alpha'
                cause = 'HP <= 0 (DEC-052 forced incapacitation)'
                break

    if not terminated:
        victor = 'None (round cap reached, no incapacitation)'
        cause = f'MAX_ROUNDS safety cap ({max_rounds}) reached'

    outcome_counts = Counter(r['outcome'] for r in log)
    effect_counts = Counter(r['effect_declared'] for r in log if r['effect_declared'])
    tagcheck_counts = Counter(r['tag_check'] for r in log if r['tag_check'])
    skill_choice_counts = Counter(r['offense_skill_chosen'] for r in log)

    summary = {
        'tie_break_mode': tie_break,
        'total_rounds': round_num,
        'total_exchanges_logged': len(log),
        'victor': victor,
        'termination_cause': cause,
        'alpha_final_hp': alpha.hp,
        'beta_final_hp': beta.hp,
        'alpha_final_pe': alpha.pe,
        'beta_final_pe': beta.pe,
        'alpha_skills': {k: v['value'] for k, v in alpha.skills.items()},
        'beta_skills': {k: v['value'] for k, v in beta.skills.items()},
        'alpha_advanced_skills': alpha.advanced_skills,
        'beta_advanced_skills': beta.advanced_skills,
        'alpha_conditions_ever': alpha.conditions,
        'beta_conditions_ever': beta.conditions,
        'alpha_total_failure_xp': alpha.total_failure_xp,
        'beta_total_failure_xp': beta.total_failure_xp,
        'alpha_general_xp': alpha.general_xp,
        'beta_general_xp': beta.general_xp,
        'outcome_counts': dict(outcome_counts),
        'effect_counts': dict(effect_counts),
        'tagcheck_counts': dict(tagcheck_counts),
        'skill_choice_counts': dict(skill_choice_counts),
    }
    return log, summary


# ---------------------------------------------------------------------------
# Execute Run A (brief's own suggested default, §8.4: fixed priority tie-break)
# and Run B (alternate: uniform-random tie-break) for comparison.
# ---------------------------------------------------------------------------

log_a, summary_a = run_scenario('priority')
fieldnames = list(log_a[0].keys())
with open('/home/claude/mirror_playtest/exchange_log_run_a_priority.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(log_a)

log_b, summary_b = run_scenario('random')
with open('/home/claude/mirror_playtest/exchange_log_run_b_random.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(log_b)

with open('/home/claude/mirror_playtest/summary.json', 'w') as f:
    json.dump({'run_a_priority_tiebreak': summary_a, 'run_b_random_tiebreak': summary_b},
               f, indent=2, default=str)

print(json.dumps({'run_a_priority_tiebreak': summary_a, 'run_b_random_tiebreak': summary_b},
                  indent=2, default=str))
