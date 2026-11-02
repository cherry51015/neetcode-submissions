class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        lt=0
        rt=c-1
        def bs(row):
            lt=0
            rt=c-1
            while lt<=rt:
                mid=(lt+rt)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]<target:
                    lt=mid+1
                else:
                    rt=mid-1
            return False
                

        x=0
        y=r-1
        while x<=y:
            mid=(x+y)//2
            if matrix[mid][c-1]==target:
                return True
            elif matrix[mid][c-1]>target:
                y=mid-1
            else:
                x=mid+1
        if x<r and matrix[x][0]<=target:
            return bs(x)
        return False


        
        