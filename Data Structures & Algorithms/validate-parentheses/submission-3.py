class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        i=0
        while i<n :
            if stack and stack[-1]=='{' and s[i]=='}':
                stack.pop()
            elif stack and stack[-1]=='[' and s[i]==']':
                stack.pop()
            elif stack and stack[-1]=='(' and s[i]==')':
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
            
        return False if stack else True