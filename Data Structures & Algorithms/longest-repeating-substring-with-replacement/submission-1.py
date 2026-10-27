class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h=defaultdict(int)
        lt=0
        maxi=0
        ans=0
        for rt in range(len(s)):
            h[s[rt]]+=1
            currmax=h[s[rt]]
            maxi=max(maxi,currmax)
            need=rt-lt+1-maxi
            while need>k:
                h[s[lt]]-=1
                lt+=1
                need-=1
            ans=max(ans, rt-lt+1)
        return ans



            
            


        