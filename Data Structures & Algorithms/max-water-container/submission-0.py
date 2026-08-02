class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        lt=0
        rt=len(heights)-1
        while lt<rt:
            d=rt-lt
            if heights[lt]<=heights[rt]:
                area=heights[lt]*d
                lt+=1
            else:
                area=heights[rt]*d
                rt-=1
            ans=max(ans,area)
        return ans


        