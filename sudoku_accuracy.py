from sudoku.classes.Evaluator import Evaluator
from sudoku.classes.loader.SudokuLoader import SudokuLoader
from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.loader.SudokuDataset import SudokuDataset

import torch
from torch import cuda
from torch.utils.data import DataLoader

import os

data_path = os.path.join('data', 'test')
xtrain, xtest, ytrain, ytest = SudokuLoader(
    x_path=os.path.join(data_path, 'test_data.parquet'),
    y_path=os.path.join(data_path, 'test_solutions.parquet')
).xy_parquet()

train_data = DataLoader(
    SudokuDataset(
        xtest.to_numpy(),
        ytest.to_numpy()
    ),
    batch_size=3
)

device = ('cuda' if cuda.is_available() else 'cpu')

# load model and saved state
model = ConvNN(
    enc_sizes=[1, *[512 for i in range(15)]]
).to(device)
model.load_state_dict(
    torch.load(os.path.join('data', 'models', 'model_current.pt'))
)

evaluator = Evaluator()
evaluator.validate_accuracy(
    dataloader=train_data, 
    model=model,
    device=device
)
