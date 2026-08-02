class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        lt=0
        rt=n1-1
        h1={}
        h2={}
        if n1>n2:
            return False
        for j in s1:
            h1[j]=h1.get(j,0)+1
        for i in s2[lt:n1]:
            h2[i]=h2.get(i,0)+1
        if h2==h1:
            return True
        lt=0
        for rt in range(n1,n2):
            h2[s2[lt]]-=1
            if h2[s2[lt]]<=0:
                del h2[s2[lt]]
            lt+=1
            h2[s2[rt]]=h2.get(s2[rt],0)+1
            if h2==h1:
                return True
        return False
