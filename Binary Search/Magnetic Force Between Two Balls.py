position = [1,2,3,4,7]
m = 3
class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        def check(distance):
            balls=1
            last=position[0]
            for x in position[1:]:
                if x-last>=distance:
                    balls+=1
                    last = x

            return balls >= m

        low=1
        high=position[-1]-position[0]
        while low<=high:
            mid=low+(high-low)//2
            if check(mid):
                low=mid+1
            else:
                high=mid-1
        return high

print(Solution().maxDistance(position,m))