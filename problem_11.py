# https://projecteuler.net/problem=11
# "Highly Divisible Triangular Number"
# Nov-2024 / RayGenWurm

# execution time: 7 seconds... im happy with it
# I guess there is a faster way working with primes but im too lazy for this ;)

from math import sqrt, floor
import time, math
start = time.time()

goal = 500

def gen_triangle(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def find_factors(x):
    n_fact = 0
    for i in range(1, floor(sqrt(x))):
        if x % i == 0:
            n_fact += 1
    return n_fact*2


result = 2
while find_factors(gen_triangle(result)) <= goal:
    result +=1

print("answer:", gen_triangle(result))

end = time.time()
print()
print(end - start, "seconds")