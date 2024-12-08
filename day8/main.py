from collections import defaultdict
from itertools import combinations


def get_antinodes(points, max_x, max_y):
    locations1 = set()
    locations2 = set()
    for a, b in combinations(points, 2):
        dir = b - a
        m1 = 1
        m2 = 1
        locations2.add(a)
        locations2.add(b)
        while 0 <= (a - dir * m1).real < max_x and 0 <= (a - dir * m1).imag < max_y:
            locations1.add(a - dir)
            locations2.add(a - dir * m1)
            m1 += 1
        while 0 <= (b + dir * m2).real < max_x and 0 <= (b + dir * m2).imag < max_y:
            locations1.add(b + dir)
            locations2.add(b + dir * m2)
            m2 += 1

    return locations1, locations2


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    points = defaultdict(list)
    max_x, max_y = len(lines[0]), len(lines)
    for y, string in enumerate(lines):
        for x, antenna in enumerate(string):
            if antenna != ".":
                points[antenna].append(complex(x, y))

    part1 = set()
    part2 = set()
    for v, p in points.items():
        p1, p2 = get_antinodes(p, max_x, max_y)
        part1 |= p1
        part2 |= p2

    print(len(part1))
    print(len(part2))


