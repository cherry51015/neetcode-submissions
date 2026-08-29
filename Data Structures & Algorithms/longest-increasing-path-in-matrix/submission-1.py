class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(matrix)
        n=len(matrix[0])
        memo=[[None]*(n) for _ in range(m)]
        def dfs(i,j):
            if i==m or j==n:
                return ans
            if memo[i][j] is not None:
                return memo[i][j]
            ans=1
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>matrix[i][j]:
                    ans=max(ans,1+dfs(ni,nj))
            memo[i][j]=ans
            return ans
        best=1
        for i in range(m):
            for j in range(n):
                best=max(best,dfs(i,j))
        return best


        