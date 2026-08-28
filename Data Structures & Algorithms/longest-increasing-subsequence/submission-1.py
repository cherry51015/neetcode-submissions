class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        best=0
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
            if dp[best]<dp[i]:
                best=i

        return dp[best]

        