class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[None]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                elif s[i]==s[j]:
                    if j-i==1:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False

        prev=float('-inf')
        for i in range(n):
            for j in range(i,n):
                if j-i+1>prev and dp[i][j]==True:
                    prev=j-i+1
                    ans=s[i:j+1]
        return ans 



                    
