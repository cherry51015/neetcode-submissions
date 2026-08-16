class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    h.append([i,j])
        for i,j in h:
            for c in range(len(matrix[0])):
                matrix[i][c]=0
            for r in range(len(matrix)):
                matrix[r][j]=0
        
        
        
                   
                
        
        