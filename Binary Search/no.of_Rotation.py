arr = [4, 5, 6, 7, 0, 1, 2]

low = 0
high = len(arr) - 1
ans = float('inf')
index = -1

while low <= high:

    # Agar current part already sorted hai
    if arr[low] <= arr[high]:
        if arr[low] < ans:
            ans = arr[low]
            index = low
        break

    mid = low + (high - low) // 2

    # Left half sorted
    if arr[low] <= arr[mid]:
        if arr[low] < ans:
            ans = arr[low]
            index = low
        low = mid + 1

    # Right half sorted
    else:
        if arr[mid] < ans:
            ans = arr[mid]
            index = mid
        high = mid - 1

print("Minimum Element:", ans)
print("Number of Rotations:", index)