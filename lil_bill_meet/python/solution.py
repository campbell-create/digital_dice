
import random

TIME_RANGE = 30  # minutes
LIL_WAIT_TIME = 5
BILL_WAIT_TIME = 7

def run_sim() -> int:
    """ Picks times of arrival for Lil and Bill and determines if they meet

    Returns 1 if they meet; 0 if they do not.
    """
    lil_arrival = 30 * random.random()
    bill_arrival = 30 * random.random()

    if lil_arrival <= bill_arrival <= lil_arrival + LIL_WAIT_TIME:
        return 1
    if bill_arrival <= lil_arrival <= bill_arrival + BILL_WAIT_TIME:
        return 1

    return 0


def run_monte_carlo() -> float:
    n_runs = 10000000
    cum_sum = 0
    for _ in range(0, n_runs):
        result = run_sim()
        cum_sum += result
    return cum_sum / n_runs

if __name__ == "__main__":
    print(
        "The chance that Lil and Bill will meet in a",
        TIME_RANGE,
        "minute period when Lil waits",
        LIL_WAIT_TIME,
        "minutes and Bill waits",
        BILL_WAIT_TIME,
        "minutes is",
        run_monte_carlo(),
    )

