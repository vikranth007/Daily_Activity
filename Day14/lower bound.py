def lower_bound(arr, target, n):
    low = 0
    high = n-1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans


arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 9, 10, 11]
target = 8
n = len(arr)

print(lower_bound(arr, target, n))
