class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in nums:
            h[i]=h.get(i,0)+1
        h=dict(sorted(h.items(),key=lambda x:x[1],reverse=True))
        ans=[]
        for i,j in h.items():
            if k==0:
                break
            ans.append(i)
            k-=1
        return ans
    
    
        
        