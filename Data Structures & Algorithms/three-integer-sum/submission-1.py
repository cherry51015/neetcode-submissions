class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lt=i+1
            rt=n-1
            while lt<rt:
                s=nums[i]+nums[lt]+nums[rt]
                if s==0:
                    ans.append([nums[i],nums[lt],nums[rt]])
                    lt+=1
                    rt-=1
                    while lt<rt and nums[lt]==nums[lt-1]:
                        lt+=1
                    while lt<rt and nums[rt]==nums[rt+1]:
                        rt-=1

                elif s<0  :
                    lt+=1
                else:
                    rt-=1
        return ans
                
                    