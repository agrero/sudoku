import pandas as pd
import os

import torch
from torch import nn
from torch.utils.data import DataLoader

from sudoku.classes.ConvNN import ConvNN
from sudoku.classes.SudokuDataset import SudokuDataset
from sudoku.classes.LabelEncoder import LabelEncoder

from sudoku.helper import reshape_2d

data_path = os.path.join('data', 'puzzles')
data_pandas = pd.read_parquet(
    os.path.join(data_path, 'puzzles_3m.parquet')
)
solution_pandas = pd.read_parquet(
    os.path.join(data_path, 'solutions_3m.parquet')
)

# too big to do alone, in the immediate 
# le = LabelEncoder(solution_pandas)
# solution_pandas = le.encode_labels()
# print(solution_pandas)

data_pandas = reshape_2d(data_pandas)
# solution_pandas = reshape_2d(solution_pandas)

# split data

data_pandas = data_pandas.iloc[0:10 ,:]
batch_size = 1
train_size = int(0.2 * len(data_pandas))

device = ('cuda' if torch.cuda.is_available() else 'cpu')

testing_data = DataLoader(
    SudokuDataset(data_pandas.to_numpy()),
    batch_size=batch_size
)


model = ConvNN().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-1)

model.train()
# need to reshape predictons
for batch, (X, y) in enumerate(testing_data):
    X, y = X.to(device), y.to(device)
    optimizer.zero_grad()

    pred = model(X.view(-1, 9, 9)).view(-1, 81, 10)
    
    loss = loss_fn(
        pred,
    )

    break
