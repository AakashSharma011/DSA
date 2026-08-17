from collections import defaultdict
import heapq
times = [[2,1,1],[2,3,1],[3,4,1]] 
n = 4
k = 2
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist=[float('inf')] * (n+1)
        dist[k]=0
        heap=[(0,k)]
        while heap:
            time ,node = heapq.heappop(heap)
            if time>dist[node]:
                continue

            for neigh,weight in graph[node]:
                new_time=time+weight
                if new_time < dist[neigh]:
                    dist[neigh]=new_time
                    heapq.heappush(heap, (new_time, neigh))
            ans=max(dist[1:])
        return -1 if ans == float('inf') else ans
print(Solution().networkDelayTime(times, n, k))