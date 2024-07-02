import os
import pandas as pd

import torch
from torch import cuda
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torch.optim import Adam

from sudoku.classes.loader.SudokuDataset import SudokuDataset
from sudoku.classes.nn.ConvNN import ConvNN

# BEGIN

device = ('cuda' if cuda.is_available() else 'cpu')

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

model = ConvNN().to(device)

loss_fn = CrossEntropyLoss().to(device)
optimizer = Adam(model.parameters(), lr=100)

for batch, (X, y) in enumerate(dataloader):
    X, y = X.to(device), y.to(device)
    pred = model(X)
    loss = loss_fn(pred, y)

    print(loss)