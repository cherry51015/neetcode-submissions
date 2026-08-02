class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        h=[]
        for x,y in zip(position,speed):
            h.append((x,y))
        h.sort(reverse=True)
        stack=[]
        count=0
        for i,j in h:
            t=(target-i)/j
            if not stack or stack[-1]<t:
                stack.append(t)
        return len(stack)


                    





        