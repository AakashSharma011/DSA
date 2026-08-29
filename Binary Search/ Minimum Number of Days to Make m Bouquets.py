bloomDay = [1,10,3,10,2]
m = 3
k = 1
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay)<m*k:
            return -1
        
        def check(days):
            flowers=0
            bouquets=0
            
            for x in bloomDay:
                if x<=days:
                    flowers+=1
                else:
                    flowers=0
                
                if flowers ==k:
                    bouquets+=1
                    flowers=0
            return bouquets >=m
        
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=low+(high-low)//2

            if check(mid):
                high=mid-1
            else:
                low=mid+1
        return low
print(Solution().minDays(bloomDay,m,k))