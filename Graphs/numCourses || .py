from collections import defaultdict,deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        indegree=[0]*numCourses
        graph=defaultdict(list)
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] +=1 
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        order=[]
        while q:
            node = q.popleft()
            order.append(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                
                if indegree[neigh]==0:
                    q.append(neigh)
        if len(order)==numCourses:
            return order
        return []