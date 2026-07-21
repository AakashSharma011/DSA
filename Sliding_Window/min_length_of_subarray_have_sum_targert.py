nums = [2,3,1,2,4,3]
def minfind(nums,target):
    left=0
    window_sum=0
    min_len=float('inf')
    for right in range(len(nums)):
        window_sum+=nums[right]
        while window_sum>=target:
            min_len=min(min_len,right-left+1)
            window_sum-=nums[left]
            left+=1
    if min_len == float('inf'):
        return 0
    return min_len
print(minfind(nums,7))