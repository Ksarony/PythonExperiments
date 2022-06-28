import random


def monte_carlo_pi(num_it):
    count = 0
    for i in range(0, num_it):
        x = random.uniform(-1.0, 1)
        y = random.uniform(-1.0, 1)
        if x ** 2 + y ** 2 < 1:
            count += 1
    pi = (count / num_it) * 4
    return pi


print(monte_carlo_pi(100))
print(monte_carlo_pi(10000))
