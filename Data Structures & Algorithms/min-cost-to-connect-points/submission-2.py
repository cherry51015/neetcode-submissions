class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(points)-1):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                graph[(x1,y1)].append((x2,y2))
                graph[(x2,y2)].append((x1,y1))
        v=set()
        h=[]
        x,y=points[0]
        heapq.heappush(h,(0,(x,y)))
        mst=0
        while h:
            cost,(i,j)=heapq.heappop(h)
            if (i,j) in v:
                continue
            v.add((i,j))
            mst+=cost
            for ni,nj in graph[(i,j)] :
                if (ni,nj) not in v:
                    ncost=abs(i - ni)+abs(j - nj)
                    heapq.heappush(h,(ncost,(ni,nj)))
        return mst

                


        
        