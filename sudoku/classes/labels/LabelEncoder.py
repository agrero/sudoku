from sklearn.preprocessing import OneHotEncoder
import numpy as np

class LabelEncoder(OneHotEncoder):
    def __init__(self, labels:np.array):
        super().__init__(sparse_output=False)

        self.labels = labels

    def encode_labels(self) -> np.array:
        """encodes labels using sklearns OneHotEncoder
        
        returns: numpy array of one hot encoded labels
        """
        return self.fit_transform(X=self.labels.reshape(-1,1))