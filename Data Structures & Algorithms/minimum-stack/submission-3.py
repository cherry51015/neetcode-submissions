class MinStack:

    def __init__(self):
        self.stack=[]
        self.ministack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack:
            self.ministack.append(val)
        else:
            self.ministack.append(min(self.ministack[-1],val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ministack[-1]

        
