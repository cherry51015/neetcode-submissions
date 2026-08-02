class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        count=0
        v=[[-1]*c for _ in range(r)]
        def dfs(i,j):
            if i>=r or j>=c:
                return
            if grid[i][j]=="0":
                return 
            if v[i][j]==1:
                return
            v[i][j]=1
            
            for di,dj in directions:
                ni=di+i
                nj=dj+j
                if 0<=ni<r and 0<=nj<c and grid[ni][nj]=="1":
                    dfs(ni,nj)
            return False
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1" and v[i][j]==-1:
                    count+=1
                    dfs(i,j)
                        
        return count


        