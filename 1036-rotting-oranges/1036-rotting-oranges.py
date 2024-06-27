class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count_fresh = 0
        queue = collections.deque()
        visited = grid

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    count_fresh += 1
                    
        if count_fresh == 0:
            return 0

        if not queue:
            return -1

        minutes = -1

        # up - down - left - right
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            size = len(queue)

            while size > 0:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    i = r + dr
                    j = c + dc

                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        queue.append((i, j))
                        visited[i][j] = 2
                        count_fresh -= 1

                size -= 1

            minutes += 1

        return minutes if count_fresh == 0 else -1