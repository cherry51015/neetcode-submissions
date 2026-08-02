class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            if matrix[i][c-1]>=target:
                lt=0
                rt=c-1
                while lt<=rt:
                    mid=(lt+rt)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        lt=mid+1
                    else:
                        rt=mid-1
        return False
                    

        