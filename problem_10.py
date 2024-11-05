# https://projecteuler.net/problem=10
# "Summation of Primes"
# Nov-2024 / RayGenWurm

# plain brute force is taking way too long...
# in this first try i am using the "Sieve of Eratosthenes" method
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# took me about 50 MINUTES to compute... but it works!

import time, math, itertools
start = time.time()

limit = 2000000
check_stop = int(math.sqrt(limit))
prime_sum = 0
prime_list = [2]

# fill list with all uneven candidates
for i in range(3, limit, 2):
    prime_list.append(i)

# perform Sieve of Eratosthenes algo
check_pos = 1
while prime_list[check_pos] <= check_stop:
    divider = prime_list[check_pos]
    print(divider)
    for index, item in enumerate(list(prime_list)):
        if index == check_pos:
            continue
        if index % 1000 == 0:
            print(divider, index)
        if item % divider == 0:
            prime_list.remove(item)
    check_pos += 1

# now our list only contains prime numbers til set limit


# now just sum them up

for x in prime_list:
    prime_sum += x

print()
print("final sum:", prime_sum)

# print()
# print(prime_list)

end = time.time()
print()
print(end - start, "seconds")

# 5736396