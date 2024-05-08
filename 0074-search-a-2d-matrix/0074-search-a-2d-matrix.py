class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if target == matrix[i][m-1]:
                return True
            elif target < matrix[i][m-1]:
                for j in range(m-1):
                    if target == matrix[i][j]:
                        return True 
                else:
                    return False
            else:
                continue