class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h={}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=i
            else:
                h[s[i]]=max(h[s[i]],i)
        
        ans=[]
        v=set()
        start=0
        end=0
        for i in range(len(s)):
            if s[i] in v:
                continue
            if start<=i<=end:
                v.add(s[i])
                end=max(end,h[s[i]])
            else:
                ans.append(end-start+1)
                start=i
                end=h[s[i]]
                v.add(s[i])
        ans.append(end-start+1)
        return ans
        