class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prv = 0
        nxt = 1
        ans = 0
        for i in range(2, n + 1):
            ans = prv + nxt
            prv = nxt
            nxt = ans

        return ans