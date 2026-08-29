class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l=len(s3)
        m=len(s1)
        n=len(s2)
        if m+n!=l:
            return False
        memo={}
        def dfs(i,j,k):
            if k==l:
                memo[(i,j,k)]=True
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            ans=False   
            if i<m and  s1[i]==s3[k]:
                ans=ans or dfs(i+1,j,k+1)
            if j<n and s2[j]==s3[k]:
               ans=ans or dfs(i,j+1,k+1)
            memo[(i,j,k)]=ans
            return memo[(i,j,k)]
        return dfs(0,0,0)





        