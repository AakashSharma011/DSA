nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(self, nums):
        best=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1= best+nums[i]
            v2=nums[i]
            best=max(v1,v2)
            ans=max(best,ans)
        return ans
print(maxSubArray(0, nums))