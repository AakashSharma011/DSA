class Solution(object):
    def findMaxLength(self, nums):
        prefix = 0
        hashmap = {0: -1}   # prefix sum 0 first seen before array starts
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in hashmap:
                ans = max(ans, i - hashmap[prefix])
            else:
                hashmap[prefix] = i

        return ans