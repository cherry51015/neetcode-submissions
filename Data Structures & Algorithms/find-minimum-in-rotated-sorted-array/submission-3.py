class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt=0
        rt=len(nums)-1
        ans=float('inf')
        
        if nums[lt]<=nums[rt]:
            return nums[lt]
        
        while lt<=rt:
            mid=(lt+rt)//2
            if nums[lt]<=nums[mid]:
                ans=min(ans,nums[lt])
                lt=mid+1
            else:
                ans=min(ans,nums[mid])
                rt=mid-1
        return ans
            