class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque([])
        r=len(grid)
        c=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        minutes=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j,0))
        while q:
            i,j,minutes=q.popleft()
            for di,dj in directions:
                ni=di+i
                nj=dj+j
                if 0<=ni<r and 0<=nj<c and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    q.append((ni,nj,minutes+1))
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        return minutes

                

        