class Solution:
    def reverse(self, x: int) -> int:
        MAX=2**31
        MIN=-(MAX)
        a=abs(x)
        res=0
        while a!=0:
            digit=a%10
            a=a//10
            res=res*10+digit
        if x<0:
            if -res<MIN:
                return 0
            return -res
        if x>=0:
            if res>MAX:
                return 0
            return res
        
        