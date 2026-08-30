class Solution(object):
    def splitArray(self, nums, k):

        def check(mid):
            total = 0
            count = 1

            for x in nums:
                if total + x > mid:
                    count += 1
                    total = x
                else:
                    total += x

            return count <= k

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low) // 2

            if check(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low