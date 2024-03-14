class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * (max(heights) + 1)
        res = 0

        for i in range(len(heights)):
            count[heights[i]] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for i in range(len(heights)):
            if count[heights[i] - 1] <= i < count[heights[i]]:
                continue
            else:
                res += 1
                
        return res
                
        
        