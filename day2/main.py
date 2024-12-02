from itertools import combinations


def check_validity(num):
    delt = [num[i + 1] - num[i] for i in range(len(num[:-1]))]
    if 0 in delt:
        return 0
    mx, mn = max(delt), min(delt)
    if mx >= 4:
        return 0
    if mn <= -4:
        return 0
    if mx > 0 > mn:
        return 0
    return 1


with open("input.txt", "r") as f:
    lines = [i.split(" ") for i in f.readlines()]
    asnums = [[int(i) for i in j] for j in lines]
    count1 = 0
    count2 = 0
    for num in asnums:
        count1 += check_validity(num)
        count2 += (sum(check_validity(i) for i in combinations(num, len(num)-1)) + check_validity(num)) >= 1
    print(count1)
    print(count2)

