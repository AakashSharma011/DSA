from heapq import heappop, heappush
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
def findMaximizedCapital(self, k, w, profits, capital):
    projects= list(zip(capital, profits))
    projects.sort()
    heap=[]
    i=0
    n=len(projects)
    for _ in range(k):
        while i<n and projects[i][0]<=w:
            heappush(heap, -projects[i][1])
            i+=1
        if not heap:
            break
        w+=-heappop(heap)
    return w
print(findMaximizedCapital(0,k,w,profits,capital))
        