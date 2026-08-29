def searchInfinite(nums, target):
    low = 0
    high = 1

    # Find a range containing target
    while nums[high] < target:
        low = high
        high = high * 2

    # Normal binary search
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1