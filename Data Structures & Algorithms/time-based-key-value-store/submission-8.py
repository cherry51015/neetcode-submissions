class TimeMap:

    def __init__(self):
        self.h=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        lt=0
        rt=len(self.h[key])-1
        while lt<=rt:
            mid=(lt+rt+1)//2
            if self.h[key][mid][0]==timestamp:
                return self.h[key][mid][1]
            elif self.h[key][mid][0]<timestamp:
                lt=mid+1
            else:
                rt=mid-1
        return self.h[key][lt-1][1] if lt!=0 else ''

        
