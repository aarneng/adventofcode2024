def ways(lines):
    h = len(lines)
    w = len(lines[0])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def f(i, j, m, v):
        if lines[i][j] == '9':
            return 1
        if (i, j) in m:
            return m[(i, j)]
        if (i, j) in v:
            return 0
        v.add((i, j))
        s = 0
        c = int(lines[i][j])
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w:
                n = int(lines[ni][nj])
                if n - c == 1:
                    s += f(ni, nj, m, v)
        v.remove((i, j))
        m[(i, j)] = s
        return s
    s = 0
    for i in range(h):
        for j in range(w):
            if lines[i][j] == '0':
                currs = f(i, j, {}, set())
                s += currs
    return s


def reachable_nines(lines):
    h = len(lines)
    w = len(lines[0])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def f(i, j, m, v):
        if lines[i][j] == '9':
            return frozenset([(i, j)])
        if (i, j) in m:
            return m[(i, j)]
        if (i, j) in v:
            return frozenset()
        v.add((i, j))
        s = frozenset()
        c = int(lines[i][j])
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w:
                if lines[ni][nj] == ".":
                    continue
                n = int(lines[ni][nj])
                if n - c == 1:
                    s = s.union(f(ni, nj, m, v))
        m[(i, j)] = s
        v.remove((i, j))
        return s

    s = 0
    for i in range(h):
        for j in range(w):
            if lines[i][j] == '0':
                currs = len(f(i, j, {}, set()))
                s += currs
                # print((i, j), currs)
    return s


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    print(reachable_nines(lines))
    print(ways(lines))
