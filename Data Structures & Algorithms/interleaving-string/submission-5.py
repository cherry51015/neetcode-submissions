class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l=len(s3)
        m=len(s1)
        n=len(s2)
        if m+n!=l:
            return False
        c1=0
        c2=0
        memo={}
        def dfs(i,j,k):
            nonlocal c1,c2
            if k==l and abs(c1-c2)<=1:
                memo[(i,j,k)]=True
                return True
            if i==m:
                if s2[j:]==s3[k:]:
                    memo[(i,j,k)]=True
                    return True
                else:
                    memo[(i,j,k)]=False
                    return False
            if j==n:
                if s1[i:]==s3[k:]:
                    memo[(i,j,k)]=True
                    return True
                else:
                    memo[(i,j,k)]=False
                    return False
            if (i,j,k) in memo:
                return memo[(i,j,k)]

            if s1[i]==s3[k] and s2[j]==s3[k]:
                memo[(i,j,k)]= dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
                return memo[(i,j,k)]
            if s1[i]==s3[k]:
                c2+=1
                memo[(i,j,k)]= dfs(i+1,j,k+1)
                return memo[(i,j,k)]
            if s2[j]==s3[k]:
                c1+=1
                memo[(i,j,k)]= dfs(i,j+1,k+1)
                return memo[(i,j,k)]
            memo[(i,j,k)]=False
            return memo[(i,j,k)]
        return dfs(0,0,0)





        