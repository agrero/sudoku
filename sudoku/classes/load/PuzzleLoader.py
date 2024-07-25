import pandas as pd

from sudoku.helper.helper import conv_framelist

class PuzzleLoader:
    def __init__(self, puzzle_path='') -> None:
        self.data = None

    def load_kaggle(self, path_to_kaggle, batch_size=100_000):
        """path_to_kaggle: path to kaggle 3m sudoku dataset"""

        df = pd.read_csv(path_to_kaggle,
                         usecols=[0,1],
                         index_col=0)
        
        conv_framelist(df, conv=True, batch_size=batch_size)

    def load_parquet(self):
        self.data = pd.read_parquet(self.puzzle_path)

    def load_csv(self):
        self.data = pd.read_csv(self.puzzle_path)