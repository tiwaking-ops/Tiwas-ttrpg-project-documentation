import numpy as np

def roll_d100(n, rng):
    return rng.integers(1, 101, size=n)  # 1..100 inclusive; 100 represents "00"

def succeeds(roll, skill):
    return (roll <= skill) & (roll != 100)

def q_margin(roll, skill):
    return (skill - roll).astype(np.float64)

def q_blackjack(roll, skill):
    return roll.astype(np.float64)

def simulate(candidate, skill_A, skill_O, n_trials, rng, max_rounds=300):
    active = np.ones(n_trials, dtype=bool)
    rounds = np.zeros(n_trials, dtype=np.int32)
    cost_A = np.zeros(n_trials, dtype=np.float64)
    cost_O = np.zeros(n_trials, dtype=np.float64)
    winner = np.full(n_trials, -1, dtype=np.int8)
    win_quality = np.full(n_trials, np.nan, dtype=np.float64)
    fumble_A = np.zeros(n_trials, dtype=bool)
    fumble_O = np.zeros(n_trials, dtype=bool)
    decisive_had_100 = np.zeros(n_trials, dtype=bool)
    forced_guard_A = np.zeros(n_trials, dtype=bool)
    forced_guard_O = np.zeros(n_trials, dtype=bool)

    for _ in range(max_rounds):
        idx = np.where(active)[0]
        if idx.size == 0:
            break
        n = idx.size
        roll_A = roll_d100(n, rng)
        roll_O = roll_d100(n, rng)

        rounds[idx] += 1
        cost_A[idx] += roll_A
        cost_O[idx] += roll_O
        is100_A = roll_A == 100
        is100_O = roll_O == 100
        fumble_A[idx] |= is100_A
        fumble_O[idx] |= is100_O

        succ_A = succeeds(roll_A, skill_A)
        succ_O = succeeds(roll_O, skill_O)

        if candidate == "margin":
            qA = q_margin(roll_A, skill_A)
            qO = q_margin(roll_O, skill_O)
        elif candidate == "blackjack":
            qA = q_blackjack(roll_A, skill_A)
            qO = q_blackjack(roll_O, skill_O)
        elif candidate == "hybrid":
            stance_A_committed = ~forced_guard_A[idx]
            stance_O_committed = ~forced_guard_O[idx]
            qA = np.where(stance_A_committed, q_blackjack(roll_A, skill_A), q_margin(roll_A, skill_A))
            qO = np.where(stance_O_committed, q_blackjack(roll_O, skill_O), q_margin(roll_O, skill_O))
        else:
            raise ValueError(candidate)

        both_succ = succ_A & succ_O
        only_A = succ_A & ~succ_O
        only_O = succ_O & ~succ_A
        neither = ~succ_A & ~succ_O

        A_higher = both_succ & (qA > qO)
        O_higher = both_succ & (qO > qA)
        tie_q = both_succ & (qA == qO)
        tie_roll_A_lower = tie_q & (roll_A < roll_O)
        tie_roll_O_lower = tie_q & (roll_O < roll_A)
        tie_full = tie_q & (roll_A == roll_O)

        decide_A = only_A | A_higher | tie_roll_A_lower | tie_full
        decide_O = only_O | O_higher | tie_roll_O_lower

        decisive_this_round = decide_A | decide_O
        had100_this_round = decisive_this_round & (is100_A | is100_O)

        w_A = idx[decide_A]
        w_O = idx[decide_O]
        winner[w_A] = 0
        winner[w_O] = 1
        win_quality[w_A] = qA[decide_A]
        win_quality[w_O] = qO[decide_O]
        decisive_had_100[idx[had100_this_round]] = True
        active[w_A] = False
        active[w_O] = False

        if candidate == "hybrid":
            new_forced_A = np.zeros(n, dtype=bool)
            new_forced_O = np.zeros(n, dtype=bool)
            committed_fail_A = stance_A_committed & ~succ_A & neither
            committed_fail_O = stance_O_committed & ~succ_O & neither
            new_forced_A[committed_fail_A] = True
            new_forced_O[committed_fail_O] = True
            forced_guard_A[idx] = new_forced_A
            forced_guard_O[idx] = new_forced_O

    return dict(
        winner=winner, rounds=rounds, cost_A=cost_A, cost_O=cost_O,
        win_quality=win_quality, fumble_A=fumble_A, fumble_O=fumble_O,
        decisive_had_100=decisive_had_100, unresolved=int(active.sum())
    )

if __name__ == "__main__":
    rng = np.random.default_rng(42)
    # sanity test
    for cand in ["margin", "blackjack", "hybrid"]:
        r = simulate(cand, 55, 55, 5000, rng)
        wp = (r["winner"] == 0).mean()
        print(cand, "win%A=", round(wp, 3), "unresolved=", r["unresolved"],
              "mean_rounds=", round(r["rounds"].mean(), 3),
              "nan_quality=", np.isnan(r["win_quality"]).sum())

# ---- Full battery runner (produces every table in the design document) ----


RNG = np.random.default_rng(42)
N_TRIALS = 50000
CANDIDATES = ["margin", "blackjack", "hybrid"]
SYMMETRIC_SKILLS = [10, 25, 40, 55, 70, 85, 99, 120, 150]
ASYMMETRIC_PAIRS = [(40, 70), (25, 99), (70, 99), (99, 150), (70, 150), (40, 150)]

def pct(x, p):
    return np.nanpercentile(x, p)

print("=" * 100)
print("TABLE 1: SYMMETRIC MATCHUPS (Skill_A = Skill_O)")
print("=" * 100)
header = f"{'Cand':<10}{'Skill':>6}{'WinProbA':>10}{'MeanRnds':>10}{'MeanCostA':>11}{'Q p10':>8}{'Q p50':>8}{'Q p90':>8}{'FumbleRate':>12}"
print(header)
sym_rows = []
for cand in CANDIDATES:
    for sk in SYMMETRIC_SKILLS:
        r = simulate(cand, sk, sk, N_TRIALS, RNG)
        wp = (r["winner"] == 0).mean()
        mr = r["rounds"].mean()
        mc = r["cost_A"].mean()
        q10, q50, q90 = pct(r["win_quality"], 10), pct(r["win_quality"], 50), pct(r["win_quality"], 90)
        fr = (r["fumble_A"] | r["fumble_O"]).mean()
        row = (cand, sk, wp, mr, mc, q10, q50, q90, fr, r["unresolved"])
        sym_rows.append(row)
        print(f"{cand:<10}{sk:>6}{wp:>10.3f}{mr:>10.3f}{mc:>11.2f}{q10:>8.1f}{q50:>8.1f}{q90:>8.1f}{fr:>12.3f}   unresolved={r['unresolved']}")

print()
print("=" * 100)
print("TABLE 2: ASYMMETRIC MATCHUPS -- win probability of the HIGHER-skill side (O)")
print("=" * 100)
header2 = f"{'Cand':<10}{'SkillA':>7}{'SkillO':>7}{'WinProbO':>10}{'MeanQualO(win)':>16}"
print(header2)
asym_rows = []
for cand in CANDIDATES:
    for (a, o) in ASYMMETRIC_PAIRS:
        r = simulate(cand, a, o, N_TRIALS, RNG)
        wpo = (r["winner"] == 1).mean()
        o_wins_quality = r["win_quality"][r["winner"] == 1]
        mq = np.nanmean(o_wins_quality) if o_wins_quality.size else float("nan")
        asym_rows.append((cand, a, o, wpo, mq))
        print(f"{cand:<10}{a:>7}{o:>7}{wpo:>10.3f}{mq:>16.2f}")

print()
print("=" * 100)
print("TABLE 3: 100-FUMBLE IMPACT AT HIGH SKILL (fraction of DECISIVE rounds featuring a rolled 100)")
print("=" * 100)
header3 = f"{'Cand':<10}{'Skill':>6}{'Frac decisive rounds w/ a 100':>32}"
print(header3)
fumble_rows = []
for cand in CANDIDATES:
    for sk in [99, 120, 150]:
        r = simulate(cand, sk, sk, N_TRIALS, RNG)
        frac100 = r["decisive_had_100"].mean()
        fumble_rows.append((cand, sk, frac100))
        print(f"{cand:<10}{sk:>6}{frac100:>32.4f}")

print()
print("Analytical check at Skill>=99 (only roll=100 can fail): P(exactly one side rolls 100 among decisive rounds) "
      "should dominate table 3.")
