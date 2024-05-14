from sudoku.Board import Board

class Solver(Board):

    def __init__(self, Board) -> None:
        super().__init__()
            

    def solve_sudoku(self):
        """Solve the Sudoku puzzle using backtracking."""
        # returns false after iterating through each piece
        # this restarts the 
        for row in range(9):
            for col in range(9): # returns false after iterating through each piece
                # this 
                
                if self.board[row][col] == 0:  # Find empty cell
                    
                    # checks every single number for the cell
                    for num in range(1, 10):  # Try all possible numbers

                        if self.is_valid(row, col, num): # if the move is valid

                            self.board[row][col] = num # change piece

                            if self.solve_sudoku(): # if this solves the sudoku exit
                                return True # 
                            
                            self.board[row][col] = 0  # Reset on backtrack

                    return False  # Trigger backtrack
        return True

# iteration # 2

"""
#1) Make batch_size plays

#2) Check Tiles for Correctness
- Make sure to filter out original
- remove conflicting tiles

- to check tiles for correctness, 
    iterate over all non 0 

#3) make batch_size plays
"""



# here's how we're going to check

# define batch size

# for the length of the batch size
# # randomly select an index and make a random play from the acceptalbe plays

# check for viability
# # if its not viable undo the last step and check again - > recursion
# # else continue

# !!!!!! There needs to be some way to restart after n epochs !!!!!!!!!!!!
# # This could be easily done by just applying the inner dot product

# This could also be done by making a function to retrieve innacurate indices (making sure to ignore safe ones) 