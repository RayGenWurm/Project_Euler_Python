# https://projecteuler.net/problem=7
# "10001st Prime"
# Nov-2024 / RayGenWurm

goal = 10002
prime_counter = 1
i = 3

def is_prime(num1):
    state = True
    for x in range(2, (int(num1/2))):
        if num1 % x == 0:
            state = False
            break
    return state

while prime_counter != goal -1:
    if is_prime(i):
        prime_counter += 1

    if is_prime(i) and prime_counter == goal-1:
        print(str(prime_counter), "-", str(i))
    i += 2

