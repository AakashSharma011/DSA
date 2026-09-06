trips = [[2,1,5],[3,3,7]]
capacity = 4
class Solution(object):
    def carPooling(self, trips, capacity):
        changes=[0]*1001
        for passengers,start,end in trips:
            changes[start]+=passengers
            changes[end]-=passengers
        current=0
        for i in range(1001):
            current+=changes[i]
            if current>capacity:
                return False
        return True


print(Solution().carPooling(trips,capacity))