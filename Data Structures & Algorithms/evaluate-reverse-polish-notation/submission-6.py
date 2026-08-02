class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q=[]
        for i in range(len(tokens)):
            if tokens[i] not in {"*","-","+","/"}:
                q.append(int(tokens[i]))
            else:
                if len(q)>=2:
                    a=q.pop()
                    b=q.pop()
                    if tokens[i]=="+":
                       q.append(a+b)
                    elif tokens[i]=="-":
                       q.append(b-a)
                    elif tokens[i]=="*":
                       q.append(a*b)
                    else:
                        if a==0 or b==0:
                            q.append(0)
                        else:
                            q.append(int(b/a))
        return q[0]



        