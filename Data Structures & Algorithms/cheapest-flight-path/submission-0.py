class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for i,j,s in flights:
            graph[i].append((j,s))
        dist=[[float('inf')]*(k+2) for _ in range(n)]
        h=[]
        heapq.heappush(h,(0,src,0))
        dist[src][0]=0
        while h:
            cost,node,stop=heapq.heappop(h)
            if cost>dist[node][stop]:
                continue
            if stop==k+1:
                continue
            for nei,d in graph[node]:
                newcost=cost+d
                newstop=stop+1
                if newcost<dist[nei][newstop]:
                    dist[nei][newstop]=newcost
                    heapq.heappush(h,(newcost,nei,newstop))
        ans=min(dist[dst])
        return ans if ans!=float('inf') else -1
                


        