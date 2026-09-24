nums = [10,5,2,6]
k = 100
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    prod = 1
    ans = left = 0
    for right, value in enumerate(nums):
        prod *= value
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
print(numSubarrayProductLessThanK(nums, k))