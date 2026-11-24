class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                if i=='+':
                    num=a+b
                elif i=='-':
                    num=b-a
                elif i=='*':
                    num=a*b
                else:
                    num=int(b/a) if b!=0 else 0
                stack.append(num)
        return stack[0]

        