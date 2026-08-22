class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevend=intervals[0][1]
        count=0
        for i,j in intervals[1:]:
            if i<prevend:
                prevend=min(prevend,j)
                count+=1
            else:
                prevend=j
        return count

        