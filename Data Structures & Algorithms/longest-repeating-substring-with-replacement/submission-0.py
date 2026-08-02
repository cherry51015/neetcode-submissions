class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lt=0
        h={}
        ans=0
        for rt in range(len(s)):
            h[s[rt]]=h.get(s[rt],0)+1
            maxfreq=max(h.values())
            while rt-lt+1-maxfreq>k:
                h[s[lt]]-=1
                if h[s[lt]]<=0:
                    del h[s[lt]]
                lt+=1
                maxfreq=max(h.values())
            ans=max(ans,rt-lt+1)
        return ans
        
        
        
        