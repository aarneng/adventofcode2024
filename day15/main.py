import re
from math import prod
from itertools import product
import numpy as np


def updategrid(grid, x, y, replacewith):
    s = grid[y]
    s_p = s[:x] + replacewith + s[x + 1:]
    grid[y] = s_p
    return grid


def move_grid(dir, pos, grid):
    nummoves = 1
    x, y = pos
    dx, dy = dir
    while grid[y + dy * nummoves][x + dx * nummoves] == "O":
        nummoves += 1
    if grid[y + dy * nummoves][x + dx * nummoves] == "#":
        return grid, pos
    grid = updategrid(grid, x + dx * nummoves, y + dy * nummoves, "O")
    grid = updategrid(grid, x + dx, y + dy, "@")
    grid = updategrid(grid, x, y, ".")
    return grid, [x + dx, y + dy]


def flatten(arr):
    return [[*elem] if isinstance(elem, tuple) else elem for subarr in arr for elem in subarr]


def move_grid2(dir, pos, grid):
    nummoves = 1
    x, y = pos
    dx, dy = dir
    if dx != 0:
        while grid[y][x + dx * nummoves] in "[]":
            nummoves += 1
        if grid[y][x + dx * nummoves] == "#":
            return grid, pos
        s_p = list(grid[y])
        minx = min(x, x + dx * (nummoves - 1))
        maxx = max(x, x + dx * (nummoves - 1)) + 1

        s_p[minx + dx: maxx + dx] = s_p[minx:maxx]
        s_p[x] = "."
        grid[y] = "".join(s_p)
        return grid, [x + dx, y]
    allpos = [pos]
    pos_history = []
    while True:
        allpos_p = set()
        for nx, ny in allpos:
            ny += dy
            if grid[ny][nx] == "#":  # Hit a wall
                return grid, pos
            allpos_p.add((nx, ny))
            if grid[ny][nx] == "[":  # Moving box right
                allpos_p.add((nx + 1, ny))
                if grid[ny][nx + 1] == "#":
                    return grid, pos
            elif grid[ny][nx] == "]":  # Moving box left
                allpos_p.add((nx - 1, ny))
                if grid[ny][nx - 1] == "#":
                    return grid, pos
        pos_history.append(allpos)
        allpos = allpos_p
        if not any(grid[ny][nx] in "[]" for nx, ny in allpos_p):
            break

    for allpos in pos_history[::-1]:
        for nx, ny in allpos:
            grid = updategrid(grid, nx, ny + dy, grid[ny][nx])
            # grid[ny + dy] = grid[ny + dy][:nx] + grid[ny][nx] + grid[ny + dy][nx + 1:]
            grid[ny] = grid[ny][:nx] + "." + grid[ny][nx + 1:]

    x, y = pos
    grid[y] = grid[y][:x] + "." + grid[y][x + 1:]
    grid[y + dy] = grid[y + dy][:x] + "@" + grid[y + dy][x + 1:]
    return grid, [x, y + dy]


def printgrid(grid):
    for row in grid:
        print(row)
    print()


def mapgrid(square):
    return {"#": "##", "O": "[]", ".": "..", "@": "@."}[square]


with open("test.txt", "r") as f:
    grid, moves = f.read().strip().split("\n\n")
    grid = grid.splitlines()
    grid2 = ["".join(map(mapgrid, row)) for row in grid]
    # printgrid(grid2)
    moves = moves.splitlines()
    robotpos = []
    robotpos2 = []
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "@":
                robotpos = [x, y]
                robotpos2 = [x*2, y]
                break
        else:
            continue

        break

    for move in "".join(moves):
        movedir = []
        if move == "<":
            movedir = [-1, 0]
        elif move == ">":
            movedir = [1, 0]
        if move == "^":
            movedir = [0, -1]
        elif move == "v":
            movedir = [0, 1]
        print(move)
        p = robotpos2
        grid, robotpos = move_grid(movedir, robotpos, grid)
        grid2, robotpos2 = move_grid2(movedir, robotpos2, grid2)
        dx = robotpos2[0] - p[0]
        dy = robotpos2[1] - p[1]
        print(abs(dy) + abs(dx))
        printgrid(grid2)

    s = 0
    s2 = 0

    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "O":
                s += 100 * y + x
    for y, row in enumerate(grid2):
        # print(row)
        for x, square in enumerate(row):
            if square == "[":
                s2 += 100 * y + x
    print(s)
    print(s2)
