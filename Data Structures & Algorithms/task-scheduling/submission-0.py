class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h={}
        for i in tasks:
            h[i]=h.get(i,0)+1
        heap=[]
        for i,j in h.items():
            heapq.heappush(heap,-j)
        t=0
        q=deque([])
        while heap or q:
            t+=1
            if heap:
                freq=heapq.heappop(heap)
                freq+=1
                if freq!=0:
                    q.append((t+n,freq))
            if q:
                if q[0][0]==t:
                    _,freq=q.popleft()
                    heapq.heappush(heap,freq)
        return t




        
            