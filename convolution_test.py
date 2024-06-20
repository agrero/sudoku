import pandas as pd
import os

import torch
from torch import nn
from torch.utils.data import DataLoader

from sklearn.model_selection import train_test_split

from sudoku.classes.ConvNN import ConvNN
from sudoku.classes.SudokuDataset import SudokuDataset


data_path = os.path.join('data', 'puzzles')

data_pandas = pd.concat([
    pd.read_parquet(os.path.join(data_path, 'puzzles_3m.parquet')),
    pd.read_parquet(os.path.join(data_path, 'solutions_3m.parquet'))
    ],
    axis=1,
).astype('int32')
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
    # might help to do this before
    # reshape X to be in the 2d shape of a sudoku puzzle
    # # reshape output to match that of one hot encoded labels
    pred = model(X.view(-1, 9, 9)).view(-1, 81, 10)
    print(pred[0])
    # print(pred.view(-1, 81, 9).shape)
    # print(pred.view(-1, 81, 9)[0])

    break


    # print(batch)
    # print(f'x:{X}')
    # print(f'y:{y}')