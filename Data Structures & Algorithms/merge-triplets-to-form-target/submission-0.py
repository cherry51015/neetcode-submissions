class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        gx=False
        gy=False
        gz=False
        x,y,z=target
        for a,b,c in triplets:
            if a>x or b>y or c>z:
                continue
            if a==x:
                gx=True
            if b==y:
                gy=True
            if c==z:
                gz=True
        return gx and gy and gz



        