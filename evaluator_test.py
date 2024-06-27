from sudoku.classes.Evaluator import Evaluator 
from sudoku.classes.SudokuLoader import SudokuLoader
from sudoku.classes.ConvNN import ConvNN
from sudoku.classes.SudokuDataset import SudokuDataset

import torch
from torch import cuda
from torch.utils.data import DataLoader

import seaborn as sns
import matplotlib.pyplot as plt

import os

data_path = os.path.join('data', 'puzzles')
xtrain, xtest, ytrain, ytest = SudokuLoader(
    x_path=os.path.join(data_path, 'puzzles_3m.parquet'),
    y_path=os.path.join(data_path, 'solutions_3m.parquet')
).xy_parquet()

train_data = DataLoader(
    SudokuDataset(
        xtrain.to_numpy(),
        ytrain.to_numpy()
    ),
    batch_size=500
)

device = ('cuda' if cuda.is_available() else 'cpu')

# load model and saved state
model = ConvNN(
    enc_sizes=[1, *[512 for i in range(15)]]
).to(device)
model.load_state_dict(
    torch.load(os.path.join('data', 'models', 'model_current.pt'))
)

# evaluate model's class
evaluation = Evaluator().confusion_matrix(train_data, model)

sns.heatmap(
    evaluation,
    # fmt='d',
    cmap=sns.color_palette('rocket', as_cmap=True),
    xticklabels=[i for i in range(1, 10)],
    yticklabels=[i for i in range(1, 10)]
)
plt.ylabel('Prediction')
plt.xlabel('Actual')
plt.title('Classification Accuracy')
plt.show()