class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        dist=[[float('inf')]*n for _ in range(n)]
        a=grid[0][0]
        dist[0][0]=a
        h=[]
        
        heapq.heappush(h,(a,(0,0)))
        while h:
            wt,(i,j)=heapq.heappop(h)
            if wt>dist[i][j]:
                continue
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<n and 0<=nj<n:
                    newcost=max(wt,grid[ni][nj])
                    if newcost<dist[ni][nj]:
                        dist[ni][nj]=newcost
                        heapq.heappush(h,(newcost,(ni,nj)))

        return dist[n-1][n-1]
            

            


        