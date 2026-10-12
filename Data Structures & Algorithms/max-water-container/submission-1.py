class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt=0
        rt=len(heights)-1
        area=0
        while lt<rt:
            area=max(area,min(heights[lt],heights[rt])*(rt-lt))
            if heights[lt]<=heights[rt]:
                lt+=1
            else:
                rt-=1
            
        return area

        