from sudoku.helper import generate_dumby_data
from sklearn.preprocessing import OneHotEncoder
import pandas as pd 
import numpy as np

class LabelEncoder(OneHotEncoder):
    def __init__(self, labels):
        super().__init__(sparse_output=False)

        self.labels = labels

    def encode_labels(self) -> np.array:
        """encode labels with dumby data in order to maintain shape
        returns: one hot encoded labels with the dumby data removed
        """
        return self.fit_transform(
            pd.concat([self.labels, generate_dumby_data()], axis=0)
        )[:-10].reshape(len(self.labels), 81, 10)
    
    def encode_numpy_labels(self) -> np.array:
        """same above but for numpy instead of pandas"""
        return self.fit_transform(X=self.labels.reshape(-1,1))