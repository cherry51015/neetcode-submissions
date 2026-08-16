class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()
        while n!=1:
            total=0
            while n!=0:
               dig=n%10
               n=n//10
               total+=dig**2
            if total in v:
                return False
            v.add(total)
            n=total
        return True
        