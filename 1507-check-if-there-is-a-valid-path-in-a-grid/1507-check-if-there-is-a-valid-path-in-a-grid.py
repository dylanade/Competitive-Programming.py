class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 1 can connect to:
            # 1, 3, 5 on right-cell 
            # 1, 4, 6 on left-cell 

        # 2 can connect to:
            # 2, 3, 4 on top-cell 
            # 2, 5, 6 on bottom-cell 

        # 3 can connect to:
            # 1, 4, 6 on left-cell 
            # 2, 5, 6 on bottom-cell 

        # 4 can connect to:
            # 1, 3, 5 on right-cell 
            # 2, 5, 6 on bottom-cell 

        # 5 can connect to:
            # 1, 4, 6 on left-cell 
            # 2, 3, 4 on top-cell 

        # 6 can connect to:
            # 2, 3, 4 on top-cell
            # 1, 3, 5 on right-cell

        ## summarised pattern 
        # left can connect:     1, 4, 6
        # right can connect:    1, 3, 5
        # top can connect:      2, 3, 4
        # bottom can connect:   2, 5, 6
        
        # move:
            # (0, 1)    - move right (increase x-coordinate by 1)
            # (0, -1)   - move left (decrease x-coordinate by 1)
            # (-1, 0)   - move down (decrease y-coordinate by 1)
            # (1, 0)    - move up (increase y-coordinate by 1)]

        up = {x: set([2, 3, 4]) for x in [2, 5, 6]}
        down = {x: set([2, 5, 6]) for x in [2, 3, 4]}
        left = {x: set([1, 4, 6]) for x in [1, 3, 5]}
        right = {x: set([1, 3, 5]) for x in [1, 4, 6]}

        directions = [(0, 1, right),(0, -1, left),(-1, 0, up),(1, 0, down)]

        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        queue.append((0, 0))

        # using visited as the grid itself
        # after using the value set it to negative
        grid[0][0] = -grid[0][0]

        while queue:
            cr, cc = queue.popleft() # current cell row and column

            if cr == m-1 and cc == n-1: # goal
                return True

            # d is direction
            for dr, dc, direction in directions:
                r = cr + dr
                c = cc + dc

                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] > 0:
                        street = grid[r][c]
                        if -grid[cr][cc] in direction:
                            if grid[r][c] in direction[-grid[cr][cc]]:
                                grid[r][c] = -street
                                queue.append((r, c))
                                
                    
        return False