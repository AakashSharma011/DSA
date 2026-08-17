import heapq
heights = [[1,2,2],[3,8,2],[5,3,5]]
class Solution:
    def minimumEffortPath(self, heights):
        m=len(heights)
        n=len(heights[0])

        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=0
        pq=[(0,0,0)]
        x=[-1,1,0,0]
        y=[0,0,-1,1]

        while pq:
            effort,r,c = heapq.heappop(pq)
            if effort>dist[r][c]:
                continue
            if r == m-1 and c == n-1:
                return effort
            
            for k in range(4):
                nr=r+x[k]
                nc=c+y[k]

                if 0<=nr<m and 0<=nc<n:
                    diff= abs(heights[r][c]-heights[nr][nc])
                    new_effort =max(diff,effort)

                    if new_effort<dist[nr][nc]:
                        dist[nr][nc]=new_effort
                    
                        heapq.heappush(pq,(new_effort,nr,nc))
        return 0
print(Solution().minimumEffortPath(heights))