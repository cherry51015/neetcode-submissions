class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        candidates.sort()
        def backtracking(start,rem):
            if rem==0:
                ans.append(path[:])
                return
            if rem<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(i+1,rem-candidates[i])
                path.pop()
        backtracking(0,target)
        return ans
        