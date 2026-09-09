nums = [2,-1,2]
k = 3
from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        dq=deque()
        n=len(nums)
        prefix=[0]*(n+1)
        ans=float('inf')
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]

        for j in range(0, n + 1):
            #front check 
            while dq and prefix[j]-prefix[dq[0]]>=k:
                ans = min(ans, j - dq[0])
                dq.popleft()
            #back check
            while dq and prefix[j]<=prefix[dq[-1]]:
                dq.pop()
            dq.append(j)
        return ans if ans != float('inf') else -1
print(Solution().shortestSubarray(nums, k))