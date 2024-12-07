from collections import defaultdict
from tqdm import tqdm

def simulate_guard(x, y, map):
    dx, dy = -1, 0
    steps = 0
    guardstates = defaultdict(lambda: False)
    while 0 <= x + dx < len(map) and 0 <= y + dy < len(map[0]):
        while map[x+dx][y+dy] == "#":
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
        if guardstates[(x, y, dx, dy)]:
            return True
        guardstates[(x, y, dx, dy)] = True
        if map[x][y] != "*":
            steps += 1
        map[x] = map[x][:y] + "*" + map[x][y+1:]
    return steps


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    x, y = next((i, row.index("^")) for i, row in enumerate(lines) if "^" in row)
    part1 = simulate_guard(x, y, lines)
    print(part1)
    part2 = 0
    for r in tqdm(range(len(lines))):
        for c in range(len(lines[r])):
            if (r, c) == (x, y):
                continue
            new_arr = [row[:c] + '#' + row[c + 1:] if i == r else row for i, row in enumerate(lines)]
            if simulate_guard(x, y, new_arr) is True:
                part2 += 1
    print(part2)






