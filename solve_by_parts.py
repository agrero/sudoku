from sudoku.classes.ConvNN import ConvNN
from sudoku.classes.SudokuLoader import SudokuLoader
from sudoku.classes.SudokuDataset import SudokuDataset
from sudoku.classes.Evaluator import Evaluator
from sudoku.classes.MlSolver import MlSolver

import torch
from torch import cuda
from torch.utils.data import DataLoader

import os

# LOAD IN DATA

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
    batch_size=1
)

device = ('cuda' if cuda.is_available() else 'cpu')

model = ConvNN(
    enc_sizes=[1, *[512 for i in range(15)]]
).to(device)
model.load_state_dict(
    torch.load(os.path.join('data','models','model_current.pt'))
)

# baseline 54% accuracy
# this is cheating ! 
ev = Evaluator()
model.eval()

buffer = 5

solver = MlSolver(device='cuda')
solver.solve_by_parts(model, train_data)
print(sum(solver.accuracies) / len(solver.accuracies))

