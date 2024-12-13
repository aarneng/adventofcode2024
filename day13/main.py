import re

def solve_input(data, add=0):
    s = 0
    for block in data:
        lines = block.split('\n')
        btn_a = btn_b = prize = None

        for line in lines:
            if line.startswith("Button A:"):
                match = re.search(r"X\+(\d+), Y\+(\d+)", line)
                if match:
                    btn_a = (int(match.group(1)), int(match.group(2)))
            elif line.startswith("Button B:"):
                match = re.search(r"X\+(\d+), Y\+(\d+)", line)
                if match:
                    btn_b = (int(match.group(1)), int(match.group(2)))
            elif line.startswith("Prize:"):
                match = re.search(r"X=(\d+), Y=(\d+)", line)
                if match:
                    prize = (int(match.group(1)), int(match.group(2)))

        x1, y1 = btn_a
        x2, y2 = btn_b
        c, d = prize
        c += add
        d += add
        a = (c * y2 - d * x2) / (x1 * y2 - y1 * x2)
        b = (d * x1 - c * y1) / (x1 * y2 - y1 * x2)
        if a == int(a) and b == int(b):
            s += int(3*a + b)

    return s


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n\n")
    print(solve_input(data))
    print(solve_input(data, 10000000000000))

