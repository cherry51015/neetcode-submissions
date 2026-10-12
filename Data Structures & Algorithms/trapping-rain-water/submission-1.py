class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ltmax=[0]*n
        ltmax[0]=height[0]
        rtmax=[0]*n
        rtmax[-1]=height[-1]
        area=0
        for i in range(1,n):
            ltmax[i]=max(ltmax[i-1],height[i])
        for i in range(n-2,-1,-1):
            rtmax[i]=max(rtmax[i+1],height[i])
        total=0
        for i in range(n):
            total+=min(ltmax[i],rtmax[i])-height[i]
        return total


            

        