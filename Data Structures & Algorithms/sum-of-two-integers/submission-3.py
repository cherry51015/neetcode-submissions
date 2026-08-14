class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK=0xFFFFFFFF
        MAX=0x7FFFFFFF
        while b!=0:
            add=(a^b)&MASK
            carry=(a&b)<<1
            a=add
            b=carry
        if a>MAX:
            a=~(a^MASK)
        return a
        