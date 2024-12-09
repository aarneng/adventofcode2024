from copy import deepcopy


def index(arr, subarr):
    for i in range(len(arr) - len(subarr) + 1):
        if arr[i:i+len(subarr)] == subarr:
            return i
    return -1


def find_empty(arr, min_val=0):
    for idx, val in enumerate(arr):
        if val[0] == "." and val[1] >= min_val:
            return idx
    return -1


def checksum(st):
    s = 0
    counter = 0
    for i, c in enumerate(st):
        toadd = c[0]
        if toadd == ".":
            counter += c[1]
            continue
        s += toadd * (counter * c[1] + c[1] * (c[1] - 1) // 2)
        counter += c[1]

    return s


def prints(s):
    for val, count in s:
        print(str(val) * count, end="")
    print()


with open("input.txt", "r") as f:
    line = f.read()
    asblock1 = []
    empty = False
    counter = 0
    for char in line:
        if empty:
            asblock1 += [[".", int(char)]]
        else:
            asblock1 += [[counter, int(char)]]
            counter += 1
        empty = not empty
    asblock2 = deepcopy(asblock1)
    while find_empty(asblock1) != -1:
        last = asblock1[-1]
        idx = find_empty(asblock1)
        if asblock1[idx][1] > last[1]:
            rem = asblock1[idx][1] - last[1]
            left = asblock1[:idx]
            right = asblock1[idx+1:]
            asblock1 = left + [last] + [[".", rem]] + right
            asblock1 = asblock1[:-1]
        elif asblock1[idx][1] == last[1]:
            asblock1[idx] = last
            asblock1 = asblock1[:-1]
        else:
            asblock1[idx][0] = last[0]
            last[1] = last[1] - asblock1[idx][1]
        while asblock1[-1][0] == ".":
            asblock1 = asblock1[:-1]
    print(checksum(asblock1))
    max_len = float('inf')
    largest_tried = asblock2[-1][0]
    while find_empty(asblock2) != -1:
        min_len = float('inf')
        result, res_idx = None, None
        wherecopy = None
        for idx, x in zip(range(len(asblock2) - 1, -1, -1), reversed(asblock2)):
            l = x[1]
            if x[0] != "." and x[0] <= largest_tried:
                largest_tried -= 1
            if l < min_len and x[0] != "." and x[1] <= max_len and x[0] <= largest_tried + 1:
                wherecopy = find_empty(asblock2, l)
                if wherecopy != -1 and idx > wherecopy:
                    result = deepcopy(x)
                    res_idx = idx
                    break
                min_len = l
        else:
            break

        if asblock2[wherecopy][1] > result[1]:
            rem = asblock2[wherecopy][1] - result[1]
            left = asblock2[:wherecopy]
            right = asblock2[wherecopy + 1:]
            asblock2 = left + [result] + [[".", rem]] + right
            asblock2[res_idx + 1][0] = "."
            max_len = float('inf')
        elif asblock2[wherecopy][1] == result[1]:
            asblock2[wherecopy] = result
            asblock2[res_idx][0] = "."
            max_len = float('inf')
        else:
            max_len = result[1] - 1

    print(checksum(asblock2))
