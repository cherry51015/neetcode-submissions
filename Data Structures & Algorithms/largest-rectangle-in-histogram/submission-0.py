class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ans=0
        for i in range(n):
            lt=i-1
            rt=i
            curr=0
            while lt>=0:
                if heights[lt]>=heights[i]:
                    curr+=heights[i]
                    lt-=1
                else:
                    break
            while rt<n:
                if heights[rt]>=heights[i]:
                    curr+=heights[i]
                    rt+=1
                else:
                    break
            ans=max(ans,curr)
        return ans
    

