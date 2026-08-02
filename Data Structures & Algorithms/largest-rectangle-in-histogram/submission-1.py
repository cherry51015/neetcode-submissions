class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                rt=i
                idx=stack.pop()
                lt=stack[-1] if stack else -1
                ans[idx]=(rt-lt-1)*heights[idx]
            stack.append(i)
        while stack:
            rt=n
            j=stack.pop()
            lt=stack[-1] if stack else -1
            ans[j]=(rt-lt-1)*heights[j]
            

        return max(ans)