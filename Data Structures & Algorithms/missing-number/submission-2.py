class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums+=[0]
        xor=0
        for i in range(n+1):
            xor^=i^nums[i]
        return xor

        