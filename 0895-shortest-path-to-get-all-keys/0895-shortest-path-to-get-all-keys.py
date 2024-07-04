class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        start = []
        total_keys = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = [i, j]
                if grid[i][j].islower():
                    total_keys += 1

        sx, sy = start[0], start[1]

        queue = collections.deque()
        queue.append((sx, sy, tuple(), 0))

        visited = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            cx, cy, collected_keys, steps = queue.popleft()

            if total_keys == len(set(collected_keys)):
                return steps

            if (cx, cy, collected_keys) not in visited:
                visited.add((cx, cy, collected_keys))

                for dx, dy in directions:
                    x = cx + dx
                    y = cy + dy

                    key_set = set(collected_keys)

                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] != "#":
                            cell = grid[x][y]

                            key = cell.lower()
                            is_key = cell.islower()
                            is_lock = cell.isupper()

                            if is_key and cell != ".":
                                key_set.add(key)
                            
                            if is_lock and key not in key_set:
                                continue

                            queue.append((x, y, tuple(key_set), steps + 1))

        return -1