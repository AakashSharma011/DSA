from collections import deque
adj = [
    [2,3,1],
    [0],
    [0, 4],
    [0],
    [2]
]

def bfs(adj):
    n=len(adj)
    vis=[False]*n
    q= deque()
    res=[]
    q.append(0)
    vis[0]=True

    while q:
        node=q.popleft()
        res.append(node)
        for neigh in adj[node]:
            if not vis[neigh]:
                q.append(neigh)
                vis[neigh]=True
    return res  
print(bfs(adj))