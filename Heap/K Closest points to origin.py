from heapq import heappop, heappush
points = [[1,3],[-2,2]]
k = 1
def distance(point):
    return point[0]**2+point[1]**2
def kClosest(points, k):
    heap=[]
    for point in points:
        heappush(heap,(-distance(point),point))
        if len(heap)>k:
            heappop(heap)
    res=[]
    while heap:
        res.append(heappop(heap)[1])
    return res
print(kClosest(points,k))    