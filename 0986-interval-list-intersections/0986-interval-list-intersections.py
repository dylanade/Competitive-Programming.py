class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(a) and j < len(b):
            start = max(a[i][0], b[j][0])
            end = min(a[i][1], b[j][1])

            if start <= end:
                result.append([start, end])
            
            if a[i][1] >= b[j][1]:
                j += 1
            else:
                i += 1

        return result