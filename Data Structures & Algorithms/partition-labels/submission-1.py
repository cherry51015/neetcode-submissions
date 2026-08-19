class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h={}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=[i,i]
            else:
                h[s[i]]=[min(h[s[i]][0],i),max(h[s[i]][1],i)]
        
        ans=[]
        v=set()
        start=0
        end=0
        for i in range(len(s)):
            if s[i] in v:
                continue
            if start<=i<=end:
                v.add(s[i])
                end=max(end,h[s[i]][1])
            else:
                ans.append(end-start+1)
                start=i
                end=h[s[i]][1]
                v.add(s[i])
        ans.append(end-start+1)
        return ans
        