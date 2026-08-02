class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-i for i in stones]
        heapq.heapify(h)
        while len(h)>1:
            x=-heapq.heappop(h)
            y=-heapq.heappop(h)
            if x!=y:
                heapq.heappush(h,-(x-y))
        if len(h)==1:
            return -heapq.heappop(h)
        else:
            return 0



        