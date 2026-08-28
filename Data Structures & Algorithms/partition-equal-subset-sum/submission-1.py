class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if total%2!=0:
            return False
        need=total//2

        memo=[[None]*(need+1) for _ in range(n+1)]
        def dfs(i,rem):
            if rem==0:
                memo[i][rem]=True
                return True
            if i==n:
                memo[i][rem]=False
                return False
            if memo[i][rem] is not None:
                return memo[i][rem]
    
            memo[i][rem]=dfs(i+1,rem-nums[i]) or dfs(i+1,rem)
            return memo[i][rem]

        return dfs(0,need)

            
            

        