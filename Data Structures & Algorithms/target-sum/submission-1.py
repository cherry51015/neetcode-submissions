class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        def dfs(i,total):
            if i==n :
                if total==target:
                    memo[(i,total)]=1
                    return 1
                else:
                    memo[(i,total)]=0
                    return 0
            if (i,total)  in memo:
                return memo[(i,total)]
            
            memo[(i,total)]=dfs(i+1,total+nums[i])+dfs(i+1,total-nums[i])
            
            return memo[(i,total)]

        return dfs(0,0)