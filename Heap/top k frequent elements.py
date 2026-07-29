from heapq import heappop, heappush
nums = [1,1,1,2,2,3]
k = 2
def topKFrequent(nums, k):
    freq={}
    for num in nums:
        freq[num]=freq.get(num,0)+1
    heap=[]
    for num,count in freq.items():
        heappush(heap,(count,num))

        if len(heap)>k:
            heappop(heap)
    res=[]
    while heap:
        res.append(heappop(heap)[1])
    return res
print(topKFrequent(nums,k))

