import pandas as pd

from sudoku.helper.helper import conv_framelist

class PuzzleLoader:
    def __init__(self, puzzle_path='') -> None:
        self.puzzle_path = puzzle_path
        self.data = None

    def load_kaggle(self, path_to_kaggle, batch_size=100_000):
        """
        load the 3m sudoku dataset as found on Kaggle
        
        path_to_kaggle: path to kaggle csv dataset
        batch_size: size of chunks to be individually loaded in.
            mostly just helps with memory cost
        """

        df = pd.read_csv(path_to_kaggle,
                         usecols=[0,1],
                         index_col=0)
        
        conv_framelist(df, conv=True, batch_size=batch_size)

    def load_parquet(self):
        """reads parquet file as indicated by the puzzlepath attribute.
        assigns value to data attribute"""
        self.data = pd.read_parquet(self.puzzle_path)

    def load_csv(self):
        """reads csv as indicated by the puzzlepath attribute.
        assigns value to data attribute"""
        self.data = pd.read_csv(self.puzzle_path)