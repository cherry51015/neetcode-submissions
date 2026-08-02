from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        lt=0
        ans=[]
        q=deque()
        for rt in range(n):
            while q and q[-1]<nums[rt]:
                q.pop()
            q.append(nums[rt])
            if rt-lt+1==k:
                ans.append(q[0])
                if nums[lt]==q[0]:
                    q.popleft()
                lt+=1
        return ans


        