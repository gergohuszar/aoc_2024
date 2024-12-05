import pandas as pd


def list_check(nums):
    if nums.is_monotonic_increasing or nums.is_monotonic_decreasing:
        if nums.diff()[1:].abs().between(1, 3).all():
            return True
    return False


count = 0
with open("input.txt") as f:
    lines = f.readlines()
    lines = [x.strip().split(" ") for x in lines]
    for line in lines:
        nums = [int(i) for i in line]
        nums: pd.Series = pd.Series(nums)
        if list_check(nums):
            count += 1

print(count)
