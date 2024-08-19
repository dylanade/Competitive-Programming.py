class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        def boxID(i, j):
            return i // 3 * 3 + j // 3

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)

                    box_id = boxID(i, j)  # range = [0, 8]
                    boxes[box_id].add(num)
                
        def bt(i, j):
            nonlocal solved
            if i == 9:
                solved = True 
                return 

            ni = i + (j + 1) // 9
            nj = (j + 1) % 9

            if board[i][j] != ".":
                bt(ni, nj)
            else:
                for num in range(1, 10):
                    box_id = boxID(i, j)
                    if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[box_id].add(num)
                        board[i][j] = str(num)

                        bt(ni, nj)

                        if not solved:
                            rows[i].discard(num)
                            cols[j].discard(num)
                            boxes[box_id].discard(num)
                            board[i][j] = '.'

        solved = False
        bt(0, 0)