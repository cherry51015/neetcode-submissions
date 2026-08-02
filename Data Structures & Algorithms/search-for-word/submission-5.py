class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=[]
        path=[]
        r=len(board)
        c=len(board[0])
        used=[[False]*c for _ in range(r)]
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j,start):
            if board[i][j]!=word[start]:
                return False
            if used[i][j]:
                return
            if start==len(word)-1:
                return True
            used[i][j]=True
            for di,dj in directions:
                ni=di+i
                nj=dj+j
                if 0<=ni<r and 0<=nj<c:
                    if dfs(ni,nj,start+1):
                        return True
            used[i][j]=False
            return False

        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True
        return False

                        

        