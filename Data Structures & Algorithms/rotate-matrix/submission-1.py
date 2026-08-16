class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for row in range(n//2):
            matrix[row], matrix[n-1-row] = matrix[n-1-row], matrix[row]
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        