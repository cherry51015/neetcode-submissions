class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used=[False]*len(nums)
        ans=[]
        path=[]
        def dfs():
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                dfs()
                used[i]=False
                path.pop()
        dfs()
        return ans

        