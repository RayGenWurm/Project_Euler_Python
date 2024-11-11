# https://projecteuler.net/problem=20
# "Factorial Digit Sum"
# Nov-2024 / RayGenWurm

# this was again way too easy..

from math import factorial


fact_list = list(str(factorial(100)))
res = 0
for i in fact_list:
    res += int(i)

print("result:", res)