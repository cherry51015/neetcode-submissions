class Solution:
    def trap(self, height: List[int]) -> int:
        ltmax=0
        rtmax=0
        lt=0
        rt=len(height)-1
        total=0
        while lt<rt:
            ltmax=max(ltmax,height[lt])
            rtmax=max(rtmax,height[rt])
            if height[lt]<height[rt]:
                total+=min(ltmax,rtmax)-height[lt]
                lt+=1
            else:
                total+=min(ltmax,rtmax)-height[rt]
                rt-=1
        return total

                

        
        