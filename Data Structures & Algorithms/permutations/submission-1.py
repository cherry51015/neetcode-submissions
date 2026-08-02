class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        used=[False]*len(nums)
        def dfs():
            if len(path)==len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                path.append(nums[i])
                dfs()
                used[i]=False
                path.pop()
        dfs()
        return ans
            

        