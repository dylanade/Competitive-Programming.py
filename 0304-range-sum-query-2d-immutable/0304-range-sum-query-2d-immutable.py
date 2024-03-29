class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.pre_mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    self.pre_mat[i][j] = matrix[i][j]
                elif i==0:
                    self.pre_mat[i][j] = matrix[i][j] + self.pre_mat[i][j-1]
                elif j==0:
                    self.pre_mat[i][j] = matrix[i][j] + self.pre_mat[i-1][j]
                else:
                    self.pre_mat[i][j] = self.pre_mat[i-1][j] + self.pre_mat[i][j-1] - self.pre_mat[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pre_mat[row2][col2]

        if row1 > 0:
            ans-=self.pre_mat[row1-1][col2]
        if col1>0:
            ans-=self.pre_mat[row2][col1-1]
        if row1>0 and col1>0:
            ans += self.pre_mat[row1-1][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)