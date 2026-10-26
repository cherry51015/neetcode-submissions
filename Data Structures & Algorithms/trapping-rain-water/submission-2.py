class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ltmax=height[0]
        rtmax=height[n-1]
        t=0
        lt=0
        rt=n-1
        while lt<rt:
            if height[lt]<=height[rt]:
                ltmax=max(ltmax,height[lt])
                t+=ltmax-height[lt]
                lt+=1
            else:
                rtmax=max(rtmax,height[rt])
                t+=rtmax-height[rt]
                rt-=1
        return t





        