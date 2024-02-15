class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        
        #checking if the rows and columns have digit duplicates, done concurrently
        for i in range(len(board)):
            set_row = set() #keep track of elements in the rows
            set_col = set() #keep track of elements in the cols
            
            for j in range(len(board[i])): 
                #checking if the rows contain unique digits
                if (board[i][j] != "."):
                    if (board[i][j] not in set_row):
                        set_row.add(board[i][j])
                    else:
                        return False
                
                #checking if the columns contain unique digits
                if (board[j][i] != "."):
                    if (board[j][i] not in set_col):
                        set_col.add(board[j][i])
                    else:
                        return False
                    
        #checking each 3x3 square has unique digits
        
        #THIS PART: seperates the squares into a list
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = []
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        square += [board[m][n]]
                   
                #THIS PART: checks if the square contains duplicates
                set_square = set()
                for digit in square:
                    if (digit != "."):
                        if digit not in set_square:
                            set_square.add(digit)
                        else:
                            return False

        #no duplicate digits in each row, column, or 3x3 square, this is a Valid Sudoku     
        return True