# https://projecteuler.net/problem=1
# "Multiples of 3 or 5"
# Nov-2024 / RayGenWurm

limit = 1000
calc_sum = 0

for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
        calc_sum += i

print(str(calc_sum))