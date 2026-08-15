from collections import defaultdict,deque
class Solution:
    def shortestPath(self, V, edges, src, dest):
        graph=defaultdict(list)
        result=[-1]*V
        visited=[0]*V
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        q=deque()
        q.append((src,0))
        visited[src]=1
        while q:
           node,distance= q.popleft()
           result[node]=distance
           
           for neigh in graph[node]:
                if visited[neigh]==0:
                    q.append((neigh,distance+1))
                    visited[neigh]=1
        
        return result[dest]
                    
            
        