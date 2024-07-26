class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # flip horizontal
        for i in range(n):
            for j in range(0, n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = tmp
        # flip secondary diagonal
        for i in range(n):
            for j in range(n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = tmp
        
        