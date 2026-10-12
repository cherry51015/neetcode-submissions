class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        length=0
        for i in nums:
            if i-1 not in s:
                length=1
                while i+length in s:
                    length+=1
            ans=max(ans,length)
        return ans
            






        
        