class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt=0
        v=set()
        ans=0
        for rt in range(len(s)):
            while s[rt] in v:
                v.discard(s[lt])
                lt+=1
            v.add(s[rt])
            ans=max(ans,rt-lt+1)
        return ans
                

        