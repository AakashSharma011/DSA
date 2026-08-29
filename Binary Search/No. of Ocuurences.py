arr = [1, 1, 2, 2, 2, 2, 3]
target = 4

class Solution:
    def lowerbound(self,arr,target):
        low=0
        high=len(arr)-1
        ans=len(arr)
        while low<=high:
            mid=low + (high-low)//2
            if arr[mid]>= target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def upperbound(self,arr,target):
        low=0
        high=len(arr)-1
        ans=len(arr)
        while low<=high:
            mid=low + (high-low)//2
            if arr[mid]>target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def countFreq(self, arr, target):
        lb=self.lowerbound(arr,target)
        ub=self.upperbound(arr,target)
        return ub-lb
print(Solution().countFreq(arr,target))