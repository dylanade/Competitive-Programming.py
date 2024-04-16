class Solution:
    def maxScore(self, points: List[int], k: int) -> int:
        n = len(points)
        l = 0
        r = n-k 
        max_sum = window_sum = sum(points[n-k:])
        while r < n:
            window_sum -= points[r]
            window_sum += points[l]
            max_sum = max(max_sum, window_sum)
            l += 1
            r += 1
        return max_sum
        