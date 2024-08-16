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
        # awk
        self.solvemask = self.get_solvemask()

    def is_valid(self, row, col, num):
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
    
    def set_tile(self, no, x, y):
        self.board[x][y] = no

    def get_solvemask(self):
        try:
            return [[1 if j != 0  else 0 for j in i] for i in self.board]
        except:
            print('Unknown Error: Setting solvemask to an empty list!')
            return []
        
    def pretty_rep(self):
        return '\n'.join([''.join(str(i)) for i in self.board])
    
    def flatten_board(self):
        return sum(self.board, [])

    def _read_json(self, path):
        
        f = open(path)
        data = json.load(f)
        f.close()
        return data
    
    def to_str(self):
        """Assumes board is in 2d"""
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
    
