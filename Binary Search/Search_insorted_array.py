def search(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Target mil gaya
        if arr[mid] == k:
            return mid

        # Left half sorted hai
        if arr[low] <= arr[mid]:
            if arr[low] <= k <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half sorted hai
        else:
            if arr[mid] <= k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
arr = [4, 5, 6, 7, 0, 1, 2]
k = 0
print(search(arr, k))