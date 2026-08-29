piles = [3,6,7,11]
h = 8
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def form(piles,speed):
            hours=0
            for x in piles:
                hours+= (x+speed-1)//speed
            return hours
        
        low=1
        high=max(piles)
        while low<=high:
            guess=low+(high-low)//2
            hours=form(piles,guess)

            if hours>h:
                low=guess+1
            else:
                high=guess-1
        return low

print(Solution().minEatingSpeed(piles,h))