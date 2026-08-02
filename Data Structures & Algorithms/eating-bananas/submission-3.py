class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        def canfinish(k):
            hours=0
            for p in piles:
                hours+=((p+k-1)//k)
            return hours<=h
        
        lt=1
        rt=max(piles)
        while lt<rt:
            mid=(lt+rt)//2
            if canfinish(mid):
                rt=mid
            else:
                lt=mid+1
        return lt

        