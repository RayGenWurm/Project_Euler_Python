# https://projecteuler.net/problem=2
# "Even Fibonacci Numbers"
# Nov-2024 / RayGenWurm

limit = 4000000     # 4 million
x = 0
y = 1
tmp = 0
calc_cum = 0

while x + y < limit:
    tmp = x + y
    x = y
    y = tmp

    if y % 2 == 0:
        calc_cum += y

print(str(calc_cum))

