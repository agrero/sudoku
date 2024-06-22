from torch.utils.data import Dataset

class SudokuDataset(Dataset):
    def __init__(self, data, labels) -> None:

        self.data = data
        self.labels = labels
        super().__init__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        # may want to encode the labels right here
        # inheriting the label encoder and just doing the transform
        # # Be warned as the label encoder is usually for dataframes
        # # but here we are moreso worried about 
        label = self.data[index].astype('int32')
        data = self.data[index].astype('float32')

        return data, label
