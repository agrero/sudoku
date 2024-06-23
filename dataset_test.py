import os
import pandas as pd

from torch import cuda
from torch.utils.data import DataLoader

from sudoku.classes.SudokuDataset import SudokuDataset
from sudoku.classes.LabelEncoder import LabelEncoder

# BEGIN

device = ('cuda' if cuda.is_available() else 'cpu')
print(device)
batch_size = 10

test_data_path = os.path.join('data', 'test')
data = pd.read_parquet(
    os.path.join(test_data_path, 'test_data.parquet')
)
solutions = pd.read_parquet(
    os.path.join(test_data_path, 'test_solutions.parquet')
)

 
# Encoding Labels
# solution_pandas = LabelEncoder(solutions).encode_labels()

# Loading into DataLoader
dataloader = DataLoader(
    SudokuDataset(
        data.to_numpy(), 
        solutions.to_numpy()
        ),
    batch_size = batch_size
)

for batch, (X, y) in enumerate(dataloader):
    X, y = X.to(device), y.to(device),
    print(X.shape)
    # X and y should be (batch, 81)