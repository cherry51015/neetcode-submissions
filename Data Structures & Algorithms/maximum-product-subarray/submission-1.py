class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currpro=nums[0]
        maxpro=nums[0]
        minpro=nums[0]
        ans=nums[0]
        for i in nums[1:]:
            oldminpro=minpro
            oldmaxpro=maxpro
            minpro=min(i,oldminpro*i,oldmaxpro*i)
            maxpro=max(i,oldminpro*i,oldmaxpro*i)
            ans=max(ans,maxpro)
        return ans
            
        