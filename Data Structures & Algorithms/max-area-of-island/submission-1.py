class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            nonlocal area
            if i>=r or j>=c:
                return 
            if grid[i][j]==0:
                return
            if grid[i][j]=="#":
                return
            grid[i][j]='#'
            area+=1
            
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<r and 0<=nj<c and grid[ni][nj]==1:
                    dfs(ni,nj)
            return 
        ans=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    area=0
                    dfs(i,j)
                    ans=max(ans,area)
        return ans

        