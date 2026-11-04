class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lt=1
        rt=sum(piles)
        def valid(k):
            hrs=0
            for i in piles:
                hrs+=((i+k-1)//k)
            return hrs<=h 
        while lt<rt:
            mid=(lt+rt)//2
            if valid(mid):
                rt=mid
            else:
                lt=mid+1
        return lt
            
            

        