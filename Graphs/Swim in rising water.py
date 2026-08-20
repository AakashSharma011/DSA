import heapq
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

class Solution(object):
    def swimInWater(self, grid):
        n=len(grid)
        m=len(grid[0])
        INF=10**8
        res=[[INF]*m for _ in range(n)]
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        pq=[]
        heapq.heappush(pq,(grid[0][0],(0,0)))
        res[0][0]=grid[0][0]

        while pq:
            money,(row,col)= heapq.heappop(pq)
            if row == n-1 and col == m-1 :
                return money
            
            for i in range(4):
                r=row+x[i]
                c= col +y[i]

                if 0>r or r>=n or c<0 or c>=m :
                    continue

                newmoney = max(grid[r][c],money)
                if newmoney < res[r][c]:
                    res[r][c]= newmoney
                    heapq.heappush(
                        pq,
                        (newmoney, (r, c))
                    )

print(Solution().swimInWater(grid))

    
        