import re
from math import prod
from itertools import product
import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()
    mx = 0
    my = 0
    finalpositions1 = []
    steps1 = 100
    for line in data:
        x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
        mx = max(mx, x)
        my = max(my, y)
        fx = x + vx * steps1
        fy = y + vy * steps1
        finalpositions1.append([fx, fy])

    quadrants = [0] * 4
    for x, y in finalpositions1:
        x = x % (mx + 1)
        y = y % (my + 1)

        if x < mx // 2 and y < my // 2:
            quadrants[0] += 1
        if x < mx // 2 and y > my // 2:
            quadrants[1] += 1
        if x > mx // 2 and y < my // 2:
            quadrants[2] += 1
        if x > mx // 2 and y > my // 2:
            quadrants[3] += 1

    print(prod(quadrants))

    """
    SLOW!!!!
    """
    # steps2 = 0
    # mc = 0
    #
    # while steps2 <= 200000:
    #     finalpositions2 = set()
    #     for line in data:
    #         x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
    #         fx = (x + vx * steps2) % (mx + 1)
    #         fy = (y + vy * steps2) % (my + 1)
    #         finalpositions2.add((fx, fy))
    #     for x, y in product(range(mx), range(my)):
    #         cx, cy = x, y
    #         count = 0
    #         while {(cx, y), (x, cy)} <= finalpositions2:
    #             count += 1
    #             cx += 1
    #             cy += 1
    #         mc = max(mc, count)
    #         if count >= 5:
    #             print(steps2)
    #             break
    #     else:
    #         continue
    #     break
    # print(mc)
    variances_avgx = 830  # empirically tested
    variances_avgy = 830  # empirically tested
    steps2 = 0
    while steps2 <= 200000:
        finalpositions2x = []
        finalpositions2y = []
        for line in data:
            x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
            fx = (x + vx * steps2) % (mx + 1)
            fy = (y + vy * steps2) % (my + 1)
            finalpositions2x.append(fx)
            finalpositions2y.append(fy)
        finalpositions2x = np.array(finalpositions2x)
        finalpositions2y = np.array(finalpositions2y)
        vx = np.var(finalpositions2x)
        vy = np.var(finalpositions2y)
        if vx <= 0.6 * variances_avgx and vy <= 0.6 * variances_avgy:
            print(steps2)
            break
        variances_avgx = (steps2 * variances_avgx + vx) / (steps2 + 1)
        variances_avgy = (steps2 * variances_avgy + vy) / (steps2 + 1)
        steps2 += 1
