from torch.utils.data import Dataset
from sudoku.classes.labels.LabelEncoder import LabelEncoder

class SudokuDataset(Dataset):
    def __init__(self, data, labels) -> None:
        super().__init__()

        self.data = data
        self.labels = labels


    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):

        label = self.labels[index]
        label = LabelEncoder(label).encode_labels().astype('float32')

        data = self.data[index].astype('float32')
        
        return data, label
