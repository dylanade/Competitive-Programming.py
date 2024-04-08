class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        primary = 0
        secondary = 0
        for i in range(m):
            primary += mat[i][i]
            if i != n-i-1:
                secondary += mat[i][n-i-1]
            
        return primary + secondary
        