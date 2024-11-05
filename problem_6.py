# https://projecteuler.net/problem=6
# "Sum Square Difference"
# Nov-2024 / RayGenWurm

limit = 100
sum1 = sum2 = final_res = 0

for i in range(1, limit+1):
    sum1 += i**2

for i in range(1,limit + 1):
    sum2 += i
sum2 = sum2**2

final_res = sum2 - sum1


print(str(final_res))