def longestSubarrayWithSumK(arr: [int], k: int) -> int:
    n = len(arr)

    Sum = arr[0]
    max_len = 0
    left, right =0, 0
    
    while right < n:
        while left <= right and Sum > k:
            Sum -= arr[left]
            left += 1

        if Sum == k:
            max_len = max(max_len , right - left + 1) 
        right += 1   

        if right < n:
            Sum += arr[right]


    return max_len


arr = [1, 2, 3, 4, 5]
k = 9
print(longestSubarrayWithSumK(arr, k))  # Output: 3 (subarray [2, 3, 4])