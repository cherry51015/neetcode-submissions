class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h1={}
        for i in t:
            h1[i]=h1.get(i,0)+1
        lt=0
        have=0
        need=len(h1)
        h2={}
        mini=float('inf')
        start=0
        end=0
        
        for rt, ch in enumerate(s):
            h2[ch]=h2.get(ch,0)+1
            if ch in h1 and h1[ch]==h2[ch]:
                have+=1
            while have==need:
                l=rt-lt+1
                if mini>l:
                    mini=l
                    start=lt
                    end=rt
                h2[s[lt]]-=1
                if s[lt] in h1 and h2[s[lt]]<h1[s[lt]]:
                    have-=1
                lt+=1
        return s[start:end+1] if mini!=float('inf') else ''




        