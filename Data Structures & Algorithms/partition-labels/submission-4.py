class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h={}
        for i,ch in enumerate(s):
            h[ch]=i
        
        ans=[]
        start=0
        end=0
        for i in range(len(s)):
            end=max(end,h[s[i]])
            if i==end:
                ans.append(end-start+1)
                start=i+1
        return ans
        