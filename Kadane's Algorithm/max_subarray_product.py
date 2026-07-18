nums=[2, 3, -2, 4]
def Maxproduct(self,nums):
    ans=mini=best=nums[0]
    for i in range(1,len(nums)):
        v1=best*nums[i]
        v2=nums[i]
        v3=mini*nums[i]
        best=max(v1,v2,v3)
        mini=min(v1,v2,v3)
        ans=max(best,ans)
    return ans
print(Maxproduct(0, nums))