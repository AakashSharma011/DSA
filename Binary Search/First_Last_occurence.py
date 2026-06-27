def lower_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def first_last_occurrence(arr, x):
    lb = lower_bound(arr, x)

    # x doesn't exist
    if lb == len(arr) or arr[lb] != x:
        return (-1, -1)

    ub = upper_bound(arr, x)

    return (lb, ub - 1)


# Driver Code
arr = [1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11]
x = 2

print(first_last_occurrence(arr, x))