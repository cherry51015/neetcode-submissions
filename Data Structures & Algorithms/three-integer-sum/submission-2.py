class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            lt=i+1
            rt=len(nums)-1
            s=nums[i]
            while lt<rt:
                temp=s+nums[lt]+nums[rt]
                if temp<0:
                    lt+=1
                elif temp>0:
                    rt-=1
                else:
                    ans.append([nums[i],nums[lt],nums[rt]])
                    lt+=1
                    rt-=1
        final=[]
        for x in ans:
            if x in final:
                continue
            final.append(x)
        return final
    
                



        