nums = [0,1,0,3,12]
def moveZeroes(self, nums):
        n=len(nums)
        slow=0
        for fast in range(n):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
        for i in range(slow, n):
            nums[i] = 0
        return nums
print(moveZeroes(0, nums))