# https://projecteuler.net/problem=15
# "Lattice Paths"
# Nov-2024 / RayGenWurm

# runs in milliseconds... pretty easy

import time
start = time.time()

size = 20

# generate grid filled with 0
my_grid = []
for y in range(size+1):
    tmp = []
    for x in range(size+1):
        tmp.append(0)
    my_grid.append(tmp)

# fill first row and column with 1
for i in range(size+1):
    my_grid[0][i] = 1
    my_grid[i][0] = 1

# now count up path for all points
# simply sum number above and left of point
for y in range(1, size+1):
    for x in range(1, size+1):
        my_grid[y][x] = my_grid[y][x-1] + my_grid[y-1][x]

print()
print("n paths: ", my_grid[size][size])

end = time.time()
print()
print(end - start, "seconds")