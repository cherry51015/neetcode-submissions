class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack1.append(i)
            elif s[i]=='*':
                stack2.append(i)
            else:
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
        if stack1:
            if not stack2:
                return False
            else:
                while stack1 and stack2:
                    x=stack2.pop()
                    if x>stack1[-1]:
                        stack1.pop()
                if stack1:
                    return False
        if not stack1:
            return True


        

        