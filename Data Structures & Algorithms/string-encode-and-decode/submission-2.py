class Solution:
    def __init__(self):
        self.h=[]

    def encode(self, strs: List[str]) -> str:
        s=''
        for word in strs:
            self.h.append(len(word))
            s+=word
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        n=len(self.h)
        ans=[]
        x=0
        while i<n:
            ans.append(s[x:x+self.h[i]])
            x+=self.h[i]
            i+=1
        return ans
