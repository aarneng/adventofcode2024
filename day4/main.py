# def get_possible_paths(x, y, max_x, max_y):
#     directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#     paths = [
#         (x + dx, y + dy) for dx, dy in directions
#         if 0 <= x + dx < max_x and 0 <= y + dy < max_y
#     ]
#     return paths
#
#
# def get_num_match(x, y, max_x, max_y, lines, want="XMAS"):
#     current = want[0]
#     if lines[y][x] != current:
#         return 0
#     want = want[1:]
#     if want == "":
#         return 1
#     s = 0
#     for coords in get_possible_paths(x, y, max_x, max_y):
#         s += get_num_match(*coords, max_x, max_y, lines, want)
#     return s


def num_x_maxses(max_x, max_y, lines):
    windows = []
    for i in range(max_y - 2):
        for j in range(max_x - 2):
            window = lines[i:i + 3, j:j + 3]
            windows.append(window)
    return windows


def get_possible_paths_n_grouped(x, y, max_x, max_y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    grouped_paths = []
    depth = 3

    for dx, dy in directions:
        path = []
        for step in range(1, depth + 1):
            new_x, new_y = x + step * dx, y + step * dy
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                path.append((new_x, new_y))
            else:
                break
        if path:
            grouped_paths.append(path)

    return grouped_paths


def get_num_match(x, y, max_x, max_y, lines, want="XMAS"):
    if lines[y][x] != want[0]:
        return 0
    want = want[1:]
    total1 = 0
    for path in get_possible_paths_n_grouped(x, y, max_x, max_y):
        if len(path) != 3:
            continue
        for i, coord in enumerate(path):
            xx, yy = coord
            if lines[yy][xx] != want[i]:
                break
        else:
            total1 += 1
    return total1


def get_window(x, y, max_x, max_y, lines):
    if x + 2 >= max_x or y + 2 >= max_y:
        return False
    return [row[y:y + 3] for row in lines[x:x + 3]]


def is_x_mas(x, y, max_x, max_y, lines):
    window = get_window(x, y, max_x, max_y, lines)
    if not window:
        return 0
    if window[1][1] != "A":
        return 0
    if window[0][0] == "M":
        if window[0][2] == "M":
            return window[2][0] == "S" == window[2][2]
        if window[2][0] == "M":
            return window[0][2] == "S" == window[2][2]
    if window[2][2] == "M":
        if window[0][2] == "M":
            return window[2][0] == "S" == window[0][0]
        if window[2][0] == "M":
            return window[0][2] == "S" == window[0][0]
    return 0


with open("test.txt", "r") as f:
    lines = f.read().splitlines()
    max_y = len(lines)
    max_x = len(lines[0])
    part1 = 0
    part2 = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            part1 += get_num_match(x, y, max_x, max_y, lines)
            part2 += is_x_mas(x, y, max_x, max_y, lines)
    print(part1)
    print(part2)
