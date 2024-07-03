from torch.utils.data import Dataset

from sudoku.classes.labels.LabelEncoder import LabelEncoder

import numpy as np

class SudokuNoisedDataset(Dataset):
    def __init__(self, data, noise_level=60) -> None:
        super().__init__()

        self.data = data
        self.noise_level = noise_level

    def noise_ndxs(self):
        """
        generate random ndxs for each of the 81 sudoku tiles.
        number of noised positions 

        returns np.array of length self.noise_level
        """
        return np.random.choice(np.arange(81), size=self.noise_level)
    
    def noise_labels(self):
        data = np.array(self.data, copy=True)
        data[self.noise_ndxs()] = 0.0

        return data 
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):

        # GET LABELS
        labels = LabelEncoder(
            self.data[index]
        ).encode_labels().astype('float32')
        # NOISE LABELS TO GET DATA
        data = self.noise_labels().astype('float32')

        print(data, labels)

        return data, labels