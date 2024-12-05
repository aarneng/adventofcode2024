from functools import cmp_to_key


def custom_cmp(x, y):
    v = str(y) + "|" + str(x)
    isin = v in order
    isin = (2 * isin) - 1
    return isin


with open("input.txt", "r") as f:
    order, lists = f.read().split("\n\n")
    order, lists = order.splitlines(), lists.splitlines()
    lists = [list(map(int, data.split(','))) for data in lists]
    part1 = 0
    part2 = 0
    for li in lists:
        sortedlist = sorted(li, key=cmp_to_key(custom_cmp))
        if li == sortedlist:
            part1 += li[len(li) // 2]
        else:
            part2 += sortedlist[len(li) // 2]
    print(part1)
    print(part2)



