class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        n=len(intervals)
        s_queries=sorted(queries)
        h=[]
        res={}
        i=0
        for q in s_queries:
            while i<n and q>=intervals[i][0]:
               lt=intervals[i][0]
               rt=intervals[i][1]
               l=rt-lt+1
               heapq.heappush(h,(l,rt))
               i+=1
            while h and  h[0][1]<q:
                heapq.heappop(h)
            if h:
                res[q]=h[0][0]
            else:
                res[q]=-1
        return list(res[x] for x in queries)

        