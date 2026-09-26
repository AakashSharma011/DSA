nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
def longestOnes(self, nums, k):
        left=0
        freq={}
        ans=0
        for right in range(len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1
            zero_freq=freq.get(0,0)
            while zero_freq>k:
                freq[nums[left]]-=1
                if nums[left]==0:
                    zero_freq-=1

                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
print(longestOnes(0, nums, k))