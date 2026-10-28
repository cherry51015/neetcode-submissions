class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lt=0
        ans=[]
        q=deque()
        for rt in range(len(nums)):
            while q and  q[0]<lt:
                q.popleft()
            while q and nums[q[-1]]<nums[rt]:
                q.pop()
            q.append(rt)
            if rt-lt+1==k:
                ans.append(nums[q[0]])
                lt+=1
        return ans
