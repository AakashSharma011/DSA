nums = [2,6,4,8,10,9,15]
def findUnsortedSubarray(self, nums):
        n=len(nums)
        left=n-1
        right =0
        #check Extreme left
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                left=min(left,i-1)
        # check Extreme right
        for j in range(n-2,-1,-1):
            if nums[j]>nums[j+1]:
                right=max(right,j+1)
        # Already Sorted
        if left==n-1:
            return 0
        
        # 3. Find min and max in current range
        minimum=min(nums[left:right+1])
        maximum=max(nums[left:right+1])

        while left>0 and nums[left-1]>minimum:
            left-=1
        while right <n-1 and nums[right+1]<maximum:
            right+=1
                
        return right-left+1
print(findUnsortedSubarray(0, nums))