from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V
        self.cycle = False

        def dfs(node, parent):
            visited[node] = True

            for neigh in graph[node]:
                if visited[neigh] and neigh != parent:
                    self.cycle = True

                if not visited[neigh]:
                    dfs(neigh, node)

        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        return self.cycle