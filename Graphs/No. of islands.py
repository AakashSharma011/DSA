grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

class Solution:
    def valid(self,i,j,m,n):
        if i <0 or i>=m or j<0 or j>=n:
            return False
        return True

    def dfs(self,grid,i,j,vis,m,n):
        vis[i][j]=True
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        for k in range(4):
            row=i+x[k]
            col=j+y[k]
            if (self.valid(row,col,m,n) and grid[row][col]=="1" and not vis[row][col]):
                self.dfs(grid,row,col,vis,m,n)

    def numIslands(self,gris):
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*n for _ in range(m)]
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not vis[i][j]:
                    count+=1
                    self.dfs(grid,i,j,vis,n,m)
        return count


print(Solution().numIslands(grid))