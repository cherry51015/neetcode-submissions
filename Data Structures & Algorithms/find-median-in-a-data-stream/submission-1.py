class MedianFinder:

    def __init__(self):
        self.h=[]
        self.maxh=[]
        self.minh=[]
        

    def addNum(self, num: int) -> None:
        if not self.maxh or num<=(-self.maxh[0]):
            heapq.heappush(self.maxh,-num)
        else:
            heapq.heappush(self.minh,num)
        n=len(self.minh)
        x=len(self.maxh)
        if n-x>1:
            heapq.heappush(self.maxh,-heapq.heappop(self.minh))
        elif x-n>1:
            heapq.heappush(self.minh,-heapq.heappop(self.maxh))


    def findMedian(self) -> float:
        n=len(self.minh)
        x=len(self.maxh)
        if (n+x)%2==1:
            return self.minh[0] if n>x else -self.maxh[0]
        else:
            return (self.minh[0]-self.maxh[0])/2

        


        
        