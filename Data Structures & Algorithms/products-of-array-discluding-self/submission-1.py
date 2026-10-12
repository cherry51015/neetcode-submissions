class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        count=0
        for i in nums:
            if i!=0:
               p*=i
            else:
                count+=1
        ans=[]
        for j in nums:
            if count>1:
                ans.append(0)
            elif count==1:
                if j==0:
                    ans.append(p)
                else:
                    ans.append(0)
            else:
                ans.append(p//j)
        return ans



            


        