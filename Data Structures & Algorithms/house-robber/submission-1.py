class Solution:
    def rob(self, nums: List[int]) -> int:
        amount=0
        n=len(nums)
        memo=[None]*(n+2)
        def dfs(i):
            nonlocal amount
            if i>=n:
                memo[i]=0
                return 0
            if memo[i] is not None:
                return memo[i]
            take=nums[i]+dfs(i+2)
            skip=dfs(i+1)
            memo[i]=max(take,skip)
            return memo[i]
        
        return dfs(0)
            

        