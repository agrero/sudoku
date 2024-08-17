import json
from sudoku.helper.helper import to_matrix


class Board:
    """I'm going to make a design choice here and say
    that the board attribute should be 2d and manipulations
    should be returned"""
    def __init__(
            self, board=[[0 for i in range(9)] for j in range(9)]
            ) -> None:
        self.board = board

    def is_valid(self, row, col, num) -> bool:
        """
        checks the validity of the current sudoku board
        
        returns: boolean
        """
        # Check the row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check the column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True
    
    def set_tile(self, no:int, x:int, y:int) -> None:
        """set tile for self.board
        no: number to set tile to
        x: row
        y: column"""
        self.board[x][y] = no

    def get_solvemask(self) -> list:
        """
        converts self.board to binary
        any non-zero tile converted to zero
        returns: 2d sudoku board as a list of lists
        """
        try:
            return [[1 if j != 0  else 0 for j in i] 
                    for i in self.board]
        except:
            print('Unknown Error: Setting solvemask to an empty list!')
            return []
        
    def pretty_rep(self) -> str:
        """
        Converts self.board to a formatted string 
        for better readability
        """
        return '\n'.join([''.join(str(i)) for i in self.board])
    
    def flatten_board(self) -> list:
        """
        flattens self.board into a singular list of 81 items
        
        returns: 1d list of length 81
        """
        return sum(self.board, [])

    def _read_json(self, path):
        """DEPRECATED
        reads in json data and returns it
        """
        f = open(path)
        data = json.load(f)
        f.close()
        return data
    
    def to_str(self):
        """ I'm honestly lost to the usefullness of this
        i have a vague recollection of adding it
        
        Converts board to a string"""
        bad = [',','[',']']
        return ''.join(
            [i for i in self.flatten_board(self.board)
            if i not in bad]
            )
    
    def from_str(self, string:str):
        self.board = to_matrix(
            [int(i) for i in string], n=9
        )

    def __repr__(self) -> str:
        return f'{self.board}'
    
