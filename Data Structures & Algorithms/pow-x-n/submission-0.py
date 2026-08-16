class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            a=recursion(x*x,n//2)
            return a if n%2==0 else a*x
        res=recursion(x,abs(n))
        return res if n>=0 else 1/res

        
            