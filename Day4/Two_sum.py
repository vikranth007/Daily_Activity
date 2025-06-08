def twosum(nums, target):
    prev = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev:
            return [prev[diff],i]
        prev[n] = i
    return







nums =  [2, 1, 5, 3, 4, 2]
target = 4
print(twosum(nums, target))
