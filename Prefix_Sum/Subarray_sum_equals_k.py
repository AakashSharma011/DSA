nums=[1,2,3]
def subarraySum(nums, k):
    couunt=0
    prefix={0:1}
    curr_sum=0
    for num in nums:
        curr_sum+=num
        if curr_sum-k in prefix:
            couunt+=prefix[curr_sum-k]
        if curr_sum in prefix:
            prefix[curr_sum]+=1
        else:
            prefix[curr_sum]=1
    return couunt
print(subarraySum(nums,3))