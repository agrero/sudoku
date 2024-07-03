import os
import pandas as pd

import torch
from torch import cuda
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torch.optim import Adam

from sudoku.classes.loader.SudokuNoisedDataset import SudokuNoisedDataset
from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.nn.Trainer import Trainer
from sudoku.classes.loader.SudokuLoader import SudokuLoader

from sklearn.model_selection import train_test_split

# IMPORT DATA
data_path = os.path.join('data', 'puzzles')
xtrain, xtest, ytrain, ytest = SudokuLoader(
    x_path=os.path.join(data_path, 'puzzles_3m.parquet'),
    y_path=os.path.join(data_path, 'solutions_3m.parquet')
).xy_parquet()

train_dataloader = DataLoader(
    SudokuNoisedDataset(
        data=ytrain.to_numpy(),
        noise_level=50,
    ),
    batch_size=50
)

device = ('cuda' if cuda.is_available() else 'cpu')

model = ConvNN(
    enc_sizes=[1, *[512 for i in range(15)]]
).to(device)

load=True

if load: 
    model.load_state_dict(
        torch.load(
            os.path.join('data', 'models', 'model_current.pt')
        )
    )

loss_fn = CrossEntropyLoss().to(device)
optimizer = Adam(model.parameters(), lr=1e-2)
trainer = Trainer()

# I do not think the dataloading method is going to work
# my favorite solution
    # add a permute method to each X and Y being loaded.
    # this will just return whatever is inputted normally
    # but we can use inheritance in order to overwrite this method 
    # in some other kind of class! 