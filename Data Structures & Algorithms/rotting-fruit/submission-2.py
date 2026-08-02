class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque([])
        r=len(grid)
        c=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        fresh=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
            
        
        minutes=0
        while q:
            n=len(q)
            for _ in range(n):
                i,j=q.popleft()
                for di,dj in directions:
                    ni=di+i
                    nj=dj+j
                    if 0<=ni<r and 0<=nj<c and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        fresh-=1
                        q.append((ni,nj))
            if q:
                minutes+=1

            
        if fresh>0:
            return -1
        return minutes

                

        