class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt=0
        rt=len(nums)-1
        while lt<rt:
            mid=((lt+rt+1)//2)
            if nums[mid]>nums[lt]:
                lt=mid
            else:
                rt=mid-1
        return nums[lt+1] if lt+1<len(nums) else nums[0]