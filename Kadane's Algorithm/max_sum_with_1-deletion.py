nums=[1, -2, 3, -4, 5,6]
def maxSumWithOneDeletion(self, nums):
    No_deletion=nums[0]
    One_deletion=0
    ans=nums[0]
    for i in range(1,len(nums)):
        One_deletion=max(One_deletion+nums[i],No_deletion)
        No_deletion=max(No_deletion+nums[i],nums[i])
        ans=max(ans,One_deletion,No_deletion)
    return ans
print(maxSumWithOneDeletion(0, nums))