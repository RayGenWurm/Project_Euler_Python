# https://projecteuler.net/problem=5
# "Smallest Multiple"
# Nov-2024 / RayGenWurm

# V2 ugly but maybe it's faster... after some testing => yes it is about 4x faster and takes around 1s !

import time
start = time.time()
x = 20

while True:
    if\
    x % 20 == 0 and \
    x % 19 == 0 and \
    x % 18 == 0 and \
    x % 17 == 0 and \
    x % 16 == 0 and \
    x % 15 == 0 and \
    x % 14 == 0 and \
    x % 13 == 0 and \
    x % 12 == 0 and \
    x % 11 == 0:
        break
    x += 20

print(x)
end = time.time()
print(end - start)