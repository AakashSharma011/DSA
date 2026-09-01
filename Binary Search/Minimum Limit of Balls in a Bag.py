nums = [9]
maxOperations = 2
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        def check(guess):
            operations=0
            for x in nums:
                if x>guess:
                    operations+=(x-1)//guess
            return operations <= maxOperations

        
        low=1
        high=max(nums)
        ans=high
        while low<=high:
            mid=low+(high-low)//2

            if check(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

print(Solution().minimumSize(nums, maxOperations))