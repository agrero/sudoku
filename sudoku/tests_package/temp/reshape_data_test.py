import os
import pandas as pd

from sudoku.helper import reshape_2d

# load data
data_path = os.path.join('data', 'puzzles')
solutions_pandas = pd.read_parquet(
    os.path.join(data_path, 'solutions_3m.parquet')
)
data_pandas = pd.read_parquet(
    os.path.join(data_path, 'puzzles_3m.parquet')
)

# reshape data
reshaped_solutions = reshape_2d(solutions_pandas)
reshaped_data = reshape_2d(data_pandas)

# should be (batch, 9, 9)
print(reshaped_data.shape)
print(reshaped_solutions.shape)

# sanity check
print('data')
for i in reshaped_data[0]:
    print(i)

print('solutions')
for i in reshaped_solutions[0]:
    print(i)