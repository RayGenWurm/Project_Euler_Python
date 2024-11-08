# https://projecteuler.net/problem=10
# "Summation of Primes"
# Nov-2024 / RayGenWurm

# plain brute force is taking way too long...
# in this second try I am using optimized the "Sieve of Eratosthenes" method
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# in insight... last attempt was just stupid...
# took only 0.5 seconds - im fine with that

# I guess deleting non-prime numbers would further reduce run time but that's changing the list length and im too lazy to counter that

import time, math
start = time.time()

limit = 2000000
check_stop = int(math.sqrt(limit))
prime_sum = 0
prime_list = [2]

# fill a list with all uneven candidates
for i in range(3, limit, 2):
    prime_list.append(i)

# perform Sieve of Eratosthenes algo - 0 all non-prime numbers
check_pos = 1
while prime_list[check_pos] <= check_stop:
    divider = prime_list[check_pos]
    if divider != 0:
        for z in range(check_pos, int(limit/2), prime_list[check_pos]):
            prime_list[z] = 0
    prime_list[check_pos] = divider
    check_pos += 1



# now our list only contains prime numbers til set limit
# now just sum them up

for x in prime_list:
    if x != 0:
        prime_sum += x

print()
print("final sum:", prime_sum)


end = time.time()
print()
print(end - start, "seconds")
