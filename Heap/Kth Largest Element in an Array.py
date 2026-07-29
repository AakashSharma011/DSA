from heapq import heappush, heappop,heapify
nums = [3,2,1,5,6,4] 
k = 2
def findKthLargest(nums, k):
    heap=nums[:k]
    heapify(heap)
    for i in range(k,len(nums)):
        if nums[i]> heap[0]:
            heappop(heap)
            heappush(heap,nums[i])
    return heap[0]
print(findKthLargest(nums,k))
        

