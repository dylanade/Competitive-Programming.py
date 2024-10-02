class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        SROWS, SCOLS = 3 * ROWS, 3 * COLS # scale grid by 3 works best
        sgrid = [[0] * SROWS for _ in range(SCOLS)]

        for r in range(ROWS):
            for c in range(COLS):
                sr, sc = r * 3, c * 3
                if grid[r][c] == "/":
                    sgrid[sr][sc+2] = 1
                    sgrid[sr+1][sc+1] = 1
                    sgrid[sr+2][sc] = 1
                elif grid[r][c] == "\\":
                    sgrid[sr][sc] = 1
                    sgrid[sr+1][sc+1] = 1
                    sgrid[sr+2][sc+2] = 1

        def dfs(r, c):
            if ((r < 0 or c < 0) or (r == SROWS or c == SCOLS) or 
                (sgrid[r][c] == 1)):
                return 

            sgrid[r][c] = 1
            neighbours = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
            for nr, nc in neighbours:
                dfs(nr, nc)

        answer = 0
        for r in range(SROWS):
            for c in range(SCOLS):
                if sgrid[r][c] == 0:
                    dfs(r, c)
                    answer += 1

        return answer
