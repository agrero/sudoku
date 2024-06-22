import pandas as pd
import os
import numpy as np

from sudoku.helper import conv_framelist

breakup = True
n_datapoints = 3_000_000
batch_size= 100_000

if breakup:

    # for i in range(0, n_datapoints, batch_size):
        # print(i)
    # 
    data_sudoku = pd.read_csv(os.path.join('data', 'sudoku-3m.csv'), 
                            nrows = n_datapoints,
                            usecols=[0,2], 
                            index_col=0)


    puzzles = conv_framelist(data_sudoku, conv=True, batch_size=batch_size)
    
puzzle_dir = os.path.join('data', 'puzzles')

data = pd.read_parquet(
    os.path.join(
        puzzle_dir,
        os.listdir(puzzle_dir)[0]
    )
)

for i in sorted(os.listdir(puzzle_dir))[1:]:
    df = pd.read_parquet(
        os.path.join(
            puzzle_dir,
            i
        )
    )
    data = pd.concat([data, df], ignore_index=True)

if data.shape[0] == n_datapoints:
    for i in os.listdir(puzzle_dir):
        os.remove(
            os.path.join(puzzle_dir, i)
        )

data.to_parquet(os.path.join(puzzle_dir, 'solutions_3m.parquet'))
