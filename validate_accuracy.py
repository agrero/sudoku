from sudoku.classes.Evaluator import Evaluator
from sudoku.classes.load.SudokuLoader import SudokuLoader
from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.load.SudokuDataset import SudokuDataset

import torch
from torch import cuda
from torch.utils.data import DataLoader

import os

# part of config
data_path = os.path.join('data', 'puzzles')
model_path = os.path.join('data', 'models', 'model_current.pt')

# ooooo config could auto read these in
xtrain, xtest, ytrain, ytest = SudokuLoader(
    x_path=os.path.join(data_path, 'puzzles_3m.parquet'),
    y_path=os.path.join(data_path, 'solutions_3m.parquet')
).xy_parquet(split=True, exclude_to=2_000_000)

train_data = DataLoader(
    SudokuDataset(
        xtest.to_numpy(),
        ytest.to_numpy()
    ),
    batch_size=500
)

device = ('cuda' if cuda.is_available() else 'cpu')

# load model and saved state
model = ConvNN(
    enc_sizes=[1, *[512 for i in range(15)]]
).to(device)
model.load_state_dict(
    torch.load(model_path)
)

evaluator = Evaluator()
evaluator.validate_accuracy(
    dataloader=train_data, 
    model=model,
    device=device
)
