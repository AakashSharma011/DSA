from heapq import heappush,heappop
arr = [1,2,3,4,5] 
k = 4
x = 3
def findClosestElements(self, arr, k, x):
        heap = []
        for num in arr:
            heappush(heap, (abs(num - x), num))
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])

        ans.sort()
        return ans
print(findClosestElements(0,arr,k,x))