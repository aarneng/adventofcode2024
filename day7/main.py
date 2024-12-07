from itertools import product
from tqdm import tqdm


def is_result_possible(result, nums, numops=3):
    all_operators = [
        lambda x, y: x+y,
        lambda x, y: x * y,
        lambda x, y: int(str(x) + str(y))
    ]
    operators = all_operators[:numops]
    for op in product(operators, repeat=len(nums) - 1):
        ans = nums[0]
        for val, func in zip(nums[1:], op):
            ans = func(ans, val)
            if ans > result:
                break
        if result == ans:
            if all_operators[-1] in op:
                _, ans_less_ops = is_result_possible(result, nums, 2)
                return True, ans_less_ops
            return True, True
    return False, False


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    data = [(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))) for line in lines]
    part1 = 0
    part2 = 0
    for calibration, nums in tqdm(data):
        ans_p2, ans_p1 = is_result_possible(calibration, nums)
        part1 += calibration * ans_p1
        part2 += calibration * ans_p2
    print(part1)
    print(part2)


