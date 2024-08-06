class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        columns = set()
        rows = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows.add(r)
                    columns.add(c)

        for c in range(COLS):
            if c in columns:
                for r in range(ROWS):
                    matrix[r][c] = 0
                    if r in rows:
                        matrix[r] = [0] * COLS