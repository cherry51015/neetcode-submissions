

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        res=[]
        for i,j in points:
            a=(i*i + j*j)
            heapq.heappush(h,(a,[i,j]))
        while k:
            v,[u,v]=heapq.heappop(h)
            res.append([u,v])
            k-=1
        return res 



        