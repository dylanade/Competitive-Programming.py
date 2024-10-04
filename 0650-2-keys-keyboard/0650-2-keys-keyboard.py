class Solution:
    def minSteps(self, n: int) -> int:
        def dp(n, i):
            if n == 1:
                return i

            start = 2
            while start < n:
                if n%start == 0:
                    i += start
                    break
                start += 1
            else:
                i += n

            n = n // start
            return dp(n, i)

        return dp(n, 0)