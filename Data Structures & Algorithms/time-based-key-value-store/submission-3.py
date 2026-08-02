class TimeMap:

    def __init__(self):
        self.h=defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        lt=0
        rt=len(self.h[key])-1
        ans=""
        while lt<=rt:
            mid=(lt+rt)//2
            i,j=self.h[key][mid]
            if i<=timestamp:
                ans=j
                lt=mid+1
            else:
                rt=mid-1
        return ans 
    
        

        
