# https://projecteuler.net/problem=13
# "Large Sum"
# Nov-2024 / RayGenWurm

# this one was pretty simple...

intput_file = "problem_13_input.txt"
big_sum = 0

with open(intput_file) as f:
    for line in f:
        big_sum += int(line)

sum_10_dig = ""
tmp = str(big_sum).split()
print(tmp)
for i in range(10):
    sum_10_dig += str(tmp[0][i])

print(sum_10_dig)