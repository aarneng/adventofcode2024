from collections import defaultdict


def blink(stones):
    ret = defaultdict(lambda: 0)
    for key, val in stones.items():
        if key == 0:
            ret[1] += val
        elif len(str(key)) % 2 == 0:
            num = str(key)
            ret[int(num[:len(num) // 2])] += val
            ret[int(num[len(num) // 2:])] += val
        else:
            ret[key * 2024] += val
    return ret


with open("input.txt", "r") as f:
    lines = f.read().strip().split(" ")
    lines = {int(x): lines.count(x) for x in set(lines)}
    for i in range(75):
        lines = blink(lines)
    s = 0
    for key, val in lines.items():
        s += val
    print(s)
