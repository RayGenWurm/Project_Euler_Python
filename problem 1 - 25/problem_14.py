# https://projecteuler.net/problem=14
# "Longest Collatz Sequence"
# Nov-2024 / RayGenWurm

# runs in about 14 seconds... I have no idea how to improve this so I will go with it

# UPDATE: after a bit of research => you only have to check for the upper half of possible numbers
# cuts runtime down to 8 sec

import time
start = time.time()


limit = 1000000
highest = 0
highest_i = 0

def calc_collatz(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        counter += 1
    return counter

for i in range(int(limit/2+1), limit, 2):
    if ((i - 1) // 2 + 1) % 1000 == 0: # just to print some progress while waiting
        print("progress:",i, "of 1000000")
    tmp = calc_collatz(i)
    if tmp > highest:
        highest = tmp
        highest_i = i

print(highest, highest_i)

end = time.time()
print()
print(end - start, "seconds")