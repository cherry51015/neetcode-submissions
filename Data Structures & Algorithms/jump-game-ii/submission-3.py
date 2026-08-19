class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        count=[0]+[n]*(n-1)
        for i in range(n-1):
            x=i+nums[i]
            if x>=n-1:
                x=n-1
            for j in range(i+1,x+1):
                count[j]=min(count[j],count[i]+1)
        return count[n-1]



        