class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt=0
        ans=0
        seen=set()
        for rt in range(len(s)):
            while s[rt] in seen:
                seen.remove(s[lt])
                lt+=1
                
            seen.add(s[rt])
            ans=max(ans,rt-lt+1)
        return ans


