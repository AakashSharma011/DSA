nums = [4,5,0,-2,-3,1]
k = 5
def subarraySum(nums, k):
    Sum=0
    hashmap={0:1}
    ans=0
    for i in nums:
        Sum+=i
        rem =Sum % k
        if rem < 0:
            rem += k
        if rem in hashmap:
            ans+=hashmap[rem]
            hashmap[rem]+=1
        else:
            hashmap[rem]=1
    return ans
print(subarraySum(nums,k))