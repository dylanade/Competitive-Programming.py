class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        # TABLE

        m, n = len(X), len(Y)

        # TABLE DP - MEMOIZATION
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def LCS(m, n):
            # base cases
            if m == 0 or n == 0:
                return 0

            # return prev calculated answer
            if dp[m][n] != -1:
                return dp[m][n]

            # RECURRENCE RELATION

            # if a char in X == char in Y
            if X[m - 1] == Y[n - 1]:
                dp[m][n] = 1 + LCS(m - 1, n - 1)

            # otherwise
            else:
                dp[m][n] = max(LCS(m - 1, n), LCS(m, n - 1))

            return dp[m][n]

        return LCS(m, n)


            