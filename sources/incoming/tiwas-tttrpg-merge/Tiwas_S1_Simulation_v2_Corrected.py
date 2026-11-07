import numpy as np

def roll_d100(n, rng):
    return rng.integers(1, 101, size=n)

def succeeds(roll, skill):
    return (roll <= skill) & (roll != 100)

def q_margin(roll, skill):
    return (skill - roll).astype(np.float64)

def q_blackjack(roll, skill):
    return roll.astype(np.float64)

def q_hybrid_committed(roll, skill):
    # S-1C, DOCUMENTED formula per Comparative Design Direction Brief Sec 2.1:
    # Committed = Roll + max(0, Skill - 99)
    return roll.astype(np.float64) + max(0, skill - 99)

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
    forced_guard_A = np.zeros(n_trials, dtype=bool)  # only used by stance_variant (S-1D)
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
            qA, qO = q_margin(roll_A, skill_A), q_margin(roll_O, skill_O)
        elif candidate == "blackjack":
            qA, qO = q_blackjack(roll_A, skill_A), q_blackjack(roll_O, skill_O)
        elif candidate == "hybrid_committed":
            qA, qO = q_hybrid_committed(roll_A, skill_A), q_hybrid_committed(roll_O, skill_O)
        elif candidate == "stance_variant":
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

        if candidate == "stance_variant":
            new_forced_A = np.zeros(n, dtype=bool)
            new_forced_O = np.zeros(n, dtype=bool)
            committed_fail_A = stance_A_committed & ~succ_A & neither
            committed_fail_O = stance_O_committed & ~succ_O & neither
            new_forced_A[committed_fail_A] = True
            new_forced_O[committed_fail_O] = True
            forced_guard_A[idx] = new_forced_A
            forced_guard_O[idx] = new_forced_O

    winner_cost = np.where(winner == 0, cost_A, cost_O)
    loser_cost = np.where(winner == 0, cost_O, cost_A)

    return dict(
        winner=winner, rounds=rounds, cost_A=cost_A, cost_O=cost_O,
        winner_cost=winner_cost, loser_cost=loser_cost,
        win_quality=win_quality, fumble_A=fumble_A, fumble_O=fumble_O,
        decisive_had_100=decisive_had_100, unresolved=int(active.sum())
    )

if __name__ == "__main__":
    rng = np.random.default_rng(42)
    for cand in ["margin", "blackjack", "hybrid_committed", "stance_variant"]:
        r = simulate(cand, 55, 55, 5000, rng)
        wp = (r["winner"] == 0).mean()
        print(cand, "win%A=", round(wp, 3), "unresolved=", r["unresolved"],
              "mean_rounds=", round(r["rounds"].mean(), 3))
