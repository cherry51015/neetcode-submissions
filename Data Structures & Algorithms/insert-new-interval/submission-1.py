class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a=newInterval[0]
        b=newInterval[1]
        res=[]
        for i in intervals:
            if i[1]<a:
                res.append(i)
            elif  b<i[0]:
                res.append([a,b])
                res.append(i)
                res.extend(intervals[intervals.index(i)+1:])
                return res
                
            else:
                a=min(a,i[0])
                b=max(b,i[1])
        res.append([a,b])
        return res

