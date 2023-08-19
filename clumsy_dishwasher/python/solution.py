
import random

NUM_WAITERS = 5
NUM_BROKEN_DISHES = 5
BREAK_THRESHOLD = 4
CLUMSY_WAITER_NUMBER = 1

def run_sim() -> int:
    """ Runs one round of the MC simulation
    Picks which waiter breaks each of NUM_BROKEN_DISHES dishes.
    Returns how many dishes our clumsy waiter broke.
    """
    clumsy_waiter_break_count = 0
    # figure out who breaks each dish
    for _ in range(0, NUM_BROKEN_DISHES):
        # pick a waiter
        waiter = random.randint(1, NUM_WAITERS)
        if waiter == CLUMSY_WAITER_NUMBER:
            clumsy_waiter_break_count += 1
    return 1 if clumsy_waiter_break_count >= BREAK_THRESHOLD else 0


def run_monte_carlo() -> float:
    n_runs = 10000000
    cum_sum = 0
    for _ in range(0, n_runs):
        result = run_sim()
        cum_sum += result
    return cum_sum / n_runs


if __name__ == "__main__":
    print(
        "The chance of the clumsy waiter breaking at least 4 of 5 dishes is",
        run_monte_carlo(),
    )
