nums=[5,-3,2,1,-1,3,-2,2]
def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        curMax = curMin = maxSum = minSum = nums[0]

        for i in range(1, len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(maxSum, curMax)

            curMin = min(nums[i], curMin + nums[i])
            minSum = min(minSum, curMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)
print(maxSubarraySumCircular(0, nums))