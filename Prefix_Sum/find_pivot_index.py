nums=[1, 7, 3, 6, 5, 6]
left=0
total=sum(nums)
def PIVOTINDEX(self,nums):
    left=0
    total=sum(nums)
    for i in range(len(nums)):
        right=total-nums[i]-left
        if left==right:
            return i
        left+=nums[i]
    return -1
print(PIVOTINDEX(0,nums))   
