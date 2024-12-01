with open("input.txt", "r") as f:
    lines = [i.split("   ") for i in f.readlines()]
    left = [int(i[0]) for i in lines]
    right = [int(i[1]) for i in lines]
    left = sorted(left)
    right = sorted(right)
    s = sum(abs(i[0] - i[1]) for i in zip(left, right))
    print(s)
    s2 = sum(right.count(i) * i for i in left)
    print(s2)
