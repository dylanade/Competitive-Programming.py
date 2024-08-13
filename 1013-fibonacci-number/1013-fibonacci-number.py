class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prv = 0
        nxt = 1
        
        for i in range(2, n + 1):
            nxt = prv + nxt
            prv = nxt - prv
 

        return nxt