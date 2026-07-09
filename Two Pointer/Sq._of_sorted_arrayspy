nums=[-4,-6,-1,0,2,3,5]
def sortedSquares(self, nums):
        n=len(nums)
        result=[0]*n
        left =0
        right=n-1
        pos=n-1
        
        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos]=nums[left]*nums[left]
                left+=1
            else:
                result[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return result
print(sortedSquares(0,nums))
        