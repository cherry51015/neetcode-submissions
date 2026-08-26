class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[0]*(n) for _ in range(n)]
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                elif s[i]==s[j]:
                    if j-i==1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=0
                ans+=dp[i][j]
        return ans

        