def findMin(nums):
    l, r = 1, len(nums) - 1

    while l < r:
        if nums[l] < nums[r]:
            return nums[l]

        mid = (l + r) // 2

        if nums[mid] > nums[r]:
            l = mid + 1
        
        else:
            r = mid

    return nums[l]





if __name__ == "__main__":
    nums = [5, 6, 1, 2, 3, 4]
    print(findMin(nums))