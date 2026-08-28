class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if total%2!=0:
            return False
        need=total//2

        def dfs(i,need):
            if need==0:
                return True
            if i==n:
                return False
            return dfs(i+1,need-nums[i]) or dfs(i+1,need)
        return dfs(0,need)
            
            

        