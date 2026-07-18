nums=[1, -2, 3, -4, 5]
def maxAbsSum(self, nums):
    maximum=minimum=ans1=ans2=nums[0]
    for i in range(1,len(nums)):
        maximum=max(maximum+nums[i],nums[i])
        minimum=min(minimum+nums[i],nums[i])
        ans1=max(maximum,ans1)
        ans2=min(minimum,ans2)
       
    return max(ans1, abs(ans2))
print(maxAbsSum(0, nums))
    