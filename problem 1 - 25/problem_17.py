# https://projecteuler.net/problem=17
# "Number Letter Counts"
# Nov-2024 / RayGenWurm

# tricky one... took me a while to get right
# runs

limit = 1000


letters_19 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]   # 0, 1, 2, 3... 19
letters_10 = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]                                 # 0, 0, 20, 30, 40 ... 90


letter_sum = 0

for i in range(1, limit + 1):

    # 0-19
    if i < 20:
        letter_sum += letters_19[i]

    # 20 - 99
    elif i < 100:
        tmp = list(str(i))
        letter_sum += letters_10[int(tmp[0])] + letters_19[int(tmp[1])]

    # 100 - 999
    elif i < 1000:
        tmp = list(str(i))
        if tmp[int(1)] == "0" and tmp[int(2)] == "0":
            letter_sum += letters_19[int(tmp[0])] + 7
        else:
            tmpx = int(tmp[1] + tmp[2])
            if tmpx < 20:
                letter_sum += letters_19[int(tmp[0])] + 10 + letters_19[tmpx]
            else:
                letter_sum += letters_19[int(tmp[0])] + 10 + letters_10[int(tmp[1])] + letters_19[int(tmp[2])]

    # 1000
    elif i == 1000:
        letter_sum += 11

    else:
        print("ERROR this should never execute !")

print("final sum: ", letter_sum)


