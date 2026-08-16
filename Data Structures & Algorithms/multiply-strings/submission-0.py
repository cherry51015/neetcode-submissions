class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        n=len(num1)
        m=len(num2)
        res=[0]*(n+m)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                p=int(num1[i])*int(num2[j])
                x1=i+j
                x2=i+j+1
                dig=p+res[x2]
                res[x1]+=dig//10
                res[x2]=dig%10
        while res[0]==0:
            res.pop(0)
        return ''.join(map(str,res))

        