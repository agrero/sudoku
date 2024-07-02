import os
import pandas as pd

import torch
from torch import cuda
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torch.optim import Adam

from sudoku.classes.loader.SudokuDataset import SudokuDataset
from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.nn_helper import train

from sklearn.model_selection import train_test_split


# IMPORT DATA
data_path = os.path.join('data', 'puzzles')
data = pd.read_parquet(
    os.path.join(data_path, 'puzzles_3m.parquet')
)
solutions = pd.read_parquet(
    os.path.join(data_path, 'solutions_3m.parquet')
)

train_size = train_size = int(0.05 * len(data))

# SPLIT DATA
train_data, _ = train_test_split(
    data,
    test_size=len(data) - train_size,
    train_size=train_size
)

train_labels = solutions.iloc[train_data.index, :]

dataloader = DataLoader(
    SudokuDataset(
        train_data.to_numpy(),
        train_labels.to_numpy()
    ),
    batch_size=500
)

# MODEL INSTANTIATION
device = ('cuda' if cuda.is_available() else 'cpu')

load = True

model = ConvNN(
    enc_sizes=[1, *[512 for i in range(15)]]
).to(device)
if load: 
    model.load_state_dict(
        torch.load(
            os.path.join('data', 'models', 'model_current.pt')
        )
    )

loss_fn = CrossEntropyLoss().to(device)
optimizer = Adam(model.parameters(), lr=1e-2)

epochs = 5
for t in range(epochs):
    print(f'Epoch {t+1}\n-----------')
    train(
        dataloader=dataloader,
        model=model,
        loss_fn=loss_fn,
        optimizer=optimizer,
        device=device
    )
    
model_path = os.path.join('data', 'models', 'model_current.pt')

torch.save(
    model.state_dict(), 
    model_path
)

# a logger for training runs might be nice