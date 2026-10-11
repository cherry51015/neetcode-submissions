import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lt=0
        rt=len(s)-1
        while lt<rt:
            if re.search(r"[^a-zA-Z0-9]",s[lt]):
                lt+=1
                continue
            if re.search(r"[^a-zA-Z0-9]",s[rt]):
                rt-=1
                continue
            if s[lt].lower()==s[rt].lower():
                lt+=1
                rt-=1
            else:
                return False
        return True
        