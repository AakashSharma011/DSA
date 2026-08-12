from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[v].append(u)

        vis=[False]*numCourses
        path=[False]*numCourses
        self.cycle=False

        def dfs(node):
            vis[node]=True
            path[node]=True

            for neigh in graph[node]:
                if vis[neigh] and path[neigh]:
                    self.cycle=True
                if not vis[neigh]:
                    dfs(neigh)
            path[node]=False

        for i in range(numCourses):
            if not vis[i]:
                dfs(i)
        return not self.cycle
