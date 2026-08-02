class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h1={}
        for i in range(len(s)):
            h1[s[i]]=h1.get(s[i],0)+1
        h2={}
        for j in range(len(t)):
            h2[t[j]]=h2.get(t[j],0)+1
        
       
        for i in s:
            if i not in h2 or h1[i]!=h2[i]:
                return False
        return True
