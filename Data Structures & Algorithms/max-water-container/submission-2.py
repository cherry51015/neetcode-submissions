class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt=0
        rt=len(heights)-1
        area=0
        while lt<rt:
            area=max(area,(rt-lt)*min(heights[lt],heights[rt]))
            if heights[lt]<heights[rt]:
                lt+=1
            else:
                rt-=1
        return area


        
        
        