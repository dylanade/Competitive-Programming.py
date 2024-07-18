class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # multisource BFS
        # start at all the land pieces
        n = len(grid)
        
        queue = collections.deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        answer = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            answer = grid[r][c]
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (min(new_r, new_c) >= 0 and 
                    max(new_r, new_c) < n and
                    grid[new_r][new_c] == 0):
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = grid[r][c] + 1

        return answer-1 if answer > 1 else -1 
