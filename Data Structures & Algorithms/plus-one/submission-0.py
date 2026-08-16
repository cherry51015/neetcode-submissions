class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        dig=int(s)+1

        res=[]
        while dig!=0:
            res.append(dig%10)
            dig=dig//10
        
        return res[::-1]
        

        