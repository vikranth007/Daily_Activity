def maxiumsubarray(nums):
    maxSub = nums[0]
    cursum = 0

    for num in nums:
        if cursum < 0:
            cursum = 0
        cursum += num
        maxSub = max(maxSub, cursum)
    return maxSub




nums = [2,-3,4,-2,2,1,-1,4]
print(maxiumsubarray(nums))
# Output: 8








































































