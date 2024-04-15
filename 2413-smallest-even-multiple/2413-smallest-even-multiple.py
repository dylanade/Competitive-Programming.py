class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if not n%2 else n*2        