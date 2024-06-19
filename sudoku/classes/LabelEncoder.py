from sudoku.helper import generate_dumby_data
from sklearn.preprocessing import OneHotEncoder
import pandas as pd 

class LabelEncoder(OneHotEncoder):
    def __init__(self, labels):
        super().__init__(sparse_output=False)

        self.labels = labels

    def encode_labels(self):
        """encode labels with dumby data in order to maintain shape
        
        returns: one hot encoded labels with the dumby data removed
        """
        return self.fit_transform(
            pd.concat([self.labels, generate_dumby_data()], axis=0)
        )[:-10]