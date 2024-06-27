import os
import pandas as pd
from statistics import mean 

from torch import cuda
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torch.optim import Adam

from sudoku.classes.SudokuDataset import SudokuDataset
from sudoku.classes.ConvNN import ConvNN
from sudoku.nn_helper import train

from sklearn.model_selection import train_test_split

import time 


# IMPORT DATA
data_path = os.path.join('data', 'puzzles')
data = pd.read_parquet(
    os.path.join(data_path, 'puzzles_3m.parquet')
)
solutions = pd.read_parquet(
    os.path.join(data_path, 'solutions_3m.parquet')
)

train_size = train_size = int(0.07 * len(data))

# SPLIT DATA
train_data, _ = train_test_split(
    data,
    test_size=len(data) - train_size,
    train_size=train_size
)

train_labels = solutions.iloc[train_data.index, :]

batch_sizes = [1_000, 10_000, 100_000]

avg_times = []
for batch in batch_sizes:
    times = []
    for i in range(5):
        t0 = time.time()
        dataloader = DataLoader(
            SudokuDataset(
                train_data.to_numpy(),
                train_labels.to_numpy()
            ),
            batch_size=batch
        )

        # MODEL INSTANTIATION
        device = ('cuda' if cuda.is_available() else 'cpu')

        model = ConvNN(enc_sizes=[1, *[10 for i in range(14)]]).to(device)
        loss_fn = CrossEntropyLoss().to(device)
        optimizer = Adam(model.parameters(), lr=1e-2)

        train(
            dataloader=dataloader,
            model=model,
            loss_fn=loss_fn,
            optimizer=optimizer,
            device=device
        )
        t1 = time.time()

        times.append(t1-t0)
    avg_times.append(mean(times))
print(f'Average Times: {avg_times}')