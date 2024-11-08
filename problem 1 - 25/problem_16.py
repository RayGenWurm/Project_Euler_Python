# https://projecteuler.net/problem=16
# "Power Digit Sum"
# Nov-2024 / RayGenWurm

# well that was the easiest problem so far...

exp = 1000

dig_sum = 0
for x in str(2**exp):
    dig_sum += int(x)

print(dig_sum)
