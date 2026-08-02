class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt=0
        rt=len(nums)-1
        ans=float('inf')
        while lt<=rt:
            mid=(lt+rt)//2
            if nums[lt]>=nums[mid]<=nums[rt] or nums[lt]<=nums[mid]<=nums[rt]:
                ans=min(ans,nums[mid])
                rt=mid-1
            elif nums[lt]<=nums[mid]>=nums[rt] or nums[lt]>=nums[mid]>=nums[rt]:
                ans=min(ans,nums[lt])
                lt=mid+1
        return ans
        