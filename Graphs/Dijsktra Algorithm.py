import heapq
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        graph=[[] for _ in range(V)]
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
             
        
        dist=[float('inf')]*V
        dist[src]=0
        
        pq=[(0,src)]
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            
            for neigh,wt in graph[node]:
                new_dist=d+wt
                if new_dist<dist[neigh]:
                    dist[neigh]=new_dist
                    heapq.heappush(pq,(new_dist,neigh))
        return dist

print(Solution().dijkstra(V, edges, src))
