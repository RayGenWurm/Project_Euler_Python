# https://projecteuler.net/problem=9
# "Special Pythagorean Triplet"
# Nov-2024 / RayGenWurm

# first try - brute force but cut out impossible combinations
# takes about 20 seconds

import time
start = time.time()

goal = 1000

for x in range(1, goal):
    print("x -", str(x))
    for y in range(x, goal):
        for z in range(y, goal):
            if x**2 + y**2 == z**2 and x+y+z == 1000:
                print("found it !")
                print(str(x), str(y), str(z))
                print("the product is:", str(x*y*z))
                break
        else: # no break
            continue
        break
    else: # no break
        continue
    break

end = time.time()
print(end - start)