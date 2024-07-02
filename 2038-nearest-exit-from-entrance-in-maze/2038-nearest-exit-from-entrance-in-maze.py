class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        answer = 0
        er, ec = entrance

        queue = collections.deque()
        queue.append((er, ec, 0)) # start, steps
        
        m, n = len(maze), len(maze[0])
        visited = []
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(False)
            visited.append(row)
        visited[er][ec] = True

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            cr, cc, steps = queue.popleft()

            if (cr in {0, m - 1} or cc in {0, n - 1}) and [cr, cc] != entrance:
                return steps

            # Iterate through all the directions
            for r, c in directions:
                r, c = r + cr, c + cc
                # Make sure each neighbour cell is within the boundary and 
                # not yet visited and it is an empty cell
                if 0 <= r < m and 0 <= c < n and \
                not visited[r][c] and maze[r][c] == '.':
                    queue.append((r, c, steps + 1))
                    visited[r][c] = True

        return -1
            