class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        row, col = 0, 0
        direction = True
        result = []

        for i in range(n*m):
            result.append(mat[row][col])

            if direction:
                if row == 0 and col != m-1:
                    direction = False
                    col += 1 
                elif col == m-1:
                    direction = False
                    row += 1 
                else:
                    row -= 1 
                    col += 1 
            else:
                if col == 0 and row != n-1:
                    direction = True
                    row += 1 
                elif row == n-1:
                    direction = True
                    col += 1 
                else:
                    col -= 1
                    row += 1 

        return result

        