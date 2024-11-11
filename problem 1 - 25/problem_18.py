# https://projecteuler.net/problem=18
# "Number Letter Counts"
# Nov-2024 / RayGenWurm

# my most complicated algo so far...
# the code calculates every combination for the next *depth* layers and chooses the best one an from there again searches for *depth* layers

import time
start = time.time()


intput_file = "problem_18_input.txt"
depth = 3       # search-depth => higher is better but slower


# fill list with input values
tri_str = []
with open(intput_file) as f:
    for line in f:
        tri_str.append(line.strip().split(" "))


# remove leading 0s
tri_int = []
for str_y in tri_str:
    tmp_l = []
    for str_x in str_y:
        tmp = str_x.split()
        if tmp[0] == "0":
            tmp_l.append(int(tmp[1]))
        else:
            tmp_l.append(int(str_x))
    tri_int.append(tmp_l)


# add depth many extra layer with 00s to simplify loop logic
n_layer = len(tri_int)
for o in range(1, depth+1):
    tm = []
    for oo in range(n_layer+o):
        tm.append(0)
    tri_int.append(tm)



def dec_to_bin(n, d):
    my_format = "{0:0" + str(d) + "b}"
    return my_format.format(n)

def calc_path_sum(dir,x,y,path_sum):
    tmp_list = list(str(dir))
    for i in range(len(tmp_list)):
        if tmp_list[i] == "0":
            path_sum += tri_int[y+1][x]
        else:
            path_sum += tri_int[y+1][x+1]
            x += 1
        y+=1
    return path_sum

def first_move(dir, d):
    first = ("{0:0" + str(d) + "b}").format(dir)
    return first[0]



path = [tri_int[0][0]]
pos = [0,0]
last_highest_test = [0,0]



for step in range(len(tri_int)-depth-1):
    highest = [0,tri_int[0][0]]

    tmp_sum = 0
    for i in range(2**depth):
        tmp_sum = calc_path_sum(dec_to_bin(i, depth),pos[0],pos[1],0)
        if tmp_sum > highest[1]:
            highest[0] = i
            highest[1] = tmp_sum

    next_move = first_move(highest[0], depth)
    if int(next_move) == 0:
        path.append(tri_int[pos[1]+1][pos[0]])
    else:
        path.append(tri_int[pos[1]+1][pos[0]+1])
        pos[0] += 1
    pos[1] += 1


print(path)

xsum = 0
for m in path:
    xsum += m

print("sum:", xsum)
end = time.time()
print()
print(end - start, "seconds")



# print as triangle and as list... just for overview
# for step in tri_int:
#     print(str(step).center(100))

# for step in tri_int:
#     print(step)