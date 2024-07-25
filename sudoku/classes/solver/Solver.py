from sudoku.classes.game.Board import Board

class Solver(Board):

    def __init__(self, Board) -> None:
        super().__init__()
            

    def solve_sudoku(self, board):
        """Solve the Sudoku puzzle using backtracking."""
        # returns false after iterating through each piece
        # this restarts the 
        self.board = board
        for row in range(9):
            for col in range(9): # returns false after iterating through each piece
                # this 
                
                if board[row][col] == 0:  # Find empty cell
                    
                    # checks every single number for the cell
                    for num in range(1, 10):  # Try all possible numbers

                        if self.is_valid(row, col, num): # if the move is valid

                            board[row][col] = num # change piece

                            if self.solve_sudoku(self.board): # if this solves the sudoku exit
                                return True # 
                            
                            board[row][col] = 0  # Reset on backtrack

                    return False  # Trigger backtrack
        return True