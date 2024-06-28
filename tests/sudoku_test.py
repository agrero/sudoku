from sudoku.classes.Board import Board
from sudoku.classes.Solver import Solver
import numpy as np
import random
import os

import time

import pandas as pd

random.seed(42)

solver = Solver(Board())


test_board = [
    [1,0,0,0,0,3,5,0,6],
    [0,0,0,0,0,0,8,0,7],
    [0,5,0,6,0,0,0,0,0],
    [0,0,6,0,0,7,0,0,8],
    [0,0,8,0,6,0,2,0,0],
    [4,0,0,9,0,0,6,0,0],
    [0,0,0,0,0,4,0,2,0],
    [2,0,4,0,0,0,0,0,0],
    [9,0,7,5,0,0,0,0,3]
]

# solver.board = test_board

filepath = os.path.join('data', 'sudoku-3m.csv')

n_datapoints = 20000

data = pd.read_csv(filepath, 
                   header=0,
                   skiprows=[i for i in range(1, n_datapoints + 1)],
                   nrows=n_datapoints, 
                   index_col=0)
print(data.columns)
data['puzzle'] = data['puzzle'].apply(lambda x:
         [int(i) if i != '.' else 0 for i in x]                            
)

data['puzzle'] = data['puzzle'].apply(
    lambda row: [[row[i] for i in range(j, j+9)] for j in range(0, 81, 9)]        
)
solver = Solver(Board())

# can run this as a try except, if the code breaks it saves wherever its at and writes a log file 

times = [0] * n_datapoints
n_trials = 1 # minimal variance across different trials
for ndx, puzzle in enumerate(data['puzzle'].to_numpy()):
    t0 = time.time()

    solver.board = puzzle
    if solver.solve_sudoku():  

        t1 = time.time()
        print(f'finished puzzle {ndx} in {t1-t0}')
        times[ndx] = t1-t0

# add intermittent saving stuff
pd.DataFrame(times).to_csv(os.path.join('data', f'times_n-{len(times)}.csv'))
# as a reminder the 