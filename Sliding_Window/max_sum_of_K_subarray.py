nums=[1,43,5,4,324,1,3,22,34]
def max_sum_of_k_subarray(nums, k):
    max_sum= window_sum= sum(nums[:k])
    for i in range(k,len(nums)):
        window_sum+=nums[i]
        window_sum-=nums[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum
print(max_sum_of_k_subarray(nums,3))