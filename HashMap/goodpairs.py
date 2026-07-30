nums=[1,2,3,1,1,3]
def numIdenticalPairs(self, nums):
        freq={}
        count=0
        for num in nums:
            if num in freq:
                count+=freq[num]
                freq[num]+=1
            else:
                freq[num]=1
        return count
print(numIdenticalPairs(0,nums))