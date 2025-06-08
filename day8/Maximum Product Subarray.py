def maxproduct(nums):
    res = nums[0]
    curMax, curMin = 1, 1

    for num in nums:
        tmp = curMax & num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(tmp, curMin * num, num)
        res =max(res, curMax)
    return res
    





nums = [1,2,-3,4]

print(maxproduct(nums))





























