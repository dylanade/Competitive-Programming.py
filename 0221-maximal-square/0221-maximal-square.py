class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # maybe an extension of this problem is to flip a digit to find a maximal square
        # BRUTE FORCE: O(m*n)^2

        # Dynamic programming: bottom up O(m*n)
        # Recursive: top down

        rows, cols = len(matrix), len(matrix[0])
        cache = {} # map each (r, c) - maxLength of the square

        def helper(r, c):
            # base cases
            if r >= rows or c >= cols:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c) # go down
                right = helper(r, c + 1) # go right
                diag = helper(r + 1, c + 1) # go diagnally (down and right)
                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2
        