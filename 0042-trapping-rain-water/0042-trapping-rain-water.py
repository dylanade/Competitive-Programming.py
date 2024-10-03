class Solution:
    def trap(self, heights: List[int]) -> int:
        # FORMULA: min(L, R) - h[i]
        
        answer = 0

        if not heights:
            return answer

        n = len(heights)
        l, r = 0, n-1
        maxL = heights[l]
        maxR = heights[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, heights[l])
                answer += maxL - heights[l]
            else:
                r -= 1
                maxR = max(maxR, heights[r])
                answer += maxR - heights[r]

        return answer