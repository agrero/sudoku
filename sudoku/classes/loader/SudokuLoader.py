from pandas import read_parquet

from sklearn.model_selection import train_test_split

class SudokuLoader():
    """A class for loading SudokuDatasets for a variety of filetypes"""
    def __init__(self, data_path='', x_path='', y_path='') -> None:
        self.data_path = data_path
        self.x_path = x_path
        self.y_path = y_path

    def split(self, X, y, train_size):
        """
        Method wrapper for sklearn's train_test_split
        specifically tailored for SudokuLoader class
        """
        xtest, xtrain, ytest, ytrain = train_test_split(
            X, y,
            test_size = len(X) - train_size,
            train_size=train_size
        )
        return xtrain, xtest, ytrain, ytest
    
    def xy_parquet(self, train_size=10000, skip_to=0, split:bool=True):
        """
        Load data and labels as parquet files.
        Split data using sklearn's train_test_split.

        train_size:int = number of sudoku puzzles in the training set 
        skip_to:int = number of puzzles to skip
        split:bool = whether or not to split the data

        if split:
            returns train/test (X,y) split data as a pandas dataframe
        else:
            returns (X,y) data as a pandas dataframe
        """

        X = read_parquet(self.x_path).iloc[skip_to:,:]
        y = read_parquet(self.y_path).iloc[skip_to:,:]

        if split: return self.split(X,y,train_size)
        else: return X, y
        