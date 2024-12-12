from collections import defaultdict


def flood_fill(lines, y, x, label, labels, plant_map):
    stack = [(y, x)]
    original_plant = lines[y][x]
    plant_map[label] = original_plant
    while stack:
        cy, cx = stack.pop()
        if labels[cy][cx] != 0:
            continue
        labels[cy][cx] = label
        for ny, nx in [(cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)]:
            if 0 <= ny < len(lines) and 0 <= nx < len(lines[0]):
                if lines[ny][nx] == original_plant and labels[ny][nx] == 0:
                    stack.append((ny, nx))


def calculate_areas(lines):
    labels = [[0] * len(lines[0]) for _ in lines]
    plant_map = {}
    label = 0

    for y, line in enumerate(lines):
        for x, plant in enumerate(line):
            if labels[y][x] == 0:
                label += 1
                flood_fill(lines, y, x, label, labels, plant_map)

    counts = defaultdict(lambda: 0)
    areas = defaultdict(lambda: 0)
    for y, line in enumerate(lines):
        for x, plant in enumerate(line):
            lbl = labels[y][x]
            add_area = 4
            if y != 0 and labels[y - 1][x] == lbl:
                add_area -= 2
            if x != 0 and labels[y][x - 1] == lbl:
                add_area -= 2
            counts[lbl] += 1
            areas[lbl] += add_area

    s = 0
    for lbl, area in areas.items():
        s += area * counts[lbl]
    print(s)


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    calculate_areas(lines)
