# https://projecteuler.net/problem=4
# "Largest Palindrome Product"
# Nov-2024 / RayGenWurm

limit = 99     # 2 digit
limit = 999    # 3 digit
highest = 0
a = 0
b = 0

def check_it(n1, n2):
    if str(n1 * n2) == str(n1 * n2)[::-1]:
        return True
    else:
        return False

print(check_it(99, 91))

for x in range(limit, 2, -1):
    for y in range(limit, 2, -1):
        if check_it(x,y) and x*y > highest:
            highest = x*y
            a = x
            b = y

print(str(highest), str(a), str(b))