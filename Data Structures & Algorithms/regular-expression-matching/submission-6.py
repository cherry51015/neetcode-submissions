class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        memo=[[None]*(n+1) for _ in range(m+1) ]
       
        def dfs(i,j):
            if j==n and i==m:
                memo[i][j]=True
                return True
            if memo[i][j] is not None:
                return memo[i][j]
            if j<n-1 and p[j+1]=='*':
                if (i<m) and (s[i]==p[j] or p[j]=='.'):
                    memo[i][j]= dfs(i,j+2) or dfs(i+1,j)
                else:
                    memo[i][j]= dfs(i,j+2)
            elif i<m and j<n and (s[i]==p[j] or p[j]=='.'):
                memo[i][j]= dfs(i+1,j+1)
            else:
                memo[i][j]=False
            
            return memo[i][j]

        return dfs(0,0)
            

        