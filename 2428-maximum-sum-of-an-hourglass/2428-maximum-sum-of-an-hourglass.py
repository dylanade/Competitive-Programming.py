class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        score = float('-inf')
        
        for i in range(n-2):
            for j in range(m-2):
                hourglass = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                score = max(score, hourglass)
        return score
        
                    
                