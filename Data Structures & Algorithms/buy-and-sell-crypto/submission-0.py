class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[i]<=prices[j]:
                    ans=max(ans,prices[j]-prices[i])
        return ans
        