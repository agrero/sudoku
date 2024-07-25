import json

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
    
    def to_dict(self):
        return {ndx:i for (ndx, i) in enumerate(self.flatten_board())}
    
    def from_dict(self, dictionary:dict):
        sudoku = [[0 for i in range(9)] for j in range(9)]
        count = 0
        for key, value in dictionary.items():
            sudoku[int(key) // 9][count] = value
            count += 1
            if count == 9:
                count = 0
        return sudoku
    
    def read_json(self, path):
        
        f = open(path)
        data = json.load(f)
        f.close()
        return data

    
    
    def __repr__(self) -> str:
        return f'{self.board}'
    
