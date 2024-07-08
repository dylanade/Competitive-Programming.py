class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        m = len(board)
        n = len(board[0])

        q = deque()
        q.append(click)

        visited = set()
        visited.add(tuple(click))
        
        distances = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                count_mine = 0
                for dx, dy in distances:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 'M':
                            count_mine += 1

                if count_mine <= 0:
                    board[x][y] = 'B'
                    for dx, dy in distances:
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < m and 0 <= ny < n:
                            if (nx, ny) not in visited:
                                q.append([nx, ny])
                                visited.add((nx, ny))
                else:
                    board[x][y] = str(count_mine)

        return board