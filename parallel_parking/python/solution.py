import random

def run_monte_carlo(num_cars: int) -> float:
    total_mn = 0
    num_runs = 1000000

    for _ in range(1, num_runs + 1):
        pos = sorted([random.random() for _ in range(num_cars)])
        nn = []
        nn.append(1)
        for i in range(1, num_cars - 1): # go from 1 to num_cars - 2
            if pos[i] - pos[i-1] < pos[i+1] - pos[i]:
                nn.append(i - 1)
            else:
                nn.append(i + 1)
        nn.append(num_cars - 2)

        mn = 0
        if nn[2] == 1:
            mn += 1

        i = 1
        while i < num_cars:
            if nn[i] == i + 1 and nn[i+1] == i:
                mn += 1
                i += 2
            else:
                i += 1

        #breakpoint()
        total_mn += mn

    return 2 * total_mn / (num_runs * num_cars)

if __name__ == "__main__":
    num_cars = 30
    print(
        "for",
        num_cars,
        "cars parked on a street, the probability of randomly selecting one",
        "that has a mutual nearest neighbor is",
        run_monte_carlo(num_cars),
        "percent",
    )
