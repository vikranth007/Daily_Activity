def Duplicate(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False



nums = [1, 2, 3, 4]

if __name__ == "__main__":
    print(Duplicate(nums))





































    