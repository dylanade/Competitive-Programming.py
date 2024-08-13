class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # row = [1] * n

        # for i in range(m - 1):
        #     new_row = [1] * n
        #     for j in range(n - 2, -1, -1):
        #         new_row = new_row[j + 1] + row[j]
        #     row = new_row

        # return row[0]

        # SOLN2
        #return math.comb(m+n-2, m-1)

        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]