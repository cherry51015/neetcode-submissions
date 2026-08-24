class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        def robber(arr):
            amount=0
            n=len(arr)
            dp=[0]*(n+2)
            for i in range(n-1,-1,-1):
                dp[i]=max(arr[i]+dp[i+2],dp[i+1])
            return dp[0]
        if l==1:
            return nums[0]
        return max(robber(nums[0:l-1]),robber(nums[1:l]))


    