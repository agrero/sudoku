from torch.utils.data import Dataset

class SudokuDataset(Dataset):
    def __init__(self, data, labels) -> None:

        self.data = data
        self.labels = labels
        super().__init__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        label = self.data[index, 81:].astype('int64')
        data = self.data[index, :81].astype('float32')

        return data, label
