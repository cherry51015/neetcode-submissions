class Solution:
    def reverseBits(self, n: int) -> int:
        a=31
        total=0
        while a!=-1:
            bit=n&1
            total+=(bit*(2**a))
            a-=1
            n=n>>1
        return total



        