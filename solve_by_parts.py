from sudoku.classes.ConvNN import ConvNN
from sudoku.classes.SudokuLoader import SudokuLoader
from sudoku.classes.SudokuDataset import SudokuDataset
from sudoku.classes.Evaluator import Evaluator

import torch
from torch import cuda
from torch.utils.data import DataLoader

import os

# LOAD IN DATA

data_path = os.path.join('data', 'puzzles')
xtrain, xtest, ytrain, ytest = SudokuLoader(
    x_path=os.path.join(data_path, 'puzzles_3m.parquet'),
    y_path=os.path.join(data_path, 'solutions_3m.parquet')
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

for batch, (X, y) in enumerate(train_data):
    print(batch)
    X, y = X.to(device), torch.argmax(y, dim=2).to(device)
    for i in range(10):
        print(f'iteration {batch}')
        # get all incorrect values and set equal to 0
        check = torch.eq(X, y)
        for i in X.data.view(9,9):
            print(i)
        X[~check] = 0 
        print('\nx post')
        for i in X.data.view(9,9):
            print(i)
        
        print('\ny')
        for i in y.data.view(9,9):
            print(i)
        # print(check)
        # print(check.sum(1))
        X = torch.argmax(
            model(X), 
            dim=2
        ).to(torch.float32)
        break
    break


