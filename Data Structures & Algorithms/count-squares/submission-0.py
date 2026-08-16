class CountSquares:

    def __init__(self):
        self.h=defaultdict(lambda: defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        x,y=point
        self.h[x][y]+=1
        

    def count(self, point: List[int]) -> int:
        x,y=point
        ans=0
        for nx in list(self.h):
            if nx==x:
                continue
            d=abs(nx-x)
            for ny in [y+d,y-d]:
                ans+=(self.h[x][ny]*
                self.h[nx][ny]*
                self.h[nx][y])
        return ans
        
