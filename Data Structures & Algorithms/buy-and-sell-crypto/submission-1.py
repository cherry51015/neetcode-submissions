class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minprice=float('inf')
        profit=0
        for i in prices:
            if i>minprice:
                profit=max(profit,i-minprice)
            minprice=min(minprice,i)
        return profit