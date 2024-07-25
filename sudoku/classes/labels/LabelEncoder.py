from sudoku.helper.helper import generate_dumby_data # I think is useless now
from sklearn.preprocessing import OneHotEncoder
import numpy as np

class LabelEncoder(OneHotEncoder):
    def __init__(self, labels):
        super().__init__(sparse_output=False)

        self.labels = labels

    def encode_labels(self) -> np.array:
        """same above but for numpy instead of pandas"""
        return self.fit_transform(X=self.labels.reshape(-1,1))