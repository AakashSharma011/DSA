arr = [2,3,4,7,11]
k = 5
class Solution(object):
    def findKthPositive(self, arr, k):
        low=0
        high=len(arr)
        while low<high:
            mid= (low+high) //2
            missing=arr[mid]-mid-1
            if missing<k:
                low=mid+1
            else:
                high=mid
        return low+k
print(Solution().findKthPositive(arr,k))