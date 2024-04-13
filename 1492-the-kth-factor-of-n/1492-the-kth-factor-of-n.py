class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        count_factor = 0
        for i in range(1, n+1):
            if not n%i:
                count_factor += 1
                if count_factor == k:
                    return i
        
        return -1
        
        