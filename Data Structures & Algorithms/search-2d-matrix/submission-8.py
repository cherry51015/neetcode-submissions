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
        while x<r:
            if matrix[x][c-1]>=target:
                return bs(x)
            x+=1
        return False


        
        