class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        def backtracking(start,rem):
            if rem==0:
                ans.append(path[:])
                return
            if rem<0:
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtracking(i,rem-nums[i])
                path.pop()
        backtracking(0,target)
        return ans



        