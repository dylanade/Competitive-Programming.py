class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0
        for i in range(2, n + 1):
            result = (result + k) % i
            
        return result + 1