class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        if n<k:
            return [] 
        ans.append(max(nums[:k]))
        lt=0
        for rt in range(k,n):
            lt+=1
            ans.append(max(nums[lt:rt+1]))
        return ans
        