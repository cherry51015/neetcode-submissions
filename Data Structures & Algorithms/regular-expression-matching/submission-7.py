class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[m][n]=True
        for i in range(m,-1,-1):
            for j in range(n-1,-1,-1):
                if j<n-1 and p[j+1]=='*':
                    if (i<m) and (s[i]==p[j] or p[j]=='.'):
                        dp[i][j]= dp[i][j+2] or dp[i+1][j]
                    else:
                        dp[i][j]= dp[i][j+2]
                elif  i<m and (s[i]==p[j] or p[j]=='.'):
                    dp[i][j]= dp[i+1][j+1]   
        return dp[0][0]

        