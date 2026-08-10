adj = [
    [2,3,1],
    [0],
    [0, 4],
    [0],
    [2]
]

def dfs(adj,visited,result,node):
    result.append(node)
    visited[node]=True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(adj,visited,result,neighbor)


def dfs_traversal(adj):
    n=len(adj)
    visited=[False]*n
    result=[]
    dfs(adj,visited,result,0)
    return result

print(dfs_traversal(adj))