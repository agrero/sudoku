

class Board:
    def __init__(self) -> None:
        self.board = []

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
    
    def format_kaggle(self):
        pass

    def set_tile(self, no, x, y):
        self.board[x][y] = no

    def get_solvemask(self):
        return [[1 if j != 0  else 0 for j in i] for i in self.board]

    def pretty_rep(self):
        for i in self.board:
            print(i)

    def flatten_board(self):
        return sum(self.board, [])
    
    def __repr__(self) -> str:
        return f'{self.board}'
    
