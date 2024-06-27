from pandas import read_parquet

from sklearn.model_selection import train_test_split

class SudokuLoader():
    def __init__(self, data_path='', x_path='', y_path='') -> None:
        self.data_path = data_path
        self.x_path = x_path
        self.y_path = y_path

    def load_xy_parquet(self, train_ratio:float=0.1):
        """
        Load data and labels as parquet files.
        Split data using sklearn's train_test_split.

        train_ratio:float = ratio of total data to 
        use for training set

        returns np.array's of x and y train and test respectively
        """
        X, y = read_parquet(self.x_path), read_parquet(self.y_path)
        train_size = int(train_ratio * len(X))

        xtrain, xtest = train_test_split(
            X, 
            test_size = len(X) - train_size,
            train_size=train_size
        )

        ytrain, ytest = y.iloc[xtrain.index,:], y.iloc[xtest.index,:]

        return xtrain, xtest, ytrain, ytest 