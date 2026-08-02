class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque([])
        r=len(grid)
        c=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    q.append((i,j,0))
        while q:
            i,j,dist=q.popleft()
            for di,dj in directions:
                ni=di+i
                nj=dj+j
                if 0<=ni<r and 0<=nj<c and  grid[ni][nj]==2147483647:
                    grid[ni][nj]=dist+1
                    q.append((ni,nj,grid[ni][nj]))
        

        