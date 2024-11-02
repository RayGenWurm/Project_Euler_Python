# https://projecteuler.net/problem=3
# "Largest Prime Factor"
# Nov-2024 / RayGenWurm

# first try - simple brute forcing

import math
import time

start = time.time()

given_number = 600851475143
# given_number = 13195

def is_prime(number):
    state = True
    for x in range(2, (int(number/2))):
        if number % x == 0:
            state = False
            break
    return state


for i in range(int(math.sqrt(given_number) / 2), 0, -2):
    if given_number % i == 0:
        if is_prime(i):
            print(str(i))
            break

end = time.time()
print(end - start)