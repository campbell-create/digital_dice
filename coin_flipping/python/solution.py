import random

def run_sim(l,m,n,p) -> int:
    """Simulates 1 game of the coin-flip game

    Player 1 has l coins
    Player 2 has m coins
    Player 3 has n coins

    All coins will be Heads with probability p.

    Returns:
        The number of turns it takes to oust one player.
    """
    rounds = 0
    while l > 0 and m > 0 and n > 0:
        rounds += 1
        l_flip = 0 if random.random() < p else 1
        m_flip = 0 if random.random() < p else 1
        n_flip = 0 if random.random() < p else 1
        if l_flip == m_flip == n_flip:  # no one loses a coin
            continue
        else:
            if l_flip == m_flip:
                l -= 1
                m -= 1
                n += 2
            elif m_flip == n_flip:
                m -= 1
                n -= 1
                l += 2
            elif l_flip == n_flip:
                l -= 1
                n -= 1
                m += 2
    return rounds


def run_monte_carlo(l,m,n,p) -> float:
    n_trials = 1000000
    cum_sum = 0

    for _ in range(n_trials):
        result = run_sim(l, m, n, p)
        cum_sum += result

    return cum_sum / n_trials

if __name__ == "__main__":
    l = 4
    m = 7
    n = 9
    p = 0.5
    print(
        "The average number of rounds before someone is ousted from the coin",
        "game when L =",
        l,
        "m =",
        m,
        "and n =",
        n,
        "with P(head) =",
        p,
        "is",
        run_monte_carlo(l, m, n, p),
    )
