class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for i,j,t in times:
            graph[i].append((j,t))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        h=[]
        heapq.heappush(h,(0,k))
        while h:
            cost,node=heapq.heappop(h)
            if dist[node]<cost:
                continue
            for nei,wt in graph[node]:
                newcost=wt+cost
                if newcost<dist[nei]:
                    dist[nei]=newcost
                    heapq.heappush(h,(newcost,nei))
        ans=max(dist[1:])
        return ans if ans!=float('inf') else -1
        