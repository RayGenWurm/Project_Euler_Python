# https://projecteuler.net/problem=5
# "Smallest Multiple"
# Nov-2024 / RayGenWurm

# V1 simple brute force... takes about 40 seconds on my machine

import time
start = time.time()

x = highest_divisor = 20

while True:
    for i in range(highest_divisor, 1, -1):
        if x % i != 0:
            break
    if i == 2 and x % i == 0:
        break
    x += 2

print(str(x))
end = time.time()
print(end - start)