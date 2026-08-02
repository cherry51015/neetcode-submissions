class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-i for i in stones]
        heapq.heapify(h)
        while len(h)>1:
            x=-heapq.heappop(h)
            y=-heapq.heappop(h)
            if abs(x-y)!=0:
                heapq.heappush(h,-abs(x-y))
        if len(h)==1:
            return -heapq.heappop(h)
        else:
            return 0



        