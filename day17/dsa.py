def findMin(arr):
    low = 0
    high = len(arr)-1
    ans = float('inf')
    index = -1

    while low <= high:
        mid = low + high // 2

        if arr[low] <= arr[high]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            break

        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low 
            low = mid + 1
        else:
            high = mid - 1
            if arr[mid] < ans:
                index =  mid
                ans = arr[mid]
    return index

if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    ans = findMin(arr)
    print("The minimum element is:", ans)


                