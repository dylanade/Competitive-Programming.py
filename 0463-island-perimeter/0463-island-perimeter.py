class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # O(n*m) # TC
        # O(n*m) # SC
        visit = set() # cells visited

        def dfs(i, j):
            if (i >= len(grid) or j >= len(grid[0]) 
                or i < 0 or j < 0 or grid[i][j] == 0):
                return 1

            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perimeter = dfs(i, j + 1) # move right
            perimeter += dfs(i, j - 1) # move left
            perimeter += dfs(i + 1, j) # move up
            perimeter += dfs(i - 1, j) # move down
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)