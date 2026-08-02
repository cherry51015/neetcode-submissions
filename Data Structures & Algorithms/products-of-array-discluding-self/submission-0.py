class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ps=[1]*n
        ss=[1]*n
        for lt in range(1,n):
            ps[lt]=ps[lt-1]*nums[lt-1]
        for rt in range(n-2,-1,-1):
            ss[rt]=ss[rt+1]*nums[rt+1]
        ans=[]
        for i in range(n):
            ans.append(ps[i]*ss[i])
        return ans


