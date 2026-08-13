class Solution(object):
    def isBipartite(self, graph):
        n=len(graph)
        colour=[-1]*n
        def dfs(node,c):
            colour[node]=c
            for neigh in graph[node]:
                if colour[neigh]==-1:
                    if not dfs(neigh,1-c):
                        return False
                elif colour[neigh]==c:
                    return False
            return True
        for i in range(n):
            if colour[i]==-1:
                if not dfs(i,0):
                    return False
        
        return True
    