class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        m, n = len(isWater), len(isWater[0])

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((0, i, j))
                    
        answer = [[-1] * n for _ in range(m)]

        while queue:
            val, x, y = queue.popleft()

            if answer[x][y] != -1: 
                continue

            answer[x][y] = val

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and answer[nx][ny] == -1:
                    queue.append((val + 1, nx, ny))

        return answer