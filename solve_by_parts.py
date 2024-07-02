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

buffer = 5

for batch, (X, y) in enumerate(train_data):
    print(f'iteration {batch}')
    X, y = X.to(device), torch.argmax(y, dim=2).to(device)
    check_sum = torch.zeros(2).to(device)
    print(check_sum)
    guessing = True
    while guessing:
        print(f'iteration: {check_sum[1]}')
        check = torch.eq(X, y+1)

        X[~check] = torch.argmax(
            model(X),
            dim=2
        )[~check].to(dtype=torch.float32)
        check_sum[0] += check.sum()
        check_sum[1] += 1.0
        print(check_sum[0] / check_sum[1])
        print((check.sum() - 1))
        if ((check_sum[0] / check_sum[1]) > (check.sum() - 1.)) & (check_sum[1] > buffer):
            print('shall not pass')
            guessing=False
            

    print(y+1.)
        
    break


