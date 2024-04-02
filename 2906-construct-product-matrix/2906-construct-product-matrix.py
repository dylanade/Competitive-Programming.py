class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
##       Test cases passed (TIME LIMIT EXCEEDED): 1564/1566
#         m, n = len(grid), len(grid[0])
#         product = 1
#         for i in range(m):
#             for j in range(n):
#                 product *= grid[i][j]
#         output = [[1]*n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 output[i][j] = int(product // grid[i][j]) % 12345
#         return output

        m, n = len(grid), len(grid[0])
        mod = 12345
    
        right = [1]
        for i in range(m):
            for j in range(n):
                right.append((right[-1] * grid[i][j]) % mod)
                
        left = [1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                left.append((left[-1] * grid[i][j]) % mod)
        left.reverse()
                
        output = [[1]*n for _ in range(m)]
        k = 0
        for i in range(m):
            for j in range(n):
                output[i][j] = (right[k] * left[k+1]) % mod
                k += 1
                
        return output
        
        
    
        
        