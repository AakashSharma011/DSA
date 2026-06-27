arr = [1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11]
low = 0
high = len(arr) - 1
x = 2
answer = -1   # safe default

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] >= x:
        answer = mid
        high = mid - 1   # go left
    else:
        low = mid + 1

print("Lower bound of", x, "is at index", answer)