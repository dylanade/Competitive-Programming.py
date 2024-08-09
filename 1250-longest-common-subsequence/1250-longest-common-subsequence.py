class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        M, N = len(X), len(Y)

        # TABLE DP - MEMOISATION
        dp = [[-1] * (N + 1) for _ in range(M + 1)]

        def LCS(m, n):
            # BASE CASES
            if m == M or n == N:
                return 0

            # return prev calculated answer
            if dp[m][n] != -1:
                return dp[m][n]

            # RECURRENCE RELATION

            # if a char in str1 == char in str2
            if X[m] == Y[n]:
                dp[m][n] = 1 + LCS(m + 1, n + 1)

            # otherwise, 
            else:
                dp[m][n] = max(LCS(m + 1, n), LCS(m, n + 1))

            return dp[m][n]

        return LCS(0, 0)