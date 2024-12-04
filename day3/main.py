import re
from math import prod


def match_with_indices(pattern, string):
    return [(match.group(), match.start()) for match in re.finditer(pattern, string)]


with open("input.txt", "r") as f:
    lines = f.read()
    s1 = 0
    s2 = 0
    add_to_sum = True
    pattern_muls = r"mul\(\d{1,3},\d{1,3}\)"
    muls = match_with_indices(pattern_muls, lines)
    dos = [(True, match[1]) for match in match_with_indices("do\(\)", lines)]
    donts = [(False, match[1]) for match in match_with_indices("don't\(\)", lines)]
    fullmatch = [match[0] for match in sorted(muls + dos + donts, key=lambda x: x[1])]
    for match in fullmatch:
        if type(match) is str:
            nums = re.findall(r"\d{1,3}", match)
            p = prod(int(num) for num in nums)
            s1 += p
            s2 += p * add_to_sum
        else:
            add_to_sum = match
    print(s1)
    print(s2)

