class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        a=intervals[0][0]
        b=intervals[0][1]
        for i in intervals[1:]:
            if (a<=i[0] and a<=i[0]<=b) or (a>i[0] and i[0]<=a<=i[1]):
                a=min(a,i[0])
                b=max(b,i[1])
            else:
                res.append([a,b])
                a=i[0]
                b=i[1]
        res.append([a,b])
        return res
        