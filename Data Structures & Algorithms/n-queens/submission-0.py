class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["."]*n for _ in range(n)]
        col=set()
        dia1=set()
        dia2=set()
        def dfs(r):
            if r==n:
                ans.append(["".join(board[i]) for i in range(n)])
                return 
            for c in range(n):
                if (c not in col) and (r+c not in dia1) and (r-c not in dia2):
                   board[r][c]='Q'
                   col.add(c)
                   dia1.add(r+c)
                   dia2.add(r-c)

                   dfs(r+1)
                   board[r][c]="."
                   col.discard(c)
                   dia1.discard(r+c)
                   dia2.discard(r-c)
                else:
                    continue
        dfs(0)
        return ans

           

        
