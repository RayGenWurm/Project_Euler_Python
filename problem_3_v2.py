# https://projecteuler.net/problem=3
# "Largest Prime Factor"
# Nov-2024 / RayGenWurm

# second try doing factorization like i would by hand...
# test show this is about 2x to 3x slower than first version...

import math
import time

start = time.time()


given_number = 600851475143
# given_number = 13195
highest_factor = 2


def is_prime(num1):
    state = True
    for x in range(2, (int(num1/2))):
        if num1 % x == 0:
            state = False
            break
    return state

def find_next_factor(num2):
    i = highest_factor
    while not is_prime(i) or (num2 % i) != 0:
        i += 1
    return i

cycle = 1
while cycle < math.sqrt(given_number):
    next_factor = find_next_factor(given_number)
    print(str(next_factor))
    given_number /= next_factor
    if next_factor > highest_factor:
        highest_factor = next_factor
    cycle += 1

print("highest factor is:", str(highest_factor))
end = time.time()
print(end - start)