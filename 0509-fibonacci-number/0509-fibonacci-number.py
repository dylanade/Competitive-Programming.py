class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        elif n < 3:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2) 