class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return
        m,n= len(board),len(board[0])
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        def dfs(r,c):
            board[r][c]='#'
            for k in range(4):
                nr=r+x[k]
                nc=c+y[k]

                if 0<=nr<m and 0<=nc<n and board[nr][nc]=='O':
                    dfs(nr,nc)
            
        for i in range(m):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][n-1]=='O':
                dfs(i,n-1)
        for j in range(n):
            if board[0][j]=='O':
                dfs(0,j)
            if board[m-1][j]=='O':
                dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
            


        