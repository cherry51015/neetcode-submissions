class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        ans=0
        for i in nums:
            c=0
            if i-1 not in nums:
                c+=1
            else:
                c=1
                while i-1 in h:
                    c+=1
                    i-=1
            ans=max(ans,c)
        return ans

                


        