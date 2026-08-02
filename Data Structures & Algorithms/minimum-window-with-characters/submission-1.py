class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        if len(s)<len(t):
            return ""
        tar={}
        h={}
        for i in t:
            tar[i]=tar.get(i,0)+1
        lt=0
        minlen=float('inf')
        have=0
        need=len(tar)
        ans=""
        for rt in range(len(s)):
            h[s[rt]]=h.get(s[rt],0)+1
            if s[rt] in tar and h[s[rt]]==tar[s[rt]]:
                have+=1
            while need==have:
                length=rt-lt+1
                if minlen>length:
                    minlen=length
                    ans=s[lt:rt+1]
                h[s[lt]]-=1
                if s[lt] in tar and h[s[lt]]<tar[s[lt]]:
                    have-=1
                if h[s[lt]]<=0:
                    del h[s[lt]]
                lt+=1
        return ans
        
            