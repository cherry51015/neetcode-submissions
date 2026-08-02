class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r=len(board)
        c=len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)] 
        def dfs(i,j):
            if i>=r or i<0 or j<0 or j>=c:
                return
            if board[i][j]!='O':
                return
            board[i][j]='S'
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<r and 0<=nj<c and board[ni][nj]=='O':
                    dfs(ni,nj)
  
        for i in range(r):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][c-1]=='O':
                dfs(i,c-1)
        for j in range(c):
            if board[0][j]=='O':
                dfs(0,j)
            if board[r-1][j]=='O':
                dfs(r-1,j)
        for i in range(r):
            for j in range(c):
                if board[i][j]=='S':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        
            

            